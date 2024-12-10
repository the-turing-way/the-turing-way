(cm-ro)=
# Research Object to capture the Research Life Cycle

## Prerequisites / recommended skill level
| Prerequisite |  Importance  | Notes        |
| ---------------- |------------------ |--------------|
| {ref}`rr-rdm` | Helpful | RDM lifecyle |

## Summary
Research outcomes encompass publications, data, software, bibliographical material and any other resources (such as experimental workflows, standards) that can be potentially useful for conducting research.

A Research Object (RO) {cite:ps}`Garciasilva2019-research-objects` is a method for the identification, aggregation and exchange of scholarly information on the Web. 
ROs allow working 'open by design' and share research outputs during the research process and not only results at the end.
The primary goal of the RO approach is to provide a mechanism to associate or link related resources about a research investigation so that they can be shared using a single identifier [{term}`def<Identifier>`] {cite:ps}`Belhajjame2015RO`.

In this chapter, we will introduce ROs, their typologies and which platform and technologies exist to create and publish them.

```{figure} ../figures/research-object.*
---
name: ro-lifecyle
alt: This image shows how research objects evolve and grow in content during the collaboration process and how new research objects can be derived from existing ones.
---
Research Objects allow working open by design and share during the research process and not only the research outputs at the end. _The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(cm-ro-motivation)=
## Background & Motivation

Research objects (ROs) are living resources helping to organise and describe the inputs, materials, and methods used in a scientific experiment and obtained as a result and not only at the end when publishing the research outcomes. 
ROs encompass research outputs created, revised and shared throughout the research lifecycle that help validate findings claimed in scholarly publications.
In short, ROs can be seen as a "single information unit" where any research material can be shared with other scientists at discrete milestones of the investigation within and outside the project.

Motivation behind RO is the need to identify and share all components such as data, source code, tools, method documentation, as well as communication materials such as presentations, videos, blogs and other tangible outcomes. 
The entire research lifecycle can be captured, allowing the release and publication of results progressively, keeping track of versioning and change information. 
ROs facilitate reproducibility of the scientific methods and results through access to resources, context and metadata, and reuse with the possibility of forking existing ROs. 

There are three guiding principles for RO:
- Digital identity - Using unique identifiers, such as DOIs for tangible outcomes such as publications or data, and ORCID ids for researchers (explained in detail in the {ref}`ORCID section<cm-citable-orcid>`.
- Data aggregation - Using a method to aggregate all outcomes so that they are discoverable and hence allow anyone to investigate and reproduce the research.
- Annotation - Use rich machine-readable metadata (discussed in {ref}`Chapter on Documentation and Metadata<rr-rdm-metadata>`) that help ensure findability and accessibility of all scientific work.
RO helps understand the entire research lifecycle through research outcomes including publication shared progressively, allowing to track the versioning and development of the entire project.

All the research work, including potential failures, dead ends or any other information such as experimental protocols, software code, standards as well as all the individuals who contributed to the research can also be recorded in the RO. 
As a result, ROs support evidence and support validation of findings claimed in scholarly articles.

(cm-ro-contribute)=
## Contribute to this Chapter
We invite all contributions in the following areas:
- Add or update relevant concepts regarding ROs and related concept such as FAIR Digital Objects {cite:ps}`desmedtetal20202-FAIR-digitalobjects`;
- Complete and/or add information about typologies;
- Include additional implementation of ROs and associated services.
