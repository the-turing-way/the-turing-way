(rr-renv-containers)=
# Containers

(rr-renv-containers-why)=
## Why Containers?

Even for moderately complex projects, the size of the software dependency stack can be huge.
Take a simple pipeline to build a pdf report for an analysis scripted in R using `Rmarkdown`, for example.
To make this reproducible, not only do (i) the respective R packages need to be installed and (ii) the R version needs to be the same, but also (iii) the versions of `pandoc` and `LaTeX` need to be the same as during runtime.

Instead of trying to resolve these dependencies via a package manager (such as conda) -  which also depends on all required software being available in a single package manager - it might be easier to create a snapshot of the entire computing environment including all dependencies.
These computing environments are then self-contained, hence the name 'containers'.

[This RedHat blog
post](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction)
provides an introduction to containers and container terminology.

(rr-renv-containers-what)=
## What are Containers?

Containers allow a researcher to package up a project with all of the parts it needs - such as libraries, dependencies, and system settings - and ship it all out as one package.
Anyone can then open up a container and work within it, viewing and interacting with the project as if the machine they are accessing it from is identical to the machine specified in the container - regardless of what their computational environment _actually_ is.
They are designed to make it easier to
transfer projects between very different environments.

In a way, containers behave like a virtual machine. To the outside world, they look like their own complete system.
However, unlike a virtual machine, rather than creating a whole virtual operating system plus all the software and tools typically packaged with one, containers only contain the individual components they need in order to operate the project they contain.
This gives a significant performance boost and reduces the size of the application.

Containers are a particularly useful way for reproducing research which relies on software to be configured in a certain way, or which makes use of libraries that vary between (or do not exist on) different systems.
In summary, containers are a more robust way of sharing reproducible research than package management systems or Binder because they reproduce the entire system used for the research, not just the packages explicitly used by it.
Their major downside is that due to their greater depth, they are conceptually more difficult to grasp and produce than many other methods of replicating computational environments.

