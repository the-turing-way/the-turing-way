(rr-rdm-cleaning)=
# Data Cleaning

Data cleaning is an important part of the RDM process. 
During data cleaning mistakes in the data collection and processing phase can be fixed. 
In projects where data collection is not structured properly, data cleaning can take up a lot of time. 
Sometimes, it may even be quicker to restart data collection in order to avoid a messy dataset. 

(rr-rdm-cleaning-how)=
# How to clean data?
During data cleaning there are several steps to take into account:

## 1. Backup Your Raw Data

Always save an untouched copy of your dataset before you begin! 
If you make mistakes during the data cleaning process you can still go back to the original information. 
All changes to data need to happen in one data file; if you use multiple versions it will be a mess to identify the correct/latest version to work in.  

## 2. Understand/Validate the Data

Data validation is a process used to determine if data are inaccurate, incomplete, or unreasonable (@Chapman2005data).

To validate the data you can check if data are:

**Complete**
* Check for missing/duplicate cases, rows, and columns.

**Accurate**
* Check for invalid, non-unique, or missing study IDs.
* Check for incorrect or inconsistent variables. 
* Check for incorrect inconsistent formatting.
* Check missing values.

**Reasonable**
* Check if values are out of range or unexpected.

Creating tables, plots, or calculating summaries and statistics are a helpful way to search for errors.

## 3. Remove unnecessary data, duplicates and consider outliers

Each unnecessary entry can complicate your analyses distort your findings. 
Delete draft or test entries and duplicates, after carefully reviewing if they are indeed test entries or duplicates. 
Consider unexpected data, such as unusually high or low values. 
These could be data entry errors, but they may also be the most interesting findings! 
Sum-to-total, range and validity checks can help you to find errors. 

## 4. Standardize entries

Align all variables, by for example writing all dates out in a similar manner, and keeping capitalisation consistent. 
For example, "Yes,” “yes,” and “Y” are treated by computers as separate responses. 
Ensure that all variables are labeled and used in a consistent manner across different data formats. 
Use clear [naming conventions](#rr-rdm-storage-conventions] for your files and folders.

## 5. One variable is one data entry

Each variable should only collect one piece of information (@Wickham2014tidydata) (see [Data Organisation in Spreadsheets for more tips](#rr-rdm-spreadsheets-format).
Consider how to split variables into multiple variables if more than one thing is measured. 

## 6. Handle Missing Data Thoughtfully

Decide how to manage missing values. 
Missing data can mean a variety of things: perhaps a participant did not know the answer, or they refused to answer, the question was accidentally skipped, the handwriting was illegible, or there was an error made in data entry, or the value should be blank on purpose. 
Should missing data be removed, imputed, or marked as “Unknown” or "Not Applicable"? 
Make sure that this decision is transparently documented somewhere.
Deleting missing data entirely may not always make sense as missing data can provide insights on the data collection process.

## 7. Document Cleaning Steps

If your data is under [version control](#vcs), changes to the data will be automatically tracked. 
You can also keep a text file with the changes, such as a "Data Cleaning Log.” 
Record what you changed, when, and most importantly: why. 
This documentation increases transparency and by adding clear and detailed notes you will allow others to replicate your data cleaning process. 
Versioning files and updating documentation takes time and consideration - and is worthwhile in the long run to save future you and others time trying to retrace your steps.

## 8. Update the data collection process to prevent future mistakes

It is easier to not have to clean data - you can prevent data errors during data collection. 
Define range limits on your data where possible (for example, the score must be a value between 0 and 10 for household members; a birthday must be between certain dates). 
Prevent blank values by requiring data entry, or ensure that where blank values should be present they are intentional. 

(rr-rdm-cleaning-old)=
# Cleaning up old data

Sometimes it is needed to make data cleaning decisions after the data is already processed an organized. 
Data takes up space - which data should be kept for the long term and what can be removed? 

(rr-rdm-cleaning-lab)=
# Data cleaning with a Team/Lab

Often data cleaning is done by one person, but it can be helpful to do data cleaning as a team. 
This may save time and will guarantee that at least one other person is able to retrace the data cleaning steps. 
Consider setting up a [data cleaning day at the lab](https://www.dataorchard.org.uk/news/introducing-the-data-cleaning-day) to hold each other accountable, and make sure that lab/data cleaning activities are equitably distributed. 
You can also outline data cleaning activities in the [Team/Lab manual](#cl-team-manual).

## Resources

* [Data Cleaning](https://datamgmtinedresearch.com/clean), chapter in Data Management in Large-Scale Education Research
* [The Quartz guide to bad data](https://github.com/Quartz/bad-data-guide/tree/master)
