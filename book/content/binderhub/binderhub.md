# BinderHub

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
|---|---|---|
| [Version Control](./book/content/version_control/version_control.md) | Very Important | |
| [Reproducible Environments](./book/content/reproducible_environments/reproducible_envrionment.md) | Very Important | Particularly read the section on [Binder](https://the-turing-way.netlify.com/reproducible_environments/reproducible_environments.html#Binder_section). |

## Table of Contents

- [BinderHub](#binderhub)
  - [Prerequisites / recommended skill level](#prerequisites--recommended-skill-level)
  - [Table of Contents](#table-of-contents)
  - [Summary](#summary)
  - [How this will help you/ why this is useful](#how-this-will-help-you-why-this-is-useful)
  - [What is BinderHub?](#what-is-binderhub)
  - [How does a BinderHub work?](#how-does-a-binderhub-work)
    - [Kubernetes](#kubernetes)
    - [JupyterHub](#jupyterhub)
    - [repo2docker](#repo2docker)
    - [What happens when a Binder link is clicked?](#what-happens-when-a-binder-link-is-clicked)
  - [Checklist](#checklist)
  - [What to learn next](#what-to-learn-next)
  - [Further reading](#further-reading)
  - [Definitions/glossary](#definitionsglossary)
  - [Bibliography](#bibliography)

## Summary

This chapter will discuss BinderHub, which is the cloud technology powering BinderHub.
We will cover the technologies and tools that BinderHub utilises and the resources you will need to setup your own BinderHub.

## How this will help you/ why this is useful
> why we think you should read the whole thing

## What is BinderHub?

A [BinderHub](https://binderhub.readthedocs.io/en/latest/index.html) is a cloud-based technology that can launch a repository of code (from GitHub, GitLab,...) in a browser window such that the code can be executed and interacted with.
A unique URL is generated allowing the interactive code to be easily shared.

The purpose of these Binder instances is to promote reproducibility in research projects by encouraging researchers to document their software dependencies and produce fun, interactive environments!

## How does a BinderHub work?

BinderHub relies on different tools and resources in order to create and launch the Binder instances.

A high-level explanation of the BinderHub architecture can be found [here](https://binderhub.readthedocs.io/en/latest/overview.html).

| ![cloud_neutral_binderhub](../content/figures/cloud_neutral_binderhub.png) |
|:---:|
| A representation of the BinderHub architecture. |

### Kubernetes

[Kubernetes](https://kubernetes.io/) is a system for automating deployment, scaling (making more or fewer copies), and management of containers across a compute cluster (it doesn't have to be cloud-based).
BinderHub uses Kubernetes to manage the resources requested by the users of the Binder service, and to support the tools of that build the instances.

### JupyterHub

[JupyterHub](https://jupyter.org/hub) is a multi-user server for Jupyter Notebooks and containers alike.
The JupyterHub's main role is to connect the user's browser to the BinderHub instance running on the Kubernetes cluster.
However, the JupyterHub can be further customised to provide greater control over the operation of the BinderHub.

### repo2docker

[repo2docker](https://repo2docker.readthedocs.io/en/latest/?badge=latest) is a tool that automatically builds a Docker image from a code repository given a configuration file.
This Docker container will contain all of the code, data and resources that are listed in the repository.
All the software required to run the code will also be preinstalled from the configuration file.

### What happens when a Binder link is clicked?

1. The link to the repository is resolved by BinderHub.
2. BinderHub searches for a Docker image relating to the provided reference (for example, git commit hash, branch or tag).
3. **If a Docker image is not found**, BinderHub requests resources from the Kubernetes cluster to run repo2docker to do the following:
   * Fetch the repository,
   * Build a Docker image containing the software requested in the configuration file,
   * Push that image to the Docker registry.
4. BinderHub sends the Docker image to JupyterHub.
5. JupyterHub requests resources from the Kubernetes cluster to serve the Docker image.
6. JupyterHub connects the user's browser to the running Docker container.
7. JupyterHub monitors the container for activity and destroys it after a period of inactivity.

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
