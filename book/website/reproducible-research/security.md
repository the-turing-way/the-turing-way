(rr-security)=
# Secure Software Development Practices

## Summary

Software security has various aspects that touch upon all parts of software development.
This guide intents to raise awareness of security concerns in data science and 
research software applications, and to provide practical guidelines to address common security threats.

The audience of these instructions are research software engineers without particular security expertise.
This guide will allow them to conceptually understand different types of risks and to enable best practices to avoid the most common caveats.

```{warning}
Written by research software developers rather than security specialists, this section is designed to raise awareness of cybersecurity risks in research workflows.

Because every institutional infrastructure is unique, we strongly recommend consulting your local IT security team for tailored guidance that aligns with your organization's specific rules and policies.
```


## Application Areas

The security principles introduced on this page can be applied to:

1. [Secure development](#rr-secure-development)
2. [Secure deployment](#rr-secure-deployment)
1. [Web server security](#rr-webserver)

## Foundations

Security is about controlling information: who can interact when with it, and 
what they can do with it [2]. Security can be characterized by three closely related goals:
- *Confidentiality* protects data against unauthorized disclosure.
    - For instance, the personal data of survey participants must not be public.
    - As another example, software must prevent access to database.
- *Integrity* protects data against unauthorized modification or assures that 
data are trustworthy.
    - For instance, before a bank transfer is executed, it is important
    to validate that the receiver has not been manipulated.
- *Availability* protects services that provide access to data.
    - For instance, [denial-of-service-attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack) 
    reduce a server's uptime and thus its availability to users.

Modern computing systems, particularly cloud services, are highly complex and
rely on many interacting hardware and software components maintained by different 
organizations. As a result, individual users usually have only limited control 
over the overall security of these systems. Rather than attempting to make existing
systems more secure, users should focus on avoiding introducing vulnerabilities
or creating new attack paths.

(rr-security-principles)=

## Software Security Principles


These goals can be achieved by designing the software securely, and by
building/distributing it securely.

### Secure design


When designing software from a security perspective,
the first question is to ask **what can go wrong**.
This activity is part of a design process called threat modeling. 

The threat model differs case by case. Here are some example use cases
and security aspects:

- Software that uses only public data, few developers and users:
happens if one of the developers' laptop is stolen? How does the team
minimize the risks from this?
- Software that handles sensitive data: How does the system
protect data from illegitimate requests from an insider---an
administrator, analyst or developer? Do they all need access 
to the entire data system?
- Software with many contributors where not everyone knows each other:
How does the development process protect from an adversarial
developer that aims to steal others' credentials?
- Software that is distributed to hundreds of users: How does it protect from
an attacker that uses the software to infiltrate users' systems?
- An application that is exposed to the internet on a server: [Web Server Setup](#rr-webserver).
- Third-party software that is used during development
(interpreters, dependencies, IDE's and plugins, etc.): Are they obtained from
trusted sources? What level of access rights do they have on the user's system
and data? What happens if a tool is compromised? For further discussion
on dependencies, also see the [specific section](#rr-security-managing-dependencies).


Depending on what can go wrong, one needs to define **what to 
do about it**. Incorporating this early in the design process
ensures that security is not an afterthought.

For the secure design of software, it is useful to be aware of, and follow,
security principles such as [4, 5]:

#### No security guarantee

No application or system is guaranteed to be protected from all attacks.
The goal of security is to make an attack as unattractive
as possible, by increasing the hurdles for a successful attack,
and by minimizing the reward of an attack. 
This principle also 
matters for [managing dependencies](#rr-security-managing-dependencies).

#### Least privilege and separation of duties

Least privilege means that users should only be given access to the 
resources they need for doing their job.
Separation of duties means that tasks and responsibilities are distributed
across different roles, so that no single person has access to everything.

Examples:
- A team develops code that uses an API to collect information. 
Each team member uses their own API key that they store locally.
They make sure that they do not accidentally include their key in the shared codebase.
- In the spirit of Open Science, a team shares their code publicly via GitHub
repositories. Sensitive participant data is, however, only shared via 
institutionally approved services.
- In a system that collects sensitive personal data from a survey, use role-based 
database access so that developers, users and administrators only see
the data they need to see.

#### Defense-in-depth

Securing a system across different layers reduces the risk of a successful attack:
if one layer fails, other layers still stand and protect the asset. 

Example:
- To protect a data system, requiring users to log in gives one layer of protection.
Another layer comes from restricting which data a user can see, for instance
by restricting access to information on the person name.


#### Zero trust

This principle assumes that all users, devices, and networks are untrusted
and must be verified before they are processed further.

Example:
- When collecting survey data through a questionnaire, there is a risk that
an attacker enters malicious answers that allow them to extract data from the 
survey database. This can be avoided by sanitization techniques.


### Secure implementation

Implementation concerns building and deploying the software as well as 
managing the defects.

#### Documentation

Software development teams should discuss, agree upon, and, where appropriate, document threats, security techniques, and tools. This increases awareness among all contributors and helps them follow good practices.

For public codebases, a security policy can be added to the 
repository. The policy gives instructions on how to report a security
vulnerability to the developers confidentially instead of via a public report [6]. This reduces the risk 
that the vulnerability is exploited by an attacker.

In 2026, GitHub has added an experimental [feature for private vulnerability reports](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
These are enabled per repository and allow a user to report a security-related issue to the repository maintainers.


(rr-security-managing-dependencies)=
#### Managing dependencies

Tracking dependencies is important also from a security point of view 
because they can be an entry point for an attacker:

- If a dependency has a vulnerability, all users (including the developers) are potentially
exposed to it. 
- So-called *supply chain attacks* are deliberate attempts to inject malicious code into widely used packages. Attackers aim to introduce hidden vulnerabilities into valuable target systems that rely on the compromised dependencies.
    - For example, in an incident from 2026, the `lite-llm` package contained code that
extracts secrets such as passwords whenever Python is called.
- Developer tools such as editors or editor plugins can also be compromised and hence form a security risk for the security of the developer's machine and their data.

Not only code and software, but also machine learning models
are dependencies and can represent a threat. For instance, using the `pickle`
module in Python to store and distribute machine learning model weights is vulnerable
to arbitrary code execution. This is why the [`safetensors`](https://huggingface.co/docs/safetensors/index) format was
introduced and should be used.

**Reducing dependency risks**

A few rules help reduce risks from dependencies:

- Be conscious about _dependencies_ and _developer tools_ you choose to use -- it is about trade-offs:
    - On the one hand, don't reinvent the wheel -- there are myriads of great open source tools that are there for you to use. That means you do not need to build that functionality on your own!
    - Be careful with dependencies that only add trivial or obscure functionality.
- Prefer widely used existing frameworks and tools, especially those implementing core security features. They are likely more secure because they have been hardened "in the wild".
- Prefer software and packages that are still under active development and that don't rely on outdated dependencies.
- Be mindful of the number of dependencies that are used in your project, including the ones used by the dependencies on their own.
    - The more dependencies you use, the higher the chance that one of them might be compromised.
    - Consider checking for and removing dependencies that are no longer needed by your software.
- Keep dependencies up to date. 
    - This ensures that you and your users receive security
fixes from dependencies.
    - To reduce exposure to supply chain attacks, consider reducing 
    immediate upgrades to new versions: For instance, `uv` allows for 
    specifying a time lag (e.g. 1 week) for upgrading dependencies in deployed software ([dependency cooldowns](https://docs.astral.sh/uv/concepts/resolution/#dependency-cooldowns)). 
    This gives maintainers of dependencies time to react.
- Regularly run vulnerability scans for your dependencies.
    - [GitHub Dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart) for generic dependency checks.
    - [OWASP dependency check for web applications](https://devguide.owasp.org/en/05-implementation/02-dependencies/01-dependency-check/).
    - Python dependency checks: [`pip-audit`](https://github.com/pypa/pip-audit) 
      and [`uv audit`](https://docs.astral.sh/uv/reference/cli/#uv-audit).
- Run security scans for files.
    - Example: [clamscan](https://docs.clamav.net/manual/Usage/Scanning.html)




## Ethics & Data Privacy

The present section touches on ethics and data privacy from a perspective of software
design and development.
For more information on ethics and data privacy, check out these sections
- [](##er-intro)
- [](##er-social-data)
- [](##er-committees)
- [](##er-law-policy)
- [](##er-datahazardsintro)
- [](##er-ethics-open-source-governance)

### Institutional Compliance & Project Design
Topics that cover the foundational steps taken before code is written, ensuring alignment 
with institutional policies and ethical standards. 
1. {ref}`Privacy and Security in Research Ethics Committees<er-committees>`
2. {ref}`Data Security and Project Planning<pd-sdp>` 

### Data Privacy Strategies
The chapter {ref}`Data Privacy Strategies<pd-sdpm-privacy>` discusses specific 
strategies for keeping sensitive research data secure.




## Further Reading

1. OWASP Foundation, "OWASP Application Security Verification Standard 5.0.0," Open Web Application Security Project, v5.0.0, 2023. [Online]. Available: https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf
2. OWASP Foundation. "OWASP Developer Guide". [Online]. Available: https://devguide.owasp.org/.
3. OWASP Foundation. "Secure Design". https://devguide.owasp.org/en/04-design/
4. OWASP Foundation. "Principles of security". https://devguide.owasp.org/en/02-foundations/03-security-principles/
5. OWASP Foundation. "Secure Product Design Cheat Sheet". https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet
6. GitHub. Adding a security policy to your repository. https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy
7. PyPI has completed its second audit. https://blog.pypi.org/posts/2026-04-16-pypi-completes-second-audit/
8. CRAN. CRAN Repository Policy. https://cran.r-project.org/web/packages/policies.html
