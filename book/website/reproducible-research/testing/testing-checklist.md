(testing-checklist)=
# Checklist for Code Testing

This checklist contains a lot of items.
As [mentioned before](#rr-testing-write-tests), it is far better to do some of the items than none of them.
Do not be discouraged if this list of tasks seems insurmountable.

(testing-checklist:writing-tests)=
## Writing tests

- Write a few {term}`smoke tests <smoke testing>`.
- Write {term}`unit tests <unit testing>` for all your code units.
- Write {term}`integration tests <integration testing>` to check the integration between units.
- Write a few {term}`system tests <system testing>`. Prioritise common and important paths through the program.
- Write {term}`regression tests <regression testing>`. Regression tests can exist at any level of testing.
- If appropriate for your project write {term}`acceptance tests <acceptance testing>`.
- Add {term}`runtime tests <runtime testing>` into your project.

(testing-checklist:good-practice-checks)=
## Good practice checks

- Document the tests and how to run them.
  - Write scripts to set up and configure any resources that are needed to run the tests.
- Pick and make use of a {term}`testing framework <testing framework>`.
- Run the tests regularly.
  - Automate the process of running tests. Consider making use of {term}`continuous integration <continuous integration>` (see continuous integration chapter) to do this.
- Check the code coverage of your tests and try to improve it.
- Engage in code review with a partner.

