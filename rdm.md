# Research Data Management

## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful
Having data available is a key component of reproducing an analysis. 
To be able to share data that is understandable and re-usable, research data needs to be managed properly. 
Thus, this chapter lays out good data management practice to allow you to plan your data management activities at the start of your reproducible research project.

## Prerequisites / recommended skill level
The following sections in this handbook provide useful context and complementary information to this chapter:
- Version control
- Open Research 

## Chapter content

### Storage and backup

Data loss can be catastrophic for your research project and happens regularly.
You can prevent data loss by picking suitable storage solutions and backing your data up regularly.

#### Where to store data
Most institutions will provide a *network drive* that you can use to store data.  
*Portable storage media* such as memory sticks (USB sticks) are more risky and vulnerable to loss and damage.  
*Cloud storage* provides a convenient way to store, back and up and retrieve data. You should check terms of use before using them for your research data. 
Especially if you are handling personal or sensitive data, you need to ensure the cloud option is compliant with any data protection rules the data is bound by.  
To add an additional layer of security, you should encrypt devices and/or files where needed.

#### Backups

### Documentation and metadata

#### Step 2: Make your data easy to understand

Having data available is of no use if it cannot be understood. For example a table of numbers is useless if there are no headings which describe what the columns/rows contain. 
Therefore you should ensure that open datasets include consistent core metadata, and that the data is fully described. 
This requires that all documentation accompanying data is written in clear, plain language, and that data users have sufficient information to understand the source, strengths, weaknesses, and analytical limitations of the data so that they can make informed decisions when using it.

- link to metadata standards and e.g. BIDS 

Recycle a lot from http://doi.org/10.5281/zenodo.1914401 (cc-by)



### Sharing and archiving data

## Open data

The world is witnessing a significant global transformation, facilitated by technology and digital media, and fueled by data and information. This transformation has enormous potential to foster more transparent, accountable, efficient, responsive, and effective research.
 Only a very small proportion of the original data is published in conventional scientific journals. Existing policies on data archiving notwithstanding, in today’s practice data are primarily stored in private files, not in secure institutional repositories, and effectively are lost to the public. This lack of access to scientific data is an obstacle to international research for two main reasons:

1. It is generally difficult or impossible to fully reproduce a scientific study without the original data.
2. It often causes unnecessary duplication of research efforts; large amounts of research funds are spent every year to recreate already existing data. Further it inhibits joint research activities on various aspects of the same problem.

Accordingly, there is an ongoing global data revolution that seeks to advance collaboration and the creation and expansion of effective, efficient research programs. Open data is crucial to meeting these objectives.
Open data means that the data is freely available on the internet permitting any user to download, copy, analyse, re-process, and re-use it for any other purpose without financial, legal, or technical barriers other than those inseparable from gaining access to the internet itself.
This represents a real shift in how research works. At the moment anyone who wishes to use scientific data from a researcher often has to contact that researcher and make a request. Open by default turns this on its head and says that there should be a presumption of publication for all. Researchers need to justify data that’s kept closed, for example for security or data protection reasons.
Free access to, and subsequent use of, data is of significant value to society and the economy, and that data should, therefore, be open by default. So, how do you go about making your data open?

### Steps to make your data open

#### Step 1: Make your data available

Put your data online. It should be easily discoverable and accessible, and made available without bureaucratic or administrative barriers, which can deter people from accessing the data. Choose a location to store the data which will ensure historical copies of datasets are preserved, archived, and kept accessible as long as they retain value. As much as possible researchers should provide data in its original, unmodified form.

#### Licensing as potential separate sub chapter
> or call it re-use and cover data citation principles here?
Data should be free of charge, under an open license, (for example, those developed by Creative Commons) so it can be reused and remixed by other researchers. The data should be available as a whole and at no more than a reasonable reproduction cost i.e. no expensive piece of software should be required to read the file as this may obstruct researchers who wish to work with the dataset.


#### Step 3: Make your data easy to use

The data should be made available in a modifiable, machine-readable format so that it can be effectively used and  manipulated.
It is also important to think about the file formats that information is provided in. Data should be presented in structured and standardized formats to support interoperability, traceability, and effective reuse. In many cases, this will include providing data in multiple, standardized formats, so that it can be processed by computers and used by people.

