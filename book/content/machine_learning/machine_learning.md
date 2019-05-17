
# Machine Learning

https://hackmd.io/s/r1v4BWnn4

## Prerequisites / recommended skill level
> other chapters that should have been read before or content you should be familiar with before you read this

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| [Reproducible Environments](eproducible_environments/reproducible_environments) | Useful | Any notes |

## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful

This chapter will cover best practises for reproducable machine learning projects. It will include examples of workflows with test data as well as tips and tricks for machine learning pipelines and Python modules to help with reproducibility.

## Chapter content

1. [Introduction to Machine Learning](#intro) 
3. [Retrieving and versioning input data](#data-retrieval)
4. [Tracking input parameters](#input-params)
5. [Pipeline diagnostics, visualisation and outputs](#visualisation)
6. [Deploying a containerised algorithm](#deployment)
2. [Popular Resources](#resources)

<a name="intro"></a>
### Introduction to basic machine learning concepts




#### Supervised learning
Supervised machine learning algorithms use a set of labeled data in order to learn how features can be used to predict class labels. Once the algorithm has been trained and validated, it can be applied to new unlabeled sources in order to classify them.

#### Unsupervised learning
Un-supervised machine learning algorithms have no prior knowledge of class labels. They try to separate the data into classes based on having similar features.

#### Clustering (or data visualisation techniques?)

### Highlighting popular machine learning resources
Here we point out some popular go to places for machine learning algorithms and libraries. We make no attempt to explain how to use them, but simply point towards documentation.

Listed below is a small selection of software libraries that can be used for machine learning. They contain implementations of many useful algorithms, allowing the researcher to leveage powerful tools for data science whilst still focusing on experimentation and building on the existing state of the art.

- [`sklearn`](https://scikit-learn.org/stable/)
- [`TensorFlow`](https://www.tensorflow.org/)
- [`Keras`](https://keras.io/)


### Why is it important to think about reproducibility with machine learning?

As mentioned in [Pete Warden's blog post](https://petewarden.com/2018/03/19/the-machine-learning-reproducibility-crisis/), Machine Learning is going through a _reproducibilty crisis_ at the moment; but why does this matter?

> I’ve had several friends contact me about their struggles reproducing published models as baselines for their own papers. If they can’t get the same accuracy that the original authors did, how can they tell if their new approach is an improvement? 

If one is unable to reproduce the state of the art results, one can not trust that these results are in fact the state of the start. Furthermore, as more and more models are developed in which rely on other models, reproducitbily at all levels is for transparecy. 

At present, it is impractical to _binderise_ or use Jupyter notebooks for complete reproduceability of Machine Learning pipelines, and so researchers need additional workflows specific to the data analysis and machine learning. In the remainder of this chapter these workflows are describes along with best practises for maintaining a reproducible machine learning pipeline.

<a name="data-retrieval"></a>
### Retrieving and versioning input data
This section will cover the problems associated with retrieving data from remote repositories 

Having a reproducable way to gather a data set forms the basis for obtaining a consistent result. In practise the data in a remote repository can change over time. Furthermore, the same data could be available from various locations (some which you may not be aware of), but with subtle differences between them. Therefore, it is very important to document exactly where you get your data, and what those data contain.


In some cases, the data set required to obtain a result can be packaged together with the scipts and models. However, in many machine learning scenarios the data sets are extremely large and cannot be practically packaged or containerised with the scripts. This makes it especially important to document the retrieval of data, and provide a detailed recipe (in script form) to follow to obtain the exact data set that was used to obtain a result.

#### Best practices for retrieving data

<a name="logger"></a>
#### An introduction to the python `logger` module


<a name="input-params"></a>
### Tracking input parameters
Machine learning algorithms require a number of input parameters, [model hyperparameters](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning)), that need to be optimized to solve a particular problem. Those parameters will depend on your specific problem, data set, implementation and objectives, so it is a good idea to work with code flexible enough to work with a range of possible parameters that can be feed to the algorithm without needing to modify the actual code. A particular code will produce different results depending on which parameters are used, which can be provided by an external file, also known as configuration file.

> It is a good practice to separate your stable and immutable code from all those parameters that are susceptible to change.

It is often the case that several iterations are needed to find the optimal set of parameters, so it is important to keep track of which values are used at different stages and which ones were used to produce the current output of a particular execution of the code.

Generally you want your input parameters to be stored in a human-readable file that is also easy to modify and update. There are different types of general-purpose serialization format that can be useful to store parameters.

- JSON. 
- XML
- YAML
- TOML
- Scripting language
- Plain text decoded manually
<!-- Maybe add some description, like this from wikipedia (https://en.wikipedia.org/wiki/Serialization): JSON. Plain-text file commonly used for client-server communication in web applications. Good human readability and easy to decode to be used in your program. 

Also, good discussion about pros/cons here: https://www.lucidchart.com/techblog/2018/07/16/why-json-isnt-a-good-configuration-language/
-->

Some of this formats accept nested structures. Different programming languages will have modules to read and decode configuration files into easy-to-use structures like dictionaries in python.

Example yaml file (config_file.yml):

```
function1:
        parameter1: 10.0
        parameter2: 20.0
        parameter3: 30.0
        useoption: True
function2:
        name1: example
        parameter2: 1.0 
        parameter3: 2.0 
        useoption: False

```

How to read the file in python:
```python
import yaml

with open('./config_file.yml', 'r') as stream:
    try:
        inputs = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
```

That will generate a python dictionary with the same key:value structure of the yaml file. It accepts different variable types like strings, floats, lists, dictionaries, booleans, etc.


sklearn.pipeline etc

#### Best practices for implementing algorithms
(sklearn.pipeline)

<a name="diagnostics"></a>

### Pipeline diagnostics, visualisation and outputs
Running complex, parallel and computationally-intensive pipelines is a necessary part of data science, however these can be slow to run and difficult to debug when they go wrong. Whilst we all strive for good code design, your pipeline will probably involve some level of error handling that may affect the validity of the output. It is therefore good practice to record as much output as possible from the functions that are called in the pipeline. This may include:
- error messages that are explicitly handled by your code
- warnings that are generated by functions within the pipeline.

If your code breaks in the future, having a record of the warnings associated with that attempt could save a lot of time during debugging. An Python approach for recording and writing to file different types of error, warning is described [here](#logger).

> **A note on plotting:** Your pipeline may output diagnostic plots. These are to help you and your close collaborators make operational decisions about your pipeline and are for internal use only. The figures that you will make for your next high impact publication or to show your clients should be generated separately.

([RDM](/rdm/rdm.md#Sharing-Archiving))


output datasets that will be used to generate your final, publication- or customer- ready figures.




<a name="deployment"></a>
### Deploying a containerised algorithm

<a name="resources"></a>
### Popular Resources

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
