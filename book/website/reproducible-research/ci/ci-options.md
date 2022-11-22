(rr-ci-options)=
# What is continuous integration?

Continuous integration (CI) is the practice of integrating changes to a project made by individuals into a main, shared version frequently (usually multiple times per day). CI software is also typically used to identify any conflicts and bugs that are introduced by changes, so they are found and fixed early, minimising the effort required to do so. Running tests regularly also saves humans from needing to do it manually. By making users aware of bugs as early as possible researchers (if the project is a research project) do not waste a lot of time doing work that may need to be thrown away, which may be the case if tests are run infrequently and results are produced using faulty code.

This chapter demands a strong understanding of version control. The central concepts you will need to recall are:

- How it can be used to enable people collaborating on a single project to combine their work via merging
- What merge conflicts are and the difficulties they can present
- What GitHub is and how to use it

In brief if a group of researchers are collaborating on a project it is good practice for them to use version control to keep track of their changes over time, and combine their work regularly. If they do not combine (integrate) their work regularly then when they come to do so it is likely to be very difficult as different people may have made contradictory changes.

Continuous Integration is a software development practice where members of a team integrate their work frequently, rather than doing work in isolation and merging in large changes at infrequent intervals. In CI usually each person integrates at least daily. Each integration is verified by an automated build (usually including tests) to detect integration errors as quickly as possible.

The idea is to minimize the cost of integration by making it an early consideration. Researchers can discover conflicts at the boundaries between new and existing code early, while they are still relatively easy to reconcile. Once the conflict is resolved, work can continue with confidence that the new code honours the requirements of the existing codebase. The goal is to build healthier software by developing and testing in smaller increments. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop more rapidly.

Integrating code frequently does not, by itself, offer any guarantees about the quality of the new code or functionality. This leads us to the second aspect of CI. When a developer merges code into the main repository, automated processes build a working version of the project. Afterwards, test suites are run against the new build to check whether any bugs were introduced. If either the build or the test phase fails, the team is alerted so that they can work to fix the problem. It is easier to fix a bug in something you wrote a few minutes ago than something you wrote yesterday (or last week, or last month).

By ensuring that your code is built and tested regularly CI helps researchers to demonstrate that their code does what it claims to do, and that it does so correctly. Typically, continuous integration servers will also allow build-and-test jobs to run at specific times, so a [cron job](https://en.wikipedia.org/wiki/Cron), nightly-build-and-test, can be done, as well as a build-and-test job run on-demand.


## Some options for CI service providers, covering the most often used ones

There are many CI service providers readily available, providing free access for open, public projects. Each of these
services however has its own advantages and disadvantages.  In this section we provide a brief overview with links to
examples to help you select the most suitable one for you.  Alternatively a few systems also provide the option of self-hosting.

 - [GitHub Actions](https://help.github.com/en/actions), for some examples see the [language and framework guides](https://help.github.com/en/actions/language-and-framework-guides) and [this tutorial](https://github.com/NLESC-JCER/ci_for_science#-github-actions).
 - [GitLab CI](https://docs.gitlab.com/ee/ci/), for some examples the [GitLab CI examples](https://docs.gitlab.com/ee/ci/examples/README.html) and [this tutorial](https://github.com/NLESC-JCER/ci_for_science#-gitlab-ci).
 - [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/), for some examples see the [ecosystem support page](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/?view=azure-devops) and [this tutorial](https://github.com/trallard/ci-research).
 - [Circle CI](https://circleci.com/), for getting started visit [this circleCI project tutorial](https://circleci.com/docs/2.0/project-walkthrough/) or [these shorter "Hello World" examples](https://circleci.com/docs/2.0/hello-world/).
 - [Jenkins](https://www.jenkins.io/), for some examples the see [this tutorial](https://www.jenkins.io/doc/tutorials/)
 - [Travis CI](https://travis-ci.com/), for some examples the [Travis tutorial](https://docs.travis-ci.com/user/tutorial/).


A more extensive list of CI service providers can be found in [this guide](https://www.software.ac.uk/resources/guides/hosted-continuous-integration)
provided by the Software Sustainability Institute.
