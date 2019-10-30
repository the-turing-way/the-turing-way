# Reviewing

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| [Version control](/version_control/version_control) | Necessary | Understanding the way that [Github](https://github.com) arranges its branches, forks, and pull requests within repositories is needed. |

<a name="Summary"></a>
## Summary

Code review provides an additional way of testing code quality. Instead of relying simply on [tests](/testing/testing) which the original author puts together themselves, code review gets another programmer to look over the new code and assess it. The goal is to point out strengths and also potential areas of improvement.

Code review is often done in pairs, with each reviewer also having some of their code reviewed by their partner. Doing this can help programmers to see and discuss issues and alternative approaches to tasks, and to learn new tips and tricks. This also means code review practices are particularly well-suited to projects with more than one contributor making changes, where each is working on different parts of the code. Nonetheless, even the smallest scale projects can harness these approaches with some creative project management.

Because of their nature code reviews act a qualitative rather than quantitive tests, but are no less valuable for that.

This section will provide an overview of rationales, best practice, and some possible workflows for code review. Some details refer specifically to github's code review functionality as a powerful and widely-used example of a formal code review system; however, equivalent and very similar systems are available elsewhere (for example, [Gitlab](https://about.gitlab.com)), and even informal code review practices can also be very beneficial to a project.
