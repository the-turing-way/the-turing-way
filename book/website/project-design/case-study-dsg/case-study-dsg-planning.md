# Planning - Data Preparation 

Considerations of the data suitability, readiness and collection should begin at the time of project proposal development. 
If the data is unsuitable, incomplete or won't be ready in time then the whole project could be compromised. Data preparation should begin as soon as the project question is finalised. 

Initial data readiness will be different for every project. 
In case the data may not exist and a method of collection will be the first action. 
In other cases, pre-curated data sets may be used with the key action being obtaining use rights. 

Data is research ready when it has been collected, constructed, cleaned, checked for gaps when potential sensitivities have been considered (and mitigated against) and you have the right to use and work on the datasets. 

## Key Considerations 

* **Data Readiness**: If the data doesn't yet exist, a method of data collection must be devised. 
If the raw data exists but it has yet to be curated for purpose, methodology for this must be established. 
If the data is nearly ready, then it must be checked for gaps and cleanliness. 
* **Data Appropriateness**: Data should be highly relevant to the research question. 
Even if data looks to be suitable, there may be additional sets of resources that already exist that can enrich and improve the scope of research. 
* **Data Quantity**: Data must be large enough to effectively run analysis and experimentation, if not enough data point exists, a method of generating more should be pursued. 
This could be by obtaining complementary data sets or generating synthetic or collecting new data. 
Equally, researchers may be faced with an abundance of data, so much that meaningful analysis becomes hard. 
In such cases, researchers may need to edit and refine what data will be used. 
* **Data Sensitivity**: How sensitive is the data that will be used? 
The more sensitive the data set is, the more restrictions will be needed to protect it during the research phase which inhibits researchers ease of access and experiment. 
If the data contains personal information or sensitive commercial information then it is likely to be highly sensitive. 
In such cases, it may be possible to reduce the sensitivity of the data by either removing or anonymising areas of interest. 
Even if the data is not especially sensitive, the project as a whole may produce sensitive results, so it may be worth taking the same measures to reduce sensitivity as much as possible, reducing the security measures that will be necessary and minimising negative implications of a data breach. 
* **Data Completeness/Reliability**: The data should be checked for missing observations and unreliable data points. Any incompleteness or unreliability must be assessed as to its impact on the project and what can be done to minimise missing values and maximise overall reliability. 
* **Data Permission/Legal Considerations**: It is essential that you have the right to use the data. If data has been generated in house and involves no human data, then this may not be necessary. 
However, in many cases, the data will come from a collaborator or from a third-party data provider. 
In these cases, at minimum, a data-sharing agreement should be enacted so that both parties are protected. 
Depending on organisations, this may be a straightforward process or may take many iterations and discussions with legal teams. 
Data sharing agreements should therefore be discussed from the get-go and be one of the first actions when considering data preparation. 
If the data contains personal information, such as patient data, then you must be able to prove that the subjects have consented for their data to be collected and used. 

## Data Transfer 

If a project is considered sensitive, security measures will be required when the data is transferred from a third party to the research manager.
Methods such as Azure storage explorer could be used, in which a secure one-way upload link is sent to the device uploading the data. 
This link is only usable by that devices specific public-facing IP address.

It is likely each institution will have its preferred method of transferring specific kinds of data through personal channels and so a discussion may be required to meet the system and security needs of each party. 

## Data Storage and Access 

When deciding how to store the data, managers should consider who will need access and what they will need to do with the data in terms of research. This may impact the storage method used. 

Non-sensitive data may not require exhaustive security measures like they are needed for sensitive data. 
However, it should still be stored securely, so that only those who need access have it. 
This is good practice for handling data. 

Sensitive data once transferred should be placed in some kind of secure location including security measures. 
This could be a research environment, such as a 'Safe Haven ‘or equivalent trusted secure platform. 
Depending on the storage method, this may need to be deployed/ set up beforehand so be sure to establish a need for this (or not) early on. 

Following Turing’s 'Safe Haven' Model of secure research environments, there are various security measures that can be implemented depending on the sensitivity of the contents. 
These can include restrictions on internet access, packages, and copy and paste functions from within the environment. 
The more restrictions in place from within the environment, the slower it will be for researchers to work on the project. 
It is therefore essential that only necessary measures are in place. 
Researchers and the data provider should agree beforehand on how sensitive the project is, as well as what security measures should be present. 
