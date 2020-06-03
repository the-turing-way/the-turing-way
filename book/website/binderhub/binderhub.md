# BinderHub

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
|---|---|---|
| [Version Control](/version_control/version_control) | Very Important | |
| [Reproducible Environments](/reproducible_environments/reproducible_environments) | Very Important | Particularly read the section on [Binder](https://the-turing-way.netlify.com/reproducible_environments/reproducible_environments.html#Binder_section). |

## Table of Contents

- [Summary](#summary)
- [How this will help you/ why this is useful](#how-this-will-help-you-why-this-is-useful)
- [What is BinderHub and why is it good for Reproducibility?](#what-is-binderhub-and-why-is-it-good-for-reproducibility)
- [How does a BinderHub work?](#how-does-a-binderhub-work)
  - [Compute Resources](#compute-resources)
  - [Kubernetes](#kubernetes)
  - [Helm](#helm)
  - [JupyterHub](#jupyterhub)
  - [repo2docker](#repo2docker)
  - [What happens when a Binder link is clicked?](#what-happens-when-a-binder-link-is-clicked)
- [Why would you build your own BinderHub?](#why-would-you-build-your-own-binderhub)
  - [Issues you may face when deploying a BinderHub](#issues-you-may-face-when-deploying-a-binderhub)
- [Further reading](#further-reading)
- [Definitions/glossary](#definitionsglossary)
- [Bibliography](#bibliography)

## Summary

This chapter will discuss [BinderHub](https://binderhub.readthedocs.io/en/latest/index.html), which is the cloud technology powering [Binder](https://mybinder.readthedocs.io/en/latest/).
We will cover the technologies and tools that BinderHub utilises and the resources you will need to setup your own BinderHub.

This chapter is primarily aimed at Research Software Engineers and IT Services who wish to provide a BinderHub as a service to a group of researchers.
Though anyone can build a BinderHub.

## How this will help you/ why this is useful

Reading this chapter will give you a clearer picture of how Binder services (such as [mybinder.org](https://mybinder.org)) operate, the technologies powering BinderHub and how they interact with one another.
This chapter also covers reasons why you might build your own BinderHub, rather than using the public service at mybinder.org.

## What is BinderHub and why is it good for Reproducibility?

[BinderHub](https://binderhub.readthedocs.io/en/latest/index.html) is a cloud-based technology that can launch a repository of code (from GitHub, GitLab, and others) in a browser window such that the code can be executed and interacted with.
A unique URL is generated allowing the interactive code to be easily shared.

The purpose of these Binder instances is to promote reproducibility in research projects by encouraging researchers to document their software dependencies and produce fun, interactive environments!

Binder, as a user interface, is useful for reproducibility because the code needs to be version controlled and the computational environment needs to be documented in order to benefit from the functionality of Binder.
Each change to the code repository also forces a new build of the Binder instance.
This acts as a proxy for continuous integration of the computational environment as the Binder instance will break if the configuration file is not updated.

Learn more about Continuous Integration in [this chapter](/continuous_integration/continuous_integration).

## How does a BinderHub work?

BinderHub relies on different tools and resources in order to create and launch the Binder instances.

For more information, see this [high-level explanation of the BinderHub architecture](https://binderhub.readthedocs.io/en/latest/overview.html).

| ![/figures/cloud_neutral_binderhub.png](https://zenodo.org/api/iiif/v2/e4125eaf-b456-4097-85fc-6a2e80482d1c:96c70193-2f9e-442d-8cf8-21485d8864e1:1728_TURI_Book%20sprint_45%20repo2docker_040619_v2_MK.jpg/full/750,/0/default.jpg) |
|:---:|
| A representation of the BinderHub architecture. This image was created by [Scriberia](http://www.scriberia.co.uk/) for The Turing Way community and is used under a CC-BY licence. |

### Compute Resources

BinderHub is cloud-neutral which means it can be deployed on any cloud platform.
Therefore, the minimum requirement is a subscription to a cloud platform of your choosing.

In fact, BinderHub is not dependent on cloud-hosting at all and can be deployed onto an on-premise computing system.

### Kubernetes

[Kubernetes](https://kubernetes.io/) is a system for automating deployment, scaling (making more or fewer copies), and management of containers across a compute cluster (it doesn't have to be cloud-based).
BinderHub uses Kubernetes to manage the resources requested by the users of the Binder service, and to support the tools that build the environments.

### Helm

[Helm](https://helm.sh/) is a package manager for Kubernetes.
Packages come in the form of *Charts* which are a set of instructions to deploy, upgrade and manage applications running on a Kubernetes cluster.
They can make installing and managing Kubernetes applications much easier and specific Charts for projects can be published online.
For example, the Helm Chart for BinderHub is available [here](https://jupyterhub.github.io/helm-chart/#development-releases-binderhub).

### JupyterHub

[JupyterHub](https://jupyter.org/hub) is a multi-user server for Jupyter Notebooks and containers alike.
In the context of Binder, the JupyterHub's main role is to connect the user's browser to the BinderHub instance running on the Kubernetes cluster.
However, the JupyterHub can be further customised to provide greater control over the operation of the BinderHub.

### repo2docker

[repo2docker](https://repo2docker.readthedocs.io/en/latest/?badge=latest) is a tool that automatically builds a Docker image from a code repository given a configuration file.
This Docker image will contain all of the code, data and resources that are listed in the repository.
All the software required to run the code will also be preinstalled from the configuration file.

BinderHub can be thought of as thin layer that sits on top of repo2docker and JupyterHub, orchestrating their interactions and resolving URLs.

### What happens when a Binder link is clicked?

1. The link to the repository is resolved by BinderHub.
2. BinderHub searches for a Docker image relating to the provided reference (for example, git commit hash, branch or tag).
3. **If a Docker image is not found**, BinderHub requests resources from the Kubernetes cluster to run repo2docker to do the following:
   - Fetch the repository,
   - Build a Docker image containing the software requested in the configuration file,
   - Push that image to the Docker registry.
4. BinderHub sends the Docker image to JupyterHub.
5. JupyterHub requests resources from the Kubernetes cluster to serve the Docker image.
6. JupyterHub connects the user's browser to the running Docker environment.
7. JupyterHub monitors the container for activity and destroys it after a period of inactivity.

## Why would you build your own BinderHub?

[mybinder.org](https://mybinder.org/) is the free, public BinderHub that hosts almost 100k Binder launches per week.
Why might you want to build your own?

Binder is an open source project maintained by volunteers and as such they ask that users stay within certain computational limitations in order to keep running costs as low as possible whilst still providing a usable service.
By hosting your own BinderHub, you can offer your users much more flexible and tailored resources.

These customisations could include:

- authentication,
- greater computational resources per user,
- bespoke library stacks and packages,
- allowing access to private repos,
- persistent storage for users,
- restrict sharing within a certain institution or team.

### Issues you may face when deploying a BinderHub

BinderHubs are becoming increasingly popular amongst universities and research institutes.
This is because they can facilitate multiple instances of the same set of notebooks for use in a tutorial or workshop setting.

If you are deploying a cloud-hosted BinderHub on behalf of your organisation, you may need specific permissions on your organisation's cloud platform subscription.
Which permissions you require will vary based on the cloud platform you have access to and your IT Services policies.
At minimum, you'll need to be able to assign [Role Based Access Control (RBAC)](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) to your resources so they can act autonomously in order to manage user traffic.

## Further reading

- [Binder documentation](https://mybinder.readthedocs.io/en/latest/)
- [BinderHub documentation](https://binderhub.readthedocs.io/en/latest/index.html)
- [Zero-to-JupyterHub with Kubernetes documentation](https://zero-to-jupyterhub.readthedocs.io/en/latest/index.html)
- [JupyterHub documentation](https://jupyterhub.readthedocs.io/en/stable/)
- [_The Turing Way_ Build a BinderHub Workshop](http://bit.ly/zero-to-binderhub-workshop)

## Definitions/glossary

| | |
|:---|:---|
| Docker image | A machine-readable set of instructions to create a specified computational environment.|
| Docker container | An active computational environment executed from a Docker image. |
| Docker registry | A storage and distribution system for named Docker images. The registry allows Docker users to pull images locally, as well as push new images to the registry (given adequate access permissions when applicable). Such systems are often hosted in the cloud for ease of access. |
| BinderHub | Technology for hosting reproducible computational environments. |
| Binder | The user-facing service of a BinderHub. |
| Kubernetes | Autonomous computational cluster manager. |
| Helm | A package manager for Kubernetes applications. |
| JupyterHub | A multi-user server for Jupyter Notebook instances. |
| repo2docker | A tool to build Docker images from code repositories. |

## Bibliography

- **Kubernetes documentation**: [https://kubernetes.io/](https://kubernetes.io/)
- **Helm documentation**: [https://helm.sh/](https://helm.sh/)
- **repo2docker**: [https://repo2docker.readthedocs.io/en/latest/?badge=latest](https://repo2docker.readthedocs.io/en/latest/?badge=latest)
- **Microsoft Azure documentation on Role Based Access Control**: [https://docs.microsoft.com/en-us/azure/role-based-access-control/overview](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)
