(pd-missing-data-structures)=
# Missing Data Structures

This subchapter introduces the main missing data structures. In order to decide on how to best handle any missing data, understanding our data and any context in how the data was acquired is important. To that end, data can be usually classified into three main types based on why the data may be missing: 
1. [Missing Completely at Random (MCAR)](pd-missing-data-structures-mcar)
2. [Missing at Random (MAR)](pd-missing-data-structures-mar)
3. [Missing not at Random (MNAR)](pd-missing-data-structures-mnar)

These were originally proposed by Rubin {cite:ps}`Rubin1976missingdata` and are explained in more detail below. As this chapter has been created as part of the Turing-Roche Community Scholar scheme, the examples provided will be based in healthcare. 

> **Example Dataset**: We will be using a fictional study of health outcomes to explain the different mechanisms of missing data. For demonstration purposes, the dataset is first shown (below) as being fully complete and only has 8 participants. 
>  
> | Participant Number | Age | Diastolic Blood Pressure | Systolic Blood Pressure | Blood Test Result | Motor Score | Cognitive Score |
> |--------------------|-----|--------------------------|-------------------------|-------------------|-------------|-----------------|
> | 1                  | 56  | 82                       | 118                     | Positive          | 10          | 35              |
> | 2                  | 78  | 87                       | 134                     | Negative          | 32          | 29              |
> | 3                  | 85  | 90                       | 130                     | Negative          | 27          | 14              |
> | 4                  | 43  | 83                       | 121                     | Negative          | 15          | 36              |
> | 5                  | 67  | 86                       | 131                     | Positive          | 20          | 25              |
> | 6                  | 82  | 92                       | 133                     | Negative          | 26          | 12              |
> | 7                  | 88  | 95                       | 140                     | Positive          | 34          | 10              |
> | 8                  | 71  | 87                       | 126                     | Negative          | 33          | 22              |
>
>
> Where generally worse health outcomes are associated with: 
> - a higher blood pressure measurement
> - a positive blood test result
> - a high motor score
> - a low cognitive score 
>
> In the examples below, any missing values will be indicated by "N/A" (Not Available) in red bold font. 


(pd-missing-data-structures-mcar)=
## Missing Completely at Random (MCAR) 

Just as the name may suggest, missing data can be characterized as MCAR when it occurs completely randomly and is not due to an event caused by any variables of interest (whether observed or unobserved). Thus, there are no systemic differences between data entries with or without missing values, and no bias is introduced because of the missing data. 

In reality, this is quite a strict classification and rarely occurs. Essentially any variable that affects the reason for why the data is missing in the first place has no affect on any of the variables in the study. Therefore, this means that the probability of a data entry being missing is the same for any given data point. 

> **Example**: A specific batch of blood samples were incorrectly processed, so the results were discarded. The missing data in the variable of interest (blood test result), is not explained by any observed or unobserved variables. 
>
> | Participant Number | Age | Diastolic Blood Pressure | Systolic Blood Pressure | Blood Test Result                                  | Motor Score | Cognitive Score |
> |--------------------|-----|--------------------------|-------------------------|---------------------------------------------------|-------------|-----------------|
> | 1                  | 56  | 82                       | 118                     | <span style="color:red;"><strong>N/A</strong></span> | 10          | 35              |
> | 2                  | 78  | 87                       | 134                     | <span style="color:red;"><strong>N/A</strong></span> | 32          | 29              |
> | 3                  | 85  | 90                       | 130                     | <span style="color:red;"><strong>N/A</strong></span> | 27          | 14              |
> | 4                  | 43  | 83                       | 121                     | Negative                                           | 15          | 36              |
> | 5                  | 67  | 86                       | 131                     | Positive                                           | 20          | 25              |
> | 6                  | 82  | 92                       | 133                     | Negative                                           | 26          | 12              |
> | 7                  | 88  | 95                       | 140                     | Positive                                           | 34          | 10              |
> | 8                  | 71  | 87                       | 126                     | Negative                                           | 33          | 22              |
> 
> Here, the first batch of blood samples had to be discarded. 

(pd-missing-data-structures-mar)=
## Missing at Random (MAR) 

In contrast, when missingness can be explained by variables with complete data, and is not random, this is known as MAR. Therefore, for a given group defined by and observed variable, the probability of being missing is the same for all individuals of that group. Such missingness may or may not result in bias; if there is bias this can be handled by accounting for the known variable correlated with the reason for missingness. 

