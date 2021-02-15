(rr-rdm-fair)=
# The FAIR Principles

The FAIR guiding principles for scientific data management and stewardship {cite}`Wilkinson2016fair` were developed as guidelines to improve the **F**indability, **A**ccessibility, **I**nteroperability and **R**eusability of digital assets; all of which support research reproducibility. 
The FAIR principles play an important role in making your data available to others for reuse (see points 4 and 5 of the {ref}`Data Management Plan<rr-rdm-dmp>` chapter). 
Even though the FAIR principles have been defined to allow machines to find and use digital objects automatically, they improve the reusability of data by humans as well.
The capacity of computational systems to find, access, interoperate, and reuse data, with none or minimal human intervention, is essential in today's data-driven era, where humans increasingly rely on computational support to deal with data as a result of the increase in [volume, velocity and
variety](https://www.zdnet.com/article/volume-velocity-and-variety-understanding-the-three-vs-of-big-data/).

This chapter provides an abstract and broad view of what the FAIR principles are. How to put the FAIR principles into practise is discussed in other sub chapters ( {ref}`Data Organisation in Spreadsheets<rr-rdm-fair>`, {ref}`Documentation and Metadata<rr-rdm-metadata>` and {ref}`Sharing and Archiving Data<rr-rdm-sharing>`). You can also use the [Wellcome Getting Started Guide](https://f1000researchdata.s3.amazonaws.com/resources/FAIR_Open_GettingStarted.pdf) or the [How To FAIR](https://howtofair.dk/) website to find out more about the FAIR principles and how to get started. 

It is much easier to make data FAIR if you plan to do this from the beginning of your research project.
One way to do this is to create a Data Management Plan (DMP), in [DMPonline](https://dmponline.dcc.ac.uk/) or just as a text file, to help you think through how to manage your data.


(rr-rdm-fair-theory)=
## Theory

Here is an [overview](https://www.go-fair.org/fair-principles) of what the FAIR principles recommend. In brief, data should be:

**Findable:** The first step in (re)using data is to find them! 
Descriptive metadata (information about the data such as keywords) are essential.

**Accessible:** Once the user finds the data and software they need to know how to acess it. It is possible that authentication and authorisation procedures are necessary, or if data is open with no restrictions.

**Interoperable:** Data needs to be integrated with other data and interoperate with applications or workflows.

**Reusable:** Data should be well-described so that they can be used, combined and extended in different settings.

It is important to stress that making data 'FAIR' is not the same as making it 'open'.
Accessible means that there is a procedure in place to access the data. 
Data should be as open as possible, and as closed as necessary.

The FAIR principles are also applied to software (see [Lamprecht et al. 2020]((https://dx.doi.org/10.3233/DS-190026) and [Hasselbring et al. 2020](https://doi.org/10.1515/itit-2019-0040) and projects. 


(rr-rdm-fair-community)=
## Community involvement

Although started by a community operating in the life science, the FAIR principles have rapidly been adopted by publishers, funders, and pan-disciplinary infrastructure programmes and societies.
Many groups and organisation are working to define guidance and tools to help researchers, and other stakeholders (like librarians, funders, publishers, and trainers) make data more FAIR.

It is important to say that the FAIR principles are aspirational, in that they do not strictly define how to achieve a state of FAIRness, but rather describe a continuum of features, attributes, and behaviours that will move a digital resource closer to that goal.

If you are interested in participating in these communities there are two global and international initiatives that act as umbrella organizations and reference points for many discipline-specific efforts: [GOFAIR](https://www.go-fair.org) and the [Research Data Alliance (RDA)](https://www.rd-alliance.org).
Under GOFAIR, there are many [Implementation Networks (INs)](https://www.go-fair.org/implementation-networks) committed to implementing the FAIR principles.
Under the RDA, there are several groups tackling different aspects relevant to the RDM life cycle. Among these, one [group](https://www.rd-alliance.org/groups/fair-data-maturity-model-wg) is reviewing existing efforts, building on them to define a standard set of common assessment criteria for the evaluation of FAIRness.

(rr-rdm-fair-standards)=
## Community Standards - Metadata and Identifiers

Metadata (to describe and report the data) and unique persistent identifiers (to cite and reference data) are the two pillars of the FAIR principles.
The use of community-defined standards for metadata and identifiers is vital for high-quality, reproducible research, and integrative analysis and comparison of heterogeneous data from multiple sources, domains and disciplines.
However, there is much work in progress, and metadata standards are discipline-specific, or specific to a given digital object.
You need to know what these are and which ones are relevant to your data type in order to mention them in your DMP and use them.

You can use [FAIRsharing](https://fairsharing.org) as a lookup resource to identify and cite the metadata or identifier schemas, databases or repositories that exist for your data and discipline. 
This resource can be useful when creating a data management plan for a grant proposal or funded project or when submitting a manuscript to a journal, for example.
It can be used to identify the recommended databases and repositories, as well as the standards they implement to ensure all relevant information about the data is collected at the source. 
FAIRsharing also operates under GO FAIR and the RDA
and is [widely adopted](https://fairsharing.org/communities) by publishers, funders, and other organizations. 
Like any other FAIR-enabling resources, it will continue to evolve, better linking to DMP and FAIRness assessment tools, to better help you making data FAIR a reality.
