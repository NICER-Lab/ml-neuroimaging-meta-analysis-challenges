# Using, misusing, and improving online machine learning-based meta-analysis of neuroimaging published data: A perspective on NeuroQuery
This repository contains code for replicating analysis related to the use of the NeuroQuery meta-analysis tool

---
AI based meta analysis and literature review of large numbers of papers can help support research and manual review. While recent natural language models such as ChatGPT4 are extremely powerful at processing documents, their complexity also hurts the transparency of how their responses are generated. 

The need for this transparency is demonstrated by Neuroquery, which uses older more explainable methods for identifying regions of potential activity in the brain based on user-defined text queries (e.g. "Distance + Color"). Neuroquery results are often dominated by terms that have strong activations, such as those relating to the visual cortex, even if the user did not intend those associations to be present (Neuroquery associations are based on words that often appear together; something Large Language Models are also susceptible too).

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for src
│                         and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src                <- Source code for use in this project.
    │
    ├── __init__.py    <- Makes src a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        └── visualize.py
```

## Running code 

### Installing requirements
```
make requirements
```
or 
```
pip install -r requirements.txt
```

### Downloading data
Data used by neuroquery and they're published models is found here https://github.com/neuroquery/neuroquery_data

```
git clone https://github.com/neuroquery/neuroquery_data data/neuroquery_data
```
- At the time of writing this, the most recent commit is "4580f86" 

--------

<small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">Cookiecutter Data Science project template</a>. #cookiecutterdatascience</small>
