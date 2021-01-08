(rr-ci-ghactions)=
# Continuous Integration with GitHub Actions

In this section, we walk you through a basic setup of continuous integration using GitHub Actions. **GitHub Actions** is a task automation system fully integrated with GitHub. In other words, it is an API that orchestrates any workflow based on any event. It can make makes it easier than ever to incorporate CI into the repositories. It is a flexible way to automate nearly every aspect of your software workflow. Here are just a few examples of use cases of GitHub Actions:

- Automated testing of the software
- Generate reports of the status of any changes in the repository
- Responding to workflow triggers using labels, issues, `@` mentions, and more
- Triggering code reviews and pull requests
- Managing branches

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
GitHub Actions are event-driven, meaning it responds to an event (e.g., PR created, issue created, etc.) and triggers an action (e.g., label, test, sort, ..).
=======
GitHub Actions are event-driven, meaning it responds ti an event (PR created, issue created, ...) and trigger an action (label, test, sort, ...). A collection of jobs are called a workflow.

>>>>>>> divide to sub-chapters
=======
GitHub Actions are event-driven, meaning it responds to an event (e.g., PR created, issue created, etc.) and triggers an action (e.g., label, test, sort, ..).
>>>>>>> add more describtion to the vocab sec
=======
GitHub Actions are event-driven, meaning it responds to an event (`PR` created, issue created, etc.) and triggers an action (label, test, sort, ..). A collection of actions is called a workflow.
>>>>>>> minor changes
=======
GitHub Actions are event-driven, meaning it responds to an event (`PR` created, issue created, ...) and triggers an action (label, test, sort, ...). A collection of actions is called a workflow.
>>>>>>> remove eg/etc

```{figure} ../../figures/gih_action_diagrame.png
---
width: 400px
align: center
name: Github actions
alt: a diagrame showing how events can trigger a job, and a collection of jobs called a workflow.
---
```

## Getting started with GitHub Action

GitHub Actions uses YAML syntax and stored in a directory called `.github/workflows` in the repository. You can either use a templated workflow or create your own.

#### 1- Using GitHub Actions template

If you want to get started with GitHub Actions, you can start by clicking the "Actions" tab in the repository where you want to create a workflow, as shown below.

```{figure} ../../figures/gifs/start_ghactions.gif
---
width: 600px
align: center
name: GitHub action template
alt: A gif showing where you can find GitHub Actions template in your Github repo.
---
```

#### 2- Using libraries-specific templates.

<<<<<<< HEAD
<<<<<<< HEAD
## GitHub-related Vocabulary
=======


# GitHub-related Vocabulary
>>>>>>> divide to sub-chapters
<!-- (I'll explain each vocab separately using diagrams made with adobe illustrator) -->
=======
## GitHub-related Vocabulary


```{figure} ../../figures/gh_actions_structure.png
---
width: 600px
align: center
name: GitHub action Structure
alt: a diagrame showing how the workflow is divided into jobs and steps.
---
```
>>>>>>> add more describtion to the vocab sec

**1. WorkFlow**

The workflow is is a unit of automation from start to finish. It consisits of all the aspects which should be taken into account during the atomation including what event can be trigger the automation. The workflow can be used to build, test, package, release, or deploy a project on GitHub.

**2. Job**

A job is a section of the workflow, and is made up of one or more steps. In this section of our workflow, the template defines the steps that make up the build job.

**3. Step**

Step: A step represents one effect of the automation. A step could be defined as a GitHub Action, or another unit, like printing something to the console.

**4. Actions**

A GitHub Action is a piece of automation written in a way that is compatible with workflows. Actions can be written by GitHub, by the open source community, or you can write them yourself!
