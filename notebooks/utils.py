from typing import Dict, Tuple

import openai
import pandas as pd
from pathlib import Path


def add_full_stop(sentence: str) -> str:
    if sentence.endswith('.'):
        return sentence
    else:
        return sentence + '.'


def parse_vignettes_2015(filepath: Path) -> pd.DataFrame:
    """Parse the clinical vignettes from (2015)."""
    
    vignettes = []
    with open(filepath, 'r') as f:
        lines = f.read().split('\n\n')
        for i in range(0, len(lines), 3):
            vignettes.append({
                'Correct Diagnosis': lines[i],
                'Problem': lines[i+1].replace('\n', ' ').strip(),
                'Simplified': lines[i+2].replace('\n', ' ').strip(),
            })

    vignettes = pd.DataFrame(vignettes)
    
    # Add full stop at the end of sentences       
    vignettes['Problem'] = vignettes['Problem'].map(add_full_stop)
    
    # Add triage info (present in supplement)
    vignettes['Correct Triage'] = ['Emergent']*15 + ['Non-emergent']*15 + ['Self-care']*15

    return vignettes


def parse_vignettes_2020(filepath: Path) -> pd.DataFrame:
    """Parse the clinical vignettes from (2020)."""
    
    vignettes = pd.read_csv(filepath, sep='\t', index_col='Case #')
    
    # Remove double quotes since this throws off GPT-3.
    vignettes['Additional Details'] = vignettes['Additional Details'].str.replace('"', '')
    
    # Make column names consistent with the other vignettes
    vignettes.columns = ['Correct Diagnosis', 'Correct Triage', 'Problem', 'Additional Details']
    
    # Add full stop at the end of sentences       
    vignettes['Problem'] = vignettes['Problem'].map(add_full_stop)
    vignettes['Additional Details'] = vignettes['Additional Details'].map(add_full_stop)
    
    # Insert hyphens in triage categories.
    vignettes.loc[vignettes['Correct Triage'] == '1 week', 'Correct Triage'] = '1-week'
    vignettes.loc[vignettes['Correct Triage'] == '1 day', 'Correct Triage'] = '1-day'
    
    return vignettes


def get_completion_prob(prompt: str, gpt3_params: Dict) -> Tuple[str, float]:
    
    response = openai.Completion.create(
        prompt=prompt,
        **gpt3_params
    )
    
    # Get the top completion
    res = response.choices[0]
    
    if res["finish_reason"] == 'length':
        raise Exception("Completetion terminated prematurely. Consider increasing max_tokens.")
                
    tokens = res['logprobs']['tokens']
    
    # Calculate probability of completion
    # Get index of stop token
    last_idx = -1
    for stopkw in gpt3_params['stop']:
        try:
            last_idx = tokens.index(stopkw)
            break
        except ValueError:
            continue
            
    if last_idx == -1:
        raise ValueError("STOP token not present in token list.")
            
    # Subset
    tokens = tokens[:last_idx]
    logprobs = res['logprobs']['token_logprobs'][:last_idx]
    
    assert len(logprobs) == len(tokens), "Length of logprobs and tokens don't match"
    
    completion = ''.join(tokens[:last_idx]).strip()
    prob_completion = sum(logprobs)
    
    return completion, prob_completion

 
