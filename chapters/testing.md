# Testing

## Structure

- Why you should write tests
  - For yourself
    - Saves you having to redo lots of work when you realise there's a bug, catch things early.
    - Forces you to write more modular, clean code. Improves your code quality. Much quicker and easier to work with than a tangled rats nest.
    - You have to test your code anyway as you're writing it, you don't just write it and assume it's right. It's very little work to put those tests in a file. The time lost to incorrect results or broken code is much, much bigger.
  - For science
    - Fewer mistakes, very costly for time and funding, include a horror story or two.
    - More reproducible. Answers the question "how do we even know this code works". If tests are never saved, just done and deleted the proof cannot be reproduced easily.
    - SSI slogan: "better software, better research".
- Types of tests
  - Unit tests
    - Test small "units" of code
  - Integration tests
    - Check the pieces work together properly.
  - End to end tests
    - Doesn't need to include every single feature.
  - Regression tests
    - Test if the result changes after the code is updated. Fail if so.
    - A unit test can also be a regression test (can integration and end to end tests etc *also* be considered regression tests?)
  - Runtime tests
  - Tests where there is not a well defined output
    - E.g. look and see if a graph seems reasonable.
    - Can't test all the ways it may be wrong, but can do sanity checks, e.g. if you have a graph of global population vs you should never have a negative number of people.
- Test driven development (ensure we do the thing right)
- Behaviour driven development (ensure we do the right thing)
- General best practice
  - Write small things
  - Defensive programming (e.g. test inputs are the right type, not applicable in static type languages)
  - Code review to test code quality
  - Continuous integration very briefly, and link to that chapter,


## material from the hack.md

- https://github.com/alan-turing-institute/ReproducibleResearchResources/blob/master/resources/testing.md
- https://alan-turing-institute.github.io/rsd-engineeringcourse/ch03tests/
- Seven Testing Principles: https://www.utest.com/articles/seven-testing-principles
- eScience center section of Testing & CI
- SSI blogpost on Testing: Software development doesn’t end when the software is written. How can you, and any developers you work with, be sure that your software meets its requirements? Does your software work as expected, and will it continue to work over its lifetime?


Jenkins is a good tool for running tests locally.

https://jenkins.io



Ask folks what they CURRENTLY do to check that their work is right.

- Make a plot and visually inspect it

- Describe a dataframe and check that the means and standard deviations are within the right range

- Run a few different random simulations and check that they all give back values that are in the right range

Give them some examples of code tests that do exactly these steps!

(Note that its difficult to do this for images)


There are some really standard unit tests that I (Kirstie) personally find a bit unhelpful to get started with. For example checking that the values returned are floats rather than integers or strings etc is not a thing that I’m usually super worried about!

But checking the length of lists is a good one, or making sure that before I merge two data frames they DO actually have the heading in common?

I think the most important thing in this section is to make sure its clear why testing is the SELFISH option, not the goodie two shoes option!! It helps YOU check that your work actually works.

To be honest, the unit tests are cute but I don’t think they’re the best places to start - in the real world the way that I test my code is to actually see if it runs without errors all the way to the end! I think getting people up and running with this end-to-end kinda “test” might be the easiest way to get over the activation energy of learning something new



[smoke testing](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**

## Smoke testing

Smoke tests are a special kind of initial checks designed to ensure very basic functionality as well as some basic implementation and environmental assumptions. Smoke tests are generally run at the very start of each testing cycle as a sanity check before running a more complete test suite.

The idea behind this type of test is to help to catch big red flags in an implementation and to bring attention to problems that might indicate that further testing is either not possible or not worthwhile. Smoke tests are not very extensive, but should be extremely quick. If a change fails a smoke test, its an early signal that core assertions were broken and that you should not devote any more time to testing until the problem is resolved.

Context-specific smoke tests can be employed at the start of any new phase testing to assert that the basic assumptions and requirements are met. For instance, smoke tests can be used both prior to integration testing or deploying to staging servers, but the conditions to be tested will vary in each case.

*As an example maybe if it's failed to read in the data not much point testing the rest of the code*

## Unit Testing
Unit tests are responsible for testing individual elements of code in an isolated and highly targeted way. The functionality of individual functions and classes are tested on their own. Any external dependencies are replaced with stub or mock implementations to focus the test completely on the code in question.

Unit tests are essential to test the correctness of individual code components for internal consistency and correctness before they are placed in more complex contexts. The limited extent of the tests and the removal of dependencies makes it easier to hunt down the cause of any defects. It also is the best time to test a variety of inputs and code branches that might be difficult to hit later on. Often, after any smoke tests, unit tests are the first tests that are run when any changes are made.

Unit tests are typically run by individual developers on their own work station prior to submitting changes. However, continuous integration servers almost always run these tests again as a safe guard before beginning integration tests.

## Integration Testing

After unit tests, integration testing is performed by grouping together components and testing them as an assembly. While unit tests validate the functionality of code in isolation, integration tests ensure that components cooperate when interfacing with one another. This type of testing has the opportunity to catch an entirely different class of bugs that are exposed through interaction between components.

Typically, integration tests are performed automatically when code is checked into a shared repository. A continuous integration server checks out the code, performs any necessary build steps (usually performing a quick smoke test to make sure the build was successful) and then runs unit and integration tests. Modules are hooked together in different combinations and tested.

Integration tests are important for shared work because they protect the health of the project. Changes must prove that they do not break existing functionality and that they interact with other code as expected. A secondary aim of integration testing is to verify that the changes can be deployed into a clean environment. This is frequently the first testing cycle that is performed off of the developer's own machines, so unknown software and environmental dependencies can also be discovered during this process. This is usually also the first time that new code is tested against real external libraries, services, and data.

## System Testing
Once integration tests are performed, another level of testing called system testing can begin. In many ways, system testing acts as an extension to integration testing. The focus of system tests are to make sure that groups of components function correctly as a cohesive whole.

Instead of focusing on the interfaces between components, system tests typically evaluate the outward functionality of a full piece of software. This set of tests ignores the constituent parts in order to gauge the composed software as a unified entity. Because of this distinction, system tests usually focus on user- or externally-accessible interfaces.

## Acceptance Testing

Acceptance tests are one of the last tests types that are performed on software prior to delivery. Acceptance testing is used to determine whether a piece of software satisfies all of the requirements from the business or user's perspective. These tests are sometimes built against the original specification and often test interfaces for the expected functionality and for usability.

Acceptance testing is often a more involved phase that might extend past the release of the software. Automated acceptance testing can be used to make sure the technological requirements of the design were met, but manual verification also usually plays a role.

Frequently, acceptance testing begins by deploying the build to a staging environment that mirrors the production system. From here, the automated test suites can be run and internal users can access the system to check whether it functions the way they need it to. After release or offering beta access to customers, further acceptance testing is performed by evaluating how the software functions with real use and by collecting feedback from users.

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
