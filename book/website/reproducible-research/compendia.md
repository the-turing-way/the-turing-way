(rr-compendia)=
# Research Compendia

## Prerequisite

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| {ref}`Version Control<rr-vcs>` | Helpful | Can be used to version the compendium|
| {ref}`Open Research<rr-open>`       | Helpful | Components are part of the compendium |
| {ref}`Reproducible Environments<rr-renv>` | Helpful | Can be used to make the compendium reproducible |
| {ref}`Binder Hub<rr-binderhub>` | Helpful | Can be used to publish the compendium |
| {ref}`Make<rr-make>` | Helpful | Can be used for automation in the compendium |

## Summary

A research compendium is a collection of all digital parts of a research project including data, code, texts (protocols, reports, questionnaires, meta data).
The collection is created in such a way that reproducing all results is straightforward {cite:ps}`Nuest2017compendia,Gentleman2007statistical`.

This chapter has many prerequisites as it takes all digital components of a project together into a reproducible research package.
That said: a research compendium can be constructed with minimal technical knowledge.
The main purpose is that all elements of a project are published together, so a basic folder structure combining all components can be sufficient.

```{figure} ../figures/research-compendium.*
---
height: 500px
name: research-compendium
alt: An illustration showing a person churning a big machine that takes scientific information from multiple papers and gives one output of readable file.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

## Motivation

A research compendium [{term}`def<Research Compendia>`] combines all elements of your project, allowing others to reproduce your work, and should be the final product of your research project.
Publishing your research paper along with a research compendium allows others to access your input, test your analysis, and, if the compendium can be executed, rerun to assess the resulting output.
This does not only instill trust in your research but can give you more visibility.
Others may use your research in unexpected ways, some of which are discussed below (refer to section: {ref}`Using a research compendium<rr-compendia-using>`).

## Background

A research compendium at its most basic is a comprehensive set of files that combines all components of a project.
This compendium can be downloaded and run locally to recreate the work done, or it can contain elements that allow it to be executed on a remote server.
Executable research compendia aim to make the computational part of a scientific publication reproducible by providing all the building blocks available and give a description of how the user can execute the contained code.


### Structure of a Research Compendium

Three principles should be kept in mind when constructing a research compendium {cite:ps}`Marwick2018compendia`.

- Files should be organized in a conventional folder structure;
- Data, methods, and output should be clearly separated;
- The computational environment should be specified.

With these principles, a wide variety of compendia are possible.
Let's start with the most basic version.


#### Basic Compendium

A basic compendium follows these three principles.
It separates data and methods into a conventional folder structure, and describes the computational environment in a designated file.
Furthermore, any compendium should have a landing page in the form of a README document.

```text
compendium/
├── data
│   ├── my_data.csv
├── analysis
│   └── my_script.R
├── DESCRIPTION
└── README.md
```

#### Executable Compendium

The following folder can be considered an executable research compendium.
It contains all the digital parts of the research project (code, data, text, figures) and all the information on how to obtain the results.
The computing environment is described in the `Dockerfile`, the dependencies of files and how to automatically generate the results are described in the `Makefile`.
Additionally we have a `README.md` describing what the compendium is about and a `LICENSE` file with info on how it can be used.

```text
compendium/
├── CITATION
├── code
│   ├── analyse_data.R
│   └── clean_data.R
├── data_clean
│   └── data_clean.csv
├── data_raw
│   ├── datapackage.json
│   └── data_raw.csv
├── Dockerfile
├── figures
│   └── flow_chart.jpeg
├── LICENSE
├── Makefile
├── paper.Rmd
└── README.md
```

#### Separating Methods, Data, Output

The principles of a research compendium state that it should clearly separate Methods, Data, and Output.
Phrased differently, this means we should distinguish between three types of files and folders:

- **Read-only**: raw data (`data_raw\`), metadata (`datapackage.json`, `CITATION`)
- **Human-generated**: code (`clean_data.R`, `analyse_data.R`), paper (`paper.Rmd`), documentation (`README.md`)
- **Project-generated**: clean data (`data_clean\`, figures (`figures\`), other output

The examples mentioned here are not exhaustive and some may first be "human-generated" and at some point become "read-only" (for example a human may generate the data metadata `datapackage.json`, but once that is done it may become something not to be touched).
In other words, whether a folder contains files in either of these categories, may depend on the life cycle of the project.


### Creating a Compendium

If you already use some of the tools in this book - such as version control, Makefiles, and/or reproducible environments - it may come naturally to you to create a research compendium.
This is, because a version control repository can be a research compendium; A Makefile makes it executable; A reproducible environment makes it reproducible.
To create a research compendium, we recommend to first think about *what the components of your project are* and create the folder structure accordingly.
Use names for files and folders that make it easy for others to understand what they contain.
It is a good idea to think about this early in the research process and start your project with the mindset that the output in the end is a research compendium rather than just a research paper.


### Publishing a Compendium

There are several options to publish a research compendium:

- On a versioning platform such as GitHub or GitLab (potentially with a link to Binder).
- On a research archive such as Zenodo or the Open Science Framework (OSF).
- As supplementary material of a paper publication.

For examples, see the label/tag/community "research-compendium" (applied on GitHub, Zenodo, OSF) or as a fallback the term "research compendium" in the description (used on GitLab). For more info, see also [Research Compendium](https://research-compendium.science).

In the future, the research compendium may even be the publication itself allowing peer review of the entire research project.

(rr-compendia-using)=
### Using a Compendium

A research compendium can be used in several ways, including (but not limited to):

- Peer review: If peers can check what you have done, they can review it much more thoroughly.
- Understanding research: If you really want to understand what someone has done in their research project, the research compendium is what you need to look at.
- Teaching: Research compendia can be great examples to be used in teaching.
- Reproducibility studies / repro hacks: A research compendium allows other researchers to attempt (and hopefully succeed) to redo your computations.


## Checklist

To create a research compendium, follow these steps:

- Think about a good folder structure (see example above)
- Create folder structure (main directory and sub directories)
- Optional: Make the compendium into a git repository
- Add all files needed for reproducing the results of the project
- Try to have the compendium as clean and easy to use as possible when you advertise it for others to use
- Optional: Have a peer check the compendium and see if it works correctly
- Publish your compendium

See the [EMNLP 2020 reproducibility checklist](https://2020.emnlp.org/call-for-papers#new-reproducibility-criteria) or the [AGILE reproducible checklist](https://doi.org/10.17605/OSF.IO/CB7Z8) for conference submission checklists. 

## Further Reading

- The website [Research Compendium](https://research-compendium.science) contains links to further resources and publications on research compendia as well as links to examples.
