# [Blog: The Turing Way: An open source resource promoting best practice for reproducible research](https://www.software.ac.uk/blog/2019-03-05-turing-way-open-source-resource-promoting-best-practice-reproducible-research)

By [Becky Arnold](https://software.ac.uk/about/fellows/becky-arnold?_ga=2.183212641.611590810.1551866598-1336468516.1531506806), [University of Sheffield](https://www.sheffield.ac.uk/), with additional material by [Rosie Higman](https://rosiehigman.wordpress.com/), [University of Manchester](https://www.manchester.ac.uk/)

[The Turing Way](https://www.turing.ac.uk/research/research-projects/turing-way-handbook-reproducible-data-science) is a project [funded](https://www.turing.ac.uk/news/alan-turing-institute-spearhead-new-cutting-edge-data-science-and-artificial-intelligence) as part of UKRI’s Strategic Priorities fund. It aims to help researchers and RSEs improve the reproducibility of their research. It has three main components:

- An open source textbook [hosted on GitHub](https://github.com/alan-turing-institute/the-turing-way) providing guidance on best practice for reproducible research
- Case studies of reproducible research
- Workshops teaching researchers and RSEs to use tools to make their work more reproducible

If you want to be kept up to date with the project’s progress, you can [sign up](https://tinyletter.com/TuringWay) to the project’s newsletter. Myself and a lot of the [team](https://github.com/alan-turing-institute/the-turing-way/blob/main/ways_of_working.md) will also be at the [Collaborations Workshop](https://www.software.ac.uk/cw19) 2019 to discuss the project if you’re there and want to chat.

## A Curated, Open Textbook

There are a lot of fantastic open source resources available providing tutorials and discussions related to practically every facet of reproducible research. However these materials are not centralised or integrated, but scattered across the web. The goal of the textbook is not to spend time reinventing the wheel by writing more, but to synthesise materials that already exist into the form of an open-source textbook covering topics such as

- Why research reproducibility matters and how to define it ([ready for community feedback](https://github.com/alan-turing-institute/the-turing-way/blob/main/chapters/reproducibility.md))
- Version control ([ready for community feedback](https://github.com/alan-turing-institute/the-turing-way/blob/main/chapters/version_control.md))
- Open research ([ready for community feedback](https://github.com/alan-turing-institute/the-turing-way/blob/main/chapters/open_research.md))
- Sustainable research data management (in progress)
- Testing (in progress)
- Reproducible computational environments (in progress)
- Continuous integration (in progress)
- Continuous analysis (in progress)
- Reproducibility with [interactive notebooks](https://jupyter.org/) (community help wanted)
- Good coding practice (community help wanted)
- Reproducibility with Deep Learning (community help wanted)

Fundamentally this is an open project so everyone is encouraged to get involved! Whether that’s by making improvements to already complete chapters, writing new ones, reviewing new work, raising issues, or any other contribution it’s welcome and appreciated. We want this to be a living, evolving resource that serves and is supported by the wider community.

## Case Studies of Reproducible Research in Practice

We’re working with several [researchers](https://github.com/alan-turing-institute/ReproducibleResearchResources#announcement-turing-reproducible-research-champions) from the Alan Turing Institute (the Turing reproducible research champions) to reproduce their work, share their experiences and provide case studies of reproducible research in practice. We’re interested in why reproducibility is important to them, how they went about trying to work in a reproducible way, and crucially what advice they would give to their previous selves.   

Once complete, these case studies will be will be interwoven throughout the textbook to demonstrate how theory translates to practice. They will allow readers to follow along with the work of the Turing reproducible research champions as we collaborated with them to overcome challenges including reproducible analysis when using HPC resources, managing and packaging fast-growing projects and sharing workflows built for sensitive data.

If you have tips and tricks, or “gotchas” that caught you out as you tried to make your work reproducible, please share them through [this google form](https://docs.google.com/forms/d/e/1FAIpQLSfcyYH_E03Y5zuBdwrikQP4QldqzKmD-aPngCKthdV9e9alaA/viewform).

## Workshops for Researchers and Research Software Engineers

We’re running some workshops as part of the project. Two (one in Manchester on March 1st and one in [London on March 12th](https://www.eventbrite.co.uk/e/boost-your-research-reproducibility-with-binder-london-registration-55337162944)) was/will be on helping people to boost their research reproducibility with [Binder](https://mybinder.readthedocs.io/en/latest/). Binder is a tool for helping people share code without worrying about the computational environment they're running or installing a long list of requirements.

During these free workshops we discuss reproducible computing environments, show examples of others’ projects in Binder and help you learn how to prepare a binder-ready project. At the end of the workshop you will be able to take some of your own content (in a R or Jupyter notebook, or scripts that can be run in the terminal) and prepare it so that it can be used by others on [myBinder.org](https://mybinder.org/).

This workshop is geared towards people who are:

- Interested in reproducibility, containers, Docker or continuous integration;
- Already familiar with R Markdown or Jupyter notebooks;
- Looking to communicate their research more effectively.

We’ll also be running a workshop on how to build a BinderHub in [Sheffield on March 18th](https://www.eventbrite.co.uk/e/build-a-binderhub-registration-55336756729). Hosting your own [BinderHub](https://binderhub.readthedocs.io/en/latest/) locally allows you to control who has access to code and data and to provide greater computational power. This is not the case in the public Binder instance, [myBinder.org](https://mybinder.org/), which requires all code and data to be fully open, and computational power and data storage is limited.

During this free workshop we will demonstrate how to build your own BinderHub on Microsoft Azure cloud computing resources. We will help you get started with building a BinderHub on your institution's computing platform and discuss the challenges of maintaining a BinderHub. At the end of the workshop you will know why this would be a useful resource for your team, and will know where to look for help and support building your institution's BinderHub.

This workshop is geared towards Research Software Engineers and IT staff who are:

- Interested in reproducibility, containers, Docker or continuous integration;
- Already familiar with Binder and R Markdown or Python for data science;
- Interested in setting up their own local BinderHub.


## See you soon

Working on this project had been fascinating, and it's been a great excuse to set aside time to learn more about a whole host of topics. It’s also given me the opportunity to work with a lot of fantastic [people](https://github.com/alan-turing-institute/the-turing-way/blob/main/humans.md). I hope to see you in the future on [GitHub](https://github.com/alan-turing-institute/the-turing-way) if you have the time to contribute to the project, or even just saying hello in our [gitter chat room](https://gitter.im/alan-turing-institute/the-turing-way).


Useful links:
- GitHub repository: https://github.com/alan-turing-institute/the-turing-way
- Gitter chat room: https://gitter.im/alan-turing-institute/the-turing-way
- Newsletter: https://tinyletter.com/TuringWay
- Manchester event (1 March): https://www.eventbrite.co.uk/e/boost-your-research-reproducibility-with-binder-manchester-registration-55331997494
- London event (12 March): https://www.eventbrite.co.uk/e/boost-your-research-reproducibility-with-binder-london-registration-55337162944
- Sheffield event (18 March): https://www.eventbrite.co.uk/e/build-a-binderhub-registration-55336756729
