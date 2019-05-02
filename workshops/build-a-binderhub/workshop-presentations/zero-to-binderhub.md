# Zero to BinderHub!

Sarah Gibson, _The Alan Turing Institute_

[**The Turing Way**](https://github.com/alan-turing-institute/the-turing-way) - making reproducible data science _too easy not to do_!

These steps will walk you through deploying a BinderHub on Microsoft Azure.
It will be publicly available like [mybinder.org](https://mybinder.org).
To follow along with these instructions, go to this link: [**bit.ly/zero-to-binderhub**](http://bit.ly/zero-to-binderhub)

**BinderHub Documentation:**
* [Step Zero: Setting up a Kubernetes Cluster](https://zero-to-jupyterhub.readthedocs.io/en/latest/create-k8s-cluster.html)
* [Setup JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-jupyterhub)
* [Setup BinderHub](https://binderhub.readthedocs.io/en/latest/setup-registry.html#set-up-the-container-registry)

## Table of Contents

* [Cloud Resource Requirements](#cloud-resource-requirements)
* [Container Registry](#container-registry)
* [Installation Requirements](#installation-requirements)
* [A Note on Secret Files](#a-note-on-secret-files)
* [Deploying a Kubernetes Cluster on Azure](#deploying-a-kubernetes-cluster-on-azure)
* [Setting up Helm](#setting-up-helm)
* [Setup BinderHub](#setup-binderhub)
* [Debugging your BinderHub](#debugging-your-binderhub)
* [Authenticating Users with GitHub](#authenticating-users-with-github)
* [Tearing Down your BinderHub Deployment](#tearing-down-your-binderhub-deployment)
* [Example config files](#example-config-files)
* [Glossary of Kubernetes terms](#glossary-of-kubernetes-terms)

## Cloud Resource Requirements

This workshop assumes you have a "Free Trial" subscription with [Microsoft Azure](https://azure.microsoft.com/en-gb/).
It's quick to set one up and you get £150 free credit for the first 30 days as well as access to some _always free_ services.

**NOTE:** Please do not sign up with an institutional email as you may encounter some issues with Service Principal permissions when we deploy the Kubernetes cluster.

> BinderHub is Cloud-neutral.
> We are using Azure as an example.

## Container Registry

These instructions will link the BinderHub to a [DockerHub](https://hub.docker.com/) Container Registry, and so you will need a DockerHub account as well.

> BinderHub also works with Google Container Registry and custom registries.
> We are using DockerHub as an example.

## Installation Requirements

This workshop will use a terminal (if you are on a Windows machine, you should use Azure's [Cloud Shell](https://azure.microsoft.com/en-gb/features/cloud-shell/)) and so we require some command line interfaces.

* **Azure CLI:** Installation guidelines found [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) (not required for Windows users)
* **Kubernetes CLI (`kubectl`):** Installation guidelines found [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos)
* **Helm (Kubernetes package manager):** Installation guidelines found [here](https://helm.sh/docs/using_helm/#installing-helm)

We used Homebrew on MacOS to install these:
```bash
brew install azure-cli
brew install kubernetes-cli
brew install kubernetes-helm
```

## A Note on Secret Files

Building a BinderHub requires a few pieces of sensitive information, such as access tokens and passwords.
In this workshop, we will be saving this information to disk which is not ideal.

The ideal scenario would be to store this information in an [Azure Key Vault](https://azure.microsoft.com/en-gb/services/key-vault/) such that the secrets could be programmatically added to the relevant files and then locally deleted as necessary.
However, this falls out of the scope of a BinderHub workshop.

You can access Key Vault Quickstarts and Tutorials [here](https://docs.microsoft.com/en-gb/azure/key-vault/).

:vertical_traffic_light: :vertical_traffic_light: :vertical_traffic_light: :vertical_traffic_light: :vertical_traffic_light:

## Deploying a Kubernetes cluster on Azure

Adapted from [Step Zero: Kubernetes on Microsoft Azure Container Service (AKS)](https://zero-to-jupyterhub.readthedocs.io/en/latest/microsoft/step-zero-azure.html).

A short (and by no means exhaustive) [glossary](#glossary-of-kubernetes-terms) of Kubernetes terms is given at the end of this workshop, should you require further explanation.

### 1. Login to Azure

```bash
az login --output none
```

This command will open a browser window for you to log in to your Azure account.
You can safely close this window after logging in.

### 2. Activate your Subscription

To see a list of Azure subscriptions you have available to you, you can run the following command.
```bash
az account list --refresh --output table
```
This prints your subscriptions to the terminal in a human-readable format.

You should only see a "Free Trial" subscription (unless you have used Azure before and have others).
Let's activate this with the following command.
```bash
az account set -s "Free Trial"
```
**NOTE:** If you wish to use a different subscription, replace the text in quotes with the name of your chosen subscription.

### 3. Create a Resource Group

Resource Groups are how the Azure environment manages services that are related to each other (further details in [this blog post](http://www.onlinetech.com/resources/references/how-to-use-azure-resource-groups-a-simple-explanation)).
We will create a resource group in a specific data location and create computational resources _within_ this group.

```bash
az group create --name testhub \
    --location westeurope \
    --output table
```
* `--name` specifies the name of your resource group and should be something that uniquely identifies this hub.
* `--location` specifies the location of the data centre where your resource will exist.
  A list of data centre locations can be found [here](https://docs.microsoft.com/en-us/azure/aks/container-service-quotas#region-availability).
  We have chosen West Europe for resource availability.
* `--output table` specifies the output should be in human-readable format as opposed to JSON, which is the default output.


### 4. Choose a Cluster Name

We are now going to create some folder/files that will contain SSH keys, tokens and passwords.
You may wish to create a [_hidden_ folder](https://www.maketecheasier.com/hide-file-folder-in-mac/) (e.g. `.secret/`) create any further files and folders within this one.
If you are then collaborating with people on your BinderHub on GitHub, you would use a `.gitignore` file to prevent the contents of the folder from being pushed to GitHub by adding `.secret/` to it.

Example of hidden folder creation:
```bash
mkdir ~/.secret
cd ~/.secret
```

Create a folder in which to store files relating to the compute cluster we are about to build.
This folder should have the same name as the cluster and should be descriptive and short.

`--name` cannot exceed 63 characters and can only contain letters, numbers, or dashes (-).
This is a requirement for the `aks create` command in the next step.

```bash
mkdir hubcluster
cd hubcluster
```

### 5. Create an SSH key

Create an SSH key to secure your cluster (further details in [this blog post](https://jumpcloud.com/blog/what-are-ssh-keys-b/)). **Keep these files safe.**

```bash
ssh-keygen -f ssh-key-hubcluster
```
When prompted for a password, you can choose to leave this blank.
Some text will be printed to the terminal which you don't need to do anything with.

### 6. Create an Azure Container Service (AKS) Cluster

This command will request a Kubernetes cluster within the resource group we created.
It will request one `Standard_D2s_v3` virtual machine which a Kubernetes cluster installed.
For information on other types of virtual machines available, [see here](https://azure.microsoft.com/en-gb/pricing/details/virtual-machines/series/).

**NOTE:** If you are _not_ using a Free Trial subscription, try setting `--node-count` to **3** instead.

```bash
az aks create --name hubcluster \
    --resource-group testhub \
    --ssh-key-value ssh-key-hubcluster.pub \
    --node-count 1 \
    --node-vm-size Standard_D2s_v3 \
    --output table
```
* `--name` is the cluster name we defined in [Step 4: Choose a Cluster Name](#4-choose-a-cluster-name).
* `--resource-group` is the resource group we created in [Step 3: Create a Resource Group](#3-create-a-resource-group).
* `--ssh-key-value` is the ssh public key we created in [Step 5: Create an SSH key](#5-create-an-ssh-key).
* `--node-count` is the number of desired nodes in the Kubernetes cluster.
* `--node-vm-size` is the size of the nodes you wish to use, which varies based on the use-case of the cluster and how much RAM/CPU each user will need.

**NOTE:** The default version of Kubernetes will be installed, you can use the `--kubernetes-version` flag to install a different version.

**This step may take a few minutes to execute.** :vertical_traffic_light:

### 7. Get credentials from Azure for `kubectl`

This step automatically updates your local Kubernetes client configuration file to be configured with the remote cluster we've just deployed, and allowing `kubectl` to be "logged-in" to the cluster.

```bash
az aks get-credentials --name hubcluster --resource-group testhub
```
* `--name` is the cluster name defined in [Step 4: Choose a Cluster Name](#4-choose-a-cluster-name).
* `--resource-group` is the resource group created in [Step 3: Create a Resource Group](#3-create-a-resource-group).

### 8. Check the Cluster is Fully Functional

```bash
kubectl get nodes
```

The output of this command should list one node (unless you changed `--node-count` in [Step 6: Create an Azure Container Service (AKS) Cluster](#6-create-an-azure-container-service-aks-cluster)) with a `STATUS` of `READY`.
The `VERSION` field reports which version of Kubernetes is installed.

Example output:
```bash
NAME                       STATUS   ROLES   AGE   VERSION
aks-nodepool1-97000712-0   Ready    agent   19m   v1.9.11
```

:question: :question: Pause for questions and people to catch up :question: :question:

## Setting up Helm

Adapted from [Zero-to-JupyterHub: Setting up and Securing Helm](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html).

Helm is the package manager for Kubernetes and is used for: installing, upgrading and managing applications on a Kubernetes cluster.
Helm packages are called _charts_.

Helm has two parts: a client (`helm`) and a server (`tiller`).
Tiller runs inside your Kubernetes cluster as a pod in the `kube-system` namespace.
Tiller manages _releases_ (installations) and _revisions_ (versions) of charts deployed on the cluster.
When you run a `helm` command, the local Helm client sends instructions to `tiller` in the cluster which in turn makes the requested changes.

> **Did you know?:** Kubernetes is Greek for "captain" or "helmsman". In case you haven't noticed the nautical theme!

### 1. Setup a `ServiceAccount` for `tiller`

When you (a human) accesses your Kubernetes cluster, you are authenticated as a particular **User Account**.
Processes in containers running in _pods_ are authenticated as a particular **Service Account**.
More details [here](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/).

```bash
kubectl --namespace kube-system create serviceaccount tiller
```

### 2. Give the `ServiceAccount` full permissions to manage the cluster

This step enables Role Based Access Control (RBAC) so Kubernetes can secure which pods/users can perform what kind of actions on the cluster.
If RBAC is disabled, **all pods are given `root` equivalent permission on all the Kubernetes nodes and the cluster itself.**
This can leave the cluster vulnerable to attacks.
See [Project Jupyter's docs](https://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#use-role-based-access-control-rbac) for more details.

```bash
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
```

:question: 🤔

### 3. Initialise `helm` and `tiller`

This step will create a `tiller` deployment in the `kube-system` namespace and set-up your local `helm` client.
This is the command that connects your remote Kubernetes cluster to the commands you execute in your local terminal and only needs to be run once per Kubernetes cluster.

```bash
helm init --service-account tiller --wait
```

**NOTE:** If you wish to install `helm` on another computer, you won't need to setup `tiller` again but `helm` still needs to be initialised.
The command to only initialise `helm` is:
```bash
helm init --client-only
```

### 4. Secure Helm

Secure `tiller` from access inside the cluster.

`tiller`s port is exposed in the cluster without authentication and if you probe this port _directly_ (i.e. by bypassing `helm`) then `tiller`s permissions can be exploited.
This step forces `tiller` to listen to commands from `localhost` (i.e. `helm`) _only_ so that e.g. other pods inside the cluster cannot ask `tiller` to install a new chart. For example, this could give other pods arbitrary, elevated privileges to exploit.
More details [here](https://engineering.bitnami.com/articles/helm-security.html).

```bash
kubectl patch deployment tiller-deploy \
    --namespace=kube-system \
    --type=json \
    --patch='[{
        "op": "add",
        "path": "/spec/template/spec/containers/0/command",
        "value": ["/tiller", "--listen=localhost:44134"]
    }]'
```

:question: 🤔

### 5. Verify the installation

To verify the correct versions have been installed properly, run the following command.

```bash
helm version
```

You must have at least version 2.11.0 and the client (`helm`) and server (`tiller`) versions must match.
It may take a few moments for the client to appear - keep trying.

Example output:
```bash
Client: &version.Version{SemVer:"v2.12.3", GitCommit:"eecf22f77df5f65c823aacd2dbd30ae6c65f186e", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.12.3", GitCommit:"eecf22f77df5f65c823aacd2dbd30ae6c65f186e", GitTreeState:"clean"}
```

:question: :question: Pause for questions and people to catch up :question: :question:

## Setup BinderHub

Adapted from [Zero-to-BinderHub: Setup BinderHub](https://binderhub.readthedocs.io/en/latest/setup-binderhub.html).

### 1. Preparing to Install

Before we install a BinderHub, we need to configure several pieces of information and save them in `yaml` files.

Create a folder named after your BinderHub. (I will also create this inside `~/.secret`.)
```bash
mkdir testhub
cd testhub
```

Create two random tokens:
```bash
openssl rand -hex 32
openssl rand -hex 32
```
**NOTE:** The command is run **twice** as we need two different tokens.

### 2. Create a `secret.yaml` file
 
Create a `secret.yaml` file containing the following config and save it in the folder we created in [Step 1: Preparing to Install](#1-preparing-to-install).
```yaml
jupyterhub:
  hub:
    services:
      binder:
        apiToken: "<output of FIRST 'openssl rand -hex 32' command>"
  proxy:
    secretToken: "<output of SECOND 'openssl rand -hex 32' command>"
```

To connect to DockerHub, add the following lines.
```yaml
registry:
  username: <docker-id>
  password: <password>
```
**NOTE:** `registry` is on the same indentation level as `jupyterhub`.

Click [here](#secretyaml) for a complete example `secret.yaml` file.

### 3. Create a `config.yaml` file

Create a `config.yaml` file with the following information and save it in the folder we created in [Step 1: Preparing to Install](#1-preparing-to-install).

```yaml
config:
  BinderHub:
    use_registry: true
    image_prefix: <docker-id>/binder-dev-
```

**NOTE:**
  * If your Docker account is part of an organisation where you would like to store images instead, change the value of `image_prefix` to `<docker-organisation-name>/<prefix>-`
  * The `<prefix>` can be any string since it will be prepended to image names.
  It is recommended to be something short and descriptive, such as `binder-dev-` (for development) or `binder-prod-` (for the final product).

### 4. Install BinderHub

First, pull the latest Helm chart for BinderHub.
```bash
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart
helm repo update
```

Next, install the required Helm chart using the config files we created in Steps [2: Create a `secret.yaml` file](#2-create-a-secretyaml-file) and [3: Create a `config.yaml` file](#3-create-a-configyaml-file).
```bash
helm install jupyterhub/binderhub --version=0.2.0-3b53fce \
    --name=binderhub \
    --namespace=binderhub \
    -f secret.yaml -f config.yaml
```
* `--version` refers to the version of the BinderHub Helm Chart.
  Available versions can be found [here](https://jupyterhub.github.io/helm-chart/#development-releases-binderhub).
  We have used the version released on March 3rd 2019.
* `--name` and `--namespace` may be different, but it's recommended they be the same to avoid confusion.
  It should be something short and descriptive.

This step will deploy both a JupyterHub and a BinderHub but they are not yet configured to communicate with one another.
You may need to wait a few moments before moving on as the resources may take a while to be set up.

### 5. Connect JupyterHub and BinderHub

Print the IP address of the JupyterHub that was just deployed by running the following command.
It will be listed in the `EXTERNAL-IP` field.
```bash
kubectl --namespace=binderhub get svc proxy-public
```

Copy this IP address and add the following line to `config.yaml`.
```yaml
hub_url: http://<IP address in EXTERNAL-IP field from above>
```
**NOTE:** `hub_url` is at the same indentation level as `use_registry` and `image_prefix` in [Step 3: Create a `config.yaml` file](#3-create-a-configyaml-file).
Click [here](#configyaml) for a complete example `config.yaml` file.

Now upgrade the Helm chart to deploy the change.
```bash
helm upgrade binderhub jupyterhub/binderhub \
    --version=0.2.0-3b53fce \
    -f secret.yaml -f config.yaml
```
**NOTE:** `--version` must be the same as in [Step 4: Install BinderHub](#4-install-binderhub).

### 6. Try out your BinderHub deployment!

Find the IP address of your BinderHub under the `EXTERNAL-IP` field.
```bash
kubectl --namespace=binderhub get svc binder
```

Copy the IP address into your browser and your BinderHub should be waiting.

If you've been successful, a page identical to [mybinder.org](https://mybinder.org) should appear.
Type the following URL into the GitHub repo box and launch it: **https://github.com/binder-examples/requirements**. You can even sign in to your Docker account to see when the image has been pushed to the registry.

## Debugging your BinderHub

If something is not working correctly with your BinderHub, the quickest way to find the problem is to access the JupyterHub logs.
Executing the following commands will print the JupyterHub logs to your terminal.

```bash
kubectl get pod -n binderhub                # Lists all active pods. Find the one beginning with "hub-"
kubectl logs hub-<random-str> -n binderhub  # Where <random-str> matches the output from the last step
```

## Authenticating Users with GitHub

Adapted from [Enabling Authentication](https://binderhub.readthedocs.io/en/latest/authentication.html) and [Authentication](https://zero-to-jupyterhub.readthedocs.io/en/stable/authentication.html#github).

The default is for BinderHub to run without authentication and, for each launch, it creates a temporary user and starts a server for that user.

You can enable authentication for BinderHub by using JupyterHub as an oauth provider by editing `config.yaml`.

### 1. Editing `config.yaml`

First add `auth_enabled: true` under the `config: BinderHub:` key.
Then add the following as an unindented level key.

**NOTE:** In the following, `binderhub_url` is the IP address you visit to reach your Binder launch page (i.e. the output of [Step 6: Try out your BinderHub deployment!](#6-try-out-your-binderhub-deployment)) and `jupyterhub_url` is the IP address listed under `config: BinderHub: hub_url:` and the top of `config.yaml`.

```yaml
jupyterhub:
  cull:
    # don't cull authenticated users
    users: False

  hub:
    services:
      binder:
        oauth_redirect_uri": "http://<binderhub_url>/oauth_callback"
        oauth_client_id: "binder-oauth-client-test"
    extraConfig:
      hub_extra: |
        c.JupyterHub.redirect_to_server = False

      binder: |
        from kubespawner import KubeSpawner

        class BinderSpawner(KubeSpawner):
          def start(self):
            if 'image' in self.user_options:
              # binder service sets the image spec via user options
              self.image = self.user_options['image']
            return super().start()
        c.JupyterHub.spawner_class = BinderSpawner

  singleuser:
    # to make notebook servers aware of hub
    cmd: jupyterhub-singleuser

  auth:
    type: github
    github:
      clientId: "<Your GitHub Client ID>"
      clientSecret: "<Your GitHub Client Secret>"
      callbackUrl: "http://<jupyterhub_url>/hub/oauth_callback"
```

**NOTE:** We will generate `clientId` and `clientSecret` in the next step.

### 2. Create an OAuth App on GitHub

Go to GitHub, click your profile picture (in the top right corner) and select "Settings" from the drop down menu.
At the bottom of the list on the left, select "Developer settings", then click "New OAuth App".

Fill in the form using your `binderhub_url` and `jupyter_url` from [Step 1: Editing `config.yaml`](#1-editing-configyaml) (see image below) and click "Register Application".
The URL entered into the "Authorization callback URL" field **must** match your `auth: github: callbackUrl:` in your `config.yaml`.

<html><img src="github_oauth.png" alt="github_oauth" height="578" width="561"></html>

Once your App is registered, a Client ID and Client Secret will be generated.
Copy these into the `clientId` and `clientSecret` fields, as strings, respectively.

### 3. Update your BinderHub

To apply the config changes, we need to upgrade the deployed Helm chart using the same command as in [Step 5: Connect JupyterHub and BinderHub](#5-connect-jupyterhub-and-binderhub).
```bash
helm upgrade binderhubhub jupyterhub/binderhub \
    --version=0.2.0-3b53fce \
    -f secret.yaml -f config.yaml
```

Now reload your Binder page, you should see a sign in button and will be asked for your GitHub sign in information!

## Tearing Down your BinderHub Deployment

Adapted from [Tearing Everything Down](https://zero-to-jupyterhub.readthedocs.io/en/latest/turn-off.html).

When you're no longer using your BinderHub, you should destroy it to avoid paying extra costs for it!
This involves deleting the Helm release and all of the computing resources in Azure.

### 1. Delete the Helm release

First we delete the Helm release that installed the JupyterHub and BinderHub and any resources that it created.
```bash
helm delete binderhub --purge
```
**NOTE:** `binderhub` is the release name we defined in [Step 4: Install BinderHub](#4-install-binderhub).

### 2. Delete the Kubernetes Namespace

Next we delete the Kubernetes namespace the hub was installed in.
This will delete any disks that were created to store user's data and any IP addresses.
```bash
kubectl delete namespace binderhub
```

### 3. Delete your Resource Group

You can list your active resource groups using the following command.
```bash
az group list --output table
```

You can then delete the group for your BinderHub.
```bash
az group delete --name testhub
```
**NOTE:**
  * Be careful to select the correct resource group as this step will irreversibly delete all the resources in that group!
  * `testhub` is the `name`/`namespace` we created in [Step 3: Create a Resource Group](#3-create-a-resource-group).

You can use the [Azure Portal](https://azure.microsoft.com/en-gb/features/azure-portal/) to double check all of your resources have been deleted.
It may take a few minutes to clear up, but nothing relating to your BinderHub should remain after this step.

### 4. GitHub OAuth App

If you enabled GitHub authentication on your BinderHub, don't forget to delete the OAuth Application in "Developer Settings" as well.

## Example config files

### `secret.yaml`

```yaml
jupyterhub:
  hub:
    services:
      binder:
        apiToken: "<output of FIRST 'openssl rand -hex 32' command>"
  proxy:
    secretToken: "<output of SECOND 'openssl rand -hex 32' command>"

registry:
  username: <docker-id>
  password: <password>
```

### `config.yaml`

```yaml
config:
  BinderHub:
    use_registry: true
    image_prefix: <docker-id OR organisation-name>/<prefix>-
    hub_url: http://<EXTERNAL-IP from Step 5>
```

## Glossary of Kubernetes terms

* **Cluster**: a group of computing machines (real or virtual) to deploy apps or containers into
* **Deployment**: instructions to Kubernetes on how to update instances of a deployed application
* **Nodes**: Workers that run the applications
* **Pod**: a Kubernetes abstraction representing a group of one or more application containers and some shared resources
* **Service**: an abstraction defining a set of Pods and how they can be accessed; a Service is defined using YAML (or JSON) and allows applications to receive traffic/be exposed outside of the Cluster
