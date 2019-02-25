# Reproducible environments

- What is a computational environment?
- Why is important to capture for reproducibility
- Ways to capture computational environments
  - Very quick runthrough with advice on **which to use for which circumstances**
  - Making environments via conda etc **Other language equivalents?**
    - Reasons to do so
    - How to do it
    - mention pip freeze
  - YAML files
    - What are they
    - Syntax/tutorials
    - Gotchas
    - **Are there standard structures for yaml files/how does a novice know what to include?**
    - Quick note on security issues?
    - **How to use them for reproducibility**
      - Say can export yml from conda and create environments from them. **Other language equivalents?**
  - Binder
    - What it is
    - How to use it to capture an environments
    - mybinder config files
  - Virtual machines
    - ?
  - Images and Containers
    - What are they
    - How to use Docker to make/share images and run containers (warn need to be ok with it being open unless dockerhub)
    - **Are there less arduous ways of generating Dockerfiles/images than hand writing them? Yes, build on previous well tested ones**
    - **Are there standard structures for Dockerfiles/how does a novice know what to include?**
    - Mention Singularity (+ others maybe) and give a quick pros/cons.
  - Makefiles
    - What they are
    - How to write them to use them for reproducibility.


- feedback on order?
- Python centric (standard ways of capturing environment in other languages that I don't know about?)
- Missing anything?
- Which to use in which circumstances


## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| Experience with the command line | Necessary | Experience with downloading software via the command line is particularly useful |
| Version control | Helpful | Particularly with using version control via GitHub |

Recommended skill level: intermediate-advanced.

## Summary
> easy to understand summary - a bit like tl;dr


### What is a computational environment?

Computational environment is (in broad terms) the system setup where a program is being run. This includes features of hardware (e.g. numbers of cores in any CPUs) and features of software (e.g. the operating system, what programming languages are installed, which supporting packages/versions of those packages are included, what other pieces of software are installed and how are they configured).

Software versions are often defined  via [semantic versioning](https://semver.org). In this system three numbers, e.g 2.12.4 are used to define each version of a piece of software. When a change is made to the software then its version is incremented. These three numbers follow the pattern MAJOR.MINOR.PATCH, and are incremented as follows:

- MAJOR: significant changes.
- MINOR: to add functionality.
- PATCH: for bug fixes.

Materials used: [semantic versioning](https://semver.org)

## How this will help you/ why this is useful

The pervasive use of computation for scientific discovery has ushered in a new type of scientific research process. Researchers, irrespective of scientific domain, routinely rely on large amounts of data, specialized computational infrastructure, and sophisticated analysis processes from which to test hypotheses and derive results. While scholarly research has evolved significantly over the past decade, the same cannot be said for the methods by which research processes are captured and disseminated. In fact, the primary method for dissemination – the scholarly publication –is largely unchanged since the advent of the scientific journal in the 1660’s. This disparity has led many to argue that the scholarly publication is no longer sufficient to verify, reproduce, and extend scientific results. Despite the increasing recognition of the need to share all aspects of the research process, scholarly publications today are often disconnected from the underlying analysis and environment that produced the findings.

Let's go though an example of why computational environments are important. Say I have a very simple python script:

```
a = 1
b = 5
print(a/b)
```

One divided by five is `0.2`, and that is what is printed if this script is run using python 3. However if a slightly older version of python, python 2, is used the result printed is `0` because both a and b are integers so in python 2 an integer is returned. Therefore this simple, simple script returns *different* answers depending on the computational environment it is run in. This is a mistake that would be very easy to make, and demonstrates how a perfectly valid piece of code can output different results depending on the environment it is run in.

If such bugs can impact a simple script like this you can only imagine how many could appear in a complex analysis procedure which may involve thousands of lines of code and dozens of dependent packages/pieces of software. Therefore even if a researcher shares their code and any associated data a colleague could not confidently reproduce their work unless they also knew the computational environment to run the analysis in. Similarly if you need to come back to an old piece of your own work (as is common in research), but have updated packages since then you may find your code generating different results or not working at all. Trying to fix these kinds of issues is often time consuming and frustrating as you have to figure out what in your computational environment has changed. This is particularly difficult if you have no record of what your computational environment was when you carried out the research.

This chapter will describe how to capture, preserve and share computational environments along with code to ensure research is reproducible.

For the research to be reproducible the researcher must be able to publish and distribute the entire contained analysis not just its results. The analysis should be *mobile*. Mobility of compute is defined as the ability to define, create, and maintain a workflow locally while remaining confident that the workflow can be executed elsewhere. In essence, mobility of compute means being able to contain the entire software stack, from data files up through the library stack, and reliability move it from system to system. Any product that is limited to where it can be deployed is instantly limited in the extent that it can be reproduced.

Materials used:
[A. Brinckman, et al., Computing environments for reproducibility: Capturing the "Whole Tale", Future Generation Computer Systems (2018), https://doi.org/10.1016/j.future.2017.12.029](https://www.sciencedirect.com/science/article/pii/S0167739X17310695) **Attribution 4.0 International (CC BY 4.0)**, [Paper presenting singularity](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) **CC0 1.0 Universal (CC0 1.0)**

## Ways to capture computational environments

There are a number of ways to capture a computational environment, and which is the most appropriate for you will depend  on the nature of your project. If you are working with languages such as Python and R which have a number of tools for freezing and exporting environments as YAML files (discussed later in this chapter) then using one of those tools is likely the best course of action.

*Outline other and why*


- As always prevention is better than a cure! If you can install the specific version at the time of running and not up date it.
  - requirements.txt say install e.g. matplotlib
  - Breaks because don't have the right version of matplotlib
  - install packages that require specific versions of other packages, dependancies.
  - Useful to have different environments for different projects so that they don't go out of date! https://conda.io/docs/user-guide/tasks/manage-environments.html
  - Local computational environments
    - Python `virtualenv` and `venv`, `conda` environments
    - Equivalent for R



The advent of virtual machines [4, 5] introduced the exciting reality than an entire environment, including software dependencies, libraries, runtime code, and data, could be encapsulated and run anywhere. Virtual machines, however, also introduced large computational overhead due to the required level of virtualization for emulating the OS and kernel. With the addition of lightweight virtualization features to the Linux kernel (e.g., namespaces) a new lightweight virtualization, containers [15, 16], became possible to implement. Implementations such as Docker, one of the container solutions made open source in 2013 [15, 16], offered additional improvements over standard virtual machines. Containers could share resources with the host without incurring much of the performance penalties of hardware-level virtualization [17].

Researchers can develop reproducible containers on their local machines, providing a simple way to collaborate on code or applications without the hassle of having different software versions or broken dependencies. Containers are ideal not just for the final analysis, but for the development of it. A user is most comfortable working with his or her text editor, programs, and environment of choice, and containers make it possible to work locally and develop in a specific environment simultaneously.

If you need to work with HPC containers save having to install a whole bunch of stuff on the cluster before you can, and installing may not even be possible if you need to download form the internet.

One of the major factors that prevents Docker from being the standard container technology in HPC is its security concerns. From an IT security perspective, a machine can be considered compromised if any user is able to run arbitrary code as the root user. While Docker takes steps to mitigate the risk of allowing users to run arbitrary code, there is a fatal design flaw that limits Docker’s ability to run in HPC environments: for every container that Docker runs, the container process is spawned as a child of a root owned Docker daemon. As the user is able to directly interact with and control the Docker daemon, it is theoretically possible to coerce the daemon process into granting the users escalated privileges. Any user being able to escalate up to system administrator status, a user called “root”, would introduce unthinkable security risks for a shared compute environment.
[Paper presenting singularity](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) **CC0 1.0 Universal (CC0 1.0)**



### YAML files


- It's actually really easy to capture your computational environment:
  - `pip freeze` https://pip.pypa.io/en/stable/reference/pip_freeze/
  - equivalent command for `conda`: `conda env export`
  - equiv for `R`
  - `conda env export > environment.yml` https://conda.io/docs/user-guide/tasks/manage-environments.html#exporting-the-environment-file Note that you have to be IN this environment to run the command.
- or create the environment.yml file manually somehow
  - https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file

[yaml tutorial](https://gettaurus.org/docs/YAMLTutorial/) **[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)**

YAML is an indentation-based markup language which aims to be both easy to read and easy to write. Many projects use it for configuration files because of its readability, simplicity and good support for many programming languages. It can be used for a great many things including defining computational environments, and is well integrated with [Travis](https://travis-ci.org/) which is discussed in the chapter on continuous integration.

An a YAML file defining a computational environment might look something like this:

```
#Define the operating system as Linux
os: linux

#Use the xenial distribution of Linux
dist: xenial

#Use the programming language python
language: python

#Use version of python 3.2
python: 3.2

#Use the python package numpy and use the 1.16.1 version
packages:
  numpy:
    version: 1.16.1
```

A YAML document can consist of the following elements.

#### Scalars

Scalars are ordinary values: numbers, strings, booleans.
```
number-value: 42
floating-point-value: 3.141592
boolean-value: true
# strings can be both 'single-quoted` and "double-quoted"
string-value: 'Bonjour'
```

Note here that comments can be added by preceding them with a `#`.

YAML syntax also allows unquoted string values for convenience reasons:
```
unquoted-string: Hello World
```

#### Lists and Dictionaries

Lists are collections of elements:

```
jedis:
  - Yoda
  - Qui-Gon Jinn
  - Obi-Wan Kenobi
  - Luke Skywalker
```

Every element of the list is indented and starts with a dash and a space.

Dictionaries are collections of `key: value` mappings. All keys are case-sensitive.

```
jedi:
  name: Obi-Wan Kenobi
  home-planet: Stewjon
  species: human
  master: Qui-Gon Jinn
  height: 1.82m
```

Note that a space after the colon is mandatory.

#### YAML Gotchas

Due to the format aiming to be easy to write and read, there're some ambiguities in YAML.

- **Special characters in unquoted strings:** YAML has a number of special characters you cannot use in unquoted strings. For example, parsing the following sample will fail:
  ```
  unquoted-string: let me put a colon here: oops
  ```
  Quote the string value makes this value unambiguous:
  ```
  unquoted-string: "let me put a colon here: oops"
  ```
  Generally, you should quote all strings that contain any of the following characters: `[] {} : > |`.
- **Tabs versus spaces for indentation:** do *not* use tabs for indentation. While resulting YAML can still be valid, this can be a source of many subtle
parsing errors. Just use spaces.

#### How to use YAML to define computational environments

### Images and containers

*Have Docker running through this like git in version control.*

- An image
  - Portable: They can be pushed to a registry, or saved as a tar archive.
  - Layered: The steps in producing an image, are added in layers. In this way, images that are mostly the same, except for the last few steps, can reduce disk usage by sharing parent layers.
  - Static: The contents are not changeable, unless making a new image.
- A container
  - Runtime: An environment for PIDs.
  - Writable: It is essentially an ephemeral storage.
  - Layered: It is on an image.
- Ultimately Dockerfiles & Travis.yml files do similar things. They define computational environments. Say Singularity also exists.
- When you would use one locally (as not everyone will need to, depends on complexity of project)
- How they can be used for CI (but CI itself in different chapter)
- Note the points from this blog post: http://urssi.us/blog/2018/12/21/why-research-software-sustainability-wont-be-fixed-by-containers/


[What are containers](https://opensource.com/resources/what-are-linux-containers?intcmp=7016000000127cYAAQ) **CC BY-SA 4.0**

Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. And they are designed to make it easier to provide a consistent experience as developers and system administrators move code from development environments into production in a fast and replicable way.

In a way, containers behave like a virtual machine. To the outside world, they can look like their own complete system. But unlike a virtual machine, rather than creating a whole virtual operating system, containers don't need to replicate an entire operating system, only the individual components they need in order to operate. This gives a significant performance boost and reduces the size of the application.

Undoubtedly, one of the biggest reasons for recent interest in container technology has been the Docker open source project, a command line tool that made creating and working with containers easy for developers and sysadmins alike, similar to the way Vagrant made it easier for developers to explore virtual machines easily.

Docker is a command-line tool for programmatically defining the contents of a Linux container in code, which can then be versioned, reproduced, shared, and modified easily just as if it were the source code to a program.

Containers have also sparked an interest in microservice architecture, a design pattern for developing applications in which complex applications are broken down into smaller, composable pieces which work together. Each component is developed separately, and the application is then simply the sum of its constituent components. Each piece, or service, can live inside of a container, and can be scaled independently of the rest of the application as the need arises.

Simply putting your applications into containers probably won't create a phenomenal shift in the way your organization operates unless you also change how you deploy and manage those containers. One popular system for managing and organizing Linux containers is Kubernetes.

Kubernetes is an open source system for managing clusters of containers. To do this, it provides tools for deploying applications, scaling those application as needed, managing changes to existing containerized applications, and helps you optimize the use of the underlying hardware beneath your containers. It is designed to be extensible, as well as fault-tolerant by allowing application components to restart and move across systems as needed.

[What is docker](https://opensource.com/resources/what-docker) **CC BY-SA 4.0**

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

In a way, Docker is a bit like a virtual machine. But unlike a virtual machine, rather than creating a whole virtual operating system, Docker allows applications to use the same Linux kernel as the system that they're running on and only requires applications be shipped with things not already running on the host computer. This gives a significant performance boost and reduces the size of the application.

For developers, it means that they can focus on writing code without worrying about the system that it will ultimately be running on.

Docker is a tool that is designed to benefit both developers and system administrators, making it a part of many DevOps (developers + operations) toolchains. For developers, it means that they can focus on writing code without worrying about the system that it will ultimately be running on. It also allows them to get a head start by using one of thousands of programs already designed to run in a Docker container as a part of their application. For operations staff, Docker gives flexibility and potentially reduces the number of systems needed because of its small footprint and lower overhead.

Docker brings security to applications running in a shared environment, but containers by themselves are not an alternative to taking proper security measures.

Dan Walsh, a computer security leader best known for his work on SELinux, gives his [perspective](https://opensource.com/business/14/7/docker-security-selinux) on the importance of making sure Docker containers are secure. He also provides a [detailed breakdown](https://opensource.com/business/14/9/security-for-docker) of security features currently within Docker, and how they function.


### Makefiles
  - older option to make things reproducible
  - see issue https://github.com/alan-turing-institute/the-turing-way/issues/24
  - PHONY will keep track of files created when you run this and not recreate already existing files

## Binder

- ![binder_comic](../figures/binder_comic.png)
- \* Need to be v. careful about phrasing here - repo owner needs to provide information on the computational environment, even if hidden from Binder user.
- What's great about binder is that it will do all this for you\* - but we recommend that you specifically name the version of
- **CHANGES IN BINDER ARE NOT PUSHED BACK INTO YOUR REPO/DOCKER!** this is technically possible but not a feature offered by the public binder; it can be enabled on a local BinderHub (with some new )
- Step 1: capture computational environment
  - How Dockerfiles/images/containers are used in Binder
  - Binder only supports 2.7.15 for a `requirements.txt` file.
  - Sarah personally recommends using the conda environment because it allows you to say which python installation you want too.
  - Binder has tons of examples to capture non-python examples but they are difficult to find:
    - https://mybinder.readthedocs.io/en/latest/config_files.html
    - https://mybinder.readthedocs.io/en/latest/sample_repos.html
  - Note - the `install.R` file is a made up file to install R packages. The standard way of doing this for R users is to use a DESCRIPTION file.
    - https://mybinder.readthedocs.io/en/latest/config_files.html#install-r-install-an-r-rstudio-environment
    - https://mybinder.readthedocs.io/en/latest/config_files.html#description-install-an-r-package
  - Note that the DESCRIPTION file doesn't just install the specific package - it will ALSO install any requirements that you have :smile:
- Step 2: go to mybinder.org, add your GitHub repo link (specify more when needed) and hit "launch"
  - Note: the default binder page opens up into a jupyter **notebook** server. It may be the case that the BETTER solution is to add `?urlpath=lab` to the end of the url so that it opens up a jupyter **lab** environment instead.
  - Jupyter lab allows you to open a *terminal* rather than a notebook.
    - The terminal doesn't have access to a GUI so importing matplotlib.pyplot or .pylab (graphical stuff) won't work
    - Q: what's the difference between a console and a terminal? The console has enough for you to be able to run a bunch of python commands. The terminal doesn't have access to a graphics card! So the console won't work.
  - By default python 2 and python 3 are installed.
- Step 3: copy markdown back into your readme to get a nice "launch binder" button
- BinderHub
  - needs Kubernetes cluster that spins up a bunch of VMs with containers etc. - also does some loadbalancing (Kubernetes [Google developed] being rather new and complex but it can be wrangled to do what you want it to do)
  - jupyterLab to create the environments
  - repo2docker that grabs repo from GitHub and launches Docker
  - BinderHub basically is the high level coordinator for these 3 things and can be accessed through some frontend (the pyblic one being mybinder.org)
  - Also make this useful to run on local machines/HPCs (that might not be setup for this much networking) to enable data throughput independent of cloud availability
  - you don't need all the fancy stuff Kubernetes can do to run a BinderHub -> strip down Kubernetes to the essentials and run that locally

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
- Listed docker images `sudo docker image ls`, and it came up with the hello-world image that came with the download. The instructions didn't include the sudo but without it I get the error `Got permission denied while trying to connect to the Docker daemon socket`. As far as I can tell this issue isn't unique to me or the borrowed computer I'm using. Believe I need `sudo` in front of all my docker commands.
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
- Now looking at [this](https://geohackweek.github.io/Introductory/docker-tutorial_temp/) tutorial **Creative Commons Attribution 3.0 Unported**
- If I then run `docker run -i -t geohackweek2016/arraystutorial` then that image runs. The `-i -t` means that once I hit enter then I get a prefix "root@SHA_type_thing" in the terminal which I can then do standard linux commands with within the container. After experimenting with my own images find generally need `/bin/bash` at the end of this command on order to get the terminal as well as the `-i -t`. Not 100% sure why it wasn't needed for this example, maybe something in the dockerfile. Yeah. If you have `CMD ["/bin/bash"]` in the dockerfile then you don't need to have it when you run the container.
- When I do `ls` I see the stuff in the continer which is comletly different to the directory I ran the image in.
- Move a file from my computer into the container using
  ```
  sudo docker cp file_name Sha_or_name_of_container:path_to_pyt_file/file_name
  ```
- Created a file inside the container, want to get it out, ran
  ```
  sudo docker cp Sha_or_name_of_container:path_to_pyt_file/file_name .
  ```
  The full stop meant the file was put where the terminal I was writing in was located. Note for the copying in/out of the container I ran the commands from outside the container, hence needing the sha to point to it.
- Another [tutorial](http://www.manicstreetpreacher.co.uk/docker-carpentry/aio/) I'm looking at. **Creative Commons Attribution 4.0**
- A docker file can look like this:
  ```
  FROM centos:7
  MAINTAINER spli@dundee.ac.uk

  RUN yum install -y -q epel-release
  RUN yum install -y -q python-pip
  RUN pip install omego
  ```
  where
    - FROM: The name of a base image
    - MAINTAINER: The email of the developer or owner
    - RUN: Runs a shell command
  and some other commonly used docker commands are:
    - COPY: Copies a file (e.g. a script, configuration file, or archive) into the Docker image
    - USER: Change the user that a command is run as (useful for dropping privileges)
    - WORKDIR: Change the current working directory
    - EXPOSE: Lists ports that should be exposed to the outside world
    - VOLUMES: Directories that should be managed separately from the container (e.g. persistent data that should be kept after the container exits)
- If you do some work in a container, close it, then open a new container from the image your work will be gone because it's building from the start
- If you need to do work in a container and save it you can make a "volume" where it'll save the work so even if you close the container when you next make one from that image it'll still have your work. Do this by
  ```
  sudo docker run -i -t --mount source=my_volume_name,target=/notebooks image_name
  ```
  where the target is the directory in the container you're doing work in you want it to save. Then closed and restarted using the same command and my work was still there.
- Volume related commands:
  - List volumes: docker volume ls
  - Delete a volume: docker volume rm VOLUME-NAME
  - Delete all unattached volumes: docker volume prune
- Looking at [this](https://www.tutorialspoint.com/docker/docker_images.htm) tutorial (not open I don't think)
- To remove an image do `sudo docker rmi image_name_or_sha`
- There's docker kill, stop, pause, and unpause. Pause suspends processes running in the container, stop terminates them, kill is for terminating them when you don't case about being graceful about it. There's also restart which restarts after a stop. The syntax for using any of these is `sudo docker what_you_want_to_do container_ID`. Use exit to get out of the interactive bash shell if you started one.
- use `sudo docker rm container_ID` to remove a container. If you include a -v after the rm then it will also remove anny accociated volumes.
- Short example of a docker file
  ```
  #This is a sample Image
  FROM ubuntu
  MAINTAINER demousr@gmail.com

  RUN apt-get update
  RUN apt-get install –y nginx
  ADD my_local_file .
  CMD [“echo”,”Image created”]
  ```
  Breaking this down:
  - Comments by #'s like python.
  - You need some kind of from statement oven if it's `FROM SCRATCH`.
  - MAINTAINER self explanatory and not necessary to include.
  - RUN instructions to run when building the image
  - ADD is used if you have files on your computer you want to be put into the image. The syntax is the path to the file from where you're building the image in, and then the location in the container directory system you want the file to be placed. Note that you can only add files from the level or below where your dockerfile is. Pushed that image to DockerHub and then pulled it to a different computer. When I ran the contianer on that computer the file was in it.
  - CMD is commands to run when your container starts up. So to calify RUN are things you do to *setting up* a container from an image, and CMD is for commands to be automatically run in the container as soon as it's set up. The message only appears if I don't have interactive terminal. Not clear on why.
- It's good practice to use CMD for anything that is going to need to be run before someone starts working in the container. You *can* just follow the instreuction to run the container with a command (e.g `docker run containerID echo Imange created`)  and it'll have the same impact, but then you're relying on whoever is trying to run the container to know they need to follow that up with the command required. Putting it in the Dockerfile means it'll always be run.
- There's ENTRYPOINT, but seems like bad practice to use, so leaving it out.
- Made directories within the container, but when I try using run to cd in and then making another directory within. Didn't work. Asked, this is because each RUN saves and deletes the previous container, then makes a new one from that point, does its run thing, then saves and is deleted and so on. Each layer is like a commit. As a result my RUNing cd into the directory doesn't matter because the next RUN statement restarts the container fresh so the next mkdir goes into the top level. According to David and Will I can use && to have multiple commands on one RUN, but when I try it it doesn't work.
- There's COPY as well as ADD. Serves same function but ADD can also be used to add things from e.g. urls. At least in the one article I read they say it's best to use COPY since it's more explicit. Tested that copy could do the copying local files to an image thing the way add did and it suceeded.
- It's good practice to use .dockerignore files. When you build an image everything in the dockerfile's directory and below is sent to the Docker daemon (which may or may not be on the same machine as where your running the command) to build the image. It uses the dockerfile and the context to build the image. If you're got lots of big files in your context that aren't needed for your image then you're sending the daemon those huge files for nothing. You can make sure they're not sent by including them in a .dockerignore file. You can use syntax like for example `*.png` for example to ignore lots fo different files with similar names/types with few lines.
- Good practise to break RUN statements up to be more readable, for example
  ```
  RUN command_to_do_thing_1 \
     command_to_do_thing_2 \
     command_to_do_thing_3 \
     command_to_do_thing_4
  ```

Practising with conda

- Downloaded conda
- created a conda environment called my_env_1 including the packages numpy and matplotlib using `conda create --name my_env_1 numpy matplotlib`. When you create an environment you have to include at least one package.
- Activated the environment using `conda activate my_env_1`
- Can deactivate environment using `conda deactivate`
- To create this same environment but with a specific version of python do it like this `conda create --name my_env_2 python=2.7 numpy matplotlib`
- Get a list of the conda environments you have using `conda env list`
- To delete a conda environment do `conda remove --name your_environment_name --all`. When you delete an environment you have to rpeciify all the packages it contains. If you don't want to type them out just use the `--all` option as I have here.
- To export a conda environment activate the environment and then run `conda env export > environment.yml`
- If you have an environment file and you want to create an environment from it do `conda env create -f environment.yml`
- numpy is one of the packages included by default, so even if I don't specify it when setting up an environment if I run python in an environment and try `import numpy` it works. However for packages that aren't included, like flask, importing them only works if they're specified when creating the environment.

## Learning how to use Binder

Using Sarah's notes (workshop/10-zero-to-binder.md), adapted from bit.ly/zero-to-binder and bit.ly/zero-to-binder-rise

- Made a simple python script and put in in a new repo on github. Included a readme, not sure if that's necessary or good practise but the instructions told me to.
- Went to [mybinder.org](mybinder.org) and copied in the link to my repos where it told me, and in the branch I specified master. It gave me this link to share with others to show them my binder: https://mybinder.org/v2/gh/r-j-arnold/binder_test_1/master
- I clicked launch. Took me to a page showing the files in my repo and if I click on them I could edit them (not sure if this would impact my github, doubt it, will try)
- Went to the link it gave me (https://mybinder.org/v2/gh/r-j-arnold/binder_test_1/master). Took ages to load. When it did it just showed me my files again.
- Clicked the dropdown `New` in the upper right of that page and them selected terminal. A new tab opened with the terminal and I ran the code using `python my_script_name.py`.
- I like working with terminals but by selecting a different option on that menu you can open a Jupyter notebook instead.
- Changed my script so it imported and used numpy, then went to the link again. When I tried to run the script it failed because there was `No module named numpy` in my environment.
- Created a requirements.txt file and added numpy to it. It then sucessfuly ran.
- Added function in the script that requires a certain version of numpy, and specified that in requirements.txt.
  ```
  numpy==1.15.1
  ```
  (Note the `==` not `=`. Did single = originally and binder failed to load.)
- Reopened the binder, worked.
- In requrements.txt then changed numpy to a version which doesn't have that function. Reloaded the binder.
- Binder successfully loaded, but when I ran the code it executed the first few lines but stopped with an error on the line using numpy to do something that version couldn't.
- I guess that means *binder* only breaks if it can't put together the environment specified. Otherwise if your code breaks because *it's* trying to do something that can't be done then it breaks in the terminal with errors as usual.
- Fixed the wrong version of numpy in requirements.txt.
- Started a Jupyter notebook instead of a terminal.
- In it did `%run my_script_name.py` and ran it. It outputted the correct result.
- Saved the notebook by clicking on file and then save and typing a name for the notebook.
- Closed the notebook tab.
- In the binder there's now a .ipynb file with that name
- Shared the link to my binder to see if others could see the notebook and the results in it.




## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next

We recommend reading the chapter on Testing, and then the chapter on Continuous Integration. Note that the chapter on Version Control is a prerequisite for the chapter on Continuous Integration.

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography

[Figure](https://opendreamkit.org/2017/11/02/use-case-publishing-reproducible-notebooks/) **Permission to use granted by Juliette Taka, Logilab and the OpenDreamKit project.**
