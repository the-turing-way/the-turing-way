(rr-ci-ghactions)=
# Continuous Integration with GitHub Actions

In this section, we walk you through the basic setup of continuous integration (CI) using GitHub Actions. **GitHub Actions** is a task automation system fully integrated with GitHub. In other words, it is an API that orchestrates any workflow based on any event. Therefore, it makes it easier than ever to incorporate CI into your repositories. It is a flexible way to automate nearly every aspect of your project workflow. Here are just a few examples of use cases of GitHub Actions:

- Automated testing of the software
- Generate reports of the status of any changes in the repository
- Responding to workflow triggers using labels, issues, `@` mentions, and more
- Triggering code reviews and pull requests
- Managing branches

GitHub Actions are event-driven which means it responds to any event (`PR` created, issue created, ...) and triggers an action (label, test, sort, ...). A collection of actions is called a workflow.

```{figure} ../../figures/gih_action_diagrame.png
---
width: 400px
align: center
name: Github actions
alt: a diagrame showing how events can trigger a job, and a collection of jobs called a workflow.
---
```


### GitHub-related Vocabulary

**1. WorkFlow**

The workflow is is a unit of automation from start to finish. It consists of all the aspects which should be taken into account during the automation including what event can be trigger the automation. The workflow can be used to build, test, package, release, or deploy a project on GitHub. It is made of multiple jobs which is formed from steps as shown in the image below.

```{figure} ../../figures/gh_actions_structure.png
---
width: 600px
align: center
name: GitHub action Structure
alt: a diagrame showing how the workflow is divided into jobs and steps.
---
```

**2. Job**

A job is a section of the workflow, and is made up of one or more steps. In this section of our workflow, the template defines the steps that make up the build job.

**3. Step**

Step: A step represents one effect of the automation. A step could be defined as a GitHub Action, or another unit, like printing something to the console.

**4. Actions**

A GitHub Action is a piece of automation written in a way that is compatible with workflows. Actions can be written by [GitHub](https://github.com/actions), by the open source [community](https://github.com/sdras/awesome-actions), or you can write them yourself!

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


In the next section, we will explain building blocks for the workflow.



<!-- (I'll explain each vocab separately using diagrams made with adobe illustrator) -->
