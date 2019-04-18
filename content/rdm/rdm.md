# Research Data Management

## Prerequisites / recommended skill level
The following sections in this handbook provide useful context and complementary information to this chapter:
- Version control
- Open Research 

## Table of Contents

1. [Summary](#Summary)
2. [Why this is useful](#Why-useful)
3. [The Research Data Lifecycle](#Data-Lifecycle) 
4. [FAIR data](#FAIR)
5. [Storage and backup](#Storage-backup)
    i. [Where to store data](#Where-store)
    ii. [Backups](#Backups)
6. [Documentation and metadata](#Documentation-Metadata)
7. [Sharing and archiving data](#Sharing-Archiving)
    i. [Motivations for sharing data](#Motivations-Sharing)
    ii. [Steps to share your data](#Steps-Share)
    iii. [Barriers to data sharing](#Barriers-Share)
8. [Checklist](#Checklist)
9. [What to read next](#What-Next)
10. [Further reading](#Further-Reading)
11. [Glossary](#Glossary)
12. [Bibliography](#Bibliography)

<a name="Summary"></a>
## Summary 
> easy to understand summary - a bit like tl;dr

Research data management is a key part in encouraging reproducible research. Data management ensures efficiency in research workflows, and also greater reach and impact, as data and software become FAIR (Findable, Accessible, Interoperable and Reuseable). Data should be stored in multiple locations and backed-up regularly. Documentation and metadata ensure that others know how to access, use and re-use your data, and also enable conditions for sharing and publishing data to be outlined. 

<a name="Why-useful"></a>
## How this will help you/ why this is useful 
Having data available is a key component of reproducing an analysis. 
To be able to share data that is understandable and re-usable, research data needs to be managed properly. 
Thus, this chapter lays out good data management practice to allow you to plan your data management activities at the start of your reproducible research project.



## Chapter content
<a name="Data-Lifecycle"></a>
### The Research Data Lifecycle - A Model for Data Management 

Research data often follows a 'lifecycle' which follows the research project as it evolves. This model provides a useful basis on which to plan for research data management, from data creation at the start of a research project, through to publishing and sharing research at the end of the project, and archiving any research data for the long-term and for future re-use once the project has ended. 

The research data lifecycle involves data creation, data use, data publication and sharing, data archiving and data re-use or destruction. 
<a name="FAIR"></a>
### FAIR data 

The FAIR data principles have been developed as guidelines to help make re-using data easier. 
They refer to making data findable, accessible, interoperable and re-usable, all of which will support research reproducibility. Data should be:
* **Findable** with a unique persistent identifier and rich metadata
* **Accessible** via a standard, open and free communication protocol 
* **Interoperable** by using accessible, machine-readable formats and vocabularies 
* **Reusable** with relevant metadata attributes, clear licences, appropriate provenance information and community standards where possible. 

Drawn from [The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618)

Making data 'FAIR' is not the same as making it 'open', but it does imply that you have managed your data sufficiently well to make it usable by others.
The FAIR principles can also be applied to [software](https://doi.org/10.6084/m9.figshare.7449239.v2), and projects where the data and software are both FAIR the research is more likely to be reproducible. 

It is much easier to make data FAIR and open if you plan to do this from the beginning of your research project. 
One way to do this is to create a data management plan, in [DMPonline](https://dmponline.dcc.ac.uk/) or just as a text file, to help you think through how to manage your data. The data management plan should include information on data creation (volume, formats/types and workflows), data use (where the raw or 'live' data is being stored), data publication and data archiving at the end of the project (long-term data storage, or what data is 'kept' at the end of a project). Data management plans should also regularly be updated as the research project changes. 
<a name="Storage-backup"></a>
### Storage and backup 

Data loss can be catastrophic for your research project and happens regularly.
You can prevent data loss by picking suitable storage solutions and backing your data up regularly.
<a name="Where-store"></a>
#### Where to store data 
* Most institutions will provide a *network drive* that you can use to store data.  
* *Portable storage media* such as memory sticks (USB sticks) are more risky and vulnerable to loss and damage.  
* *Cloud storage* provides a convenient way to store, back and up and retrieve data. You should check terms of use before using them for your research data.  

Especially if you are handling personal or sensitive data, you need to ensure the cloud option is compliant with any data protection rules the data is bound by.  
To add an additional layer of security, you should encrypt devices and/or files where needed.

Your institution might provide local storage solutions and policies or guidelines restricting what you can use. 
Thus, we recommend you familiarise yourself with your local policies anc recommendations.
<a name="Backups"></a>
#### Backups 

To avoid loosing your data, you should follow good backup practices.
* You should have 2 or 3 copies of your files, stored on 
* at least 2 different storage media, 
* in different locations.

The more important the data and the more often the datasets change, the more regularly you should back them up.
If your files take up a large amount of space and backing up all of them would be difficult or expensive, you may want to create a set of criteria for when you back up the data. This can be part of your data management plan.
<a name="Documentation-Metadata"></a>
### Documentation and metadata 

Having data available is of no use if it cannot be understood. 
For example a table of numbers is useless if there are no headings which describe what the columns/rows contain. 
Therefore you should ensure that open datasets include consistent core metadata, and that the data is fully described. 
This requires that all documentation accompanying data is written in clear, plain language, and that data users have sufficient information to understand the source, strengths, weaknesses, and analytical limitations of the data so that they can make informed decisions when using it.

- The level of documentation and metadata will vary according to the project and the range of people the data needs to be understood by
- It is best practice to use recognised community metadata standards to make it easier for datasets to be combined.
Examples could include the [Brain Imaging Data Structure](https://github.com/bids-standard/bids-starter-kit) or those found via [FAIRsharing.org](https://www.fairsharing.org)
- Variables should be defined and explained using [data dictionaries](http://help.osf.io/m/bestpractices/l/618767-how-to-make-a-data-dictionary)
- Data should be stored in logical and heirarchical folder structures with a README file used to describe the structure.
The README file is helpful for others and will also help you find your data in the future. 
(Fuchs & Kuusniemi, 2018)
<a name="Sharing-Archiving"></a>
### Sharing and archiving data 
<a name="Motivations-Sharing"></a>
#### Motivations for sharing data 

The world is witnessing a significant global transformation, facilitated by technology and digital media, and fueled by data and information. 
This transformation has enormous potential to foster more transparent, accountable, efficient, responsive, and effective research.
Only a very small proportion of the original data is published in conventional scientific journals. 
Existing policies on data archiving notwithstanding, in today’s practice data are primarily stored in private files, not in secure institutional repositories, and effectively are lost to the public. 
This lack of access to scientific data is an obstacle to international research for two main reasons:

1. It is generally difficult or impossible to fully reproduce a scientific study without the original data.
2. It often causes unnecessary duplication of research efforts; large amounts of research funds are spent every year to recreate already existing data. 
Furthermore, it inhibits joint research activities on various aspects of the same problem.

Accordingly, there is an ongoing global data revolution that seeks to advance collaboration and the creation and expansion of effective, efficient research programs. 
Sharing data openly is crucial to meeting these objectives.
Open data means that the data is freely available on the internet permitting any user to download, copy, analyse, re-process, and re-use it for any other purpose without financial, legal, or technical barriers other than those inseparable from gaining access to the internet itself.
This represents a real shift in how research works. 
At the moment anyone who wishes to use scientific data from a researcher often has to contact that researcher and make a request. Open by default turns this on its head and says that there should be a presumption of publication for all. 
Researchers need to justify data that’s kept closed, for example for security or data protection reasons.
Free access to, and subsequent use of, data is of significant value to society and the economy, and that data should, therefore, be open by default. Research is often publically-funded, so the results of this research should be openly available as a public good.
<a name="Steps-Share"></a>
### Steps to share your data 

#### Step 1: Select what data you want to share
Not all data can be made openly available, due to ethical and commercial concerns, and you may decide that some of your intermediate data is too large to share. 
So you first need to decide which data you need to share for others to be able to reproduce your research.

#### Step 2: Choose a data repository or other sharing platform 
Data should be shared in a formal, open, and indexed data repository where possible so that it will be accessible in the long-run. 
Suitable data repositories by subject, content type or location can be found at [Re3data.org](https://www.re3data.org/).
If possible use a repository which assigns a DOI, a digital object identifier, to make it easier for others to cite your data.


#### Step 3: Upload your data and documentation
In line with the FAIR principles outlined above upload the data in open formats as much as possible and include sufficient documentation and metadata that someone else can understand your data.

#### Step 4: Choose a licence and link to your paper and code
So that others know what they can do with your data you need to apply a licence to your data. The most commonly used licences are [Creative Commons](https://creativecommons.org/choose/), [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), or an [Open Data Commons Attribution License](https://opendatacommons.org/licenses/by/index.html).
To get maximum value from data sharing make sure that your paper and code both link to your data, and vice versa, to allow others to best understand your project.
<a name="Barriers-Share"></a>
### Barriers to data sharing 

Some academics still find sharing data difficult.
Recent surveys (Stuart et al., 2018) amongst researchers find that sharing data is challenging for the following reasons:
* Organising data in a presentable and useful way (mentioned by 46%),
* Unsure about copyright and licensing as mentioned by 37%,
* Not knowing which repository to use as raised by 33%.

These are cultural challenges that might be addressed in changing practice going forward.
However, there are also legal, ethical or contractual reasons that sometimes prevent making data publicly available in its entirety or even in parts.
Those will be addressed in the following paragraphs.

#### Privacy and data protection 

Many fields of scientific disciplines involve working with sensitive personal data. 
Their management is well regulated in data protection legislation (in Europe through national implementations of the General Data Protection Regulation) and ethics procedures as they are established in most research institutions.

##### Consent

In order to make sure that anonymised research data can be made available for future reuse, it is important that consent forms cover sharing anonymised data with other researchers.
Research so far suggests that study participants are usually less concerned about the data being archived and shared than researchers think (Kuula, 2010)
Participant information sheets and consent forms should include how research data will be stored, preserved and used in the long-term, and how confidentiality will be protected when needed.

##### Anonymisation
Individuals must be protected from (re)identification via their personal data used for research. 
Anonymisation of the data may be sufficient in some cases, but ensuring that reidentification is not possible is becoming increasingly difficult and might be impossible due to technical progress, growing computational power and – ironically – more open data. 
For example reidentification may be possible via data-mining of accessible data and so-called quasi-identifiers, a set of (common) properties that are – in their combination – so specific that they can be used to identify.
Preserving privacy may still be possible if partial or generalised datasets are provided e.g. age bands instead of birth date or only the first two digits of postal codes. 
It may also be possible to provide the data in such a format that researchers can query it whist keeping the data itself closed, e.g. a user may be able to send a query to retrieve the mean of a dataset, but not be able to access any of the individual datapoints.
Another way to provide anonymized data is to provide [synthetic data](https://en.wikipedia.org/wiki/Synthetic_data), data generated to reflect the conditions and properties of the raw data without including any of the personal information.

#### National and commercially sensitive data

In many cases companies are understandably unwilling to publish much of their data. 
The reasoning goes that if commercially sensitive information of a company is disclosed, it will damage the company’s commercial interests and undermine competitiveness. 
This is based on the thinking that in competitive markets, innovation will only occur with some protection of information: if a company spends time and money developing something new, the details of which are then made public, then its competitors can easily copy it without having to invest the same resources. 
The result is that no-one would innovate in the first place. 
Similarly governments are often unwilling to publish data that relates to issues such as national security due to public safety concerns.
In such cases it may not be possible to make data open, or it may only be only possible to share partial/obscured datasets as outlined in the section above on privacy.

<a name="Checklist"></a>
## Checklist 
> This is a different style than the other chapters, but I really love what Alex provided so I just kept it.

- [ ]Don't Touch the Raw Data - back it up somewhere reasonable and keep a read-only copy.

- [ ]Have a plan! - Decide where your data is going to be stored, what its called, when/if it needs to be deleted BEFORE you start collecting it and note it down in a data management plan. 
If you collect sensitive data, plan for consent for sharing from the start!

- [ ]Document Everything - You know who the worst person at replying to emails is about what the sampling frequency of channel X was. 
Nope not him, it's actually yourself from a year ago. 
Keep the documentation with the data!

- [ ]Create the data you want to see in the word - Imagine someone was about to give you a dataset that you needed to analyse well in order to get that job you've been dreaming about. 
What would you want it to look like? 
That's how yours should look.

- [ ]Try not to re-invent the wheel. Before you start creating some crazy new schema, storage format or naming protocol - have a quick google, ask your colleagues. 
Something that's already being used is likely going to be better in the long run even if you think there's a better solution.
<a name="What-Next"></a>
## What to learn next 
If you haven't read the chapter on Open Research yet, you might want to read it now for more context on how research data management supports Open Research. 
<a name="Further-Reading"></a>
## Further reading 
 
* Detailed guidance on sharng personal or sensitive data from the UK Data Service: https://www.ukdataservice.ac.uk/manage-data/legal-ethical/consent-data-sharing.aspx
* An overview of storage solutions and their advantages and disadvantages: https://datasupport.researchdata.nl/en/start-the-course/iii-the-research-phase/storing-data
<a name="Glossary"></a>
## Definitions/glossary 
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

RDM - Research Data Management
DMP - Data Management Plan
FAIR - Findable, Accessible, Interoperable and Reusable
<a name="Bibliography"></a>
## Bibliography 

* Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)
Available at http://data.europa.eu/eli/reg/2016/679/oj

* Kuula, A. (2010). Methodological and ethical dilemmas of archiving qualitative data. IASSIST Quarterly, 34(3/4), 35. Available at http://www.iassistdata.org/sites/default/files/iqvol34_35_kuula.pdf 

* Siiri Fuchs, & Mari Elisa Kuusniemi. (2018, December 4). Making a research project understandable - Guide for data documentation (Version 1.2). Zenodo. http://doi.org/10.5281/zenodo.1914401

* Stuart, D., Baynes, G., Hrynaszkiewicz, I., Allin, K., Penny, D., Mithu Lucraft, & Astell, M. (2018). Whitepaper: Practical challenges for researchers in data sharing. Figshare. https://doi.org/10.6084/m9.figshare.5975011.v1

* Mark D. Wilkinson, Michel Dumontier, IJsbrand Jan Aalbersberg, Gabrielle Appleton, Myles Axton, Arie Baak, Niklas Blomberg et al., “The FAIR Guiding Principles for Scientific Data Management and Stewardship,” Scientific Data 3 (2016): 3, https://doi.org/10.1038/sdata.2016.18 