#### Step 4: Make your data citeable

Data should be considered legitimate, citable product of research. Making data citeable (and citing data yourself) facilitate giving scholarly credit; in scholarly literature, whenever and wherever a claim relies upon data, the corresponding data should be cited. Data citations facilitate identification of, access to, and verification of the specific data that support a claim, making science more reproducible. Ensure that anyone wishing to cite a dataset you host can use a persistent identifier that you provide to do so.

A data citation should include a persistent method for identification that is unique, and widely understandable by a community. There are several types of persistent identifier that could be used to identify datasets: examples include Handles, Archival Resource Keys (ARKs) and Persistent URLs (PURLs), all of which can be resolved to an Internet location. The scheme that is gaining most traction is the Digital Object Identifier (DOI).

The DOI System is an identifier scheme administered by the International DOI Foundation. The task of managing DOI registers is delegated to registration agencies (list [here](http://www.doi.org/registration_agencies.html)) that each specialise in a type of resource. For research datasets, the registration agency is the [DataCite Consortium](https://www.datacite.org/). Among the services it provides are human and machine interfaces for simple end-user administration of DOI registrations. DataCite also collects metadata about each dataset it registers so they can be more easily understood and found. Any repository wishing to register DOIs needs to obtain a username and password from DataCite to gain access to the registration service. While best practice has yet to emerge on some matters, certain conventions are already becoming established:

When organisations register a DOI for a resource, they should not introduce semantic elements into the suffix, especially not metadata that might change over time (e.g. publisher, archive, owner). Assign identifiers to static datasets only when no further changes or corrections are expected (i.e. after quality control checks are complete). As DOIs are used to cite data as evidence, the resource to which a DOI points should also remain unchanged, with any new version receiving a new DOI.

Whichever identifier scheme you pick make sure it allows the identifier to be resolved to a URL. This URL should belong to a landing page that contains descriptive information about the dataset, as well as links or instructions for accessing it. You should also ensure that datasets are made citable and identifiable at an appropriate level of granularity, i.e it would be no use citing CERN's entire data repository as someone attempting to reproduce your work would not be able to find the data used in a specific piece of work without considerable difficulty. Where possible it should be possible to cite the data used, and only the data used.

### Barriers to data sharing/ Sensitive data

- anonymization
- synthetic data?
- consent for sharing
- data sharing agreements?

Sometimes it may not be possible to make data publicly available in its entirety or even in part. There are two main reasons this may be the case:

#### Privacy

Many fields of scientific disciplines involve working with sensitive personal data, medical research being the most obvious example.
Individuals must be protected from (re)identification via their personal data used for research. Anonymisation of the data may be sufficient in some cases, but ensuring that reidentification is not possible is becoming increasingly difficult due to technical progress, growing computational power and – ironically – more open data. For example reidentification may be possible via data-mining of accessible data and so-called quasi-identifiers, a set of (common) properties that are – in their combination – so specific that they can be used to identify.

Preserving privacy may still be possible if partial or generalised datasets are provided e.g. age bands instead of birth date or only the first two digits of postal codes. It may also be possible to provide the data in such a format that researchers can query it whist keeping the data itself closed, e.g. a user may be able to send a query to retrieve the mean of a dataset, but not be able to access any of the individual datapoints.

#### National and commercially sensitive data

In many cases companies are understandably unwilling to publish much of their data. The reasoning goes that if commercially sensitive information of a company is disclosed, it will damage the company’s commercial interests and undermine competitiveness. This is based on the thinking that in competitive markets, innovation will only occur with some protection of information: if a company spends time and money developing something new, the details of which are then made public, then its competitors can easily copy it without having to invest the same resources. The result is that no-one would innovate in the first place. Similarly governments are often unwilling to publish data that relates to issues such as national security due to public safety concerns.

In such cases it may not be possible to make data open, or it may only be only possible to share partial/obscured datasets as outlined in the section above on privacy.


### FAIR data

- overview of principles and how the above applies/ feeds in
- also make a reference to apply FAIR to software and if FAIR software + data = reproducible research? 

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography
> Credit/urls for any materials that form part of the chapter's text.

