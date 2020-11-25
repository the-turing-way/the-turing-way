# What is the difference between continuous delivery and continuous deployment?

Technically speaking the above explanation conflates three related concepts, continuous integration, continuous deployment, and continuous delivery. In reality:

- Continuous integration focuses on regularly integrating work from individual researchers into a main repository.
- Continuous delivery automates and runs the steps required to build and test the project.
- Continuous deployment takes this one step further by automatically deploying each time a code change is made.

In this chapter this entire process is referred to as continuous integration for the sake of simplicity.

# Continuous integration

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Necessary | Continuous integration will follow command line instructions
| [Version control](./version-control) | Necessary | Continuous integration runs every time a new _commit_ is made to your project |
| [Reproducible computational environments](./reproducible-environments) | Necessary | Continuous integration runs your tests on a separate computer (usually in the cloud) so you need to set it up in the same way. |
| [Testing](./testing) | Very helpful | Continuous integration _tests_ if anything important has changed when you make a change in your project |

# What are the options for CI service providers?

There are many CI service providers, such as GitHub Actions and Travis CI. Each of these services has its own advantages and disadvantages. In this section we provide a brief overview with links to examples to help you select the most suitable one for you.

 - [GitHub Actions](https://help.github.com/en/actions), for some examples see the [language and framework guides](https://help.github.com/en/actions/language-and-framework-guides) and [this tutorial](https://github.com/NLESC-JCER/ci_for_science#-github-actions).
 - [Circle CI](https://circleci.com/), for some examples see [here](https://circleci.com/docs/2.0/project-walkthrough/) and [here](https://circleci.com/docs/2.0/hello-world/).
 - [GitLab CI](https://docs.gitlab.com/ee/ci/), for some examples the [GitLab CI examples](https://docs.gitlab.com/ee/ci/examples/README.html) and [this tutorial](https://github.com/NLESC-JCER/ci_for_science#-gitlab-ci).
 - [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/), for some examples see the [ecosystem support page](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/?view=azure-devops) and [this tutorial](https://github.com/trallard/ci-research).

A more extensive list of CI service providers can be found [here](https://www.software.ac.uk/resources/guides/hosted-continuous-integration).
