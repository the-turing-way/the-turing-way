# Locally Installing a BinderHub

Sarah Gibson

_The Alan Turing Institute_

## Cloning mybinder.org for development

### Getting started

**Installation requirements:**
* Install VirtualBox
  * I chose the OS X host from [here](https://www.virtualbox.org/wiki/Downloads)
* Install `minikube`
  * `brew cask install minikube`
* Install Helm
  * `brew install kubernetes-helm`

### Following the contributing guidelines

Guidelines available [here](https://github.com/jupyterhub/binderhub/blob/master/CONTRIBUTING.md#installation).

#### 0. Initial set-up

These commands were actually ignored as most of the modules were already installed and the second command is Linux-only.

```
sudo apt install python3 python3-pip npm curl
sudo apt install socat
```

#### 1. Clone the BinderHub Repo

```
git clone https://github.com/jupyterhub/binderhub
cd binderhub
```

#### 2. Install minikube

See **Getting started** instructions above.
The guidelines suggest using a script to download `minikube`, arguing that the `brew` method is not stable for Macs.
But this downloads an older version of `minikube` which then cannot install the Hub due to a timeout.
The `brew` install method works fine, however.

Initialise `minikube`:
```
minikube start
```

#### 3. Install and Initialise Helm

Again, see **Getting started** instructions above.

```
helm init
```

#### 5. Add the JupyterHub Helm Charts

```
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update
```

#### 6. Install BinderHub

You may choose to do this step inside a virtual environment, in which case:
```
python3 -m venv venv
source venv/bin/activate
```
Then:
```
python3 -m pip install -e . -r dev-requirements.txt
```

#### 7. Install the Hub

```
./testing/minikube/install-hub
```

#### 8. Set up docker for the minikube cluster

```
eval $(minikube docker-env)
```

#### 9. Start BinderHub

```
python3 -m binderhub -f testing/minikube/binderhub_config.py
```

#### 10. Visit your BinderHub!

Got to `localhost:8585` in your browser and you will see a copy of [mybinder.org](https://mybinder.org/).
Enter a URL for a GitHub repository and hit launch.
BinderHub will then build the docker image for your repo and launch it in an interactive window.

## Creating a Working Environment

* Use `anaconda` to create a working environment with `python-3.6`:
```
conda create --name py3binder python=3.6
conda activate py3binder
```

Any executed code or installed packages should be within this environment where possible.

## Following the Zero-to-BinderHub Documentation

[Docs Here](https://binderhub.readthedocs.io/en/latest/)

**N.B.:** _Zero-to-BinderHub_ Documentation is not clear that you need to set up a Kubernetes Cluster first and no guidelines or links are provided. Hopefully my notes below will make the steps a bit clearer.

**N.B.:** Probably should have done [Zero-to-JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/index.html) first as this seems to have more links/discussion about Kubernetes and Helm, among other things.

### 1. Installing Helm

Helm is the package manager for Kubernetes. Helm packages are called charts. Helm has two parts: a client (`helm`) and a server (`tiller`). `tiller` runs inside of your Kubernetes cluster as a _Pod_ in the kube-system namespace. Tiller manages both, the releases (installations) and revisions (versions) of charts deployed on the cluster. When you run `helm` commands, your local Helm client sends instructions to `tiller` in the _Cluster_ that in turn make the requested changes.

Install `helm`:
```
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
```

Create a `ServiceAccount`:
```
kubectl --namespace kube-system create serviceaccount tiller
```

Give the `ServiceAccount` full permissions to manage the cluster:
```
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
```

Initialise `helm` and `tiller`
```
helm init --service-account tiller
```

Verify the installation:
```
helm version
```
The versions for the _Client_ and the _Server_ must match!

Secure Helm (details [here](https://engineering.bitnami.com/articles/helm-security.html)):
```
kubectl patch deployment tiller-deploy --namespace=kube-system --type=json --patch='[{"op": "add", "path": "/spec/template/spec/containers/0/command", "value": ["/tiller", "--listen=localhost:44134"]}]'
```

### 2. Setting up the Container Registry

BinderHub will build Docker images from Git repositories and push them to a Docker registry. JupyterHub then launches the user servers based on these Docker images. Two most popular registries are Google Container Registry and DockerHub. I am going to use DockerHub since I already have an account. Also, the Turing may have an organisation on DockerHub which would be ideal for the final BinderHub build.

The configuration of DockerHub with BinderHub has been amalgamated with the next section on [Zero-to-BinderHub](https://binderhub.readthedocs.io/en/latest/).

### 3. Set up BinderHub

The next section will cover how to configure the Helm Chart and how to create the BinderHub deployment. Further info on Helm Charts (and Kubernetes among others) available here: [Zero-to-JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/tools.html#helm).

We need to generate several pieces of information and store them in a YAML file to configure the BinderHub.

**Preparing Configuration Files**

Create a folder to store the config files:
```
mkdir binderhub
cd binderhub
```

Create two random tokens by running the following commands then copying the outputs (run twice to get two keys):
```
openssl rand -hex 32
openssl rand -hex 32
```

Create a file called `secret.yaml` containing the following:
```
jupyterhub:
  hub:
    services:
      binder:
        apiToken: "<output of FIRST `openssl rand -hex 32` command>"
  proxy:
    secretToken: "<output of SECOND `openssl rand -hex 32` command>"
```

Configure this file to connect with our registry (DockerHub) by adding the following to `secret.yaml`:
```
registry:
  username: <docker-id>
  password: <password>
```
**WARNING:** THIS IS YOUR ACTUAL PASSWORD. DO NOT GRANT ANYONE ACCESS TO THIS FILE.

Create a `config.yaml` file containing the following:
```
config:
  BinderHub:
    use_registry: true
    image_prefix: <docker-id|organization-name>/<prefix>-
```
**N.B.:**
* `<docker-id|organization-name>` is where you want to store Docker images. This can be your Docker ID account or an organization that your account belongs to.
* `<prefix>` can be any string, and will be prepended to image names. Recommend something descriptive such as `binder-dev-` or `binder-prod-` (ending with a - is useful).

**Installing BinderHub**

Get the latest Helm Chart for BinderHub:
```
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart
helm repo update
```

Install the Helm Chart using the Config files you created where `...` is the commit hash of the BinderHub chart version you wish to deploy (list of versions [here](https://jupyterhub.github.io/helm-chart/#development-releases-binderhub), I chose the top one):
```
helm install jupyterhub/binderhub --version=0.1.0-...  --name=<choose-name> --namespace=<choose-namespace> -f secret.yaml -f config.yaml
```
`name` and `namespace` should be short and descriptive. Can be different but recommended that they are the same.

This installation step will deploy both a BinderHub and a JupyterHub, but they are not yet set up to communicate with each other. We’ll fix this in the next step. Wait a few moments before moving on as the resources may take a few minutes to be set up.

To connect JupyterHub and BinderHub, get the IP address of the JupyterHub deployment:
```
kubectl --namespace=<namespace-from-above> get svc proxy-public
```
**WARNING:** `EXTERNAL_IP` field reports `<pending>` for aaaaaagggggeeeeeesssss. Seriously, go get _several_ coffees...
