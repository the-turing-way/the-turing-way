
(rr-security-principles)=

# Software Security Principles

## Secure design

When designing an application from a security perspective,
the first question is to ask **what can go wrong**.
This activity is part of a design process called threat modeling. 

The threat model differs case by case. Here are some example use cases
and security aspects:

- An application with public data, few developers and users: What
happens if one of the developers' laptop is stolen? How does the team
minimize the risks from this?
- An application that handles sensitive data: How does the system
protect data from the curious eyes of a stakeholder---an
administrator, analyst, or developer? Do they all need access 
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
follow security principles such as [2,3]:

### No security guarantee

No application or system is guaranteed to be protected from all attacks.
The goal of security is to make attacking a software as unattractive
as possible, by making it hard and reducing the rewards.
Since it applies to all software, the principle also 
matters for [managing dependencies](#managing-dependencies).

### Least privilege and separation of duties

Least privilege means that users should only be given access to the 
resources they need for doing their job.
Separation of duties means that tasks and responsibilities are distributed
across different roles, so that no single person has access to everything.

Examples:
- In a shared file system such as a HPC cluster, 
implement access controls so that users can only read/modify/execute 
files per their needs.
- Use role-based
database access so that developers, users and administrators only 
see the data they need to see.


### Defense-in-depth

This means that a system is secured across different layers: if one layer
fails, other layers still stand and protect the asset. The layers of security
can be network security, application security, and data security. Defense-in-depth
reduces the risk of a successful attack.

Example:
- To protect a data system, application security can come from
requiring authentication to log in to the system. Data security can come 
from role-based access and/or from encrypting/hashing sensitive columns
such as person names. 

### Zero trust

This principle assumes that all users, devices, and networks are untrusted
and must be verified before access is granted. This includes data provided 
by users.

Example:
- When exposing a database to user queries, the user inputs need to be validated
and queries parameterized. This prevents from [injection attacks](https://en.wikipedia.org/wiki/Code_injection)
where the user can exfiltrate data they are not supposed to see, or change data they are not 
supposed to change.


## Secure implementation

Implementation concerns building and deploying the software as well as 
managing the defects.

### Documentation

Software development teams should have good documentation about
security techniques, tools and threats. This increases
awareness for everyone in the development process and helps following
good practices.

In cases where users can interact in public with developers---such as
by opening issues on GitHub---, a security policy can be added to the 
repository. The policy gives instructions on how to report a security
vulnerability, avoiding a public report [4], and thus reducing the risk 
that the report is exploited by an attacker.

In 2026, GitHub has added an experimental [feature for private vulnerability reports](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
These are enabled per repository and allow a user to report a security-related issue to the repository maintainers.


### Managing dependencies

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

#### Reducing dependency risks
- Choose dependencies carefully.
    - This is about trade-offs:
    - On the one hand, don't reinvent the wheel -- existing frameworks and tools are likely
    more secure because they have been hardened "in the wild".
    - On the other hand, do not add dependencies that are obscure or 
    provide trivial functionality.
- Keep dependencies up to date. 
    - This ensures your users receive vulnerability
fixes from your dependencies.
    - To reduce exposure to supply chain attacks, consider reducing 
    immediate upgrades to new versions: For instance, `uv` allows for 
    specifying a time lag (e.g. 1 week) for upgrading dependencies in deployed software ([dependency cooldowns](https://docs.astral.sh/uv/concepts/resolution/#dependency-cooldowns)). 
    This gives maintainers of dependencies time to react.
- Run vulnerability scans for dependencies.
    - [GitHub Dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart) for generic dependency checks
    - [OWASP dependency check for web applications](https://devguide.owasp.org/en/05-implementation/02-dependencies/01-dependency-check/)
    - Python dependency checks: [`pip-audit`](https://github.com/pypa/pip-audit) 
      and [`uv audit`](https://docs.astral.sh/uv/reference/cli/#uv-audit)
- Run security scans for files.
    - Example: [clamscan](https://docs.clamav.net/manual/Usage/Scanning.html)

## Further Reading

1. OWASP Foundation. "Secure Design". https://devguide.owasp.org/en/04-design/
2. OWASP Foundation. "Principles of security". https://devguide.owasp.org/en/02-foundations/03-security-principles/
3. OWASP Foundation. "Secure Product Design Cheat Sheet". https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet
4. GitHub. Adding a security policy to your repository. https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy

