(rr-testing-overview)=
# Overview of Testing Types

There are a number of different kinds of tests, which will be discussed here.

Firstly there are positive tests and negative tests.
Positive tests check that something works, for example testing that a function that multiplies some numbers together outputs the correct answer.
Negative tests check that something generates an error when it should.
For example nothing can go quicker than the speed of light, so a plasma physics simulation code may contain a test that an error is outputted if there are any particles faster than this, as it indicates there is a deeper problem in the code.

In addition to these two kinds of tests, there are also different levels of tests which test different aspects of a project.
These levels are outlined below and both positive and negative tests can be present at any of these levels.
A thorough test suite will contain tests at all of these levels (though some levels will need very few).

(rr-testing-types-of-testing)=
## Types of Testing

[][rr-testing-smoketest]: Very brief initial checks that ensures the basic requirements required to run the project hold.
If these fail there is no point proceeding to additional levels of testing until they are fixed.

[][rr-testing-unittest]: A level of the software testing process where individual units of a software are tested. The purpose is to validate that each unit of the software performs as designed.

[][rr-testing-types-integrationtest]: A level of software testing where individual units are combined and tested as a group.
The purpose of this level of testing is to expose faults in the interaction between integrated units.

[][rr-testing-systemtest]: A level of the software testing process where a complete, integrated system is tested.
The purpose of this test is to evaluate whether the system as a whole gives the correct outputs for given inputs.

[][rr-testing-acceptance-regression]: A level of the software testing process where a system is tested for acceptability.
The purpose of this test is to evaluate the system's compliance with the project requirements and assess whether it is acceptable for the purpose.

Here's an analogy: during the process of manufacturing a ballpoint pen, the cap, the body, the tail, the ink cartridge and the ballpoint are produced separately and unit tested separately.
When two or more units are ready, they are assembled and integration testing is performed, for example a test to check the cap fits on the body.
When the complete pen is integrated, system testing is performed to check it can be used to write like any pen should.
Acceptance testing could be a check to ensure the pen is the colour the customer ordered.

There is also another kind of testing called regression testing.
Regression testing is a type of testing that can be performed at any of the four main levels and compares the results of tests before and after a change is made to the code, and gives an error if these are different.

These different types of tests are discussed in more detail in the next subchapters.
