(rr-rdm-smp)=
# Software Management Plan
## Introduction
A Software Management Plan (SMP), similar to a [](#rr-rdm-dmp), is a document that describes how your software will be generated, used and shared during and after your project.
And similar to a DMP, an SMP is a living document, which should be updated throughout the research project as needed.

According to {cite:ps}`Grossmann2024smp`, a SMP is:

> an instrument to collect ideas and information necessary for [researchers] programming activity, which helps [researchers] gain awareness and provide for the necessary resources. 
> Such an instrument can be an SMP, which aims to collect all information relevant for the software development in a scientific context to support a structured approach or help distributed teams to adhere to (self-) defined standards.
> 
> A Software Management Plan (SMP) contains general and technical information about the software project, information on quality assurance, release and public availability as well as legal and ethical aspects that affect the software. 
> The SMP summarises information that adequately describes and documents the creation, documentation, storage, versioning, licensing, archiving and/or publication of the software created or used in a project. 
> Associated hardware and other necessary resources, as well as other associated software and software libraries, text and data publications must also be described and are a special feature of the SMP.
> The purpose of an SMP is initially to support the traceability and, if necessary, the longterm usability of the software (for direct application as well as for further processing) and to facilitate user support in the event of queries. 
> The SMP therefore also serves the purpose of quality assurance.
> The SMP can be linked to one or more DMPs if the software is used for data generation or processing. 
> SMP and DMP can be summarised as output plans.

One important thing to say in this context is that software includes a wide range of things: from analysis code used by only one researcher to software libraries with many users.
See [](#rr-rdm-smp-what-software) for more details.

Here is [a good introduction to SMPs](https://tu-delft-dcc.github.io/docs/software/fair_software/software_management_plan.html).

### What is it?
An SMP is a document which describes how a specific software project will be developed and maintained, and over what period of time.
It describes, for example, how the software will manage [version control](#rr-vcs), how it will be [licensed](#rr-licensing-floss), how it will manage [license compatibility](#rr-licensing-compatibility), and so on.

More than a document, a SMP should be a way for developers of research software to reflect on their process, their choices more explicit, and consider what options are available to them.
Ideally, this reflection should happen early on in the development process, and should be revised and updated on a regular basis.

### How can they benefit your research?
An SMP can help the developers of research software make explicit their intentions and choices on how they will manage their software project.
If you plan on sharing your code, it will help you ensure that your code is reusable by others.

(rr-rdm-smp-what-software)=
### What software to manage?
Some researchers say they do not create any software, they only write one-off scripts to analyse data.
These scripts, short as they may be, are still software.
The Australian [National Agenda for Research Software](https://ardc.edu.au/project/research-software-agenda-for-australia/) proposes different categories of research software: analysis code, prototype tools, infrastructure software.
The key point is that SMPs apply to research software across this spectrum, although it may apply differently depending on the needs of the software.

[Defining the roles of research software (Version 2)](https://doi.org/10.54900/xdh2x-kj281) provides a different view of the different categories of research software.
The common thread with these different interpretations is that not all software is created under the same circumstances.
The context of the software is important to understand how it should be managed.

The [Practical guide to Software Management Plans](https://doi.org/10.5281/zenodo.7038280) provides a collection of optional requirements to be included in an SMP.
From these requirements "Purpose" is recommended as a starting point, and should always be there: software should always be made with a purpose in mind, and its purpose determines its management level.

(rr-rdm-smp-when)=
### When to write an SMP?
Ideally, a SMP should be drafted during the planning phase of your research project, alongside your DMP. 
Some funders (for example NWO, ZonMw, the Netherlands eScience Center) require an SMP as part of your grant application.

- Find out if your institution has its own Software Management Plan template, if so, use it
- If not, determine the management level of your software
- Use the SMP template appropriate to your software

An SMP is a living document.
As such, it should be updated on a regular basis.
For example, when you release major versions of your software.

(rr-rdm-smp-templates)=
## Existing SMP templates

- [SSI Checklist for a Software Management Plan](https://doi.org/10.5281/zenodo.1422656)
- [Netherlands eScience Center Software Sustainability Protocol](https://doi.org/10.5281/zenodo.1451750)
- [ELIXIR Software Management Plan for Life Sciences](https://doi.org/10.37044/osf.io/k8znb)
- [Checklists for different types of software](https://gitlab.com/HDBI/data-management/checklists/)
- [WUR SMP template and guidance](https://doi.org/10.5281/zenodo.10473646)

(rr-rdm-smp-tools)=
## SMP tools

- [SMP decision tree](https://smp.research.software/)

## Additional Resources

- [Self-study materials on SMPs](https://esciencecenter-digital-skills.github.io/research-software-support/modules/softwaremanagementplans/slides-smp)
- [TU Delft Library ‘Navigating Research Data and Software: A Practical Guide for PhD Supervisors’ 2025](https://www.youtube.com/watch?v=5Zy3l4dTJd4)
- [Recommendations for Developing and Aligning Policies on Research Software](https://doi.org/10.5281/zenodo.13740998)
- @Grossmann2024smp
