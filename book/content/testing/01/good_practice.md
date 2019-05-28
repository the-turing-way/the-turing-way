## General guidance and good practice for testing

There are a number of [different kinds](#Types_of_tests) of testing which each have best practice specific to them. Nevertheless there is some general guidance that applies to all of them, which will be outlined here.

<a name="Write_tests_any_tests"></a>
### Write tests. Any tests.

Starting the process of writing tests can be overwhelming, especially if you have a large code base. Further to that, as mentioned, there are many kinds of tests, and implementing all of them can seem like an impossible mountain to climb. That is why the single most important piece of guidance in this chapter is as follows: **write some tests**. Testing one tiny thing in a code that's thousands of lines long is infinitely better than testing no things in a code that's thousands of lines long. You may not be able to do everything, but doing *something* is valuable.

Do not be discouraged. Make improvements where you can, and do your best to include tests with new code you write even if it's not feasible to write tests for all the code that's already written.

<a name="Run_the_tests"></a>
### Run the tests

The second most important piece of advice in this chapter: run the tests. Having a beautiful, perfect test suite is no use if you rarely run it. Leaving long gaps between test runs makes it more difficult to track down what has gone wrong when a test fails because a great deal in the code will have changed. Also if it's been weeks or months since tests have been run and they fail it is difficult or impossible to know what work/results that have been done in the intervening time are still valid, and which have to be thrown away as they could have been impacted by the bug.

As such it is best to automate your testing as far as possible. If each test needs to be run individually then that boring painstaking process is likely to get neglected. This can be done by making use of a testing framework ([discussed later](#Use_a_testing_framework)). [Jenkins](https://jenkins.io) is another good tool for this. Ideally set your tests up to run at regular intervals, possibly each night.

Consider setting up continuous integration (discussed in the continuous integration chapter) on your project. This will automatically run your tests each time you make a change to your code and, depending on the continuous integration software you use, will notify you if any of the tests fail.

<a name="Consider_how_long_it_takes_your_tests_to_run"></a>
### Consider how long it takes your tests to run

Some tests, like [unit tests](#Unit_tests) only test a small piece of code and so typically are very fast. However other kinds of tests, such as [system tests](#System_tests) which test the entire code from end to end, may take a long time to run depending on the code. As such it can be obstructive to run the entire test suite after each little bit of work. In that case it is better to run lighter weight tests such as unit tests frequently, and longer tests only once per day overnight. It is also good to scale the number of each kind of tests you have in relation to how long they take to run. You should have a lot of unit tests (or other types of tests that are fast) but much fewer tests which take a long time to run.

<a name="Document_the_tests_and_how_to_run_them"></a>
### Document the tests and how to run them

It is important to provide documentation that describes how to run the tests, both for yourself in case you come back to a project in the future, and for anyone else that may wish to build upon or reproduce your work. This documentation should also cover subjects such as

- Any resources e.g. test dataset files that are required
- Any configuration/settings adjustments needed to run the tests
- What software (such as [testing frameworks](#Use_a_testing_framework)) need to be installed

Ideally, you would provide scripts to set up and configure any resources that are needed.

<a name="Test_realistic_cases"></a>
### Test realistic cases

Make the cases you test as realistic as possible. If for example, you have dummy data to run tests on you should make sure that data is as similar as possible to the actual data. If your actual data is messy with a lot of null values, so should your test dataset be.

<a name="Use_a_testing_framework"></a>
### Use a testing framework

There are tools available to make writing and running tests easier, these are known as testing frameworks. Find one you like, learn about the features it offers, and make use of them. Common testing frameworks (and the languages they apply to) include:

- Language agnostic
  - CTest, test runner for executables, bash scripts, etc, great for legacy code hardening
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
  - pytest (recommended)
  - unittest comes with standard Python library
- R unit-tests
  - RUnit
  - svUnit (works with SciViews GUI)
- Fortran unit-tests:
  - funit
  - pfunit (works with MPI)

<a name="Aim_to_have_a_good_code_coverage"></a>
### Aim to have a good code coverage

Code coverage is a measure of how much of your code is "covered" by tests. More precisely it a measure of how much of your code is run when tests are conducted. So for example, if you have a `if` statement but only test things where that if statement evaluates to "True" then none of the code that comes under "False" will be run. As a result your code coverage would be < 100% (the exact number would depend on how much code comes under the True and False cases). Code coverage doesn't include documentation like comments, so adding more documentation doesn't affect your percentages.

As [mentioned](#Write_tests_any_tests) any tests are an improvement over no tests. Nevertheless it is good to at least aspire to having your code coverage as high as feasible.

Most programming languages have tools either built into them, or that can be imported, or as part of testing frameworks, which automatically measure code coverage. There's also a nice little [bot](https://codecov.io/) for measuring code coverage available too.

**Pitfall: The illusion of good coverage.** In some instances, the same code can and probably should be tested in multiple ways. For example, coverage can quickly increase on code that applies "sanity check" tests to its output ([see below](#tests-that-are-difficult-to-quantify)), but this doesn't preclude the risk that the code is producing the broadly right answer for the wrong reasons. In general, the best tests are those that isolate the smaller rather than larger chunks of coherent code, and so pick out individual steps of logic. Try to be guided by thinking about the possible things that might happen to a particular chunk of code in the execution of the whole, and test these individual cases. Often, this will result in the same code being tested multiple times - this is a good thing!

<a name="Use_test_doubles_stubs_mocking_where_appropriate"></a>
### Use test doubles/stubs/mocking where appropriate

If a test fails it should be constructed such that is as easy to trace the source of the failure as possible. This becomes problematic if a piece of code you want to test unavoidably depends on other things. For example if a test for a piece of code that interacts with the web fails that could be because the code has a bug *or* there is a problem with the internet connection. Similarly if a test for a piece of code that uses an object fails it could be because there is a bug in the code being tested, or a problem with the object (which should be tested by its own, separate tests). These dependencies should be eliminated from tests, if possible. This can be done via using test replacements (test doubles) in the place of the real dependencies. Test doubles can be classified as follows:

- A dummy object is passed around but never used i.e. its methods are never called. Such an object can for example be used to fill the parameter list of a method.
- Fake objects have working implementations, but are usually simplified. For example, they use an in memory database and not a real database.
- A stub is an partial implementation for an interface or class with the purpose of using an instance of this stub during testing. Stubs usually don’t respond to anything outside what’s programmed in for the test. Stubs may also record information about calls.
- A mock object is a dummy implementation for an interface or a class in which you define the output of certain method calls. Mock objects are configured to perform a certain behaviour during a test. They typically record the interaction with the system and tests can validate that.

Test doubles can be passed to other objects which are tested.

You can create mock objects manually (via code) or use a mock framework to simulate these classes. Mock frameworks allow you to create mock objects at runtime and define their behaviour. The classical example for a mock object is a data provider. In production an implementation to connect to the real data source is used. But for testing a mock object simulates the data source and ensures that the test conditions are always the same.

<a name="Testing_stochastic_code"></a>
### Testing stochastic code

Sometimes code contains an element of randomness, a common example being code that makes use of [Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method). Testing this kind of code can be very difficult because if it is run multiple times it will generate different answers, all of which may be "right", even is it contains no bugs. There are two main ways to tackle testing stochastic code:

<a name="Use_random_number_seeds"></a>
#### Use random number seeds

Random number seeds are a little difficult to explain so here's an example. Here's a little Python script that prints three random numbers.
```
import random

# Print three random numbers
print(random.random())
print(random.random())
print(random.random())
```

This script has no bugs but if you run it repeatedly you will get different answers each time. Now let's set a random number seed.
```
import random

# Set a random number seed
random.seed(1)

# Print three random numbers
print(random.random())
print(random.random())
print(random.random())
```

Now if you run this script it outputs
```
0.134364244112
0.847433736937
0.763774618977
```

and every time you run this script you will get the *same* output, it will print the *same* three random numbers. If the random number seed is changed you will get a different three random numbers:

```
0.956034271889
0.947827487059
0.0565513677268
```
but again you will get those same numbers every time the script is run in the future.

Random number seeds are a way of making things reliably random. However a risk with tests that depend on random number seeds is they can be brittle. Say you have a function structured something like this:
```
def my_function()

  a = calculation_that_uses_two_random_numbers()

  b = calculation_that_uses_five_random_numbers()

  c = a + b
```

If you set the random number seed you will always get the same value of `c`, so it can be tested. But, say the model is changed and the function that calculates `a` uses a different number of random numbers that it did previously. Now not only will `a` be different but `b` will be too, because as shown above the random numbers outputted given a random number seed are in a fixed order. As a result the random numbers produced to calculate `b` will have changed. This can lead to tests failing when there is in fact no bug.

<a name="Measure_the_distribution_of_results"></a>
#### Measure the distribution of results

Another way to test code with a random output is to run it many times and test the distribution of the results. Perhaps the result may fluctuate a little, but is always expected around 10 within some tolerance. That can be tested. The more times the code is run the more reliable the average and so the result. However the more times you run a piece of code the longer it will take your tests to run, which may make tests prohibitively time-consuming to conduct if a reliable result is to be obtained. Furthermore, there will always be an element of uncertainty and if the random numbers happen to fall in a certain way you may get result outside of the expected tolerance even if the code is correct.

Both of these approaches to testing stochastic code can still be very useful, but it is important to also be aware of their potential pitfalls.

<a name="Tests_that_are_difficult_to_quantify"></a>
### Tests that are difficult to quantify

Sometimes (particularly in research) the outputs of code are tested according to whether they "look" right. For example say we have a code modelling the water levels in a reservoir over time. The result may look like this:

![eyeball_test_1](/assets/figures/eyeball_test_1.jpg)

On a day with rain it might look like this:

![eyeball_test_2](/assets/figures/eyeball_test_2.jpg)

and on a dry day it might look like this:

![eyeball_test_3](/assets/figures/eyeball_test_3.jpg)

All of these outputs look very different but are valid. However, if a researcher sees a result like this:

![eyeball_test_error](/assets/figures/eyeball_test_error.jpg)

they could easily conclude there is a bug as a lake is unlikely to triple it's volume and then lose it again in the space of a few hours. "Eyeballing" tests like these are time consuming as they must be done by a human. However the process can be partially or fully automated by creating basic "sanity checks". For example the water level at one time should be within, say, 10% of the water level at the previous time step. Another check could be that there are no negative values, as a lake can't be -30% full. These sort of tests can't cover every way something can be visibly wrong, but they are much easier to automate and will suffice for most cases.

<a name="Testing_if_non_integer_numbers_are_equal"></a>
### Testing if non-integer numbers are equal

<a name="When_point_1_plus_point_2_does_not_equal_point_3"></a>
#### When 0.1 + 0.2 does not equal 0.3

There is a complication with testing if the answer a piece of code outputs is equal to the expected answer when the numbers are not integers. Let's look at this Python example, but note that this problem is not unique to Python.

If we assign 0.1 to `a` and 0.2 to `b` and print their sum, we get 0.3, as expected.
```
>>> a = 0.1
>>> b = 0.2
>>> print(a + b)
0.3
```

If, however, we compare the result of `a` plus `b` to 0.3 we get False.
```
>>> print(a + b == 0.3)
False
```

If we show the value of `a` plus `b` directly, we can see there is a subtle margin of error.
```
>>> a + b
0.30000000000000004
```

This is because floating point numbers are approximations of real numbers. The result of floating point calculations can depend upon the compiler or interpreter, processor or system architecture and number of CPUs or processes being used. Obviously this can present a major obstacle for writing tests.

<a name="Equality_in_a_floating_point_world"></a>
#### Equality in a floating point world

When comparing floating point numbers for equality, we have to compare to within a given tolerance, alternatively termed a threshold or delta. For example, we might consider the calculated and expected values of some number to be equal if the absolute value of their difference is within the absolute value of our tolerance.

Many testing frameworks provide functions for comparing equality of floating point numbers to within a given tolerance. For example for the framework pytest:
```
import pytest

a = 0.1
b = 0.2
c = a + b
assert c == pytest.approx(0.3)
```

this passes, but if the 0.3 was changed to 0.4 it would fail.

Unit test frameworks for other languages also often provide similar functions:

- Cunit for C: CU_ASSERT_DOUBLE_EQUAL(actual, expected, granularity)
- CPPUnit for C++: CPPUNIT_ASSERT_DOUBLES_EQUAL(expected, actual, delta)
- googletest for C++: ASSERT_NEAR(val1, val2, abs_error)
- FRUIT for Fortran: subroutine assert_eq_double_in_range_(var1, var2, delta, message)
- JUnit for Java: org.junit.Assert.assertEquals(double expected, double actual, double delta)
- testthat for R:
  - expect_equal(actual, expected, tolerance=DELTA) - absolute error within DELTA
  - expect_equal(actual, expected, scale=expected, tolerance=DELTA) - relative error within DELTA
