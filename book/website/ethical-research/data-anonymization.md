# Data Anonymization

## Prerequisites / recommended skill level
The following sections of the Reproducible Research book will better help understand the motivation for this chapter:
<!--would appreciate some help with linking the sections to this table-->

| Prerequisite | Importance | 
| -------------|----------|
| [Open Research](/book/website/reproducible-research/open.md)| Helpful |
| [Research Data Management](/book/website/reproducible-research/rdm.md) | Helpful |
## Summary
The Data Anonymization chapter intends to provide an overview into the privacy considerations involved in contributing to open data and in extension, open research.
It outlines some current motivations to anonymize data and aims to delineate a few different terminologies, techniques and tools surrounding the process of anonymizing data today.
It also presents some data-driven considerations that need to be taken before choosing an anonymization technique and closes with an acknowledgment of the re-identification risks that remain despite the use of anonymization. 

## Why This is Useful
Sharing Data is an important prerequisite in facilitating Open Research that is reproducible, re-usable, accountable, and accessible.
However, when this data is extremely personal or sensitive in nature, it is often difficult or even impossible to make the data sets publicly available in their original form. 
There is a wide array of ethical concerns about individual privacy as well as a number of data protection laws that rightfully hinder this free sharing of personal data.
To this effect, there exist methods that can be employed by researchers to protect and anonymize their data while preserving their statistical utility. 
And it is imperative for any researcher who intends to share data to apply all relevant anonymization techniques and beyond that, identify any re-identification risks that could ensue from the release of this anonymized data.   

## What is Anonymization?
Data Anonymization is the process of protecting private and sensitive information of individuals by erasing, encrypting or translating a variety of attributes in the database such that the people who are described by the data remain anonymous. 
It is most strictly outlined in the General Data Protection Regulation (GDPR) of the European Union as:
>_“…information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable.”_ - GDPR Recital (26)

While strict, the GDPR provides for data that meets these standards to be collected without consent, used and stored indefinitely.

## Need for Anonymization
In order to facilitate Open Research, the researcher needs to have the ability to share the data upon which their work was done. 
This would be virtually impossible if the raw data consisted of personal or sensitive data. 
Indeed, legal frameworks across the world are increasingly sensitive to privacy concerns and hence, anonymization is an essential prerequisite if the researcher intends to collect, analyze or store data of a sensitive nature at all. 
Examples of such legislation are:
  * The General Data Protection Regulation (GDPR), in the European Union
  * A collection of state and federal laws like Health Insurance Portability and Accountability Act (HIPAA) and California Consumer Privacy Act (CCPA), in the United States,
  * The Personal Data Protection Act, in Singapore,
  
Further, the willingness of volunteers to provide data for research appears dependent on their trust in the researcher as well as on an early de-identification process {cite}`dankar2012reidentify`. 
Retaining volunteer trust and protecting their privacy makes for a healthy and sustainable data science process. 
Since some of these techniques might be as easy as not collecting/deleting unimportant, sensitive data, a preliminary data anonymization process seems too easy to not do. 

## Considerations When Anonymizing Data
Determinations regarding the need for anonymization as well as choice of the most effective anonymization techniques that can be applied both depend intimately on the kind of data the researcher possesses.
### Understanding Your Data
In terms of need for anonymization, a specific attribute of the dataset may fall under any of the following umbrellas:
* **Personally Identifiable Information (PII)** {cite}`Orzag2010DataAnon`: data of this nature can be used independently or in conjunction with other data to distinguish or identify the individual. 
  * **Direct Identifiers**: are able to unambiguously trace back to the individual independently. 
  This includes information like Social Security Number or passport number and must be treated with the highest care and preferably removed if not necessary or at the very least they must be strongly encrypted.
  * **Quasi-Identifiers**: while data of this nature may not uniquely identify the source by themselves, in combination with other quasi-identifiers, it may result in a unique identifier. 
  For example, it was proven in 2000, that 87% of Americans could be found simply with the help of their Date of Birth, Gender and Postal Code {cite}`sweeney2000identify`. 
  Determining what is a quasi-identifier is non-trivial and care must be taken in anonymising these unassuming attributes as well.
* **Confidential Attributes**: Include information like salaries and health conditions, these are sometimes the focus of the dataset and often important for analytics. 
Microdata protection techniques, that hide the individual data while preserving the statistical properties of the database, are often applied to protect these attributes.
* **Non Confidential Attributes**: this constitutes data that doesn't belong to any of the above groups and as such can be spared from the more rigorous anonymization techniques.

