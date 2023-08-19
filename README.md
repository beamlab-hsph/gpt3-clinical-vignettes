# The Diagnostic and Triage Accuracy of the GPT-3 Artificial Intelligence Model

This repository contains the code and datasets used in our paper titled "The Diagnostic and Triage Accuracy of the GPT-3 Artificial Intelligence Model", available at https://www.medrxiv.org/content/10.1101/2023.01.30.23285067v1

# Table of Contents
- [Abstract](#abstract)
- [Setup](#setup)
- [Data](#data)
- [Notebooks](#notebooks)
- [License](#license)
- [Citation](#citation)

## Abstract

**Importance** Artificial intelligence (AI) applications in health care have been effective in many areas of medicine, but they are often trained for a single task using labeled data, making deployment and generalizability challenging. Whether a general-purpose AI language model can perform diagnosis and triage is unknown.

**Objective** Compare the general-purpose Generative Pre-trained Transformer 3 (GPT-3) AI model’s diagnostic and triage performance to attending physicians and lay adults who use the Internet.

**Design** We compared the accuracy of GPT-3’s diagnostic and triage ability for 48 validated case vignettes of both common (e.g., viral illness) and severe (e.g., heart attack) conditions to lay people and practicing physicians. Finally, we examined how well calibrated GPT-3’s confidence was for diagnosis and triage.

**Setting and Participants** The GPT-3 model, a nationally representative sample of lay people, and practicing physicians.

**Exposure** Validated case vignettes (<60 words; <6th grade reading level).

**Main Outcomes and Measures** Correct diagnosis, correct triage.

**Results** Among all cases, GPT-3 replied with the correct diagnosis in its top 3 for 88% (95% CI, 75% to 94%) of cases, compared to 54% (95% CI, 53% to 55%) for lay individuals (p<0.001) and 96% (95% CI, 94% to 97%) for physicians (p=0.0354). GPT-3 triaged (71% correct; 95% CI, 57% to 82%) similarly to lay individuals (74%; 95% CI, 73% to 75%; p=0.73); both were significantly worse than physicians (91%; 95% CI, 89% to 93%; p<0.001). As measured by the Brier score, GPT-3 confidence in its top prediction was reasonably well-calibrated for diagnosis (Brier score = 0.18) and triage (Brier score = 0.22).

**Conclusions and Relevance** A general-purpose AI language model without any content-specific training could perform diagnosis at levels close to, but below physicians and better than lay individuals. The model was performed less well on triage, where its performance was closer to that of lay individuals.

## Setup
At present, the `environment.yml` isn't available. We apologize for the inconvenience.

## Data
The `data` directory is split into `processed` and `raw` subdirectories.
- `raw/vignettes-2015.txt` and `raw/vignettes-2020.txt` contain the raw case vignettes used in the experiment. The code to process and read these is in `notebooks/utils.py`.
- `processed/vignettes{15|20}_{diagnosis|triage}_predictions*.csv` contain the predictions made on the vignettes by GPT-3.

## Notebooks
The `notebooks` directory contains the following notebooks:
- `triage-prediction.ipynb` - Notebook used to obtain the triage predictions from GPT-3.
- `diagnosis-prediction.ipynb` - Notebook used to obtain the diagnosis predictions from GPT-3.
- `final-figutes-tables.ipynb` - Code to generate the figures and tables used in the paper.
- `final-figures-tables-2015.ipynb` - Same as `final-figures-tables.ipynb` but for the vignettes from the 2015 study.
- `ethnicity-gender-bias-triage-prediction.ipynb` - Contains code used to obtain predictions from GPT-3 for bias assessment.
- `bias-assessment.ipynb` - Analyzes differential performance of GPT-3 across gender, demographic groups (unpublished analysis).

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Citation
If you use this code or data, please cite our paper:
```
The Diagnostic and Triage Accuracy of the GPT-3 Artificial Intelligence Model
David M Levine, Rudraksh Tuwani, Benjamin Kompa, Amita Varma, Samuel G. Finlayson, Ateev Mehrotra, Andrew Beam
medRxiv 2023.01.30.23285067; doi: https://doi.org/10.1101/2023.01.30.23285067
``````