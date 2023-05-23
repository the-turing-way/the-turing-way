# Checklist for Code Testing

This checklist contains a lot of items.
As {ref}`mentioned before<rr-testing-write-tests>`, it is far better to do some of the items than none of them.
Do not be discouraged if this list of tasks seems insurmountable.

<a name="Writing_tests"></a>
## Writing tests

- Write a few smoke tests.
- Write unit tests for all your code units.
- Write integration tests to check the integration between units.
- Write a few system tests. Prioritise common and important paths through the program.
- Write regression tests. Regression tests can exist at any level of testing.
- If appropriate for your project write acceptance tests.
- Add runtime tests into your project.

<a name="Good_practice_checks"></a>
## Good practice checks

- Document the tests and how to run them.
  - Write scripts to set up and configure any resources that are needed to run the tests.
- Pick and make use of a testing framework.
- Run the tests regularly.
  - Automate the process of running tests. Consider making use of continuous integration (see continuous integration chapter) to do this.
- Check the code coverage of your tests and try to improve it.
- Engage in code review with a partner.
