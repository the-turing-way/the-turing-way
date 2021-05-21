(rr-ci-ghactions)=
# Continuous Integration with GitHub Actions

This section will walk you through the basic setup of continuous integration (CI) using **GitHub Actions (GHA)**. GHA is a task automation system fully integrated with GitHub. In other words, it is an API that orchestrates any workflow based on any event. Although there are many CI service providers, GHA makes it easier than ever to incorporate CI into your repositories. It provides a flexible way to automate nearly every aspect of your project workflow. Here are just a few examples of use cases of GitHub Actions:

- Automated testing of the software
- Generate reports of the status of any changes in the repository
- Responding to workflow triggers using labels, issues, special mentions, and more
- Triggering code reviews and pull requests
- Managing branches

GitHub Actions are event-driven, which means it responds to any event (for example: pull request (PR) created, issue created) and triggers an action (for example adds a label, runs tests, sort). Any collection of these actions is called a workflow. A more detailed description of this GitHub-related Vocabulary is described in the next section.

```{figure} ../../figures/gih_action_diagrame.png
---
width: 400px
align: center
name: Github actions
alt: a diagram describes GitHub action listen to an event (for example, `PR` created, issue created) and then trigger a job, which can be testing, labelling, sorting or other tasks .
---
A diagram describing GitHub action listen to an event (for example, `PR` created, issue created) and then trigger a job. It will be replaced with a new _The Turing Way_ project illustration by Scriberia.
```
### GitHub-related Vocabulary
#### 1. WorkFlow

**The workflow** is a unit of automation from start to finish. It consists of all the aspects which should be taken into account during the automation including what event can trigger the automation. The workflow can be used to build, test, package, release, or deploy a project on GitHub. It is made of multiple jobs which is formed from steps as shown in the overview diagram below.

```{figure} ../../figures/ci-01.png
---
name: ContinuousIntegration-Nov20
alt: An illustration of how continuous integration works with multiple jobs and actions working alongside each other to feed into an illustration of steps to show merging into the main version.
---
On the left: _The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300. On the right: Overview of the most important concepts of GitHub Actions, adapated from [morioh.com](https://morioh.com/p/aadcfe6cac57).
```

#### 2. Job

A  *job* is defined as a set of sequential steps run on the same runner. A workflow can build up of one or several jobs, and can be run either parallel (default) or sequentially.


#### 3. Step

A **step** represents one effect of the automation. A step could be defined as a GitHub Action, or another unit, like printing something to the console.

#### 4. Actions

A GitHub **Action** is a piece of automation written in a way that is compatible with workflows. Actions can be written by [GitHub](https://github.com/actions), by the open source [community](https://github.com/sdras/awesome-actions), or you can write them yourself!

## Getting started with GitHub Action

GitHub Actions uses YAML syntax and stored in a directory called `.github/workflows` in the repository. You can either use a templated workflow or create your own.


#### 1- Using GitHub Actions template

If you want to get started with GitHub Actions, you can start by clicking the "Actions" tab in the repository where you want to create a workflow, as shown below. Under the "Actions" tab, you will find popular CI workflows, which can help deploy or automate some tasks in the repository.

```{figure} ../../figures/gifs/start_ghactions.gif
---
width: 600px
align: center
name: GitHub action template
alt: A gif showing where you can find GitHub Actions template in your Github repo.
---
```
You can choose any of these starter workflows and customise them further.  An explanation for building blocks within the workflow is described in a later section.


#### 2- Using libraries-specific templates.


Github Action template is not the only starter kit available; there are libraries-specific templates for the language of interest. For example, you can  use  {usethis} package in R to create a template for R packages by running `usethis::use_github_action_check_standard()`. This will generate GitHub Actions to run CRAN checks after every commit or pull request. That’s all you have to do!


#### 3- Using the configuration of other projects as inspriration

Many well maintained open source libraries and estableshed projects use GitHub Actions for their CI.
Have a look at the checks lists on pull requests of these projects for inspiration and ideas;
following by checking out their CI configuration files.
In most cases their licence will allow to copy the bits that would work for your case.
The advantage of this approach is to use some approaches that are already working.

For example:

- the Turing Way workflow to [build the Turing Way book and to provide a preview for the pull requests](https://github.com/alan-turing-institute/the-turing-way/blob/master/.github/workflows/ci.yml)
- a matrix of tests on [3 operating systems and multiple Python versions for the Python package NetworkX](https://github.com/networkx/networkx/blob/main/.github/workflows/test.yml)
- a more complex setup of testing the [build in multiple circumstances for the Python package Numpy](https://github.com/numpy/numpy/blob/main/.github/workflows/build_test.yml)


In the next section, we will explain building blocks for the workflow.



<!-- (I'll explain each vocab separately using diagrams made with adobe illustrator) -->
