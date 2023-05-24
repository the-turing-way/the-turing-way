(pd-project-repo)=
# Creating Project Repositories

## Prerequisites

| Prerequisite | Importance |
| -------------|----------|
| {ref}`cl-github-novice` | Helpful |


## Summary

This chapter introduces a step-by-step guide on how to set up a project repository.
Specifically, we describe key documents that you should add to your repository in order to maintain documentation and ensure effective collaboration.
We provide examples from GitHub repository hosted and maintained by researchers in open science, however, the principles are applicable to any team-led online repository.

## Motivation

Online project repositories require documentation so that all collaborators are informed of the updates and contributors are provided with details they need to contribute efficiently.
Shared documents can help you get your ideas across to new or potential contributors.
Contributions can be anything from new ideas to bug reports and actual code contributions.
Open science practices described here will also make it easier for you to lead closed-source projects collaboratively and transparently for your teams.

```{figure} ../figures/file-management-manual.*
---
name: file-management-manual
alt: image shows two people organising files. One person is holdinng up a README file and other person is reading the details to set up the data and analysis files in the drawer
---
Illustration about managing files in a repository.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: 10.5281/zenodo.3332807.
```

In this chapter, we have described following documents that should be added to a project repository:
- {ref}`Landing Page - README File<pd-project-repo-readme>`
- {ref}`Roadmapping<pd-project-repo-roadmapping>`
- {ref}`Contributor Pathways<pd-project-repo-contributors>`
- {ref}`Participation Guidelines<pd-project-repo-participation>`

(pd-project-repo-license)=
## Start by Adding a License

One of the most important documents for your project is a license.

```{note}
Without a license, all rights are with the author of the code, and that means nobody else can use, copy, distribute, or modify the work without consent.
A license gives this consent.
If you do not have a license for your software, it is effectively unusable by the whole research community.

**See {ref}`rr-licensing` chapter for details**
```

The first file you can add to your project repository is a 'LICENSE' file.
You can select a license type based on the level of freedom you would like to give to your users to use and build upon your project, visit [choosealicense.com](https://choosealicense.com/).
Please follow the {ref}`Licensing Checklist<rr-licensing-checklist>` when adding a license to your project repository.
