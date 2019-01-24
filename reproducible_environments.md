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

## Material from binder.md
Step 1: capture your python environment

https://conda.io/docs/user-guide/tasks/manage-environments.html#exporting-the-environment-file

https://pip.pypa.io/en/stable/reference/pip_freeze/

`conda env export > environment.yml`

Note that you have to be IN this environment to run the command above.

or create the environment.yml file manually somehow

https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file

Binder only supports 2.7.15 for a `requirements.txt` file.

Sarah personally recommends using the conda environment because it allows you to say which python installation you want too.

Binder has tons of examples to capture non-python examples but they are difficult to find:

https://mybinder.readthedocs.io/en/latest/config_files.html
https://mybinder.readthedocs.io/en/latest/sample_repos.html

Note - the `install.R` file is a made up file to install R packages. The standard way of doing this for R users is to use a DESCRIPTION file.

https://mybinder.readthedocs.io/en/latest/config_files.html#install-r-install-an-r-rstudio-environment
https://mybinder.readthedocs.io/en/latest/config_files.html#description-install-an-r-package

Note that the DESCRIPTION file doesn't just install the specific package - it will ALSO install any requirements that you have :smile:


Step 2: go to mybinder.org, add your GitHub repo link (specify more when needed) and hit "launch"

Note: the default binder page opens up into a jupyter **notebook** server. It may be the case that the BETTER solution is to add `?urlpath=lab` to the end of the url so that it opens up a jupyter **lab** environment instead.

Note: difference between lab and notebook environment will (may) need to be covered in computing environment chapter (if we have time!)!

By default python 2 and python 3 are installed.

Jupyter lab allows you to open a *terminal* rather than a notebook.

The terminal doesn't have access to a GUI so importing matplotlib.pyplot or .pylab (graphical stuff) won't work

Q: what's the difference between a console and a terminal?

The console has enough for you to be able to run a bunch of python commands.

The terminal doesn't have access to a graphics card! So the console won't work.

Step 3: copy markdown back into your readme to get a nice "launch binder" button

**CHANGES IN BINDER ARE NOT PUSHED BACK INTO YOUR REPO/DOCKER!**

-> this is technically possible but not a feature offered by the public binder; it can be enabled on a local BinderHub (with some new )



## BinderHub

- needs Kubernetes cluster that spins up a bunch of VMs with containers etc. - also does some loadbalancing (Kubernetes [Google developed] being rather new and complex but it can be wrangled to do what you want it to do)
- jupyterLab to create the environments
- repo2docker that grabs repo from GitHub and launches Docker
- BinderHub basically is the high level coordinator for these 3 things and can be accessed through some frontend (the pyblic one being mybinder.org)


Also make this useful to run on local machines/HPCs (that might not be setup for this much networking) to enable data throughput independent of cloud availability
- you don't need all the fancy stuff Kubernetes can do to run a BinderHub -> strip down Kubernetes to the essentials and run that locally




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
