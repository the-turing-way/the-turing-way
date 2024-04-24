(rr-reviewing)=
# Code Reviewing Process

(rr-reviewing-prerequisites)=
## Prerequisites

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| {ref}`Version Control<rr-vcs>` | Necessary | Understanding the way that [Github](https://github.com) arranges its branches, forks, and pull requests within repositories is needed. |

```{figure} ../figures/bug-catching.*
---
height: 500px
name: bug-catching
alt: People catching different insects in different ways - representing bugs in our code or project.
---
Catching bugs. _The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(rr-reviewing-summary)=
## Summary

Code review provides an additional way of testing code quality.
Instead of relying simply on {ref}`tests<rr-testing>` which the original author puts together themselves, code review gets another programmer to look over the new code and assess it. The goal is to point out strengths and also potential areas of improvement.

There are many variants of code review; the choice of approach forms part of the project culture. 
Common among them all is a goal to ensure code is seen by more than one developer before being introduced to the main branch.

Code review may be performed in pairs with each reviewer also having some of their code reviewed by their partner.
Or it may be asymmetrical with one code author and several reviewers, each contributing different ideas at different times.
Doing this can help programmers to see and discuss issues and alternative approaches to tasks, and to learn new tips and tricks.
This also means code review practices are particularly well-suited to projects with more than one contributor making changes, where each is working on different parts of the code.
Nonetheless, even the smallest scale projects can harness these approaches with some creative project management.
Code review is also critical for open source projects, which may have a core set of developers while also inviting contributions from others across the Internet with only an ephemeral relationship with the project.

Because of their nature, code reviews act as qualitative - rather than quantitative - tests but are no less valuable for that.

This section will provide an overview of rationales, best practices, and some possible workflows for code review.
Some details refer specifically to GitHub's code review functionality as a powerful and widely-used example of a formal code review system; however, equivalent and very similar systems are available elsewhere (for example, [GitLab](https://about.gitlab.com)), and even informal code review practices can also be very beneficial to a project.

## Differences in closed and open source code review

Code review dynamics are usually project-specific. 
They are both a product of, and a driver for, the culture of a project. 
There are also specific differences between the way closed and open source projects tend to operate.

Closed projects by their nature involve a defined group of contributors. In this case code review may be organised in a more central or defined manner, with pairs or groups of developers working together to review each others' code. It's also possible to arrange specialists to review different aspects of a change: design, security, API, accessibility and so on. Closed source or commercial projects may also be better placed to use more structured or "extreme" approaches such as pair programming.

In an open source environment contributions may be received from anyone at any time; there's no expectation that a particular contributor should have prior experience with the project. 
In this case, it's common for a core set of developers associated with a project to perform reviews. 
Even if reviews are not explicitly required, its typically the case that not everyone has commit rights to a project (the permissions to merge pull requests). 
A consequence of this is that those with merge rights must take on a reviewer role for the pull requests they merge.

