(rr-testing-driven-development)=
# Test Driven Development

One way of ensuring tests are not neglected in a project is to adopt test-driven development.
This is an approach in which unit tests are written before the code.
The tests thus describe a "contract" that the code is expected to comply with.
This ensures that the code will be correct (as far as can be enforced by the testing contract) as written, and it provides a useful framework for thinking about how the code should be designed, what interfaces it should provide, and how its algorithms might work.
This can be a very satisfying mental aid in developing tricky algorithms.

Once the tests are written, the code is developed so that it passes all the associated tests.
Testing the code from the outset ensures that your code is always in a releasable state (as long as it passes the tests!).
Test driven development forces you to break up your code into small discrete units, to make them easier to test; the code must be modular.
The benefits of this were discussed in the section on {ref}`unit testing<rr-testing-unittest>`.

An alternative development approach is behaviour driven development.
Simply put, under the test driven development paradigm, we check "has the thing been done correctly?", whereas under behaviour driven development we test "has the correct thing been done?".
It is more often used in commercial software development to focus development on making the software as simple and effective as possible for users.
User experience is very rarely at the heart of code written for the purposes of research, but there are cases where such software is written with a large user-base in mind.
In such cases behaviour-driven development is a path worth considering.
