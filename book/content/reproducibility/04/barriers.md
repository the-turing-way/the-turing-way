# Barriers to reproducibility

So far we have described the [importance](../01/importantforscience) of reproducible research and motivated why we think [you should care](../02/whycare).

But there are many barriers to reproducible research.
You can watch Kirstie Whitaker describe some of them in [her talk about The Turing Way](https://youtu.be/wZeoZaIV0VE?t=312) at [csv,conf,v4](https://csvconf.com/2019) in May 2019.
The section describing the slide below starts around 5 minutes into the video.

| ![Barriers to reproducible research](../../figures/reproducibility/barriers.png) |
| -------------------------------------------------------------------------------------------------------- |
|  Some of the barriers to reproducible research. |

This chapter outlines some of those barriers, and a couple of suggestions to get around them.

## Barrier 1

*replace this text with the content of barrier 1*

## Barrier 2

*replace this text with the content of barrier 2*

## Barrier 3

*replace this text with the content of barrier 3*

## Barrier 4

*replace this text with the content of barrier 4*

## Barrier 5

*replace this text with the content of barrier 5*

## Barrier 6

*replace this text with the content of barrier 6*

## Barrier 7

*replace this text with the content of barrier 7*

## Big data and complex computational infrastructure

Big data is conceptualised in different ways by different researchers. 
"Big" data may be complex, come from a variety of data sources, is large in storage volume and/or be streamed at very high temporal resolution. 
Although there are ways to set random seeds and take snapshots of a dataset at a particular moment in time, it can be difficult to have identical data across different runs of an analysis pipeline.
This is particularly relevant in the context of tools for parallel computing.
In some cases, when data is sampled from a larger collection of data consistency cannot be guaranteed.

A large variety of tools and products with a constantly changing ecosystem of supported technologies is available, meaning reproducing results in the future is highly dependent on the available technology at the time. 
Some tools require in depth technical skills which are not widely available to data scientists. 
The Hadoop framework, for instance, is extremely complex to deploy data science experiments without strong software and hardware engineering knowledge. 
Combined with the need for high performance computing, the barrier to access big data processing is even greater. 
Very often the results of statistical tests will vary depending on the configuration of the infrastructure that was used in each of the experiments, therefore reproducibility is difficult to achieve (experiments are often dependent on random initialisation for iterative algorithms, fixing a pseudorandom number will result in limiting parallelisation capabilities, e.g. in Tensorflow).

## Barrier 9

*replace this text with the content of barrier 9*
