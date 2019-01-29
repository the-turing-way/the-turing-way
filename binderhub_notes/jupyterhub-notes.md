# Following the Zero-to-JupyterHub Documentation

Sarah Gibson

_The Alan Turing Institute_

Following the notes [here](https://zero-to-jupyterhub.readthedocs.io/en/latest/index.html).

## Intro

JupyterHub allow users to interact with a computing environment via a webpage.
This makes it easier to provide and standardise a computing environment for a group of people since most devices have access to a web browser.

The following will assist in setting up and customising your own JupyterHub on a cloud, but not tied to a specific cloud provider thanks to Kubernetes. 

### What we will become familiar with

* **Cloud provider:** Google Cloud, Microsoft Azure, AWS, etc...
* **Kubernetes:** resource management API
* **Helm:** configures and controls the packaged JupyterHub installation
* **JupyterHub:** user access to a Jupyter computing environment
* **Terminal interface**

Also may run into:
* **Docker:** building customised images
* **Domain registration:** making the hub available at https://your-domain-name.com

List of [Utilised Tools](https://zero-to-jupyterhub.readthedocs.io/en/latest/tools.html#tools).

## Step 0: Setup a Kubernetes cluster (on Microsoft Azure)

See the `kubernetes-notes.md` file for terminology, commands and a link to tutorials.

### Portal Instructions

[This guide](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal) will follow setup instructions for Microsoft Azure, but instructions for other cloud platforms are available.
[Values in square brackets are what I tried to use during setup.]

A glossary of Azure terms can be found [here](https://docs.microsoft.com/en-us/azure/azure-glossary-cloud-terminology).

1. **Sign in to the Azure portal** at [https://portal.azure.com](https://portal.azure.com).

2. **Create an AKS cluster**

   In the top left-hand corner of the Azure portal, select **+ Create a resource > Kubernetes Service**.
   
   a. **Basics:**
   
      * _PROJECT DETAILS_: Select an Azure subscription, then select or create a resource group.
        [Research Engineering, TuringHub]
      * _CLUSTER DETAILS_: Select a cluster name, region, Kubernetes version and DNS name prefix for the cluster. (What is DNS name prefix?)
        [turinghubcluster, UK South, 1.11.5, turinghubcluster]
      * _SCALE_: Select a VM size (Node size on the portal), this **cannot** be changed after deployment. (What do the options mean? What size will we need for full deployment?) Select number of nodes to be deployed into the cluster, this **can** be adjusted after deployment.
        [Standard DS2 v2, 1]
      * Select **Next: Authentication**

   b. **Authentication:**
      * Create a new service principal (or _Configure_ for an existing one.) When using an existing SPN, need to provide the SPN client ID and secret. (Just... what?)
      * Enable the Kubernetes role-based access controls (RBAC) - these provide fine-grained control over access to the Kubernetes resources deployed in the cluster.
      * _Basic_ networking is used by default and Azure Monitor for containers is enabled.
      * Select **Review + create** then **Create** when ready.

   !!! This step is failing. Unable to create new service principal. !!!

### Command Line Instructions

*Discussion/Hackathon with Martin O'Reilly, 29/01/2019*
