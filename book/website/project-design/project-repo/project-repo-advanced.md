# Advanced Structure for Data Analysis

## Prerequisites/Recommended Skill Level

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| {ref}`Version Control<rr-vcs>` | Helpful | Knowledge of using git for version control |
| {ref}`Open Research<rr-open>` | Helpful | Components are part of the compendium |
| {ref}`Reproducible Environments<rr-renv>` | Helpful | Can be used to make the compendium reproducible |

## Summary 

When planning out a research study, one crucial and often forgotten component is setting up a repository. 
In this section, the benefits and considerations of designing a repository will be outlined, along with an example structure and further resources to guide your workflow.

The prerequisites for this chapter can vary depending on the organisational needs of a project. Creating a repository with a simple research project layout can require minimal technical knowledge (such as managing only input data and output results). Meanwhile, advanced repository layouts can be required for more complicated projects (such as projects with dependencies on other projects).

## Background

A repository (or a "repo") is a storage location for your research project. A repository can contain a range of digital objects and can be used to store your project by using online platforms such as GitHub. The aim of a repository is to organise your project in such a way this is both accessible to others and efficient to use. 

In this section, the benefits and considerations of designing a repository will be outlined, along with an example structure and further resources to guide your workflow.

```{note}
**Creating an infrastructure for ethical, open and high-quality research from the get-go**
- Transparent, open, reproducible
- Version control - no more analysis_script_final_v2_FINAL.R 
- Easy to navigate - a time saver for everyone involved!
- Communication - a means of sharing your work 
- Others can build on your work! 
```

## Main considerations

- Include a {ref}`README file<pd-project-repo-readme>`, detailing _what_ the repository is for and _how_ to navigate it 
- Always consider designing your project for collaboration by adding key documents describing project goals, vision, roadmap, contribution and communication process (as described in earlier subchapters in {ref}`pd-project-repo`)
- General structure should separate input (data), methods (scripts) and output (results, figures, manuscript)
- Specify what shouldn't be tracked in the .gitignore file, such as data
- Include information on your computational environment {ref}`Reproducible Environments<rr-renv>` to ensure reproducibility (this can also be specified in the README)

## Example Repository Structure 

### Simple research project example

```
Project Folder/
├── docs                     <- documentation
│   └── codelist.txt 
├── data
│   └── raw/
│       └── my_data.csv
│   └── clean/
│       └── data_clean.csv
├── analysis                 <- scripts
│   └── my_script.R
├── results                  <- analysis output     
│   └── figures
├── .gitignore               <- files excluded from git version control 
├── CODE_OF_CONDUCT          <- Code of Conduct for community projects
├── CONTRIBUTING             <- Contribution guideline for collaborators
├── LICENSE                  <- software license
├── install.R                <- environment setup
├── README.md                <- information about the repo
└── report.md                <- report of project
```

### Every Possible Folder Example

Example more for if the project is building an application or is related to software engineering.

```
Project Folder/                        

├── analysis                 <- scripts
│   └── my_script.R
├── build                    <- built files, Makefile
|   ├── debug
|   └── release
├── data
│   └── raw/
│       └── my_data.csv
│   └── clean/
│       └── data_clean.csv
├── docs                     <- documentation
│   └── codelist.txt 
├── project-management       <- project management related documents
│   └── communication.md
│   └── people.md
│   └── project-report.md
│   └── tools.md
├── res                      <- static resources (images and audio files)
│   └── figures
├── .gitignore               <- files excluded from git version control 
├── CODE_OF_CONDUCT          <- Code of Conduct for community projects
├── CONTRIBUTING             <- Contribution guideline for collaborators
├── lib                      <- dependencies (shared components that can be used across an application or across projects, code that supports the core application)
├── logs.txt                 <- history of all major updates like feature release, bug fix, updates
├── example                  <- example code application
├── LICENSE                  <- software license
├── environment.yml          <- anaconda environment setup   
├── install.R                <- R environment setup
├── requirements.txt         <- python environment setup
├── runtime.txt              <- R in binder setup
├── report.md                <- report of analysis
├── README.md                <- information about the repo
├── src                      <- source files
└── test                     <- unit tests  
```

## Resources

### Curated Examples from GitHub

- [_The Turing Way_ project](https://github.com/alan-turing-institute/the-turing-way)
- [Jupyter Book project](https://github.com/executablebooks/jupyter-book)
- [Pandas Package](https://github.com/pandas-dev/pandas)

### R and Python Packages

|    R     | Python | 
| -------- | -------|
|[rrtools](https://annakrystalli.me/rrresearch/10_compendium.html)|[compendium-dodo](https://pypi.org/project/compendium-dodo/)|
|[template](https://github.com/Pakillo/template)|[css-compendium](https://pypi.org/project/ccs-compendium/)|
|[rcompendia](https://github.com/FRBCesab/rcompendium)| |
|[remake](https://github.com/richfitz/remake)| |

### Further Reading

- This [presentation](https://mbjoseph.github.io/intro-research-compendia/#1) on research compendia
- This [paper](https://arxiv.org/abs/1806.09525) on how to read a research compendia
- This [paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004947)  on how to use GitHub includes example repository structures
- This [paper](https://arxiv.org/abs/2102.12727) details the different folder types typically found in repositories
- This [paper](http://mockiene.com/papers/folder-short.pdf) is a case study on what folders most often makeup GitHub repositories
- This [paper](https://www.tandfonline.com/doi/abs/10.1080/00031305.2017.1375986) describes how research compendia in different disciplines can be created using R. 
