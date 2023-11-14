(rr-vcs)=
# Version Control

(rr-vcs-prerequisites)=
## Prerequisites

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| {ref}`Experience with the command line<rr-overview-resources-commandline>` | Helpful |  |

**Recommended Skill Level**: _Beginner-Intermediate_

(rr-vcs-summary)=
## Summary

No matter how your group is organized, the work of many contributors needs to bemanaged into a single set of shared working documents.
Management of changes or revisions to any types of information made in a file or project is called versioning.

In particular, reproducibility requires the provision of **the code and the data** that was used to produce a figure.
In practice, data and code are modified regularly and one needs to record what was changed when, in order to provide provenance information. 
As we will see in this chapter, version control has a lot of other advantages, which explains why most data science project are hosted on Git platforms.

**Version control is an approach to record changes made in a file** or set of files over time so that you and your collaborators can track their history, review any changes, and revert or go back to earlier versions. 
Management of changes or revisions to any types of information made in a file or project is called versioning.
For example, when writing a paper with multiple collaborators, version control can help track what changed, who changed them, and what updates were made.



```{figure}  ../figures/project-history.*
---
name: project-history
alt: Contrast in project history management. On the left - choosing between ambiguously named files. On the right - picking between successive versions (from V01 to V06).
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```


In this chapter, we introduce  versioning best practices regardless of tools{ref}`in the workflow chapter<rr-vcs-workflow>`, before describing in more details the use of version control and {ref}`git for research projects<rr-vcs-git4research>` that comprise  documentation, datasets and code.
Most instructions given in this chapter will be indeed geared towards Git, which is most commonly used by researchers, and a web-based Git repository hosting service, [GitHub](https://github.com/), which facilitates online collaborations. 
We also give information about {ref}`larger dataset versioning<rr-vcs-data>`, and introduce tools allowing the use Git workflows for this purpose, although Git is not appropriate for binary files versioning.

### Version control systems

Different version control systems can be used through a program with a graphical user interface, web browser-based applications, or command-line tools.
Tools such as Google Drive and Dropbox offer platforms to update files and share them with others in real-time, collaboratively.
More sophisticated version control system exists within tools like [Google docs](https://docs.google.com/) or [HackMD](http://hackmd.io/).
These allow collaborators to update files while storing each version in its version history (we will discuss this in detail).
Advanced version control systems (VCS) such as [Git](https://en.wikipedia.org/wiki/Git), [Mercurial](https://www.mercurial-scm.org/), and [SVN](https://subversion.apache.org/) provide much more powerful tools.
Accessing the version history and keeping control over the main version of your files are particular feature of these advanced tools.

Versioning practices mainly come from managing changes in the code repositories.
However, in reality, you can use version control for nearly any type of file on a computer.
Later in this chapter, we will discuss version control for data and other research project files, which can be applied to keep track of revisions of large amounts of data.
It is useful to know that data can be volatile andversioning them can improve the reproducibility of your scientific analyses.



(rr-vcs-useful)=
### Motivation

In terms of reproducibility, version control is promordial in order to follow **provenance information**.
Because data and analysis code do evolve over time, it can become very difficult or even impossible to know what version of the code and what version of the data was used to produce a particular figure.
This provenance information is enabled and facilitated when both the data, the code and the figure files are under versioning.

In addition, version control creates **version history** to help us understand what changes were made, or why a specific analysis was run, even weeks or months later.
With the help of comments and commit messages in Git, for instance, each version can explain what changes it contains compared to the previous versions.
This is helpful when we share our analysis (not only data), and make it auditable or **reproducible** - which is good scientific practice.

A version control system **neatly hide older versions** of the data. 
So your working directory is not cluttered by the debris of previous versions, while they remain accessible, in case you need them.
Similarly, with version control, there is no need to leave unused chunks of code should you ever need to come back to an old version again.


Finally, version control is invaluable for collaborative projects where different people work on the same data or code simultaneously and build on each other's work.
Using a version contol system, **changes made by different people can be tracked and often automatically combined**, saving a great deal of painstaking manual efforts.
Using version control for your research project means that your work is more transparent. 
Because all your actions are recorded, your studies are easier to reproduce and build upon.
Moreover, version control hosting services such as {ref}`GitHub<cl-github-novice-motivation>`, GitLab and others provide a way to communicate and collaborate in a more structured way, such as in pull requests, code reviews, and issues.
