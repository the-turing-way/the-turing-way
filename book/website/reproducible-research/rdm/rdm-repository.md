(rr-rdm-repository)=
# Data Repositories

A repository is a place where digital objects can be stored and shared with others (see also [this repository definition](https://book.the-turing-way.org/afterword/glossary.html#term-Repository)).

Data repositories provide access to academic outputs that are reliably accessible to any web user (see the [OpenDOAR inclusion criteria](https://v2.sherpa.ac.uk/opendoar/about.html)). 
Repositories must earn the trust of the communities they intend to serve and demonstrate that they are reliable and capable of appropriately managing the data they hold ({cite:ps}`Lin2020trust`).

```{figure} ../../../figures/data-repo.*
---
height: 500px
name: data-repo
alt: A tree representing a general data repository, with squirrels symbolizing researchers gathering FAIR data, which can be open or restricted. Next to the tree are examples showing how different academic disciplines and institutions have unique types of data repositories, and how FAIR data may differ when obtained from general or domain-specific repositories.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence.  [](10.5281/zenodo.13882307).
```

Long-term archiving repositories are designed for secure and permanent storage of data, ensuring data preservation over extended periods.
This differs from platforms like GitHub and GitLab which primarily serve as collaborative development tools, facilitating version control and project management in a more dynamic and transient environment.
Platforms such as GitHub and GitLab do not assign persistent identifiers to repositories, and their preservation policies are more flexible compared to those of data repositories. 

This chapter includes:

- Introduction to repositories
- An overview of how repositories facilitate you to comply to the FAIR principles
- How to select an appropriate repository
- An introduction to the Open Science Framework

(rr-rdm-repository-FAIR)=
## Repositories and FAIR

Selecting an appropriate repository for your research outputs has many benefits:
- It helps make your Research Objects more [FAIR](#rr-rdm-fair). This is achieved through:
    - Repositories assign a Persistent Identifier (PID) such as a DOI to your Research Objects, which makes them findable and citable (see [](#cm-citable-cite)).
    See our [chapter on persistent identifiers](#rr-rdm-pid) to understand how PIDs work and why they're essential for FAIR research.
    - Repositories use metadata standards in describing your Research Object, which ensures that other people can find it using search engines.
    - Repositories add a licence to the Research Objects.
A [license](#rr-licensing) describes to potential reusers of your work what they are allowed to do with it. 
    - Repositories provide documentation for Research Objects.
This can be in the form of [READMEs](#rr-rdm-readme) and/or wikis that provide a description of your project and why it might be relevant to people.
    - Encouraging widely-used file formats.
Many repositories have restrictions on the file formats used to ensure the sustainability of Research Objects.
Some file formats (especially proprietary ones with a limited user base) can become deprecated.
- It allows to determine the levels of access to Research Objects.
As covered in [](#rr-open-data-barriers), there are good reasons to not to make all Research Objects completely open.
However, it's still worthwhile to at least open the metadata and provide an option for people to obtain access to the actual Research Objects if they have certain credentials or if they have been given explicit access.
That way, your work will still be FAIR (because the metadata are findable and there is an access procedure in place), as well as and secure (because you can control who has access).
    - Restricting access and storing data on European servers can help to [manage sensitive data](#pd-sdpm)

(rr-rdm-repository-supplemental)=
## Why not the supplemental materials?

Supplemental materials are not following the FAIR principles - as there is no separate DOI assigned to the supplemental materials which makes it difficult to retrieve these materials. 
Next to supplemental materials not being aligned with the FAIR principles, there are other reasons why a data repository is a better solution: 

- Data control: Supplementary materials cannot be updated, unlike materials available at data repositories.
- Interoperability: If publishers only allow text and PDF formats it hampers data sharing and it will be difficult to reuse the data.
- Availability: Supplementary materials are difficult to access if the article is behind the paywall, and links to supplementary materials can break (since they do not have their own persistent identifier).
- Impact: Data and code should be a primary research output instead of being hidden in the supplementary materials.
- Publisher requirements: Some publishers recommend using a data repository instead.
- Size limits: There may be size limits in place of how large or how many supplementary materials can be shared.

## Why not "data available upon request"? 

Several studies indicate that "data available upon request", is not actually available upon request!

We encourage you to explore some of the existing research on this question.
We extract key quotes from a selection of studies here:
- _"Only "38% of the researchers sent their data immediately or after reminders"_ [Vanpaemel et al. 2015](http://dx.doi.org/10.1525/collabra.13)
- _"We received only one of ten raw data sets requested."_ [Savage and Vickers 2009](https://doi.org/10.1371/journal.pone.0007078)
- _"..less than one-third of the contacted authors sent us the requested data."_ [Dutra dos Reis et al. 2021](https://doi.org/10.1080/08989621.2021.1910029)
- _"73% of the authors did not share their data._" [Wicherts et al. 2006](https://doi.org/10.1037/0003-066X.61.7.726)
- _"..the odds of a data set being extant fell by 17% per year. 
In addition, the odds that we could find a working e-mail address for the first, last, or corresponding author fell by 7% per year."_ [Vines et al. 2014](http://dx.doi.org/10.1016/j.cub.2013.11.014)
- _"We received no response to 41.3% of our data requests."_ - [Tedersoo et al. 2021](https://doi.org/10.1038/s41597-021-00981-0)
- _"..only 7/157 research articles shared their data sets, 4.5%."_ [Rowhani-Farid and Barnett 2016](http://dx.doi.org/10.1136/bmjopen-2016-011784)
- _“Data were recoverable online or through direct data requests for 30% of this sample.
Data recovery declines exponentially with time since publication, halving every 6 years,…."_ [Minocher et al. 2021](https://doi.org/10.1098/rsos.210450)
- _"Among articles stating that data was available upon request, only 17% shared data upon request."_ [Hussey 2023](https://doi.org/10.31234/osf.io/jbu9r)
- _"..only 123 (6.8%) provided the requested data."_ - [Gabelica et al. 2022](https://doi.org/10.1016/j.jclinepi.2022.05.019)
- _"..we found raw data/code for 133 (47%) of those 283 preprints (15% of all analyzed preprint articles)._ [Strcic et al. 2022](https://doi.org/10.1007/s11192-022-04346-1)
- only one (0.8%) out of 130 analyzed articles contained a direct link to the analyzed data [Gorman 2020](https://doi.org/10.1007/s11948-020-00203-7)

Unfortunately, journals often [do not mandata data sharing](https://metaresearch.nl/blog/2026/2/3/promised-data-unavailable-im-sorry-maam-theres-nothing-we-can-do) or do not enforce data sharing where these policies are in place. 

(rr-rdm-repository-select)=
## Selecting an appropriate repository
This chapter outlines some of the crucial functionalities that you should look out for when picking where to share your data, code, methods, hardware, slides, or any other Research Object.

Data should be submitted to domain or discipline specific, community recognised, repository where possible. 
A [general purpose repository](#rr-rdm-repository-types-general) can be used when there are no suitable discipline specific repositories. 
Discipline specific data repositories are likely to have more functionalities for the type of data that you would like to share, as well as community standards that you can adhere to make the data more [FAIR](#rr-rdm-fair).
Why sharing data is a good idea is covered in [](#rr-rdm-sharing-motivations) and [](#rr-open-data).

The choice of repository can depend on multiple factors:

- Your discipline
- Type of digital output
- File size
- Policies/requirements from institutions, national policies, funding agencies
- Access restrictions

You can search for relevant repositories on [re3data](https://www.re3data.org/) and [FAIRsharing](https://fairsharing.org/). 
However, a search will likely result in a long list of repositories, which you will need to narrow down. 
The following questions may help you with that:

- Is the data repository discipline-specific and community-recognised? 
Does it use the recognised standards in my discipline?
- Is the data repository known by the research community?
- Are others using the data repository to share their data?
- Has a data repository been specified by my funder/publisher/institution?
- What are the file size requirements and limitations?
- What are the costs for data sharing?
- What data formats are allowed? 
Will it take the data that you want to share?
- Does it provide a [persistent identifier](#rr-rdm-pid-ecosystem), for example a Digital Object Identifier (DOI)?
- Does it provide the right type of access control (restricted access/embargo's) that suits the sharing conditions of the data? 
- Is there support available on how to curate the data/metadata?

See the [ARDC's Guide to choosing a data repository](https://ardc.edu.au/resource/guide-to-choosing-a-data-repository) or the [DCC checklist for evaluating data repositories](https://www.dcc.ac.uk/guidance/how-guides/where-keep-research-data) for more information. 

(rr-rdm-repository-types)=
## Types of repositories

If your discipline does not have a disciplinary specific repository you can make use of several general repositories. 
Below follows a (non-exhaustive) list of these different types of repositories: 

(rr-rdm-repository-types-general)=
### General purpose repositories

- [Zenodo](https://zenodo.org/) (see this [Data Umbrella webinar](https://www.youtube.com/watch?v=eChOfh8t04k) for practical guidance on Zenodo)
- [Figshare](https://figshare.com/)

For a detailed comparison of general purpose repositories including file size limits, versioning features, access control options, and other key criteria, see the [Generalist Repository Comparison Chart](https://doi.org/10.5281/zenodo.11105429).

### Project repositories

- [Open Science Framework (OSF)](https://osf.io/)
- [Research Equals](https://www.researchequals.com/)
- [Octopus](https://www.octopus.ac/)
- [CRAN](https://cran.r-project.org/) for R-Packages

### Generic data repositories

- [Dryad](https://datadryad.org/stash)
- [Dataverse](https://dataverse.org/)
- [4TU.ResearchData](https://data.4tu.nl/)
- [UK Data Service](https://ukdataservice.ac.uk/)

### Institutional or National repositories

Many countries and/or institutions also provide access to repositories that you could use. 
Check with your local Research Data Management support to see if this available at your institute, or try to search for such a national repository using [re3data](https://www.re3data.org/) and [FAIRsharing](https://fairsharing.org/). 

## Recommended Repositories 

Several lists of Recommended Repositories by publishers exist: 

- [PLOS ONE Recommended Repositories](https://journals.plos.org/plosone/s/recommended-repositories)
- [Springer Nature Data repository guidance](https://www.springernature.com/gp/authors/research-data-policy/recommended-repositories)
- [Elsevier's Public repositories to store and find data](https://www.journals.elsevier.com/data-in-brief/policies-and-guidelines/public-repositories-to-store-and-find-data)

(rr-rdm-repository-osf)=
## Example: Open Science Framework (OSF) 

The OSF is a free open-source software project that facilitates open collaboration in science research. 
OSF is way more than a data repository or an archive; it is a collaboration tool which can be used by research teams to work on projects privately or openly, similar to GitHub. 
This case study highlights OSF as one of the  repositories *for everything* that you can choose to store your research output long term and make it citable through getting a persistent identifier.
An example of what you could share on the OSF is a [](#rr-compendia).
[Get started with the OSF](https://help.osf.io/article/342-getting-started-on-the-osf) by using the introduction on their website. 

### OSF access management
OSF helps to control levels of access you want to give to different people. 
This can be achieved through OSF folder structure that allows to assign different privacy settings to different folders within one project. 
In OSF terminology, these folders with custom privacy settings are called *components*.
OSF has servers in Europe which allows compliance with the [GDPR](#pd-sdp-personal-policies).

### OSF and FAIR principles
The following functionality of OSF helps to make such a folder [FAIR](rr-rdm-fair):

- In addition to its own unique, persistent URLs, OSF offers DOIs for public folders.
- OSF allows to add metadata to your folder.
Project metadata fields include at Title, Description, License, Tags and Persistent Identifiers.
It is possible to add more metadata into the project Wiki or submit in form of a separate file.
- It is possible to add license to a project to specify how others are allowed to copy, distribute, and make use of this work. 
- OSF provides detailed landing pages to document projects.
Each *component* has its own wiki that allows to add reach documentation on multiple levels.
- File formats are not limited by OSF; it is your decision which format to use to make your project future proof. 

### Additional OSF resources

- [Introduction to OSF](https://vimeo.com/668636108) by Dr Amy Gillespie 
- [Collaborating, sharing, and preregistering through OSF](https://www.youtube.com/watch?v=48Xy62spsLI) by Anita Eerland.

