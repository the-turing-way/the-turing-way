(rr-testing-unittest)=
# Unit Testing

Unit tests are responsible for testing individual elements of code in an isolated and highly targeted way.
The functionality of individual functions and classes are tested on their own.
The purpose is to validate that each unit of the software performs as designed.
A unit is the smallest testable part of any software.
In procedural programming, a unit may be an individual program, function or procedure.
In object-oriented programming the smallest unit is typically a method.
It usually has one or a few inputs and usually a single output.
Any external dependencies should be replaced with stub or mock implementations to focus the test completely on the code in question.

Unit tests are essential to test the correctness of individual code components for internal consistency and correctness before they are placed in more complex contexts.
The limited extent of the tests and the removal of dependencies makes it easier to hunt down the cause of any defects.
It also is the best time to test a variety of inputs and code branches that might be difficult to hit later on.
For example system tests are often time consuming to run and it will likely be impractical to have system tests for every possible path through a code that has more than a few conditional statements.
Unit tests are smaller, faster, and so it is more practical to cover all possible cases with them.

Often, after any smoke tests, unit tests are the first tests that are run when any changes are made.

## Benefits of Unit Testing

If a researcher makes a change to a piece of code or how it is run then how can they be sure that doing so has not broken something?
They may run a few tests, but without testing every small piece of code individually how can they be certain?
Unit testing gives researchers that certainty, and allows them to be confident when changing and maintaining their code.

Here's a little example.
Say a researcher has a small function that does one simple thing (here only a single line for brevity).
In this example this will be raising a number to the 5th power:

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

So it checks that the correct result is outputted for a given input.
If not the test will fail.
The researcher carries on with their work.
In the middle of it they decide to tidy up this function, multiplying the number five times like this is a bit crude.
They change the `result = x * x * x * x * x` line to `result = x * 5`.
Next time they run their unit tests, this test will fail, because they just made a mistake.
Maybe they needed a coffee, maybe their finger slipped, maybe their coworker shot them in the ear with a nerf dart and distracted them, but when they were tidying up this function they should have written `result = x ** 5` *not* `result = x * 5`.
The failed test will flag up the mistake and it can quickly be corrected.
If a mistake like this went unobserved it could lead to serious errors in the researcher's work.

So unit testing leads to more reliable code, but there are other benefits too.
Firstly, it makes development faster by making bugs easier to find.
Larger-scale tests which test large chunks of code (while still useful) have the disadvantage that if they fail it is difficult to pinpoint the source of the bug.
Because unit tests by their very definition test small pieces of code, they help developers find the cause of a bug much more quickly than higher-level tests or code with no tests at all.
Unit tests also make fixing bugs faster and easier because they catch bugs early while the impact is limited to small individual units.
If bugs are not detected early via unit tests then it may be a long time before they are discovered, impacting later work that built on the faulty code.
This means that much more code is at risk and that fixing the bug is more time consuming.

The other major benefit of unit testing is that it strongly incentivises researchers to write modular code because modular code is far easier to write unit tests for.
Modular code is code that is broken up into manageable chunks which each accomplish simple tasks.
This is typically achieved by dividing the code into functions and groups of functions.
In contrast a script which is just one long continuous series of lines which produces a result is highly non-modular.

Modular code is much easier to reuse, too.
For example, if a researcher has an individual function that does some Useful Thing and in a future project they need to do that thing again, it is trivial to copy or import the function.
In contrast, if the code that does this Useful Thing is entwined with a great deal of other code in a long script it is much harder to separate it out for re-use.

## Unit Testing Tips

- Many testing frameworks have tools specifically geared towards writing and running unit tests.
- Isolate the development environment from the test environment.
- Write test cases that are independent of each other. For example, if a unit A utilises the result supplied by another unit B, you should test unit A with a [test double][rr-testing-guidance-mocking], rather than actually calling the unit B. If you don't do this your test failing may be due to a fault in either unit A *or* unit B, making the bug harder to trace.
- Aim at covering all paths through a unit. Pay particular attention to loop conditions.
- In addition to writing cases to verify the behaviour, write cases to ensure the performance of the code. For example, if a function that is supposed to add two numbers takes several minutes to run there is likely a problem.
- If you find a defect in your code write a test that exposes it. Why? First, you will later be able to catch the defect if you do not fix it properly. Second, your test suite is now more comprehensive. Third, you will most probably be too lazy to write the test after you have already fixed the defect. Say a code has a simple function to classify people as either adults or children:

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

And say this code has a unit test like this:

```
def test_adult_or_child():

  # Test that an adult is correctly classified as an adult
  assert adult_or_child(22) == 'Adult'

  # Test that an child is correctly classified as a child
  assert adult_or_child(5) == 'Child'

  return
```

There's a problem with this code that isn't being tested: if a negative age is supplied it will happily classify the person as a child despite negative ages not being possible.
The code should throw an error in this case.

So once the bug is fixed:
```
def adult_or_child(age):

  # Check age is valid
  if age < 0:
    raise ValueError, 'Not possible to have a negative age'

  # If the age is greater or equal to 18 classify them as an adult
  if age >= 18:
    person_status = 'Adult'

  # If the person is not an adult classify them as a child
  else:
    person_status = 'Child'

  return person_status
```

Go ahead and write a test to ensure that future changes in the code can't cause it to happen again:
```
def test_adult_or_child():

  # Test that an adult is correctly classified as an adult
  assert adult_or_child(22) == 'Adult'

  # Test that an child is correctly classified as a child
  assert adult_or_child(5) == 'Child'

  # Test that supplying an invalid age results in an error
  with pytest.raises(ValueError):
    adult_or_child(-10)
```
