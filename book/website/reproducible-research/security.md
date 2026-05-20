(rr-security)=
# Secure Software Development Practices

## Summary

Software security has various aspects that touch upon all parts of software development.
This guide intents to raise awareness of security concerns and to provide practical guidelines to cover common security threats.

The audience of these instructions are research software engineers without particular security expertise.
This guide will allow them to conceptually understand different types of risks and to enable best practices to avoid the most common caveats.

```{warning}
Written by research software developers rather than security specialists, this section is designed to raise awareness of cybersecurity risks in research workflows.

Because every institutional infrastructure is unique, we strongly recommend consulting your local IT security team for tailored guidance that aligns with your organization's specific rules and policies.
```


## Foundations

Security is about controlling information: who can interact when with it, and 
what they can do with it [2]. 

Security can be characterized by three closely related goals:
- *Confidentiality* protects data against unauthorized disclosure.
- *Integrity* protects data against unauthorized modification or assures that 
data are trustworthy.
- *Availability* protects services that provide access to data, such as through
load balancing.

The goals can be achieved through three action categories:
- *Authentication* confirms the identity of an entity that wants to interact with a 
secure system.
- *Authorization* specifies access rights to secure resources.
- *Auditing* tracks events in a system, answering the questions "Who did what, when
and how?"


## Outline


1. {ref}`Dependency Management <rr-security-dependencies>`
2. {ref}`Web Server Setup<rr-webserver>`
4. Server Security 
5. Third-party platforms and services
4. Integrity: Signing commits
5. Authorization: Protect development and deployment environments. 
    - Examples: Use 2FA on GitHub accounts; use trusted publishing in CD
6. Confidentiality: Protect from injections by untrusted sources
    - SQL injection attacks on databases
    - Prompt injection attacks in LLMs


### Third-party platforms and Services

It is essential to understand the security implications of the third-party platforms and services used in your research software workflows. For instance, the University of Sheffield provides an excellent example of this with their security guidelines for GitHub Organizations [(RSE Sheffield Infrastructure Guidelines)](https://rse.shef.ac.uk/blog/2026-01-30-github-organisations/). Check if your organization has similar guidelines. 

### Signing commits and tags

To verify that commits are from a trusted source, you can use GPG in `git`.
Read more about GPG here: https://en.wikipedia.org/wiki/GNU_Privacy_Guard

In git, you can sign individual commits, tags, and you can verify the signature
of tags by other people.

Read more about signing commits in the git documentation: https://git-scm.com/book/ms/v2/Git-Tools-Signing-Your-Work


## Further Reading

1. OWASP Foundation, "OWASP Application Security Verification Standard 5.0.0," Open Web Application Security Project, v5.0.0, 2023. [Online]. Available: https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf
2. OWASP Foundation. "OWASP Developer Guide". [Online]. Available: https://devguide.owasp.org/.
1.
1.
