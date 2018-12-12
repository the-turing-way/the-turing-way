# Locally Installing a BinderHub

Sarah Gibson

_The Alan Turing Institute_

## Creating a Working Environment

* Use `anaconda` to create a working environment with `python-3.6`:
```
conda create --name py3binder python=3.6
conda activate py3binder
```

## Following the Zero-to-BinderHub Documentation

[Docs Here](https://binderhub.readthedocs.io/en/latest/)

### 0. Kubernetes Cloud Resources

Working through these tutorials:
1. [Foundational resources for Kubernetes](https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/)

**Terminology:**
* Cluster is a group of machines (real or virtual) to deploy apps/containers into
* Master automatically handles scheduling across the Nodes in the cluster
* Nodes are workers that run the applications
* Kubernetes API manages communication between Master and Nodes
* Deployment configuration instructs Kubernetes on how to update instances of the app being deployed (self-healing)
* Kubelet, a process responsible for communication between the Kubernetes Master and the Node; it manages the Pods and the containers running on a machine
* Pod is a Kubernetes abstraction that represents a group of one or more application containers and some shared resources for those containers - can include:
  * Volumes (shared storage)
  * Networking (unique cluster IP address)
  * Run info on each container
*

**Required or Potential resources:**
* `minikube` - tool to run Kubernetes locally, runs a single-node Kubernetes cluster inside a VM on your laptop
* `kubectl` - command line interface using Kubernetes API to interact with clusters

**Learned commands:**
* `minikube version` - prints `minikube` version
* `minikube start` - launches VM
* `kubectl version` - prints `kubectl` version
* `kubectl cluster-info` - prints cluster details
* `kubectl get nodes` - prints node information
* `kubectl run __ --image=__ --port=__` - command to deploy a containerised app, `__` needs to be replaced with deployment name, app image location and port location respectively
* `kubectl get deployments` - lists current deployments
* `kubectl proxy` - opens a connection between host and the Kubernetes cluster, proxy enables direct access to the API from these terminals
* `curl http://localhost:8001/version` - query the version on host 8001 directly through API
* `xport POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metaata.name}}{{"\n"}}{{end}}')` - get the pod name and store it in POD_NAME (`echo Name of the Pod: $POD_NAME`)
* `curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/` - make an HTTP request to the application running in that pod
* `kubectl get` - list resources
* `kubectl describe` - show detailed information about a resource
* `kubectl logs` - print the logs from a container in a pod
* `kubectl exec` - execute a command on a container in a pod

### 1. Installing Helm

* Standard installation method:
```
$ curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
$ helm init
```

* Using an alternative installation method:
```
$ curl https://raw.githubusercontent.com/helm/helm/master/scripts/get > get_helm.sh
$ chmod 700 get_helm.sh
$ ./get_helm.sh
$ helm init --service-account default
```

Both methods produce errors when `helm init` is run:
```
Error: error installing: Post http://localhost:8080/apis/extensions/v1beta1/namespaces/kube-system/deployments: dial tcp [::1]:8080: connect: connection refused
```

Found [this issue](https://github.com/helm/helm/issues/3460) on the topic.

**N.B.:** _Zero-to-BinderHub_ Documentation not clear that you need to set up a Kubernetes Cluster first and no guidelines or links are given in the documentation. (Go to section 0.)

