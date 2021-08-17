(rr-testing-systemtest)=
# System Testing

Once integration tests are performed, another level of testing called system testing can begin.
System testing is a level of software testing where a complete and integrated software is tested.
The tester supplies the program with input and verifies if the program's output is correct.
If it is not then there is a problem somewhere in the system.
Note that this does not have to be done manually, it can be automated.
The purpose of these tests is to evaluate the system's compliance with the specified requirements.
In many ways, system testing acts as an extension to integration testing.
The focus of system tests are to make sure that groups of components function correctly as a cohesive whole.

However, instead of focusing on the interfaces between components, system tests typically evaluate the outward functionality of a full piece of software.
This set of tests ignores the constituent parts in order to gauge the composed software as a unified entity.
Because of this distinction, system tests usually focus on user- or externally-accessible outputs.

System testing can also test features of the system other than correctness.
Examples include:

- Performance testing: does the program performance meet the minimum requirements? A performance test may measure how long the system takes to run in a given case.
- Migration testing: does the program work when transferred to another computational environment?
- Stress/scale/load testing: testing how the program behaves when under stress, for example, when required to process very large volumes of data.
- Usability testing: how user-friendly the program is (more common in commercial software, tests typically conducted by humans rather than automated).
- Recovery testing: whether the program can continue if errors occur (again, more common in commercial software).

## System Testing Tips

System tests, also called end-to-end tests, run the program, well, from end to end.
As such these are the most time consuming tests to run.
Therefore you should only run these if all the lower-level tests (smoke, unit, integration) have already passed.
If they haven't, fix the issues they have detected first before wasting time running system tests.

Because of their time-consuming nature it will also often be impractical to have enough system tests to trace every possible route through a program, especially if there are a significant number of conditional statements.
Therefore you should consider the system test cases you run carefully and prioritise:

- The most common routes through a program.
- The most important routes for a program.
For example, the LIGO detector aims to find gravitational wave events, which are extremely rare.
If there's a bug in that path through the program which monitors the detector then it's a *huge* problem.
- Cases that are prone to breakage due to structural problems within the program.
Though ideally it's better to just fix those problems, but cases exist where this may not be feasible.

Because system tests can be time consuming it may be impractical to run them very regularly (such as multiple times a day after small changes in the code).
Therefore it can be a good idea to run them each night (and to automate this process) so that if errors are introduced that only system testing can detect the programmer will be made aware of them relatively quickly.
