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

The Binder project is an open community that makes it possible to create sharable, interactive, reproducible environments [@project_jupyter-proc-scipy-2018]. 
The main technical product that the community creates is called BinderHub, a cloud platform that captures the computing environment of a GitHub repository within a Docker image. 
It then provides an interactive browser from which code can be run in the environment under which it was developed without placing installation responsibilities on the user. 
A unique URL to this browser is generated making the software easy to share with others. 
This can improve reproducibility by making it easy to showcase and re-run analyses, improve reliability by making it easy to review analyses and catch bugs early in the development process without installation, and improve the reusability of the code by capturing the computing environment. 
To help facilitate the use of Binder in research, the *[Turing Way](https://github.com/alan-turing-institute/the-turing-way)* project developed a one-day *Boost your research reproducibility with Binder* workshop. 
The learning objectives were to improve participants understanding of reproducible computing environments, showcase examples of others’ projects in [myBinder.org](https://mybinder.org/) and train researchers how to prepare a Binder-ready project.

This repository contains everything required to run the one-day workshop. 
All materials were used in the *Turing Way* run workshops, and can be easily remixed and reused when adopted by others to suit their target audience and number of event facilitators. 
They include the workshop advertisement, pre-event communication emails, agenda, instructor guide, a folder of workshop presentations, a paired example exercise to explore example Binderised notebooks, a feedback form and report to help measure the impact of the event and how to improve in the future. 
The presentations include an introduction to the workshop, slides on reproducible computational environments and a Zero to Binder code-along built heavily off the [Build a Binder](https://build-a-binder.github.io/) workshop resources. 
There are also slides on using Binder for fully reproducible research in R as an alternative to the Python-focused code-along. 
At the end of the workshop, participants are able to take their own content (in a R or Jupyter notebook, or scripts that can be run in the terminal) and prepare it so that it can be used by others on [myBinder.org](https://mybinder.org/). 
Individuals unable to attend a workshop can also work through these resources to improve their understanding of reproducible computational environments and how to prepare their project for sharing with Binder. 
This material is aimed at aimed at researchers and others who are who are interested in reproducibility, containers or continuous integration; already familiar with R Markdown or Jupyter notebooks; and looking to communicate their research more effectively.

The feedback report summarises our experience of using these materials in teaching and learning situations. On average, participants report an increase  in their understanding and confidence in using Binder, capturing their computational environment and reproducing their research. Areas that participants identified could be improved include highlighting the difficulties using R with Binder and in particular the tidyverse package which takes a long time to build, that the demonstrations in the afternoon were slower and that some time was taken during the workshop to explain Git terminology,  Markdown and help people get set up.

# Statement of Need

Reproducible research is necessary to ensure that scientific work can be trusted. 
Funders and publishers are beginning to require that publications include access to the underlying data and the analysis code. 
The goal is to ensure that all results can be independently verified and built upon in future work, which is sometimes easier said than done. 
Sharing these research outputs means understanding data management, library sciences, software development, and continuous integration techniques: skills that are not widely taught or expected of academic researchers and data scientists. 

*The Turing Way: A Handbook for Reproducible Data Science* [@the_turing_way_community_2019_3233986] is an open source handbook to support students, their supervisors, funders and journal editors in ensuring that reproducible data science is "too easy not to do". 
The goal is to provide all the information that researchers need at the start of their projects to ensure that they are easy to reproduce at the end. 
The [handbook](https://the-turing-way.netlify.com) currently includes chapters and training material on reproducibility, open research, version control, collaborating on GitHub/GitLab, research data management, reproducible environments, analysis testing, reviewing, continuous integration, reproducible research with Make and risk assessment. 
Further chapters in development include coding style for reproducibility, credit for reproducible research and reproducible data analysis pipelines for machine learning, and will build upon Alan Turing Institute case studies. 
The project demonstrates open and transparent project management and communication with future users, as it is openly developed at the [GitHub repository](https://github.com/alan-turing-institute/the-turing-way). 
It also facilitates workshops to train researchers and research software engineers to use tools to make their work more reproducible - one of which is the *Boost your research reproducibility with Binder* workshop.

The Binder project supports the ability to instantly reproduce and interact with shared code, as it allows a user to try out someone else's work simply by clicking a single link. 
The majority of researchers and educators interested in reproducible research have not yet discovered the Binder project, or they have heard it mentioned but do not know how to get started [@build_a_binder]. 
The tool is most impactful if some time is invested to understand its potential and workings. 
The *Boost your research reproducibility with Binder* workshops were conducted to increase the number of people publishing their data analyses using this tool which enables others to access, edit, re-run and re-use that content. 
Preparing and delivering these workshops also enabled the *Turing Way* project to feedback directly to the open source Binder project. 
It also had the immediate impact that one of the participants has already incorporated using Binder in their teaching, and contributed their slides on using Binder for fully reproducible research in R as an alternative to the Python-focused workshop.

# Acknowledgements

This work was supported by The UKRI Strategic Priorities Fund under the EPSRC Grant EP/T001569/1, particularly the "Tools, Practices and Systems" theme within that grant, and by The Alan Turing Institute under the EPSRC grant EP/N510129/1.


# References
