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

There are a number of CI tools available, such Circle (tutorials [here](https://circleci.com/docs/2.0/project-walkthrough/) and [here]([CircleCI Hello World.](https://circleci.com/docs/2.0/hello-world/)). A list of others CI tools can be found [here](https://www.software.ac.uk/resources/guides/hosted-continuous-integration). In this chapter we will focus on [Travis](https://travis-ci.org/) because it's free (if your code is openly available), widely used, and well integrated with the version control platform [GitHub](https://github.com/).

*To use Travis with a project the project must include a file called `.travis.yml` file. This file must specify the computational environment to run the project and conatin a script to run any tests/ o other steps to run each time a change to the code is integrated. The .travis.yml file can also do a whole buch other stuff. Hoe to wwrite these files covered in detail later. Minimum this needs to include is a script, if the script runs sucessfully travis will pass it.*

 Green, amber, red
  - failures in "install" section create travis build fail errors (grey message - test didn't run)
  - failures in "script" creates test failure and thus red error messages
  - yellow while it's running

    - *You can make "test passed" a requirement for merging *
      - *you can protect branches so that there's no way to merge a pull request unless the tests pass.*
  - *How to link github repo and travis*



  [Info about how travis works](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/for-beginners.md) **MIT**


  ## CI builds and automation: building, testing, deploying

*runs script not tests*
  When you run a build, Travis CI clones your GitHub repository into a brand new virtual environment, and build and test your code. If one or more of those tasks fails, the build is considered broken. If none of the tasks fail, the build is  considered passed, and Travis CI can deploy your code to a web server, or application host.

  CI builds can also automate other parts of your delivery workflow. This means you can setup [notifications](/user/notifications/) and many other tasks.

  ## Builds, Jobs, Stages and Phases

  In the Travis CI documentation, some common words have specific meanings:

  - Job - an automated process that clones your repository into a virtual environment and then carries out a series of phases such as compiling your code, running tests, etc. A job fails if the return code of the `script` encounters an error.
  - Build - a group of jobs. For example, a build might have two *jobs*, each of which tests a project with a different version of a programming language. A build finishes when all of its jobs are finished.

  ## Breaking the Build

  The build is considered broken when one or more of its jobs completes with a
  state that is not passed:

   - *errored* - a command in the `before_install`, `install`, or `before_script`
     phase returned a non-zero exit code. The job stops immediately.
   - *failed* - a command in the `script` phase returned a non-zero exit code. The
     job continues to run until it completes.
   - *canceled* - a user cancels the job before it completes.

This page on [Common Builds Problems](/user/common-build-problems/) is a good place to start troubleshooting if your build is broken.


## Setting up continuous integration with Travis

  [light travis tutorial](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/tutorial.md) **MIT**

 [Core Concepts for Beginners](/user/for-beginners)

---

## To get started with Travis CI

1. Go to [Travis-ci.com](https://travis-ci.com) and [*Sign up with GitHub*](https://travis-ci.com/signin).

2. Accept the Authorization of Travis CI. You'll be redirected to GitHub.

3. Click the green *Activate* button, and select the repositories you want to use with Travis CI.

4. Add a `.travis.yml` file to your repository to tell Travis CI what to do.

5. Add the `.travis.yml` file to git, commit and push, to trigger a Travis CI build:

6. Check the build status page to see if your build [passes or fails](/user/job-lifecycle/#breaking-the-build), according to the return status of the build command by visiting the [Travis CI](https://travis-ci.com/auth) and selecting your repository.


---
[CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**

In order to activate testing for your project, go to the Travis-CI site and login with your GitHub account. Then activate your project in your profile settings and you’re ready to go. From now on, your project’s tests will be run on every push to GitHub.

---

- .travis.yml
  - Outline minimum basic structure


As Travis files are so small, they "hide" quite a lot of the action (similar to binder, it might make it too easy) - the log gives full transparency of the "magic"  

Travis files start with . so they might be hidden files

### Setting up the computational environment

#### Operating system

Travis CI works with a few different operating systems. In the .travis.yml  file define the operating system to run a project on via
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

It is also possible to build and test a project on multiple operating systems. This will be not be discussed here as this presents and extra level of complexity and will not be needed in most cases, but it is discussed later *aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadddddddd link*.

#### Selecting a different programming language

Travis CI supports many [programming languages](/user/languages/). In the `.travis.yml` languages can be specified like

```
language: ruby
language: java
language: php
```

[CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**


- Dockefiles can be used with Travis
 [install dependencies](/user/job-lifecycle/#customizing-the-installation-phase)

---

[Installing dependencies via yaml](https://github.com/travis-ci/docs-travis-ci-com/edit/master/user/installing-dependencies.md) **MIT**

## Installing Packages on Standard Infrastructure


Not all languages/software are available on all operating systems however they can typically be installed within the .travis.yml file.

To install Ubuntu packages that are not included in the standard [precise](/user/reference/precise/), [trusty](/user/reference/trusty/), or [xenial](/user/reference/xenial/) distributions, use apt-get in the `before_install` step of your `.travis.yml`:

```
before_install:
  - sudo apt-get install -y libxml2-dev
```


## The .travis.yml script

If there is anything that it will need to carry out the script beyond the linux command line you need to install it, set lenguages to run any tests, etc. If that's a lot/complex then continers etc are good, but those do kind of hide things, pros and cons.

    - Script, say to run tests/do anything else (**check compiled successfully for compiled languages?**)

If you've got steps that NEED to be taken and you want fail to return if not (e.g. push online) then they need to go in the script, not an after sucesss section because travis doesn't care if things in after sucess fail.

TRAVIS DOESN'T KNOW WHAT A TEST IS
 -- it just runs commands and throws errors


     Working through the scona travis file

     https://github.com/WhitakerLab/scona/blob/dev/.travis.yml

     Here are a few updates:

     ```
     language: python
     python:
     #  - "3.5"
       - "3.6"
     install:
       - pip install -q networkx==$NETWORKX_VERSION
       - pip install -q -r requirements.txt
       - pip install sphinx sphinx sphinxcontrib-napoleon sphinx_rtd_theme
     script:
      #- python3 -m pytest -v
       - cd docs
       - make html
       - touch .nojekyll

     ```


         script section is where tests are run; those are just unit commands
         - this uses language specific tests so you need to be aware of test conventions in the language you use
         - If any of the scripts fail, the build fails.

## After success

- After success (optional)
   - E.g. automatically merge.
Can have need approving review or tests pass or both or nither before merging is alowed.

Travis CI isn't just for running tests, there are many others things you can do with your code:

* deploy to [GitHub pages](/user/deployment/pages/)
* run apps on [Heroku](/user/deployment/heroku/)
* upload [RubyGems](/user/deployment/rubygems/)
* send [notifications](/user/notifications/)

---

[travis multiple operating systems](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/multi-os.md) **MIT**

If your code is used on multiple operating systems it probably should be tested on
multiple operating systems. Travis CI can test on Linux and macOS.

To enable testing on multiple operating systems add the `os` key to your `.travis.yml`:

```
os:
  - linux
  - osx
  - windows
```

If you are already using a [build matrix](/user/customizing-the-build/#build-matrix) to test multiple versions, the `os` key also multiplies the matrix.

## Allowing Failures

To ignore the results of jobs on one operating system, add the following
to your `.travis.yml`:

```
matrix:
  allow_failures:
    - os: osx
```

[Travis docs: customising the build](https://docs.travis-ci.com/user/customizing-the-build/) **MIT**
You can define rows that are allowed to fail in the build matrix. Allowed failures are items in your build matrix that are allowed to fail without causing the entire build to fail. This lets you add in experimental and preparatory builds to test against versions or configurations that you are not ready to officially support.

Define allowed failures in the build matrix as key/value pairs:

```
matrix:
  allow_failures:
  - rvm: 1.9.3
```

Can test it using multiple versions of python etc by having multiple versions of python specified under languages.

Specifying the language saves you from manually installing it/choosing a docker with it in your install section. It's a shortcut.

Q: if you have more than one language for your code, can you use travis for that?

Yes - best to start with something more simple but you can add a second language too. Do those tricky kinds of things in the script in case you need to run certain files with certain languages.
In order to get started, add a .travis.yml file to your repository with this example content:

```
language: python
python:
  - "2.6"
  - "2.7"
  - "3.2"
  - "3.3"
# command to install dependencies
script: python tests/test_all_of_the_units.py
branches:
  only:
    - master
```

This will get your project tested on all the listed Python versions by running the given script, and will only build the master branch. There are a lot more options you can enable, like notifications, before and after steps, and much more. The Travis-CI docs explain all of these options, and are very thorough.

## Example Multi OS Build Matrix

## Operating System differences

When you test your code on multiple operating systems, be aware of differences
that can affect your tests:

- Not all tools may be available on macOS.

  We are still working on building up the toolchain on the [macOS Environment](/user/reference/osx/).
  Missing software may be available via Homebrew.

- Language availability.

  Not all languages are available on all operating systems.

- The file system behaviour is different. Your tests may implicitly rely on these behaviours, and could fail because of them. They are different operating systems, after all.

  Commands may have the same name on the Mac and Linux, but they may have different flags, or the same flag may mean different things. In some cases, commands that do the same thing could have different names.

Here's an example `.travis.yml` file using if/then directives to customize the [build lifecycle](/user/job-lifecycle/) to use [Graphviz](https://graphviz.gitlab.io/) in both Linux and macOS.

```
language: c

os:
  - linux
  - osx

compiler:
  - gcc
  - clang

addons:
  apt:
    packages:
      - graphviz

before_install:
  - if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then brew update          ; fi
  - if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then brew install graphviz; fi

script:
  - cd src
  - make all
```

There are many options available and using the `matrix.include` key is essential to include any specific entries. For example, this matrix would route builds to the [Trusty build environment](/user/reference/trusty/) and to a [macOS image using Xcode 7.2](/user/languages/objective-c#supported-xcode-versions):

```
matrix:
  include:
    - os: linux
      dist: trusty
    - os: osx
      osx_image: xcode7.2
```
---


  ### Setting up my own CI step by step

  - On my computer I made a diretory, made a simple function adding two numbers and a test for it. Ran pytest and it passed.
  - Used git init, added and commited the files.
  - On github made a repo with the same name as the directory (CI-practise)
  - Put my code on github using `git remote add origin the_url` then `git push -u origin master`
  - Went to https://travis-ci.org/
  - Clicked "Sign in with GitHub"
  - Redirected me to GitHub where permission was aked for Travis to have access to my stuff, clicked authorise
  - Came up with a page with a list of my repos each of which had a switch next to them, they were all off. For my CI-practise repo I turned it on.
  - On my local machine I created subtract.py which subtracts two numbers and a test for it, added and committed those files.
  - I pushed to my github but travis didn't run.
  - On my machine I created a branch called multiply_feature and added and committed a function and test to do that
  - Pushed that to github using `git push -u origin multiply_feature`
  - Switched to that branch on github and made a pull request to master
  - Continuos intergration didn't run, but there is a link just above the bit saying no merge conficts saying continuous intergration hasn't been set up and there are apps that can do it.
  - Clicked that, it took me to a github page about contuinous intergration
  - Remembered I need a .travis.yml file if travis is to run. Created one on my local machine

  ```
  language: python
  python:
  - "2.7"
  script:
  - pytest
  ```

  - Pushed to the github version of the branch. On the pull request travis automatically started running and the tests passed. Worth noting that throughout I was still able to merge.
  - Merged.
  - Switched back to master on my machine and github.
  - Made an inconsequential change, just added a print statement to the add funtion. Committed and pushed to github.
  - The change immediatly appeared in my master on github, however on travis it did run the tests and showed up green.
  - Made another branch, on it created a function and test to square numbers. Made a deliberate mistake so the tests would fail. Pushed to github.
  - The files/code I added immediatly appeared in my github version of that branch, however on travis the tests failed.
  - Made a pull request from the branch to master. The travis tests re-ran on the pull request and failed again (though i still had the option to merge if I wanted).
  - On my computer I fixed the bug, added, committed and pushed. On the pull request the tests automatically re-ran.
  - The tests passed and I merged into master.


## Limitations of CI

### Continuous integration is only as effective as you are

    Your CI is only as good as the tests you have!

    CI can also be set up to measure code coderage (see testing chapter)

    Here's an example of a yaml file to configure code coverage: https://github.com/ME-ICA/tedana/blob/master/.codecov.yml

    Here's an example output: https://github.com/ME-ICA/tedana/pull/120#issuecomment-416545219


### Security


    whereever the docs are hosted will need to know that it's used for that and you pushing ther -e, so you need a key to allow Travis to push there in example case it's an encrypted key  # Doesn't make sense?

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
## Best practise for Continuous integration,


Resource on good practice. [*source*](https://guide.esciencecenter.nl/best_practices/testing.html)


[diff between CI C deplyment and C delivery](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**

Small, Iterative Changes
One of the most important practices when adopting continuous integration is to encourage small changes. Developers should practice breaking up larger work into small pieces and committing those early. Special techniques like branch by abstraction and feature flags (see below) help to protect the functionality of the main branch from in-progress code changes.

Small changes minimize the possibility and impact of integration problems. By committing to the shared branch at the earliest possible stage and then continually throughout development, the cost of integration is diminished and unrelated work is synchronized regularly.

Trunk-Based Development
With trunk-based development, work is done in the main branch of the repository or merged back into the shared repository at frequent intervals. Short-lived feature branches are permissible as long as they represent small changes and are merged back as soon as possible.

The idea behind trunk-based development is to avoid large commits that violate of concept of small, iterative changes discussed above. Code is available to peers early so that conflicts can be resolved when their scope is small.

Releases are performed from the main branch or from a release branch created from the trunk specifically for that purpose. No development occurs on the release branches in order to maintain focus on the main branch as the single source of truth.

Keep the Building and Testing Phases Fast
Each of the processes relies on automated building and testing to validate correctness. Because the build and test steps must be performed frequently, it is essential that these processes be streamlined to minimize the time spent on these steps.

Increases in build time should be treated as a major problem because the impact is compounded by the fact that each commit kicks off a build. Because continuous processes force developers to engage with these activities daily, reducing friction in these areas is a worthwhile pursuit.

When possible, running different sections of the test suite in parallel can help move the build through the pipeline faster. Care should also be taken to make sure the proportion of each type of test makes sense. Unit tests are typically very fast and have minimal maintenance overhead. In contrast, automated system or acceptance testing is often complex and prone to breakage. To account for this, it is often a good idea to rely heavily on unit tests, conduct a fair number of integration tests, and then back off on the number of later, more complex testing.

Consistency Throughout the Deployment Pipeline
Because a continuous delivery or deployment implementations is supposed to be testing release worthiness, it is essential to maintain consistency during each step of the process—the build itself, the deployment environments, and the deployment process itself:

Code should be built once at the beginning of the pipeline: The resulting software should be stored and accessible to later processes without rebuilding. By using the exact same artifact in each phase, you can be certain that you are not introducing inconsistencies as a result of different build tools.
Deployment environments should be consistent: A configuration management system can control the various environments, and environmental changes can be put through the deployment pipeline itself to ensure correctness and consistency. Clean deployment environments should be provisioned each test cycle to prevent legacy conditions from compromising the integrity of the tests. The staging environments should match the production environment as closely as possible to reduce unknown factors present when the build is promoted.
Consistent processes should be used to deploy the build in each environment: Each deployment should be automated and each deployment should use the same centralized tools and procedures. Ad-hoc deployments should be eliminated in favor of deploying only with the pipeline tools.
Decouple Deployment and Release
Separating the deployment of code from its release to users is an extremely powerful part of continuous delivery and deployment. Code can be deployed to production without initially activating it or making it accessible to users. Then, the organization decides when to release new functionality or features independent from deployment.

This gives organizations a great deal of flexibility by separating business decisions from technical processes. If the code is already on the servers, then deployment is no longer a delicate part of the release process, which minimizes the number of individuals and the amount of work involved at the time of release.

There are a number of techniques that help teams deploy the code responsible for a feature without releasing it. Feature flags set up conditional logic to check whether to run code based on the value of an environmental variable. Branch by abstraction allows developers to replace implementations by placing an abstraction layer between resource consumers and providers. Careful planning to incorporate these techniques gives you the ability to decouple these two processes.

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

* [SSI Build and Test Examples](https://github.com/softwaresaved/build_and_test_examples) for various languages / frameworks

Travis's official tutorial is [here](ttps://docs.travis-ci.com/user/tutorial/). A tutorial focussed on using Travis with R can be found [here](https://juliasilge.com/blog/beginners-guide-to-travis/), tutorials geared towards python can be found [here](https://docs.python-guide.org/scenarios/ci/) and [here](https://docs.travis-ci.com/user/languages/python/)

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

## Acknowledgements

Thanks to David Jones of the University of Sheffield RSE group for useful discussions.
