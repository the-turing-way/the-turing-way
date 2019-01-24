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
