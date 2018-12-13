# Locally Installing a BinderHub

Sarah Gibson

_The Alan Turing Institute_

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

### 0. Kubernetes Cloud Resources

Working through these tutorials: [Foundational resources for Kubernetes](https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/)

**Terminology:**
* _Cluster_ is a group of machines (real or virtual) to deploy apps/containers into
* _Master_ automatically handles scheduling across the _Nodes_ in the _Cluster_
* _Nodes_ are workers that run the applications
* _Kubernetes API_ manages communication between _Master_ and _Nodes_
* _Deployment_ configuration instructs Kubernetes on how to update instances of the app being deployed (self-healing)
* _Kubelet_, a process responsible for communication between the Kubernetes _Master_ and the _Node_; it manages the _Pods_ and the containers running on a machine
* _Pod_ is a Kubernetes abstraction that represents a group of one or more application containers and some shared resources for those containers - can include: _Volumes_ (shared storage), Networking (unique cluster IP address), Run info on each container; _Pods_ are mortal and 'die' with their host _Nodes_
* _Service_ is an abstraction defining a set of _Pods_ and how to access them, they enable a loose coupling between dependent _Pods_, a _Service_ is defined using YAML (preferred) or JSON, allow your applications to receive traffic/be exposed outside the _Cluster_
* _LabelSelector_ determines a set of _Pods_ to be targeted by a _Service_, _Services_ without specified _Selectors_ can be manually mapped to _Endpoints_
* _ServiceSpec_ or type: _ClusterIP_ (default) - exposes the _Service_ on an internal IP in the _Cluster_, makes the _Service_ only reachable from within the _Cluster_; _NodePort_ - exposes the _Service_ on the same port of each selected _Node_ in the cluster, makes a _Service_ accessible from outside the _Cluster_; _LoadBalancer_ - creates an external load balancer in the current cloud and assigns a fixed, external IP to the _Service_; and _ExternalName_ - exposes the _Service_ using an arbitrary name (requires `kube-dns>=v1.7`)
* _Scaling_ is changing the number of replicas of a _Deployment_ with user demand
* _Rolling Updates_ allow _Deployments_ to be updated to new versions with zero downtime by incrementally updating _Pod_ instances with new ones

**Required or Potential resources:**
* `minikube` - tool to run Kubernetes locally, runs a single-node Kubernetes _Cluster_ inside a VM on your laptop
* `kubectl` - command line interface using Kubernetes API to interact with _Clusters_

**Learned commands:**
* `minikube version` - prints `minikube` version
* `minikube start` - launches VM
* `kubectl version` - prints `kubectl` version
* `kubectl cluster-info` - prints _Cluster_ details
* `kubectl get nodes` - prints _Node_ information
* `kubectl run __ --image=__ --port=__` - command to deploy a containerised app, `__` needs to be replaced with deployment name, app image location and port location respectively
* `kubectl get deployments` - lists current _Deployments_
* `kubectl proxy` - opens a connection between host and the Kubernetes _Cluster_, proxy enables direct access to the API from these terminals
* `curl http://localhost:8001/version` - query the version on host 8001 directly through API
* `export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metaata.name}}{{"\n"}}{{end}}')` - get the _Pod_ name and store it in POD_NAME (`echo Name of the Pod: $POD_NAME`)
* `curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/` - make an HTTP request to the application running in that _Pod_
* `kubectl get` - list resources, takes arguments such as `services`, `pods`, `deployments`
* `kubectl describe` - show detailed information about a resource (_WARNING:_ `describe` has a lot of output!)
* `kubectl logs` - print the logs from a container in a _Pod_, anything that the application would normally send to `STDOUT` becomes logs for the container within the _Pod_
* `kubectl exec` - execute a command on a container in a _Pod_
* `url http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/` - url is the route to the API of the _Pod_
* `kubectl exec $POD_NAME env` - list the environment variables of a _Pod_
* `kubectl exec -ti $POD_NAME bash` - start a bash session in the _Pod_, use `exit` to... well, exit.
* `kubectl expose __ --type=__` - create and expose a new _Service_
* `kubectl describe deployment` - run to find the name of a _Label_
* `-l` option to a `get` command allows label selection
* `kubectl label pod $POD_NAME app=v1` - assign the label `app=v1` to the _Pod_ called `$POD_NAME` (where this has been exported as above)
* `kubectl delete service -l __` - deletes a _Service_ with a specified label
* `kubectl scale __ --replicas=__` - scale a _Deployment_ to a desired number of instances
* `kubectl set image deployments/current_deployment current_deployment=new_deployment` - initiated a _Rolling Update_ for the new _Deployment_
* `kubectl rollout undo __` - rollback an image to a previous working version

**Installing Minikube and Kubernetes API**

[Docs here](https://kubernetes.io/docs/tasks/tools/install-minikube/)
 
Install a Hypervisor (see link above, I chose VisualBox for macOSX).
 
Install `minikube`:
 ```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.31.0/minikube-darwin-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube
```
 
Start `minikube` (If you have launched the VirtualBox window, or whichever Hypervisor you chose, you will see a VM appear called `minikube` and it's status):
```
minikube start
```
 
Install `kubectl` via `homebrew` (other methods for installation [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)):
```
brew install kubernetes-cli
```
 
Test installation by printing version:
```
kubectl version
```

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

Install the Helm Chart using the Config files you created where `...` is the commit hash of the BinderHub chart version you wish to deploy (list of versions [here](https://jupyterhub.github.io/helm-chart/#development-releases-binderhub)):
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
