<a name="Regression_testing"></a>
## Regression testing

Regression testing is a style of testing that focuses on retesting after changes are made. The results of tests after the changes are compared to the results before, and errors are raised if these are different. Regression testing is intended to ensure that changes (enhancements or defect fixes) to the software have not adversely affected it. The likelihood of any code change impacting functionalities that are not directly associated with the code is always there and it is essential that regression testing is conducted to make sure that fixing one thing has not broken another. Regression testing can be performed during any level of testing (unit, integration, system, or acceptance) but it is most relevant during system testing. Any test can be reused, and so any test can become a regression test.

Regression testing is obviously especially important in team working, but it is surprisingly easy to break your own code without noticing it, even if you are working on your own. And because regression testing is next to impossible to do satisfactorily by hand (it's simply too tedious), it's an obvious case for automation.

Regression tests are written by first running the (or part of the) code for given inputs and recording the outputs. This could be done by writing input files and saving the corresponding output files. These outputs serve as the expected outputs from the program given the corresponding inputs. Regression tests are then written. Each regression test runs the code for the set of inputs. It then compares the output from the code to the expected outputs and raises an error if these do not match.

Regression testing approaches differ in their focus. Common examples include:

- Bug regression: We retest a specific bug that has been allegedly fixed.
- Old fix regression testing: We retest several old bugs that were fixed, to see if they are back. (This is the classical notion of regression: the program has regressed to a bad state.)
- General functional regression: We retest the project broadly, including areas that worked before, to see whether more recent changes have destabilized working code.
- Conversion or port testing: The program is ported to a new platform and a regression test suite is run to determine whether the port was successful.
- Configuration testing: The program is run with a new device or on a new version of the operating system or in conjunction with a new application. This is like port testing except that the underlying code hasn't been changed--only the external components that the software under test must interact with.

<a name="Limitations"></a>
### Limitations

Regression tests are not guaranteed to test all parts of the code. Most importantly, regression tests do not test if the result outputted by a piece of code is *correct*, only that has not changed. This the remit of other kinds of tests, though regression tests can serve as the starting point for introducing tests for correctness, by both the use of analytical solutions and test functions which read output files and check the data for correctness, as defined by a researcher.

<a name="Runtime_testing"></a>
## Runtime testing

Runtime tests are tests that run as part of the program itself. They may take the form of checks within the code, as shown below:
```python
population = population + people_born - people_died

// test that the population is positive
if (population < 0):
  error( 'The number of people can never be negative' )
```

Another example of a use of runtime tests is internal checks within functions that verify that their inputs and outputs are valid, as shown below:
```python
function add_arrays( array1, array2 ):

  // test that the arrays have the same size
  if (array1.size() != array2.size()):
    error( 'The arrays have different sizes!' )

  output = array1 + array2

  if (output.size() != array1.size()):
    error( 'The output array has the wrong size!'' )

  return output
```

Advantages of runtime testing:

- Run within the program, so can catch problems caused by logic errors or edge cases.
- Makes it easier to find the cause of the bug by catching problems early.
- Catching problems early also helps prevent them from escalating into catastrophic failures. It minimises the blast radius.

Disadvantages of runtime testing:

- Tests can slow down the program.
- What is the right thing to do if an error is detected? How should this error be reported? Exceptions are a recommended route to go with this.

<a name="Test_driven_development"></a>
## Test driven development

One way of ensuring tests are not neglected in a project is to adopt test-driven development. This is an approach in which unit tests are written before the code. The tests thus describe a "contract" that the code is expected to comply with. This ensures that the code will be correct (as far as can be enforced by the testing contract) as written, and it provides a useful framework for thinking about how the code should be designed, what interfaces it should provide, and how its algorithms might work. This can be a very satisfying mental aid in developing tricky algorithms.

Once the tests are written, the code is developed so that it passes all the associated tests. Testing the code from the outset ensures that your code is always in a releasable state (as long as it passes the tests!). Test-driven development forces you to break up your code into small discrete units, to make it easier to test; the code must be modular. The benefits of this were discussed in the section on [unit testing](#Unit_tests).

An alternative development approach is a behaviour-driven development. Simply put test-driven development tests "has the thing been done correctly?", behaviour driven development tests "has the correct thing been done?". It is more often used in commercial software development to focus development on making the software as simple and effective as possible for users. User experience is very rarely at the heart of code written for the purposes of research, but there are cases where such software is written with a large user-base in mind. In such cases, behaviour-driven development is a path worth considering.
