# Alternative binderhub-build on Digital Ocean
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/DigitalOcean_logo.svg/145px-DigitalOcean_logo.svg.png?download" style="height:20px">

### Instead of azure-cli
#### we need doctl (Digital Ocean ConTroL)
`wget https://github.com/digitalocean/doctl/releases/download/v1.13.0/doctl-1.13.0-linux-amd64.tar.gz`
`tar -xvf doctl-1.13.0-linux-amd64.tar.gz`
`sudo mv doctl /usr/bin/`

### Instead of az-login
You'll need an authentication token. Login to digital ocean online. Select API and then generate a new token. Give it a cool name, like 'bindertime'.
`doctl auth init`

## Create your cluster!
digital ocean's k8s support from the command line is in beta, but it works fine`
`export DIGITALOCEAN_ENABLE_BETA=1`

`doctl k8s cluster create bindertime-k8s --region lon1 --version 1.12.1-do.2 --node-pool="name=worker-pool;count=2"`

### Save config file
Make a directory to store your config
`mkdir binderhub; cd binderhub`
`doctl k8s cluster kubeconfig show bindertime-k8s > config.yaml`

### Check we are up and running
`kubectl --kubeconfig='config.yaml' get node`

### Setting up Helm
Same as in azure case, but you might need the `--kubeconfig='config.yaml'` flag.

### Automate creation of the config files
```
docker_id=alexmorley
docker_pass=*********
docker_prefix=alex-binder-
```

```
token1=`openssl rand -hex 32`
token2=`openssl rand -hex 32`
cat <<EOF > secret.yaml
jupyterhub:
  hub:
    services:
      binder:
        apiToken: $token1
  proxy:
    secretToken: $token2
registry:
  username: $docker_id
  password: $docker_pass
EOF
```
and then:
```
cat <<EOF > config.yaml
config:
  BinderHub:
    use_registry: true
    image_prefix: $docker_id/$docker_prefix
EOF
```
