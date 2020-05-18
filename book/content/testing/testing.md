# Testing

| Prerequisite | Importance |
| -------------|------------|
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Necessary |

## Table of contents

1. [Summary](#Summary)
2. [How this will help you/ why this is useful](#How_this_will_help_you_why_this_is_useful)
    1. [The advantages of testing for research](#The_advantages_of_testing_for_research)
3. [General guidance and good practice for testing](/testing/01/testing-guidance#General_guidance_and_good_practice_for_testing)
    1. [Write tests. Any tests.](/testing/01/testing-guidance#Write_tests_any_tests)
    2. [Run the tests](#Run_the_tests)
    3. [Consider how long it takes your tests to run](#Consider_how_long_it_takes_your_tests_to_run)
    4. [Document the tests and how to run them](#Document_the_tests_and_how_to_run_them)
    5. [Test realistic cases](#Test_realistic_cases)
    6. [Use a testing framework](#Use_a_testing_framework)
    7. [Aim to have a good code coverage](#Aim_to_have_a_good_code_coverage)
    8. [Use test doubles/mocking where appropriate](#Use_test_doubles_stubs_mocking_where_appropriate)
4. [Types of tests](/testing/02/testing-types#Types_of_tests)
    1. [Overview of Testing](/testing/02/testing-types#Overview_of_testing)
    2. [Smoke testing](/testing/02/testing-types#Smoke_testing)
    3. [Unit tests](/testing/02/testing-types#Unit_tests)
        1. [Benefits of unit testing](/testing/02/testing-types#Benefits_of_unit_testing)
        2. [Unit testing tips](/testing/02/testing-types#Unit_testing_tips)
    4. [Integration testing](/testing/02/testing-types#Integration_testing)
        1. [Approaches](/testing/02/testing-types#Approaches)
        2. [Integration testing tips](/testing/02/testing-types#Integration_testing_tips)
    5. [System tests](/testing/02/testing-types#System_tests)
        1. [System testing tips](/testing/02/testing-types#System_testing_tips)
    6. [Acceptance testing](/testing/02/testing-types#Acceptance_testing)
    7. [Regression testing](/testing/02/testing-types#Regression_testing)
        1. [Limitations](/testing/02/testing-types#Limitations)
    8. [Runtime testing](#Runtime_testing)
    9. [Test driven development](#Test_driven_development)
5. [Testing Challenging or Exceptional Cases](/testing/03/testing-exception#Testing_challenging_or_exceptional_cases)
    1. [Testing stochastic code](/testing/03/testing-exception#Testing_stochastic_code)
        1. [Use random number seeds](/testing/03/testing-exception#Use_random_number_seeds)
        2. [Measure the distribution of results](/testing/03/testing-exception#Measure_the_distribution_of_results)
    2. [Tests that are difficult to quantify](/testing/03/testing-exception#Tests_that_are_difficult_to_quantify)
    3. [Testing if non-integer numbers are equal](/testing/03/testing-exception#Testing_if_non_integer_numbers_are_equal)
        1. [When 0.1 + 0.2 does not equal 0.3](/testing/03/testing-exception#When_point_1_plus_point_2_does_not_equal_point_3)
        2. [Equality in a floating point world](/testing/03/testing-exception#Equality_in_a_floating_point_world)
5. [Checklist](/testing/04/testing-checklist#Checklist)
    1. [Writing tests](/testing/04/testing-checklist#Writing_tests)
    2. [Good practice checks](/testing/04/testing-checklist#Good_practice_checks)
6. [Resources](/testing/05/testing-resources#Resources)
    1. [What to learn next](/testing/05/testing-resources#What_to_learn_next)
    2. [Further reading](/testing/05/testing-resources#Further_reading)
    3. [Definitions/glossary](/testing/05/testing-resources#Definitions_glossary)
    4. [Bibliography](/testing/05/testing-resources#Bibliography)

<a name="Summary"></a>
## Summary

Researcher-written code now forms a part of a huge portion of the research, and if there are mistakes in the code the results may be partly or entirely unreliable. Testing code thoroughly and frequently is vital to ensure reliable, reproducible research. This chapter will cover general guidelines for writing tests and describes several different kinds of testing, their uses, and how to go about implementing them.

<a name="How_this_will_help_you_why_this_is_useful"></a>
## How this will help you/ why this is useful

Here's a couple of examples of why should write tests:

![testing_motivation_1](../figures/testing_motivation_1.png)

![testing_motivation_2](../figures/testing_motivation_2.png)

It is very, very easy to make mistakes when coding. A single misplaced character can cause a program's output to be entirely wrong. One of the examples above was caused by a plus sign which should have been a minus. Another was caused by one piece of code working in meters while a piece of code written by another researcher worked in feet. *Everyone* makes mistakes, and in research, the results can be catastrophic. Careers can be damaged/ended, vast sums of research funds can be wasted, and valuable time may be lost to exploring incorrect avenues. This is why tests are vital.

Even if problems in a program are caught before the research is published it can be difficult to figure out what results are contaminated and must be re-done. This represents a huge loss of time and effort. Catching these problems as early as possible minimises the amount of work it takes to fix them, and for most researchers, time is by far their most scarce resource. You should not skip writing tests because you are short on time, you should write tests *because* you are short on time. Researchers cannot afford to have months or years of work go down the drain, and they can't afford to repeatedly manually check every little detail of a program that might be hundreds or hundreds of thousands of lines long. Writing tests to do it for you is the time-saving option, and it's a safe option.

As researchers write code they generally do some tests as they go along, often by adding in print statements and checking the output. However, these tests are often thrown away as soon as they pass and are no longer present to check what they were intended to check. It is comparatively very little work to place these tests in functions and keep them so they can be run at any time in the future. The additional labour is minimal, the time saved and safeguards provided are invaluable. Further, by formalising the testing process into a suite of tests that can be run independently and automatically, you provide a much greater degree of confidence that the software behaves correctly and increase the likelihood that defects will be found.

Testing also affords researchers much more peace of mind when working on/improving a project. After changing their code a researcher will want to check that their changes or fixes have not broken anything. Providing researchers with a fail-fast environment allows the rapid identification of failures introduced by changes to the code. The alternative, of the researcher writing and running whatever small tests they have time for, is far inferior to a good testing suite which can thoroughly check the code.

Another benefit of writing tests is that it typically forces a researcher to write cleaner, more modular code as such code is far easier to write tests for, leading to an improvement in code quality. [Good quality code](../code_quality/code_quality) is far easier (and altogether more pleasant) to work with than tangled rat's nests of code I'm sure we've all come across (and, let's be honest, written). This point is expanded upon in the section on [unit tests](#Unit_tests).

<a name="The_advantages_of_testing_for_research"></a>
### The advantages of testing for research

As well as advantaging individual researchers testing also benefits research as a whole. It makes research more reproducible by answering the question "how do we even know this code works". If tests are never saved, just done and deleted the proof cannot be reproduced easily.

Testing also helps prevent valuable grant money being spent on projects that may be partly or wholly flawed due to mistakes in the code. Worse if mistakes are not at found and the work is published any subsequent work that builds upon the project will be similarly flawed.

Perhaps the clearest expression of why testing is important for research as a whole can be found in the [Software Sustainability Institute](https://www.software.ac.uk/) slogan: better software better research.