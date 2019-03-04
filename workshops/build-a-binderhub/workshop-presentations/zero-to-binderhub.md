# Zero to BinderHub! <a name="title"></a>

Sarah Gibson, _The Alan Turing Institute_

**BinderHub Documentation:**
* [Step Zero: Setting up a Kubernetes Cluster](https://zero-to-jupyterhub.readthedocs.io/en/latest/create-k8s-cluster.html)
* [Setup JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-jupyterhub)
* [Setup BinderHub](https://binderhub.readthedocs.io/en/latest/setup-registry.html#set-up-the-container-registry)

To follow along with these instructions, go to this link: [**bit.ly/sg-zero-to-binderhub**](http://bit.ly/sg-zero-to-binderhub)

## Cloud Resource Requirements <a name="cloudresoures"></a>

This workshop assumes you have a "Free Trial" subscription with [Microsoft Azure](https://azure.microsoft.com/en-gb/).
It's quick to set one up and you get £150 free credit for the first 30 days as well as access to some _always free_ services.

> BinderHub is Cloud-neutral.
> We are using Azure as an example.

## Container Registry <a name="containerreg"></a>

These instructions will link the BinderHub to a [DockerHub](https://hub.docker.com/) Container Registry, and so you will need a DockerHub account as well.

> BinderHub also works with Google Container Registry and custom registries.
> We are using DockerHub as an example.

## Installation Requirements <a name="installation"></a>

This workshop will use a terminal (as opposed to Azure's [Cloud Shell](https://azure.microsoft.com/en-gb/features/cloud-shell/) interface) and so we require some command line interfaces.

* **Azure CLI:** Installation guidelines found [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
* **Kubernetes CLI (`kubectl`):** Installation guidelines found [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos)
* **Helm (Kubernetes package manager):** Installation guidelines found [here](https://helm.sh/docs/using_helm/#installing-helm)

We used Homebrew on MacOS to install these:
```bash
brew install azure-cli
brew install kubernetes-cli
brew install kubernetes-helm
```

## Deploying a Kubernetes cluster on Azure <a name="k8s"></a>

Adapted from [Step Zero: Kubernetes on Microsoft Azure Container Service (AKS)](https://zero-to-jupyterhub.readthedocs.io/en/latest/microsoft/step-zero-azure.html).

### 1. Login to Azure <a name="aks-step1"></a>

```bash
az login
```

This command will open a browser window for you to log in to your Azure account.
You can safely close this window after logging in.

### 2. Activate your Subscription <a name="aks-step2"></a>

To see a list of Azure subscriptions you have available to you, you can run the following command:
```bash
az account list --refresh --output table
```
This prints your subscriptions to the terminal in a human-readable format.

You should only see a "Free Trial" subscription (unless you have used Azure before and have others).
Let's activate this with the following command:
```bash
az account set -s "Free Trial"
```
**N.B.:** If you wish to use a different subscription, replace the text in quotes with the name of your chosen subscription.

### 3. Create a Resource Group <a name="aks-step3"></a>

Resource Groups are how the Azure environment manages services that are related to each other (further details in [this blog post](http://www.onlinetech.com/resources/references/how-to-use-azure-resource-groups-a-simple-explanation)).
We will create a resource group in a specific data location and create computational resources _within_ this group.

```bash
az group create --name=shf_test_hub \
    --location="West Europe" \
    --output table
```
* `--name` specifies the name of your resource group and should be something that uniquely identifies this hub.
* `--location` specifies the location of the data centre where your resource will exist.
  A list of data centre locations can be found [here](https://docs.microsoft.com/en-us/azure/aks/container-service-quotas#region-availability).
* `--output table` specifies the output should be in human-readable format as opposed to JSON, which is the default output.

### 4. Choose a Cluster Name <a name="aks-step4"></a>

Somewhere on your machine (e.g. `~/Desktop`), create a folder in which to store files relating to the compute cluster we are about to build.
This folder should have the same name as the cluster and should be descriptive and short.

```bash
mkdir shfhubcluster
cd shfhubcluster
```

> **Discussion topic for later in the day:**
> As a team of RSEs managing a BinderHub, where would the best place for folders such as this to live?

### 5. Create an SSH key <a name="aks-step5"></a>

Create an SSH key to secure your cluster (further details in [this blog post](https://jumpcloud.com/blog/what-are-ssh-keys-b/)). **Keep these files safe.**

```bash
ssh-keygen -f ssh-key-shfhubcluster
```
When prompted for a password, you can choose to leave this blank.
Some text will be printed to the terminal which you don't need to do anything with.

### 6. Create an Azure Container Service (AKS) Cluster <a name="aks-step6"></a>

This command will request a Kubernetes cluster within the resource group we created.
It will request one `Standard_D2s_v3` virtual machine which a Kubernetes cluster installed.
For information on other types of virtual machines available, [see here](https://azure.microsoft.com/en-gb/pricing/details/virtual-machines/series/).

**N.B.:** If you are _not_ using a Free Trial subscription, try setting `--node-count` to **3** instead.

```bash
az aks create --name shfhubcluster \
    --resource-group shf_test_hub \
    --ssh-key-value ssh-key-shfhubcluster.pub \
    --node-count 1 \
    --node-vm-size Standard_D2s_v3 \
    --output table
```
* `--name` is the cluster name we defined in [Step 4](#aks-step4).
* `--resource-group` is the resource group we created in [Step 3](#aks-step3).
* `--ssh-key-value` is the ssh public key we created in [Step 5](#aks-step5).
* `--node-count` is the number of desired nodes in the Kubernetes cluster.
* `--node-vm-size` is the size of the nodes you wish to use, which varies based on the use-case of the cluster and how much RAM/CPU each user will need.

**N.B.:** The default version of Kubernetes will be installed, you can use the `--kubernetes-version` flag to install a different version.

**This step may take a few minutes to execute.**

### 7. Get credentials from Azure for `kubectl` <a name="aks-step7"></a>

This step automatically updates your Kubernetes client configuration file to be configured with the cluster we've just deployed.

```bash
az aks get-credentials --name shfhubcluster \
    --resource-group shf_test_hub \
    --output table
```
* `--name` is the cluster name defined in [Step 4](#aks-step4).
* `--resource-group` is the resource group created in [Step 3](#aks-step3).

### 8. Check the Cluster is Fully Functional <a name="aks-step8"></a>

```bash
kubectl get node
```

The output of this command should list one node (unless you changed `--node-count` in [Step 6](#aks-step6)) with a `STATUS` of `READY`.
The `VERSION` field reports which version of Kubernetes is installed.

Example output:
```bash
NAME                       STATUS   ROLES   AGE   VERSION
aks-nodepool1-97000712-0   Ready    agent   19m   v1.9.11
```

## Setting up Helm <a name="helm"></a>

Adapted from [Zero-to-JupyterHub: Setting up and Securing Helm](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html).

### 1. Setup a `ServiceAccount` for `tiller` <a name="helm-step1"></a>

When you (a human) accesses your Kubernetes cluster, you are authenticated as a particular **User Account**.
Processes in containers running in _pods_ are authenticated as a particular **Service Account**.
More details [here](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/).

```bash
kubectl --namespace kube-system create serviceaccount tiller
```

### 2. Give the `ServiceAccount` full permissions to manage the cluster <a name="helm-step2"></a>

This step enables Role Based Access Control (RBAC) so Kubernetes can secure which pods/users can perform what kind of actions on the cluster.
If RBAC is disabled, **all pods are given `root` equivalent permission on all the Kubernetes nodes and the cluster itself.**
This can leave the cluster vulnerable to attacks.

```bash
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
```

### 3. Initialise `helm` and `tiller` <a name="helm-step3"></a>

This step will create a `tiller` deployment in the `kube-system` namespace and set-up your local `helm` client.

```bash
helm init --service-account tiller --wait
```

### 4. Secure Helm <a name="helm-step4"></a>

Secure `tiller` from access inside the cluster.

`tiller`s port is exposed in the cluster without authentication and if you probe this port _directly_ (i.e. by bypassing `helm`) then `tiller`s permissions can be exploited.
This step forces `tiller` to listen to commands from `localhost` (i.e. `helm`) _only_ so that e.g. other pods inside the cluster cannot ask `tiller` to install a new chart granting them arbitrary, elevated RBAC privileges and exploit them.

More details [here](https://engineering.bitnami.com/articles/helm-security.html).

```bash
kubectl patch deployment tiller-deploy \
    --namespace=kube-system \
    --type=json \
    --patch='[{
        "op": "add",
        "path": "/spec/template/spec/container/0/command",
        "value": ["/tiller", "--listen=localhost:44134"]
    }]'
```

### 5. Verify the installation <a name="helm-step5"></a>

To verify the correct versions have been installed properly, run the following command.

```bash
helm version
```

You must have at least version 2.11.0 and the client (`helm`) and server (`tiller') versions must match.

Example output:
```bash
Client: &version.Version{SemVer:"v2.12.3", GitCommit:"eecf22f77df5f65c823aacd2dbd30ae6c65f186e", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.12.3", GitCommit:"eecf22f77df5f65c823aacd2dbd30ae6c65f186e", GitTreeState:"clean"}
```
