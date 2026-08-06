
(rr-secure-development)=


# Secure Software Development


The principles of security can also be applied to the development and 
collaboration workflow:
- **Defense in depth**: Securing ssh keys adds a layer of security: If a developer's
laptop is stolen, the attacker may gain access to development environments 
in the cloud or on an HPC system. Securing ssh keys reduce the chances of this happening.
- **Least privilege**: Give different privileges to different developers on platforms such as
GitHub. For instance, only core maintainers can make releases, or letting
certain developers only modify parts of the code base.


## Security in research and software development in the _Turing Way_

The book covers specific aspects related to secure code development.

### Secure Code Development & Quality Assurance 

Topics covering the active development phase, where code quality, input/output sanitation, 
and configuration formats are strictly evaluated. 

1. Code Quality chapter specifically mentions {ref}`Static Code Analysis <rr-code-quality>`
2. Example of code execution vulnerabilities is given by {ref}`YAML Security Issues <rr-renv-yaml-security>`
3. Checklist for the Code Review Process mentions {ref}`Security of New Code<rr-checklist-for-code-review:security-new-code>`
4. Signed commits ensure integrity of the data in a version control system. See {ref}`Version Control workflow<rr-vcs-workflow>`


### Sensitive Data and use of Third-party platforms/Services

Topics focusing on securing the inputs of your research, tracking data gathering responsibly, 
and keeping sensitive files safe. 

1. {ref}`Electronic Lab Notebooks (ELNs)<rr-rdm-elns>` section mentions security concerns around ELNs. 
2. {ref}`Keeping Sensitive Files Secure<pd-sdpw-sensitive-files>`, for instance, by preventing .env, passwords or API tokens from being committed to public repositories

It is essential to understand the security implications of the third-party platforms and services 
used in your research software workflows. For instance, the University of Sheffield provides an 
excellent example of this with their security guidelines for GitHub Organizations [(RSE Sheffield Infrastructure Guidelines)](https://rse.shef.ac.uk/blog/2026-01-30-github-organisations/). Check if your organization has similar guidelines. 

