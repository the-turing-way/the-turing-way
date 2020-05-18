## Open data

The world is witnessing a significant global transformation, facilitated by technology and digital media, and fuelled by data and information. 
This transformation has enormous potential to foster more transparent, accountable, efficient, responsive, and effective research.
Only a very small proportion of the original data is published in conventional journals. 
Existing policies on data archiving notwithstanding, in today’s practice data are primarily stored in private files, not in secure institutional repositories, and effectively are lost to the public (and often even to the researcher who generated the data).
This lack of data sharing is an obstacle to international research (be it academic, governmental, or commercial) for two main reasons:

1. It is generally difficult or impossible to fully reproduce a study without the original data.
2. The data cannot be reused or incorporated into new work by other researchers if they cannot obtain access to it.

Accordingly, there is an ongoing global data revolution that seeks to advance collaboration and the creation and expansion of effective, efficient research programs.
Open data is crucial to meeting these objectives.
Open data is freely available on the internet and any user is permitted to download, copy, analyse, re-process, and re-use it for any other purpose with minimal financial, legal, and technical barriers.

This represents a real shift in how research works and funders are starting to require reasearchers to make their data available and submit data management plans as part of project proposals (see also our chapter on [research data management](/rdm/rdm).
At the moment anyone who wishes to use data from a researcher often has to contact that researcher and make a request.
"Open by default" turns this on its head and says that there should be a presumption of publication for all.
If access to data is restricted, for instance due to security reasons, the justification for this should be made clear.
Free access to, and subsequent use of, data is of significant value to society and the economy, and that data should, therefore, be open by default.

Listed below are the steps to making your data open.

### Steps to make your data open

The steps below help you make your data findable, accessible, interoperable and reusable (FAIR). You can learn more about FAIR principles in the chapter on [research data management](/rdm/rdm).

#### Step 1: Make your data available

Put your data online. 
It should be easily discoverable and accessible, and made available without bureaucratic or administrative barriers, which can deter people from accessing the data. 
Choose a location to store the data which will ensure historical copies of datasets are preserved, archived, and kept accessible as long as they retain value. 
Whenever possible, researchers should provide data in its original, unmodified form.

Data should be free of charge, under [an open licence](https://fossbytes.com/open-sources-license-type/), (for example, those developed by Creative Commons) so it can be reused and remixed by other researchers. 
The data should be available as a whole and at no more than a reasonable reproduction cost. 
That is, no expensive piece of software should be required to read the file as this may obstruct researchers who wish to work with the dataset.

#### Step 2: Make your data easy to understand

Having data available is of no use if it cannot be understood. 
For example, a table of numbers is useless if there are no headings which describe the contents of the rows and columns. 
Therefore you should ensure that open datasets include consistent core metadata, and that the data is fully described. 
This requires that all documentation accompanying data is written in clear, plain language, and that data users have sufficient information to understand the source, strengths, weaknesses, and analytical limitations of the data so that they can make informed decisions when using it.

#### Step 3: Make your data easy to use

The data should be made available in a modifiable, machine-readable format so that it can be effectively used and  manipulated.
It is also important to think about the file formats that information is provided in. 
Data should be presented in structured and standardized formats to support interoperability, traceability, and effective reuse. 
In many cases, this will include providing data in multiple, standardized formats, so that it can be processed by computers and used by people.

#### Step 4: Make your data citeable

Data should be considered a legitimate, citable product of research. 
Making data citeable (and citing data yourself) facilitates the giving of scholarly credit; in scholarly literature, whenever and wherever a claim relies upon data, the corresponding data should be cited. 
Data citations facilitate identification of, access to, and verification of the specific data that support a claim, making it possible to reproduce the underlying analysis. 

You should ensure that anyone who wishes to cite a dataset that you host has access to a persistent identifier such as a DOI in order to do so.
Have a look in the [Credit for reproducible research chapter][credit] to see how to share and cite your data and other outputs.
[credit]: /credit/credit

A data citation should include a persistent method for identification that is unique, and widely understandable by a community. 
There are several types of persistent identifier that could be used to identify datasets: examples include Handles, Archival Resource Keys (ARKs) and Persistent URLs (PURLs), all of which can be resolved to an Internet location. 
The scheme that is gaining most traction is the Digital Object Identifier (DOI).

<a name="doi_system"></a>
The DOI System is an identifier scheme administered by the International DOI Foundation. 
The task of managing DOI registers is delegated to registration agencies (for a list, see [here](http://www.doi.org/registration_agencies.html)) that each specialise in a type of resource. For research datasets, the registration agency is the [DataCite Consortium](https://www.datacite.org/). 
Among the services it provides are human and machine interfaces for simple end-user administration of DOI registrations. 
DataCite also collects metadata about each dataset it registers so they can be more easily understood and identified. 
Any repository wishing to register DOIs needs to obtain a username and password from DataCite to gain access to the registration service. 
While best practice has yet to emerge on some matters, certain conventions are already becoming established.

In particular, when organisations register a DOI for a resource, they should not introduce semantic elements into the suffix, especially not metadata that might change over time (for example, publisher, archive, owner). 
Assign identifiers to static datasets only when no further changes or corrections are expected (such as after quality control checks are complete). 
As DOIs are used to cite data as evidence, the resource to which a DOI points should also remain unchanged, with any new version receiving a new DOI.

Furthermore, whichever identifier scheme you pick make sure it allows the identifier to be resolved to a URL. 
This URL should belong to a landing page that contains descriptive information about the dataset, as well as links or instructions for accessing it. 
You should also ensure that datasets are made citable and identifiable at an appropriate level of granularity.
For example, it would be no use citing CERN's entire data repository as someone attempting to reproduce your work would not be able to find the data used in a specific piece of work without considerable difficulty. 
Where possible you should be able to cite the data used, and only the data used.

### Barriers to data sharing

Sometimes it may not be possible to make data publicly available in its entirety or even in part. 
There are two main reasons this may be the case:

#### Privacy

Many fields of research involve working with sensitive personal data, medical research being the most obvious example.
Individuals must be protected from (re)identification via their personal data used for research. 
Anonymisation of the data may be sufficient in some cases, but ensuring that reidentification is not possible is becoming increasingly difficult due to technical progress, growing computational power and – ironically – more open data. 
For example, reidentification may be possible via data-mining of accessible data and so-called quasi-identifiers, a set of (common) properties that are – in their combination – so specific that they can be used to identify individuals.

Preserving privacy may still be possible if partial or generalised datasets are provided.
For example, providing age bands instead of birth date or only the first two digits of postal codes.
It may also be possible to provide the data in such a format that researchers can query it whist keeping the data itself closed, for example, a user may be able to send a query to retrieve the mean of a dataset, but not be able to access any of the individual datapoints.

Data privacy is also maintained when dealing with data of national or commercial interest, details for which are listed in the chapter [Research Data Management](/rdm/rdm), in the section: *National and commercially sensitive data*.
[rdm]: /rdm
