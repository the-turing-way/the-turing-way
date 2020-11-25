(rr-ci-github-actions)=
# Continuous Integration with GitHub Actions
GitHub Actions is a task automation system fully integrated with GitHub. In other words, it is an API that orchestrates any workflow, based on any event and it is not explicitly used for continuous integration (CI). However, it can make makes it easier than ever to incorporate CI into the repositories. 

## Getting started with GitHub Action
If you want to get started with GitHub Actions, you can start by clicking the "Actions" tab in the repository where you want to create a workflow as shown in Fig 1.

You can either use a templated workflow or create your own. 
<!--needs to create gifs-->

## GitHub-related Vocabulary
<!-- (I'll explain each vocab separately using diagrams made with adobe illustrator) -->

**1. WorkFlow**
<!-- needs paraphrasing -->
The workflow is an automated procedure that you add to your repository. 
Workflows are made up of one or more jobs and can be scheduled or triggered by an event. 
The workflow can be used to build, test, package, release, or deploy a project on GitHub.


**2. Action**
<!-- needs paraphrasing -->
<!--An action is a specific activity that triggers a workflow. For example, the activity can originate from GitHub when someone pushes a commit to a repository or when an issue or pull request is created. You can also use the repository dispatch webhook to trigger a workflow when an external event occurs. For a complete list of events that can be used to trigger workflows, see Events that trigger workflows -->.


**3. Steps** 
<!-- needs paraphrasing -->
A step is an individual task that can run commands in a job. A step can be either an action or a shell command. Each step in a job executes on the same runner, allowing the actions in that job to share data.


## Building a block of a WorkFlow
**1. name**
This is the name of the workflow. GitHub will use this name to be displayed on the repository's actions page.
```
name:
    CI Jupyter book
```
**3. on**
The `on` field tells GitHub Actions when to run. For example, we can run the workflow anytime there's a `push` or a `pull`. 
```
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master 
```
Many events can be used to trigger a workflow. You can explore them [here](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions).

**4. env**
**5. jobs**

Any workflow consists of one or more jobs. Every job also runs in an environment specified by`runs-on`. These Jobs run in parallel by default but can also be defined to run sequentially.
```
Jobs:
    runs-on: ubuntu-latest
``` 
**7. steps**

## What makes Github actions a powerful tool

### Matrix build 
### Real-time feedback
### Edit, Reuse, and Share Actions and Workflow like Code

## Use Cases

Always remember that the goal is to have fewer bugs in production and faster feedback while developing.

