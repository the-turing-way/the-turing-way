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


As a continuous integration platform, Travis CI supports your development process by automatically building and testing code changes, providing immediate feedback on the success of the change. Travis CI can also automate other parts of your development process by managing deployments and notifications.  

- Green, amber, red
  - failures in "install" section create travis build fail errors (grey message - test didn't run)
  - failures in "script" creates test failure and thus red error messages
  - yellow while it's running

    - *You can make "test passed" a requirement for merging *
      - *you can protect branches so that there's no way to merge a pull request unless the tests pass.*
  - *How to link github repo and travis*



  [Info about how travis works](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/for-beginners.md) **MIT**


  ## CI builds and automation: building, testing, deploying

  When you run a build, Travis CI clones your GitHub repository into a brand new virtual environment, and carries out a series of tasks to build and test your code. If one or more of those tasks fails, the build is considered broken. If none of the tasks fail, the build is  considered passed, and Travis CI can deploy your code to a web server, or application host.

  CI builds can also automate other parts of your delivery workflow. This means you can setup [notifications](/user/notifications/) and many other tasks.

  ## Builds, Jobs, Stages and Phases

  In the Travis CI documentation, some common words have specific meanings:

  * Job - an automated process that clones your repository into a virtual environment and then carries out a series of phases such as compiling your code, running tests, etc. A job fails if the return code of the `script` encounters an error.
  * Build - a group of jobs. For example, a build might have two *jobs*, each of which tests a project with a different version of a programming language. A build finishes when all of its jobs are finished.

  ## Breaking the Build

  The build is considered broken when one or more of its jobs completes with a
  state that is not passed:

   * *errored* - a command in the `before_install`, `install`, or `before_script`
     phase returned a non-zero exit code. The job stops immediately.
   * *failed* - a command in the `script` phase returned a non-zero exit code. The
     job continues to run until it completes.
   * *canceled* - a user cancels the job before it completes.

  Our [Common Builds Problems](/user/common-build-problems/) page is a good place
  to start troubleshooting why your build is broken.

  ## Infrastructure and environment notes

  Travis CI offers a few different infrastructure environments, so you can select
  the setup that suits your project best:

  * *Ubuntu Linux* - these Linux Ubuntu environments run inside full virtual machines, provide plenty of computational resources, and support the use of `sudo`, `setuid`, and `setgid`.
  * *macOS* - uses one of several versions of the macOS operating system. This environment is useful for building projects that require the macOS software, such as projects written in Swift. It is not a requirement to use the macOS environment if you develop on a macOS machine.

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


## Setting up continuous integration with Travis

  [light travis tutorial](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/tutorial.md) **MIT**


  This is a very short guide to using Travis CI with your GitHub hosted code repository.
  If you're new to continuous integration or would like some more information on
  what Travis CI does, start with [Core Concepts for Beginners](/user/for-beginners)
  instead.


---

## To get started with Travis CI

1. Go to [Travis-ci.com](https://travis-ci.com) and [*Sign up with GitHub*](https://travis-ci.com/signin).

2. Accept the Authorization of Travis CI. You'll be redirected to GitHub.

3. Click the green *Activate* button, and select the repositories you want to use with Travis CI.

4. Add a `.travis.yml` file to your repository to tell Travis CI what to do.

   The following example specifies a Ruby project that should
   be built with Ruby 2.2 and the latest versions of JRuby.

   ```yaml
   language: ruby
   rvm:
    - 2.2
    - jruby
   ```
   {: data-file=".travis.yml"}

   The defaults for Ruby projects are `bundle install` to [install dependencies](/user/job-lifecycle/#customizing-the-installation-phase),
   and `rake` to build the project.

5. Add the `.travis.yml` file to git, commit and push, to trigger a Travis CI build:

   > Travis only runs builds on the commits you push *after* you've added a `.travis.yml` file.

6. Check the build status page to see if your build [passes or fails](/user/job-lifecycle/#breaking-the-build), according to the return status of the build command by visiting the [Travis CI](https://travis-ci.com/auth) and selecting your repository.


---
[CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**

In order to activate testing for your project, go to the Travis-CI site and login with your GitHub account. Then activate your project in your profile settings and you’re ready to go. From now on, your project’s tests will be run on every push to GitHub.

---

- .travis.yml
  - Outline minimum basic structure


Need to create a .travis.yml file. Minimum this needs to include is a script, if the script runs sucessfully travis will pass it. If there is anything that it will need to carry out the script beyond the linux command line you need to install it, set lenguages to run any tests, etc. If that's a lot/complex then continers etc are good, but those do kind of hide things, pros and cons.

As Travis files are so small, they "hide" quite a lot of the action (similar to binder, it might make it too easy) - the log gives full transparency of the "magic"  

Travis files start with . so they might be hidden files

## Setting up the computational environment

[CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**

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

- Dockefiles can be used with Travis

Can test it using multiple versions of python etc by having multiple versions of python specified under languages.

Specifying the language saves you from manually installing it/choosing a docker with it in your install section. It's a shortcut.

Q: if you have more than one language for your code, can you use travis for that?

Yes - best to start with something more simple but you can add a second language too. Do those tricky kinds of things in the script in case you need to run certain files with certain languages.

## Selecting a different programming language

Use one of these common languages:

```yaml
language: ruby
```
{: data-file=".travis.yml"}

```yaml
language: java
```
{: data-file=".travis.yml"}

```yaml
language: node_js
```
{: data-file=".travis.yml"}

```yaml
language: python
```
{: data-file=".travis.yml"}

```yaml
language: php
```
{: data-file=".travis.yml"}

If you have tests that need to run on macOS, or your project uses Swift or
Objective-C, use our macOS environment:

```yaml
os: osx
```
{: data-file=".travis.yml"}

> You do *not* necessarily need to use macOS if you develop on a Mac.
> macOS is required only if you need Swift, Objective-C or other
> macOS-specific software.

Travis CI supports many [programming languages](/user/languages/).

---

[Installing dependencies via yaml](https://github.com/travis-ci/docs-travis-ci-com/edit/master/user/installing-dependencies.md) **MIT**

## Installing Packages on Standard Infrastructure

To install Ubuntu packages that are not included in the standard [precise](/user/reference/precise/), [trusty](/user/reference/trusty/), or [xenial](/user/reference/xenial/) distribution, use apt-get in the `before_install` step of your `.travis.yml`:

```yaml
before_install:
  - sudo apt-get install -y libxml2-dev
```
{: data-file=".travis.yml"}

---

[travis multiple operating systems](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/multi-os.md) **MIT**

If your code is used on multiple operating systems it probably should be tested on
multiple operating systems. Travis CI can test on Linux and macOS.

To enable testing on multiple operating systems add the `os` key to your `.travis.yml`:

```yaml
os:
  - linux
  - osx
```
{: data-file=".travis.yml"}

The value of the `$TRAVIS_OS_NAME` variable is set to `linux` or `osx` according to the operating system a particular build is running on, so you can use it to conditionalize your build scripts.

If you are already using a [build matrix](/user/customizing-the-build/#build-matrix) to test multiple versions, the `os` key also multiplies the matrix.

## Operating System differences

When you test your code on multiple operating systems, be aware of differences
that can affect your tests:

- Not all tools may be available on macOS.

  We are still working on building up the toolchain on the [macOS Environment](/user/reference/osx/).
  Missing software may be available via Homebrew.

- Language availability.

  Not all languages are available on all operating systems, and different versions maybe installed on different systems.
  Before you embark on the multi-os testing journey, be sure to check
  this GitHub issue [detailing what languages are available](https://github.com/travis-ci/travis-ci/issues/2320).

- The file system behaviour is different.

  The HFS+ file system on our macOS workers is case-insensitive (which is the default for macOS),
  and the files in a directory are returned sorted.
  On Linux, the file system is case-sensitive, and returns directory entries in
  the order they appear in the directory internally.

   Your tests may implicitly rely on these behaviors, and could fail because of them.

- They are different operating systems, after all.

  Commands may have the same name on the Mac and Linux, but they may have different flags,
  or the same flag may mean different things.
  In some cases, commands that do the same thing could have different names.
  These need to be investigated case by case.

## Allowing Failures on Jobs Running on One Operating System

To ignore the results of jobs on one operating system, add the following
to your `.travis.yml`:

```yaml
matrix:
  allow_failures:
    - os: osx
```
{: data-file=".travis.yml"}

## Example Multi OS Build Matrix

Here's an example `.travis.yml` file using if/then directives to customize the [build lifecycle](/user/job-lifecycle/) to use [Graphviz](https://graphviz.gitlab.io/) in both Linux and macOS.

```yaml
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
{: data-file=".travis.yml"}

There are many options available and using the `matrix.include` key is essential to include any specific entries. For example, this matrix would route builds to the [Trusty build environment](/user/reference/trusty/) and to a [macOS image using Xcode 7.2](/user/languages/objective-c#supported-xcode-versions):

```yaml
matrix:
  include:
    - os: linux
      dist: trusty
    - os: osx
      osx_image: xcode7.2
```
{: data-file=".travis.yml"}

### Python example (unsupported languages)

For example, this `.travis.yml` uses the `matrix.include` key to include four specific entries in the build matrix. It also takes advantage of `language: generic` to test Python on macOS. Custom requirements are installed in `./.travis/install.sh` below.

```yaml
language: python

matrix:
    include:
        - os: linux
          python: 3.2
          env: TOXENV=py32
        - os: linux
          python: 3.3
          env: TOXENV=py33
        - os: osx
          language: generic
          env: TOXENV=py32
        - os: osx
          language: generic
          env: TOXENV=py33
install:
    - ./.travis/install.sh
script: make test
```
{: data-file=".travis.yml"}


---

## The .travis.yml script

    - Acceptable errors (optional)
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



## Limitations of CI

### Continuous integration is only as effective as you are

    Your CI is only as good as the tests you have!

    Here's a nice little bot for code coverage: https://codecov.io/

    pytest can also tell you about code coverage, probably similar things for most commonly used languages.

    Here's an example of a yaml file to configure code coverage: https://github.com/ME-ICA/tedana/blob/master/.codecov.yml

    Here's an example output: https://github.com/ME-ICA/tedana/pull/120#issuecomment-416545219

    This tells you how much of your code is used when you run your test suite.

    So for example, if you have a if statement and you only test things where that if statement evaluates to "True" then none of the code that comes under "False", or that would be used when the statement is false will be run. The code coverage bot will tell you that (for example) 45% of the code wasn't accessed. This doesn't include documentation. So adding more documentation doesn't affect your percentages.

    A side note for this code coverage bot: you may configure it so that it tells you that your builds are failing if the coverage goes down. In the example below Ross has added

    Here's an example: https://github.com/rmarkello/pyls/pull/44

### Security

    - *Encryption/security keys, a bit hacky, travis has instructions.*

    Q: What is
    global:  
        secure:   
     ?  
    whereever the docs are hosted will need to know that it's used for that and you pushing ther -e, so you need a key to allow Travis to push there in example case it's an encrypted key  # Doesn't make sense?

    NOTE TO US: sometimes you need to understand how to handle tokens:
    - [Travis CI Encryption keys](https://docs.travis-ci.com/user/encryption-keys/)


    If your tests require authentication credentials, do not run tests from PRs (as PRs can include code that exposes such credentials). Comment by Noam Ross when I asked a question about this practice on one the rOpenSci packages I was editor on:
    > If your test suite needs credentials, then running all tests on PRs is not great security practice; someone can create a PR that will reveal/do something nasty with your credentials. I think it is best practice to reduce the extent of tests requiring credentials with conditional statements testing for the presence of things like the encrypted environment variables, and use mocking for things like testing processing of returned values. BUT I think this is a pretty high bar to ask for. The owner can trigger a re-run with the secure variables exposed (some CIs have an option, or one can merge into a non-master branch first), as one should after checking for nasties.


    [security](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/best-practices-security.md) **MIT**

    ## Steps Travis CI takes to secure your data
    Travis CI obfuscates secure environment variables and tokens displayed in the UI. Our [documentation about encryption keys](/user/encryption-keys/) outlines the build configuration we require to ensure this, however, once a VM is booted and tests are running, we have less control over what information utilities or add-ons are able to print to the VM’s standard output.

    To prevent leaks made by these components, we automatically filter secure environment variables and tokens that are longer than three characters at runtime, effectively removing them from the build log, displaying the string `[secure]` instead.

    Please make sure your secret is never related to the repository or branch name, or any other guessable string. Ideally use a password generation tool such as `mkpasswd` instead of choosing a secret yourself.

    ## Recommendations on how to avoid leaking secrets to build logs
    Despite our best efforts, there are however many ways in which secure information can accidentally be exposed. These vary according to what tools you are using and what settings you have enabled. Some things to look out for are:

    * settings which duplicate commands to standard output, such as `set -x` or `set -v` in your bash scripts
    * displaying environment variables, by running `env` or `printenv`
    * printing secrets within the code, for example `echo "$SECRET_KEY"`
    * using tools that print secrets on error output, such as `php -i`
    * git commands like `git fetch` or `git push` may expose tokens or other secure environment variables
    * mistakes in string escaping
    * settings which increase command verbosity
    * testing tools or plugins that may expose secrets while operating

    Preventing commands from displaying any output is one way to avoid accidentally displaying any secure information. If there is a particular command that is using secure information you can redirect its output to `/dev/null` to make sure it does not accidentally publish anything, as shown in the following example:

    ```
    sh
    git push url-with-secret >/dev/null 2>&1
    ```

    ## If you think that you might have exposed secure information

    As an initial step, it’s possible to delete logs containing any secure information by clicking the *Remove log* button on the build log page of Travis CI.

    If you discover a leak in one of your build logs it’s essential that you revoke the leaked token or environment variable, and update any build scripts or commands that caused the leak.

    ### Alternative methods of deleting logs

    Instead of deleting build logs manually, you can do so using the [Travis CI CLI](https://github.com/travis-ci/travis.rb#logs) or the  [API](https://developer.travis-ci.com/resource/log#delete).

    > Note that if you're still using [travis-ci.org](http://www.travis-ci.org) you need to use the [open source API](https://developer.travis-ci.org/resource/log#delete) instead.

    ## Rotate tokens and secrets periodically
    Rotate your tokens and secrets regularly. GitHub OAuth tokens can be found in your [Developer Settings](https://github.com/settings/developers) on the GitHub site. Please regularly rotate credentials for other third-party services as well.


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
*This looks like a useful resource for a glossary/intro: https://docs.travis-ci.com/user/for-beginners/*

## Bibliography

### Materials used: What is continuous integration?

- [What is CI](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/for-beginners.md) **MIT**
- [SSI blog](https://software.ac.uk/using-continuous-integration-build-and-test-your-software?_ga=2.231776223.1391442519.1547641475-1644026160.1541158284)
- [The difference between continuous integration, continuous deployment, and continuous delivery](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
- [Martin Fowler, who first wrote about Continuous Integration (short: CI) together with Kent Beck via CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**

## Acknowledgements

Thanks to David Jones of the University of Sheffield RSE group for useful discussions.
