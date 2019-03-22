# Continuous integration

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| Experience with the command line | Necessary | A tutorial on working via the command line can be found [here](https://programminghistorian.org/en/lessons/intro-to-bash) |
| Version control | Necessary | See the chapter on this for more information |
| Testing | Very helpful | See the chapter on this for more information  |
| Reproducible computational environments | Necessary | See the chapter on this for more information, particularly the sections on YAML files and containers |

## Table of contents

- [Summary](#Summary)
- [How this will help you/ why this is useful](#Why_this_is_useful)


- [Best practise for continuous integration](#Best_practise_for_continuous_integration)
  - [Small, iterative changes](#Small_iterative_changes)
  - [Trunk-based development](#Trunk_based_development)
  - [Keep the building and testing phases fast](#Keep_the_building_and_testing_phases_fast)
  - [Dependencies tracking](#Dependencies_tracking)
  - [Consistency throughout the pipeline](#Consistency_throughout_the_pipeline)

<a name="Summary"></a>
## Summary
> easy to understand summary - a bit like tl;dr

*Need to say abbreviation = CI near the top*

<a name="Why_this_is_useful"></a>
## How this will help you/ why this is useful

*Very brief, say helps coordinate/runs tests* Just a few bullet points

- Encourages the writing of tests
- If you include tests then you don't need to remember to run them, it's done automatically each time


Using CI is important to:
- Find out if there are problems early on.

<a name="What_is_continuous_integration"></a>
## What is continuous integration?

This chapter demands a strong understanding of version control. The central concepts you will need to recall are:

- How it can be used to enable people collaborating on a single project to combine their work via merging
- What merge conflicts are and the difficulties they can present

In brief if a group of researchers are collaborating on a project it is good practise for them to use version control to keep track of their changes over time, and combine their work regularly. If they do not combine (integrate) their work regularly then when they come to do it is likely to be very difficult as different people may have made contradictory changes.

Continuous Integration is a software development practice where members of a team integrate their work frequently, rather than doing work in isolation and merging in a large change when they're done. Usually each person integrates at least daily. Each integration is verified by an automated build (usually including tests) to detect integration errors as quickly as possible.

The idea is to minimize the cost of integration by making it an early consideration. Researchers can discover conflicts at the boundaries between new and existing code early, while conflicts are still relatively easy to reconcile. Once the conflict is resolved, work can continue with confidence that the new code honours the requirements of the existing codebase. The goal is to build healthier software by developing and testing in smaller increments.  Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop more rapidly.

Integrating code frequently does not, by itself, offer any guarantees about the quality of the new code or functionality. This leads us to the second aspect of CI. When a developer merges code into the main repository, automated processes build a working version of the project. Afterwards, test suites are run against the new build to check whether any problems were introduced. If either the build or the test phase fails, the team is alerted so that they can work to fix the problem. It is easier to fix a bug in something you wrote a few minutes ago, than something you wrote yesterday (or last week, or last month).

By ensuring that your code is built and tested regularly CI helps researchers to demonstrate that their code does what it claims to do, and that it does so correctly. Typically, continuous integration servers will also allow build-and-test jobs to run at specific times, so a CRON-like, nightly-build-and-test, can be done, as well as a build-and-test job run on-demand.

### What are continuous delivery and continuous deployment?

Technically speaking the above explanation conflates three related concepts, continuous integration, continuous deployment, and continuous delivery. In reality:

- Continuous integration focuses on regularly integrating work from individual researchers into a main repository.
- Continuous delivery automates and runs the steps required to build and test the project.
- Continuous deployment takes this one step further by automatically deploying each time a code change is made.

In this chapter this entire process is referred to as continuous integration for the sake of simplicity.

## What is Travis and how does it work?

There are a number of CI tools available, such Circle (tutorials [here](https://circleci.com/docs/2.0/project-walkthrough/) and [here]([CircleCI Hello World.](https://circleci.com/docs/2.0/hello-world/)). A list of other CI tools can be found [here](https://www.software.ac.uk/resources/guides/hosted-continuous-integration). In this chapter we will focus on [Travis](https://travis-ci.org/) because it's free (if your code is openly available), widely used, and well integrated with the version control platform [GitHub](https://github.com/).

To use Travis you will need to add a file to your project called `.travis.yml` which describes the computational environment to run the project in, and includes a script to run your tests. See the chapter on reproducible computational environments for more information on them, including writing `.yml` files to specify them. See the chapter on testing for information on writing and automating tests. The .travis.yml has a number of other capabilities, which will be described [later] *liiiiiiiiiiiiiiiiiiiiiink* along with more detailed instructions for writing these files.

Once Travis has been set up on a project then each time a commit is made it:

- Clones a copy of your project
- Generates a copy of the computational environment specified in the .travis.yml file in a brand new virtual environment
- Builds the project within that environment
- Runs the tests by following the script specified in the .travis.yml file
- Reports the results
  - Travis will attach a badge to the results, green if all steps in the script (which run the tests) pass, red if not. The badge will be yellow whilst the tests are still running. If Travis is unable to generate the computational environment described in the .travis.yml file then it will not proceed futher and the badge will be grey.
  - Travis will also report the results via email (notification settings can be adjusted).

You can use Travis to test your project in multiple computational environments my specifying them in the .travis.yml file. A quick note on Travis vocabulary:

- Job - an automated process that clones your repository into a virtual environment and then carries out a series of phases such as compiling your code, running tests, etc. A job fails if the return code of the script encounters an error.
- Build - a group of jobs. For example, a build might have two *jobs*, each of which tests a project with a different version of a programming language. A build finishes when all of its jobs are finished.

## Setting up continuous integration with Travis

### Basic steps

- Write a `.travis.yml` file and add it to your project.
- Upload your project to GitHub if you have not already.
- Go to [Travis-ci.com](https://travis-ci.com) and [Sign up with GitHub](https://travis-ci.com/signin).
- Accept the Authorization of Travis CI. You'll be redirected to GitHub.
- You will see a list of your GitHub repositories with buttons next to them. Click the button next to your project repository to activate Travis on it.
- Check the build status page to see if your build [passes or fails](/user/job-lifecycle/#breaking-the-build), according to the return status of the build command by visiting the [Travis CI](https://travis-ci.com/auth) and selecting your repository.
- Next time you commit to your repository Travis will run on the updated version of your project and report the results.

It's that simple. The rest of this section will describe the different components of the .travis.yml file and how to write them.

<a name="The_travis_yml_file"></a>
### Setting up the computational environment

This page on [Common Builds Problems](/user/common-build-problems/) is a good place to start troubleshooting if your build is broken.

#### Operating system

Travis CI works with a few different operating systems. In the .travis.yml  file define the operating system to run a project on via the os keyword like:
```
os: linux
```

or
```
os: macOS
```

or
```
os: windows
```

It is possible to build and test a project on multiple operating systems. This will be not be discussed here as this presents and extra level of complexity and will not be needed in most cases for research, but it is discussed later *aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadddddddd link*.

#### Programming language

Specify the programming language to run your project with using the language keyword, and specify which version of the language to use. So for python2.7 this would look like:
```
language: python
python:
- "2.7"
```
Further information on the programming languages that are compatible with Travis can be found [here](https://docs.travis-ci.com/user/languages/)

#### Compilers

If a compiled language is being used which compiler to use can be specified with the compiler keyword:
```
compiler:
  - gcc
```

#### Dependencies

Not all languages/software are available on all operating systems however they can typically be installed within the .travis.yml file.

To install Ubuntu packages that are not included in the standard version of the operating system specified you can include a `before_install` step in your `.travis.yml` along with the necessary code to install it, e.g.:

```
before_install:
  - sudo apt-get install -y libxml2-dev
```

#### Containers

It is possible to use Docker containers (see the reproducible computational environments chapter) to generate the computational environment but pulling and running the image from the .travis.yml file. See [here](https://docs.travis-ci.com/user/docker/) for more information on this.

### The .travis.yml script

Travis will report that the build has failed if any commands in the script section return an error. Technically any commands can be included in the scrpt, but it is mainly used for running tests. A script does not need to be long or complicated, as demonstrated by this example which uses the pytest command to run tests in python scripts:
```
script:
- pytest
```

If there are steps that need to be done before a project to be considered to be "fully" working these should also be included in the script too. Lets say some project needs a figure to be converted to a png file for some reason. the script could included
```
  - convert figure_name.jpg figure_name.png
```

If for any reason this cannot be done an error will be returned and the build will be marked as having failed.

### After success

The after success section is much like the script section in that it contains commands to run on the project. The key difference if that the build will not fail if steps in the after success section return errors.

The after success section is run after the script, and can be used to automate steps that need to be taken once a build has passed all the tests. Examples of things that can be automated include automatically merging the new version of the project to the master branch in GitHub. Another example is for the code coverage (see testing chapter) to be automatically measured and reported.

### Testing a project with multiple versions of a programming language

When a project is expected to be run on systems with different versions of a programming language you can set Travis to run the tests on each of these versions, for example to test on a variety of versions of python:
```
language: python
python:
  - "2.6"
  - "2.7"
  - "3.2"
  - "3.3"
```

### Testing your project on multiple operating systems

If your code is used on multiple operating systems it should be tested on multiple operating systems. To enable testing on multiple operating systems add multiple entries under the `os` key in your `.travis.yml` file, e.g.:
```
os:
  - linux
  - osx
```

When you test your code on multiple operating systems, be aware of differences that can affect your tests, for example not all tools and programming languages are available on all operating systems. This should be taken into account when write commands for your script file (or other sections of the .travis.yml file). Also file system behaviour may differ between OSs. Your tests may implicitly rely on these behaviours, and could fail because of them. They are different operating systems, after all.

When Travis is running a job it sets the `TRAVIS_OS_NAME` variable which describes the operating system being tested. you can use this to run commands only on specified operating systems like this:
```
  - if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then command_to_run; fi
```

It is possible to go further and construct a [build matrix](https://docs.travis-ci.com/user/build-matrix/) to test a the project in a range of computational environments.

#### Allowing Failures

To ignore the results of jobs on one operating system you can define rows that are allowed to fail in the build matrix by adding an  `allow_failures` section. Allowed failures are items in your build matrix that are allowed to fail without causing the entire build to fail.  For example to allow the build to pass even if the build using the osx operating system you'd add the following to your `.travis.yml`:
```
matrix:
  allow_failures:
    - os: osx
```

This is useful if you ideally want the build to be successful in multiple environments, but not all of them are vital.

## Limitations of CI

CI does have its limitations. Firstly it is only as effective at finding bugs as the test provided to it. If a project contains few or poor tests then it is entirely possible the project will contain bugs the tests do not catch and Travis will report the build as successful.

Secondly, depending on the nature of your project there may be security considerations to think about. Because Travis is only free if projects are open source



    If your tests require authentication credentials, do not run tests from PRs (as PRs can include code that exposes such credentials). Comment by Noam Ross when I asked a question about this practice on one the rOpenSci packages I was editor on:
    > If your test suite needs credentials, then running all tests on PRs is not great security practice; someone can create a PR that will reveal/do something nasty with your credentials. I think it is best practice to reduce the extent of tests requiring credentials with conditional statements testing for the presence of things like the encrypted environment variables, and use mocking for things like testing processing of returned values.

    [security](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/best-practices-security.md) **MIT**

    Travis CI obfuscates secure environment variables and tokens displayed in by the user interface. The [documentation about encryption keys](/user/encryption-keys/) outlines the build configuration required to set this up. However, if secret information is outputted in the course of running a script (for example in an error message) it may be included in Travis's build logs which may be accessible by others. To prevent leaks like this, secure environment variables and tokens that are longer than three characters are automatically filtered at runtime, effectively removing them from the build log, displaying the string `[secure]` instead. Nevertheless you should rotate your tokens and secrets regularly.

    There are however many ways in which secure information can accidentally be exposed. These vary according to what tools you are using being used and the settings you enabled. Some things to look out for are:

    - settings which duplicate commands to standard output, such as `set -x` or `set -v` in your bash scripts
    - displaying environment variables, by running `env` or `printenv`
    - printing secrets within the code, for example `echo "$SECRET_KEY"`
    - git commands like `git fetch` or `git push` may expose tokens or other secure environment variables
    - settings which increase command verbosity

    Preventing commands from displaying any output is one way to avoid accidentally displaying any secure information. If there is a particular command that is using secure information you can redirect its output to `/dev/null` to make sure it does not accidentally publish anything, as shown in the following example:

    ```
    sh
    git push url-with-secret >/dev/null 2>&1
    ```

<a name="Best_practise_for_continuous_integration"></a>    
## Best practise for continuous integration

<a name="Small_iterative_changes"></a>  
### Small, iterative changes

One of the most important practices when adopting continuous integration is to encourage small changes. Small changes minimize the possibility and impact of problems cropping up when they're integrated, this minimises the cost of integration.

<a name="Trunk_based_development"></a>  
### Trunk-based development

With trunk-based development, work is done in the main branch of the repository or merged back into the shared repository at frequent intervals. Short-lived feature branches are permissible as long as they represent small changes and are merged back as soon as possible.

The idea behind trunk-based development is to avoid large commits that violate of concept of small, iterative changes discussed above. Code is available to peers early so that conflicts can be resolved when their scope is small.

<a name="Keep_the_building_and_testing_phases_fast"></a>  
### Keep the building and testing phases fast

Because the build and test steps must be performed frequently, it is essential that these processes be streamlined to minimize the time spent on them. Increases in build time should be treated as a major problem because the impact is compounded by the fact that each commit kicks off a build.

When possible, running different sections of the test suite in parallel can help move the build through the pipeline faster. Care should also be taken to make sure the proportion of each type of test makes sense. Unit tests are typically very fast and have minimal maintenance overhead. In contrast, automated system or acceptance testing is often complex and prone to breakage. To account for this, it is often a good idea to rely heavily on unit tests, conduct a fair number of integration tests, and then back off on the number of later, more complex testing.

<a name="Dependencies_tracking"></a>  
### Dependencies tracking

Checking for dependency updates should be done regularly. It can save a lot of time, avoiding bugs due to code dependent on deprecated functionality. Services such as [David](https://david-dm.org/) are available for dependency management.

<a name="Consistency_throughout_the_pipeline"></a>  
### Consistency throughout the pipeline

A project should be built once at the beginning of the pipeline, the resulting software should be stored and accessible to later processes without rebuilding. By using the exact same artefact in each phase, you can be certain that you are not introducing inconsistencies as a result of different build tools.

Also, the environment defined by the .travis.yml file should reflect the actual environment the code is run in. If that environment is modified don't forget to update the .travis.yml file, otherwise the results Travis returns will not be trustworthy.

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next

If you have not already read the testing chapter it is suggested to do so to learn more about the different kinds of tests and their benefits in order to make the most of CI.

## Further reading

Travis offers a great deal of functionality not described here for automating other processes related to the testing and deployment of  projects. Look into these, the Travis [documentation](https://docs.travis-ci.com/user/deployment) offers a good starting point for this.

A list of example Travis builds and tests for various languages/frameworks is available [here](https://github.com/softwaresaved/build_and_test_examples).

Travis's official tutorial is [here](ttps://docs.travis-ci.com/user/tutorial/). A tutorial focussed on using Travis with R can be found [here](https://juliasilge.com/blog/beginners-guide-to-travis/), tutorials geared towards python can be found [here](https://docs.python-guide.org/scenarios/ci/) and [here](https://docs.travis-ci.com/user/languages/python/).

## Definitions/glossary

**:**

**Build:**

**Continuous integration:**

**:**

**:**

**:**

**Travis:**

**:**

**:**

**:**


## Bibliography

### Materials used: What is continuous integration?

- [What is CI](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/for-beginners.md) **MIT**
- [SSI blog](https://software.ac.uk/using-continuous-integration-build-and-test-your-software?_ga=2.231776223.1391442519.1547641475-1644026160.1541158284)
- [The difference between continuous integration, continuous deployment, and continuous delivery](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
- [Martin Fowler, who first wrote about Continuous Integration (short: CI) together with Kent Beck via CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**


### Materials used: Best practise for continuous integration

- [Continuous integration, continuous deployment and continuous delivery](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
- [Netherlands eScience Center guide](https://guide.esciencecenter.nl/best_practices/testing.html) **Creative Commons Attribution 4.0 International**

### Materials used: What is Travis and how does it work?

- [Info about how Travis works](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/for-beginners.md) **MIT**

### Materials used: Setting up continuous integration with Travis

- [Light travis tutorial](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/tutorial.md) **MIT**
- [CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**
- [Installing dependencies via yaml](https://github.com/travis-ci/docs-travis-ci-com/edit/master/user/installing-dependencies.md) **MIT**
- [Testing multiple versions of programming languages](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)**
- [Using Travis with multiple operating systems](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/multi-os.md) **MIT**
- [Travis docs: customising the build](https://docs.travis-ci.com/user/customizing-the-build/) **MIT**

## Acknowledgements

Thanks to David Jones of the University of Sheffield RSE group for useful discussions.
