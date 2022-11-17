(cl-infrastructure-rse)=
# Research Software Engineer: Overview

Research Software Engineers (RSEs) are a broad group of people who combine software engineering expertise with an intimate understanding of research to contribute to the academic community. [1](https://society-rse.org/about/)
RSEs are involved in developing, maintaining, and deploying research software so that it is widely useable, well-documented, and produces reproducible outputs. [2](https://us-rse.org/about/what-is-an-rse/)

While RSEs are increasingly critical to academic research, they often come from a variety of backgrounds and make diverse contributions which may not fit neatly into current formal academic roles, creating barriers to recognition and advancement. [3](https://nl-rse.org/posts/2017-06-13-what-is-rse)
Therefore, this chapter provides information about RSE roles, outlines the challenges RSEs face and the benefits they bring, and lists active community groups promoting RSE awareness.
<!-- 
To footnote:
This overview combines parts of the following descriptions and definitions of the RSE role:
https://rse-aunz.github.io
https://nl-rse.org/posts/2017-06-13-what-is-rse
https://us-rse.org/about/what-is-an-rse/
https://society-rse.org/about/
-->

(cl-infrastructure-rs-importance)=
## The Importance of Research Software (and Research Software Engineers!)
A comprehensive survey of academics indicated that more than nine in ten academics use research software, and seven in ten academics say their research would not be practical without it {cite:ps}`Hettrick2014SIRSurvey`.
However, support and funding for the development of research software is insufficient, if not non-existent.
For example, Astropy is a Python package widely used by the astronomical community, from national laboratories to NASA space telescopes, which includes over 200,000 lines of code.
Hiring professional software developers to write the Astropy package would have required about $8.5 million USD, by one estimate [4](https://arxiv.org/abs/1610.03159).
But instead the academics who wrote Astropy did so during their own spare time without funding dedicated to software development -- creating great benefits for the astronomical community with no guarantee of financial reward or career recognition.

In 2013 the UK Research Software Engineers Association was launched in response to the lack of recognition and advancement opportunities for software developers in academia [5](https://society-rse.org/about/history).
Since then the RSE movement has expanded around the world, with the [International Council of RSE Associations](https://researchsoftware.org/council.html) overseeing formal collaboration between national RSE associations.
The RSE movement is a largely volunteer-driven effort to help RSEs understand their unique roles and capabilities, and help academia establish better career pathways and recognition for the work RSEs do.

(cl-infrastructure-rse-role)=
## What do Research Software Engineers do? 
As already mentioned, RSEs can come from a wide range of backgrounds.
It is important to mention, however, that the overarching characteristic element of all RSEs is that the output of their research is not papers, but software and toolboxes (which might be accompanied by an overview paper or published manual).
Thus, an important step to allow the acknowledgement of research software work  has been setting up policies that allow the assignment of DOIs for dataset and software for example by the FFORCE11 Software Citation Working Group  {cite:ps}`smith2016software,Cohen2021FourPillars`.
The challenges that are created by shifting the focus of output of research away from the traditional research output will be discussed later. 

https://ieeexplore.ieee.org/abstract/document/8994167



Additionally, RSEs can also be PIs and run their own independent research projects, depending on the institution and policies of the projects they are working on. 

## Who are Research Software Engineers?

The term "research software engineer" is meant to be broad and inclusive, and people discover RSE roles from a variety of entry points.
RSEs usually come from either a domain science background, a pure computer science background, or industry experience as a software developer {cite:ps}`Cosden2022RSECareers`.
These different backgrounds each bring their own advantages and challenges, making every RSE journey unique!
You can find out more about the diversity of RSE backgrounds and experiences through the latest [RSE International Survey (2022)](https://softwaresaved.github.io/international-survey-2022/).

## What qualifications or skills do you need to be a Research Software Engineer? 
RSEs are usually able to program -- from the latest RSE International Survey, the top five languages used by RSEs are Python, C++, R, JavaScript, and SQL.
RSEs are also likely to understand concepts such as agile development, integration and testing, software architecture, and version control. 
Most importantly, RSEs apply these skills to academic research, creating and promoting computerized approaches to make research more efficient and reproducible.
This means that RSEs need to have (and will develop!) excellent communication skills as they bridge the gaps between academia, software engineering, and research infrastructure maintenance.

## Challenges for Research Software Engineers
* Lack of formal pathways for development
* Production of software and tools not always recognised as a research output 
* RSEs not viewed as researchers in their own right
* Adjusting to working on different projects, possibly far from their original background 

## Benefits of having Research Software Engineers
* Highly technical skills that support researchers who cannot program
* Sharing of best practices in research software engineering across projects 
* Apply cross-disciplinary knowledge to different projects 
* Software will be more reliable and robust, supporting reuse and reproducibility 

(cl-infrastructure-rse-support)=
## Organisations and Resources for Research Software Engineers
* [Research Software Engineers International](https://researchsoftware.org)
    * Maintains a [list of links to national or multinational RSE associations](https://researchsoftware.org/assoc.html)
* [Research Software Alliance](https://www.researchsoft.org)
    * Open Slack channel and links to [resources](https://www.researchsoft.org/resa-resources/) and [guidelines](https://www.researchsoft.org/guidelines/)
* [Software Sustainability Institute](https://www.software.ac.uk/)
* [Research Software Engineers' GitHub Organization](https://rseng.github.io/) is a GitHub repository dedicated to cool RSE projects, such as a [glossary of RSE terms](https://rseng.github.io/rse-glossary/)
* [Research Computing Teams](https://www.researchcomputingteams.org/) is a helpful newsletter.

(cl-infrastructure-rse-summary)=
## Summary
Research Software Engineers are highly skilled, valuable members of any research group that is conducting computational research.
They bring technical programming skills as well as best practices from software architecture and open source development to academic research. 
Some also conduct their own independent research projects. 




<!-- 
> See the [style guide](https://the-turing-way.netlify.app/community-handbook/style/style-crossref.html) for The Turing Way's recommendations on cross referencing.
> To include an image in your writing, use the MyST directive shown below. 
> Remember to add your image to the `figures` [folder](https://github.com/alan-turing-institute/the-turing-way/tree/main/book/website/figures) and use the correct path, else it will not be displayed.

```{figure} ../../figures/image-name.png
---
name: image-name
alt: describe your image for readers who rely on screen readers
---
Your image caption here
```

> To include code blocks, simply enclose your code in three sets of backticks shown below.

```
def simple_function():
    pass
```

> To include an admonition or to highlight a block of text that exists slightly apart from the narrative of your section, use the directive shown below. Jupyter Book's [documentation](https://jupyterbook.org/content/content-blocks.html#) has other useful examples.

```{note}
Here is a note!
```




<!-- IMPORTANT!

- Use this template to create your chapter's subchapters.
- Refrain from writing very long subchapters as readers may be unwilling to read them. Rather, you should split long subchapters into smaller subchapters if necessary.



BEFORE YOU GO

- Have a look at the Style Guide and the Maintaining Consistency chapters to ensure that you have followed the relevant recommendations on
  - Avoiding HTML
  - Consecutive headers
  - Labels and cross referencing
  - Using images
  - Latin abbreviations
  - References and citations
  - Title casing
  - Matching headers with reference in table of content

-->
