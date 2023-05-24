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

Code review is often done in pairs, with each reviewer also having some of their code reviewed by their partner.
Doing this can help programmers to see and discuss issues and alternative approaches to tasks, and to learn new tips and tricks.
This also means code review practices are particularly well-suited to projects with more than one contributor making changes, where each is working on different parts of the code.
Nonetheless, even the smallest scale projects can harness these approaches with some creative project management.

Because of their nature, code reviews act as qualitative - rather than quantitative - tests but are no less valuable for that.

This section will provide an overview of rationales, best practices, and some possible workflows for code review.
Some details refer specifically to GitHub's code review functionality as a powerful and widely-used example of a formal code review system; however, equivalent and very similar systems are available elsewhere (for example, [GitLab](https://about.gitlab.com)), and even informal code review practices can also be very beneficial to a project.