The application of anonymization techniques will also vary depending on whether the target data is static or streaming {cite}`PDPC2018Anonymization`. 
Static data is data that is entirely available before the anonymization process while streaming continuously provides new data with time. 
An example for streaming data would be website user analytics data. 
In case of streaming data, relationships are not fully established as new data keeps streaming, hence it requires special considerations when anonymizing. 
Further, the choice of anonymization techniques may vary depending on whether the data is textual or a different form of multimedia as the needs of the different forms vary widely. While textual data may require deletion or replacement of words, video data might require blurring whereas audio data may require bleeping and so on.

<!--Not sure if this below section is necessary -irenekp-->

There exists a variety of anonymization techniques that vary in the level of data loss they cause and also vary in terms of the amount of statistical and relationship data that they preserve.
### Existing Techniques

This section provides a quick overview of a variety of anonymization techniques. 
Combinations of these anonymization techniques can be used in accordance to the specific needs of a dataset and its expected utility.

* **Attribute/Record Suppression**: involves deleting an entire column/row of sensitive data that cannot be anonymized.
* **Character Masking**: replacing actual text with a constant symbol (like x, * and so on), care should be taken to see whether length of the replaced data is also sensitive and should be hidden.
* **Generalization**: Decrease the granularity of the data. For example, make the postal code less specific, zoom out in terms of geographical location, convert birthdays to ages, ages to age ranges and so on. 
* **Aggregation**: Decrease granularity of the data by converting the listed records into summative statistical measures like average, sum and so on.
* **Query systems**: provide access to the data only through a set of specialized queries that can obtain statistical information about the data but not any individual level data.
* **Data Perturbation**: involves adding noise to the data to prevent identification. If done without taking into consideration the probability distribution, it affects data accuracy adversely.
* **Swapping**: involves rearranging the data across records such that all individual values are still reflected in the final dataset. 
This method can be used when analysis is on an intra-attribute level and doesn’t depend on record level attribute relationships.


## Reidentification Risks

In 2007, Netflix released anonymized movie ratings of almost 500K users. 
Despite the non-availability of usernames, some University of Texas researchers were able to reidentify users by using the Internet Movie Database as a base source {cite}`narayanan2006break`. 
This highlights the importance of considering the potential re-identification risks before releasing insufficiently anonymized data. 
There are three key types of reidentification risks that the researcher has to account for when anonymizing their data. 
* **Identity Disclosure**: This form of disclosure takes place when an individual is re-identified with a high degree of confidence due to either insufficient anonymization or identification through linking with external databases among other methods.
* **Attribute Disclosure**: Attribute Disclosure takes place when an intruder is able to ascertain that an attribute in a database belongs to a specific user with a great degree of certainty. 
Having outliers in the database increases the possibility of this form of disclosure. 
* **Inference Disclosure**: Inference Disclosure occurs when an inference can be made about an individual with a high level of confidence irrespective of whether or not they belong to the dataset. 
Demographical statistics like "82% of millennials use this social media" would help make inferences about people who weren't polled as well.

In addition to considering the variety of disclosure risks, it is also important to consider the various motivations and competencies a hypothetical intruder might possess. 
Potential intruders can be generalized into three main categories {cite}`EHIL2008PrivacyRisks`:
* **Prosecutor**: here, the intruder is interested in finding a specific person in a specific database. 
Risks pertaining to this intruder can be measured by determining the uniqueness of quasi-identifiers in a database. 
* **Journalist**: While they still want to re-identify individuals, this type of attacker doesn't usually focus on which records are re-identified. 
As this intruder depends on other pre-existing public databases (like voter registration lists) to re-identify individuals, the statistical risk analysis for this type of intruder will rely heavily on the nature of public databases available.
* **Marketer**: this type of intruder wants to maximise the number of individuals that they intend to reidentify at the cost of mis-identifying some of the records. 
They too, try to map the de-identified data with available databases.

<!--not sure where this subheading fits(?), also not sure if this section is necessary for the book(?) -irenekp -->
### Privacy Models 
Measurement of reidentification risks is a non-trivial problem, however, there exists a class of helpful privacy models that act both as techniques of anonymization as well as measures for the risk levels of the data. 
These mainly focus on expressing the uniqueness of a record in a database as most risk evaluations today are focused on determining record uniqueness {cite}`dankar2012reidentify`. 
This privacy class includes, among others:
* **k-anonymity**: Released data is said to have k-anonymity when an individual cannot be distinguished from k-1 others who have similar properties.
* **ℓ-diversity**: Is an extension of k-anonymity that protects data against attribute disclosure by ensuring that each sensitive attribute has at least ℓ "well represented" values in each equivalence class. 
* **t-closeness**: As an extension of ℓ-diversity, this privacy model prevents attribute disclosure by treating the values of an attribute distinctly by taking into account the distribution of data values for that attribute.

