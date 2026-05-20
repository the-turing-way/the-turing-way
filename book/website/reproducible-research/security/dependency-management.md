
(rr-security-dependencies)=
# Dependency management

Dependencies are a potential entry point for an attacker. For example,
the in an incident from 2026, the `lite-llm` package contained code that
extracts secrets such as passwords whenever Python is called.

Not only dependency packages, but also trained machine learning models
are dependencies and can represent a threat. For instance, before the 
`safetensors` format for storing and distributing ML model weights,
tensors used to be pickled, which can execute arbitrary Python code when loaded.

## Mitigation
- Reduce the number dependencies: consider implementing some functionality yourself.
- Reduce immediate upgrades to new versions: For instance, `uv` allows for 
specifying a time lag (1 week) for upgrading dependencies in deployed software. 
This gives buffer for the maintainers of your dependencies to react. 
- Run security scans for dependencies, for instance with GitHub dependabot.
- Run security scans for files, such as [clamscan](https://docs.clamav.net/manual/Usage/Scanning.html).