Ben Corrie give a reasonably accessible overview of core concepts in ['What is a container?'](https://www.youtube.com/watch?v=EnJ7qX9fkcU).

(rr-renv-containers-images)=
## What are Images?

Images are the files used to generate containers.
Humans do not make images; they write recipes to generate images.
Containers are then identical copies instantiated from images.

Think of it like this:

- A recipe file a human writes contains all the steps to generate a working version of the project and its computational environment, but no actual materials.
Think of this as a blueprint.
- Building an image takes that recipe and using it, assembles all the packages, software libraries, and configurations needed to make the full-fledged project and environment, and bundles them up in a condensed lump.
Think of images like a piece of flat-pack furniture made using the blueprint.
- Containers take that image and assemble a fully working version of the project and the environment needed to run it.
Think of this as assembling the flat-pack furniture.

So if a researcher wants to allow others to reproduce their work, they would need to write a recipe file, and use it to build an image of their project.
They can then share this image file with anyone who wants to replicate their work.
That person can then use the image to generate a container containing a working version of the project.

(rr-renv-containers-docker)=
## Docker

(rr-renv-containers-whatdocker)=
### What is Docker?

There are many tools available for creating and working with containers.
We will focus on [Docker](https://www.docker.com/), which is widely used, but be aware that others such as [Apptainer](http://apptainer.org/), [LXC](https://linuxcontainers.org/), [Podman](https://podman.io/), [Singularity](https://sylabs.io/singularity/) also exist.
Apptainer and Singularity are designed with a focus on high-performance computing and tend to be well supported and preferred on such systems.
Podman may be seen as a completely free and open-source alternative to Docker.
It has a Docker compatible command-line interface and can run Docker container images.
Apptainer, Singularity and Podman do not need `sudo` permissions to be run, while up until April 2020 Docker did (please see the {ref}`rr-renv-containers-rootless` section).

In Docker, the recipe files used to generate images are known as Dockerfiles, and should be named `Dockerfile`.

[Docker Hub](https://hub.docker.com/) hosts a great many pre-made images, such as
[images](https://hub.docker.com/_/ubuntu) of Ubuntu machines, which can be downloaded and build upon.
This makes the process of writing Dockerfiles relatively easy since users very rarely need to start from scratch, they can just customise existing images.
However, this leaves a user vulnerable to similar security issues as described in the {ref}`rr-renv-yaml-security` of the {ref}`rr-renv-yaml` sub-chapter:

- It is possible to include malicious code in Docker images
- It is possible for people producing images to unknowingly include software in them with security vulnerabilities

[This](https://opensource.com/business/14/7/docker-security-selinux) article goes deeper into the potential security vulnerabilities of containers and here is a [detailed breakdown](https://opensource.com/business/14/9/security-for-docker) of security features currently within Docker, and how they function.
The best advice for using images built by others is, as usual, only download and run something on your machine if it comes from a trusted source.
Docker Hub has "official image" badges for commonly used, verified images as shown here:

```{figure} ../../figures/docker-official-image.*
---
name: docker-official-image
alt: A screenshot of official image badges
---
```

(rr-renv-containers-installdocker)=
### Installing Docker

Installers for Docker on a variety of different systems are available [here](https://docs.docker.com/install/).
Detailed installation instructions are also available for a variety of operating systems such as [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/), [Debian](https://docs.docker.com/install/linux/docker-ce/debian/), [Macs](https://docs.docker.com/docker-for-mac/install/), and [Windows](https://docs.docker.com/docker-for-windows/install/).

(rr-renv-containers-commands)=
### Key Commands

Here are a few key commands for creating and working with containers:

- To build an image from a Dockerfile, go to the directory where the Dockerfile is and run:
  ```
  sudo docker build --tag image_name .
  ```
- To list the images on your system, use:
  ```
  sudo docker image ls
  ```
- To remove an image, run:
  ```
  sudo docker rmi image_name
  ```
- To open a container from an image, run:
  ```
  sudo docker run -i -t image_name
  ```
  The `-i -t` flags automatically open up an interactive terminal within the container so you can view and interact with the project files.
- To exit an interactive terminal, use:
  ```
  exit
  ```
- To get a list of active containers with IDs, run:
  ```
  sudo docker container ls
  ```
- There are also three main commands used for changing the status of containers:
  - Pausing suspends the process running the container.
    ```
    sudo docker pause container_ID
    ```
    Containers can be unpaused by replacing `pause` with `unpause`.
  - Stopping a container terminates the process running it. A container must be stopped before it can be deleted.
    ```
    sudo docker stop container_ID
    ```
    A stopped container can be restarted by replacing `stop` with `restart`.
  - If `stop` does not work containers can be killed using
    ```
    sudo docker kill container_ID
    ```
- To remove a container, run:
  ```
  sudo docker rm container_ID
  ```
(rr-renv-containers-dockerfiles)=
### Writing Dockerfiles

Let us go through the anatomy of a very simple Dockerfile:

```
# Step 1: Set up the computational environment

# Set the base image
FROM ubuntu:18.04

# Install packages needed to run the project
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3.7 python3-pip && \
    rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install numpy

#-----------------------

# Step 2: Include the project files in the image

# Copy files from the `project_files` directory on the machine building the image
# into the `project` folder in the container. This folder and any missing
# directories in its path are created automatically.
COPY project_files/ project/
```

This looks complicated, but most of the lines in this example are comments (which are preceded by `#`'s).
There are only six lines of actual code.
The first of these is a `FROM` statement specifying a base image.
All Dockerfiles require a FROM, even if it is just `FROM SCRATCH`.
All the following commands in a Dockerfile build upon the base image to make a functioning version of the researcher's project.
Specifying a version for the image (`18.04` in this case) is optional.
However, it is best practice as it ensures that our Dockerfile remains valid after new releases of Ubuntu, which may not include packages (or specific versions thereof) that we require later (for example `python3.7`).

It is worth spending time to choose an appropriate base image, as doing so can reduce the amount of work involved in writing a Dockerfile dramatically.
For example, a collection of images with the R programming language included in them can be found [here](https://github.com/rocker-org/rocker-versioned).
If a project makes use of R, it is convenient to use one of these as a base image rather than spend time writing commands in your Dockerfile to install R.

The biggest block of lines comes next.
It's a series of `RUN` statements, which run shell commands when building the image.
In this block, they are used to install the software necessary to run the project. The first `RUN` block is a
chain of commands of this form:

```
RUN command_to_do_thing_1 \
   && command_to_do_thing_2 \
   && command_to_do_thing_3 \
   && command_to_do_thing_4
```

It is good practice to group related commands into a single `RUN` block to reduce the final size of your image by
[avoiding the creation of unnecessary layers](https://docs.docker.com/develop/develop-images/#minimize-the-number-of-layers).
We also follow best-practice by using `--no-install-recommends` to [avoid installing unnecessary packages](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#dont-install-unnecessary-packages)
and [cleaning up the `apt-cache`](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run), both of which further reduce the size of Debian or Ubuntu images.

After we have installed Python, we use another RUN statement to install a library required by our code.

Finally the `COPY` command is used to copy the project files from the machine building the image into the image itself.
The syntax of this command is `COPY file_to_copy location_in_container_to_copy_to`.
In this example, all the files in the `project_files` directory are included in the `project` file in the container.
Note that you can only copy files from the directory where the Dockerfile is located, or subdirectories within it (in the example, that is the
`project_files` subdirectory).

The `ADD` command has the same capabilities as `COPY`, but it can also be used to add files not on the machine building the image.
For example it can be used to include files hosted online by following `ADD` with a URL to the file.
It is good practice to use `COPY`, except where `ADD` is specifically required, as the term `COPY` is more explicit about what is being done.

Here is what happens if a container is opened from an image called `book_example`, built from the example above:

```{figure} ../../figures/container-example.*
---
name: container-example
alt: A screenshot of what happens when a container is opened from an image
---
```

As you can see, the directory `project` has been created, and inside the project files, `analysis.py` and `data.csv` have been copied into it.
Because the Dockerfile already includes the software required for the project, in the image, the `analysis.py` script runs without installing more software.

(rr-renv-containers-dockerfiles-workdir)=
### `WORKDIR`

This command can be used in Dockerfiles to change the current working directory.
Commands that follow this in the Dockerfile will be applied within the new working directory unless/until another `WORKDIR` changes the working directory.
When a container is opened with an interactive terminal, the terminal will open in the final working directory.
Here is a simple example of a Dockerfile that uses `WORKDIR`, and the container it generates.

```
# Basic setup
FROM ubuntu
RUN apt-get update

# Make a directory called A
RUN mkdir A

# Make the working directory A
WORKDIR A

# Make two directories, one called B_1 and one called B_2
RUN mkdir B_1
RUN mkdir B_2
```

```{figure} ../../figures/workdir-example.*
---
name: workdir-example
alt: Screenshot of container generated using WORKDIR command
---
```

Directories `B_1` and `B_2` have been created within directory `A`.

`WORKDIR` should be used when changing directories is necessary while building an image.
It may be tempting to use `RUN cd directory_name` instead, as this syntax will be more familiar to those that commonly work via the command line,
but this can lead to errors.
After each `RUN` statement in a Dockerfile, the image is saved, and any following commands are applied to the image anew.
As an example, here is what happens in the above example if the `WORKDIR A` line is swapped
for `RUN cd A`.

```{figure} ../../figures/cd-example.*
---
name: cd-example
alt: A screenshot of what happens when the WORKDIR command is swapped with RUN cd
---
```

All the directories have are in the top level in this case, rather than `B_1` and `B_2` being inside `A`.
This is because the image was restarted after the `RUN cd A` command and opened at the top (root) level by default, so that is where the
`mkdir B_1` and `mkdir B_2` commands took effect.

(rr-renv-containers-dockerfiles-commands)=
#### Other Commands

Other commands that are sometimes used in Dockerfiles include:

- `CMD`: This is used to run commands as soon as the container is opened.
This is different to RUN commands which are commands run as part of _setting up_ a container.
For example, to have a welcome message when a container is opened from the image, `CMD` could be used as follows:
  ```
  CMD ["echo","Welcome! You just opened this container!"]
  ```
  It is good practice to use CMD for any commands that need to be run before someone starts working in the container
  instead of forcing users to run them themselves (and trusting that they will even know that they need to).
- `VOLUMES`: These will be discussed {ref}`later <rr-renv-containers-volumes>`.
- `MAINTAINER`: This contains information regarding the person that wrote the Dockerfile.
It is typically included at the top of a Dockerfile.
- `EXPOSE`: This includes ports that should be exposed.
It is more relevant to people using Docker to share web apps.
- `USER`: Change the user that a command is run as (useful for dropping privileges).

(rr-renv-containers-dockerignore)=
### Building Images and `.dockerignore` Files

As mentioned in the {ref}`key commands <rr-renv-containers-commands>` section, to build an image open a terminal in the same directory as
the Dockerfile to be used and run:

```
sudo docker build --tag name_to_give_image .
```

When an image is built everything in the Dockerfile's directory and below (this is called the "context") is sent to the Docker daemon to build the image.
The daemon uses the Dockerfile and its context to build the image.
If the context contains many large files, which are not needed for building the image, (old datafiles, for example) then it is a waste of time sending them to the daemon.
Doing so can make the process of building an image slow.
Files can be excluded from the context by listing them in a text file called `.dockerignore`.
It is good practice to do so.

The files do not need to be listed individually in the `.dockerignore` file.
Here is an example of the contents of a `.dockerignore` file:

```
*.jpg
**/*.png
data_files/*
file_to_exclude.txt
```

This excludes from the context:

- All `.jpg` files in the same directory as the Dockerfile file
- All `.png` files in the same directory as the Dockerfile file _or any subdirectories within it_
- All files within the `data_files` directory
- The file named `file_to_exclude.txt`

(rr-renv-containers-sharing)=
### Sharing Images

Docker images can be shared most easily via [Docker Hub](https://hub.docker.com/), which requires an account.
Say two researchers, Alice and Bob, are collaborating on a project and Alice wishes to share an image of some of her work with Bob.

To do this, Alice must:

- Write a Dockerfile to produce an image of her work.
- Build the image. She (being inventive) calls it image_name
- Go to Docker Hub and sign up for an account. Say Alice (again, being inventive) chooses the username `username_Alice`
- Log into Docker Hub via the terminal on her machine using:
  ```
  sudo docker login
  ```
- Tag the image of her project on her machine via the command line by supplying the name of the image and using the pattern `username/image_name:version`. So Alice runs the command:
  ```
  sudo docker tag image_name username_Alice/image_name:version_1
  ```
- Push the image to her Docker Hub account using:
  ```
  sudo docker tag push username_Alice/image_name:version_1
  ```
- Alice's image is now online and can be downloaded. Over to Bob...

Bob (assuming he already has Docker installed) can open a container from Alice's image simply by running

```
sudo docker run -i -t username_Alice/image_name:version_1
```

Initially, Docker will search for this image on Bob's machine.
When it does not find it, it will _automatically_ search Docker Hub, download Alice's image, and open the container with Alice's work and environment on Bob's machine.

(rr-renv-containers-copying)=
### Copying Files To And From Containers

Containers act much like virtual machines; as a result, copying files into and out of them is not as trivial as copying files to different locations within the same computer is.

A file can be copied from the machine running a container into the container using:

```
sudo docker cp file_name container_ID:path_to_where_to_put_file/file_name
```

Recall that container IDs can be obtained using `sudo docker container ls`.

A file can be copied from within a container to the machine running the container by running the following command on the machine running the container:

```
sudo docker cp container_ID:path_to_file/file_name path_to_where_to_put_file/file_name
```

If the second part (the `path_to_where_to_put_file/file_name`) is substituted for a `.`, then the file will be copied to whatever directory the terminal running the command is in.

(rr-renv-containers-volumes)=
### Volumes

Every time a container is opened from an image, that container is completely new.
Say a container is opened, and work is done within it.
If that container is closed, and the image it came from is again used to start another container, none of that work will be in the new one.
It will simply have the starting state described in the image.

This can be a problem if a researcher wants to work in a container over time. Fortunately, there is a way around this using volumes.
Volumes store the work done within a container even after it is closed, and can be used to load that work into future containers.

To create/use a volume, run:

```
sudo docker run -i -t --mount source=volume_name,target=/target_directory image_name
```

You should give your volume a more descriptive name than `volume_name`.
A `target` directory is required; only work within this directory will be saved in the volume.
Once the researcher is done, they can close the container as normal.
When they come back to the project and want to continue their work, they only need to use the same command as above, and it will load the work contained in `volume_name` into the new container.
It will save any new work there too.

Below is a list of volume related commands:

- To list volumes: `sudo docker volume ls`
- To delete a volume: `sudo docker volume rm volume_name`
- To delete all unattached volumes: `sudo docker volume prune`

If, when deleting a container, a `-v` is included after `rm` in `sudo docker rm container_ID`, any volumes associated with the container will also be deleted.

(rr-renv-containers-rootless)=
### Docker without root access

Up until April 2020, the only way to run Docker was with root access.
"Rootless" mode was made available as part of the [v20.10](https://docs.docker.com/engine/security/rootless/) release.
Rootless mode is currently only available on Linux and requires an initial install of Docker >= v20.10.

The underlying difference between Docker without and with rootless mode is that previously any system running Docker had a daemon running as `uid0` that creates and owns all images, but with rootless mode the user creates and owns any images that they initialize.
To install and run the rootless version of Docker as a non-root user, use the following commands (where `20.10` refers to the installed version of Docker):

```
dockerd-rootless-setuptool.sh install
docker run -d --name dind-rootless --privileged docker:20.10-dind-rootless
```

The following prequisites, which are part of the [`shadow-utils`](https://github.com/shadow-maint/shadow) package are required to run Docker rootless: `newuidmap` and `newgidmap`.

(rr-renv-containers-podman)=
## Podman

[Podman](https://podman.io/) is an open-source container engine that can be seen as a meaningful alternative to Docker.
In fact, Podman provides a Docker-compatible command-line interface.
For most use cases, a user familiar with Docker can simply alias the Docker command to Podman (`alias docker=podman`) and carry on as normal.
Podman includes a [full set of tools](https://docs.podman.io/en/latest/Commands.html) to create, run, manage, and share containers.

Podman is free and open-source software released under the Apache License 2.0.
This is in contrast to Docker which has some open-source components, such as the engine and command-line interface, but also develops closed-source, [subscription-requiring](https://www.docker.com/blog/updating-product-subscriptions/) software, including the Docker Desktop clients for MacOS and Windows.

All [Open Container Initiative](https://opencontainers.org/) container images can be used with Podman including Docker images hosted on Docker Hub.
It is likely existing projects using Docker can be migrated to Podman.

Unlike Docker which uses a daemon running as root, Podman is daemonless.
Unprivileged users can run containers using Podman.
In most cases this will be configured automatically.
This avoids a problem with the standard Docker configuration where users able to run containers have implicit access to the Docker daemon.
The Docker Daemon is run by root by default and provides a trivial way to escalate privileges and get a high level of access to the hosts devices and filesystem.

````{note}
Adding a user to the docker group is essentially giving them a high-level of access to the host with a very simple route to privilege escalation.
For example:

```console
$ docker run --mount=type=bind,source=/,destination=/host -it busybox
```

The user now has access to the filesystem of the host with the permissions of `root`.
````

(rr-renv-containers-installpodman)=
### Installing Podman

The Podman documentation has up-to-date instructions for [installing Podman](https://podman.io/getting-started/installation).

It is important to understand that Podman is a tool for running Linux containers and so it requires a Linux host.
If your computer is running Windows or MacOS, you can use the [Podman remote client](https://github.com/containers/podman/blob/main/docs/tutorials/mac_win_client.md) to interact with Podman on a Linux virtual machine or remote Linux Host.

Alternatively, the MacOS Podman client includes the experimental `podman machine` subcommand for managing a Linux virtual machine that Podman can use.
Detailed instructions can be found [on Podman's GitHub repository](https://github.com/containers/podman/blob/main/docs/tutorials/mac_experimental.md)
On Windows you can also run Podman in the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) (>= 2.0).
[This RedHat blog post](https://www.redhat.com/sysadmin/podman-windows-wsl2) has instructions.

For most recent Linux distributions you should [find Podman in the official repositories](https://podman.io/getting-started/installation#linux-distributions).
Most distributions (including Arch, Debian, Fedora, and Ubuntu) will apply the appropriate configuration to let unprivileged users run Podman automatically.
If there are any problems, the Podman documentation [has instructions for configuration](https://docs.podman.io/en/latest/markdown/podman.1.html?highlight=rootless#rootless-mode).
This is as simple as two commands per user who should be able to run Podman.

(rr-renv-containers-commandspodman)=
### Podman Commands

Podman has a Docker-compatible command line interface so those commands will not be reiterated here.
The Docker commands in the {ref}`key commands <rr-renv-containers-commands>` should all work by substituting `sudo docker` with `podman`.
Details of all commands and their options can be found [in the Podman documentation](https://docs.podman.io/en/latest/Commands.html).

(rr-renv-containers-imagespodman)=
### Building Container Images

Podman can build container images using the `podman build` command.
Podman will build images from either Dockerfiles or Containerfiles.
Containerfiles use the same format as Dockerfiles, which are discussed in {ref}`Writing Dockerfiles <rr-renv-containers-dockerfiles>`

(rr-renv-containers-rootlesspodman)=
### Rootless Containers

Rootless containers are containers run by a normal user (not using `sudo` or with the `root` account).
These containers never have more privileges than the account that runs them.
This is an strong security advantage for rootless containers compared to running containers as root or through the Docker daemon.

```{note}
If you are running a distribution with SELinux (for example Fedora or CentOS) you may need to add the `--privileged` flag to the Podman commands below in order to access the host filesystem inside of containers.
```

This can be demonstrated with a simple example. Create a directory and put file with some text in it:
```console
$ mkdir tmp
$ echo "Hello" > tmp/a.txt
```

Now mount this directory into an interactive [busybox](https://www.busybox.net/) container:
```console
$ podman run --mount=type=bind,source=./tmp,destination=/tmp -it docker.io/library/busybox
```

In the container's shell, confirm that the session belongs to the root user:
```console
/ # id
uid=0(root) gid=0(root) groups=10(wheel)
/ # whoami
root
```

Append some text to the file created on the host, mounted at `/tmp/a.txt` in the container:
```console
/ # echo "World!" >> /tmp/a.txt
```

Create a new file in the `tmp` directory and close the container:
```console
/ # touch /tmp/b.txt
/ # exit
```

Inspect the files in `tmp` on the host. The file `a.txt` was modified by the container process:
```console
$ cat tmp/a.txt
Hello
World!
```

The file `b.txt` was created. However, despite being created by `root` inside the container, on the host it is owned by the user which ran the container.
This can be confirmed with `ls -l tmp/b.txt`.

It is also impossible to read or modify files that the user running the container would not be able to.
For example, the `/etc/shadow` file which contains users' hashed passwords:

```console
$ podman run --mount=type=bind,source=/etc/shadow,destination=/shadow -it docker.io/library/busybox
/ # cat /shadow
cat: can't open '/shadow': Permission denied
```

If the above Podman command were run as root, using `sudo`, then the container would not be rootless and it would be possible to read and modify `etc/shadow`.

(rr-renv-containers-singularity)=
## Singularity

```{note}
As Singularity is a tool for running Linux containers it can not run natively on
Windows or MacOS.

Singularity provides [Vagrant](https://www.vagrantup.com/) boxes which let users
on Windows or MacOS quickly deploy a virtual machine with Singularity installed.
Instuctions can be found [in the Singularity
documentation](https://sylabs.io/guides/latest/admin-guide/installation.html#installation-on-windows-or-mac)
```

Historically, a significant drawback of using Docker for reproducible research is that it was not intended as a user-space application but as a tool for server administrators.
As such, it required root access to operate.
There is, however, no reason why the execution of an analysis should require root access for the user.
This is especially important when computations are conducted on a shared resource like high-performance computing (HPC) systems where users will never have root access.

The [singularity](https://www.sylabs.io/) container software was introduced to address this issue.
Singularity was created with HPC systems and reproducible research in mind (see [this](https://www.youtube.com/watch?v=DA87Ba2dpNM) video).
Singularity containers do not require root access to run.
Root access is normally required to build container images.
However it is possible to build images as a normal user (with some restrictions) using the [fakeroot feature](https://sylabs.io/guides/latest/user-guide/fakeroot.html).
This enables users to build container images locally before running them on a high-performance cluster.
As an added benefit, this makes it possible to bring software and project dependencies to an HPC system without requiring the system administrators to install or maintain them.

Furthermore, Singularity can take advantage of the large Docker ecosystem by building Singularity container images from Docker container images.
Docker images can also be extend by building new images based on docker containers as a base layer.

(rr-renv-containers-singularity-images)=
### Singularity Container Images

Just as Docker images are built using `Dockerfile` files, singularity containers are built from singularity definition files.
The Singularity documentation has a complete [specification of the definition file format](https://sylabs.io/guides/latest/user-guide/definition_files.html)

As a minimal working example, we can build a `lolcow` container based on the official ubuntu docker container image.
This is based on [an example](https://sylabs.io/guides/latest/user-guide/build_a_container.html) in the Singularity documentation.
Put the following text in a file named `lolcow.def`:

```
Bootstrap: docker
From: ubuntu

%post
    apt-get -y update
    apt-get -y install fortune cowsay lolcat

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript
    fortune | cowsay | lolcat
```

This example uses a docker image (`ubuntu`) as a basis.
The required packages are installed packages with `apt-get`.
The `PATH` variable is updated so that the run commands will be found when the container is run.
The `%runscript` defines the command to be executed when the container is run.

A container image can then be built:

```console
$ sudo singularity build lolcow.sif lolcow.def
```

This will pull the ubuntu image from Docker Hub, run the steps of the recipe in the definition file and produce a Singularity image file (`lolcow.sif`).
The container can be run with:

```console
$ singularity run lolcow.sif
```

or, simply:

```console
$ ./lolcow.sif
```

````{note}
The way that Singularity packages container images as a single file in your working directory is convenient for migrating your work to HPC.
You may simply copy your container image to a cluster using `scp` or `rsync`:

```console
$ rsync -avz lolcow.sif <user>@<hpc_system>:~/
```
````

You should see a nice ASCII cow and a few words of wisdom:

```
___________________________________
/ You will be called upon to help a \
\ friend in trouble.                /
-----------------------------------
       \   ^__^
        \  (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
```

(rr-renv-containers-singularity-gpu)=
### GPU Support

A key distinction of Singularity is that it is able to natively utilise host GPUs in containers.
Singularity has support for CUDA supporting GPUs from Nvidia and ROCm supporting GPUs from AMD.
Running containers with GPU support does not require root privileges.
Complete details on using GPUs can be found [in the Singularity documentation](https://sylabs.io/guides/latest/user-guide/gpu.html)

To use Nvidia GPUs in a container pass the `--nv` flag to the `run`, `exec` or `shell` command.
For example:

```console
$ singularity pull docker://tensorflow/tensorflow:latest-gpu
$ singularity exec --nv tensorflow_latest_gpu.sif nvidia-smi
```

Using AMD GPUs is similar but the `--rocm` flag is used.
For example:

```console
$ singularity pull docker://rocm/tensorflow:latest
$ singularity run --rocm tensorflow_latest.sif
```

When using the `--nv` and `--rocm` graphics drivers and libraries from the host are passed to the container.
You must therefore ensure that the application inside the container is compatible with the driver stack on the host.
For example, if the host has support for CUDA 10.2 a container featuring PyTorch build for CUDA 11.3 is likely to problems running.

(rr-renv-containers-singularity-hpc)=
### Singularity on HPC

Being HPC compatible, singularity containers are also supported by a wide range of workflow management tools.
For example, both [snakemake](https://snakemake.readthedocs.io/en/stable/) and [nextflow](https://www.nextflow.io/docs/latest/singularity.html) support job-specific singularity containers.
This makes singularity containers uniquely suited for parallelizing workflows on HPC systems using the widely used [slurm](https://slurm.schedmd.com/documentation.html) workload manager.
Using singularity, containers and snakemake/nextflow is a way of scaling reproducibility to a massive scale.
Furthermore, as an added benefit, bringing workflows from a desktop machine to an HPC system no longer requires writing custom job submission scripts.

(rr-renv-containers-singularity-storage)=
### Long-term Storage of Container Images

It is important to note that a mere container recipe file is not reproducible in itself since the build process depends on various (online) sources.
Thus, the same recipe file might lead to different images if the underlying sources were updated.

To achieve true reproducibility, it isimportant to store the actual container _images_.
For singularity images, this is particularly easy since an image is simply a large file.
These can vary in size, from a few tens of megabytes (micro-containers) to several gigabytes, and are therefore not suited for being stored in a git repository themselves
A free, citable, and long-term solution to storing container images is [zenodo.org](https://zenodo.org/) which allows up to 50 Gb per repository.
Since zenodo mints DOIs for all content uploaded, the images are immediately citable.
In contrast to [Docker Hub](https://hub.docker.com/) (which also only accepts docker images),
zenodo is also clearly geared towards long-term storage and discoverability via a sophisticated metadata system.
Thus, it is ideally suited for storing scientific containers associated with particular analyses since these tend to not change over time.

(rr-renv-containers-warning)=
### Words of Warning

Even though singularity and docker might look similar, they are conceptually very different.
Singularity handles the distinction between the host and container file system differently.
For instance, by default, singularity includes a few bind points in the container, namely:

- `$HOME`
- `/sys:/sys`
- `/proc:/proc`
- `/tmp:/tmp`
- `/var/tmp:/var/tmp`
- `/etc/resolv.conf:/etc/resolv.conf`
- `/etc/passwd:/etc/passwd`
- `$PWD`

Note, `$PWD` comes in handy since it implies that all files in the working directory are visible within the container.
Binding `$HOME` by default, however, also implies that software using configuration files from `$HOME` might behave unexpectedly since the image specific configuration files are overwritten with the current users settings in `$HOME`.
While this behaviour is handy in HPC scenarios, it is potentially dangerous for reproducible research.
To avoid potential issues, any software installed in a singularity container should be pointed to a global, user-independent configuration file.
