#!/bin/bash

# Variables
prefix=binder-dev   # Docker image prefix
#jupyter_ip=   # Fill in the IP Address of your JupyterHub here

# Get DockerHub login details here
echo Please provide your DockerHub login details.
read -p "DockerHub ID (NOT email): " docker_id
read -sp "DockerHub password: " docker_pass
echo

# Make secrets directory if it doesn't already exist
mkdir -p secrets

# Populate secret.yaml
sed -e "s/<apiToken>/$(cat secrets/apiToken.txt)/" \
  -e "s/<secretToken>/$(cat secrets/secretToken.txt)/" \
  -e "s/<docker-id>/${docker_id}/" \
  -e "s/<password>/${docker_pass}/" \
  secret-template.yaml > secrets/secret.yaml

# Populate config.yaml
sed -e "s/<docker>/${docker_id}/" \
  -e "s/<prefix>/${prefix}/" \
  config-template.yaml > secrets/config.yaml
#  -e "s/<jupyter-ip>/${jupyter_ip}/" \

# End script with some outputs
echo Your BinderHub files have been configured!
ls secrets/
echo
