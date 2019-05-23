---
title: 'Boost Your Research Reproducibility with Binder'
tags:
- reproducibility
- reproducible research
- data science
- binder
- jupyter
- reproducible environments
- workshop
authors:
- name: The Turing Way
  orcid: 
  affiliation: 1 # (Multiple affiliations must be quoted)
- name: Rachael Ainsworth
  orcid: 0000-0003-2591-9462
  affiliation: 2
- name: Becky Arnold
  orcid: 0000-0003-0355-0617
  affiliation: 3
- name: Louise Bowler
  orcid: 0000-0002-4910-9205
  affiliation: 1
- name: Sarah Gibson
  orcid: 0000-0003-0356-2765
  affiliation: 1
- name: Patricia Herterich
  orcid: 0000-0002-4542-9906
  affiliation: 4
- name: Rosie Higman
  orcid: 0000-0001-5329-7168
  affiliation: "2, 3"
- name: Anna Krystalli
  orcid: 0000-0002-2378-4915
  affiliation: 3
- name: Alexander Morely
  orcid: 0000-0002-4997-4063
  affiliation: "5, 6"
- name: Martin O'Reilly
  orcid: 0000-0002-1191-3492
  affiliation: 1
- name: Andrew Stewart
  orcid: 0000-0002-9795-4104
  affiliation: 2
- name: Kirstie Whitaker
  orcid: 0000-0001-8498-4059
  affiliation: "1, 7"
affiliations:
- name: Alan Turing Institute 
  index: 1
- name: University of Manchester
  index: 2
- name: University of Sheffield
  index: 3
- name: University of Birmingham
  index: 4
- name: Mozilla Foundation
  index: 5
- name: University of Oxford
  index: 6
- name: University of Cambridge
  index: 7
date: 23 May 2019
bibliography: paper.bib
---

# Summary

The Binder Project is an open community that makes it possible to create sharable, interactive, reproducible environments [@Jupyter2018]. 
The main technical product that the community creates is called BinderHub, a cloud platform that captures the computing environment of a GitHub repository within a Docker image. 
It then provides an interactive browser from which code can be run in the environment under which it was developed without placing installation responsibilities on the user. 
A unique URL to this browser is generated making the software easily sharable with collaborators. 
It can improve reproducibility by making it easy to showcase and re-run analyses, improve reliability by making it easy to review analyses and catch bugs early in the development process without installation, and improve the reusability of the code by capturing the computing environment.
To help facilitate the use of Binder in research, the *[Turing Way](https://github.com/alan-turing-institute/the-turing-way/tree/master)* project developed a one-day *Boost your research reproducibility with Binder* workshop to cover reproducible computing environments, showcase examples of others’ projects in [myBinder.org](https://mybinder.org/) and help researchers and data scientists learn how to prepare a Binder-ready project.

This repository contains everything required to run a one-day *Boost your research reproducibility with Binder* workshop. 
This includes the workshop advertisement, pre-event communication emails, agenda, instructor guide, a folder of workshop presentations, a paired example exercise to explore example Binderised notebooks and a feedback form to help measure the impact of the event.
The presentations include an introduction to the workshop, reproducible computational environments and a Zero to Binder code-along built heavily off the [Build a Binder](https://build-a-binder.github.io/) workshop materials.
At the end of the workshop, participants are able to take their own content (in a R or Jupyter notebook, or scripts that can be run in the terminal) and prepare it so that it can be used by others on myBinder.org.
This workshop is aimed at people who are interested in reproducibility, containers, Docker or continuous integration; already familiar with R Markdown or Jupyter notebooks; and looking to communicate their research more effectively.


# Statement of Need

Reproducible research is necessary to ensure that scientific work can be trusted. 
Funders and publishers are beginning to require that publications include access to the underlying data and the analysis code. 
The goal is to ensure that all results can be independently verified and built upon in future work, which is sometimes easier said than done. 
Sharing these research outputs means understanding data management, library sciences, software development, and continuous integration techniques: skills that are not widely taught or expected of academic researchers and data scientists. 

*The Turing Way* is a handbook to support students, their supervisors, funders and journal editors in ensuring that reproducible data science is "too easy not to do". 
Our goal is to provide all the information that researchers need at the start of their projects to ensure that they are easy to reproduce at the end. 
So far, the book (https://the-turing-way.netlify.com) includes chapters and training material on reproducibility, open research, version control, collaborating on GitHub/GitLab, research data management, reproducible environments, analysis testing, reviewing, continuous integration, reproducible research with Make and risk assessment. 
Further chapters currently in progress include coding style for reproducibility, credit for reproducible research and reproducible data analysis pipelines for machine learning, and will build upon Alan Turing Institute case studies. 
The project also demonstrates open and transparent project management and communication with future users, as it is openly developed at our GitHub repository: https://github.com/alan-turing-institute/the-turing-way. 

[add need for Binder]

# References

Jupyter et al., "Binder 2.0 - Reproducible, Interactive, Sharable Environments for Science at Scale." Proceedings of the 17th Python in Science Conference. 2018. 10.25080/Majora-4af1f417-011
