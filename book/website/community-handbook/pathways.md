(ch-pathways)=
# Pathways Feature in *The Turing Way*

## Introduction

Since its inception in 2019, *The Turing Way* has experienced significant growth, with a diverse community of contributors creating a range of chapters covering various aspects of data science practices.

This expansion, although necessary for enhancing the usability of *The Turing Way* for diverse user groups, has introduced a challenge for both the new and returning users of the book: *how can users efficiently locate the information most relevant to their specific needs and skill levels?*
To address this, the 'Pathways' feature was developed and implemented within *The Turing Way*, which is briefly described in this chapter.

### Background

*The Turing Way* is an ever-evolving book, written by hundreds of contributors, used by thousands of individuals monthly, and cited in numerous projects across diverse sectors.
Despite its significant impact and broad adoption, the sheer volume of information within *The Turing Way* poses a navigational challenge.
This can overwhelm users, making it difficult to find relevant content and understand the full spectrum of good data science practices it advocates.
This user experience risks discouraging community members from effectively using *The Turing Way* and adopting the good practices we champion.

To tackle this issue, we've introduced the 'Pathways' feature.
Drawing on the concepts of [Personas and Pathways](#pd-persona), this is implemented as a [MyST plugin](https://github.com/the-turing-way/myst-curation), designed to improve content discovery (pathways) by preventing users (personas) from being overwhelmed with information that may not be immediately relevant.

This MyST plugin replaces a Python package developed within *The Turing Way* to integrate with the JupyterBook ecosystem, and make the reuse of this feature easier for others.

```{figure} ../../figures/open-development-path.jpg
---
height: 400px
name: open-development-path
alt: >
  Here we have a group of people from different areas who are talking about topics of their interests.
  A good way to show how pathways can help not just the people from the group it is prepared for, but others who are interested in the field.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

This [package](https://github.com/the-turing-way/myst-curation) is now maintained by members of the Infrastructure Working Group, who also collaborate with the Jupyter Book team and contribute upstream.

## Enhancing Navigation of *The Turing Way* Resources

The Pathways feature was conceived to enhance the usability of *The Turing Way* by establishing user-specific entry points with curated sets of chapters tailored to particular personas or specific themes, referred to as 'profiles'.
The primary motivation behind this addition to *The Turing Way*'s infrastructure was to simplify navigation, enabling users to quickly access content relevant to their roles and interests.

By offering curated content drawn from the book's extensive resources, Pathways in *The Turing Way* provide clear 'ways' for users to begin their journey with the book quickly and in a more intuitive and efficient manner.
For instance, a user identifying as an [early-career researcher](#pathway-early-career-researchers) or a [research software engineer](#pathway-research-software-engineers) can start using *The Turing Way* by directly engaging with these curated chapter sets.
They can also easily share resources on specific themes, such as [software citation](#pathway-software-citation) or [leadership skills](#pathway-project-leaders) with their colleagues.
These kinds of engagement eventually lead to users identifying gaps in the materials, and contribute back by developing needed resources in *The Turing Way*.

By lowering the entry barrier and facilitating easy engagement, Pathways helps individuals improve their skills in their desired areas and foster curiosity to explore additional resources within the book.

### Pathway Files and Resources

For readers, Pathways can be found in a [dedicated section](#pw) immediately after the welcome page.

For contributors, the `curation` directives can be edited.
These are written in the Markdown files in the Pathways section.
For example, [the Data Stewards pathway](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/pathways/pathways-data-stewards.md)
The [myst-curation demo site](https://the-turing-way.github.io/myst-curation/) also has examples of how to use the directive.

### Transitioning Python Package to MyST Plugin

The MyST plugin replaces a Python package implementation of the Pathway feature originally developed to address the community's need to make resources browsable.
With the book's migration to MyST and JupyterBook2, we wanted to create a new MyST-native pathways implementation taking advantage of the [MyST abstract syntax tree](xref:myst-spec/#myst-abstract-syntax-tree).
In the long term this approach has a number of advantages, including,

- Fewer lines of code
- A simpler process to build the book with pathways
- A more generic package, which other MyST or JupyterBook projects may want to use

The Python package was developed in two stages through separate funding and team involvement:

* **Stage 1 - Prototype Development**: A team of developers collaborated with *The Turing Way* team between 2021 and 2022 to explore various solutions for improving content discoverability within *The Turing Way*.
  To maintain the book's lightweight nature and minimise the maintenance burden, a Python package was developed and implemented on a test version of the book.
  This stage received support through internal funding and collaboration with the Research Engineering Group at The Alan Turing Institute ([read proposal](https://github.com/the-turing-way/project-management/blob/main/proposals/2021-07-ux-funding-turing.md)).
* **Stage 2 - User Testing and Implementation**: This stage focused on gathering and integrating user feedback on the prototype and incorporating the Python package into *The Turing Way*'s main GitHub repository.
  This stage was supported by volunteer members and *The Turing Way* through Google Summer of Code in 2023 (read [proposal and report](https://github.com/the-turing-way/pathways/)).

The development process, driven by active user engagement, feedback, and an open-source approach, has resulted in a valuable addition to *The Turing Way*, further supporting its mission of making data science accessible to all.