There are a variety of similar measures that extend these privacy models by focusing on obscuring different statistical properties that could otherwise act as loopholes by facilitating re-identification. 

### When to evaluate re-identification risks?
When releasing anonymized data, while it may appear that none of the current day tools might be able to re-identify it, the researcher should account for technological advancements in the future. 
Evaluation of re-identification risks is not intended to be a one-time process that takes place at the time of release of data. 
The researcher should periodically test and re-evaluate the identifiability of their data over time with consideration of the newly available tools and methods.

## Common Misconceptions
There are many data-privacy related terms that are often used interchangeably in ordinary language. 
Below, some of these concepts are introduced for the purpose of clarifying how they differ from traditional data anonymization.
  * Synthetic Data - is fake information that is artificially generated to closely resemble the original data.
  <!-- (ambiguous: wikipedia calls it a subset of anonymized data) - irenekp -->
  * Pseudonymization - here, Personally Identifiable fields are replaced by an unrelated and randomized reference number. 
  However, if there exists a database that maps the Personally Identifiable fields with the reference number, the process becomes reversible and identifiable.
  * Storing unedited source data after anonymization invalidates the anonymization process and results in the new data being pseudo-anonymized data instead, which does not meet the same legal requirements.
### Does Anonymization render data useless for analytics?
  Anonymizing data doesn't necessarily destroy the quality of the data or make it ineligible for data analytics purposes. 
  Depending on the technique used and the level of data required, it is possible to retain key relationships and statistical properties required for analytics. 
  This requires the researcher to pick their anonymization techniques with greater care. 
  In fact, many anonymization techniques provide a generalized trend instead of individual data, if the loss of an individual's data makes a huge difference to the researcher's machine learning/data science models, there is a possibility that the model was overfit initially {cite}`Lorica2018AnonymizeML`. 
  In general for statistical uses, the researcher should be careful if they are picking perturbative data anonymization techniques that add noise to, and change the distribution characteristics of the data.

<!-- Not sure if this below section is necessary -irenekp -->
## Anonymization Tools
There are several open source tools that aid the process of anonymizing data. 
* [Cornell's Anonymization Toolkit](https://sourceforge.net/projects/anony-toolkit/)
* [sdcMicro: Statistical Disclosure Control Methods for Anonymization of Data and Risk Estimation](https://cran.r-project.org/web/packages/sdcMicro/) - an R library
* [IQDA Qualitative Data Anonymizer](https://sourceforge.net/projects/datatool/)
* [Amnesia](https://amnesia.openaire.eu/) by Openaire

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next
> recommended next chapters that are a good next step up

## Further reading
<!--I don't fully understand licenses (?) so not sure which of my references are ineligible -irenekp-->

[The Anonymization Code by the Information Commissioner's Office, UK](https://ico.org.uk/media/1061/anonymisation-code.pdf) \
[Privacy and data anonymization from a data scientist’s point of view](https://blog.concurlabs.com/privacy-and-data-anonymization-from-a-data-scientists-point-of-view-956226888d6b)\
[Evaluation of Re-identification Risk for Anonymized Clinical Documents](https://www.phusewiki.org/docs/Conference%202017%20RG%20Papers/RG02.pdf) \
[Privacy models](https://arx.deidentifier.org/overview/privacy-criteria/)\
[Protecting Privacy when Disclosing Information: k-Anonymity and Its Enforcement through Generalization and Suppression](https://epic.org/privacy/reidentification/Samarati_Sweeney_paper.pdf) 


## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography

[1] https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/memoranda/2010/m10-23.pdf [Appendix]\
[2] https://dataprivacylab.org/projects/identifiability/paper1.pdf \
[3] https://iapp.org/media/pdf/resource_center/Guide_to_Anonymisation.pdf \
[4] https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/1472-6947-12-66 \
[5] https://www.oreilly.com/radar/podcast/how-privacy-preserving-techniques-can-lead-to-more-robust-machine-learning-models/ \
[6] https://arxiv.org/abs/cs/0610105 \
[7] http://www.ehealthinformation.ca/wp-content/uploads/2014/08/2009-De-identification-PA-whitepaper1.pdf \
[8] https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/1472-6947-12-66
  
