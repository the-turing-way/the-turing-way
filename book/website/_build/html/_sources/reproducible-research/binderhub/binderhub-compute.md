(rr-binderhub-compute)=
# Compute Resources

BinderHub is cloud-neutral which means it can be deployed on any cloud platform.
Therefore, the minimum requirement is a subscription to a cloud platform of your choosing.

In fact, BinderHub is not dependent on cloud-hosting at all and can be deployed onto an on-premise computing system.

## Kubernetes

[Kubernetes](https://kubernetes.io/) is a system for automating deployment, scaling (making more or fewer copies), and management of containers across a compute cluster (it doesn't have to be cloud-based).
BinderHub uses Kubernetes to manage the resources requested by the users of the Binder service, and to support the tools that build the environments.

## Helm

[Helm](https://helm.sh/) is a package manager for Kubernetes.
Packages come in the form of *Charts* which are a set of instructions to deploy, upgrade and manage applications running on a Kubernetes cluster.
They can make installing and managing Kubernetes applications much easier and specific Charts for projects can be published online.
For example, the Helm Chart for BinderHub is available [here](https://jupyterhub.github.io/helm-chart/#development-releases-binderhub).

## repo2docker

[repo2docker](https://repo2docker.readthedocs.io/en/latest/?badge=latest) is a tool that automatically builds a Docker image from a code repository given a configuration file.
This Docker image will contain all of the code, data and resources that are listed in the repository.
All the software required to run the code will also be preinstalled from the configuration file.

## JupyterHub

[JupyterHub](https://jupyter.org/hub) is a multi-user server for Jupyter Notebooks and containers alike.
In the context of Binder, the JupyterHub's main role is to connect the user's browser to the BinderHub instance running on the Kubernetes cluster.
However, the JupyterHub can be further customised to provide greater control over the operation of the BinderHub.

BinderHub can be thought of as thin layer that sits on top of repo2docker and JupyterHub, orchestrating their interactions and resolving URLs.

## What happens when a Binder link is clicked?

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
