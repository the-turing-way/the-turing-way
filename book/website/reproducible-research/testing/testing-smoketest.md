(rr-testing-smoketest)=
# Smoke Testing

Smoke tests (also known as build verification tests) are a special kind of initial checks designed to ensure very basic functionality as well as some basic implementation and environmental assumptions.
Smoke tests are generally run at the very start of each testing cycle as a sanity check before running a more complete test suite.

The idea behind this type of test is to help to catch big red flags in an implementation and to bring attention to problems that might indicate that further testing is either not possible or not worthwhile.
Normally, the tester is asking whether any components are so obviously or badly broken that the build is not worth testing or some components are broken in obvious ways that suggest a corrupt build or some critical fixes that are the primary intent of the new build didn't work.
Smoke tests are not very extensive, but should be extremely quick.
If a change to a project causes it to fail a smoke test, its an early signal that core assertions were broken and that you should not devote any more time to testing until the problem is resolved.
For example if a function that reads in the data a project requires to run is broken there's no point testing any further before that's fixed.
The typical result of a failed smoke test is rejection of the build (testing of the build stops) not just a new set of bug reports.
