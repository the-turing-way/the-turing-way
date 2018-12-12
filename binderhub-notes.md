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

* [Foundational resources for Kubernetes](https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/)

Began working through the

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

_Zero-to-BinderHub_ Documentation not clear that you need to set up a Kubernetes Cluster first and no guidelines or links are given in the documentation. 

