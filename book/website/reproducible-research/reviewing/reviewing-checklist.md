(rr-checklist-for-code-review)=
# Checklist for code review process

This section presents some checklists for both the coder and the reviewer, as part of a formal review process.
The reviewer checklists are split into two categories: one for the whole program, and one for individual files or proposed changes.

The lists are created with a focus on good software engineering practice and are intended to be a source of inspiration.
When assessing the checklists, it is recommended to consider to what extent the item mentioned is implemented.
Some items on the lists may not apply to your project or programming language, in which case they should be disregarded.

In all cases, the goal is to use your programming experience to figure out how to make the code better.

## For the coder

- Does the new code meet the required standards of the project?
  The standards are typically written under `contributing guidelines` by the project you are contributing to.
- Is there [documentation](#documentation) that meets the required standards of the project?
- Are you following any declared {ref}`style guide<rr-code-quality>` for the project?
- Are there new [tests](#tests) for the new material, based on the required standards of the project?
  - Do these tests pass locally?
  - Are the tests in the rest of the code base still passing locally?
- Create the pull request.
- Many {ref}`continuous integration (CI)<rr-ci>` systems will check if the tests in the main project pass automatically once you create a pull request.
  If the repository is using a CI, make sure all builds and tests complete.
  Consult the CI reports to see if your code is causing the tests in the main project to fail.
- If necessary, now formally request a review.

## For the reviewer

- Check the required standards of the project. The standards are typically written under
`contributing guidelines` by the project you are contributing to.
- Check the code meets basic project {ref}`style guide<rr-code-quality>`, if this is not automatically checked by {ref}`continuous integration (CI)<rr-ci>`.
- Do the [tests](#tests) and [documentation](#documentation) conform to the standards?
- Is all the code easily understood? Depending on the language, files may contain interfaces, classes or other type definitions, and functions (see [Architecture](#architecture)).
    The essential architectural concepts can be reviewed as follows:
  - Check the [interfaces](#interfaces) lists.
  - Check the [classes and types](#classes-and-types) lists.
  - Check the [function/method declarations](#functionmethod-declarations) lists.
  - Check the [function/method definitions](#functionmethod-definitions) lists.
- Do the [tests](#tests) actually ensure the code is robust in its intended use?
  - Are there any bugs or other defects?
- Are [security](#security) issues handled correctly?
  - Check the [security of new code](#security-of-new-codes).
- Does the new code meet the [legal requirements](#legal)?

## Program level checklist

Here is a list of things to consider when looking at the program as a whole,
rather than when looking at an individual file or change.

### Documentation

Documentation is a prerequisite for using, developing, and reviewing the program.
Someone who isn’t involved with your project should understand what your code does,
and what approach you’re taking. Here are some things to check for.

- Is there a description of the purpose of the program or library?
- Are detailed requirements listed?
- Are requirements ranked according to [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method)?
- Is the use and function of third-party libraries documented?
- Is the structure/architecture of the program documented? (see below)
- Is there an installation manual?
- Is there a user manual?
- Is there documentation on how to contribute?
  - Including how to submit changes
  - Including how to document your changes

### Architecture

These items are mainly important for larger programs, but may still be good
to consider for small ones as well.

- Is the program split up into clearly separated modules?
- Are these modules as small as they can be?
- Is there a clear, hierarchical or layered, dependency structure between
  these modules?
  - If not, the functionality should be rearranged, or perhaps heavily
    interdependent modules should be combined.
- Can the design be simplified?

### Security

If you're making software that is accessible to the outside world (for example a web
application), then security becomes important. Security issues are defects,
but not all defects are security issues. A security-conscious design can help
mitigate the security impact of defects.

- Which modules deal with user input?
- Which modules generate output?
- Are input and output compartmentalized?
  - If not, consider making separate modules that manage all input
    and output, so validation can happen in one place.
- In which modules is untrusted data present?
  - The fewer the better.
- Is untrusted data compartmentalized?
  - Ideally, validate in the input module and pass only
    validated data to other parts.

### Legal

As a developer, you should pay attention to the legal rights of the
creators of the code you're using. Here are some things to check. When in
doubt, ask someone experienced in licensing for advice.

- Are the licenses of all modules/libraries that are used documented?
- Are the requirements set by those licenses fulfilled?
  - Are the licenses included where needed?
  - Are copyright statements included in the code where needed?
  - Are copyright statements included in the documentation where needed?
- Are the licenses of all the parts compatible with each other?
- Is the project license compatible with all libraries?

## File/Change level checklist

When you're checking individual changes or files in a pull request, the
code itself becomes the subject of scrutiny. Depending on the language, files
may contain interfaces, classes or other type definitions, and functions. All
these should be checked.

### Interfaces

- Is the interface documented?
- Does the concept it models make sense?
- Can it be split up further? (Interfaces should be as small as possible)

Note that most of the following items assume an object-oriented programming
style, which may not be relevant to the code you're looking at.

### Classes and types

- Is the class documented?
  - Are external programs needed by the class documented?
- Does it have a single responsibility? Can it be split?
- If it's designed to be extended, can it be?
- If it's not designed to be extended, is it protected against that?
- If it's derived from another class, can you substitute an object of this class for one of its parent class(es)?
- Is the class testable?
  - Are the dependencies clear and explicit?
  - Does it have a small number of dependencies?
  - Does it depend on interfaces, rather than on classes?

### Function/Method declarations

- Are there comments that describe the intent of the function or method?
- Are input and output documented? Including units?
- Are pre- and postconditions documented?
- Are edge cases and unusual things commented?

### Function/Method definitions

- Are edge cases and unusual things commented?
- Is there any incomplete code?
- Could this function be split up (is it not too long)?
- Does it work? Perform intended function, logic correct, ...
- Is it easy to understand?
- Is there redundant or duplicate code? (DRY)
- Do loops have a set length and do they terminate correctly?
- Can debugging or logging code be removed?
- Can any of the code be replaced by library functions?

### Security of new codes

- If you're using a library, do you check errors it returns?
- Are all data inputs checked?
- Are output values checked and encoded properly?
- Are invalid parameters handled correctly?

### Tests

- Do unit tests actually test what they are supposed to?
- Is bounds checking being done?
- Is a test framework and/or library used?
