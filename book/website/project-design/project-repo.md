(pd-project-repo)=
# Creating A Project Repository

## Prerequisites

| Prerequisite | Importance |
| -------------|----------|
| {ref}`cl-github-novice` | Helpful |


## Summary

This chapter introduces a step-by-step guide on how to set up a project repository.
This chapter includes examples of GitHub repository hosted and maintained by researchers in open science, however, the principles are applicable to any team-led online repository.
Open science practices described here will also make it easier for you to lead closed-source projects collaboratively and transparently for your teams.

## Background

Developing projects collaboratively on a shared repository requires documentation of our work in detail so that our collaborators are informed of all the updates and information they need to contribute efficiently.
Contributions can be everything from new ideas to bug reports and actual code contributions.
It is also an opportunity to get your ideas across to new or potential contributors.

```{figure} ../figures/file-management-manual.jpg
---
name: file-management-manual
alt: image shows two people organising files. One person is holdinng up a README file and other person is reading the details to set up the data and analysis files in the drawer
---
Illustration about managing files in a repository.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: 10.5281/zenodo.3332807.
```

In this chapter, we have described following documents that should be added to a project repository:
- {ref}`landing page or README file<pd-project-repo-readme>`
- {ref}`Roadmapping<pd-project-repo-roadmapping>`
- {ref}`Contribution Guideline<pd-project-repo-contributors>`
- {ref}`Contribution Guideline<pd-project-repo-participation>`

## First, Add A License

One of the most important documents for your project is a license.

```{note}
Without a license, all rights are with the author of the code, and that means nobody else can use, copy, distribute, or modify the work without consent.
A license gives this consent.
If you do not have a license for your software, it is effectively unusable by the whole research community.

**See {ref}`rr-licensing` for details**
```

The first file you can add to your project repository is a 'LICENSE' file.
You can select a license type based on the level of freedom you would like to give to your users to use and build upon your project, visit [choosealicense.com](https://choosealicense.com/).
Please follow the {ref}`Licensing Checklist<rr-licensing-checklist>` when adding a license to your project repository.
