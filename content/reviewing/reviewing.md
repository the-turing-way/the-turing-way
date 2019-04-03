# Reviewing

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| Version control | Necessary | Understanding the way that [Github](https://github.com) arranges its branches, forks, and pull requests within repositories is needed.  |

## Table of contents

1. [Summary](#Summary)
2. [How this will help you/ why this is useful](#How_this_will_help_you_why_this_is_useful)
    1. [Lorem ipsum(#lorem_ipsum)

XX. [Checklist](#Checklist)
    1. [Lorem ipsum](#lorem_ipsum)
    2. [Lorem ipsum](#lorem_ipsum)
XX. [What to learn next](#What_to_learn_next)
XX. [Further reading](#Further_reading)
XX. [Definitions/glossary](#Definitions_glossary)
XX. [Bibliography](#Bibliography)

<a name="Summary"></a>
## Summary

Code review provides an additional way of testing code quality. Instead of relying simply on [tests](#Testing) which the original author puts together themselves, code review gets another programmer to look over the new code and assess it. The goal is to point out strengths and also potential areas of improvement.

Code review is often done in pairs, with each reviewer also having some of their code reviewed by their partner. Doing this can help programmers see and discuss issues, alternative approaches to tasks, and learn tips and tricks. This means code review practices are particularly well-suited to larger scale projects with more than one contributor already attached to the project and working on different parts of the code. Nonetheless, even smaller scale teams can harness these aspects with some creative project management.

Because of their nature code reviews act a qualitative rather than quantitive tests, but are no less valuable for that.

<!-- check me later for accuracy!-->
This section will provide an overview of review workflows and best practice. Later sections will focus in particular on github's code review functionality as a powerful and widely-used example of a formal code review system; however, equivalent systems are available elsewhere (e.g., [Gitlab](https://about.gitlab.com)), and even informal code review practices can also be very powerful.

<a name="How_this_will_help_you_why_this_is_useful"></a>
## How this will help you/ why this is useful

As with [testing](#Testing), a key objective of code review is to remove mistakes and bad practice from changes made to a software project before those changes enter the main master code base. However, it also has a number of other direct and indirect benefits to projects. These are discussed below.

<a name="Catching_bugs_and_elementary_errors></a>"
### Catching bugs and elementary errors

A simple objective of the review process is to catch bugs and elementary errors in proposed changes before they make it into the code base. In this way, code review shares aspects with testing. However, a robust testing programme should in many cases in fact reduce the importance of review for identifying errors. In principle, this kind of error catching should be restricted to trivial changes like documentation typos. In practice, however, code review does act as this secondary line of defence against bugs and errors.

<a name="Improvements_to_testing></a>"
### Improvements to testing

As noted above, review should, and often does, catch actual bugs in proposed code changes. This, of course, is a sign that the proposed changes were not well-tested enough in the first place. A major aim of code review is to highlight places in the code where existing or newly developed testing processes are inadequate. In this way, code review helps to ensure the future health of the code base by providing a second perspective on what kinds of tests are needed not only now but under hypothetical scenarios that could arise in the future as the code evolves.

<a name="Documentation"></a>
###Documentation

<!--SiccarPoint notes a whole section on documentation is justified in the book!-->
Thorough documentation is a key component of reproducibility and of sustainable software more generally. Code review provides a second pair of eyes to consider whether the documentation provided along with the proposed code changes is fit-for-purpose. This is doubly valuable, as the reviewer looking in from outside the development process may have a clearer perspective on whether provided documentation offers enough information for a user coming to the code for the first time.

This kind of feedback on documentation applies equally to user-facing documentation and to inline comments.

<a name="Style_enforcement"></a>
### Style enforcement

Many projects enforce certain code style guidelines, be they widely-adopted standards (e.g., [PEP8](https://www.python.org/dev/peps/pep-0008/), the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html)) or more project-specific conventions. Code review provides an opportunity to ensure all proposed changes meet the minimum require standards for the project.

<a name="Group_knowledge_and_cohesion"></a>
### Group knowledge and cohesion

Code review practices provide significant advantages outwith simply defending the health of the trunk code for a project when changes are proposed. Code review creates two-way exchange of information across a web of knowledge between all contributing members of a team. This provides effective, organic transfer of best practice.

Reviews conducted in the right spirit (see especially [here](#Be_nice)) also serve an important purpose in bringing team members together and creating group cohesion. In particular, good reviews by core team members of the work of newcomers to a project can help make those newcomers feel welcomed and valued, and encourage their continued participation.

<a name="Best_practice"></a>
## Best practice

<a name="Be_nice"></a>
### Be nice!

Lorem ipsum.





< a name="Keep_it_collaborative"></a>
### Keep it collaborative
Unlike traditional, "academic-style" peer review, most code review systems have a number of advantages: they're rarely anonymous, they're public-facing, and without the middleman of an editor, interactions between reviewer and review-ee can be direct and rapid. This means code review is typically a flexible, dynamic, collaborative process. Good peer review will be fully collaborative, where once a potential query has been flagged by a reviewer, the two involved parties can work forward together to find a solution. It's also not atypical for third parties to chime in during the discussion strings that can grow under more gnarly review comments. This is all to the good.

< a name="Who_reviews"></a>
### Who reviews?

Individual large-scale development projects will likely have existing, concrete rules for how reviewers are allocated to individual pull requests. Within small-scale projects where the developers all typically already know each other, typical practice is for the coder to tag someone in the group who they feel will have enough knowledge of this part of the code to do a good job in a reasonable amount of time. In practice, the point of transition between these two models will become very obvious within a growing project - typically when core personnel start to complain about the uneven workload for reviewing they are under!

For projects where multiple rounds of review on similar material are likely and long development cycles are anticipated, a degree of strategic thinking on who completes reviews is sensible. A single reviewer is likely to be able to make comments on code they have reviewed before much more efficiently. However, letting reviewer-coder pairs like this ossify is generally a bad idea, as it can lead to the same kinds of groupthink that the review process is designed to avoid in the first place. Individual projects will tend to find this balance for themselves.




<a name="Typical_workflows_with_reference_to_github"></a>
## Typical workflows (with reference to Github)

<a name="Formal_vs_informal_reviews"></a>
### Formal vs informal reviews

This section focuses on the typical workflows behind a formal review process, typically as implemented within a social coding environment like Github. However, it bears stating that **all review of code is very valuable**, including informal or ad-hoc approaches. Indeed, this kind of informal "over the shoulder" peer review can form a key preliminary component even in highly formalised review pipelines, saving a lot of stress and arguing further down the line.

<a name="forks_and_branches"></a>
### Forks and branches

For a formal review process to work effectively, it's imperative that the project is using good [version control](#version_control). The review step occurs between the point where the coder believes their contribution is complete and that contribution being merged into the trunk code for the project, and so it is intimately associated with a pull request. Creation of the review and discussion between the reviewer and the coder occurs once the pull request is made and before it is merged into the master.

Within the Github environment, projects can be configured to require a review before a given pull request can be merged. If this option hasn't been selected, it's still possible to manually request a review on a pending PR.

### Prepare the code

<!--Discusses passing tests, initial style review, etc-->

### Create and discuss the review

### Make the changes

### Make the merge




<a name="Checklist"></a>
## Checklist

### Lorem ipsum

<a name="Good_practice_checks"></a>
### Good practice checks

- [ ] Lorem ipsum.
  - [ ] Lorem ipsum.


<a name="What_to_learn_next"></a>
## What to learn next

Lorem ipsum

<a name="Further_reading"></a>
## Further reading

Lorem ipsum

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


