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
efficiency in research workflows, and also greater reach and impact, as data become FAIR (Findable, Accessible,
Interoperable and Reuseable). Data should be stored in multiple locations and backed-up regularly to prevent loss or
data corruption. Clearly describing data using documentation and metadata ensures that others know how to access, use
and re-use your data, and also enable conditions for sharing and publishing data to be outlined.

<a name="Why-useful"></a>

## How this will help you/ why this is useful

To be able to share data that is understandable and re-usable by third parties, research data needs to be managed
properly. The FAIR principles provide guidance on how to make data discoverable and reusable. FAIR data is a key
component of reproducing an analysis. However, FAIR data is not a synonym for open data or quality data. This chapter
lays out good data management practice to allow you to plan your data management activities at the start of your
reproducible research project.

## Chapter content

<a name="What-Data"></a>

### What Is Data?

Data are all digital objects that you use and produce during your research life cycle, encompassing datasets, software,
code, workflow, models, figures, tables, images, articles. Data are your research asset. In some fields it's obvious
what data means - you have observations or results of simulations. However, in other fields, particularly in Social
Sciences, Humanities or Arts, you may be thinking "I don't think I have any data". A good way of thinking about what
might be classed as data that needs to be managed is to ask yourself the questions "What is the information that I need
to use and write about in my paper or book?", "What information would I need to back up my conclusions?" and "What
information is needed by a third party to understand and possibly replicate the research that I've done?". This
information is your data.

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
all of which will support research reproducibility. Defined and endorsed by a growing community, these principles put a
specific emphasis on enhancing the ability of machines to automatically find and use digital objects, in addition to
supporting its reuse by individuals throughout their life cycle. The capacity of computational systems to find, access,
interoperate, and reuse data, with none or minimal human intervention, is essential in today's data-driven era, where
humans increasingly rely on computational support to deal with data as a result of the increase in volume, velocity and
variety and complexity.

<a name="Theory"></a>

#### Theory

