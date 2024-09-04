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
| {ref}`Research Data Management <rdm>` | Helpful | Beginner |  |



(pd-missing-data-summary)=
## Summary

This chapter aims to introduce missing data handling. Although we live in the age of "big data", "big data" can often be fragmented, incomplete, and erroneous. The methods we develop and any analysis we conduct can only be as good as the data we provide. So, is there anything we can do about a dataset riddled with missing data?


```{figure} ../figures/missing-data-handling.*
---
height: 400px
name: first-pull-request
alt: Cartoon-like sketch with four people assembling puzzle pieces. There are four different buckets with puzzle pieces with blue dots in them. One bucket is labelled "RANDOM" and another "NOT RANDOM". Two of the people are holding a dotted puzzle piece. Another person is looking up at a hanging puzzle. Some pieces of the puzzle are dotted, others are filled with solid orange. The last person standing to the left of the hanging puzzle is painting an empty puzzle piece tile using paint from a bucket labelled "DATA HANDLING". This paint has the same dotted pattern found on the puzzle pieces in the buckets. 
---
Missing Data Handling.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```
<!---
TODO: change the doi above to the right one
-->

To answer this question, we will start by defining different types of {ref}`pd-missing-data-structures` and see how we can visualise these {ref}`pd-missing-data-visualising-missingness`. This will help us develop a strategy on choosing the appropriate missing data handling method, of which we outline a few in {ref}`pd-missing-data-methods`. Lastly, we introduce the relatively new field of {ref}`pd-missing-data-structured-missingness`, pioneered by researchers in the Turing-Roche partnership. 



> **Write a brief overview of the content of your chapter.**
> Summaries should be concise, but also introduce all the sub-topics that your chapter will talk about.
> When you mention a sub-topic, link to the subchapter where you expand on the topic.
> See the Summary in the Open Research [chapter](https://the-turing-way.netlify.app/reproducible-research/open.html) for inspiration.

> Optionally, you can add an image that captures the gist of your chapter.
> For reference, you may reuse our images hosted on Zenodo [here](https://zenodo.org/record/3332808) and [here](https://zenodo.org/record/3695300).
> You may also use this collection of [royalty free images](https://www.manypixels.co/gallery/) hosted on ManyPixels.
> Recommendations for using figures in _The Turing Way_ can be found in the [Style Guide](https://the-turing-way.netlify.app/community-handbook/style/style-figures.html).

(pd-missing-data-motivation)=
## Motivation and Background

> **Explain why readers should pay attention to this chapter.**
> For example, how can your chapter's content have a positive impact on your reader's data science project?
> Think about the reader demographic that would be interested in your chapter and tailor this section appropriately.
> Remember to cross-reference relevant subchapters using this directive: `{ref}Subchapter<sectioninitials-filename-subchaptername>`.

<!-- IMPORTANT!

- Use this template to create the landing page for your chapter

BEFORE YOU GO

- Have a look at the Style Guide and the Maintaining Consistency chapters to ensure that you have followed the relevant recommendations on
  - Labels and cross referencing
  - Using images
  - Latin abbreviations
  - References and citations

-->

