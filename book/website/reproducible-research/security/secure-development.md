
(rr-secure-development)=


# Secure code development


The principles of security can also be applied to the development and 
collaboration workflow:
- **Defense in depth**: Securing ssh keys adds a layer of security: If a developer's
laptop is stolen, the attacker may gain access to development environments 
in the cloud or on an HPC system. Securing ssh keys reduce the chances of this happening.
- **Least privilege**: Give different privileges to different developers on platforms such as
GitHub. For instance, only core maintainers can make releases, or letting
certain developers only modify parts of the code base.

### Secure Code Development & Quality Assurance in the _Turing Way_

Topics covering the active development phase, where code quality, input/output sanitation, 
and configuration formats are strictly evaluated. 

1. Code Quality chapter specifically mentions {ref}`Static Code Analysis <rr-code-quality>`
2. Example of code execution vulnerabilities is given by {ref}`YAML Security Issues <rr-renv-yaml-security>`
3. Checklist for the Code Review Process mentions {ref}`Security of New Code<rr-checklist-for-code-review-security-new-code>`
4. Signed commits ensure integrity of the data in a version control system. See {ref}`Version Control workflow<rr-vcs-workflow>`


