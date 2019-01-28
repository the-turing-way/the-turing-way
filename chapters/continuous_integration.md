# Continuous integration

## Setting up my own CI step by step

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

Can use containers with CI

Dockefiles can be used with Travis

*Make this chapter about CI with travis running though it the same way the VC chapter is about version control with git running through it.*

> **Using a CI server will help with it works for me problems.**
[*source*](https://guide.esciencecenter.nl/best_practices/testing.html)

> This looks like a useful resource for a glossary/intro: https://docs.travis-ci.com/user/for-beginners/

Using CI is important to:
- Find out if there are problems early on.
- Make sure things are integrated often, changes not made in isolation.

Build, see if that works, if not need to change, if it works then run tests, see if they fail/their completeness. If so deploy the code.

An interesting discussion from [Software Engineering SE](https://softwareengineering.stackexchange.com/questions/379996/continuous-integration-for-scientific-software) on testing and CI for scientific software - might be useful when we're trying to motivate towards scientific computing types rather than professional software engineers.


### Useful uses

- Building docs after successful tests passing

### List of [Hosted continuous integration ](https://www.software.ac.uk/resources/guides/hosted-continuous-integration) services

### Circle

Links to tutorials:

* https://circleci.com/docs/2.0/project-walkthrough/

* https://howchoo.com/g/ztu1ztlimtz/getting-started-with-circleci

* https://www.upwork.com/hiring/development/continuous-integration-development-github-circleci-works-get-started/

* https://github.com/dwyl/learn-circleci (Node.js/Javascript, also covers continuous deployment, i.e. of an app)

* [Continuous Integration with Python and Circle CI.
](https://scotch.io/tutorials/continuous-integration-with-python-and-circle-ci) Looks like a good template for an example. Really small Python project, but not much detail about config files.

* [CircleCI Hello World.](https://circleci.com/docs/2.0/hello-world/) Similar level to the Python guide above, more generic but would linking to Python feel more familiar to most people?



### Travis

Links to tutorials:
* https://docs.travis-ci.com/user/tutorial/

* A BEGINNER'S GUIDE TO TRAVIS-CI FOR R:    https://juliasilge.com/blog/beginners-guide-to-travis/

* https://docs.python-guide.org/scenarios/ci/

* https://docs.travis-ci.com/user/languages/python/

* SSI [blogpost on CI](https://software.ac.uk/using-continuous-integration-build-and-test-your-software?_ga=2.231776223.1391442519.1547641475-1644026160.1541158284)

* [SSI Build and Test Examples](https://github.com/softwaresaved/build_and_test_examples) for various languages / frameworks
* [Adopting automated testing](https://github.com/softwaresaved/automated_testing/blob/master/README.md): An example of how automated testing can be adopted for software to give researchers the security to refactor, extend, optimise or tidy, their code without the overhead of having to implement dozens of unit tests at the outset.

Need to create a .travis.yml file. Minimum this needs to include is a script, if the script runs sucessfully travis will pass it. If there is anything that it will need to carry out the script beyond the linux command line you need to install it, set lenguages to run any tests, etc. If that's a lot/complex then continers etc are good, but those do kind of hide things, pros and cons. Travis doesn't know what the tests are, it only knows if errors crop up when running the script.

If you've got steps that NEED to be taken and you want fail to return if not (e.g. push online) then they need to go in the script, not an after sucesss section because travis doesn't care if things in after sucess fail.

Travis is free to public and for educational workers like github, need to pay for private.

Need to add a setting in github to get it to run travis

Can have need approving review or tests pass or both or nither before merging is alowed.

Encryption/security keys, a bit hacky, travis has instructions.

Github has easy intergration with travis + widely used so reccomended, but not the only game in town.

Travis is cloud based, makes a virtual linux machine and tries to build your project and runs tests. Can test it using multiple versions of python etc by having multiple versions of python specified under languages.

Working through the scona travis file

https://github.com/WhitakerLab/scona/blob/dev/.travis.yml

Here are a few updates:

```yaml
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

Specifying the language saves you from manually installing it/choosing a docker with it in your install section. It's a shortcut.


Q: if you have more than one language for your code, can you use travis for that?

Yes - best to start with something more simple but you can add a second language too. Do those tricky kinds of things in the script in case you need to run certain files with certain languages.

script section is where tests are run; those are just unit commands
- this uses language specific tests so you need to be aware of test conventions in the language you use

TRAVIS DOESN'T KNOW WHAT A TEST IS
-- it just runs commands and throws errors

Travis is a cloud service, you can't use it locally (Jenkins for local testing)

failures in "install" section create travis build fail errors (grey message - test didn't run)

failures in "script" creates test failure and thus red error messages

Q: What is
global:  
    secure:   
 ?  
whereever the docs are hosted will need to know that it's used for that and you pushing ther -e, so you need a key to allow Travis to push there in example case it's an encrypted key  # Doesn't make sense?

NOTE TO US: sometimes you need to understand how to handle tokens:
- [Travis CI Encryption keys](https://docs.travis-ci.com/user/encryption-keys/)

Travis is free for public and kind of integrated with GitHub - so we can promote though not open source as it is so much easier to set up than Circle

Q: How different would this be for Circle?  
A: looks fairly similar, will need more investigation/comparison of examples  
    - [Continuous Integration. CircleCI vs Travis CI vs Jenkins](https://hackernoon.com/continuous-integration-circleci-vs-travis-ci-vs-jenkins-41a1c2bd95f5)  
    - Circle will have longer runtime, so you can pass it larger datasets

As Travis files are so small, they "hide" quite a lot of the action (similar to binder, it might make it too easy) - the log gives full transparency of the "magic"  
-> chapter could map yaml file to log file action to uncover hidden layers

GitHub insists on surfacing files in a folder called docs

Travis files start with . so they might be hidden files

Q: What does touch .nojekyll mean?  
A: By default, GitHub will render files using jekyll, this just tells it to ignore that as you can't just disable that default setting

> you can have a pride banner on your Travis dashboard page *yeah*

If any of the scripts fail, the build fails.

yellow while it's running

THIS IS ONLY USEFUL AS LONG AS YOUR TESTS ARE GOOD!

You can make "test passed" a requirement for merging

Squashing reduces all changes to one commit to master - you can have it as an option but we might not enable it for the Turing Way as we want to show our "mess" transparently

after success:
* add the things there that you would like to catch but don't want to mess up getting your green tick :smile:

You can delete most sections in the yaml file but you will need the script section.

Explain why we're promoting travis and github

Travis links in very nicely to github - you can protect branches so that there's no way to merge a pull request unless the tests pass.

### Limitations of CI

Your CI is only as good as the tests you have!

Here's a nice little bot for code coverage: https://codecov.io/

pytest can also tell you about code coverage, probably similar things for most commonly used languages.

Here's an example of a yaml file to configure code coverage: https://github.com/ME-ICA/tedana/blob/master/.codecov.yml

Here's an example output: https://github.com/ME-ICA/tedana/pull/120#issuecomment-416545219

This tells you how much of your code is used when you run your test suite.

So for example, if you have a if statement and you only test things where that if statement evaluates to "True" then none of the code that comes under "False", or that would be used when the statement is false will be run. The code coverage bot will tell you that (for example) 45% of the code wasn't accessed. This doesn't include documentation. So adding more documentation doesn't affect your percentages.

A side note for this code coverage bot: you may configure it so that it tells you that your builds are failing if the coverage goes down. In the example below Ross has added

Here's an example: https://github.com/rmarkello/pyls/pull/44


### Taking CI from the software dev community to scientists

I love this blog post on what CI is and how it can be translated into an analysis framework that's more accessible for researchers.

https://elifesciences.org/labs/e623676c/reproducibility-automated

![](https://iiif.elifesciences.org/journal-cms/labs-post-content%2F2017-10%2Fimage2.png/full/925,/0/default.jpg)

### Important considerations:

#### Security

If your tests require authentication credentials, do not run tests from PRs (as PRs can include code that exposes such credentials). Comment by Noam Ross when I asked a question about this practice on one the rOpenSci packages I was editor on:
> If your test suite needs credentials, then running all tests on PRs is not great security practice; someone can create a PR that will reveal/do something nasty with your credentials. I think it is best practice to reduce the extent of tests requiring credentials with conditional statements testing for the presence of things like the encrypted environment variables, and use mocking for things like testing processing of returned values. BUT I think this is a pretty high bar to ask for. The owner can trigger a re-run with the secure variables exposed (some CIs have an option, or one can merge into a non-master branch first), as one should after checking for nasties.


Travis is a cloud service - you can’t run travis commands locally.



[diff between CI C deplyment and C delivery](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**

Introduction
Developing and releasing software can be a complicated process, especially as applications, teams, and deployment infrastructure grow in complexity themselves. Often, challenges become more pronounced as projects grow. To develop, test, and release software in a quick and consistent way, developers and organizations have created three related but distinct strategies to manage and automate these processes.

Continuous integration focuses on integrating work from individual developers into a main repository multiple times a day to catch integration bugs early and accelerate collaborative development. Continuous delivery is concerned with reducing friction in the deployment or release process, automating the steps required to deploy a build so that code can be released safely at any time. Continuous deployment takes this one step further by automatically deploying each time a code change is made.

In this guide, we will discuss each of these strategies, how they relate to one another, and how incorporating them into your application life cycle can transform your software development and release practices. To get a better idea of the differences between various open-source CI/CD projects, check out our CI/CD tool comparison.

What is Continuous Integration and Why Is It Helpful?
Continuous integration is a practice that encourages developers to integrate their code into a main branch of a shared repository early and often. Instead of building out features in isolation and integrating them at the end of a development cycle, code is integrated with the shared repository by each developer multiple times throughout the day.

The idea is to minimize the cost of integration by making it an early consideration. Developers can discover conflicts at the boundaries between new and existing code early, while conflicts are still relatively easy to reconcile. Once the conflict is resolved, work can continue with confidence that the new code honors the requirements of the existing codebase.

Integrating code frequently does not, by itself, offer any guarantees about the quality of the new code or functionality. In many organizations, integration is costly because manual processes are used to ensure that the code meets standards, does not introduce bugs, and does not break existing functionality. Frequent integration can create friction when the level of automation does not match the amount quality assurance measures in place.

To address this friction within the integration process, in practice, continuous integration relies on robust test suites and an automated system to run those tests. When a developer merges code into the main repository, automated processes kick off a build of the new code. Afterwards, test suites are run against the new build to check whether any integration problems were introduced. If either the build or the test phase fails, the team is alerted so that they can work to fix the build.

The end goal of continuous integration is to make integration a simple, repeatable process that is part of the everyday development workflow in order to reduce integration costs and respond to defects early. Working to make sure the system is robust, automated, and fast while cultivating a team culture that encourages frequent iteration and responsiveness to build issues is fundamental to the success of the strategy.

What is Continuous Delivery and Why Is It Helpful?
Continuous delivery is an extension of continuous integration. It focuses on automating the software delivery process so that teams can easily and confidently deploy their code to production at any time. By ensuring that the codebase is always in a deployable state, releasing software becomes an unremarkable event without complicated ritual. Teams can be confident that they can release whenever they need to without complex coordination or late-stage testing. As with continuous integration, continuous delivery is a practice that requires a mixture of technical and organizational improvements to be effective.

On the technology side, continuous delivery leans heavily on deployment pipelines to automate the testing and deployment processes. A deployment pipeline is an automated system that runs increasingly rigorous test suites against a build as a series of sequential stages. This picks up where continuous integration leaves off, so a reliable continuous integration setup is a prerequisite to implementing continuous delivery.

At each stage, the build either fails the tests, which alerts the team, or passes the tests, which results in automatic promotion to the next stage. As the build moves through the pipeline, later stages deploy the build to environments that mirror the production environment as closely as possible. This way the build, the deployment process, and the environment can be tested in tandem. The pipeline ends with a build that can be deployed to production at any time in a single step.

The organizational aspects of continuous delivery encourage prioritization of "deployability" as a principle concern. This has an impact on the way that features are built and hooked into the rest of the codebase. Thought must be put into the design of the code so that features can be safely deployed to production at any time, even when incomplete. A number of techniques have emerged to assist in this area.

Continuous delivery is attractive because it automates the steps between checking code into the repository and deciding on whether to release well-tested, functional builds to your production infrastructure. The steps that help assert the quality and correctness of the code are automated, but the final decision about what to release is left in the hands of the organization for maximum flexibility.

What is Continuous Deployment and Why Is It Helpful?
Continuous deployment is an extension of continuous delivery that automatically deploys each build that passes the full test cycle. Instead of waiting for a human gatekeeper to decide what and when to deploy to production, a continuous deployment system deploys everything that has successfully traversed the deployment pipeline. Keep in mind that while new code is automatically deployed, techniques exist to activate new features at a later time or for a subset of users. Deploying automatically pushes features and fixes to customers quickly, encourages smaller changes with limited scope, and helps avoid confusion over what is currently deployed to production.

This fully automated deploy cycle can be a source of anxiety for organizations worried about relinquishing control to their automation system of what gets released. The trade-off offered by automated deployments is sometimes judged to be too dangerous for the payoff they provide.

Other groups leverage the promise of automatic release as a method of ensuring that best practices are always followed and to extend the testing process into a limited production environment. Without a final manual verification before deploying a piece of code, developers must take responsibility for ensuring that their code is well-designed and that the test suites are up-to-date. This collapses the decision of what and when to commit to the main repository and what and when to release to production into a single point that exists firmly in the hands of the development team.

Continuous deployment also allows organizations to benefit from consistent early feedback. Features can immediately be made available to users and defects or unhelpful implementations can be caught early before the team devotes extensive effort in an unproductive direction. Getting fast feedback that a feature isn't helpful lets the team shift focus rather than sinking more energy into an area with minimal impact.

Key Concepts and Practices for Continuous Processes
While continuous integration, delivery, and deployment vary in the scope of their involvement, there are some concepts and practices that are fundamental to the success of each.

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

---
[CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**

Martin Fowler, who first wrote about Continuous Integration (short: CI) together with Kent Beck, describes CI as follows:

Continuous Integration is a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily - leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop cohesive software more rapidly.

Travis-CI is a distributed CI server which builds tests for open source projects for free. It provides multiple workers to run Python tests on and seamlessly integrates with GitHub. You can even have it comment on your Pull Requests whether this particular changeset breaks the build or not. So if you are hosting your code on GitHub, Travis-CI is a great and easy way to get started with Continuous Integration.

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

In order to activate testing for your project, go to the Travis-CI site and login with your GitHub account. Then activate your project in your profile settings and you’re ready to go. From now on, your project’s tests will be run on every push to GitHub.

---

## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful
> why we think you should read the whole thing

## Prerequisites / recommended skill level
An understanding of version control is necessary for this chapter (see the version control chapter for details). It is also highly recommended that you read the chapters on testing and reproducible environments prior to reading this chapter.  



## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography
> Credit/urls for any materials that form part of the chapter's text.

## Acknowledgements

Thanks to David Jones for useful discussions.
