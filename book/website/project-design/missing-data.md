(pd-missing-data)=
# Missing Data Handling


(pd-missing-data-prerequisites)=
## Prerequisites

<!--

>**Itemise other chapters in _The Turing Way_ or topics that readers should be familiar with to understand your chapter better.**
> Ensure that you link to those chapters using the [Style Guide's](https://the-turing-way.netlify.app/community-handbook/style/style-crossref.html) cross referencing recommendations.
> If the topics are only available on the web, appropriately link to them too.
> Importance should either be `Helpful` or `Necessary`

> For each prerequisite, you should also provide an indication of the skill level readers should have to understand your chapter better
> Skill level can either be _beginner_, _intermediate_, or _advanced_.
>

 None. 

| Prerequisite | Skill Level | Notes |
| -------------|------|----|
| None. | Beginner | Any useful notes the reader should know | -->

| Prerequisite | Importance | Skill Level | Notes |
| -------------|----------|------|----|
| {ref}`Research Data Management <rr-rdm>` | Helpful | Beginner |  |



(pd-missing-data-summary)=
## Summary

This chapter aims to introduce missing data handling. Although we live in the age of "big data", "big data" can often be fragmented, incomplete, and erroneous. The methods we develop and any analysis we conduct can only be as good as the data we provide. So, is there anything we can do about a dataset riddled with missing data?


```{figure} ../figures/missing-data-handling.*
---
height: 500px
name: first-pull-request
alt: Cartoon-like sketch with four people assembling puzzle pieces. There are four different buckets with puzzle pieces with blue dots in them. One bucket is labelled "RANDOM" and another "NOT RANDOM". Two of the people are holding a dotted puzzle piece. Another person is looking up at a hanging puzzle. Some pieces of the puzzle are dotted, others are filled with solid orange. The last person standing to the left of the hanging puzzle is painting an empty puzzle piece tile using paint from a bucket labelled "DATA HANDLING". This paint has the same dotted pattern found on the puzzle pieces in the buckets. 
---
Missing Data Handling.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```
<!---
TODO: change the doi above to the right one
-->

To answer this question, we will start by defining different types of {ref}`pd-missing-data-structures` and see how we can visualise these {ref}`pd-missing-data-visualising-missingness`. This will help us develop a strategy on choosing the appropriate missing data handling method, of which we outline a few in {ref}`pd-missing-data-methods`. Lastly, we introduce the relatively new field of {ref}`pd-missing-data-structured-missingness`, pioneered by researchers in the Turing-Roche partnership. This is a big area of research and this chapter is only a simple introduction to it. Therefore, if you are interested in learning more we encourage you to read on further by having a look at the {ref}`pd-missing-data-checklist-resources` page. 


(pd-missing-data-motivation)=
## Motivation and Background

Missing data can disrupt research and create challenges in results interpretation and in the validity of any conclusions {cite:ps}`Pederson2017missingdata`. Understanding missing data structures and handling missing data appropriately is important to prevent creating or worsening pre-existing biases of the dataset and to ensure fair, generalizable models {cite:ps}`Buuren2018imputation`. Both missing data itself, or how it is handled, can have a large impact on subsequent analyses. Missing data handling is one step in the process to figuring out the best use of your data, in the most efficient way possible. 