Here is a [simple overview](https://www.go-fair.org/fair-principles) of what the FAIR principles recommend. In breif,
data should be:

**Findable:** the first step in (re)using data is to find them, and descriptive metadata is essential.

- F1. (Meta)data are assigned a globally unique and persistent identifier
- F2. Data are described with rich metadata (defined by R1 below)
- F3. Metadata clearly and explicitly include the identifier of the data they describe
- F4. (Meta)data are registered or indexed in a searchable resource

**Accessible:** to get data one needs to know if authentication and authorisation is necessary, or if data is open with
no restrictions.

- A1. (Meta)data are retrievable by their identifier using a standardised communications protocol
- A1.1 The protocol is open, free, and universally implementable
- A1.2 The protocol allows for an authentication and authorisation procedure, where necessary
- A2. Metadata are accessible, even when the data are no longer available

**Interoperable:** data need to be integrated with other data and/or interoperate with applications or workflows.

- I1. (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.
- I2. (Meta)data use vocabularies that follow FAIR principles
- I3. (Meta)data include qualified references to other (meta)data

**Reusable:** data should be well-described so that they can be used or replicated in different settings.

- R1. Meta(data) are richly described with a plurality of accurate and relevant attributes
- R1.1. (Meta)data are released with a clear and accessible data usage license
- R1.2. (Meta)data are associated with detailed provenance
- R1.3. (Meta)data meet domain-relevant community standards

It is important to stress that making data 'FAIR' is not the same as making it 'open' (as accessibility principle
clearly explains). Data should be as open as possible, as closed as necessary.

The FAIR principles refer to three types of entities: data (as any digital object), metadata (information about that
digital object), and infrastructure (such as software and repositories). For instance, the findability principle F4 defines
that both metadata and data are registered or indexed in a searchable resource (such as a data repository). For example,
the FAIR principles are also being applied to [software](https://doi.org/10.6084/m9.figshare.7449239.v2), and projects
where the data and software are both FAIR the research is more likely to be reproducible.

It is much easier to make data FAIR if you plan to do this from the beginning of your research project. One way to do
this is to create a Data Management Plan (DMP), in [DMPonline](https://dmponline.dcc.ac.uk/) or just as a text file, to
help you think through how to manage your data. The DMP should include information on data creation (volume,
formats/types and workflows), data use (where the raw or 'live' data is being stored), data publication and data
archiving at the end of the project (long-term data storage, or what data is 'kept' at the end of a project). DMPs
should also regularly be updated as the research project progresses or diverge from the initial design.

<a name="Tools-indicators"></a>

#### Tools and indicators

Altought started by a community operating in the life science, the FAIR principles have rapidly been adopted by
publishers, funders, and pan-disciplinary infrastructure programmes and societies, in all disciplines. Many groups and
organization are working to define guidances and tools to help researchers, as well as other stakeholders (such as
librarians, funders, publishers, and trainers) to make data FAIR and assess its FAIRness level.

This rapid uptake and community involvement, however, has also caused some confusion and ambiguity on what FAIRness is
and how we can measure it. It is important to say that the FAIR principles are aspirational, in that they do not
strictly define how to achieve a state of FAIRness, but rather describe a continuum of features, attributes, and
behaviors that will move a digital resource closer to that goal.

Listing all efforts working in and around FAIRness is practically impossible, as this is a fast moving, disperse and
diverse field. Nevethless, if you are interested in following the discussion and/or participate in it, here are two
global and international initiatives that act as umbrella organizations and reference points for many discipline
specific efforts: [GOFAIR](https://www.go-fair.org) and the [Research Data Alliance (RDA)](https://www.rd-alliance.org).
Under GOFAIR there are many [Implementation Networks (INs)](https://www.go-fair.org/implementation-networks) committed
to implementing elements of the Internet of FAIR Data and Services within the three pillars: GO Build (Technology), GO
Change (Culture) and GO Train (Training). Under the RDA there are several groups tackling different aspects relevant to
the RDM life cycle, and among these one [group](https://www.rd-alliance.org/groups/fair-data-maturity-model-wg) is
reviewing existing efforts, building on them to define a common set of common assessment criteria for the evaluation of
FAIRness. Watch this space!

<a name="Metadata-identifiers"></a>

#### Metadata and identifiers - community standards

Metadata (to describe and report the data) and unique persistent identifiers (to cite and reference data) are the two
pillars of the FAIR principles. The use of community-defined standards for metadata and identified is vital for
high-quality, reproducible research and for the integrative analysis and comparison of heterogeneous data from multiple
sources, domains and disciplines. Although also in this areas there is a lot of work in progress, and expecially
metadata standards are disciplines specific, or specific to a given digital object, you need to know what these are and
which one are relevant to your data type in order to mention them in your DMP and use them.

You can use [FAIRsharing](https://fairsharing.org) as a lookup resource to identify and cite the metadata and/or
identifier schemas, databases or repositories that exist for your data and discipline, for example, when creating a data
management plan for a grant proposal or funded project; or when submitting a manuscript to a journal, to identify the
recommended databases and repositories, as well as the standards they implement to ensure all relevant information about
the data is collected at the source. FAIRsharing also operates under GOFAIR and the RDA, and is
[widely adopted](https://fairsharing.org/communities) by publishers, funders, and other organizations; like any other
FAIR-enabling resources, it will continue to evolve, better linking to DMP and FAIRness assessment tools, to better help
you maing data FAIR a reality.

<a name="Storage-backup"></a>

### Storage and backup

Data loss can be catastrophic for your research project and can happen often. You can prevent data loss by picking
suitable storage solutions and backing your data up frequently.

<a name="Where-store"></a>

#### Where to store data

- Most institutions will provide a _network drive_ that you can use to store data.
- _Portable storage media_ such as memory sticks (USB sticks) are more risky and vulnerable to loss and damage.
- _Cloud storage_ provides a convenient way to store, back and up and retrieve data. You should check terms of use
  before using them for your research data.

Especially if you are handling personal or sensitive data, you need to ensure the cloud option is compliant with any
data protection rules the data is bound by. To add an additional layer of security, you should encrypt devices and/or
files where needed.

Your institution might provide local storage solutions and policies or guidelines restricting what you can use. Thus, we
recommend you familiarise yourself with your local policies anc recommendations.

When you are ready to release the data to the wider community, you can also search for the appropriate
[databases and repositories](https://fairsharing.org/databases) in FAIRsharing, according to your data type, and type of
access to the data. Major
[publishers are progressively defining clearer recommendations for data deposition and sharing](https://fairsharing.org/recommendations),
endorsing specific generics as well as domain-sepecific databases and repositories.

<a name="Backups"></a>

#### Backups

To avoid loosing your data, you should follow good backup practices.

- You should have 2 or 3 copies of your files, stored on
- at least 2 different storage media,
- in different locations.

The more important the data and the more often the datasets change, the more frequently you should back them up. If your
files take up a large amount of space and backing up all of them would be difficult or expensive, you may want to create
a set of criteria for when you back up the data. This can be part of your data management plan.

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
- Don't leave any cells empty
- Put just one thing in a cell
- Organize the data as a single rectangle
- Create a data dictionary
- Don't include calculations in the raw data files
- Don’t use font color or highlighting as data
- Choose good names for things
- Make backups
- Use data validation to avoid data entry mistakes
- Save the data in plain text files

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
- Data should be stored in logical and heirarchical folder structures with a README file used to describe the structure.
  The README file is helpful for others and will also help you find your data in the future
  {% cite Fuchs2018documentation %}.

<a name="Sharing-Archiving"></a>

### Sharing and archiving data

<a name="Motivations-Sharing"></a>

#### Motivations for sharing data

The world is witnessing a significant global transformation, facilitated by technology and digital media, and fueled by
data and information. This transformation has enormous potential to foster more transparent, accountable, efficient,
responsive, and effective research. Only a very small proportion of the original data is published in conventional
scientific journals. Existing policies on data archiving notwithstanding, in today’s practice data are primarily stored
in private files, not in secure institutional repositories, and effectively are lost to the public. This lack of access
to scientific data is an obstacle to international research for two main reasons:

1. It is generally difficult or impossible to fully reproduce a scientific study without the original data.
2. It often causes unnecessary duplication of research efforts; large amounts of research funds are spent every year to
   recreate already existing data. Furthermore, it inhibits joint research activities on various aspects of the same
   problem.

Accordingly, there is an ongoing global data revolution that seeks to advance collaboration and the creation and
expansion of effective, efficient research programs. Sharing data openly is crucial to meeting these objectives. Open
data means that the data is freely available on the internet permitting any user to download, copy, analyse, re-process,
and re-use it for any other purpose without financial, legal, or technical barriers other than those inseparable from
gaining access to the internet itself. This represents a real shift in how research works. At the moment anyone who
wishes to use scientific data from a researcher often has to contact that researcher and make a request. Open by default
turns this on its head and says that there should be a presumption of publication for all. Researchers need to justify
data that’s kept closed, for example for security or data protection reasons. Free access to, and subsequent use of,
data is of significant value to society and the economy, and that data should, therefore, be open by default. Research
is often publically-funded, so the results of this research should be openly available as a public good.
<a name="Steps-Share"></a>

### Steps to share your data

#### Step 1: Select what data you want to share

Not all data can be made openly available, due to ethical and commercial concerns, and you may decide that some of your
intermediate data is too large to share. So you first need to decide which data you need to share for others to be able
to reproduce your research.

#### Step 2: Choose a data repository or other sharing platform

Data should be shared in a formal, open, and indexed data repository where possible so that it will be accessible in the
long-run. Suitable data repositories by subject, content type or location can be found at
[Re3data.org](https://www.re3data.org/) and in [FAIRsharing](https://fairsharing.org/databases) where you can also see
which standards (metadata and identifier) the repositories implement and which journal/publisher recommend them. If
possible use a repository which assigns a DOI, a digital object identifier, to make it easier for others to cite your
data.

#### Step 3: Upload your data and documentation

In line with the FAIR principles outlined above upload the data in open formats as much as possible and include
sufficient documentation and metadata that someone else can understand your data.

#### Step 4: Choose a licence and link to your paper and code

So that others know what they can do with your data you need to apply a licence to your data. The most commonly used
licences are [Creative Commons](https://creativecommons.org/choose/),
[Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), or an
[Open Data Commons Attribution License](https://opendatacommons.org/licenses/by/index.html). To get maximum value from
data sharing make sure that your paper and code both link to your data, and vice versa, to allow others to best
understand your project. <a name="Barriers-Share"></a>

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
forms cover sharing anonymised data with other researchers. Research so far suggests that study participants are usually
less concerned about the data being archived and shared than researchers think {% cite Kuula2010archiving %}.
Participant information sheets and consent forms should include how research data will be stored, preserved and used in
the long-term, and how confidentiality will be protected when needed.

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
that no-one would innovate in the first place. Similarly governments are often unwilling to publish data that relates to
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

If you haven't read the chapter on Open Research yet, you might want to read it now for more context on how research
data management supports Open Research. <a name="Further-Reading"></a>

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
<a name="Bibliography"></a>

## Bibliography

{% bibliography --cited %}
