(rr-reviewing-motivation)=
# Importance and Personal Benefits

*How this will help you / why this is useful*

As with {ref}`testing<rr-testing>`, a key objective of code review is to remove mistakes and bad practice from changes made to a software project before those changes enter the main code base.
However, it also has a number of other direct and indirect benefits to projects. These are discussed below.

Code reviews are an effective method for improving software quality.
McConnell {cite:ps}`McConnell200testing` suggests that unit testing finds approximately 25% of defects, function testing 35%, integration testing 45%, and code review 55-60%.
While that means that none of these methods are good enough on their own, and that they should be combined, clearly code review is an essential quality control tool.

(rr-reviewing-motivation-bugs)=
## Catching Bugs and Elementary Errors

Although the evidence is mixed, a common opinion in the software engineering industry is that bugs become more costly (in terms of development effort) to fix the longer they're left unresolved {cite:ps}`Menzies2016defects,Westland2002errors`.
As a result, many of the tools in the software engineering toolbox are designed to find bugs earlier in the process.
Unit tests and continuous integration are examples of this, as is code review.

A simple objective of the review process is therefore to catch bugs and elementary errors in proposed changes before they make it into the trunk code.
In this way, code review shares aspects with testing.
However, a robust testing programme should reduce the importance of code review for identifying these kinds of straightforward errors, as the tests should catch them before the code makes it to review stage.
So in principle, this function of code review should be restricted to trivial changes like documentation typos. In practice, however, code review does act as an important second line of defence against all kinds of bugs and errors.

(rr-reviewing-motivation-improvements)=
## Improvements to Testing

As noted above, a review should, and often does, catch actual bugs in proposed code changes.
While this is one of the aims of code review, if bugs can be caught even earlier, through automated tests, that's an even better situation.

A major aim of code review is therefore to highlight places in the code where existing or newly developed testing processes are inadequate at identifying bugs.
In this way, code review helps to ensure the future health of the code base by providing a second perspective on what kinds of tests are needed - not only now, but also under hypothetical scenarios that could arise in the future as the code evolves.

Certain types of issue, such as those related to design, integration, readability and certain types of logic error, are less amenable to automated checks.
For these issues code review remains an important guard.

(rr-reviewing-motivation-documentation)=
## Documentation

<!--SiccarPoint notes a whole section on documentation is justified in the book!-->
Thorough documentation<!--reference goes here once section exists--> is a key component of reproducibility and of sustainable software more generally.
Code review provides another pair of eyes to consider whether the documentation provided along with the proposed code changes is fit-for-purpose.
This is doubly valuable, as the reviewer looking in from outside the development process may have a clearer perspective than the coder on whether new documentation offers enough information for a user coming to the code for the first time.

This kind of feedback on documentation applies equally to user-facing documentation and to inline comments.

(rr-reviewing-motivation-readability)=
## Readability

Related to documentation, code review can also help to ensure that code is readable and easy to understand. Having a second pair of eyes can help spot areas where the code might be difficult to follow.
The more readable your code is, the easier it will be for other developers to reproduce your code for their own purposes.

## Deployability

One of the most challenging tasks in software engineering is ensuring code can be successfully built and run across a range of different environments.
The operating system, package manager, window manager, existing dependencies, installed software, localisation and individual settings all contribute to the environment within which a piece of software runs.
There have been many attempts, from packaging to containerisation, to reproducible builds {cite:ps}`Builds2023reprobuilds` and reproducible build environments {cite:ps}`Choi2023reproenvs`, to constrain the environment in order to make deployment easier and more consistent.

It remains an unsolved problem.
For open source projects especially, having changes built and run in a mixture of different environments by different developers is therefore a valuable exercise.
Reviewers should aim to always build and run changes themselves.
This is a test for the robustness of the changes to different environments, robustness of the build system and also the documentation for setting things up.

(rr-reviewing-motivation-enforcement)=
## Style Enforcement

Many projects enforce certain {ref}`code style guidelines<rr-code-quality>`, be they widely-adopted standards (for example, [PEP8](https://www.python.org/dev/peps/pep-0008/), the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html)) or more project-specific conventions.
{ref}`Automated services<pd-code-styling-tools>` provide a convenient way to enforce a coding style and start the discussion about code quality.

While it is important to automate as many checks as possible, it is worth noting that for many projects the style requirements extend beyond those enforced through automated checks.
In practice there are often 'unwritten' rules built up through collective understanding of the developers involved.
Certain types of style choice may be hard to capture automatically, such as whether to use a more functional or imperative style, tolerance of complexity, or density of comments.

Code review offers an opportunity to reach consensus on styles that aren't written down or enforced deterministically, as well as helping identify how the written or automated coding conventions can be improved.

(rr-reviewing-motivation-knowledge)=
## Group Knowledge and Cohesion

Code review practices provide significant advantages beyond simply defending the health of the trunk code of a project when changes are proposed.
Peer-to-peer review creates two-way exchange of information across a web strung between all contributing members of a team. This provides effective, organic transfer of best practice.

Reviews conducted in the right spirit (see especially {ref}`here<rr-reviewing-recommendation-be-nice>`) also serve an important purpose in bringing team members together and creating group cohesion.
In particular, good reviews by core team members of the work of newcomers to a project can help make those newcomers feel welcomed and valued, and encourage their continued participation.

For some projects it may even make sense to have code review as a step in the onboarding process, having contributors perform a certain number of reviews before they are invited to contribute in other areas.



