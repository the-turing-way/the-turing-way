---
breaks: false
---

(rr-open-hardware)=
# What is Open Source Hardware (OSH)?

<!-- Can we have some criteria for writing?
- It was agreed to aim for a total of 3000 words
- If we show project examples they should have a DO to ensure their persistence.
- Use foundational references such as OSWHA DIN
- Is the goal to provide a summary of open hardware so that readers can start discovery open hardware.
 -->
 
## Definition

<!-- Is a short opener needed on open source movement in general as the chapter is probably situated after free and open source software? E.g. Open source hardware  -->

“Open source hardware” refers to the design specifications of a physical object that are licenced such that they and the object can be studied, modified, created, and distributed by anyone. 
Its formal definition [{term}`def<Open Source Hardware>`] was written by the open hardware community back in 2010, and is maintained by the [Open Source Hardware Association (OSHWA)](https://oshwa.org), a US-based non-profit. 

Translations of *hardware* in some languages may bias the concept towards electronics, but with *hardware* we refer to any physical, tangible object: machines, electronic devices, biomaterials, textiles. You will also often see the terms *open hardware* and *open source hardware* used interchangeably. 




<!-- 
JC: I would put that away, I included link to oshwa, I think that is enough:
This definition was written by the open hardware community back in 2010. It is maintained by the [Open Source Hardware Association (OSHWA)](https://oshwa.org), a US-based non-profit that also hosts the annual [Open Hardware Summit](https://2023.oshwa.org/) and runs the [Open Source Hardware certification program](https://certification.oshwa.org/). 


-->

## OSH in Research 


In 2016, the [Global Open Science Hardware](https://openhardware.science) community took the OSHWA definition and tailored it to the specific needs of science:

> Open Science Hardware (OscH) refers to any piece of hardware used for scientific investigations that can be obtained, assembled, used, studied, modified, shared, and sold by anyone. This includes standard lab equipment as well as auxiliary materials, such as sensors, biological reagents, analog and digital electronic components.

In 2021, the [UNESCO Open Science Recommendation](https://en.unesco.org/science-sustainable-future/open-science/recommendation) became the first policy document to include OSH as a component of open science.
The recommendation considers open hardware as a pillar of scientific knowledge that should be open.

<a href="https://unesdoc.unesco.org/ark:/48223/pf0000379949.locale=en">
    <img src="https://creativecommons.org/wp-content/uploads/2021/11/UNESCO-Open-Science-circle-768x979.png" width=50%>
</a>

## What is the source of open source hardware?

Like open source software, the “source code” for open hardware is available for modification or enhancement by anyone.
In contrast to software, where the source is plain text code, the OSH source is more complex. 
OSH design information refers to: 
schematics, blueprints, logic designs, Computer Aided Design (CAD) drawings or files, and the like (see ref-technicaldocumentation).
It usually entails text, binary files and software.

Importantly, OSH projects should share both raw and derived source files.
For instance, 3D object designs should be shared as print-ready files (.stl), but also as modifyable 3D objects (the format of these files will depend on the software used). 
The raw files are necessary to allow modification, but can often only be opened in proprietary sotware, and their use require specific skills.
The derived versions are used to build the hardware, but often make modification difficult.
Users with access to the tools that can read and manipulate these raw source files can update and improve the physical device. 
If they wish, they can proceed to share such modifications.



Although OSH projects are diverse in their degree of "openness", best practices in OSH guide us to identify a core, minimum documentation that needs to be in place so others can study, modify, distribute, make or sell our hardware.
We will go through these various components in the following sections. 



<!-- include DIN SPEC?-->
<!-- (Julieta) I think I'd mention it in the how to share, or some section about standards -->

<!-- Nico M.: I may be able to throw some words here about the "openness gradient" meaning how the word "open" is used to describe projects that are very different in terms of openness (in terms of hardware, associated software, community building, the documentation's coverage and audience, community support, "official" support, etc.). -->

## Types and phases of open source hardware 

OSH projects emerge as **a response to a concrete need**. 
For example, you may need to process lots of samples, or to measure a parameter you were not considering before, or to take measurements outside of the lab. 
With the analysing of your need, your OSH project starts.
It is advisable to scope the project at this point (see project scope chapter, In preparation).
It may indeed be usefull to draw a roadmap, look and find future users, contributors and manufacturers (who may have complementary skills to yours), and decide for a license.
It is reasonable to invest quite a lot of time in looking for similar projects.
OSH are often difficult to find and comprehend, but finding projects may save you a lot of time and hassle.
Indeed, you may learn a lot about your needs, refine your ideas, and may even find collaborators while browsing existing OSH projects.



 
<!---
Today you can easily learn online how to design your first hardware project! Projects like Arduino or RaspberryPi have lowered access barriers to prototyping electronics, there's better free/open source software for hardware design, and electronic components are also more accessible.
--->
You may then look and test some ideas  to address your particular need, a process called **prototyping**.
After many iterations and testing, you will be able to select a prototype for further development.
The design that solves your need but is not yet complete nor stable is called a **demonstrator**.  
When the design and documentation is polished and can be taken up by hardware producers, the hardware is usually labeled as a **market-ready product**.

While many people start generating **documentation** and share their design online at the demonstrator stage, open science enthusiasts advise to be open from the beginning of the phase of the description of the needs.


There are different degree in how open an OSH project can be (ref paper roberthttps://www.sciencedirect.com/science/article/pii/S2212827118312095 ), but every step in the right direction is welcome and an opportunity for better research and new career path.
Designs that are well-documented and offer a solution to a concrete problem can be easily **reused** by others.
They may **replicate** your design exactly to test it, or **reproduce** it to adapt it to their particular need. 
It is worth thinking about your future self as one of the project collaborators when balancing the resources used in opening and documenting an OSH project, and the resources used to develop the hardware further.
 



<!---
:::info
<<can someone add the comment on the degrees of openness here? Maybe Nico?>> 
 

<< Nico says glad to help and wrote something up \/ >>
:::

As an open hardware developer, you will also choose how thorough the documentation of your project will be. This choice translates directly to a certain *degree* of openness and, thus, impact and reproducibility.

There is an implicit equilibrium between the resources assigned to writing documentation, or to developing new features. Minimal documentation is essential to broaden the project's audience (e.g. from just you to a small crowd), while features are essential to achieve function.

Users and contributors will also appreciate knowing on what part of the openness spectrum the project lies: *between a cold black-box and a bright, colorful rainbow.*

Your project can win openness points by working on several aspects of open source, which are outlined in the following sections, and meant to further the well known pillars of open source: the freedom to study, modify, make and distribute.


--->
**Scriberia picture**

# Why should you use or develop open source hardware?

## For you

People develop and share OSH for a variety of reasons. Particularly in research, OSH provides very concrete advantages:

- Flexibility and Speed: you can quickly customize and combine open designs to test new research questions in an accessible way, instead of depending on vendors, their timelines and bureaucracy.

- Simplicity: As OSH has a lower price tag than conventional equipment, it is much easier to obtain while bypassing the bureaucracy of contracting vendors.


- Control: if a supplier goes out of business, users and/or third party companies have the information to keep systems running. 

- Visibility: researchers and engineers developing OSH make their work more visible. They also increase opportunities for networking and impact,especially in project involving a community.

- Education: By using open hardware, researchers pick new skills and fully understand how a certain tool captures data on specific phenomena/events.


> It is worth mentioning here that building and developing OSH may require  specific knowledge and skills on one hand, and  quite a lot of time,on the other hand.
> Buying industrial hardware with their support may be cheaper, especially if you do not have enough technical support. 

<!--
 [name=Julieta Arancio]  The only caveat is that we're talking about prototypes and not products, which won't be cheaper once marketing, UX, tech support work is factored in.
-->

## For science

- Quality: to make science, we need research instruments; we also need to build on top of others' knowledge. A contributor might offer a totally novel solution to a design problem that would never occur to you; contributors may also catch errors that you’ve missed. 

- Reproducibility: OSH designs can be replicated, allowing for verification and reproduction of experiments and data. Moreover, users can have much better control on the calibration of their devices, boosting replicability even further.

- Inclusiveness: OSH can make science possible where resources are scarce. Local adaptation and production of OSH helps reducing the impact of import restrictions and bureaucracies that obstaculise science. Also, more students may be able to interact with scientific tools in hands-on sessions, as the equipment is cheaper.

- Sustainability: OSH means you have all the information for repairing and maintaining devices locally, extending the lifespan of the product and reducing waste. 


Many researchers who develop or use OSH for research also value OSH as an educational tool.
Working with OSH designs allows students and researchers to fully understand how a certain tool captures data on specific phenomena/events.
<!--
This part is included in inclusiveness?

Moreover, as the cost of OSH is often lower than proprietary equipment, more students are able to interact with scientific tools in hands-on sessions, performing experiments similar to in-real-life scenarios.
-->




# How to make hardware open source
<!--- short introduction, what is the minimal requirements are, and why does this chapter conist of Project documentation and technical documentation --->

In order to make your hardware reusable and modifyable by others, its source should be shared with an appropriate license.
This is usually done via specific online platforms.
The type and amount of shared content depends on the complexity of the OSH, and on the importance of the community aspects of the project.

In the following sections, you can find descriptions of the common types of content that you should consider sharing as project documentation, technical documentation, and community interactions.
You are not required to post or document them all, but the more you share, the more the community benefits, and the more it can give back.


There is a lot of crossover with files to include in open source software projects. 
(see {ref}`rr-rdm-metadata-documentation`)



:::info
*/// Nico: I propose to move these paragraphs over here, up from tech docs.*
There are two essential types of published source files associated to an OSH project:

- **Design files** with parts metadata, typically including the manufacturing process, the materials (with dimensions, mass, and units), suppliers, etc.
    - A functional overview of the project's parts or modules can also be included. This will help manufacturers and makers adapt the project to other contexts (e.g. where different parts or budgets are available).
    - Ideally, your OSH project has been designed using free and [open source software tools](https://opentoolchain.org/tools/), to maximize the ability of others to view and edit it. It is essential to share these original design files, in both original and accessible ready-to-view formats.
    - The type of parts can also be mentioned with unambiguous reference, between, custom parts (e.g. developed as a result of this or another project), off-the-shelf parts (e.g. screws) or <!--proprietary--> integrated modules (e.g. a single board computer). 
-  **Software and firmware**. You should share any code or firmware required to operate your hardware. This will allow others to use the machine, customize both to their specific need, and reproduce reserach results.
    -  Document the process of building the software, including links to dependencies (for example, third-party libraries or tools), and versions of each program.
    -  In addition, it is helpful to provide an overview of the state of the software (for example, “stable” or “beta” or “barely-working hack”).
    -  Note that the software and its documentation should be distributed under an appropriate licence.
:::

## Project documentation

Your open source hardware project should include a general description of the hardware’s identity and purpose, written as much as possible for a general audience.
That is, explain what the project is and what it is for before you get into the technical details.
And add a proper license.

On top of what is mentioned in detail in the open source project documentation page ({ref}`pd-overview-repro`) for project plan, people involved, and contribution process, 
you should specifically **think about your audience** when writing OSH documentation.
Indeed,
your project might be reused by people with different skills, roles, objectives, and socio-economic and cultural environments.
Because of this it can be useful to create a **list of skills** that are required to build or use the hardware.
Someone trying to build it from scratch, for example, will require specific set of prior knowledge, skills, and tools.
A different set is needed to perform maintenance tasks.
An end user operating the assembled project might require an entirely distinct skillset (and documentation).

Take particular care about safety instructions. OSH makers are not always trained engineer and may not recognize dangerous from safe manipulations.

<!-- 
moving to project doc page of the book

Your OSH project should at a minimum provide a license together with a README file with all the basic, general information a newcomer needs to get oriented. It should contain a **recognizable name** for your project, as well as a **declaration of the licensing terms** under which it may be distributed (see the {ref}`OH_licences` chapter). Furthermore, it helps to include the **current state**, **ongoing development**, and/or any **future plans** for the project.

In addition to the above, it is interesting to document the *principal need* for your project. That includes a **problem description** of whatever issue sparked the project, a **functional description** of how your project is meant to address it, and a **context description** of the users and environment your project is targeting. The context description should include an estimation of the overall required budget and build time, and also make it clear what your project is not meant to be.

Your project should also include a **list of contributors**, **contribution guidelines**, and information on **contact points** where to ask for help. You should also include an index of all the project's documentation, so people can easily find what they are looking for. In order to make your project discoverable, you may add a machine-readable metadata file, such as an [Open-Know-How manifest](https://www.internetofproduction.org/openknowhow).

You should also **think about your audience** when writing documentation. Your project might be reused by people with different skills, roles, objectives, and socio-economic and cultural environments. Because of this it can be useful to create a **list of skills** that the project requires. Someone trying to build it from scratch, for example, will require specific set of prior knowledge, skills, and tools. A different set is needed to perform maintenance tasks. An end user operating the assembled project might require an entirely distinct skillset.

Common types of documentation, their audiences, and content suggestions are summarized in the table below.

<!--  
## ⚠️ (Sacha, Moritz, Nico M.) TODO next week (Sacha)

:::info
/// Nico: I've redacted the contents a bit. The table is hard to edit in this format. Let me paste the link again: https://docs.google.com/spreadsheets/d/1JYgMqKapGX7TDFkFo0ZeGXGMx-m2-svK-o4p6NKt1Ns/edit#gid=564457047
:::

| Documentation item | Audience | Content | Location |
| -------- | -------- | -------- | -------- |
|Project overview| General community| Project definition, scope, audience, licensing, and directions to more specialized documentation. Expectation management: state what information is missing and main caveats. | Front page, README.md| 
|Communication| General community| Links to communication channels: support platforms (e.g. forum, issues at an online repository), online community platforms (e.g. forums, chats, etc.), direct contact information, dates for joining in-person or online events. | Front page, README.md| 
|Contributions| General community| Description of the process of getting involved. List of possible contributions: donations, investments, beta testing, feature development, collaborations, reporting issues. | Contributions page, CONTRIBUTING.md| 
|Usage| Users| Intended usage instructions, limitations, other use cases. Troubleshooting. Links to learning resources, maintenance and assembly guides. | Usage guide| 
|Assembly| Manufacturers, Users | Complete description of: the assembly process, used parts, required knowledge, training, number of people, time, and tools. Links to learning resources. | Assembly guide| 
|Maintenance| Technical support, Users| Instructions for manintenance operations, stating frequency, tested replacement parts, alternatives, and the required skills. List of maintenance services and learning resources. | Maintenance guide| 
|Design | Developers, Contributors, Educators| Description of the overall design rationale. List of the main design choices and implications (e.g. functional compromises). Minimal explanation of the working principles, and links to external learning resources. | Development page, DEVELOPMENT.md| 
|Technical contributions| Manufacturers, Developers, Technical support| Development roadmap, guidelines, core team and contributors, communication channels, version control system, related works. Description of the typical contribution process. Examples of (un)successful contribution processes. | Contributions page, CONTRIBUTING.md| 
|Development| Developers| Development tools (e.g. IDEs, EDA, or CAD software) and style guidelines. Setup for development and testing. Detailed overview of the hardware modules and software. Specifications of the internal and external hardware interfaces. Tutorials and examples of how to get started. | Development page, DEVELOPMENT.md| 

-->



<!--
I also just found out about the open-o-meter, which can be used as a reference, and greatly reduce the contents below to a simplified table: https://www.sciencedirect.com/science/article/pii/S2212827118312095

Maybe we can build from this table, but we should perhaps rather summarise all the contents we explained in the previous sections in a synthetic table, what do you think? (SH) Great! (NM)-->

## Technical documents

Technical documents provide the source needed to study and replicate a hardware design.
In contrast to project documentation and community building, technical documents for OSH are quite specific, but can be considered analogous to what source code is for software.
Depending on the project technical documents may include technical drawings, images describing electronic schematics, computer-aided design ([CAD](https://en.wikipedia.org/wiki/Computer-aided_design)) files, or assembly instructions to replicate the design. A thoroughly documented project will have all types of documents.
It may also include code (firmware and software) necessary to run the hardware.
The source files (e.g. CAD files) are best accompanied by textual and multi-medial documentation, such as guides for manufacturing, assembly, maintenance, and development.

<!--I mean to argue in favor of describing the "learning path" required to study the project. I would argue that for hardware this can be more important than the source if you have access to the equipment (except for packaged ICs, which are naturally highly obfuscated). SH: do we develop this here?
-->

<!-- A note on scope of documentation. Technical documentation also reflects aspects of projects such as a project maturity, complexity, intention of authors on how it should be used and technical specifications. -->

<!-- Maybe we can have examples of low complex projects vs high complex projects.
Nico M.: Yes! This would be great. The minimal documentation for a pair of pliers is not the same as a microscope. There are differences in complexity over several levels.
-->

<!--
:::info

/// Nico: I've copied and redacted the 2 source files items up to the main heading of this section. My read is that there is a mix here between "source" and "documentation", which confuses me a bit.

We may se physical hardware as the compiled desgin files, but in the code analogy those are not automatically documentation by themselves.

I propose we move them and delete the ones down here.
:::
-->

We provide here a quite exhaustive list of documentation elements.
Your project may not need all of them, but it is worth considering having at least minimal information for most of these elements:

- A **context description** which may reflects project maturity, complexity, the intentions of authors on how it should be used, and technical specifications. It may include standards compliance (the [DIN-SPEC](https://gitlab.com/OSEGermany/OHS-3105) standard for instance) and an estimation of the overall required budget and build time.

- A **Bill of Materials** (BOM): a list or spreadsheet describing part numbers, putative suppliers, costs, and a short description. Make it easy to tell which item in the bill of materials corresponds to which component in your design files: use matching reference designators in both places, provide a diagram indicating which part goes where, or otherwise explain the correspondence.

- **Assembly instructions**. To help others make and modify your hardware design, you should provide instructions for going from your design files to the working physical hardware. It is good to publish annotated photographs (or video) from multiple viewpoints and at various stages of assembly. If you do not have photos, posting annotated 3D renderings of your design is a good alternative. Either way, it is good to provide captions or text that explain what is shown in each image and why it is useful.
    - **Manufacturing instructions**: The manufacturing process of parts that have been made for this project should be documented as well. This is specially important if they are available for purchase from only a handful of small/medium businesses.

- A **list of required tools** and associated settings, for both software used for development, and machine tools for replication.

- **Design files** with parts metadata, typically including the manufacturing process, the materials with dimensions, mass, and units. A functional overview of the project's parts/modules can also be included. Ideally, your OSH project would be designed using a free and open source software application, to maximize the ability of others to view and edit it. It is essential to share these original design files, in both original and accessible ready-to-view formats. The type of parts can also be mentionned with unambiguous reference, between, custom parts (e.g. developed as a result of this or another project), off-the-shelf parts (e.g. screws) or <!--proprietary--> complex modules (e.g. a single board computer). 

-  **Software and firmware**. You should share any code or firmware required to operate your hardware. This will allow others to use it with their hardware or modify it along with their modifications to your hardware. Document the process required to build your software, including links to any dependencies (for example, third-party libraries or tools). In addition, it is helpful to provide an overview of the state of the software (for example, “stable” or “beta” or “barely-working hack”). 

- **Instructions for operation and maintenance**. Describe how hardware users should operate the hardware (for example how to calibrate and test it). Indicate any maintenance that should be done to secure a good functionality of the hardware.

- **Repair and disposal**. Indicate where or how the hardware can be repaired, and indicate how to dispose or recycle the hardware if it is beyond repair.

> Note that producing documentation-quality pictures consistently requires adequate tools and setup.


## Building community in open source hardware 
<!--
:::info
This section is quite long at the moment, would appreciate to have more context on the goals, the audience and what are we going after. 

some of this may come to a different part of the book. I copied it to
https://hackmd.io/shSc84_-Tu2OUP3jX_UFhQ

see
https://github.com/alan-turing-institute/the-turing-way/issues/3131
:::
 Some ideas behind the writing:
If a hardware design serves properly a user, which may well include the author in the first place, that is a first start. Community building shouldnt be a goal on its own but rather a result of a social validation that a certain design and project is relevant for a critical mass of users and beneficiaries.

Help wanted:
- If you know of good references on this subject we can cite, scholarly literature, etc it would be great to insert or refer to in the text.
- Any criteria on to define the scope of this section, as its been developed a bit freely and without an approach or style in mind. 

-->

OSH communities comes in all sizes and forms.
They often develop around people facing similar needs who realise they will get "something that none of [them] could have developed alone." (Interview: White rabbit, by the Open make team, Javier Serrano and Amanda Diez Frenandez.)
We should therefore consider that by simply developing good quality hardware and making it open source already entails an important aspect of community building.

In the following section, we share some consideration about community building for OSH project.
You may want to refer to the {ref}`collaboration<cl>`  and {ref}`cl-new-community`  guide of the turing way book for a more detailed description of certain aspects such as practices, metrics, behaviors and observables that can be related to thriving communities.


### Considerations for OSH community building

While scoping your project (ref scoping chapter in preparation), it is well advised to think about the different people who may engage with your OSH (see {ref}`cl-stakeholder-mapping`)
Different OSH projects have included different partners at varying stages of their developement.
On top of user and contributor roles that OSH have in common with open source software, local or global hardware manufacturers may become important partners of your project.
You may also think early about the people who will eventually have to maintain and repair the hardware.
To make it easier for them, it also helps to make your hardware designs modular (splitting your hardware in modules which may have alternative designs).
Anoter specificity of hardware may be the importance of the creation of replication tutorials, workshops, seminars, or training material, which can impact the adoption of hardware designs.
This is particularly relevant if the OSH is meant to be produced in Do-It-Yourself environments or as a teaching opportunity.

Importantly, it is important to decide whether, when and where you want to engage with or build one community.
Most OSH communities are local in comparison to open source software project.
You may not have the time or skills to build a community, and your project may not need a community to flourish.
Always be honest with your collaborators and yourself about what support they can expect.
The [GOSH forum](https://forum.openhardware.science) has been an enabler for finding collaborators for OSH and OSH-related projects.



```{note}
Engineers is still a world full of tech-bros, who got irritated when one does not understand their jargon, and are not very welcoming with beginners and women. 

It is therefore particularly important to Valuing Diversity and Differences in OSH {ref}`cl-new-community-difference`

```


## Bonus Section: Learning from community roadblocks


- It is better to keep an open attitude towards diversification and unstable features, and this does not need to be in conflict with the main project being conservative.
- There should always be space for "extensions" and "plugins" to be seeded and grow in the same community as the main project. 3rd-party plugins should be labeled as "external and unsupported by maniline development" but still encouraged.
- It is good practice to build modular and extensible hardware, with documented interfaces, to be able to grow a developer community.
- It is a bad idea to respond to a request for help with the following: "It is 'open source', if you want that to happen, you are free to work on it in your own time". Be honest of what you can do, but do not be a jerk. 
- If the upstream developers do not have time to write enough documentation, or do not have time to review pull requests, this fact should be stated to avoid generating false expectations.
- Be ready to delegate (or create new spaces) if you are overwhelmed by a fast-growing community. Otherwise, small projects will stall, the community will be frustrated, and then become fragmented. 


# Sharing open source hardware
One of the goals of making OSH is to share the documentation so others can reuse your project (build upon, improve, derive from). Once a project is shared, it can be continuously developed and manintained. 


For OSH to be effectively adopted, reused, and developed further, the hardware documentation and other relevant information needs to be shared in a way that is easily accessible at no cost.
The global open hardware community utilizes a variety of platforms and online resources to share their work and enable others to collborate on different projects.
The details on the some of the platforms used and their efficay is in the "platforms" section below. 

## Platforms

The easiest way to share an open hardware project is pushing it online.
There is no best platform or place to do this, as it depends on the specifics of your project.
However, some platforms commonly used for OSH are [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), [Wikifactory](https://wikifactory.com/) and [hackaday.io](https://hackaday.io/).
Please refer to {ref}`cl-github-novice`for an introduction to GitHub and GitLab.
Some hardware project have large files, and one may need to look for platform and workflows allowing to work with big files (see chapter on version control for data).


## Making hardware discoverable


There is (yet) no straightforward ways to let others to know about your project online. 
Here we list some actions you may take in order to 
makes your project more visible, reach more people, and improves the changes of reproducability:

1. Use a commonly used platforms, often they have a discovery page and people expect your project to be on such platforms.
2. Use metadata to discribe your project, apart from just your technical data it is also important to share the metadata of your project, for example a short disciption, a statement of the license, the context of your project. Addding a [Open-Know-How manifest](https://www.internetofproduction.org/openknowhow) yaml file may help.
3. Refer to the guide for communication {ref}`cm-comms-overvie` and make a presskit or media content for others to easily share your project on other blogs or websites.


In academia, researchers may also **publish** their hardware (usually at the demonstrator stage), as peer-reviewed articles and **archive** a version to generate a DOI. 

## Making hardware citable

In contrast to data and software, there is no recommendatation for hardware citation yet.
However, we think it is good practice to treat hardware citation similarly to other research ouptuts {ref}`cm-citable`.
Making open hardware citable is indeed useful for academic and research output.
The use of archives that can assign persistent identifiers (DOI) can help to guarantee specific versions/releases of the hardware project available over the long term. 
Though within the open hardware community this is not the practice, it would be beneficial to adopt going forward. For research to be reproducible, long term archiving through a platform that is dedicated to it would be necessary.

[Zenodo](https://zenodo.org/) is a good example of the type of archive that can issue a persistent identifier like a DOI.
Zenodo also has an integration with Github such that projects that are shared and developed there can be archived with ease and a DOI obtained for a specifc version/release. 


## Open source hardware licencing

OSH are not open without a license.
Without license, others cannot legally use, copy, distribute, or modify that project
The situation of license for hardware is a bit more complex than for sofware as there are some cases where patent law and not copyright law will apply. 
Also note that you may use different licenses for different part of the project.
In particular, you may use a software license for code, and a creative commons license for the test and video documentation.
Please refer to the license for hardware part of the turing way book ({ref}`OH_licences` ), and its disclaimer.

Common OSH license are:

[TAPR](https://tapr.org/the-tapr-open-hardware-license/) Similar to GNU GPL 3.0, [SOLDERPAD](http://solderpad.org/) Similar to Apache License 2.0, [CERN-OHL 2](https://ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2) which comes as: CERN-OHL-S (Strongly reciprocal), CERN-OHL-W (Weakly reciprocal), CERN-OHL-P (Permissive).

# References/glossary


Bonvoisin, Jérémy, Jenny Molloy, Martin Haeuer, and Tobias Wenzel. “Standardisation of Practices in Open Source Hardware.” Journal of Open Hardware 4, no. 1 (August 19, 2020): 2. https://doi.org/10.5334/joh.22.

This Chapter of the book was created reusing the following documents:

- Open Hardware Academy: https://www.openhardware.academy/03_Lessons.html
- Open Hardware Makers: https://curriculum.openhardware.space/
- UKRN primer on open science hardware 
