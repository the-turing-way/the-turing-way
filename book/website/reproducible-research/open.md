(rr-open)=
# Open Research

(rr-open-prerequisites)=
## Prerequisites

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| {ref}`rr-vcs` | Helpful | Experience with GitHub is particularly useful |


```{figure} ../figures/evolution-open-research.jpg
---
name: evolution-open-research
alt: This image shows a researcher evolving their research practices to move towards the era of open research.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(rr-open-summary)=
## Summary

Open research aims to transform research by making it more reproducible, transparent, reusable, collaborative, accountable, and accessible to society. It pushes for change in the way that research is carried out and disseminated by digital tools. One definition of open research, [as given by the Organisation for Economic Co-operation and Development (OECD)](https://www.fct.pt/dsi/docs/Making_Open_Science_a_Reality.pdf "Making Open Science a Reality, OECD Science, Technology and Industry Policy Papers No. 25"), is the practice of making "the primary outputs of publicly funded research results – publications and the research data – publicly accessible in a digital format with no or minimal restriction." To achieve this openness in research, each element of the research process should:

- _Be publicly available_: It is difficult to use and benefit from knowledge hidden behind barriers such as passwords and paywalls.
- _Be reusable_: Research outputs need to be licensed appropriately, so that prospective users know any limitations on re-use.
- _Be transparent_: With appropriate metadata to provide clear statements of how research output was produced and what it contains.

The research process typically has the following form: data is collected and then analysed (usually using software). This process may involve the use of specialist hardware. The results of the research are then published. Throughout the process, it is good practice for researchers to document their working in notebooks. Open research aims to make each of these elements open:

- _Open Data_: Documenting and sharing research data openly for re-use.
- _Open Source Software_: Documenting research code and routines, and making them freely accessible and available.
- _Open Hardware_: Documenting designs, materials, and other relevant information related to hardware, and making them freely accessible and available.
- _Open Access_: Making all published outputs freely accessible for maximum use and impact.
- _Open Notebooks_: An emerging practice, documenting and sharing the experimental process of trial and error.

These elements are expanded upon in this chapter.

Open scholarship [{term}`def<Open Scholarship>`] is a concept that extends open research further. It relates to making other aspects of scientific research open to the public, for example:

- _Open educational resources_: Making educational resources publicly available to be re-used and modified.
- _Equity, diversity, inclusion_: Ensuring scholarship is open to anyone without barriers based on factors such as race, background, gender, and sexual orientation.
- _Citizen science_: The inclusion of members of the public in scientific research.

These elements are also discussed in detail in this chapter.

(rr-open-useful)=
## Motivation and Background

There are five main schools of thought motivating open practices to benefit research:

| School                     | Belief               | Aim                                               |
| -------------------------- | -------------------- | ------------------------------------------------- |
| Infrastructure | Efficient research depends on the available tools and applications. | Creating openly available platforms, tools, and services for researchers. |
| Pragmatic | Knowledge-creation could be more efficient if researchers worked together. | Opening up the process of knowledge creation. |
| Measurement | Academic contributions today need alternative impact measurements. | Developing an alternative metric system for research impact. |
| Democratic | The access to knowledge is unequally distributed. | Making knowledge freely available for everyone. |
| Public | Research needs to be made accessible to the public. | Making research accessible for citizens. |

Open practices also benefit the researchers that propagate them.
For example, there is evidence {cite}`McKiernan et al. 2016<McKiernan2016Open>` that open access articles are cited more often, as shown by the metastudy presented in the figure below.

```{figure} ../figures/open-access-citations.jpg
---
height: 500px
name: open-access-citations
alt: A scatter plot of the relationship between citation rates and discipline
---
The relative citation rate (OA: non-OA) in 19 fields of research. This rate is defined as the mean citation rate of OA articles divided by the mean citation rate of non-OA articles. Multiple points for the same discipline indicate different estimates from the same study or estimates from several studies. (See footnote 1 for references.)
```

Another benefit of openness is that while research collaborations are essential to advancing knowledge, identifying and connecting with appropriate collaborators is not trivial. Open practices can make it easier for researchers to connect by increasing the discoverability and visibility of one's work, facilitating rapid access to novel data and software resources, and creating new opportunities to interact with and contribute to ongoing communal projects.
