## How this will help you/ why this is useful

As with [testing](#Testing), a key objective of code review is to remove mistakes and bad practice from changes made to a software project before those changes enter the master code base. However, it also has a number of other direct and indirect benefits to projects. These are discussed below.

<a name="Catching_bugs_and_elementary_errors"></a>
### Catching bugs and elementary errors

A simple objective of the review process is to catch bugs and elementary errors in proposed changes before they make it into the trunk code. In this way, code review shares aspects with testing. However, a robust testing programme should reduce the importance of code review for identifying these kinds of straightforward errors, as the tests should catch them before the code makes it to review stage. So in principle, this function of code review should be restricted to trivial changes like documentation typos. In practice, however, code review does act as an important second line of defence against all kinds of bugs and errors.

<a name="Improvements_to_testing"></a>
### Improvements to testing

As noted above, review should, and often does, catch actual bugs in proposed code changes. This, of course, is a sign that the proposed changes were not well-tested enough in the first place. A major aim of code review is to highlight places in the code where existing or newly developed testing processes are inadequate. In this way, code review helps to ensure the future health of the code base by providing a second perspective on what kinds of tests are needed - not only now, but also under hypothetical scenarios that could arise in the future as the code evolves.

<a name="Documentation"></a>
### Documentation

<!--SiccarPoint notes a whole section on documentation is justified in the book!-->
Thorough documentation<!--reference goes here once section exists--> is a key component of reproducibility and of sustainable software more generally. Code review provides another pair of eyes to consider whether the documentation provided along with the proposed code changes is fit-for-purpose. This is doubly valuable, as the reviewer looking in from outside the development process may have a clearer perspective than the coder on whether new documentation offers enough information for a user coming to the code for the first time.

This kind of feedback on documentation applies equally to user-facing documentation and to inline comments.

### Readability

Related to documentation, code review can also help to ensure that code is readable and easy to understand. Having a second pair of eyes can help spot areas where the code might be difficult to follow. The more readable your code is, the easier it will be for other developers to reproduce your code for their own purposes.


<a name="Style_enforcement"></a>
### Style enforcement

Many projects enforce certain [code style guidelines](../../code_quality/code_quality#coding-style), be they widely-adopted standards (for example, [PEP8](https://www.python.org/dev/peps/pep-0008/), the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html)) or more project-specific conventions. [Automated services](../../code_quality/code_quality#online-services-providing-software-quality-checks) provide a convenient way to enforce a coding style and start the discussion about code quality. Code review provides an opportunity to ensure all proposed changes meet the minimum require standards for the project.

<a name="Group_knowledge_and_cohesion"></a>
### Group knowledge and cohesion

Code review practices provide significant advantages outwith simply defending the health of the trunk code of a project when changes are proposed. Peer-to-peer review creates two-way exchange of information across a web strung between all contributing members of a team. This provides effective, organic transfer of best practice.

Reviews conducted in the right spirit (see especially [here](#Be_nice)) also serve an important purpose in bringing team members together and creating group cohesion. In particular, good reviews by core team members of the work of newcomers to a project can help make those newcomers feel welcomed and valued, and encourage their continued participation.
