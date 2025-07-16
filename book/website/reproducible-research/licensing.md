(rr-licensing)=
# Licensing

A license is a legal agreement between creator or owner of a resource such as software, data, and documentation, and its users.
The specific license accompanying a resource clearly defines the scope and communicates what users can and cannot do with the work.
This protects the creator's rights over their resources while granting users some, limited rights.

```{note}
In the context of Intellectual Property (IP) Law, IPs are intangible expressions, such as words, designs, literary and artistic work and scholarly outputs, patents, trademarks and trade secrets, with specific copyrights or monopoly rights.
IPs form the basis of a licensing agreement, where a licensor owns the IP and grants the licensee (users) the right to use it. 

*Reference: {cite}`harvard2025ip`*
```

> This chapter was written using American English, in which the word **license** is a noun **_and_** a verb.
> With British English, however, **licence** is a noun (as in, _to issue a licence_), while **license** is a verb (as in, _they licensed the event_).

(rr-licensing-prerequisites)=
## Prerequisites

No previous knowledge is needed; this chapter explains how important it is to understand how laws and licensing can affect your project.

(rr-licensing-summary)=
## Summary

```{figure} ../../figures/licensing.*
---
height: 500px
name: licensing
alt: "A hand reaches out of an open safe and makes a thumbs-up gesture. The Safe is high-tech-looking with circuit tracery on its surface. The thumb of the hand looks like a signed document. There is a happy face in green looking at the thumbs up from the open safe. In contrast, on the other side of the image, there is a locked version of a similar safe. There is a red and grumpy face looking at the locked safe, which is being shaken in frustration."
---
Licensing. _The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

Licensing of software, data, AI/ML models, hardware and other creative works, such as documentation and visuals, share common attributes and concepts.
This chapter describes those concepts, making it easier for more people to read and understand the usage rights granted by most licenses relevant to the research and data science community.

```{caution}
Good legal advice is timely, specific, and given by an expert; this chapter is none of these.
It was written by engineers & scientists, not by lawyers, and it is a heavily simplified overview of a very complex field.
The intent is to give you an overview of the basics so that you will know when to check whether something you want to do has potential legal ramifications.
Do not make any important decisions based solely on the contents of this chapter.
This document is not intended to be used in that manner.

Consult your librarian and a legal expert to provide actual legal advice for your case.
```

(rr-licensing-where)=
### What, How and Where of License Documentation

Licenses are legal documents that the licensor attaches to the artefacts they share with the licensee/their users.
A license should be clearly visible and state the chosen conditions of the agreement.

A project with multiple resources is organised in a hierarchy of directories and files. 
A licensor should place a plain text file containing the license agreement in the top-level (root) directory of their project.
In a git project, for example, that is shared on a git forge like GitHub or GitLab, a standard file with a name like `LICENSE` will allow the license to be picked up by the host and displayed on their online project repository.
If the license has a standardised short name from [SPDX](https://spdx.org/licenses/), then this will be displayed as a small icon on the project's home page by these hosts.
It can also be useful to include license information in the form of standard strings at the top of each text file in the project.

There are useful tools which automate this available from [REUSE](https://reuse.software/), a project from the [FSFe](https://fsfe.org/) which developed the spec.
This is especially true if your project contains material that is licensed in multiple different ways, or a part of your project is being used in someone else's which uses a different (compatible) license.

### Intellectual Properties

In this chapter, we provide a brief summary of relevant IP laws, without going into too much detail due to their complexity.
A basic understanding of IP law is important for anyone producing creative works governed by it, including documentation, software, datasets, graphics and more.
This is true irrespective of the nature of your project: closed commercial projects building on open tooling; commercial projects maintaining an open resource; open community-driven and/or non-profit projects building shared resources.
Each of these may need to make slightly different licensing choices from the beginning of their projects to be compatible with their goals.

**Read details in the subchapter {ref}`rr-licensing-ip`.**

### Licenses to Support Open Usage

Since, in *The Turing Way*, we aim to promote open and reproducible ways of working, in a subchapter we have explained free and open source software (FLOSS) licensing - **read details in the subchapter {ref}`rr-licensing-floss`.**

We also explain how combining different artefacts from different sources works from a legal perspective  - **read details in the subchapter {ref}`rr-licensing-compatibility`.**

### Ethical Licensing

Decisions about the license selected at the inception of a project can have long-lasting and significant ramifications.
The choices that you make about how your work is licensed shape who can and cannot legally use your work and for what purpose.
Consequently, this chapter will feature some discussion of the ethical ramifications of licensing choices.
It aims to be informative about the implications of licensing choices for the use of your work, but not to prescribe a specific ethic, as there are divergent schools of thought on the ethics of different licensing choices.

We will address the specifics of licensing each of these types of output in their own sub-chapters, as well as a separate sub-chapter on license compatibility.

**Read details in the subchapter {ref}`rr-licensing-ethical-source`.**

### Licensing Other Artefacts

We have also provided separate subchapters for the following resources:

- [Data](#rr-licensing-data)
- [Machine Learning Models](#rr-licensing-ml)
- [Hardware](#rr-licensing-hardware)
