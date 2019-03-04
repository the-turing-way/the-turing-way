# Zero to BinderHub!

Sarah Gibson, _The Alan Turing Institute_

**BinderHub Documentation:**
* [Step Zero: Setting up a Kubernetes Cluster](https://zero-to-jupyterhub.readthedocs.io/en/latest/create-k8s-cluster.html)
* [Setup JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-jupyterhub)
* [Setup BinderHub](https://binderhub.readthedocs.io/en/latest/setup-registry.html#set-up-the-container-registry)

To follow along with these instructions, go to this link: [**bit.ly/sg-zero-to-binderhub**](http://bit.ly/sg-zero-to-binderhub)

## Cloud Resource Requirements

This workshop assumes you have a "Free Trial" subscription with [Microsoft Azure](https://azure.microsoft.com/en-gb/).
It's quick to set one up and you get £150 free credit for the first 30 days as well as access to some _always free_ services.

> BinderHub is Cloud-neutral.
> We are using Azure as an example.

## Container Registry

These instructions will link the BinderHub to a [DockerHub](https://hub.docker.com/) Container Registry, and so you will need a DockerHub account as well.

> BinderHub also works with Google Container Registry and custom registries.
> We are using DockerHub as an example.

## Installation Requirements

This workshop will use a terminal (as opposed to Azure's [Cloud Shell](https://azure.microsoft.com/en-gb/features/cloud-shell/) interface) and so we require some command line interfaces.

* **Azure CLI:** Installation guidelines found [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
* **Kubernetes CLI (`kubectl`):** Installation guidelines found [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos)

We used Homebrew on MacOS to install these:
```bash
brew install azure-cli
brew install kubernetes-cli
```

## Instructions

