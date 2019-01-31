# Reproducible environments

## Setting up docker, taking notes.

- Using [this](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)
- According to that step 1 is setting up a docker repository. Following the instructions for that.
  - Run `sudo apt-get update`
  - Run
    ```
    sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
    ```
   - Add GPG key using `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
   - Verify that's worked by running `sudo apt-key fingerprint 0EBFCD88` and checking the output against the model output they give which is
     ```   
     pub   4096R/0EBFCD88 2017-02-22
           Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
     uid                  Docker Release (CE deb) <docker@docker.com>
     sub   4096R/F273FCD8 2017-02-22
     ```
   - Use `lsb_release -cs` to check my ubuntu distribution, found it's xenial. Don't appear to do anything with the info but it was in the instructions.
   - Run
     ```
     sudo add-apt-repository \
     "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) \
     stable"
     ```
   - Run `sudo apt-get update` again.rjarnold/learning_docker:first_image_online
   - Install docker by `sudo apt-get install docker-ce`
   - Ran `sudo docker run hello-world`, it downloaded something automatically and then came up with a message saying hello and indicating the installation had been sucessful.
     ```
     Hello from Docker!
     This message shows that your installation appears to be working correctly.

     To generate this message, Docker took the following steps:
      1. The Docker client contacted the Docker daemon.
      2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
         (amd64)
      3. The Docker daemon created a new container from that image which runs the
         executable that produces the output you are currently reading.
       4. The Docker daemon streamed that output to the Docker client, which sent it
          to your terminal.

     To try something more ambitious, you can run an Ubuntu container with:
       $ docker run -it ubuntu bashrjarnold/learning_docker:first_image_online

     Share images, automate workflows, and more with a free Docker ID:
       https://hub.docker.com/

     For more examples and ideas, visit:
       https://docs.docker.com/get-started/
     ```
- Listed docker images `sude docker image ls`, and it came up with the hello-world image that came with the download. The instructions didn't include the sudo but without it I get the error `Got permission denied while trying to connect to the Docker daemon socket`. As far as I can tell this issue isn't unique to me or the borrowed computer I'm using. Believe I need `sudo` in front of all my docker commands.
- Ran the hello world using `sudo docker run hello-world` and got the welcome message again but nothing else happened as far as I can tell, which may be what's supposed to happen.
- Made a new directory (docker-practice) and cd into in.rjarnold/learning_docker:first_image_online
- Made a file called app.py which contained
  ```
  from flask import Flask
  from redis import Redis, RedisError
  import os
  import socket

  # Connect to Redis
  redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

  app = Flask(__name__)

  @app.route("/")
  def hello():
      try:
          visits = redis.incr("counter")
      except RedisError:
          visits = "<i>cannot connect to Redis, counter disabled</i>"

      html = "<h3>Hello {name}!</h3>" \
             "<b>Hostname:</b> {hostname}<br/>" \
             "<b>Visits:</b> {visits}"
      return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

  if __name__ == "__main__":
      app.run(host='0.0.0.0', port=80)
  ```
- Made a file called requirements.txt that just read
  ```
  Flask
  Redis
  ```
- Created a file called `Dockerfile` containing
  ```
  # Use an official Python runtime as a parent image
  FROM python:2.7-slim

  # Set the working directory to /app
  WORKDIR /app

  # Copy the current directory contents into the container at /app
  COPY . /app

  # Install any needed packages specified in requirements.txt
  RUN pip install --trusted-host pypi.python.org -r requirements.txt

  # Make port 80 available to the world outside this container
  EXPOSE 80

  # Define environment variable
  ENV NAME World

  # Run app.py when the container launches
  CMD ["python", "app.py"]
  ```
- Then built the docker image and called it "friendlyhello" using `sudo docker build --tag=friendlyhello .`.
- Did `docker image ls` and the firndlyhello image was listed along with hello-world
- Ran the docker image using `sudo docker run -p 4000:80 friendlyhello`, the `-p 4000:80` says to map the container's port (which is 80 as seet in the docker file) to my manchine's 4000 port. As a result when I go to "http://localhost:4000/" on a web browser I get a hello world message, and a note that it couldn't connect to Redis.
- In the terminal used ctrl+C to end the app and get back to the command line.
- Can run the app in the background from the get go by adding a `-d` before the `-p`. 
- Did that then ran `sudo docker container ls` to get a list of active containers which showed that one with a container ID which looks like a git SHA.
- Did `sudo docker container stop the_SHA_like_thing` and the container stopped, so I no longer got the message I got before at "http://localhost:4000/", and when I ls the containers there's none because there's none running.
- Redid it using port 3000 instead of 4000 and it worked fine, so 4000 isn't special.
- Now onto publishing and sharing dockerfiles. Made an account on [https://hub.docker.com/](https://hub.docker.com/).
- Logged into docker via my terminal using `sudo docker login`
- "The notation for associating a local image with a repository on a registry is username/repository:tag. The tag is optional, but recommended, since it is the mechanism that registries use to give Docker images a version." Did `sudo docker tag friendlyhello rjarnold/learning_docker:first_image_online`
- Pushed the image to my account online by `sudo docker tag push rjarnold/learning_docker:first_image_online`
- Refreshed the webpage with my account, the repository had been automatically create and the image placed within it.
- Now try running the image on another machine. On another ubuntu machine I tried running `sudo docker run -p 4000:80 rjarnold/learning_docker:first_image_online` Failed because docker wasn't installed on that machine. 
- Installed docker on that machine and tried again. It regonised the image wasn't on my local machine and downloaded it
- Went to "http://localhost:4000/" and the message was there as expected, so success. It had run without making the directory and files on my machine.


Materials to look at:

- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- https://www.tutorialspoint.com/docker/docker_file.htm
- https://developers.redhat.com/blog/2016/02/24/10-things-to-avoid-in-docker-containers/?intcmp=7016000000127cYAAQ
- https://opensource.com/resources/what-are-linux-containers?intcmp=7016000000127cYAAQ
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459


## Material from hack.md

Main points to cover:
- What is a comutational environment (very brief)
- Why your computational environment (often kind of an afterthought) is actually really important for reproducibility.
- Local computational environments
    - Python `virtualenv` and `venv`, `conda` environments
    - Equivalent for R
- Containers
    - What they are
    - When you would use one locally (as not everyone will need to, depends on complexity of project)
    - How they are used in Binder
    - How they can be used for CI (but CI itself in different chapter)

requirements.txt say install e.g. matplotlib
Breaks because don't have the right version of matplotlib
install packages that require specific versions of other packages, dependancies.
Containers etc. Docker is/like a yaml file

We have a tendency to say we used "python" or "numpy" or "R" for our work, but actually there are different versions of these programming languages and packages which mean things are DIFFERENT across them.

One of the most common problems is coming back to your work after 6 months (maybe after reviewers have finally sent your paper back for revisions, or when you're about to fly off to the conference you applied for ages ago) and realising that your code doesn't work any more! Or maybe it does work but it gives you different answers.

* Need an example of errors from different packages.
  Could be a good crowd sourcing option - ask folks to tell us about their Gotchas!

Need a section on semantic versioning: https://semver.org.
Difference between major, minor and patch upgrades, commonly named as: MAJOR.MINOR.PATCH

It's actually really easy to capture your computational environment:

* `pip freeze`
* equivalent command for `conda`: `conda env export`
* equiv for `R`


As always prevention is better than a cure!
If you can install the specific version at the time of running and not up date it.

Useful to have different environments for different projects so that they don't go out of date! https://conda.io/docs/user-guide/tasks/manage-environments.html

What's great about binder is that it will do all this for you\* - but we recommend that you specifically name the version of

\* Need to be v. careful about phrasing here - repo owner needs to provide information on the computational environment, even if hidden from Binder user.

[Syntax for yaml files, think this resource is open source, and it's hosted on github](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

Yaml's a markup language.

Ultimately Dockerfiles & Travis.yml files do similar things. They define computational environments.

Note the points from this blog post: http://urssi.us/blog/2018/12/21/why-research-software-sustainability-wont-be-fixed-by-containers/

YAML is very standard for configuration files.
It's used for Rmarkdown configurations, at the top of jekyll files and for conda configurations for example.

Indentation important:
- [YAML IDIOSYNCRASIES](https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html)
- [UNDERSTANDING YAML](https://docs.saltstack.com/en/latest/topics/yaml/)

Makefiles

- older option to make things reproducible
- see issue https://github.com/alan-turing-institute/the-turing-way/issues/24
- PHONY will keep track of files created when you run this and not recreate already existing files

## Material from binder.md
Step 1: capture your python environment

https://conda.io/docs/user-guide/tasks/manage-environments.html#exporting-the-environment-file

https://pip.pypa.io/en/stable/reference/pip_freeze/

`conda env export > environment.yml`

Note that you have to be IN this environment to run the command above.

or create the environment.yml file manually somehow

https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file

Binder only supports 2.7.15 for a `requirements.txt` file.

Sarah personally recommends using the conda environment because it allows you to say which python installation you want too.

Binder has tons of examples to capture non-python examples but they are difficult to find:

https://mybinder.readthedocs.io/en/latest/config_files.html
https://mybinder.readthedocs.io/en/latest/sample_repos.html

Note - the `install.R` file is a made up file to install R packages. The standard way of doing this for R users is to use a DESCRIPTION file.

https://mybinder.readthedocs.io/en/latest/config_files.html#install-r-install-an-r-rstudio-environment
https://mybinder.readthedocs.io/en/latest/config_files.html#description-install-an-r-package

Note that the DESCRIPTION file doesn't just install the specific package - it will ALSO install any requirements that you have :smile:


Step 2: go to mybinder.org, add your GitHub repo link (specify more when needed) and hit "launch"

Note: the default binder page opens up into a jupyter **notebook** server. It may be the case that the BETTER solution is to add `?urlpath=lab` to the end of the url so that it opens up a jupyter **lab** environment instead.

Note: difference between lab and notebook environment will (may) need to be covered in computing environment chapter (if we have time!)!

By default python 2 and python 3 are installed.

Jupyter lab allows you to open a *terminal* rather than a notebook.

The terminal doesn't have access to a GUI so importing matplotlib.pyplot or .pylab (graphical stuff) won't work

Q: what's the difference between a console and a terminal?

The console has enough for you to be able to run a bunch of python commands.

The terminal doesn't have access to a graphics card! So the console won't work.

Step 3: copy markdown back into your readme to get a nice "launch binder" button

**CHANGES IN BINDER ARE NOT PUSHED BACK INTO YOUR REPO/DOCKER!**

-> this is technically possible but not a feature offered by the public binder; it can be enabled on a local BinderHub (with some new )



![binder_comic](../figures/binder_comic.png)

## BinderHub

- needs Kubernetes cluster that spins up a bunch of VMs with containers etc. - also does some loadbalancing (Kubernetes [Google developed] being rather new and complex but it can be wrangled to do what you want it to do)
- jupyterLab to create the environments
- repo2docker that grabs repo from GitHub and launches Docker
- BinderHub basically is the high level coordinator for these 3 things and can be accessed through some frontend (the pyblic one being mybinder.org)


Also make this useful to run on local machines/HPCs (that might not be setup for this much networking) to enable data throughput independent of cloud availability
- you don't need all the fancy stuff Kubernetes can do to run a BinderHub -> strip down Kubernetes to the essentials and run that locally

---

[opensource](https://opensource.com/resources/what-docker) **Attribution-ShareAlike 4.0 International**

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

Docker is a tool that is designed to benefit both developers and system administrators, making it a part of many DevOps (developers + operations) toolchains. For developers, it means that they can focus on writing code without worrying about the system that it will ultimately be running on. It also allows them to get a head start by using one of thousands of programs already designed to run in a Docker container as a part of their application. For operations staff, Docker gives flexibility and potentially reduces the number of systems needed because of its small footprint and lower overhead.

Docker brings security to applications running in a shared environment, but containers by themselves are not an alternative to taking proper security measures.

Dan Walsh, a computer security leader best known for his work on SELinux, gives his [perspective](https://opensource.com/business/14/7/docker-security-selinux) on the importance of making sure Docker containers are secure. He also provides a [detailed breakdown](https://opensource.com/business/14/9/security-for-docker) of security features currently within Docker, and how they function.

---

Woes of development can be:

keeping a consistent environment while iterating through new builds
documenting so others can use your code like you already know how to
installing dependent software without conflicting with host versions
consistent testing environment
accountable data and traceable storage
Woes of operations can be:

proper documentation of the software being monitored
process micro-management and resource quotas
network configuration for application requirements
accountable data and traceable storage
By having a standardized image format, development sees all servers the same and operations sees all containers the same. These are the woes that Docker directly addresses. It is first necessary to distinguish the use of "image" and "container" within the Docker environment.

An image
Portable: They can be pushed to a registry, or saved as a tar archive.

Layered: The steps in producing an image, are added in layers. In this way, images that are mostly the same, except for the last few steps, can reduce disk usage by sharing parent layers.

Static: The contents are not changeable, unless making a new image.

A container
Runtime: An environment for PIDs.

Writable: It is essentially an ephemeral storage.

Layered: It is on an image.

These terms will show up in various contexts, and it is important to see how they relate to each other, but are also their own entities. With this foundation it's time to explore its basic Docker application and capabilities.




## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful
> why we think you should read the whole thing

## Prerequisites / recommended skill level
> other chapters that should have been read before or content you should be familiar with before you read this

## Chapter content
> depending on the content, this might be more structured, e.g. with exercises, gotcha sections etc

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography

[Figure](https://opendreamkit.org/2017/11/02/use-case-publishing-reproducible-notebooks/) **Permission to use granted by Juliette Taka, Logilab and the OpenDreamKit project.**
