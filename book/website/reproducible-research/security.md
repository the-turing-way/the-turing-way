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
4. Integrity: Use commit signing for code repositories
5. Authorization: Protect development and deployment environments. 
    - Examples: Use 2FA on GitHub accounts; use trusted publishing in CD
6. Confidentiality: Protect from injections by untrusted sources
    - SQL injection attacks on databases
    - Prompt injection attacks in LLMs

## Links to other chapters

Beyond the topics mentioned so far, you can find related security mentions in other sections of the book, including:

### Institutional Compliance & Project Design
Topics that cover the foundational steps taken before code is written, ensuring alignment 
with institutional policies and ethical standards. 
1. {ref}`Privacy and Security in Research Ethics Committees<er-committees>`
2. {ref}`Data Security and Project Planning<pd-sdp>` 

### Sensitive Data and use of Third-party platforms/Services

Topics focusing on securing the inputs of your research, tracking data gathering responsibly, 
and keeping sensitive files safe. 

1. {ref}`Electronic Lab Notebooks (ELNs)<rr-rdm-elns>` section mentions security concerns around ELNs. 
2. {ref}`Keeping Sensitive Files Secure<pd-sdpw-sensitive-files>`, for instance, by preventing .env, passwords or API tokens from being committed to public repositories

It is essential to understand the security implications of the third-party platforms and services 
used in your research software workflows. For instance, the University of Sheffield provides an 
excellent example of this with their security guidelines for GitHub Organizations [(RSE Sheffield Infrastructure Guidelines)](https://rse.shef.ac.uk/blog/2026-01-30-github-organisations/). Check if your organization has similar guidelines. 


### Secure Code Development & Quality Assurance

Topics covering the active development phase, where code quality, input/output sanitation, 
and configuration formats are strictly evaluated. 

1. Code Quality chapter specifically mentions {ref}`Static Code Analysis <rr-code-quality>`
2. Example of code execution vulnerabilities is given by {ref}`YAML Security Issues <rr-renv-yaml-security>`
3. Checklist for the Code Review Process mentions {ref}`Security of New Code<rr-checklist-for-code-review-security-new-code>`

### Infrastructure, Deployment & Environments

Topics around the execution layer, ensuring that where your code runs 
(containers, networks, domains) is isolated and secure from outside manipulation:

1. {ref}`Security in Containers (Docker, Singularity/Apptainer)<rr-renv-containers-rootlesspodman>`
2. {ref}`SSL certificates<ch-infrastructure-dns>`

## Further Reading

1. OWASP Foundation, "OWASP Application Security Verification Standard 5.0.0," Open Web Application Security Project, v5.0.0, 2023. [Online]. Available: https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf
2. OWASP Foundation. "OWASP Developer Guide". [Online]. Available: https://devguide.owasp.org/.
1.
1.
