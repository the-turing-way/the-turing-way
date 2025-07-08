(rr-testing-types-integrationtest)=
# Integration Testing

Integration testing is a level of software testing where individual units are combined and tested as a group.
While unit tests validate the functionality of code in isolation, integration tests ensure that components cooperate when interfacing with one another.
The purpose of this level of testing is to expose faults in the interaction between integrated units.

For example, maybe a unit that reads in some data is working and passes its unit tests, and the following unit that cleans up the data once it's been read in is also working and passes its tests.
However say the first unit outputs the data as (time_data, temperature_data) but the function that cleans the data expects input of the form (temperature_data, time_data).
This can obviously lead to bugs.
While the units are correct there in an error in their integration.

An example of an integration test for this case could be to supply a test data file, use these functions to read it in and clean it, and check the resulting cleaned data against what would be expected.
If a bug like this is present then the cleaned data outputted would be very unlikely to match the expected result, and an error would be raised.

Integration testing is particularly important in collaborative projects where different people work on different parts of the code.
If two different people complete separate units and then need to integrate them integration issues are more likely as neither may understand the other's code.
A famous example of this is a multi-million dollar satellite which [crashed](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) because one piece of code outputted distance data in feet, while another assumed data in meters.
This is another example of an integration issue.

A sub-type of integration testing is system integration testing.
This tests the integration of systems, packages and any interfaces to external organizations (such as Electronic Data Interchange, Internet).
Depending on the nature of a project system integration testing may or may not be applicable.

## Integration Testing Approaches

There are several different approaches to integration testing.
Big Bang is an approach to integration testing where all or most of the units are combined together and tested at one go.
This approach is taken when the testing team receives the entire software in a bundle.
So what is the difference between Big Bang integration testing and system testing? Well, the former tests only the interactions between the units while the latter tests the entire system.

Top Down is an approach to integration testing where top-level sections of the code (that themselves contain many smaller units) are tested first and lower level units are tested step by step after that.
So is a code can be split into the main steps A, B, and C, and each of those contain steps to complete them, and these steps may have substeps like:

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

So in the top down approach the integration between sections at the top level (A, B and C) are tested, then integration between sections at the next level (for example, A.1 -> A.2) and so on.
Testing upper level units by running all the code they contain including running lower level ones can lead to upper level tests breaking due to bugs in low level units.
This is undesirable, so to prevent this the lower level sections should not be run, but [test stubs][rr-testing-guidance-mocking] should be used to simulate the outputs from them.

Bottom Up is an approach to integration testing where integration between bottom level sections are tested first and upper-level sections step by step after that.
Again test stubs should be used, in this case to simulate inputs from higher level sections.

Sandwich/Hybrid is an approach to integration testing which is a combination of Top Down and Bottom Up approaches.

Which approach you should use will depend on which best suits the nature/structure of your project.

## Integration Testing Tips

- Ensure that you have a proper Detail Design document where interactions between each unit are clearly defined. It is difficult or impossible to perform integration testing without this information.
- Make sure that each unit is unit tested and fix any bugs before you start integration testing. If there is a bug in the individual units then the integration tests will almost certainly fail even if there is no error in how they are integrated.
- Use mocking/stubs where appropriate.
