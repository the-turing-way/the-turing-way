# Open research

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| [Experience with version control](/version_control/version_control) | Helpful | Experience with GitHub is particularly useful |

Recommended skill level: low.


## Table of contents

1. [Summary](#summary)
2. [How this will help you/ why this is useful](#how-this-will-help-you-why-this-is-useful)
3. [Open data](#open-data)
    1. [Steps to make your data open](#steps-to-make-your-data-open)
        1. [Step 1: Make your data available](#step-1-make-your-data-available)
        2. [Step 2: Make your data easy to understand](#step-2-make-your-data-easy-to-understand)
        3. [Step 3: Make your data easy to use](#step-3-make-your-data-easy-to-use)
        4. [Step 4: Make your data citeable](#step-4-make-your-data-citeable)
    2. [Barriers to data sharing](#barriers-to-data-sharing)
        1. [Privacy](#privacy)
        2. [National and commercially sensitive data](#national-and-commercially-sensitive-data)
4. [Open source software](#open-source-software)
    1. [What is open source software?](#what-is-open-source-software)
    2. [How running and contributing to open source software projects benefits you](#how-running-and-contributing-to-open-source-software-projects-benefits-you)
        1. [Making your own work open source](#making-your-own-work-open-source)
        2. [Contributing to others' open source software projects](#contributing-to-others-open-source-software-projects)
    3. [How open source software benefits research](#how-open-source-software-benefits-research)
    4. [How to run your own open source software project](#how-to-run-your-own-open-source-software-project)
        1. [Welcome users by adding information to your README](#welcome-users-by-adding-information-to-your-readme)
        2. [Contributing guidelines](#contributing-guidelines)
        3. [Code of conduct](#code-of-conduct)
    5. [How to contribute to other's open source software projects](#how-to-contribute-to-others-open-source-software-projects)
        1. [Anatomy of an open source software project](#anatomy-of-an-open-source-software-project)
        2. [Contribute your changes](#contribute-your-changes)
        3. [Looking for projects to contribute to and how to contribute to them](#looking-for-projects-to-contribute-to-and-how-to-contribute-to-them)
    6. [Closed software](#closed-software)
5. [Open hardware](#open-hardware)
    1. [Why open hardware?](#why-open-hardware)
    2. [Elements of an open source hardware project](#elements-of-an-open-source-hardware-project)
    3. [Open source hardware processes and practices](#open-source-hardware-processes-and-practices)
        1. [Designing your hardware](#designing-your-hardware)
        2. [Hosting your design file](#hosting-your-design-files)
        3. [Distributing open source hardware](#distributing-open-source-hardware)
6. [Open access](#open-access)
    1. [What is open access?](#what-is-open-access)
        1. [Repositories and self-archiving](#repositories-and-self-archiving)
        2. [Open access publishing](#open-access-publishing)
    2. [Why does open access matter?](#why-does-open-access-matter)
    3. [Best practice for open access](#best-practice-for-open-access)
        1. [Self-archiving](#self-archiving)
        2. [Publication](#publication)
7. [Open notebooks](#open-notebooks)
8. [Open scholarship](#open-scholarship)
    1. [Open educational resources](#open-educational-resources)
    2. [Equity, Diversity, Inclusion](#equity-diversity-inclusion)
    3. [Citizen science](#citizen-science)
9. [Checklists](#checklists)
10. [What to learn next](#what-to-learn-next)
11. [Further reading](#further-reading)
12. [Definitions/glossary](#definitionsglossary)
13. [Bibliography](#bibliography)

## Summary

Open research aims to transform research by making it more reproducible, transparent, re-usable, collaborative, accountable, and accessible to society. It pushes for change in the way that research is carried out and disseminated by digital tools. One definition of open research, [as given by the Organisation for Economic Co-operation and Development (OECD)](https://www.fct.pt/dsi/docs/Making_Open_Science_a_Reality.pdf "Making Open Science a Reality, OECD Science, Technology and Industry Policy Papers No. 25"), is the practice of making "the primary outputs of publicly funded research results – publications and the research data – publicly accessible in digital format with no or minimal restriction”. In order to achieve this openness in research, each element of the research process should:

- Be publicly available - it is difficult to use and benefit from knowledge hidden behind barriers such as passwords and paywalls
- Be reusable - research outputs need to be licensed appropriately so that prospective users clearly know any limitations on re-use
- Be transparent and have appropriate metadata to provide clear statements of how research output was produced and what it contains

The research process typically has the following form: data is collected, it is then analysed (usually using software). This process may involve the use of specialist hardware. The results of the research are then published. Throughout the process it is good practice for researchers to document their working in notebooks. Open research aims to make each of these elements open:

- Open data - documenting and sharing research data openly for re-use
- Open source software - documenting research code and routines, and making them freely accessible and available
- Open hardware - documenting designs, materials, and other relevant information related to hardware, and making them freely accessible and available
- Open access - making all published outputs freely accessible for maximum use and impact
- Open notebooks - an emerging practice, documenting and sharing the experimental process of trial and error

These elements are expanded upon in this chapter.

Open scholarship is a concept that extends open research further. It relates to making other aspects of scientific research open to the public, e.g.

- Open educational resources - making educational resources publicly available to be re-used and modified.
- Equity, diversity, inclusion - ensuring scholarship is open to anyone without barriers based on factors such as race, gender, sexual orientation, etc.
- Citizen science - the inclusion of members of the public in scientific research

These elements are also discussed in detail in this chapter.

## How this will help you/ why this is useful

There are five main schools of thought motivating open practices to benefit research:

| School                     | Belief               | Aim                                               |
| -------------------------- | -------------------- | ------------------------------------------------- |
| Infrastructure | Efficient research depends on the available tools and applications. | Creating openly available platforms, tools and services for researchers. |
| Pragmatic | Knowledge-creation could be more efficient if researchers worked together. | Opening up the process of knowledge creation. |
| Measurement | Academic contributions today need alternative impact measurements. | Developing an alternative metric system for research impact. |
| Democratic | The access to knowledge is unequally distributed. | Making knowledge freely available for everyone. |
| Public | Research needs to be made accessible to the public. | Making research accessible for citizens. |

Open practices also benefit the researchers that propagate them. For example there is evidence [(Mckiernan et al. 2016)](https://elifesciences.org/articles/16800) that open access articles are cited more often, as shown by the metastudy presented in the figure below.

| ![open_access_citatations](/assets/figures/open_access_citatations.jpg) |
| -----------------------------------------------------|
| The relative citation rate (OA: non-OA) in 19 fields of research. This rate is defined as the mean citation rate of OA articles divided by the mean citation rate of non-OA articles. Multiple points for the same discipline indicate different estimates from the same study, or estimates from several studies. (See footnote 1 for references.) |

Another benefit of openness is that while research collaborations are essential to advancing knowledge, identifying and connecting with appropriate collaborators is not trivial. Open practices can make it easier for researchers to connect with one another by increasing the discoverability and visibility of one’s work, facilitating rapid access to novel data and software resources, and creating new opportunities to interact with and contribute to ongoing communal projects.
