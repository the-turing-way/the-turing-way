(rr-ci-ghactions)=
# Continuous Integration with GitHub Actions

**GitHub Actions** is a task automation system fully integrated with GitHub. In other words, it is an API that orchestrates any workflow, based on any event. It can make makes it easier than ever to incorporate CI into the repositories. It is a flexible way to automate nearly every aspect of your software workflow. Here are just a few use cases of GitHub Actions:

- Automated testing (CI)
- Continuous delivery and deployment
- Responding to workflow triggers using issues, `@` mentions, labels, and more
- Triggering code reviews
- Managing branches
- Triaging issues and pull requests

Automated events take place throughout this process. These events can range from running tests or deployments to cross-linking to relevant threads. Here's an example that we will use:

- Source code goes through an automated build process if necessary
- Automated testing of the software takes place
- Reports are generated and sent back to the developers with the status of their changes

## Getting started with GitHub Action

GitHub Actions uses YAML syntax and stored in a directory called `.github/workflows` in the repository. You can either use a templated workflow or create your own.
1- Using GitHub Actions template

If you want to get started with GitHub Actions, you can start by clicking the "Actions" tab in the repository where you want to create a workflow as shown below.

2- Using libraries-specific templates. 
 


## GitHub-related Vocabulary
<!-- (I'll explain each vocab separately using diagrams made with adobe illustrator) -->

**1. WorkFlow**

The workflow is is a unit of automation from start to finish. It consisits of all the aspects which should be taken into account during the atomation including what event can be trigger the automation. The workflow can be used to build, test, package, release, or deploy a project on GitHub.

**2. Job**

A job is a section of the workflow, and is made up of one or more steps. In this section of our workflow, the template defines the steps that make up the build job.

**3. Step**

Step: A step represents one effect of the automation. A step could be defined as a GitHub Action, or another unit, like printing something to the console.

**4. Actions**

A GitHub Action is a piece of automation written in a way that is compatible with workflows. Actions can be written by GitHub, by the open source community, or you can write them yourself!


## Building a block of a WorkFlow
**1. name**
This is the name of the workflow. GitHub will use this name to be displayed on the repository's actions page.
```
name:
    CI package
```
**3. on**
The `on` field tells GitHub Actions when to run. For exmple, we can run the workflow anytime there's a `push` or a `pull`. 
```
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
```
There are many events which can be used to trigger a workflow. You can explore them [here](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions).

**5. jobs**

Any workflow is consisted of one or more jobs. Every job also runs in an environment specified by`runs-on`. These Jobs run in parallel by default but can also be defined to run sequentially.
```
Jobs:
    runs-on: ubuntu-latest
``` 
This block defines the core component of an Actions workflow. Workflows are made of `jobs`. Every job also needs a specific host machine on which to run, the `runs-on:` field is how we specify it. The template workflow is running the `build` job in the latest version of Ubuntu, a Linux-based operating system.

We can also separate the `build` and `test` functions of our workflow into more than one job that will run when our workflow is triggered.

```

jobs:
  build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v2
  test:
    - name: npm install, and test
    run: |
      npm install
      npm test
    env:
      CI: true
```
**7. steps**

It is the linear sequence of operations that make up a job. 
- `uses: actions/checkout@v1`: uses a community action called [`checkout`](https://github.com/actions/checkout) to allow the workflow to access the contents of the repository
- `uses: ./action-a` : provides the relative path to the action we created in the `action-a` directory of the repository
- `with`: is used to specify the input variables that will be available to your action in the runtime environment. In this case, the input variable is `MY_NAME`, and it is currently initialized to `"Mona"`.


## Use Cases

Always remember that the goal is to have fewer bugs in production and faster feedback while developing.