> **Example**: Blood pressure readings may be missing from individuals who are older, frailer, and have less mobility, and therefore, are more likely to not attend the clinic. In this instance, the reason data is missing in the variable of interest (blood pressure), is related to other observed variables (age and mobility). 
>
> | Participant Number | Age | Diastolic Blood Pressure | Systolic Blood Pressure | Blood Test Result                                  | Motor Score | Cognitive Score |
> |--------------------|-----|--------------------------|-------------------------|---------------------------------------------------|-------------|-----------------|
> | 1                  | 56  | 82                       | 118                     | <span style="color:red;"><strong>N/A</strong></span> | 10          | 35              |
> | 2                  | 78  | 87                       | 134                     | <span style="color:red;"><strong>N/A</strong></span> | 32          | 29              |
> | 3                  | 85  | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | 27          | 14              |
> | 4                  | 43  | 83                       | 121                     | Negative                                           | 15          | 36              |
> | 5                  | 67  | 86                       | 131                     | Positive                                           | 20          | 25              |
> | 6                  | 82  | 92                       | 133                     | Negative                                           | 26          | 12              |
> | 7                  | 88  | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | Positive                                           | 34          | 10              |
> | 8                  | 71  | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | Negative                                           | 33          | 22              |
>
> Individuals with a high motor score (>26) and who were older (>70) were unable to attend the blood pressure clinic. 



(pd-missing-data-structures-mnar)=
## Missing not at Random (MNAR)

Data that are MNAR is missing due to reasons that we do not know. In other words, the reason for the missingness is related to the value of the variable that is missing. This is the most complex case of data missingness to handle, as bias may occur but cannot be adjusted for as the source of the missingness is unmeasured. 

> **Example**: Follow-up cognitive testing may be missing for individuals who have had significant cognitive decline, as they are more likely to withdraw early from the study. Here, the reason for the missing data in the variable of interest (Cognitive Score) is correlated to unobserved data (the value of the observation itself). 
>
> | Participant Number | Age | Diastolic Blood Pressure | Systolic Blood Pressure | Blood Test Result                                  | Motor Score | Cognitive Score                                  |
> |--------------------|-----|--------------------------|-------------------------|---------------------------------------------------|-------------|-------------------------------------------------|
> | 1                  | 56  | 82                       | 118                     | <span style="color:red;"><strong>N/A</strong></span> | 10          | 35                                              |
> | 2                  | 78  | 87                       | 134                     | <span style="color:red;"><strong>N/A</strong></span> | 32          | 29                                              |
> | 3                  | 85  | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | 27          | <span style="color:red;"><strong>N/A</strong></span> |
> | 4                  | 43  | 83                       | 121                     | Negative                                           | 15          | 36                                              |
> | 5                  | 67  | 86                       | 131                     | Positive                                           | 20          | 25                                              |
> | 6                  | 82  | 92                       | 133                     | Negative                                           | 26          | <span style="color:red;"><strong>N/A</strong></span> |
> | 7                  | 88  | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | Positive                                           | 34          | <span style="color:red;"><strong>N/A</strong></span> |
> | 8                  | 71  | <span style="color:red;"><strong>N/A</strong></span> | <span style="color:red;"><strong>N/A</strong></span> | Negative                                           | 33          | 22                                              |
>
> Participants with a cognitive score less than 15, withdrew early from the study due to worsening outcomes. 

(sectioninitials-filename-summary)=
## Summary

We have defined three types of missingness: MCAR, MAR, and MNAR. These definitions are particularly helpful in determining which data handling method to use. Simple implementations were used to demonstrate the types of missingness a small dataset of health outcomes. 

However, these are quite oversimplified and real-world datasets can be a lot more complex. For instance, whether a given participants may be unable to come into clinic or willing to continue participating in a study at a younger age/ lower motor score/ higher cognitive score than average. Alternatively, they may have missing data in a variable that helps explain the reason or mechanism of missingness. 

Several types of missingness may also be present in a given dataset, and sometimes multiple types may occur in one variable of interest. Therefore, handling missing data can be quite tricky. Here we directly observed the missing values by looking at the data, however this is a cumbersome and unrealistic task in many real datasets, which maybe have thousands of participants, and hundreds of variables (or more). Thus, visualisation methods that simplify determining any patterns of missingness are incredibly useful. These are explored in the next subchapter ({ref}`pd-missing-data-visualising-missingness`). 




<!-- IMPORTANT!

- Use this template to create your chapter's subchapters.
- Refrain from writing very long subchapters as readers may be unwilling to read them. Rather, you should split long subchapters into smaller subchapters if necessary.



BEFORE YOU GO

- Have a look at the Style Guide and the Maintaining Consistency chapters to ensure that you have followed the relevant recommendations on
  - Avoiding HTML
  - Consecutive headers
  - Labels and cross referencing
  - Using images
  - Latin abbreviations
  - References and citations
  - Title casing
  - Matching headers with reference in table of content

-->
