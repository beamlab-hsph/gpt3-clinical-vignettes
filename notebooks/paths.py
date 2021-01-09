from pathlib import Path

# Open AI API Key
OPENAI_API_KEY_PATH = Path('/home/rt156/.secrets/openai.json')

# Configuration file
TRIAGE_CONFIG_FILE = Path('triage_prediction_config.json')

# Folders
DATA = Path('../data/')
RAW = DATA/'raw'
PROCESSED = DATA/'processed'
 
# Vignettes
VIGNETTES_2015_FP = RAW/'vignettes-2015.txt'
VIGNETTES_2020_FP = RAW/'vignettes-2020.tsv'