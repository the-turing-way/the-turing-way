(rr-rdm-repository)=
# Data Repositories

A repository is a place where digital objects can be stored and shared with others (see also [this repository definition](https://book.the-turing-way.org/afterword/glossary.html#term-Repository)).

Data repositories provide access to academic outputs that are reliably accessible to any web user (see the [OpenDOAR inclusion criteria](https://v2.sherpa.ac.uk/opendoar/about.html)). 
Repositories must earn the trust of the communities they intend to serve and demonstrate that they are reliable and capable of appropriately managing the data they hold ({cite:ps}`Lin2020trust`).

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
- It helps make your Research Objects more FAIR ({ref}`Findable, Accessible, Interoperable and Reusable<rr-rdm-fair>`). This is achieved through:
    - Repositories assign a Persistent Identifier to your Research Objects, which makes them findable and citable (see {ref}`Citing Research Objects<cm-citable-cite>`.
The most commonly used persistent identifiers for research objects is the Digital Object Identifier, usually abbreviated to DOI.
    - Repositories use metadata standards in describing your Research Object, which ensures that other people can find it using search engines.
    - Repositories add a licence to the Research Objects.
A {ref}`license <rr-licensing>` describes to potential reusers of your work what they are allowed to do with it. 
    - Repositories provide documentation for Research Objects.
This can be in the form of READMEs and/or wikis that provide a description of your project and why it might be relevant to people.
    - Encouraging widely-used file formats.
Many repositories have restrictions on the file formats used to ensure the sustainability of Research Objects.
Some file formats (especially proprietary ones with a limited user base) can become deprecated.
- It allows to determine the levels of access to Research Objects.
As covered in {ref}`Barriers to Data Sharing<rr-open-data-barriers>`, there are good reasons to not to make all Research Objects completely open.
However, it's still worthwhile to at least open the metadata and provide an option for people to obtain access to the actual Research Objects if they have certain credentials or if they have been given explicit access.
That way, your work will still be FAIR (because the metadata are findable and there is an access procedure in place), as well as and secure (because you can control who has access).
    - Restricting access and storing data on European servers can help to manage sensitive data {ref}`manage sensitive data<pd-sdpm>`

## Why not the supplemental materials?

Supplemental materials are not following the FAIR principles - as there is no seperate DOI assigned to the supplemental materials which makes it difficult to retrieve these materials. 
Next to supplemental materials not being aligned with the FAIR principles, there are other reasons why a data repository is a better solution: 

- Data control: Supplementary materials cannot be updated, unlike materials available at data repositories.
- Interoperability: If publishers only allow text and PDF formats it hampers data sharing and it will be difficult to reuse the data.
- Availability: Supplementary materials are difficult to access if the article is behind the paywall, and links to supplementary materials can break (since they do not have their own persistent identifier).
- Impact: Data and code should be a primary research output instead of being hidden in the supplementary materials.
- Publisher requirements: Some publishers recommend using a data repository instead.
- Size limits: There may be size limits in place of how large or how many supplementary materials can be shared.

(rr-rdm-repository-select)=
## Selecting an appropriate repository
This chapter outlines some of the crucial functionalities that you should look out for when picking where to share your data, code, methods, hardware, slides, or any other Research Object.

Data should be submitted to domain or discipline specific, community recognised, repository where possible. 
A {ref}`general purpose repository<rr-rdm-repository-types-general>` can be used when there are no suitable discipline specific repositories. 
Discipline specific data repositories are likely to have more functionalities for the type of data that you would like to share, as well as community standards that you can adhere to to make the data more FAIR ({ref}`Findable, Accessible, Interoperable and Reusable<rr-rdm-fair>`). Why sharing data is a good idea is covered in {ref}`Motivations for sharing and archiving data<rr-rdm-sharing-motivations>` and {ref}`Open Data<rr-open-data>`.

The choice of repository can depend on multiple factors:

- Your discipline
- Type of digital output
- File size
- Policies/requirements from institutions, national policies, funding agencies
- Access restrictions

You can search for relevant repositories on [re3data](https://www.re3data.org/) and [FAIRsharing](https://fairsharing.org/). 
However, a search will likely result in a long list of repositories, which you will need to narrow down. 
The following questions may help you with that:

- Is the data repository discipline-specific and community-recognised? Does it use the recognised standards in my discipline?
- Is the data repository known by the research community?
- Are others using the data repository to share their data?
- Has a data repository been specified by my funder/publisher/institution?
- What are the file size requirements and limitations?
- What are the costs for data sharing?
- What data formats are allowed? Will it take the data that you want to share?
- Does it provide a persistent identifier, for example a Digital Object Identifier (DOI)?
- Does it provide the right type of access control that suits the sharing conditions of the data? (restricted access/embargo's)
- Is there support available on how to curate the data/metadata?

See the [ARDC's Guide to choosing a data repository](https://ardc.edu.au/resource/guide-to-choosing-a-data-repository) or the [DCC checklist for evaluating data repositories](https://www.dcc.ac.uk/guidance/how-guides/where-keep-research-data) for more information. 

(rr-rdm-repository-types)=
## Types of repositories

If your disicpline does not have a disciplinary specific repository you can make use of several general repositories. 
Below follows a (non-exhaustive) list of these different types of repositories: 

(rr-rdm-repository-types-general)=
### General purpose repositories

- [Zenodo](https://zenodo.org/)
- [Figshare](https://figshare.com/)

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
An example of what you could share on the OSF is a {ref}`research compendium<rr-compendia>`.
[Get started with the OSF](https://help.osf.io/article/342-getting-started-on-the-osf) by using the introduction on their website. 

### OSF access management
OSF helps to control levels of access you want to give to different people. 
This can be achieved through OSF folder structure that allows to assign different privacy settings to different folders within one project. 
In OSF terminology, these folders with custom privacy settings are called *components*.
OSF has servers in Europe which allows compliance with the {ref}`GDPR<pd-sdp-personal-policies>`.

### OSF and FAIR principles
The following functionality of OSF helps to make such a folder FAIR ({ref}`Findable, Accessible, Interoperable and Reusable<rr-rdm-fair>`):

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

(rr-rdm-repository-resources)=
## Additional Repository Resources

