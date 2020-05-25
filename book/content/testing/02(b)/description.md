<a name="Smoke_testing"></a>
## Smoke testing

Smoke tests (also known as build verification tests) are a special kind of initial checks designed to ensure very basic functionality as well as some basic implementation and environmental assumptions. Smoke tests are generally run at the very start of each testing cycle as a sanity check before running a more complete test suite.

The idea behind this type of test is to help to catch big red flags in implementation and to bring attention to problems that might indicate that further testing is either not possible or not worthwhile. Normally, the tester is asking whether any components are so obviously or badly broken that the build is not worth testing or some components are broken in obvious ways that suggest a corrupt build or some critical fixes that are the primary intent of the new build didn't work. Smoke tests are not very extensive but should be extremely quick. If a change to a project causes it to fail a smoke test, its an early signal that core assertions were broken and that you should not devote any more time to testing until the problem is resolved. For example, if a function that reads in the data a project requires to run is broken there's no point testing any further before that's fixed. The typical result of a failed smoke test is a rejection of the build (testing of the build stops) not just a new set of bug reports.

<a name="Unit_tests"></a>
## Unit tests

Unit tests are responsible for testing individual elements of code in an isolated and highly targeted way. The functionality of individual functions and classes are tested on their own. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software. In procedural programming, a unit may be an individual program, function or procedure. In object-oriented programming, the smallest unit is typically a method. It usually has one or a few inputs and usually a single output. Any external dependencies should be replaced with [stub or mock implementations](#Use_test_doubles_stubs_mocking_where_appropriate) to focus the test completely on the code in question.

Unit tests are essential to test the correctness of individual code components for internal consistency and correctness before they are placed in more complex contexts. The limited extent of the tests and the removal of dependencies makes it easier to hunt down the cause of any defects. It also is the best time to test a variety of inputs and code branches that might be difficult to hit later on. For example system tests are often time-consuming to run and it will likely be impractical to have system tests for every possible path through a code that has more than a few conditional statements. Unit tests are smaller, faster, and so it is more practical to cover all possible cases with them.

Often, after any smoke tests, unit tests are the first tests that are run when any changes are made.

<a name="Benefits_of_unit_testing"></a>
### Benefits of unit testing

If a researcher makes a change to a piece of code or how it is run then how can they be sure that doing so has not broken something? They may run a few tests, but without testing every small piece of code individually how can they be certain? Unit testing gives researchers that certainty and allows them to be confident when changing and maintaining their code.

Here's a little example. Say a researcher has a small function that does one simple thing (here only a single line for brevity). In this example this will be raising a number to the 5th power:
```python
def take_fifth_power(x):
    result = x * x * x * x * x
    return result
```

The unit test for this function could look like this:
```python
def test_take_fifth_power():
    assert take_fifth_power(1.5) == 7.59375
```

So it checks that the correct result is outputted for a given input. If not the test will fail. The researcher carries on with their work. In the middle of it, they decide to tidy up this function, multiplying the number five times like this is a bit crude. They change the `result = x * x * x * x * x` line to `result = x * 5`. Next time they run their unit tests, this test will fail, because they just made a mistake. Maybe they needed a coffee, maybe their finger slipped, maybe their coworker shot them in the ear with a nerf dart and distracted them, but when they were tidying up this function they should have written `result = x ** 5` *not* `result = x * 5`. The failed test will flag up the mistake and it can quickly be corrected. If a mistake like this went unobserved it could lead to serious errors in the researcher's work.

So unit testing leads to more reliable code, but there are other benefits too. Firstly it makes development faster by making bugs easier to find. Larger-scale tests which test large chunks of code (while still useful) have the disadvantage that if they fail it is difficult to pinpoint the source of the bug. Because unit tests by their very definition test small pieces of code they help developers find the cause of a bug much more quickly than higher-level tests or code with no tests at all. Unit tests also make fixing bugs faster and easier because they catch bugs early while they only impact small individual units. If bugs are not detected early via unit tests then it may be a long time before they are discovered, impacting later work that built on the faulty code. This means much more code is at risk and fixing the bug is more time-consuming.

The other major benefit of unit testing is that it strongly incentivises researchers to write modular code because modular code is far easier to write unit tests for. Modular code is code that is broken up into manageable chunks which each accomplish simple tasks. This is typically achieved by dividing the code into functions and groups of functions. In contrast, a script which is just one long continuous series of lines which produces a result is highly non-modular.

Modular code is much easier to reuse, for example, if a researcher has an individual function that does some Useful Thing and in a future project they need to do that thing again it is trivial to copy or import the function. In contrast, if the code that does this Useful Thing is entwined with a great deal of other code in a long script it is much harder to separate it out for re-use.

<a name="Unit_testing_tips"></a>
### Unit testing tips

- Many testing frameworks have tools specifically geared towards writing and running unit tests.
- Isolate the development environment from the test environment.
- Write test cases that are independent of each other. For example, if a unit A utilises the result of another unit B supplies you should test unit A with a [test double](#Use_test_doubles_stubs_mocking_where_appropriate), rather than actually calling the unit B. If you don't do this your test failing may be due to a fault in either unit A *or* unit B, making the bug harder to trace.
- Aim at covering all paths through a unit. Pay particular attention to loop conditions.
- In addition to writing cases to verify the behaviour, write cases to ensure the performance of the code. For example, if a function that is supposed to add two numbers takes several minutes to run there is likely a problem.
- If you find a defect in your code, write a test that exposes it. Why? First, you will later be able to catch the defect if you do not fix it properly. Second, your test suite is now more comprehensive. Third, you will most probably be too lazy to write the test after you have already fixed the defect. Say a code has a simple function to classify people as either adults or children:

  ```python
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

  ```python
  def test_adult_or_child():

    # Test that an adult is correctly classified as an adult
    assert adult_or_child(22) == 'Adult'

    # Test that an child is correctly classified as a child
    assert adult_or_child(5) == 'Child'

    return
  ```

There's a problem with this code that isn't being tested: if a negative age is supplied it will happily classify the person as a child despite negative ages not being possible. The code should throw an error in this case. So once the bug is fixed:
```python
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

go ahead and write a test to ensure that future changes in the code can't cause it to happen again:
```python 
def test_adult_or_child():

  #Test that an adult is correctly classified as an adult
  assert adult_or_child(22) == 'Adult'

  # Test that an child is correctly classified as a child
  assert adult_or_child(5) == 'Child'

  # Test that supplying an invalid age results in an error
  with pytest.raises(ValueError):
      adult_or_child(-10)
```

<a name="Integration_testing"></a>
## Integration testing

Integration testing is a level of software testing where individual units are combined and tested as a group. While unit tests validate the functionality of code in isolation, integration tests ensure that components cooperate when interfacing with one another. The purpose of this level of testing is to expose faults in the interaction between integrated units.

For example, maybe a unit that reads in some data is working and passes its unit tests, and the following unit that cleans up the data once it's been read in is also working and passes its tests. However say the first unit outputs the data as (time_data, temperature_data) but the function that cleans the data expects an input of the form (temperature_data, time_data). This can obviously lead to bugs. While the units are correct there is an error in their integration.

An example of an integration test for this case could be to supply a test data file, use these functions to read it in and clean it and check the resulting cleaned data against what would be expected. If a bug like this is present then the cleaned data outputted would be very unlikely to match the expected result, and an error would be raised.

Integration testing is particularly important in collaborative projects where different people work on different parts of the code. If two different people completely separate units and then need to integrate then integration issues are more likely as neither may understand the other's code. A famous example of this is a multi-million dollar satellite which [crashed](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) because one piece of code outputted distance data in feet, while another assumed data in meters. This is another example of an integration issue.

A subtype of integration testing is system integration testing. This tests the integration of systems, packages and any interfaces to external organizations (such as Electronic Data Interchange, Internet). Depending on the nature of a project system integration testing may or may not be applicable.

<a name="Approaches"></a>
### Approaches

There are several different approaches to integration testing. Big Bang is an approach to integration testing where all or most of the units are combined together and tested at one go. This approach is taken when the testing team receives the entire software in a bundle. So what is the difference between Big Bang integration testing and system testing? Well, the former test only the interactions between the units while the latter tests the entire system.

Top-Down is an approach to integration testing where top-level sections of the code (that themselves contain many smaller units) are tested first and lower-level units are tested step by step after that. So is a code can be split into the main steps A, B, and C, and each of those  contain steps to complete them, and these steps may have substeps like:

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

So in the top-down approach the integration between sections at the top level (A, B and C) are tested, then integration between sections at the next level (for example, A.1 -> A.2) and so on. Testing upper-level units by running all the code they contain including running lower level ones can lead to upper-level tests breaking due to bugs in low-level units. This is undesirable, so to prevent this the lower level sections should not be run, but [test stubs](#Use_test_doubles_stubs_mocking_where_appropriate) should be used to simulate the outputs from them.

Bottom-Up is an approach to integration testing where integration between bottom level sections are tested first and upper-level sections step by step after that. Again test stubs should be used, in this case, to simulate inputs from higher-level sections.

Sandwich/Hybrid is an approach to integration testing which is a combination of Top-Down and Bottom-Up Approaches.

Which approach you should use will depend on which best suits the nature/structure of your project.

<a name="Integration_testing_tips"></a>
### Integration testing tips

- Ensure that you have a proper Detail Design document where interactions between each unit are clearly defined. It is difficult or impossible to perform integration testing without this information.
- Make sure that each unit is unit tested and fix any bugs before you start integration testing. If there is a bug in the individual units then the integration tests will almost certainly fail even if there is no error in how they are integrated.
- Use mocking/stubs where appropriate.

<a name="System_tests"></a>
## System tests

Once integration tests are performed, another level of testing called system testing can begin. System testing is a level of software testing where a complete and integrated software is tested. The tester supplies the program with input and verifies if the program's output is correct. If it is not then there is a problem somewhere in the system. Note that this does not have to be done manually, it can be automated. The purpose of these tests is to evaluate the system's compliance with the specified requirements. In many ways, system testing acts as an extension to integration testing. The focus of system tests is to make sure that groups of components function correctly as a cohesive whole.
However, instead of focusing on the interfaces between components, system tests typically evaluate the outward functionality of a full piece of software. This set of tests ignores the constituent parts in order to gauge the composed software as a unified entity. Because of this distinction, system tests usually focus on the user- or externally-accessible outputs.

System testing can also test features of the system other than correctness. Examples include:

- Performance testing: does the program performance meet the minimum requirements? A performance test may measure how long the system takes to run in a given case.
- Migration testing: does the program work when transferred to another computational environment?
- Stress/scale/load testing: testing how the program behaves when under stress, for example, when required to process very large volumes of data.
- Usability testing: how user-friendly is the program (more common in commercial software, tests typically conducted by humans rather than automated).
- Recovery testing: Can the program continue if errors occur (again, more common in commercial software).

<a name="System_testing_tips"></a>
### System testing tips

System tests, also called end-to-end tests, run the program, well, from end to end. As such these are the most time-consuming tests to run. Therefore you should only run these if all the lower-level tests (smoke, unit, integration) have already passed. If they haven't fixed the issues they have detected first before wasting time running system tests.

Because of their time-consuming nature, it will also often be impractical to have enough system tests to trace every possible route through a program, especially is there are a significant number of conditional statements. Therefore you should consider the system test cases you run carefully and prioritise:

- The most common routes through a program.
- The most important routes for a program. For example, the LIGO detector aims to find gravitational wave events, which are extremely rare. If there's a bug in that path through the program which monitors the detector then it's a *huge* problem.
- Cases that are prone to breakage due to structural problems within the program. Though ideally, it's better to just fix those problems, cases exist where this may not be feasible.

Because system tests can be time-consuming it may be impractical to run them very regularly (such as multiple times a day after small changes in the code). Therefore it can be a good idea to run them each night (and to automate this process) so that if errors are introduced that only system testing can detect the programmer will be made of them relatively quickly.

<a name="Acceptance_testing"></a>
## Acceptance testing

Acceptance tests are one of the last tests types that are performed on software prior to delivery. Acceptance testing is used to determine whether a piece of software satisfies all of the requirements from the business or user's perspective. Does this piece of software do what it needs to do? These tests are sometimes built against the original specification.

Because research software is typically written by the researcher that will use it (or at least with significant input from them) acceptance tests may not be necessary.
