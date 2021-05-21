# Designing a repository

## Prerequisites / recommended skill level¶

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| {ref}`Version Control<rr-vcs>` | Helpful | Knowledge of using git for version control |
| {ref}`Open Research<rr-open>` | Helpful | Components are part of the compendium |
| {ref}`Reproducible Environments<rr-renv>` | Helpful | Can be used to make the compendium reproducible |



## Summary 
When planning out a research study, one crucial and often forgotten component is setting up a repository. 

In this section, the benefits and considerations of designing a repository will be outlined, along with an example structure and further resources to guide your workflow.

The prerequisites for this chapter can vary depending on the organisational needs of a project. Creating a repository with a simple research project layout can require minimal technical knowledge (such as managing only input data and output results). Meanwhile advanced repository layouts can be required for more complicated projects (such as projects with dependencies on other projects).


## Background
When planning out a research study, one crucial and often forgotten about component is setting up a repository. 

A repository (or a "repo") is a storage location for your research project. A repository can contain a range of digital objects and can be used to store your project by using online platforms such as GitHub. The aim of a repository is to organise your project in such a way this is both accessible to others and efficent to use. 


In this section, the benefits and considerations of designing a repository will be outlined, along with an example structure and further resources to guide your workflow.

## Benefits
- **Transparent, open, reproducible**
- Version control - no more analysis_script_final_v2_FINAL.R 
- Easy to navigate - time saver for everyone involved!
- Communication - a means of sharing your work 
- Others can build on your work! 

= creating an infrastructure for ethical, open and high quality research from the get go

## Main considerations
- Include a README file, detailing _what_ the repository is for and _how_ to navigate it 
- General structure should separate input (data), methods (scripts) and output (results, figures, manuscript)
- Specify what shouldn't be tracked in the .gitignore file, such as data
- Think about whether a {ref}`license<rr-licensing>`  is needed  
- Include information on your computational environment {ref}`Reproducible Environments<rr-renv>` to ensure reproducibility (this can also be specified in the README)

## Example Repository Structure 
#### Simple research project example:
```
Project Folder/
├── .gitignore                          
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
├── LICENSE                  <- software license
├── install.R                <- environment setup
├── report.md                <- report of project
└── README.md                <- information about the repo
```


#### Every possible folder example:
- Example more for if the project is building an application/is software engineering
```
Project Folder/
├── .gitignore                          
├── src                      <- source files
├── lib                      <- dependencies (shared components that can be used across an application or across projects, code that supports the core application)
├── docs                     <- documentation
│   └── codelist.txt 
├── res                      <- static resources (images and audio files)
│   └── figures
├── data
│   └── raw/
│       └── my_data.csv
│   └── clean/
│       └── data_clean.csv
├── analysis                 <- scripts
│   └── my_script.R
├── build                    <- built files, Makefile
|   ├── debug
|   └── release
├── test                     <- unit tests
├── example                  <- example code application
├── LICENSE                  <- software license
├── environment.yml          <- anaconda environment setup   
├── requirements.txt         <- python environment setup
├── install.R                <- R environment setup
├── runtime.txt              <- R in binder setup
├── report.md                <- report of analysis
└── README.md  
```

## Resources

#### R and Python Packages:

|    R     | Python | 
| -------- | -------|
|[rrtools](https://annakrystalli.me/rrresearch/10_compendium.html)|[compendium-dodo](https://pypi.org/project/compendium-dodo/)|
|[template](https://github.com/Pakillo/template)|[css-compendium](https://pypi.org/project/ccs-compendium/)|
|[rcompendia](https://github.com/FRBCesab/rcompendium)| |
|[remake](https://github.com/richfitz/remake)| |

#### Further Reading:
- This [presentation](https://mbjoseph.github.io/intro-research-compendia/#1) on research compendia
- This [paper](https://arxiv.org/abs/1806.09525) on how to read a research compendia
- This [paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004947)  on how to use GitHub includes example repository structures
- This [paper](https://arxiv.org/abs/2102.12727) details the different folder types typically found in repositories
- This [paper](http://mockiene.com/papers/folder-short.pdf) is a case study on what folders most often make up GitHub repos
- This [paper](https://www.tandfonline.com/doi/abs/10.1080/00031305.2017.1375986) describes how research compendia in different disciplines can be created using R. 
