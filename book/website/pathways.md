(pathways)=
# Pathways Feature in *The Turing Way*

## Introduction

Since its inception in 2019, *The Turing Way* has experienced significant growth, with a diverse community of contributors creating a wealth of materials covering various aspects of data science practices.

This necessary expansion, aimed at enhancing the usability of *The Turing Way* for diverse user groups, has introduced a key challenge: how can users efficiently locate the information most relevant to their specific needs and skill levels?
To address this, the 'Pathways' feature was developed and implemented within *The Turing Way*, which is briefly described in this chapter.

### Background

*The Turing Way* has grown into a comprehensive resource, shaped by hundreds of contributors, used by thousands of individuals monthly, and cited in numerous projects across diverse sectors. 
However, new or returning users with varying levels of expertise might find the sheer volume of information overwhelming when engaging with the online version, potentially struggling to identify relevant chapters or grasp the breadth of topics covered.
This difficulty in navigation could hinder user engagement and impede the adoption of good data science practices, the core mission of *The Turing Way*.

This challenge led to the development of the 'Pathways' feature (inspired by the concepts of {ref}`Personas and Pathways<pd-persona>`).
Its specific aim is to improve content discovery without overwhelming users (personas) with a large amount of information that may not be immediately useful for them.

## Enhancing Navigation of *The Turing Way* Resources

The Pathways feature was conceived to enhance the usability of *The Turing Way* by establishing user-specific entry points with curated sets of chapters tailored to particular personas or specific themes, referred to as 'profiles'.
The primary motivation behind this addition to *The Turing Way*'s infrastructure was to simplify navigation, enabling users to quickly access content relevant to their roles and interests.

By offering curated content drawn from the book's extensive resources, Pathways in *The Turing Way* provide clear 'ways' for users to begin their journey with the book quickly and in a more intuitive and efficient manner.
For instance, a user identifying as an [early-career researcher](https://book.the-turing-way.org/pathways/early-career-researchers) or a [research software engineer](https://book.the-turing-way.org/pathways/research-software-engineers) can start using *The Turing Way* by directly engaging with these curated chapter sets.
They can also easily share resources on specific themes, such as [software citation](https://book.the-turing-way.org/pathways/software-citation) or [leadership skills](https://book.the-turing-way.org/pathways/project-leaders) with their colleagues.
These kinds of engagement eventually lead to users identifying gaps in the materials, and contribute back by developing needed resources in *The Turing Way*.

By lowering the entry barrier and facilitating easy engagement, Pathways helps individuals improve their skills in their desired areas and foster curiosity to explore additional resources within the book.

### Pathway Files and Resources

For readers, Pathways can be found in the [Welcome page](https://book.the-turing-way.org/#different-pathways) and in a dedicated section immediately after the welcome page.

For contributors, a 'profiles.yml' file can be edited, which is located in the [`book/website/` folder](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/profiles.yml) within *The Turing Way* Book's GitHub repository.
In this YAML file, information about different profiles can be edited, and new sets of curated chapters can be added for new profiles.

For developers, the Python package supporting this feature is hosted in an open source repository under *The Turing Way* GitHub organisation: [github.com/the-turing-way/pathways/](https://github.com/the-turing-way/pathways/).

### Development and Maintenance

With a strong emphasis on user experience, the Pathway feature was developed in two stages:

  * **Stage 1 - Prototype Development**: A team of developers collaborated with *The Turing Way* team between 2021 and 2022 to explore various solutions for improving content discoverability within *The Turing Way*.
To maintain the book's lightweight nature and minimise the maintenance burden, a Python package was developed and implemented on a test version of the book.
This stage received support through internal funding and collaboration with the Research Engineering Group at The Alan Turing Institute ([read proposal](https://github.com/the-turing-way/project-management/blob/main/proposals/2021-07-ux-funding-turing.md)).
  * **Stage 2 - User Testing and Implementation**: This stage focused on gathering and integrating user feedback on the prototype and incorporating the Python package into *The Turing Way*'s main GitHub repository.
This stage was supported by volunteer members and *The Turing Way* through Google Summer of Code in 2023 (read [proposal and report](https://github.com/the-turing-way/pathways/)).

The development process, driven by active user engagement, feedback, and an open-source approach, has resulted in a valuable addition to *The Turing Way*, further supporting its mission of making data science accessible to all.

The package is now maintained by members of the Infrastructure Working Group, who also contribute upstream in collaboration with the Jupyter Book team.

More information about their work can be found in the [Infrastructure chapter](https://book.the-turing-way.org/community-handbook/infrastructure).
