(rr-security)=
# Secure Software Development Practices

## Summary

Software security has various aspects that touch upon all parts of software development.
This guide intents to raise awareness of security concerns in data science and 
research software applications, and to provide practical guidelines to cover common security threats.

The audience of these instructions are research software engineers without particular security expertise.
This guide will allow them to conceptually understand different types of risks and to enable best practices to avoid the most common caveats.

```{warning}
Written by research software developers rather than security specialists, this section is designed to raise awareness of cybersecurity risks in research workflows.

Because every institutional infrastructure is unique, we strongly recommend consulting your local IT security team for tailored guidance that aligns with your organization's specific rules and policies.
```


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

(rr-security-principles)=

## Software Security Principles


These goals can be achieved by designing the software securely, and by
building/distributing it securely.

### Secure design


When designing an application from a security perspective,
the first question is to ask **what can go wrong**.
This activity is part of a design process called threat modeling. 

The threat model differs case by case. Here are some example use cases
and security aspects:

- An application with public data, few developers and users: What
happens if one of the developers' laptop is stolen? How does the team
minimize the risks from this?
- An application that handles sensitive data: How does the system
protect data from illegitimate requests from an insider---an
administrator, analyst or developer? Do they all need access 
to the entire data system?
- An application with many contributors where not everyone knows each other:
How does the development process protect from an adversarial
developer that aims to steal others' credentials?
- An application that is distributed to hundreds of users: How does
the application protect from an attacker that uses the application to
infiltrate users' systems?
- An application that is exposed to the internet on a server: [Web Server Setup](#rr-webserver).

Depending on what can go wrong, one needs to define **what to 
do about it**. Incorporating this early in the design process
ensures that security is not an afterthought.
When designing the security of an application, it is useful to
be aware of, and follow, security principles such as [4, 5]:

#### No security guarantee

No application or system is guaranteed to be protected from all attacks.
The goal of security is to make an attack as unattractive
as possible, by increasing the hurdles for a successful attack,
and by minimizing the reward of an attack. 
Since it applies to all software, the principle also 
matters for [managing dependencies](#managing-dependencies).

#### Least privilege and separation of duties

Least privilege means that users should only be given access to the 
resources they need for doing their job.
Separation of duties means that tasks and responsibilities are distributed
across different roles, so that no single person has access to everything.

Examples:
- In a shared file system such as an HPC cluster, 
implement access controls so that users can only read/modify/execute 
files per their needs.
- Use role-based
database access so that developers, users and administrators only 
see the data they need to see.


#### Defense-in-depth

This reduces the risk of a successful attack by securing a system across
different layers: if one layer
fails, other layers still stand and protect the asset. The layers of security
can be network security, application security, and data security.

Example:
- To protect a data system, application security can come from
requiring authentication to log in to the system. Data security can come 
from role-based access and/or from encrypting/hashing sensitive columns
such as person names. 

#### Zero trust

This principle assumes that all users, devices, and networks are untrusted
and must be verified before access is granted. This includes data provided 
by users.

Example:
- When exposing a database to user queries, the user inputs need to be validated
and queries parameterized. This prevents from [injection attacks](https://en.wikipedia.org/wiki/Code_injection)
where the user can exfiltrate data they are not supposed to see, or change data they are not 
supposed to change.


### Secure implementation

Implementation concerns building and deploying the software as well as 
managing the defects.

#### Documentation

Software development teams should have good documentation about
security techniques, tools and threats. This increases
awareness for all contributors and helps following
good practices.

In cases where users interact in public with developers---such as
by opening issues on GitHub---, a security policy can be added to the 
repository. The policy gives instructions on how to report a security
vulnerability, avoiding a public report [6], and thus reducing the risk 
that the report is exploited by an attacker.

In 2026, GitHub has added an experimental [feature for private vulnerability reports](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
These are enabled per repository and allow a user to report a security-related issue to the repository maintainers.


#### Managing dependencies

Tracking dependencies is important also from a security point of view 
because they can be an entry point for an attacker:

- If a dependency has a vulnerability, all users are potentially
exposed to it. 
- In contrast to vulnerabilities, supply chain attacks are 
deliberate attempts to inject malicious code and distribute it through
popular libraries. 
    - For example, in an incident from 2026, the `lite-llm` package contained code that
extracts secrets such as passwords whenever Python is called.
- Developer tools such as editor extensions or plugins are also dependencies,
and pose a threat to the security of the developer's machine.

Not only code and software, but also machine learning models
are dependencies and can represent a threat. For instance, using the `pickle`
module in Python to store and distribute machine learning model weights is vulnerable
to arbitrary code execution. This is why the [`safetensors`](https://huggingface.co/docs/safetensors/index) format was
introduced and should be used.

**Reducing dependency risks**

A few rules help reduce risks from dependencies:

- Choose dependencies carefully -- this is about trade-offs:
    - On the one hand, don't reinvent the wheel -- existing frameworks and tools, especially
    those implementing core security features, are likely
    more secure because they have been hardened "in the wild".
    - On the other hand, do not add dependencies that are obscure or 
    provide trivial functionality.
- Keep dependencies up to date. 
    - This ensures users receive vulnerability
fixes from dependencies.
    - To reduce exposure to supply chain attacks, consider reducing 
    immediate upgrades to new versions: For instance, `uv` allows for 
    specifying a time lag (e.g. 1 week) for upgrading dependencies in deployed software ([dependency cooldowns](https://docs.astral.sh/uv/concepts/resolution/#dependency-cooldowns)). 
    This gives maintainers of dependencies time to react.
- Run vulnerability scans for dependencies.
    - [GitHub Dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart) for generic dependency checks.
    - [OWASP dependency check for web applications](https://devguide.owasp.org/en/05-implementation/02-dependencies/01-dependency-check/).
    - Python dependency checks: [`pip-audit`](https://github.com/pypa/pip-audit) 
      and [`uv audit`](https://docs.astral.sh/uv/reference/cli/#uv-audit).
- Run security scans for files.
    - Example: [clamscan](https://docs.clamav.net/manual/Usage/Scanning.html)


## Application Areas

The security principles can be applied to application areas such as:

1. [Secure development](#rr-secure-development)
2. [Secure deployment](#rr-secure-deployment)
1. [Web server security](#rr-webserver)

~~5. Privacy -> https://book.the-turing-way.org/project-design/data-security/sdpm/data-privacy-strategies/#pd-sdpm-privacy-minimisation~~


## Security aspects covered elsewhere in the _Turing Way_

Beyond the topics mentioned so far, security is also mentioned 
in other sections of the book, including:

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


## Further Reading

1. OWASP Foundation, "OWASP Application Security Verification Standard 5.0.0," Open Web Application Security Project, v5.0.0, 2023. [Online]. Available: https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf
2. OWASP Foundation. "OWASP Developer Guide". [Online]. Available: https://devguide.owasp.org/.
3. OWASP Foundation. "Secure Design". https://devguide.owasp.org/en/04-design/
4. OWASP Foundation. "Principles of security". https://devguide.owasp.org/en/02-foundations/03-security-principles/
5. OWASP Foundation. "Secure Product Design Cheat Sheet". https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet
6. GitHub. Adding a security policy to your repository. https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy
