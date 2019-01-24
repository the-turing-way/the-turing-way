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

Dockefiles can indeed be used with Travis

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



## From the hack.md

Travis is a cloud service - you can’t run travis commands locally.


## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful
> why we think you should read the whole thing

## Prerequisites / recommended skill level
> other chapters that should have been read before or content you should be familiar with before you read this

## Chapter content
> depending on the content, this might be more structured, e.g. with exercises, gotcha sections etc

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
