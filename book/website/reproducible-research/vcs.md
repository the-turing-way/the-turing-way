(rr-vcs)=
# Version Control

(rr-vcs-prerequisites)=
## Prerequisites

| Prerequisite | Importance | Notes |
| -------------|----------|------|
|[Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Helpful |  |

**Recommended Skill Level**: _Beginner-Intermediate_

(rr-vcs-summary)=
## Summary

No matter how your group is organized, the work of many contributors needs to be managed into a single set of shared working documents.
Version control is an approach to record changes made in a file or set of files over time so that you and your collaborators can track their history, review any changes, and revert or go back to earlier versions.
Management of changes or revisions to any types of information made in a file or project is called versioning.

In this chapter, we discuss the best practices that are relevant regardless of tools.
Versioning practices mainly come from managing changes in the code repositories.
However, in reality, you can use version control for nearly any type of file on a computer.
For example, when writing a paper with multiple collaborators, version control can help track what changed, who changed them, and what updates were made.

Different version control systems can be used through a program with a graphical user interface, web browser-based applications, or command-line tools.
We have all seen a simple file versioning approach where different versions of a file are stored with a different name.
Tools such as Google Drive and Dropbox offer platforms to update files and share them with others in real-time, collaboratively.
More sophisticated version control system exists within tools like [Google docs](https://docs.google.com/) or [HackMD](http://hackmd.io/).
These allow collaborators to update files while storing each version in its version history (we will discuss this in detail).
Advanced version control systems (VCS) such as [Git](https://en.wikipedia.org/wiki/Git), [Mercurial](https://www.mercurial-scm.org/), and [SVN](https://subversion.apache.org/) provide much more powerful tools.

This chapter aims to cover the general principles underpinning all the advanced version control systems and best practice which applies for all such systems.
We discuss many tools and features; however, we encourage readers to use features that are useful for their work and tools they are comfortable with.
Most instructions given in this chapter will also be geared towards Git, which is most commonly used by researchers, and a web-based Git repository hosting service, [GitHub](https://github.com/), which facilitates online collaborations.

Later in this chapter, we also discuss version control for data, which is applied to keep track of revisions of large amounts of data, especially when working collaboratively.
It is useful to know that data can be volatile and versioning them can improve the reproducibility of your scientific analyses.

```{figure}  ../figures/project-history.*
---
name: project-history
alt: Contrast in project history management. On the left - choosing between ambiguosly named files. On the right - picking between successive versions (from V1 to V6).
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(rr-vcs-useful)=
## Motivation and Background

Version control helps us understand what changes we made in the past or why we did a specific analysis in the way we did it, even weeks or months later.
With the help of comments and commit messages, each version can explain what changes it contains compared to the previous versions.
This is helpful when we share our analysis (not only data), and make it auditable or **reproducible** - which is good scientific practice.

A version control system neatly stores a history of changes and who made them, so while it is still easy to access them, your working directory is not cluttered by the debris of previous versions that are necessary to keep just in case.
Similarly, with version control, there is no need to leave chunks of code commented should you ever need to come back to an old version again.


Finally, version control is invaluable for collaborative projects where different people work on the same code simultaneously and build on each other's work.
It allows the changes made by different people to be tracked and can automatically combine people's work while saving a great deal of painstaking effort to do so manually.
Using version control for your research project means that your work is totally transparent, and because all your actions are recorded, it enables others to reproduce your studies.
Moreover, version control hosting services such as {ref}`GitHub<cl-github-novice-motivation>` provide a way to communicate and collaborate in a more structured way, such as in pull requests, code reviews, and issues.
