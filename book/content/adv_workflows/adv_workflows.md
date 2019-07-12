#  Advanced Reproducible Batch Data Analysis Workflows (Pipelines)

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| ------------ | ---------- | ----- |
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Necessary | |
| [Version control](/version_control/version_control) | Helpful | Experience using git is useful to follow along with examples |
| [YAML](/reproducible_environments/03/yaml.html) | Helpful | Comfort with YAML is useful when writing workflows by hand |
| [Docker](/reproducible_environments/06/containers.html) | Helpful | Using/creating Docker format software containers increases the portability of your workflow |
| [Conda](/reproducible_environments/02/package-management.html) | Helpful | Packaging your own software makes for better software containers |
| [Continuous Integration](continuous_integration/continuous_integration) | Helpful | CI ensures that all the components of your workflow continue to work together |


Recommended skill level: intermediate

## Table of contents

- [Summary](#summary)
- [An Introduction to Workflows/Pipelines](#an-introduction-to-workflows_pipelines)
  - [Why Use Structured Workflows for Reproducible Research?](#why-use-structured-workfowls-for-reproducible-research)
  - [When to switch to a structured workflow from other approaches?](#when-to-switch-to-structured-workflow)
- [Bringing structure to a workflow step](#bringing-structure-to-a-workflow-step)
  - [Finding an Existing Tool Description](#finding-an-existing-tool-description)
  - [Including Your Own Script/Code](#including-your-own-script-or-code)
- [Building workflows](#building-workflows)
  - [Connecting Steps Into a Workflow Using YAML](#connecting-steps-into-a-workflow-using-yaml)
  - [Connecting Steps Into a Workflow Using a GUI](#connecting-steps-into-a-workflow-using-a-gui)
  - [Visualizing Workflows](#visualing-workflows)
  - [Testing Workflows](#testing-workflows)
- [Adding Tool & Workflow description Metadata: authorship, license, and more](#metadata)
- [Giving credit](#credit)
- [A Real Reproducible Paper Using Workflows](#a-real-reproducible-paper-using-workflows)
- [Further Reading](#further-reading)
  - [Manual](#manual)
  - [Discussions](#discussions)
  - [Blogs](#blogs)
  - [Tools](#tools)
- [Glossary](#glossary)


## Summary

In the previous chapter you may have learned that a data science or research
project can be seen as a tree of dependencies: the report depends on the
figures and tables, and these in turn depend on the data and the analysis
scripts used to process this data (illustrated in the figure 
below). If you followed the rest of the previous chapter, you would have
learned about using the tool "Make" to execute that tree of dependencies.

Some projects rise to a level of complexity beyond the scale that the Make tool
excels at. Or perhaps the computational needs to scale beyond a single
computer; for example over an institution's computing cluster or a commercial
"cloud" computing service. Or you may have a desire to have more structure,
documentation, and metadata than is normally possible with Make.

In theses cases you can upgrade your Make workflow to be compabile with
__workflow executors__ or __workflow platforms__ by using the
[CWL](https://en.wikipedia.org/wiki/Common_Workflow_Language) standards. By
upgrading your workflow to a more structured form you can easily run it on a
variety of computing platforms (mentioned above) using one of the
standards-compliant __workflow executors__. Or you can gain additonal benefits
like automated provenance tracking, assistance with data management, web based
graphical dashboards and more by running your reseach data analysis workflow on
one of the many standards-compliant __workflow platforms__.

In this chapter we give an introduction to workflows using the CWL standards
and provide a tutorial on how CWL format workflows can be used for a data 
analysis pipeline.  We also describe a real-world reproducible research 
project that uses CWL to go from the raw input data to the experiments all 
the way to the pdf file of the paper!

![Schematic of a research project](../figures/make/research_dag.png)
<small style="margin: 5pt auto; text-align: center; display: block;">A 
schematic for a research project that uses LaTeX.</small>


## An Introduction to Workflows/Pipelines


### Why Use Structured Workflows for Reproducible Research?

### When to switch to a structured workflow from other approaches?

## Bringing structure to a workflow step

### Finding an Existing Tool Description

### Including Your Own Script/Code

## Building workflows

### Connecting Steps Into a Workflow Using YAML

### Connecting Steps Into a Workflow Using a GUI

### Visualizing Workflows

### Testing Workflows

## Adding Tool & Workflow description Metadata: authorship, license, and more

### Giving credit

## A Real Reproducible Paper Using Workflows

## Further Reading

### Manual

### Discussions

### Tools

## Glossary



