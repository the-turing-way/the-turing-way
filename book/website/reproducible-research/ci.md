(rr-ci)=
# Continuous integration

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Necessary | Continuous integration will follow command line instructions
| [Version control](./version-control) | Necessary | Continuous integration runs every time a new _commit_ is made to your project |
| [Reproducible computational environments](./reproducible-environments) | Necessary | Continuous integration runs your tests on a separate computer (usually in the cloud) so you need to set it up in the same way. |
| [Testing](./testing) | Very helpful | Continuous integration _tests_ if anything important has changed when you make a change in your project |

## Summary

Continuous integration (CI) is the practice of integrating changes to a project made by individuals into a main, shared version frequently (usually multiple times per day). CI software is also typically used to identify any conflicts and bugs that are introduced by changes, so they are found and fixed early, minimising the effort required to do so. Running tests regularly also saves humans from needing to do it manually. By making users aware of bugs as early as possible researchers (if the project is a research project) do not waste a lot of time doing work that may need to be thrown away, which may be the case if tests are run infrequently and results are produced using faulty code.

```{figure} ../figures/continuous-integration-nov20.jpg
---
name: continuous-integration-nov20
alt: An illustration on how continuous integration works with multiple jobs and actions working alonside each other to then feed into an illustration of steps to show merging into the main version.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

## How this will help you/ why this is useful

CI has a number of key benefits:

- Helps bugs to be found early, minimising their damage and making them easier to fix
- Keeps project contributors up to date with each other's work so they can benefit from it as soon as possible
- Encourages users to write tests
- Automates running of tests
- Ensures tests are run frequently

## What is continuous integration?

This chapter demands a strong understanding of version control. The central concepts you will need to recall are:

- How it can be used to enable people collaborating on a single project to combine their work via merging
- What merge conflicts are and the difficulties they can present
- What GitHub is and how to use it

In brief if a group of researchers are collaborating on a project it is good practice for them to use version control to keep track of their changes over time, and combine their work regularly. If they do not combine (integrate) their work regularly then when they come to do so it is likely to be very difficult as different people may have made contradictory changes.

Continuous Integration is a software development practice where members of a team integrate their work frequently, rather than doing work in isolation and merging in large changes at infrequent intervals. In CI usually each person integrates at least daily. Each integration is verified by an automated build (usually including tests) to detect integration errors as quickly as possible.

The idea is to minimize the cost of integration by making it an early consideration. Researchers can discover conflicts at the boundaries between new and existing code early, while they are still relatively easy to reconcile. Once the conflict is resolved, work can continue with confidence that the new code honours the requirements of the existing codebase. The goal is to build healthier software by developing and testing in smaller increments. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop more rapidly.

Integrating code frequently does not, by itself, offer any guarantees about the quality of the new code or functionality. This leads us to the second aspect of CI. When a developer merges code into the main repository, automated processes build a working version of the project. Afterwards, test suites are run against the new build to check whether any bugs were introduced. If either the build or the test phase fails, the team is alerted so that they can work to fix the problem. It is easier to fix a bug in something you wrote a few minutes ago than something you wrote yesterday (or last week, or last month).

By ensuring that your code is built and tested regularly CI helps researchers to demonstrate that their code does what it claims to do, and that it does so correctly. Typically, continuous integration servers will also allow build-and-test jobs to run at specific times, so a [CRON](https://en.wikipedia.org/wiki/Cron)-like, nightly-build-and-test, can be done, as well as a build-and-test job run on-demand.

### What are continuous delivery and continuous deployment?

Technically speaking the above explanation conflates three related concepts, continuous integration, continuous deployment, and continuous delivery. In reality:

- Continuous integration focuses on regularly integrating work from individual researchers into a main repository.
- Continuous delivery automates and runs the steps required to build and test the project.
- Continuous deployment takes this one step further by automatically deploying each time a code change is made.

In this chapter this entire process is referred to as continuous integration for the sake of simplicity.
