# Data Anonymization

## Prerequisites / recommended skill level
The following sections that are part of the Reproducible Research book will better help understand the motivation for this chapter:

| Prerequisite | Importance |
| -------------|----------|
| {ref}`rr-open`| Helpful |
| {ref}`rr-rdm` | Helpful |
## Summary
The Data Anonymization chapter is intended to provide a comprehensive overview into the privacy considerations involved in contributing to open data and in extension, open research. It outlines the current motivations to anonymize data and aims to delineate the different terminology and techniques surrounding the process of anonymizing data today. It also presents the data-driven considerations that need to be taken before choosing an anonymization technique and closes with an acknowledgment of the re-identification risks that remain despite the use of anonymization. 

## Why This is Useful
Sharing Data is an important prerequisite in facilitating Open Research that is reproducible, re-usable, accountable, and accessible. However, when this data is extremely personal or sensitive in nature, it is often difficult or even impossible to make the data sets publically available in their original form. There is a wide array of ethical concerns about individual privacy as well as a number of data protection laws that rightfully hinder this free sharing of personal data. However, there exist methods that aim to fully anonymize data sets while preserving their statistical utility. And it is imperative for any researcher who intends to share data to apply all relevant anonymization techniques and beyond that, identify any re-identification risks that could ensue from release of this anonymized data.   

## Chapter content
> depending on the content, this might be more structured, e.g. with exercises, gotcha sections etc

## What is Anonymization?
Data Anonymization is the process of protecting private and sensitive information of individuals by erasing, encrypting or translating a variety of attributes in the database such that the people who are described by the data remain anonymous. It is most strictly outlined in the General Data Protection Regulation (GDPR) in the European Union as:
>_“…information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable.”_ - GDPR Recital (26)
While strict, the GDPR provides for data that meets these standards to be collected without consent, used and stored indefinitely.

## Need for Anonymization
* In order to facilitate Open Research, the researcher needs to have the ability to share the data upon which their work was done. This would be virtually impossible if the raw data consisted of personal or sensitive data.
* Legal frameworks across the world are increasingly privacy aware and anonymization is an essential prerequisite if the researcher intends to collect, analyze or store data of a sensitive nature at all.
  * In the Eurpoean Union, the General Data Protection Regulation (GDPR)
  * In the UK, the Data Protection Act (2018)
  * In the United States, a collection of state and federal laws like Health Insurance Portability and Accountability Act (HIPAA) and California Consumer Privacy Act (CCPA)
  * In Singapore, The Personal Data Protection Act,
  these and a variety of other region dependent laws provide strict guidelines and standards for anonymized data.
* The willingness of volunteers to provide data for research seems dependent on their trust in the researcher as well as on an early de-identification process [4]. 
* Retaining volunteer trust and protecting their privacy makes for a healthy and sustainable data science process. Since some of these techniques might be as easy as not collecting/deleting unimportant, sensitive data, a preliminary data anonymization process seems too easy to not do. 

## Understanding Your Data
Determinations regarding the need for anonymization as well as choice of the most effective anonymization techniques that can be applied both depend intimately on the kind of data the researcher possesess.

In terms of need for anonymization, a specific attribute of the dataset may fall under any of the following umbrellas:
* Personally Identifiable Information[1]: data of this nature can be used independently or in conjunction with other data to distinguish or identify the individual. 
  * Direct Identifiers: are able to unambiguously trace back to the individual independently. This includes information like Social Security Number or passport number and must be treated with the highest care and preferably removed if not strongly encrypted.
  * Quasi-Identifiers: while data of this nature may not uniquely identify the source by themselves, in combination with other quasi-identifiers, it may result in a unique identifier. For example, it was proven in 2000, that 87% of Americans could be found simply with the help of their Date of Birth, Gender and Postal Code[2]. Determining what is a quasi identifier is non-trivial and care must be taken in anonymising these unassuming attributes as well.
* Confidential Attributes: Include information like salaries and health conditions, these are sometimes the focus of the dataset and often important for analytics. Microdata protection techniques are often applied here to prevent access to this data on an individual level.
* Non confidential Attributes: is data that doesn't belong to any of the above groups and as such can be spared from the more rigourous anonymization techniques.

The application of anonymization techniques will also vary depending on whether the target data is static or streaming[3]. Static data is data that is entirely available before the anonymization process while streaming data continuously provides new data. Further, the choice of anonymization techniques may vary depending on the whether the data is textual or a different form of multimedia.

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
[1] https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/memoranda/2010/m10-23.pdf [Appendix]
[2] https://dataprivacylab.org/projects/identifiability/paper1.pdf
[3] https://iapp.org/media/pdf/resource_center/Guide_to_Anonymisation.pdf
[4] https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/1472-6947-12-66

  
