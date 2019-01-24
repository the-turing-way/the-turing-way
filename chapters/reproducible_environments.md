# Reproducible environments

## Material from hack.md

Main points to cover:
- What is a comutational environment (very brief)
- Why your computational environment (often kind of an afterthought) is actually really important for reproducibility.
- Local computational environments
    - Python `virtualenv` and `venv`, `conda` environments
    - Equivalent for R
- Containers
    - What they are
    - When you would use one locally (as not everyone will need to, depends on complexity of project)
    - How they are used in Binder
    - How they can be used for CI (but CI itself in different chapter)

requirements.txt say install e.g. matplotlib
Breaks because don't have the right version of matplotlib
install packages that require specific versions of other packages, dependancies.
Containers etc. Docker is/like a yaml file

We have a tendency to say we used "python" or "numpy" or "R" for our work, but actually there are different versions of these programming languages and packages which mean things are DIFFERENT across them.

One of the most common problems is coming back to your work after 6 months (maybe after reviewers have finally sent your paper back for revisions, or when you're about to fly off to the conference you applied for ages ago) and realising that your code doesn't work any more! Or maybe it does work but it gives you different answers.

* Need an example of errors from different packages.
  Could be a good crowd sourcing option - ask folks to tell us about their Gotchas!

Need a section on semantic versioning: https://semver.org.
Difference between major, minor and patch upgrades, commonly named as: MAJOR.MINOR.PATCH

It's actually really easy to capture your computational environment:

* `pip freeze`
* equivalent command for `conda`: `conda env export`
* equiv for `R`


As always prevention is better than a cure!
If you can install the specific version at the time of running and not up date it.

Useful to have different environments for different projects so that they don't go out of date! https://conda.io/docs/user-guide/tasks/manage-environments.html

What's great about binder is that it will do all this for you\* - but we recommend that you specifically name the version of

\* Need to be v. careful about phrasing here - repo owner needs to provide information on the computational environment, even if hidden from Binder user.

[Syntax for yaml files, think this resource is open source, and it's hosted on github](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

Yaml's a markup language.

Ultimately Dockerfiles & Travis.yml files do similar things. They define computational environments.

Note the points from this blog post: http://urssi.us/blog/2018/12/21/why-research-software-sustainability-wont-be-fixed-by-containers/

YAML is very standard for configuration files.
It's used for Rmarkdown configurations, at the top of jekyll files and for conda configurations for example.

Indentation important:
- [YAML IDIOSYNCRASIES](https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html)
- [UNDERSTANDING YAML](https://docs.saltstack.com/en/latest/topics/yaml/)

Makefiles

- older option to make things reproducible
- see issue https://github.com/alan-turing-institute/the-turing-way/issues/24
- PHONY will keep track of files created when you run this and not recreate already existing files

## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful
> why we think you should read the whole thing

## Prerequisites / recommended skill level
> other chapters that should have been read before or content you should be familiar with before you read this

## Chapter content
> depending on the content, this might be more structured, e.g. with exercises, gotcha sections etc

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography
> Credit/urls for any materials that form part of the chapter's text.
