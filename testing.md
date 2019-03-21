# Testing

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| Experience with the command line | Necessary |  |


## Summary


## How this will help you/ why this is useful

### The advantages of testing for the researcher

- Why you should write tests
  - For yourself
    - Saves you having to redo lots of work when you realise there's a bug, catch things early.
    - Forces you to write more modular, clean code. Improves your code quality. Much quicker and easier to work with than a tangled rats nest.
    - You have to test your code anyway as you're writing it, you don't just write it and assume it's right. It's very little work to put those tests in a file. The time lost to incorrect results or broken code is much, much bigger.


[turing testing course](https://alan-turing-institute.github.io/rsd-engineeringcourse/ch03tests/01testingbasics.html) **Creative Commons share and remix**
- runnable specification best way to let others know what a function should do and not do

A few reasons to do testing
- lazyness testing saves time
- peace of mind tests (should) ensure code is correct
- reproducible debugging debugging that happened and is saved for later reuse
- code structure / modularity since the code is designed for at least two situations
- easier to modify since results can be tested

*blog to look at https://www.software.ac.uk/resources/guides/testing-your-software?_ga=2.39233514.830272891.1552653652-1336468516.1531506806*

Software development doesn't end when the software is written. How can you, and any developers you work with, be sure that your software meets its requirements? Does your software work as expected and will it continue to work over its lifetime?

Researchers do do informal testing. By formalising the testing process into a set of tests that can be run independently and automatically, you provide a much greater degree of confidence that the software behaves correctly and increase the likelihood that defects are found

After changing your code and rebuilding it, a developer will want to check that their changes or fixes have not broken anything. Providing developers with a fail-fast environment allows the rapid identification of failures introduced by changes to the code.

### The advantages of testing for science

- For science
  - Fewer mistakes, very costly for time and funding, include a horror story or two.
  - More reproducible. Answers the question "how do we even know this code works". If tests are never saved, just done and deleted the proof cannot be reproduced easily.
  - SSI slogan: "better software, better research".

  [turing testing course](https://alan-turing-institute.github.io/rsd-engineeringcourse/ch03tests/01testingbasics.html) **Creative Commons share and remix**
  - runnable specification best way to let others know what a function should do and not do

## General guidance and good practice for testing

There are a number of [different kinds](#Types_of_tests) of testing which have best practice specific to them, however there are some general guidance that applies to all of them, which will be outlined here.

<a name="Write_tests_any_tests"></a>
### Write tests. Any tests.

Starting the process of writing tests can be overwhelming, especially if you have a large code base. Further to that, as mentioned, there are many kinds of tests, and implementing all of them can seem like an impossible mountain to climb. That is why the single most important piece of guidance in this chapter is as follows: **write some tests**. Testing one tiny thing in a code that's thousands of lines long is infinitely better than testing no things in a code that's thousands of lines long. You may not be able to do everything, but doing *something* is better than nothing.

Do not be discouraged. Make improvements where you can, and do your best to include tests with new code you write even if it's not feasable to write tests that are already written.

### Run the tests

the second most important piece of advice in this chapter. Run the tests. Having a beautiful, perfect test site is no use if you rarely run it. Leaving long gaps between test runs makes it more difficult to track down what has gone wrong when a test fails because a great deal in the code will have changed. Also if it's been weeks or months since tests have been run and they fail it is difficult or impossible to know what work/results that have been done in the intervening time are still valid, and which have to be thrown away as they could have been impacted by the bug.

As such it is best to automate your testing as far as possible. If each test needs to be run individually then that boring painstaking process is likely to get neglected. Automate this using a testing tool ([discussed later](#Use_a_testing_framework)). Ideally set your tests up to run at regular intervals, possibly each night. [Jenkins](https://jenkins.io) is a good tool for this.

Consider setting up continuous integration (discussed in the continuous integration chapter) on your project. This will automatically run your tests each time you make a change to your code and, depending on the continuous integration software you use, will notify you if any of the tests fail.

### Consider how long it takes your tests to run

Some tests, like [unit tests](#Unit_tests) only test a small piece of code and so typically very fast. However [system tests](#System_tests) test the entire code from end to end, and so may take a long time to run depending on the code. As such it can be obstructive to run the entire test suite after each little bit of work. In that case it is better to run lighter weight tests such as unit tests frequently, and longer tests only once per day overnight.  

### Document the tests and how to run them

*blog to look at https://www.software.ac.uk/resources/guides/testing-your-software?_ga=2.39233514.830272891.1552653652-1336468516.1531506806*

  It is important to provide documentation that describes how to run the tests, both for yourself in case you come back to a project in the future, and for anyone else that may wish to build upon or peproduce your work. This documentation should also cover subjects such as
  
- Any resources e.g. test dataset files that are required
- Any configuration/settings adjustments needed to run the tests
- What software (such as [testing frameworks](#Use_a_testing_framework)) need to be installed 
  
Ideally, you would provide scripts to set up and configure any resources that are needed.

### Test realistic cases

Make the cases you test as realistic as possible. If for example, you have dummy data to run tests on then make that data as similar as possible to your actual data. If your actual data is messy with a lot of null values, so should your test dataset be.

<a name="Use_a_testing_framework"></a>
### Use a testing framework

There are tools available to make writing and running tests easier, these are known as testing frameworks. Find one you like, learn about the features it offers, and make use of them. Common testing frameworks (and the languages they apply to) include:

-Language agnostic
  - CTest
    - Test runner for executables, bash scripts, etc...
    - Great for legacy code hardening
- C++ 
  - Catch 
  - CppTest
  - Boost::Test
  - google-test      
- C
  - all C++ frameworks
  - Check
  - CUnit
- Python
  - pytest, branched off of nose (recommended)
  - nose includes test discovery, coverage, etc
  - unittest comes with standard python library
- R unit-tests
  - RUnit
  - svUnit (works with SciViews GUI)
- Fortran unit-tests:
  - funit
  - pfunit(works with MPI)

### Aim to have a good code coverage

As [mentioned](#Write_tests_any_tests) any tests are an improvement over no tests.

  - *Aim to have a good code coverage. Something's better than nothing*
  - *Defensive programming (e.g. test inputs are the right type, not applicable in static type languages, sanity checks.)*
  - *Use mocking where appropriate*
  - *if an element of randomness use random number seed or similar*
  - *Can at least do sanity checks on tests that are whether something "looks right"*
  - *Code review to test code quality*
  - *careful of equalities*





      ---
    Hack md notes:

    Code coverage is a measure of how much of your code is "covered" by tests. Most programming languages have tools either build into them or that can be imported to automatically measure code coverage, and there's also a nice little [bot](https://codecov.io/) available too.

    Testing framework tools such as pytest can also tell you about code coverage, probably similar things for most commonly used languages.
    This tells you how much of your code is used when you run your test suite.

    So for example, if you have a if statement and you only test things where that if statement evaluates to "True" then none of the code that comes under "False", or that would be used when the statement is false will be run. The code coverage bot will tell you that (for example) 45% of the code wasn't accessed. This doesn't include documentation. So adding more documentation doesn't affect your percentages.

    A side note for this code coverage bot: you may configure it so that it tells you that your builds are failing if the coverage goes down. In the example below Ross has added

    Here's an example: https://github.com/rmarkello/pyls/pull/44

    ---


[turing testing course mocks](https://alan-turing-institute.github.io/rsd-engineeringcourse/ch03tests/05Mocks.html) **Creative Commons share and remix**

    #### mocking
    Often we want to write tests for code which interacts with remote resources. (E.g. databases, the internet, or data files.)

    We don't want to have our tests actually interact with the remote resource, as this would mean our tests failed due to lost internet connections, for example.

    Instead, we can use mocks to assert that our code does the right thing in terms of the messages it sends: the parameters of the function calls it makes to the remote resource.

    Can be difficult to test cases like

---
    - Make a plot and visually inspect it

    - Describe a dataframe and check that the means and standard deviations are within the right range

    - Run a few different random simulations and check that they all give back values that are in the right range

    Can sanity check within reasonable values though.


* [Adopting automated testing](https://github.com/softwaresaved/automated_testing/blob/master/README.md) **Apache License 2.0**

When 0.1 + 0.2 does not equal 0.3
There is one further complication with our data that we need to address. EPCC's oncology project found that their regression tests failed when they ran their code on the HECToR super-computer. Investigation showed that this arose due to their floating point calculations giving subtly different results when run on their development machine compared to when they were run on HECToR. To see why these differences arose, look at this Python example.

If we assign 0.1 to a and 0.2 to b and print their sum, we get 0.3, as expected.

>>> a = 0.1
>>> b = 0.2
>>> print(a + b)
0.3
If, however, we compare the result of comparing the sum of a plus b to 0.3 we get False.

>>> print(a + b == 0.3)
False
If we show the value of a plus b directly, we can see there is a subtle margin of error.

>>> a + b
0.30000000000000004
This is because floating point numbers are approximations of real numbers.

The result of floating point calculations can depend upon the compiler or interpreter, processor or system architecture and number of CPUs or processes being used.

Floating point calculations are not always guaranteed to be associative. A plus B will not necessarily equal B plus A.

Equality in a floating point world
When comparing floating point numbers for equality, we have to compare to within a given tolerance, alternatively termed a threshold or delta. For example, we might consider A equal to B if the absolute value of the difference between A and B is within the absolute value of our tolerance.

A = B if | A - B <= | tolerance |

Many languages have inbuilt frameworks for testing, and many of those provide functions for comparing equality of floating point numbers to within a given tolerance.

Unit test frameworks for other languages provide similar functions:

Cunit for C: CU_ASSERT_DOUBLE_EQUAL(actual, expected, granularity)
CPPUnit for C++: CPPUNIT_ASSERT_DOUBLES_EQUAL(expected, actual, delta)
googletest for C++: ASSERT_NEAR(val1, val2, abs_error)
FRUIT for Fortran: subroutine assert_eq_double_in_range_(var1, var2, delta, message)
JUnit for Java: org.junit.Assert.assertEquals(double expected, double actual, double delta)
testthat for R:
expect_equal(actual, expected, tolerance=DELTA) - absolute error within DELTA
expect_equal(actual, expected, scale=expected, tolerance=DELTA) - relative error within DELTA

<a name="Types_of_tests"></a>
## Types of tests

*Need to add a bit more context before jumping right in.*

*positive test, test something does right, negative tests, tests crashes when it should*

[Software testing fundamentals levels of tests](http://softwaretestingfundamentals.com/software-testing-levels/) **Copyleft - 2019 STF**

Software testing levels are the different stages of the software development lifecycle where testing is conducted. There are four levels of software testing: Unit >> Integration >> System >> Acceptance.

![software_testing_levels](../figures/software_testing_levels.jpg)

### Level	Summary

*add smoke testing*

Unit testing:	A level of the software testing process where individual units of a software are tested. The purpose is to validate that each unit of the software performs as designed.

Integration testing:	A level of the software testing where individual units are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units.

System testing:	A level of the software testing process where a complete, integrated system is tested. The purpose of this test is to evaluate the system’s compliance with the specified requirements.

Acceptance testing:	A level of the software testing process where a system is tested for acceptability. The purpose of this test is to evaluate the system's compliance with the project requirements and assess whether it is acceptable for the purpose.

Here's an analogy: during the process of manufacturing a ballpoint pen, the cap, the body, the tail, the ink cartridge and the ballpoint are produced separately and unit tested separately. When two or more units are ready, they are assembled and integration testing is performed. When the complete pen is integrated, system testing is performed to check it can be used to write like any pen should. Acceptance testing could be a check to ensure the pen is the colour the customer ordered.

There is also another kind of testing called regression testing. Regression testing is a type of testing that can be performed at any of the four main levels and compares the results of tests before and after a change is made to the code.

These different types of tests will now be discussed in more detail.

## Smoke testing

[smoke testing](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**

Smoke tests are a special kind of initial checks designed to ensure very basic functionality as well as some basic implementation and environmental assumptions. Smoke tests are generally run at the very start of each testing cycle as a sanity check before running a more complete test suite.

The idea behind this type of test is to help to catch big red flags in an implementation and to bring attention to problems that might indicate that further testing is either not possible or not worthwhile. Smoke tests are not very extensive, but should be extremely quick. If a change fails a smoke test, its an early signal that core assertions were broken and that you should not devote any more time to testing until the problem is resolved. For example if the function to read in the data the data a project will work with is broken there's no point testing any further before that's fixed.

<a name="Unit_tests"></a>
## Unit tests

*Unit testing frameworks, drivers, stubs, and mock/ fake objects can be used to assist in unit testing.*

*blog to look at https://www.software.ac.uk/resources/guides/testing-your-software?_ga=2.39233514.830272891.1552653652-1336468516.1531506806*

Automated (or unit) tests are modules or classes that invoke operations on your code. A test might verify an individual function or method, a class or module, related modules or components or the software as a whole. Tests can ensure that the correct results are returned from a function, that an operation changes the state of a system as expected, and that the code behaves as expected when things go wrong (for example, if incorrect inputs are given by a user or a database connection is cut off prematurely).

---

[digitalocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
## Unit testing
Unit tests are responsible for testing individual elements of code in an isolated and highly targeted way. The functionality of individual functions and classes are tested on their own. Any external dependencies are replaced with stub or mock implementations to focus the test completely on the code in question.

Unit tests are essential to test the correctness of individual code components for internal consistency and correctness before they are placed in more complex contexts. The limited extent of the tests and the removal of dependencies makes it easier to hunt down the cause of any defects. It also is the best time to test a variety of inputs and code branches that might be difficult to hit later on. Often, after any smoke tests, unit tests are the first tests that are run when any changes are made.

Unit tests are typically run by individual developers on their own work station prior to submitting changes. However, continuous integration servers almost always run these tests again as a safe guard before beginning integration tests.
---

[Software testing fundamentals unit tests](http://softwaretestingfundamentals.com/unit-testing/) **Copyleft - 2019 STF**

## What is unit testing?

UNIT TESTING is a level of software testing where individual units/components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software. It usually has one or a few inputs and usually a single output. In procedural programming, a unit may be an individual program, function, procedure, etc. In object-oriented programming the smallest unit is typically a method.

### Benefits of unit testing

If a researcher makes a change to a piece of code or how it is run how can they be sure that doing so has not broken something? They may run a few tests, but without testing every small piece of code individually how can they be certain? Unit testing gives researchers that certainty, and allows them to be confident when changing and maintaining their code.

Here's a little example. Say a researcher has a small function that does one simple thing (here only a single line for brevity). In this example this will be raising a number to the 5th power:
```
def take_fifth_power(x):
    result = x * x * x * x * x
    return result
```

The unit test for this function could look like this:
```
def test_take_fifth_power():
    assert take_fifth_power(1.5) == 7.59375
```

So it checks that the correct result is outputted for a given input. If not the test will fail. The researcher carries on with their work. In the middle of it they decide to tidy up this function, multiplying all the numbers together like this is a bit crude. They change the `result = x * x * x * x * x` line to `result = x * 5`. Next time they run their unit tests, this test will fail, because they just made a mistake. Maybe they needed a coffee, maybe their finger slipped, maybe their coworker shot them in the ear with a nerf dart and distracted them, but when they were tidying up this function they should have written `result = x ** 5` *not* `result = x * 5`. The failed test will flag up the mistake and it can quickly be corrected. If a mistake like this went unobserved it could lead to serious errors in the researchers work which may never be found.

So unit testing leads to reliable code, but there are other benefits too. Firstly it makes development faster by making bugs easier to find. Larger-scale tests which test large hunks of code (while still useful) have the disadvantage that if they fail it is difficult to pinpoint the source of the bug. Because unit tests by their very definition test small pieces of code they help developers find the cause of a bug much more quickly than higher-level tests or code with no tests at all. Unit tests also make fixing bugs faster and easier because they catch bugs early while they only impact small individual units. If bugs are not detected early via unit tests then it may be a long time before they are discovered, impacting later work that built on the faulty code. This means much more code is at risk and fixing the bug is more time consuming.

The other major benefit of unit testing is that it strongly incentivises researchers to write modular code because modular code is far easier to write unit tests for. Modular code is code that is broken up into manageable chunks which each accomplish simple tasks. This is typically achieved by dividing the code into functions and groups of functions. In contrast a script which is just one long continuous series of lines which produces a result is highly non-modular.

Modular code is much easier to reuse, for example if a researcher has a individual function that does some Useful Thing and in a future project they need to do that thing again it is trivial to copy or import the function. In contrast if the code that does this Useful Thing is entwined with a great deal of other code in a long script it is much harder to separate it out for re-use.

Modular code also has the benefit that even if a bug is introduced the unintended impact of changes to any code is likely to be lessened or limited to that module.

### Unit testing tips

- Find a tool/framework for your language. For example the pytest module assists with running unit tests in python.
- Isolate the development environment from the test environment.
- If your tests use test data make sure it is similar to data the actual code will be applied to.
- Write test cases that are independent of each other. For example, if a unit A utilises the result of another unit B supplies you should test unit A with a "mock" input, rather than actually calling the unit B. If you don't do this your test failing may be due to a fault in either unit A *or* unit B, making the bug harder to trace.
- Aim at covering all paths through a unit. Pay particular attention to loop conditions.
- In addition to writing cases to verify the behaviour, write cases to ensure the performance of the code. For example, if a function that is supposed to add two numbers takes several minutes to run there is likely a problem.
- Run unit tests frequently.
- If you find a defect in your code write a test that exposes it. Why? First, you will later be able to catch the defect if you do not fix it properly. Second, your test suite is now more comprehensive. Third, you will most probably be too lazy to write the test after you have already fixed the defect. For example say a code has a simple function to classify people as either adults or children:

  ```
  def adult_or_child(age):

    # If the age is greater or equal to 18 classify them as an adult
    if age >= 18:
      person_status = 'Adult'

    # If the person is not an adult classify them as a child
    else:
      person_status = 'Child'

    return person_status
  ```

  And say this code has a unit test like this

  ```
  def test_adult_or_child():

    # Test that an adult is correctly classified as an adult
    assert adult_or_child(22) == 'Adult'

    # Test that an child is correctly classified as a child
    assert adult_or_child(5) == 'Child'

    return
  ```

  There's a problem with this code that isn't being tested: if a negative age is supplied it will happily classify the person as a child despite negative ages not being possible. The code should throw an error in this case. So once the bug is fixed:

  ```
  def adult_or_child(age):

  # Check age is valid
  if age < 0:
    raise

  # If the age is greater or equal to 18 classify them as an adult
  if age >= 18:
    person_status = 'Adult'

  # If the person is not an adult classify them as a child
  else:
    person_status = 'Child'

  return person_status
  ```

  go ahead and write a test to ensure that future changes in the code can't cause it to happen again:

  ```
  def test_adult_or_child():

    # Test that an adult is correctly classified as an adult
    assert adult_or_child(22) == 'Adult'

    # Test that an child is correctly classified as a child
    assert adult_or_child(5) == 'Child'

    # Test that supplying an invalid age results in an error
    assert adult_or_child(-10) ==

    return
  ```

---

[Sound software](http://soundsoftware.ac.uk/unit-testing-why-bother/) **Creative Commons Attribution-NonCommercial 3.0 License.**

Unit testing is the practice of testing the components of a program automatically, using a test program to provide inputs to each component and check the outputs. The tests are usually written by the same programmers as the software being tested, either before or at the same time as the rest of the software.

Most unit tests are written using some sort of test framework, a set of library code designed to make writing and running tests easier. Nearly all programming languages have at least one commonly used test framework.[1] But you don't have to use a test framework to do unit testing. All you need is something that can run a bit of your code, feed it some inputs, and check the results.

Of course as well as writing tests, you have to remember to run them. Many projects combine running the tests with building the software. Larger development teams automate this using some kind of continuous integration system. For individual projects, it may be enough simply to remember to run the tests before rolling a release and after any significant code change.

Practical tips for unit tests
You can do unit testing without using a test framework, and this can be a good way to get started if the thought of learning a test framework seems too complicated. A framework saves time in the long run, and in a company context you'd always have one, but for your own use it doesn't have to be something you must learn before you can start. You can just run a bit of the code, check the results, spit out hideous abuse when the results are wrong. You can even do it from a shell script if your program is simple enough.
Tests should be small—don't think you have to use bulky real-world data. If your function gets the right median value for inputs with one value, a small odd number of values, and a small even number, it'll work for bigger inputs too. Think of tricky small cases, not easy large ones. Picking good test cases is something of an art and can be an interesting exercise in its own right.
Writing the tests first (i.e. practising test-driven development) can be a real help during development especially if you're not yet clear on how the code should actually work. When you find yourself getting stuck trying to visualise how an algorithm should work or how other code should interact with it, consider whether you can approach it from the other end by describing what its output should look like. Sketch it out in the tests, then write the code until the tests pass.
Whenever you find a bug in “finished code”, add a test for it. Make sure the test fails in the buggy code and passes when it is fixed. Areas of code you've found bugs in are more likely to be fragile in general, and bugs that have already been found are relatively highly likely to reappear.
When writing a new test, include something to make sure it is being run. For example, make it fail deliberately when you first write it. It's quite common to discover that the reason your tests are all passing is that they're not being run at all. (Overlooked in the build file, private instead of public, mistyped the method name: every testing framework has its set of common mistakes.) So, always do something to make sure your test is really working.
Don't ship code with tests that fail, even if it doesn't matter that they fail. It's not uncommon, particularly in test-driven development, to change your mind during design about which tests are correct or relevant, or to make an initial implementation that only covers some of the test suite. But that means you end up with failed tests that you don't actually care about. Remove them, or at very least, document them: anyone running your tests should be able to assume that a failed test indicates broken code.
Consider using a code coverage tool to check how much of your code is actually being tested. Coverage doesn't tell you everything: it only measures static execution paths, but it can give you some idea of things you might have missed altogether.


## Integration testing

Integration testing is a level of software testing where individual units are combined and tested as a group. While unit tests validate the functionality of code in isolation, integration tests ensure that components cooperate when interfacing with one another. The purpose of this level of testing is to expose faults in the interaction between integrated units.

Here's an analogy. During the process of manufacturing a ballpoint pen, the cap, the body, the tail and clip, the ink cartridge and the ballpoint are produced separately and unit tested separately. When two or more units are ready, they are assembled and integration testing is performed. For example, whether the cap fits into the body or not.

A sub type of integration testing is system integration testing. This tests the integration of systems, packages and any interfaces to external organizations (e.g. Electronic Data Interchange, Internet). Depending on the nature of a project system integration testing may or may not be applicable.

### Approaches

There are several different approaches to integration testing. Big Bang is an approach to integration testing where all or most of the units are combined together and tested at one go. This approach is taken when the testing team receives the entire software in a bundle. So what is the difference between Big Bang integration testing and system testing? Well, the former tests only the interactions between the units while the latter tests the entire system.

Top Down is an approach to integration testing where top-level sections of the code (that themselves contain many smaller units) are tested first and lower level units are tested step by step after that. So is a code can be split into the main steps A, B, and C, and each of those  contain steps to complete them, and these steps may have substeps like:

- A
  - A.1
    - A.1.1
    - A.1.2
  - A.2
- B
  - B.1
  - B.2
    - B.2.1
    - B.2.2
    - B.2.3
  - B.3

- C
  - C.1
    - C.1.1
    - C.1.2
  - C.2
    - C.2.1
    - C.2.2

So in the top down approach the integration between sections at the top level (A, B and C) are tested, then integration between sections at the next level and so on. Testing upper level units by running all the code they contain including running lower level ones can lead to upper level tests breaking due to bugs in low level units. This is undesirable, so to prevent this the lower level sections should not be run, but mock inputs should be used to simulate the outputs from them. These mock inputs are called test stubs.

Bottom Up is an approach to integration testing where integration between bottom level sections are tested first and upper-level sections step by step after that. Again test stubs are needed to simulate inputs from higher level sections .

Sandwich/Hybrid is an approach to integration testing which is a combination of Top Down and Bottom Up approaches.

### Integration testing tips

- Ensure that you have a proper Detail Design document where interactions between each unit are clearly defined. It is difficult or impossible to perform integration testing without this information.
- Make sure that each unit is unit tested before you start integration testing.

<a name="System_tests"></a>
## System tests

Once integration tests are performed, another level of testing called system testing can begin. System testing (sometimes called end-to-end testing) is a level of software testing where a complete and integrated software is tested. The purpose of this test is to evaluate the system's compliance with the specified requirements. In many ways, system testing acts as an extension to integration testing. The focus of system tests are to make sure that groups of components function correctly as a cohesive whole.

Instead of focusing on the interfaces between components, system tests typically evaluate the outward functionality of a full piece of software. This set of tests ignores the constituent parts in order to gauge the composed software as a unified entity. Because of this distinction, system tests usually focus on user- or externally-accessible outputs.


## Acceptance testing

[digitalocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**

Acceptance tests are one of the last tests types that are performed on software prior to delivery. Acceptance testing is used to determine whether a piece of software satisfies all of the requirements from the business or user's perspective. These tests are sometimes built against the original specification and often test interfaces for the expected functionality and for usability.

Acceptance testing is often a more involved phase that might extend past the release of the software. Automated acceptance testing can be used to make sure the technological requirements of the design were met, but manual verification also usually plays a role.

Frequently, acceptance testing begins by deploying the build to a staging environment that mirrors the production system. From here, the automated test suites can be run and internal users can access the system to check whether it functions the way they need it to. After release or offering beta access to customers, further acceptance testing is performed by evaluating how the software functions with real use and by collecting feedback from users.



## Regression testing

[Sound software](http://soundsoftware.ac.uk/unit-testing-why-bother/) **Creative Commons Attribution-NonCommercial 3.0 License**

Regression testing, the business of ensuring that new changes in code don't break things that were working before. Regression testing is obviously especially important in team working, but it is surprisingly easy to break your own code without noticing it, even if you are working on your own. And because regression testing is next to impossible to do satisfactorily by hand (it's simply too tedious), it's an obvious case for automation

---

[Software testing fundamentals regression testing](http://softwaretestingfundamentals.com/regression-testing/) **Copyleft**

Regression testing is a type of software testing that intends to ensure that changes (enhancements or defect fixes) to the software have not adversely affected it.

The likelihood of any code change impacting functionalities that are not directly associated with the code is always there and it is essential that regression testing is conducted to make sure that fixing one thing has not broken another thing.

During regression testing, new test cases are not created but previously created test cases are re-executed.

Regression literally means the act of going back to a previous place or state; return or reversion.

Regression testing can be performed during any level of testing (unit, integration, system, or acceptance) but it is mostly relevant during system testing.

In an ideal case, a full regression test is desirable but oftentimes there are time/resource constraints. In such cases, it is essential to do an impact analysis of the changes to identify areas of the software that have the highest probability of being affected by the change and that have the highest impact to users in case of malfunction and focus testing around those areas.

Due to the scale and importance of regression testing, more and more companies and projects are adopting regression test automation tools.

---

[Examples of Regression Testing by Cem Karner](http://www.testingeducation.org/k04/RegressionExamples.htm) ** Creative Commons Attribution-ShareAlike License 2.0**

Regression testing is a style of testing that focuses on retesting after changes are made. In traditional regression testing, we reuse the same tests (the regression tests). In risk-oriented regression testing, we test the same areas as before, but we use different (increasingly complex) tests. Traditional regression tests are often partially automated. These note focus on traditional regression.

Regression testing attempts to mitigate two risks:

A change that was intended to fix a bug failed.
Some change had a side effect, unfixing an old bug or introducing a new bug.
In addition, proponents of traditional regression testing argue that retesting is a measurement or control process, a means of assuring that the program is as stable as it was previously.

Regression testing approaches differ in their focus. Common examples include:

Bug regression: We retest a specific bug that has been allegedly fixed.
Old fix regression testing: We retest several old bugs that were fixed, to see if they are back. (This is the classical notion of regression: the program has regressed to a bad state.)
General functional regression: We retest the product broadly, including areas that worked before, to see whether more recent changes have destabilized working code. (This is the typical scope of automated regression testing.)
Conversion or port testing: The program is ported to a new platform and a subset of the regression test suite is run to determine whether the port was successful. (Here, the main changes of interest might be in the new platform, rather than the modified old code.)
Configuration testing: The program is run with a new device or on a new version of the operating system or in conjunction with a new application. This is like port testing except that the underlying code hasn't been changed--only the external components that the software under test must interact with.
Localization testing: The program is modified to present its user interface in a different language and/or following a different set of cultural rules. Localization testing may involve several old tests (some of which have been modified to take into account the new language) along with several new (non-regression) tests.
Smoke testing also known as build verification testing:A relatively small suite of tests is used to qualify a new build. Normally, the tester is asking whether any components are so obviously or badly broken that the build is not worth testing or some components are broken in obvious ways that suggest a corrupt build or some critical fixes that are the primary intent of the new build didn't work. The typical result of a failed smoke test is rejection of the build (testing of the build stops) not just a new set of bug reports.
Any test can be reused, and so any test can become a regression test. Regression testing naturally combines with all other test techniques. The essence of regression testing is exposure of problems that shouldn't be there, either because they were exterminated before or they weren't in the product the last time(s) it was tested.

---

* [Adopting automated testing](https://github.com/softwaresaved/automated_testing/blob/master/README.md) **Apache License 2.0**

Regression testing allows us to check that our code continues to be correct after we have made changes to it. Unit testing can then be introduced at a later date, when the demands of research permit.

Regression testing does not test whether our code produces scientifically-correct results, only that we don't change its behaviour in unexpected ways. We will return to this distinction later.

To introduce regression testing we can follow a recipe.

First, we create a test oracle. We run out code on sets of input files and parameters. We save the corresponding output files. These output files serve as the expected outputs from our program given the corresponding input files and parameters.
We then write regression tests. Each regression test runs our code for a set of input files and parameters. It then compares the output from our code to the expected outputs within the test oracle, it compares the actual outputs to the expected outputs.
We run our regression tests regularly, or after every change to the code, to check we have not introduced any bugs that have changed its behaviour.

### Limitations

Regression tests are not guaranteed to test all parts of the code. Test coverage tools can provide information on what parts of our code are, or are not, executed when we run our regression tests.

Most importantly, regression tests do not test if the result outputted by a piece of code is *correct*, only that is has not changed. This the remit of unit and system tests, though regression tests can serve as the starting point for introducing tests for correctness, by both the use of analytical solutions, and test functions which read output files and check the data for correctness, as defined by a researcher.

## Runtime testing


## Test driven development

*blog to look at https://www.software.ac.uk/resources/guides/testing-your-software?_ga=2.39233514.830272891.1552653652-1336468516.1531506806*

One way of ensuring tests are not neglected in a project, is to adopt test-driven development. This is an approach in which the tests for a function, class, module or component are written before the code. Once the tests are written, the code is developed so that it passes all the associated tests. Testing the code from the outset ensures that your code is always in a releasable state (as long as it passes the tests!).


[Sound software](http://soundsoftware.ac.uk/unit-testing-why-bother/) **Creative Commons Attribution-NonCommercial 3.0 License.**
Some developers practise test-driven development, a process in which the unit tests are written before the rest of the code. The tests thus describe a “contract” that the code is expected to comply with. This ensures that the code will be correct (as far as can be enforced by the testing contract) as written, and it provides a useful framework for thinking about how the code should be designed, what interfaces it should provide, and how its algorithms might work. This can be a very satisfying mental aid in developing tricky algorithms.


*An alternative development approach is behaviour driven development. Simply put test driven development tests "has the thing been done correctly?", behaviour driven development tests "has the correct thing been done?". It is more often used in commercial software development to focus development on making the software as simple and useful as possible for users. User experience is very rarely at the heart of code written for the purposes of research, but there are cases where such software is written with a large user-base in mind. In such cases behaviour-driven development is a path worth considering.*

## Checklist


## What to learn next

Try reading the chapter on reproducible computational environments and then the chapter on continuous integration.

## Further reading

## Definitions/glossary

- **:**

- **:**

- **Code coverage:** Code coverage is a measure which describes how much of the source code is exercised by the test suite.

- **:**

- **:**

- **:**

- **Test driven development:**

- **:**

- **:**


## Bibliography

### Materials used: general guidance and good practice for testing

- [SSI blog on testing software](https://www.software.ac.uk/resources/guides/testing-your-software?_ga=2.39233514.830272891.1552653652-1336468516.1531506806) **Creative Commons Attribution Non-Commercial 2.5 License.**
- [Turing testing course basics](https://alan-turing-institute.github.io/rsd-engineeringcourse/ch03tests/03pytest.html) **Creative Commons share and remix**

### Materials used: integration testing

- [Digitalocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
- [Software testing fundamentals: integration testing](http://softwaretestingfundamentals.com/integration-testing/) **Copyleft - 2019 STF**

### Materials used: system testing

- [Software testing fundamentals: system testing](http://softwaretestingfundamentals.com/system-testing/) **Copyleft - 2019 STF**
- [Digitalocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**

### Materials used: glossary

- [Netherlands eScience centre](https://guide.esciencecenter.nl/best_practices/testing.html) **Creative Commons Attribution 4.0 International License**
