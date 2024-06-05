# Embedding accessibility in _The Turing Way_ open source community guidance - GSoD Project Report

**Technical Writer:** Paul Owoicho

**Github ID:** [@paulowoicho](https://github.com/paulowoicho)

## Introduction

[_The Turing Way_](https://book.the-turing-way.org/welcome) is an open source book project developed asynchronously by contributors from around the world.
Since inception, the book has widened in scope to not only cover topics in Reproducible Research, but also Project Design, Communication, Collaboration, and Ethical Research.
While this increased scope enhanced the book's impact, the fact that multiple authors contributed to its content introduced aesthetic, structural, and formatting differences across the book. 
For new contributors, this made it challenging to follow the book's style recommendations when existing chapters did not consistently follow them. 
For casual readers, it made _The Turing Way_ somewhat inaccessible as some chapters were long, hard to read, lacked a consistent, well-defined content structure or were not compatible to read on different devices.

To address these concerns, my objectives as a GSoD Technical Writer on _The Turing Way_ project were:

1. **Achieving Retrospective Consistency:** to embed consistency in the existing content of the entire book,
2. **Contributing to Future Maintenance:** to make it easier for contributors to contribute to the project, and
3. **Improving the Overall Accessibility of the Online Book:** to improve the book's user-friendliness and overall accessibility.

The project lead, Kirstie Whitaker and community manager, Malvika Sharan from [The Alan Turing Institute, UK](https://www.turing.ac.uk/) were my mentors who supported my GSoD work.

*[Please see our proposal for more details](https://github.com/alan-turing-institute/the-turing-way/blob/main/communications/GSOD-applications/GSoD-2020-Project-Proposal.md).*

## Contribution Overview

### 1. Achieving Retrospective Consistency

**Goal**: *Improving the consistency of content that is already in The Turing Way in order to make the book accessible for readers from diverse backgrounds.*

To achieve this goal, I started by reviewing and editing some of _The Turing Way_'s existing chapters to familiarise myself with the book's content.
With the insights gained, I worked with my mentors to identify the consistency gaps present in the book and engaged with _The Turing Way_ community to curate a consistency checklist.
This checklist provided guidance for contributors to review existing chapters and uncover ways to improve them.
It also served as a basis for many 'good first issues' I created to fix errors and bugs across the entire book and helped Hacktoberfest contributors participate in the project throughout the month of October. 
Furthermore, with tremendous feedback from my mentors and other core contributors, I authored an extensive [consistency chapter](https://book.the-turing-way.org/community-handbook/consistency.html) to explain each item in the checklist. 
This chapter ensures that old and new contributors have sufficient guidance, recommendations and support to continue maintaining consistency in the book. 

The following GitHub pull requests and issues, and online content were developed to facilitate retrospective consistency:

| Task | PRs/Issues/Online Content |
| -------- | -------- | 
| Reviewing and editing existing chapters    | [#1458](https://github.com/alan-turing-institute/the-turing-way/pull/1458), [#1460](https://github.com/alan-turing-institute/the-turing-way/pull/1460), [#1461](https://github.com/alan-turing-institute/the-turing-way/pull/1461), [#1462](https://github.com/alan-turing-institute/the-turing-way/pull/1462), [#1463](https://github.com/alan-turing-institute/the-turing-way/pull/1463), [#1465](https://github.com/alan-turing-institute/the-turing-way/pull/1465), [#1466](https://github.com/alan-turing-institute/the-turing-way/pull/1466)    |
|Curating a Consistency Checklist| [#1174](https://github.com/alan-turing-institute/the-turing-way/issues/1174)|
|Creating 'good first issues' | [Good first issues](https://github.com/alan-turing-institute/the-turing-way/issues?q=is%3Aopen+is%3Aissue+author%3Apaulowoicho+label%3A%22good+first+issue%22)|
|Making demo videos for items in the Consistency Checklist|[#1651](https://github.com/alan-turing-institute/the-turing-way/pull/1651)|
| **PRs merged into online resources** | [Chapter on Maintaining Consistency](https://book.the-turing-way.org/community-handbook/consistency.html); Revised Chapters on [Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv.html), [Open Research](https://book.the-turing-way.org/reproducible-research/vcs.html), [Version Control](https://book.the-turing-way.org/reproducible-research/vcs.html), [Research Data Management](https://book.the-turing-way.org/reproducible-research/rdm.html), [Licensing](https://book.the-turing-way.org/reproducible-research/licensing.html), [Reproducible Research Overview](https://book.the-turing-way.org/reproducible-research/overview.html) |

### 2. Contributing to Future Maintenance

**Goal**: *Maintaining consistency of content in The Turing Way to make contributions to the project more accessible for new community members.*

For this goal, I worked to create clear pathways for future contributions to _The Turing Way_.
First, I developed templates to guide authors to structure and design new content such as subchapters, case studies and personal stories or modify existing resources. 
The new templates will make improving the book more accessible by helping new contributors write interoperable content from the start.
I also documented the community's contribution workflows and processes by engaging with different community members, and used those insights to create guidelines in a [short chapter](https://book.the-turing-way.org/community-handbook/contributing.html) in the Community Handbook.
This chapter explains all the templates, contribution workflows and guidelines to use them in _The Turing Way_.
This effort will ensure that the book has a cohesive narrative despite being written by a diverse group of authors from around the world.

The following GitHub pull requests and issues, and online content were developed to ensure support for the future contributions and maintenance:

| Task | PRs/Issues/Online Content |
| -------- | -------- | 
| Designing templates     | [#1507](https://github.com/alan-turing-institute/the-turing-way/pull/1507), [#1571](https://github.com/alan-turing-institute/the-turing-way/pull/1571), [#1601](https://github.com/alan-turing-institute/the-turing-way/pull/1601)     |
|Writing a contribution workflow Chapter| [#1646](https://github.com/alan-turing-institute/the-turing-way/pull/1646)|
|Revising existing issue templates | [#1598](https://github.com/alan-turing-institute/the-turing-way/pull/1598) |
| **PRs merged into online resources** | [Chapter on Templates and Workflow](https://book.the-turing-way.org/community-handbook/contributing.html), [Sets of templates](https://github.com/alan-turing-institute/the-turing-way/tree/main/book/templates) |

### 3. Improving the Overall Accessibility of the Online Book

**Goal**: *Improving the accessibility of the material by ensuring that the online book has responsive layout for users reading it in different devices or using accessibility apps.*

My work on this goal focused on minimising the overall information loss readers experienced when reading the book with screen readers or on mobile devices. 
Already, Jupyter Book allows the book's text to reflow to fit all screen sizes and zoom settings. However, images, videos, and tables had to be responsive for _The Turing Way_ to be readable and look great on all devices. 
I created several issues to help facilitate the migration of image formatting from vanilla Markdown to Markedly Structured Text, which automatically handles responsive styling for images. 
Some of these issues also encourage contributors to write descriptive ALT text for the book's images that did not have one. 
This ensures that people using screen readers are able to understand the image's intended message. 

Finally, I wrote custom CSS to create a better layout and responsive styling for tables and videos across the book. 
Most importantly, I documented the use of custom CSS in a [chapter](https://book.the-turing-way.org/community-handbook/style/style-custom-styling.html) in the book's Community Handbook.

The following GitHub pull requests and issues, and online content were developed to enhance book's accessibility:

| Task | PRs/Issues/Online Content |
| -------- | -------- | 
| Responsive styling for tables     | [#1656](https://github.com/alan-turing-institute/the-turing-way/pull/1656)     |
|Responsive styling for videos|[#1651](https://github.com/alan-turing-institute/the-turing-way/pull/1651)|
|Resposive formatting for images|[Issue list](https://github.com/alan-turing-institute/the-turing-way/issues?q=is%3Aopen+is%3Aissue+author%3Apaulowoicho+myst)|
| **PRs merged into online resources** | [Subchapter in style guide](https://book.the-turing-way.org/community-handbook/style/style-more-styling.html), [Subchapter on Stylesheets](https://book.the-turing-way.org/community-handbook/style/style-custom-styling.html) |

### Other Contributions
Beyond my GSoD goals, I contributed to _The Turing Way_ project in other ways.
(Acronym used PR: Pull Request, OLS: Open Life Science)

1. As part of my mentorship in _The Turing Way_, I had the opportunity to join [Open Life Science (OLS)](https://openlifesci.org) mentoring program to gain a practical understanding of open science and leadership that I could integrate into my GSoD project.
It allowed me to closely work with two members, Neha Moopen (Research Data Manager, Utrecht University, The Netherlands) as my project partner and Samuel Guay (PhD researcher,  University of Montreal, Canada) as our OLS mentor, and interact with international participants working on different open science projects.
    - [Issue on OLS issue tracker](https://github.com/open-life-science/ols-2/issues/25)
    - [OLS and _The Turing Way_ projects](https://github.com/alan-turing-institute/the-turing-way/tree/main/open-life-science-mentoring)
3. Some of Jupyter Book's powerful styling features are underutilised in _The Turing Way_. 
I co-authored a subchapter in the Style Guide to make contributors aware of those features and use them in their contributions.
    - [GitHub PR #1642](https://github.com/alan-turing-institute/the-turing-way/pull/1642) and [online chapter](https://book.the-turing-way.org/community-handbook/style/style-more-styling.html)
3. Some of _The Turing Way_'s chapters are either incomplete or missing content and, for some readers, this impacts the overall reading experience. 
I raised issues for other contributors to write content for those chapters and also completed a subchapter on Data Licensing that another contributor started.
    - [See GitHub Issues](https://github.com/alan-turing-institute/the-turing-way/issues?q=is%3Aissue+is%3Aopen+label%3Agsod2020)
4. To continue improving _The Turing Way_, the community needs an understanding of how readers interact with the book. 
I prototyped the use of [Matomo Analytics](https://matomo.org/) for capturing relevant data and monitoring reader engagement with _The Turing Way_ book.
    - [GitHub PR #1660](https://github.com/alan-turing-institute/the-turing-way/pull/1660)
5. _The Turing Way_ promotes a healthy, collaborative environment where no contribution is too small. 
I often reviewed PRs and provided helpful feedback where necessary. 
I also helped some new contributors make their first PRs.
    - [Contributions to GitHub PR's](https://github.com/alan-turing-institute/the-turing-way/pulls?q=is%3Apr+is%3Aclosed+commenter%3Apaulowoicho)
6. I facilitated Hacktoberfest contributions and mentored new contributors who were participating in an Open Source project for the first time via _The Turing Way_.
This allowed me to share my experience with new contributors by reviewing and supporting their contributions.
    - [HacktoberFest issues on _The Turing Way_ repository](https://github.com/alan-turing-institute/the-turing-way/issues?q=is%3Aissue+hacktober+label%3AHacktoberfest)
7. I participated in the November 2020 edition of the _The Turing Way's_ Book Dash event where I closely collaborated with other contributors to improve the book over the course of a week. During this time, I had the opportunity to help some contributors plan their contributions and make their first PRs. Together with Neha Moopen, I also worked on two illustrations that capture my experience on _The Turing Way_ project. 
    - [Contributions recorded under this issue](https://github.com/alan-turing-institute/the-turing-way/issues/1584#issuecomment-737202710)
    
![](https://i.imgur.com/Hq8Ww7m.jpg)

*Illustration co-designed with Scriberia artist at The Turing Way Book Dash, CC-BY 4.0 Scriberia and The Turing Way*

All PRs and Issues related to my activities on _The Turing Way_ project during the Season of Docs program are tagged with the [`gsod2020` label](https://github.com/alan-turing-institute/the-turing-way/labels/gsod2020).

## Challenges

My only challenge was that I was unable to build _The Turing Way_ book locally on a Windows computer. 
Although this did not negatively affect my outputs, it would have been beneficial for me to examine my work locally before making a PR.
At the time of this report, there is an [open issue](https://github.com/executablebooks/jupyter-book/issues/906#issuecomment-681041319) on building Jupyter Book projects on Windows computers.

During the Book Dash, some of the conversations I had with other contributors helped me understand the need for an up-to-date, on-demand PDF version of the entire online book. 
This feature is currently not possible with Jupyter Book, so I raised an issue so that Jupyter Book's maintainers could be aware of this.
    - [PDF issue on the Jupyter Book repository](https://github.com/executablebooks/jupyter-book/issues/1106) 

## Personal Experiences and Benefits

Although _The Turing Way_ is my first open source project, I thoroughly enjoyed the experience and learned a lot along the way.
Before the GSoD program, I only used Github to 'store' my projects. 
Now, I am much more proficient at using Github for collaborative endeavours and I am more adept at working with tools such as Markdown, Jupyter Book, and Sphinx. 
In addition, I gained familiarity with setting up and working with web analytics software.

Asides technical skills, I developed a deep appreciation for what working on an open source project entails. 
My mentors helped me realise that the value I left behind from the GSoD program was not in the amount of work I did, but how I enabled other contributors to also do the work I was doing. 
As a result, I learned to contribute as a Technical Writer in a manner that was reproducible, sustainable, accessible, and inclusive.

## Conclusions and Future Work

Overall, my experience on _The Turing Way_ was exciting and insightful. 
One of the outstanding tasks from the original proposal is implementing an enhanced search functionality for _The Turing Way_ book that makes it easier for readers to find information. 
I will work on this task as part of my future contributions and possibly contribute it upstream to the Jupyter Book project, if successful.

Although, I primariliy worked on _The Turing Way_, I had the opportunity to interact with and learn from other open source projects like [Jupyter Book](https://jupyterbook.org/intro.html) and [Open Life Science](https://openlifesci.org/).
In addition to all I learned, I particularly enjoyed being able to collaborate with passionate people from around the world through these projects and their communities. 
In the near future, I intend to build on the skills I have gained during the GSoD program to start an open-source book that teaches practical Data Science to beginners. 
I also plan to keep contributing to these projects and providing guidance to contributors new to open source wherever possible. 
