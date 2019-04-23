# Kubernetes Cloud Resources

Working through these tutorials: [Foundational resources for Kubernetes](https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/)

## Terminology:
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

## Required or Potential resources:
* `minikube` - tool to run Kubernetes locally, runs a single-node Kubernetes _Cluster_ inside a VM on your laptop
* `kubectl` - command line interface using Kubernetes API to interact with _Clusters_

## Learned commands:
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

## Installing Minikube and Kubernetes API

[Docs here](https://kubernetes.io/docs/tasks/tools/install-minikube/)
 
Install a Hypervisor (see link above, I chose VisualBox for macOSX).
 
Install `minikube` (alternative installation methods [here](https://github.com/kubernetes/minikube/releases)):
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
