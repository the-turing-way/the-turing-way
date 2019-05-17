# Reviewing

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| [Version control](/version_control/version_control) | Necessary | Understanding the way that [Github](https://github.com) arranges its branches, forks, and pull requests within repositories is needed. |

## Table of contents

1. [Summary](#Summary)
2. [How this will help you/ why this is useful](#How_this_will_help_you_why_this_is_useful)
    1. [Catching bugs and elementary errors](#Catching_bugs_and_elementary_errors)
    2. [Improvements to testing](#Improvements_to_testing)
    3. [Documentation](#Documentation)
    4. [Style enforcement](#Style_enforcement)
    5. [Group knowledge and cohesion](#Group_knowledge_and_cohesion)
3. [Best practice](#Best_practice)
    1. [Be nice!](#Be_nice)
    2. [Keep it collaborative](#Keep_it_collaborative)
    3. [Who reviews?](#Who_reviews)
4. [Typical workflows (with particular reference to Github)](#Typical_workflows_with_particular_reference_to_github)
    1. [Formal vs informal reviews](#Formal_vs_informal_reviews)
    2. [Forks and branches](#forks_and_branches)
    3. [Prepare the code](#prepare_the_code)
    4. [Create and discuss the review; make the changes](#create_discuss_change)
    5. [Make the merge](#make_the_merge)
5. [Checklists](#Checklists)
    1. [For the coder](#for_the_coder)
    2. [For the reviewer](#for_the_reviewer)
6. [What to learn next](#What_to_learn_next)
7. [Further reading](#Further_reading)
8. [Definitions/glossary](#Definitions_glossary)
9. [Bibliography](#Bibliography)

<a name="Summary"></a>
## Summary

Code review provides an additional way of testing code quality. Instead of relying simply on [tests](../testing/testing) which the original author puts together themselves, code review gets another programmer to look over the new code and assess it. The goal is to point out strengths and also potential areas of improvement.

Code review is often done in pairs, with each reviewer also having some of their code reviewed by their partner. Doing this can help programmers to see and discuss issues and alternative approaches to tasks, and to learn new tips and tricks. This also means code review practices are particularly well-suited to projects with more than one contributor making changes, where each is working on different parts of the code. Nonetheless, even the smallest scale projects can harness these approaches with some creative project management.

Because of their nature code reviews act a qualitative rather than quantitive tests, but are no less valuable for that.

This section will provide an overview of rationales, best practice, and some possible workflows for code review. Some details refer specifically to github's code review functionality as a powerful and widely-used example of a formal code review system; however, equivalent and very similar systems are available elsewhere (e.g., [Gitlab](https://about.gitlab.com)), and even informal code review practices can also be very beneficial to a project.

<a name="How_this_will_help_you_why_this_is_useful"></a>
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

<a name="Style_enforcement"></a>
### Style enforcement

Many projects enforce certain code style guidelines, be they widely-adopted standards (e.g., [PEP8](https://www.python.org/dev/peps/pep-0008/), the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html)) or more project-specific conventions. Code review provides an opportunity to ensure all proposed changes meet the minimum require standards for the project.

<a name="Group_knowledge_and_cohesion"></a>
### Group knowledge and cohesion

Code review practices provide significant advantages outwith simply defending the health of the trunk code of a project when changes are proposed. Peer-to-peer review creates two-way exchange of information across a web strung between all contributing members of a team. This provides effective, organic transfer of best practice.

Reviews conducted in the right spirit (see especially [here](#Be_nice)) also serve an important purpose in bringing team members together and creating group cohesion. In particular, good reviews by core team members of the work of newcomers to a project can help make those newcomers feel welcomed and valued, and encourage their continued participation.

<a name="Best_practice"></a>
## Best practice

<a name="Be_nice"></a>
### Be nice!

As with all open-source and collaborative enterprises, good internet etiquette makes the whole process go more smoothly. Perhaps most importantly, always assume good faith on both sides of the review interaction, and always be constructive. These principles are true for the review process beyond almost any other project aspect, since it necessarily involves criticism, potentially between two complete strangers. If you're the coder, don't waste your reviewer's time. If you're the reviewer, listen to what the coder is telling you in reply, and work collaboratively with them to make the code better.

<a name="Keep_it_collaborative"></a>
### Keep it collaborative
Unlike traditional, "academic-style" peer review, most code review systems have a number of advantages: they're rarely anonymous, they're public-facing, and without the middleman of an editor, contact between reviewer and review-ee can be direct and rapid. This means code review is typically a fast, flexible, and interactive process. Good peer review will be fully collaborative, where once a potential query has been flagged by a reviewer, the two involved parties can work forward together to find a solution. It's also not atypical for third parties to chime in during the discussion threads that can grow under more gnarly review comments, either voluntarily or by request. This is all to the good.

<a name="Who_reviews"></a>
### Who reviews?

Individual large-scale development projects will likely have existing, concrete rules for how reviewers are allocated to individual pull requests. These rules serve to balance the group workload and to maximise the various benefits of the process to the project and its participants. The very largest projects may even have dedicated staff - or teams of staff - to act as reviewers. In contrast, within small-scale projects where the developers all typically already know each other, typical practice is for the coder to tag someone in the group who they feel will have enough knowledge of this part of the code to do a good job in a reasonable amount of time. In practice, the point of transition between the structured and unstructured models will become very obvious within a growing project - typically when certain members of the core personnel start to complain about the uneven workload for reviewing they are under!

For projects where multiple rounds of review on similar material are likely and long development cycles are anticipated, a degree of strategic thinking on who completes reviews is sensible. A single reviewer is likely to be able to make comments on code they have reviewed before much more efficiently. However, letting reviewer-coder pairs like this ossify is generally a bad idea, as it can lead to the same kinds of groupthink that the review process is designed to avoid in the first place. Individual projects will tend to find this balance for themselves.

Typically, code reviews can only be performed by an authorised subset of contributors within larger projects.

<a name="Typical_workflows_with_particular_reference_to_github"></a>
## Typical workflows (with particular reference to Github)

<a name="Formal_vs_informal_reviews"></a>
### Formal vs informal reviews

This section focuses on the typical workflows behind a formal review process, as commonly implemented within a social coding environment like Github. However, it bears stating that **all review of code is very valuable**, including informal or ad-hoc approaches. Indeed, this kind of informal "over the shoulder" peer review can form a key preliminary component even in highly formalised review pipelines, saving a lot of stress and arguing once the formal stage begins.

<a name="forks_and_branches"></a>
### Forks and branches

For a formal review process to work effectively, it's imperative that the project is using good [version control](../version_control/version_control). The review step occurs between the points where the coder believes their contribution is complete and where that contribution is merged into the trunk code for the project, and so it is intimately associated with a single pull request. Creation of the review and discussion between the reviewer and the coder occurs once the pull request is made and before it is merged into the master. In the github system, the review is begun directly from and often accessed through the pull request page.

Within the Github environment, projects can be configured to *require* a review before a given pull request can be merged. Even if this option hasn't been selected, it's still possible (and indeed best practice) to manually request a review on a pending PR.

<a name="prepare_the_code"></a>
### Prepare the code

Before requesting a review, be sure you've met all the obvious quality benchmarks for the project you are contributing to. This means making sure:

- you have created [documentation](#Documentation) to the required standards of the project,
- you have [tested](#Improvements_to_testing) your code to the required standards of the project,
- your code is not causing the tests in the main project to fail (many [continuous integration](../continuous_integration/continuous_integration) systems will test this automatically for you once you create the PR), and
- you believe your code meets the declared [style guide](#Style_enforcement) for the project.

A reviewer should check these things, but defects on these fronts should be by occasional oversight, rather than systematic.

<a name="create_discuss_change"></a>
### Create and discuss the review; make the changes

At this point, the review process can begin. In Github, the reviewer can provide both general comments as well as line-by-line comments. Each comment becomes its own comment thread, permitting back-and-forth discussion about each issue as required. This interaction should allow consensus to be reached on every comment. In most cases, the reviewer has final say if a consensus cannot be found.

Once post-review changes have been made to the code, make final updates the comments as needed to complete a papertrail of what has been done and the reasoning behind it.

<a name="make_the_merge"></a>
### Make the merge

Once the review process is complete, the merge can occur. Individual projects typically have rules and/or guidelines for whether the coder or the reviewer actually presses the merge button, so check. In many cases, project workflows make completion of a review and its sign-off by the reviewer a formal precondition of performing the merge. For the avoidance of doubt, adopting this principle even for small or informal projects is probably sensible.


<a name="Checklists"></a>
## Checklists

The following presents some possible checklists for both the coder and the reviewer, as part of a formal review process.

<a name="for_the_coder"></a>
### For the coder

- [ ] Does the new code meet project standards? In particular,
  - [ ] Is there documentation?
  - [ ] Are there new tests for the new material?
  - [ ] Do these tests pass locally?
  - [ ] Are you following any declared style guides?
  - [ ] Are the tests in the rest of the code base still passing locally?
- [ ] Create the pull request; wait for any CI checks to complete.
- [ ] Consult the CI reports. Did all the builds and tests complete?
- [ ] If necessary, now formally request a review.
- [ ] Once review is complete, discuss any comments necessary.
- [ ] Make the changes, and record the changes made against appropriate comments.
- [ ] Check that the reviewer knows you believe you have fully addressed the review.

<a name="for_the_reviewer"></a>
### For the reviewer

- [ ] Check the code meets basic project style, if this is not automatically checked by CI.
- [ ] Check there are tests & documentation to necessary standards.
- [ ] Read the code, carefully.
  - [ ] Is it clear what all sections of the code do?
  - [ ] Are the logic and approach in the proposed changes clear?
  - [ ] Are the logic and the approach both sound?
  - [ ] Do the tests actually ensure the code is robust in its intended use?
  - [ ] Are there any bugs or other defects?
- [ ] As needed, engage constructively with the coder if they disagree on certain points in order to come to a consensus.
- [ ] Once the coder believes changes are complete, check that they do indeed address all of the initial comments.
- [ ] Approve the changes, and if it is your responsibility, make the merge.

<a name="What_to_learn_next"></a>
## What to learn next

The thorough checking of tests, coverage, and code style by hand can be tedious, so this might be a good time to learn more about [continuous integration (CI)](../continuous_integration/continuous_integration).

<a name="Further_reading"></a>
## Further reading

Lorem ipsum.

<a name="Definitions_glossary"></a>
## Definitions/glossary

- **Lorem ipsum:** Lorem ipsum.

<!--SiccarPoint is struggling to find Open License references for a lot of this (just closed). Help meeeeeeeeeee-->

<a name="Bibliography"></a>
## Bibliography

### Materials used: How this will help you/ why this is useful

- [Lorem ipsum]() **Licensing details here**

### Materials used: General guidance and good practice for reviewing

- [Lorem ipsum]() **Licensing details here**


