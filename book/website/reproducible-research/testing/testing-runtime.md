(rr-testing-runtime)=
# Runtime testing

Runtime tests are tests that run as part of the program itself.
They may take the form of checks within the code, as shown below:
```
population = population + people_born - people_died

// test that the population is positive
if (population < 0):
  error( 'The number of people can never be negative' )
```

Another example of a use of runtime tests is internal checks within functions that verify that their inputs and outputs are valid, as shown below:
```
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
- Catching problems early also helps prevent them escalating into catastrophic failures. It minimises the blast radius.

Disadvantages of runtime testing:

- Tests can slow down the program.
- What is the right thing to do if an error is detected? How should this error be reported? Exceptions are a recommended route to go with this.
