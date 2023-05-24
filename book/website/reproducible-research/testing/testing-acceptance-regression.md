(rr-testing-acceptance-regression)=
# Acceptance and Regression Testing

(rr-testing-acceptance)=
## Acceptance testing

Acceptance tests are one of the last tests types that are performed on software prior to delivery.
Acceptance testing is used to determine whether a piece of software satisfies all of the requirements from the business or user's perspective.
Does this piece of software do what it needs to do?
These tests are sometimes built against the original specification.

Because research software is typically written by the researcher that will use it (or at least with significant input from them) acceptance tests may not be necessary.

(rr-testing-regression)=
## Regression testing

Regression testing is a style of testing that focuses on retesting after changes are made.
The results of tests after the changes are compared to the results before, and errors are raised if these are different.
Regression testing is intended to ensure that changes (enhancements or defect fixes) to the software have not adversely affected it.
The likelihood of any code change impacting functionalities that are not directly associated with the code is always there and it is essential that regression testing is conducted to make sure that fixing one thing has not broken another.
Regression testing can be performed during any level of testing (unit, integration, system, or acceptance) but it is mostly relevant during system testing.
Any test can be reused, and so any test can become a regression test.

Regression testing is obviously especially important in team working, but it is surprisingly easy to break your own code without noticing it, even if you are working on your own.
And because regression testing is next to impossible to do satisfactorily by hand (it's simply too tedious), it's an obvious case for automation.

Regression tests are written by first running the (or part of the) code for given inputs and recording the outputs.
This could be done by writing input files and saving the corresponding output files.
These outputs serve as the expected outputs from the program given the corresponding inputs.
Regression tests are then written.
Each regression test runs the code for the set of inputs.
It then compares the output from the code to the expected outputs, and raises an error if these do not match.

Regression testing approaches differ in their focus.

Common examples include:
- Bug regression: We retest a specific bug that has been allegedly fixed.
- Old fix regression testing: We retest several old bugs that were fixed, to see if they are back. (This is the classical notion of regression: the program has regressed to a bad state.)
- General functional regression: We retest the project broadly, including areas that worked before, to see whether more recent changes have destabilized working code.
- Conversion or port testing: The program is ported to a new platform and a regression test suite is run to determine whether the port was successful.
- Configuration testing: The program is run with a new device or on a new version of the operating system or in conjunction with a new application.
This is like port testing except that the underlying code hasn't been changed--only the external components that the software under test must interact with.

### Limitations of Regression Testing

Regression tests are not guaranteed to test all parts of the code.
Most importantly, regression tests do not test if the result outputted by a piece of code is *correct*, only that it has not changed.
This the remit of other kinds of tests, though regression tests can serve as the starting point for introducing tests for correctness, by both the use of analytical solutions, and through test functions which read output files and check the data for correctness, as defined by a researcher.
