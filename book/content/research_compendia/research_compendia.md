# Chapter title

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| [Version Control](/version_control/version_control) | Helpful | Can be used to version the compendium| 
| [Open Research](/open_research/open_research)       | Helpful | Components are part of the compendium |
| [Reproducible Environments](reproducible_environments/reproducible_environments) | Helpful | Can be used to make the compendium reproducible |
| [Binder Hub](binderhub/binderhub) | Helpful | Can be used to publish the compendium |
| [Reproducibility with Make](make/make) | Helpful | Can be used for automation in the compendium |

## Summary

A research compendium is a collection of all digital parts of a research project including data, code, texts (protocols, reports, questionnaires, meta data).
The collection is created in such a way that reproducing all results is straight forward.

This chapter has many prerequesites as it takes all components together into a reproducible research package.

<!--- TODO: add image of package with code, text, graphs, questionnaires, ... -->

## How this will help you/ why this is useful

This should be the final product of your research project.

## Chapter content

Executable research compendia aim to make the computational part of a scientific publication reproducible by providing all the building blocks available and give a description of how the user can execute the containing code.

Imagine a research project with the following folder structure:

```text
research_project/
├── code
│   ├── analyse_data.R
│   └── clean_data.R
├── data
│   └── data_raw.csv
├── Dockerfile
├── figures
│   └── flow_chart.jpeg
├── LICENSE
├── Makefile
├── paper.Rmd
└── README.md
```

The folder `research_project` can be considered an executable research compendium. 
It contains all the digital parts of the research project (code, data, text, figures) and all the information on how to obtain theresults. 
The computing environment is described in the `Dockerfile`, the dependencies of files and how to automatically generate the results are described in the `Makefile`.
Additionally we have a `README.md` describing what the compendium is about and a `LICENSE` file with info on how it can be used.

We could now consider how to publish this research compendium.
One option would be to publish it with binder to make it easily reproducible for others. 
Or we could publish it as supplementary material with the paper.
In the future, the research compendium may even be the publication itself which is being peer reviewed (rather that just peer reviewing the paper, why not review the entire research project).

## Checklist

To create a research compendium, follow these steps:

- [ ] Think about a good folder structure (see example above)
- [ ] Create folderstructure on your computer
- [ ] Optional: Make the compendium into a git repository
- [ ] Add all files needed for reproducing the results of the project
- [ ] Try to have the compendium as clean and easy to use as possible when you advertise it for others to use
- [ ] Optional: Use Binder for publishing the compenidum in an easy to use way


## What to learn next

<!--- TODO: recommended next chapters that are a good next step up -->

## Further reading

- https://research-compendium.science

<!---
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail
-->


## Definitions/glossary

See our [glossary](glossary/glossary) for explanations of terms used in the chapter.


## Bibliography

<!--- TODO: add references -->

