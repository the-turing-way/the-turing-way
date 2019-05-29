# Ethical Decision Making

## Prerequisites / recommended skill level
> other chapters that should have been read before or content you should be familiar with before you read this

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| Chapter/topic | How important it is | Any notes |

## Summary
Over the past years, there has been a great and heated discussion over “AI ethics”, motivated in part by discomfort over targeted advertising, algorithmic bias and fake news. AI systems sit on top of social and material practices that are culturally and historically situated and they silently structure our lives. They determine our search results and the ads we see online, match patients to therapists and doctors and passengers to ridesharing drivers. But they also can predict ethnicity, who is a terrorist, if one gets a loan, if and how we are targeted in a presidential election and if one will get fired. 

Ethical questions around AI systems are wide-ranging, spanning their creation, uses, and outcomes. There are also questions about the set of values that are reflected in AI and how machines can recognize human ethical paradigms.

This chapter IS about the broader social concerns as well as the technical methods and best practices for studying and evaluating the effects of AI systems and the choices made by their designers and users. We will try to be comprehensive but concise, and also offer actionable suggestions, best practices, and tools to inform your practice. We cannot recommend a specific action (e.g., "remove variable X from your model") and we aknowledge that they are domain specific concerns not covered here. 

This chapter is NOT about research ethics, i.e. the duties, rights, costs and benefits that define the relationships among researchers, participants, and the public. Ethical considerations are very important and well understood in research, and many professional associations and academic bodies have adopted codes and policies that outline ethical behavior and guide researchers regarding IP, social responsibility, confidentiality, non-discrimination, and many others.

## How this will help you/ why this is useful
We encourage teams and practitioners to take their ethical responsibilities seriously and consider how those practices apply in their contexts. We encourage you to engage in sincere dialogue with each other and the broader data science community and civil society. However, it's not up to data scientists alone to decide what ethical action is. This conversation should be part of organizational and legal commitments to an ethical course of action. This chapter will focus on issues where data scientists have a particular responsibility and perspective. 

## Chapter content

## An End-to-End Approach 
Ethical decision making in data science doesn’t start with the data and it’s not a checklist, but rather a process. It starts with a culture of transparency and inclusivity in teams, academic labs, and organizations. 

## A.Project Selection, Scoping, and Team

### A1. Think critically about the problem you are trying to solve or understand. 
Is it a symptom of a systemic issue? Who is causing it and who is affected by it? When did the problem first occur? When did it become significant? Is this a new problem or an old one? How many people are affected by the problem? Who else is working on it? How significant is it? Who is funding you to work on it? The reason for this reflection is that if we are not mindful of a problem’s dynamics as well as power and information asymmetries we might be trying to answer the wrong questions.

### A2. Think critically about using data science methods at all. 
If you define the problem in terms of possible solutions and methods like data science, you’re closing the door to other, possibly more effective solutions and you might be wasting your time. It is important to recognize when data science is not the solution to the task at hand, when resources are better directed elsewhere or when it can be simply a bad idea in the first place (i.e. facial recognition)

### A3. Is your team inclusive and/or representative of the population being studied? 
Does your team include, consider and/or engage with those affected by your work? Data science researchers and practitioners should give voice to the target communities through their projects and engage with their realities. Instead of data extraction, practitioners should care about those and supports people in the responsible collection and use of data.

## B. Data Collection

### B1. What is “Data”?
* Data is characterized by volume, variety, and velocity but also veracity. Other scholars have attributed qualities such as exhaustivity (when an entire system is captured, rather than being sampled), fine-grained and uniquely indexical, relationality, extensionality, scalability, variability (data whose meaning can constantly be shifting in relation to the context in which they are generated). 
* Additionally, not all data is created or even collected equally and data inherit its ontology 62, that is, what is considered as meaningful data depend on the assumptions of those defining the data. All those dimensions, therefore, influence what constitutes data and what goes in for processing.

### B2. Consider data collection bias
Have you considered:
* Sources of bias that could be introduced during the data collection process? (Bias can take the form of measurement bias is the selection of data or samples in a way that does not represent the parameters or distribution of the population. It can be social bias, where data sources are based on historically discriminatory decisions and actions by humans or were informed by laws no longer in force.)
* Potential errors, ommissions, and exclusions? 
* Whether the data was collected or labeled by humans or an automated system?
* Patterns in the data and whether they are likely to stay static or change over time? 
* The sampling strategy used to collect the data?

### B3. Plan your consent mechanisms for processing & sharing data 
* Consent is an ethical requirement for most research projects and must be implemented throughout the research lifecycle. When you seek consent, you have to explain to potential participants exactly what will happen to the data that they provide and they should have a clear understanding of those data uses. For interviews or research where sensitive or confidential data are gathered, the use of written consent forms is recommended over verbal. 
* There are various special cases that have different implications for data sharing, like working with audiovisual data or working in medical research, internet, and social media, working with administrative data, children and young adults, people with learning disabilities or within the workplace. The UK Data Service provides various useful forms and examples for understanding and obtaining consent such as this model consent form and this example consent form for sharing audio-visual data separately from consent for sharing textual data.

### B4.  Choose appropriate anonymization techniques and methodologies
* Anonymising research data is best planned early in the research process and should be considered alongside getting informed consent for data sharing or imposing access restrictions. Personal data should never be disclosed from research information, unless a participant has given consent to do so, ideally in writing. Do not collect information not relevant to the analysis. 

* There are various techniques for anonymizing quantitative data and you can find an overview of how and when to use them here: 
```Attribute Suppression: removal of an entire part of data in a dataset.
_Record Suppression_:  the removal of an entire record in a dataset (it affects multiple attributes at the same time)
_Character Masking_: the change of the characters of a data value, e.g. by using a constant symbol (e.g. “*” or “x”). 
_Pseudonymisation_: The replacement of identifying data with made up values
_Generalisation (Re-coding_: a deliberate reduction in the precision of data. E.g. converting a person’s age into an age range
_Swapping_: to rearrange data in the dataset such that the individual attribute values are still represented in the dataset, but generally, do not correspond to the original records.
_Data Perturbation_: the values from the original dataset are modified to be slightly different
_Synthetic Data_: generate synthetic datasets directly and separately from the original data, instead of modifying the original dataset. 
_Data Aggregation_: converting a dataset from a list of records to summarised values```


* Anonymisation requires more than just applying the appropriate technique. Good practice includes:
1) Determining the release model (open data, safeguarded data, controlled data)
2) Classifying data attributes as direct identifiers, indirect identifiers, or non-identifiers
3) Removing any attribute that is clearly not required
4) Anonymizing direct and indirect identifiers with appropriate techniques described above
5) Determining actual risk using methods such as k-anonymity
6) Determining if any controls measure required (legal and organizational). Controls can include revocable access, query only, limiting recipients, providing only a subset of the anonymised dataset or measures to notify relevant parties if a data breach occurs or regularly reviewing re-identification risk



## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography
> Credit/urls for any materials that form part of the chapter's text.
