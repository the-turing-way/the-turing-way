# The FAIR principles and practices

The FAIR guiding principles for scientific data management and stewardship {% cite Wilkinson2016fair %} have been
developed as guidelines to improve the findability, accessibility, interoperability and re-usability of digital assets;
all of which will support research reproducibility. 
Even though the FAIR principles have been defined to allow machines to automatically find and use digital objects, they improve the reusability of data by humans as well.
The capacity of computational systems to find, access, interoperate, and reuse data, with none or minimal human intervention, is essential in today's data-driven era, where humans increasingly rely on computational support to deal with data as a result of the increase in [volume, velocity and
variety](https://www.zdnet.com/article/volume-velocity-and-variety-understanding-the-three-vs-of-big-data/).

## Theory

Here is a [simple overview](https://www.go-fair.org/fair-principles) of what the FAIR principles recommend. In brief,
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
digital object), and infrastructure (such as software, repositories). For instance, the findability principle F4 defines
that both metadata and data are registered or indexed in a searchable resource (for example, a data repository).
For example, the FAIR principles are also being applied to [software](https://dx.doi.org/10.3233/DS-190026), and projects, where the data and software are both FAIR the research, is more likely to be reproducible.

It is much easier to make data FAIR if you plan to do this from the beginning of your research project.
One way to do
this is to create a Data Management Plan (DMP), in [DMPonline](https://dmponline.dcc.ac.uk/) or just as a text file, to help you think through how to manage your data.
The DMP should include information on data creation (volume, formats/types and workflows), data use (where the raw or 'live' data is being stored), data publication and data archiving at the end of the project
(long-term data storage, or what data is 'kept' at the end of a project).
DMPs should also regularly be updated as the research project progresses or diverge from the initial design.

## Tools and indicators

Although started by a community operating in the life science, the FAIR principles have rapidly been adopted by
publishers, funders, and pan-disciplinary infrastructure programmes and societies, in all disciplines.
Many groups and
organization are working to define guidance and tools to help researchers, as well as other stakeholders (like librarians, funders, publishers, and trainers) to make data FAIR and assess its FAIRness level.

This rapid uptake and community involvement, however, has also caused some confusion and ambiguity on what FAIRness is
and how we can measure it.
It is important to say that the FAIR principles are aspirational, in that they do not
strictly define how to achieve a state of FAIRness, but rather describe a continuum of features, attributes, and
behaviours that will move a digital resource closer to that goal.

Listing all efforts working in and around FAIRness is practically impossible, as this is a fast moving, disperse and
diverse field.
Nevertheless, if you are interested in following the discussion and/or participate in it, here are two
global and international initiatives that act as umbrella organizations and reference points for many discipline
specific efforts: [GOFAIR](https://www.go-fair.org) and the [Research Data Alliance (RDA)](https://www.rd-alliance.org).
Under GOFAIR there are many [Implementation Networks (INs)](https://www.go-fair.org/implementation-networks) committed to implementing elements of the Internet of FAIR Data and Services within the three pillars: GO Build (Technology), GO Change (Culture) and GO Train (Training).
Under the RDA there are several groups tackling different aspects relevant to the RDM life cycle, and among these one [group](https://www.rd-alliance.org/groups/fair-data-maturity-model-wg) is reviewing existing efforts,
building on them to define a common set of common assessment criteria for the evaluation of FAIRness.

## Metadata and identifiers - community standards

Metadata (to describe and report the data) and unique persistent identifiers (to cite and reference data) are the two
pillars of the FAIR principles.
The use of community-defined standards for metadata and identified is vital for high-quality, reproducible research and for the integrative analysis and comparison of heterogeneous data from multiple sources, domains and disciplines.
Although also in this areas there is a lot of work in progress, and especially metadata standards are disciplines specific, or specific to a given digital object, you need to know what these are and which one are relevant to your data type in order to mention them in your DMP and use them.

You can use [FAIRsharing](https://fairsharing.org) as a lookup resource to identify and cite the metadata and/or
identifier schemas, databases or repositories that exist for your data and discipline,
for example, when creating a data management plan for a grant proposal or funded project;
or when submitting a manuscript to a journal, to identify the recommended databases and repositories, as well as the standards they implement to ensure all relevant information about the data is collected at the source. FAIRsharing also operates under GO FAIR and the RDA,
and is [widely adopted](https://fairsharing.org/communities) by publishers, funders, and other organizations; like any other FAIR-enabling resources, it will continue to evolve, better linking to DMP and FAIRness assessment tools, to better help you making data FAIR a reality.
