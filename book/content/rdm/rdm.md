# Research Data Management

## Prerequisites / recommended skill level

The following sections in this handbook provide useful context and complementary information to this chapter:

| Prerequisite                                        | Importance |
| --------------------------------------------------- | ---------- |
| [Version Control](/version_control/version_control) | Helpful    |
| [Open Research](/open_research/open_research)       | Helpful    |

## Table of Contents

- [Research Data Management](#research-data-management)
  - [Prerequisites / recommended skill level](#prerequisites--recommended-skill-level)
  - [Table of Contents](#table-of-contents)
  - [Summary](#summary)
  - [How this will help you/ why this is useful](#how-this-will-help-you-why-this-is-useful)
  - [Chapter content](#chapter-content)
    - [What Is Data?](#what-is-data)
    - [The Research Data Lifecycle - A Model for Data Management](#the-research-data-lifecycle---a-model-for-data-management)
    - [The FAIR principles and practices](#the-fair-principles-and-practices)
      - [Theory](#theory)
      - [Tools and indicators](#tools-and-indicators)
      - [Metadata and identifiers - community standards](#metadata-and-identifiers---community-standards)
    - [Storage and backup](#storage-and-backup)
      - [Where to store data](#where-to-store-data)
      - [Backups](#backups)
    - [Data organisation in spreadsheets](#data-organisation-in-spreadsheets)
    - [Documentation and metadata](#documentation-and-metadata)
    - [Sharing and archiving data](#sharing-and-archiving-data)
      - [Motivations for sharing data](#motivations-for-sharing-data)
    - [Steps to share your data](#steps-to-share-your-data)
      - [Step 1: Select what data you want to share](#step-1-select-what-data-you-want-to-share)
      - [Step 2: Choose a data repository or other sharing platform](#step-2-choose-a-data-repository-or-other-sharing-platform)
      - [Step 3: Upload your data and documentation](#step-3-upload-your-data-and-documentation)
      - [Step 4: Choose a licence and link to your paper and code](#step-4-choose-a-licence-and-link-to-your-paper-and-code)
    - [Barriers to data sharing](#barriers-to-data-sharing)
      - [Privacy and data protection](#privacy-and-data-protection)
        - [Consent](#consent)
        - [Anonymisation](#anonymisation)
      - [National and commercially sensitive data](#national-and-commercially-sensitive-data)
  - [Personal Stories](#personal-stories)
    - [Susanna-Assunta Sansone: from FAIR co-author to FAIR doer](#susanna-assunta-sansone-from-fair-co-author-to-fair-doer)
  - [Checklist](#checklist)
  - [What to learn next](#what-to-learn-next)
  - [Further reading](#further-reading)
  - [Definitions/glossary](#definitionsglossary)
  - [Bibliography](#bibliography)

<a name="Summary"></a>

## Summary

Research Data Management (RDM) covers how research data can be stored, described and reused. Data here is used as a
generic term to encompass all digital objects. RDM is a key part in enabling reproducible research. RDM ensures
efficiency in research workflows, and also [greater reach and impact](https://the-turing-way.netlify.com/credit/credit.html). Data should be stored in multiple locations and backed-up regularly to prevent loss or data corruption. Clearly describing data using documentation and metadata ensures that others know how to access, use and re-use your data, and also enable conditions for sharing and publishing data to be outlined.

<a name="Why-useful"></a>

## What are the benefits of Research Data Management?

- Managing your data allows you to always find your data
- Storing your data properly prevents data loss 
- [Recognition](https://the-turing-way.netlify.com/credit/credit.html) for all research outputs
- It stimulates **collaboration** with others, who will find it easier to understand and reuse your data
- Managing your data properly increases the quality of scientific practice 
- RDM is cost/time efficient, as you will always be able to find and use your data


## Chapter content

<a name="What-Data"></a>

### What Is Data?

Data are all digital objects that you use and produce during your research life cycle, encompassing datasets, software,
code, workflow, models, figures, tables, images and videos, interviews, articles. Data are your research asset. In some fields it's obvious what data means - you have observations or results of simulations. However, in other fields, particularly in Social
Sciences, Humanities or Arts, you may be thinking "I don't think I have any data". A good way of thinking about what
might be classed as data that needs to be managed is to ask yourself the questions "What is the information that I need
to use and write about in my paper or book?", "What information would I need to back up my conclusions?" and "What
information is needed by others to understand and possibly replicate the research that I've done?". This information is your data.

<a name="Data-Lifecycle"></a>

### The Research Data Lifecycle - A Model for Data Management

Research data often follows a 'lifecycle' which follows the research project as it evolves; here is a
[video](https://www.ukdataservice.ac.uk/manage-data/lifecycle.aspx) that describes it. This model provides a useful
basis on which to plan for research data management, from data creation at the start of a research project, through to
publishing and sharing research at the end of the project, and archiving any research data for the long-term and for
future re-use once the project has ended.

The research data lifecycle involves data creation, data use, data publication and sharing, data archiving and data
re-use or destruction. However, data have a longer lifespan than the research project that creates them.

<a name="FAIR"></a>

### The FAIR principles and practices

The FAIR guiding principles for scientific data management and stewardship {% cite Wilkinson2016fair %} have been
developed as guidelines to improve the findability, accessibility, interoperability and re-usability of digital assets;
all of which will support research reproducibility. Importantly, the FAIR principles not only improve the reusability of data by humans, but also allow machines to automatically find and use digital objects. The capacity of computational systems to find, access, interoperate, and reuse data, with none or minimal human intervention, is essential in today's data-driven era, where
humans increasingly rely on computational support to deal with data as a result of the increase in [volume, velocity and
variety](https://www.zdnet.com/article/volume-velocity-and-variety-understanding-the-three-vs-of-big-data/).

<a name="Theory"></a>

#### Theory

Here is an [overview](https://www.go-fair.org/fair-principles) of what the FAIR principles recommend. In brief,
data should be:

**Findable:** the first step in (re)using data is to find them, and descriptive metadata is essential. **Metadata** are information and keywords that provide information about your data.

**Accessible:** to get data one needs to know if authentication and authorisation is necessary, or if data is open with
no restrictions.

**Interoperable:** data need to be integrated with other data and/or interoperate with applications or workflows. This is enabled by using commmon vocabulary and using [metadata standards](https://fairsharing.org/standards/).

**Reusable:** data should be documented so that they can be used or replicated in different settings.

It is important to stress that making data 'FAIR' is not the same as making it 'open'. Not all data can be shared openly, and matters of privacy, IP rights and national security should be kept in mind. Data should therefore be as open as possible, as closed as necessary.

FAIR is also not the same as reproducible. While data and [software](https://doi.org/10.6084/m9.figshare.7449239.v2) that are compliant with the FAIR principles may be more likely to be reproducible, the FAIR principles are not a standard that improves data and software quality. 

It is much easier to make data FAIR if you plan to do this from the beginning of your research project. One way to do
this is to create a Data Management Plan (DMP), in [DMPonline](https://dmponline.dcc.ac.uk/) or just as a text file, to
help you think through how to manage your data. The DMP should include information on data creation (volume,
formats/types and workflows), data use (where the raw or 'live' data is being stored and backed-up), data publication and data
archiving at the end of the project (long-term data storage, or data archiving), and any ethical or legal issues that have to be addressed (if applicable). DMPs are not written in stone and serve as a guiding tool that should be regularly updated as the research project progresses or diverge from the initial design.

<a name="Tools-indicators"></a>

#### FAIR communities

If you are interested in following the discussion and/or participate in it, here are two global and international initiatives that act as umbrella organizations and reference points for many discipline specific efforts: [GOFAIR](https://www.go-fair.org) and the [Research Data Alliance (RDA)](https://www.rd-alliance.org). Watch these spaces!

<a name="Metadata-identifiers"></a>

#### Metadata - community standards

The use of community-defined standards for metadata and identified is vital for high-quality, reproducible research and for the integrative analysis and comparison of heterogeneous data from multiple sources, domains and disciplines. 

You can use [FAIRsharing](https://fairsharing.org) to identify community-defined standards for metadata and/or identifier schemas, databases or repositories that exist for your data and discipline. You can document these standards and repositories in your data management plan so that you can easily find and use them in your research. 
<a name="Storage-backup"></a>

### Storage and backup

Data loss can be catastrophic for your research project. You can prevent data loss by picking suitable storage solutions and backing your data up frequently.

<a name="Where-store"></a>

#### Where to store data

- Most institutions will provide a _network drive_ that you can use to store data, which is generally automatically backed up.
- _Portable storage media_ such as memory sticks (USB sticks) are more risky and vulnerable to loss and damage.
- _Cloud storage_ provides a convenient way to store, back and up and retrieve data. You should check terms of use
  before using them for your research data.

Especially if you are handling personal or sensitive data, you need to ensure the cloud option is compliant with any
data protection rules the data is bound by. To add an additional layer of security, you should encrypt devices and/or
files where needed.

Your institution might provide local storage solutions and policies or guidelines restricting what you can use. Thus, we
recommend you familiarise yourself with your local policies anc recommendations.

<a name="Backups"></a>

#### Backups

To avoid loosing your data:

- You should have 2 or 3 copies of your files, stored on
- at least 2 different storage media,
- in different locations.

The more important the data and the more often the datasets change, the more frequently you should back them up. If your
files take up a large amount of space and backing up all of them would be difficult or expensive, you may want to create
a set of criteria for when you back up the data. This can be part of your data management plan.

### File Naming conventions

Structure your file names and set up a template for this. It is very useful to start with the date (when the file was generated: YYYYMMDD) which will sort your files chronologically and also creates a unique identifier for each file. (It will be immediately clear if there are multiple files generated on the same day that will have to be given a version number –or “A, B”-, because otherwise overwriting would occurs if you store these files in the proper folder). 

Tips for file naming: 
• Date or date range of experiment: YYYYMMDD
• File type
• Researcher name/initials
• Version number of file (v001, v002) or language used in the document (ENG)
• Don’t make file names too long (this can complicates file transfers)
• Avoid special characters (?\!@*%{[<>) and spaces

You can explain the file naming convention in a README.txt file, so that it will also become clear to others what the file names mean. 


### Data organisation

To organise your data you can create a folder structure (or re-use a [folder structure](http://nikola.me/folder_structure.html) to ensure that you are able to find your files. 

-	Make sure you have enough (sub)folders so that files can be stored in the right folder and are not scattered in folders where they don’t belong or stored in large quantities in a single folder 
-	Use a clear folder structure: you can structure folders based on the person that has generated the data/folder, chronologically (month, year, sessions), per project (as done in the example above), or based on analysis method/equipment/type of data. 

You can also pull/download folder structures using GitHub. [This template](https://github.com/bvreede/good-enough-projec) by Barbara Vreede, based on [cookiecutter](https://github.com/cookiecutter/cookiecutter), follows recommended practices for scientific computing by [Wilson et al. (2017)](https://doi.org/10.1371/journal.pcbi.1005510).

<a name="Spreadsheets"></a>
### Data organisation in spreadsheets

Spreadsheets, such as Microsoft Excel files, are commonly used to collect, store, manipulate, analyse, and share
research data. Spreadsheets are convenient and easy-to-use tools for these tasks but are not amenable to reproducibility
if used as dynamic documents. There is a collection of [horror-stories](http://www.eusprig.org/horror-stories.htm) that
document the many ways that the use of spreadsheets have scuppered analyses due to unexpected behaviour or error-prone
editing processes. Some of these mishaps are not unique to spreadsheets, but
[many are](https://doi.org/10.1186/s13059-016-1044-7).

Data manipulation and analysis in spreadsheets in particular is best avoided as, without version control, it can lead to
non-reproducible workflows. By opening and editing raw data files directly by hand, for example to change values or
perform calculations, the process by which new values are obtained is not properly documented, and you may accidentally
over-write something or type in the wrong value only to notice after it's too late (or not at all).

Even if these errors are avoided, if the spreadsheet is poorly organised then it may be
[difficult for collaborators](https://luisdva.github.io/pls-don't-do-this/) to easily [read-in and re-use](#FAIR) your
data for further analysis.

It's often not practical to avoid the use of spreadsheets altogether but there are some simple steps that can be taken
to mitigate their flaws. The following principles, taken from Broman et al. {% cite Broman2018data --suppress_author %},
provide some practical advice to ensure your data is clearly organised and human- and machine-readable:

- Be consistent
- Write dates as YYYY-MM-DD
- Don't leave any cells empty, if there is no data use NA (Not Available)
- Put each observation/sample in its own row
- Put each variable in a column
- Each cell should contain information on one thing: seperate multiple pieces of information to different cells
- Don't include calculations in the raw data files: leave the raw data alone!
- Don’t use font color or highlighting, consider adding another variable/column for this information
- Choose good/clear names for observations and variables and make sure there are no spaces in names
- Use data validation to avoid data entry mistakes
- Save the data in text files (such as .CSV - comma-separated values) to ensure interoperability with other software programmes.

To learn more about spreadsheet organisation, have a look at the Data Carpentry lessions for [Social Scientists](https://datacarpentry.org/spreadsheets-socialsci/) and [Ecologists](https://datacarpentry.org/spreadsheet-ecology-lesson/). 

<a name="Documentation-Metadata"></a>

### Documentation and metadata

Having data available is of no use if it cannot be understood. For example a table of numbers is useless if there are no
headings which describe what the columns/rows contain. Therefore you should ensure that open datasets include consistent
core metadata, and that the data is fully described. This requires that all documentation accompanying data is written
in clear, plain language, and that data users have sufficient information to understand the source, strengths,
weaknesses, and analytical limitations of the data so that they can make informed decisions when using it.

- The level of documentation and metadata will vary according to the project and the range of people the data needs to
  be understood by
- It is best practice to use recognised community metadata standards to make it easier for datasets to be combined. For
  example, for brain data the [Brain Imaging Data Structure](https://doi.org/10.25504/FAIRsharing.rd1j6t) is the
  strandards to use; other [metadata standards](https://fairsharing.org/standards)(reporting requirements,
  termonologies, and models/schemas) are searchable in FAIRsharing.
- Variables should be defined and explained using
  [data dictionaries](http://help.osf.io/m/bestpractices/l/618767-how-to-make-a-data-dictionary)
- Data should be stored in logical and hierarchical folder structures with a README file used to describe the structure.
  The README file is helpful for others and will also help you find your data in the future
  {% cite Fuchs2018documentation %}. See [here](https://cornell.app.box.com/v/ReadmeTemplate) for an example. 

<a name="Sharing-Archiving"></a>

### Sharing and archiving data

<a name="Motivations-Sharing"></a>

#### Motivations for sharing data

Sharing your research data is important for several reasons:

1. It is generally difficult or impossible to fully reproduce a scientific study without the original data.
2. To prevent duplicate efforts: Large amounts of research funds and careers of researchers can be wasted by only sharing a small part of research in the form of publications. Data sharing therefore also speeds up the scientific progress.
3. It facilitates collaboration and increases the impact and quality of scientific research.
4. Research is often publically-funded, so the results of this research should be openly available as a public good.

<a name="Steps-Share"></a>

### Steps to share your data

#### Step 1: Select what data you want to share

Not all data can be made openly available, due to ethical and commercial concerns, and you may decide that some of your
intermediate data is too large to share. So you first need to decide which data you need to share for others to be able
to reproduce your research.

#### Step 2: Choose a data repository or other sharing platform

Data should be shared in a data repository where possible so that it will be accessible in the long-run. Suitable data repositories by subject, content type or location can be found at [Re3data.org](https://www.re3data.org/) and in [FAIRsharing](https://fairsharing.org/databases) where you can also see
which standards (metadata and identifier) the repositories implement and which journal/publisher recommend them. If
possible use a repository which assigns a DOI, a digital object identifier, to make it easier for others to cite your
data.

#### Step 3: Upload your data and documentation

In line with the FAIR principles outlined above upload the data in open formats as much as possible and include
sufficient documentation and metadata that someone else can understand your data.

#### Step 4: Choose a licence and link to your paper and code

So that others know what they can do with your data you need to apply a licence to your data. The most commonly used
licences are [Creative Commons](https://creativecommons.org/choose/). To get maximum value from data sharing make sure that your paper and code both link to your data, and vice versa, to allow others to best understand and cite your project. For practical guidance on how to do this, see the credit chapter.

<a name="Barriers-Share"></a>

### Barriers to data sharing

Some academics still find sharing data difficult. Recent surveys {% cite Stuart2018sharing %} amongst researchers find
that sharing data is challenging for the following reasons:

- Organising data in a presentable and useful way (mentioned by 46%),
- Unsure about copyright and licensing as mentioned by 37%,
- Not knowing which repository to use as raised by 33%.

These are cultural challenges that might be addressed in changing practice going forward. However, there are also legal,
ethical or contractual reasons that sometimes prevent making data publicly available in its entirety or even in parts.
Those will be addressed in the following paragraphs.

#### Privacy and data protection

Many fields of scientific disciplines involve working with sensitive personal data. Their management is well regulated
in data protection legislation (in Europe through national implementations of the General Data Protection Regulation)
and ethics procedures as they are established in most research institutions {% cite EU2016protection %}.

##### Consent

In order to make sure that anonymised research data can be made available for future reuse, it is important that consent
forms cover sharing data with other researchers. Participant information sheets and consent forms should include how research data will be stored, preserved and used in the long-term, and how confidentiality will be protected when needed.

##### Anonymisation

Individuals must be protected from (re)identification via their personal data used for research. Anonymisation of the
data may be sufficient in some cases, but ensuring that reidentification is not possible is becoming increasingly
difficult and might be impossible due to technical progress, growing computational power and – ironically – more open
data. For example reidentification may be possible via data-mining of accessible data and so-called quasi-identifiers, a
set of (common) properties that are – in their combination – so specific that they can be used to identify. Preserving
privacy may still be possible if partial or generalised datasets are provided. For example, providing age bands instead
of birth date or only the first two digits of postal codes. It may also be possible to provide the data in such a format
that researchers can query it whist keeping the data itself closed. For example, a user may be able to send a query to
retrieve the mean of a dataset, but not be able to access any of the individual datapoints. Another way to provide
anonymized data is to provide [synthetic data](https://en.wikipedia.org/wiki/Synthetic_data), data generated to reflect
the conditions and properties of the raw data without including any of the personal information.

#### National and commercially sensitive data

In many cases companies are understandably unwilling to publish much of their data. The reasoning goes that if
commercially sensitive information of a company is disclosed, it will damage the company’s commercial interests and
undermine competitiveness. This is based on the thinking that in competitive markets, innovation will only occur with
some protection of information: if a company spends time and money developing something new, the details of which are
then made public, then its competitors can easily copy it without having to invest the same resources. The result is
that no-one would innovate in the first place. 

Similarly governments are often unwilling to publish data that relates to
issues such as national security due to public safety concerns. In such cases it may not be possible to make data open,
or it may only be only possible to share partial/obscured datasets as outlined in the section above on privacy.

<a name="Personal-stories"></a>

## Personal Stories

<a name="SusannaSansone"></a>

### Susanna-Assunta Sansone: from FAIR co-author to FAIR doer

Let's start with my digital footprints so that you can discovery my activities:

- [Biography](https://www.eng.ox.ac.uk/people/susanna-assunta-sansone)
- [The Data Readiness group I run at Oxford University](https://sansonegroup.eng.ox.ac.uk)
- [ORCID: 0000-0001-5306-5690](https://orcid.org/0000-0001-5306-5690)
- [Profile on LinkedIn](https://uk.linkedin.com/in/sasansone)
- [Talks on SlideShare](https://www.slideshare.net/SusannaSansone)
- [Twitter; yes I am the FAIRlady](https://twitter.com/SusannaASansone)
- [Activities on GitHub; yeah, no code sorry](https://github.com/SusannaSansone)
- [Google Scholar](https://scholar.google.co.uk/citations?user=gfJ8wsIAAAAJ&hl=en)

I have worked on research data management since 2001, yes, way before this area was even considered a 'thing'. I was
also told that there is no career to make in research data management. Well, how wrong that comment was! Formely seen as
intersection between service provision and IT, data management has become a first class citizen, recognized as a
research and development subject, as it should be. A lot of the credit for this change goes to the FAIR principles. Love
it or hate it, FAIR is now an internationally-known lighthouse brand. Since we published the first article on the
[FAIR principles](https://doi.org/10.1038/sdata.2016.18), enabling FAIR has been my focus.

The reuse of other people’s data is providing useful insights for new research questions and products, and driving new
scientific discoveries. To realize its potential, however, we need new mechanisms to manage the growing availability and
scale of scholarly digital products, such as datasets, software, algorithms, articles. FAIR has been specifically
designed to emphasise the machine-readablity of these digital objects.

With my group of research software and knowledge engineerings we address the grand challenges related to information
science and scholarly communications, where data quality and readiness for (re)use is a prerequisite for success. I
believe that better data means better science, and this underpins reusable research, aids scholarly publishing, and
enables faster and reliable data-driven discoveries. As I say in my [one minute video](https://youtu.be/3VDw7XIulIk), my
vision is to transform the concept of data readiness into a powerful toolkit at the researchers’ fingertips, to realize
FAIR data by stealth.

FAIR is not a magic wand. There is a lot to be done to enable and enact this transformation. We need all hands on deck!
Researchers, service providers, journal publishers, library science experts, funders and learned societies in the
academic as well as in the commercial and governmental setting all play a role: from providing use cases, to drive
policy and culture changes that motivates, rewards and credits researchers for disseminating and publishing
high-quality, machine-readable data; to building tools and services, to inform, training and educate.

There are many community efforts around FAIR; keeping abreast with these is an activity in itself. I spend considerable
time to bring my group activities (such as [ISA](https://isa-tools.org) and [FAIRsharing](https://fairsharing.org)) in
and under larger international umbrella organizations like
[GOFAIR](https://www.go-fair.org/implementation-networks/overview/fair-strepo) and the
[RDA](http://dx.doi.org/10.15497/RDA00030) to interact with others, learn from them, compare and contrast efforts and
build new collaborations. I also play leading roles, seating on boards and chairing working groups with collagues,
because you must get your hands dirty and lead by example.

In research data management, the history is the future. The one I envision is a future where scientific evidences are
routinely available in a transparent, trustworthy and persistent manner to support peer-review and withstand
reproducibility, to underpin new results and discoveries, and effectively drive sciences forward.

My advice: be aware, be FAIR!

<a name="Checklist"></a>

## Checklist

<!-- This is a different style than the other chapters, but I really love what Alex provided so I just kept it. -->

- [ ] Don't Touch the Raw Data - back it up somewhere reasonable and keep a read-only copy.

- [ ] Have a plan! - Decide where your data is going to be stored, what its called, when/if it needs to be deleted
      BEFORE you start collecting it and note it down in a data management plan. If you collect sensitive data, plan for
      consent for sharing from the start!

- [ ] Document Everything - You know who the worst person at replying to emails is about what the sampling frequency of
      channel X was. Nope not him, it's actually yourself from a year ago. Keep the documentation with the data!

- [ ] Create the data you want to see in the word - Imagine someone was about to give you a dataset that you needed to
      analyse well in order to get that job you've been dreaming about. What would you want it to look like? That's how
      yours should look.

- [ ] Try not to re-invent the wheel. Before you start creating some crazy new schema, storage format or naming
      protocol - have a quick google, ask your colleagues. Something that's already being used is likely going to be
      better in the long run even if you think there's a better solution. <a name="What-Next"></a>

## What to learn next

If you haven't read the chapters on Open Research and Credit yet, you might want to read it now for more context on how research
data management supports Open Research and how these practises can result in getting attribution for your work (Credit). <a name="Further-Reading"></a>

## Further reading

- [Detailed guidance on sharng personal or sensitive data from the UK Data Service](https://www.ukdataservice.ac.uk/manage-data/legal-ethical/consent-data-sharing.aspx)
- [An overview of storage solutions and their advantages and disadvantages](https://datasupport.researchdata.nl/en/start-the-course/iii-the-research-phase/storing-data)

<a name="Glossary"></a>

## Definitions/glossary

<!-- Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter -->

**RDM:** - Research Data Management  
**DMP:** - Data Management Plan  
**FAIR:** - Findable, Accessible, Interoperable and Reusable  
**METADATA:** - Data that describes other data
**Data Repository** - Online archive or platform that stores and curates your data, ideally issuing a Digital Object Identifier (DOI) so your data is easily findable and citable.
**DOI** Digital Object Identifier

<a name="Bibliography"></a>

## Bibliography

{% bibliography --cited %}
