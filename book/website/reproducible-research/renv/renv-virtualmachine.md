(rr-renv-vm)=
# Virtual Machines

(rr-renv-vm-what)=
## What are Virtual Machines?

Virtual Machines (VMs) essentially package a whole computer as an app that can be run.
As an example, the figure below shows a windows laptop (note the windows search button in the lower-left corner) running a virtual ubuntu machine (note the terminal outputting the operating system).
The machine running the VM is called the `host machine`.

Using software like [VirtualBox](https://www.virtualbox.org/) or [Vagrant](https://www.vagrantup.com/), a user can create and run any number of VMs.
As you could probably guess, having several VMs running at once can be a drain on memory.
So just because you can run several VMs does not mean you should.

```{figure} ../../figures/virtual-machine.png
---
name: virtual-machine
alt: A screenshot of a Virtual Machine.
---

```

Users can download, install, backup and destroy VMs at will, which is why they are an attractive tool for sharing reproducible research.
Research often requires specific pieces of software or system settings.
If a researcher wishes to reproduce another's work on their computer, making the necessary changes to their environment to run the project may impact their work.
For example, in the {ref}`rr-renv-useful` section of this chapter, we described how using a different version of Python can lead to unexpected changes in the results of an analysis.
Say a researcher installs an updated version of Python to replicate an analysis because the analysis requires features only present in the updated version.
By doing so, they put their own work at risk.
VMs remove that risk; any tools downloaded or settings changed will only impact the VM, keeping the reproducer's research safe.
If they do inadvertently break something in the VM, they can delete it and make another one.
VMs are effectively a quarantined area.

(rr-renv-vm-research)=
## Using Virtual Machines for Reproducible Research

Virtual machines can be shared by exporting them as single files.
Another researcher can then import that file using their own virtualisation software like [VirtualBox](https://www.virtualbox.org/) and open up a copy of the VM which will contain all the software files and settings put in place by the person that made the VM.
Therefore in practice, they will have a working version of the project without the pain of setting it up themselves.

(rr-renv-vm-research-settingup)=
### Setting up a Virtual Machine

First, choose a tool for generating VMs.
Here the widely-used [VirtualBox](https://www.virtualbox.org/) is chosen.
Download and install it on your system.
To create a new machine, click "New" in the top left.
A window will pop up where you can enter a name for the machine and select what operating system (and version) to use.
In the figure below, a machine called `demo_VM` running Ubuntu is being created:

```{figure} ../../figures/vm-create-machine.png
---
name: vm-create-machine
alt: A screenshot showing a Virtual Machine is created.
---

```

As you click through, you can adjust other features of the machine to be created, such as how much memory it should have access to.
The default options are suitable for most purposes, but this process permits customisation.

(rr-renv-vm-research-starting)=
### Starting a Virtual Machine

To start a virtual machine, select the machine from the list of VMs on the left, and click the green `Start` arrow at the top:

```{figure} ../../figures/vm-start-machine.png
---
name: vm-start-machine
alt: A screenshot showing how to start a Virtual Machine.
---

```

(rr-renv-vm-research-sharing)=
### Sharing Virtual Machines

A researcher can do work on their VM, and then export it.
To export a VM, click `File` in the top left and then `Export`.
This will export the VM as a single file which can be shared.

```{figure} ../../figures/vm-export-machine.png
---
name: vm-export-machine
alt: A screenshot showing how to export a Virtual Machine.
---

```

Someone that has access to this file and VirtualBox installed just needs to click `File` in the top left, then `Import` to select that file.
Once it is imported, they can start the VM as described before, by selecting it from the menu clicking the green start arrow at the top.

(rr-renv-vm-vagrant)=
## Declarative Environments with Vagrant

[Vagrant](https://www.vagrantup.com/) is a tool which *"enables users to create and configure lightweight, reproducible, and portable development environments"*.
In this context, an environment is a virtual machine (its CPUs, RAM, networking and so on) and the machines state (operating system, packages).

### How Vagrant Works

Unlike some other tools you may use to create or manage virtual machines, like [VirtualBox](https://www.virtualbox.org/) and [QEMU](https://www.qemu.org/), Vagrant does not have its own hypervisor.
Instead, Vagrant uses [providers](https://developer.hashicorp.com/vagrant/docs/providers) to interact with other virtualisation tools.
Vagrant has built in providers for [VirtualBox](https://www.virtualbox.org/), [Hyper-V](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/) and [Docker](https://www.docker.com/).
Other providers can be supported by plugins.
In particular, the Vagrant developers maintain an [official plugin](https://developer.hashicorp.com/vagrant/docs/providers/vmware/installation) for [VMWare](https://www.vmware.com/).
For Linux users there is also a [community supported provider](https://vagrant-libvirt.github.io/vagrant-libvirt/) for [libvirt](https://libvirt.org/).

```{note}
A hypervisor is software which allows virtual machines to interact with host machines hardware at a low level.
[This](https://www.redhat.com/en/topics/virtualization/what-is-a-hypervisor) article from Red Hat gives a good overview.
```

Vagrant environments can be packed into [boxes](https://developer.hashicorp.com/vagrant/docs/boxes).
When using Vagrant you will most likely start from an existing box and build your environment on top of it.
You can browse and search for public boxes [here](https://app.vagrantup.com/boxes/search).

After deploying a box, Vagrant can also use [provisioners](https://developer.hashicorp.com/vagrant/docs/provisioning) to apply further configuration.
This is useful to adapt a generic box to a specific purpose, for example by installing packages.
Provisioning can be as simple as a shell script but can also incorporate powerful configuration management tools like [Ansible](https://docs.ansible.com/ansible/latest/index.html), [Puppet](https://puppet.com/) and [Chef](https://www.chef.io/).

### The Vagrantfile

With Vagrant, users can define the configuration of a virtual machine (or group of virtual machines) in a declarative configuration language stored in a Vagrantfile.
This configuration is written in the [Ruby](https://www.ruby-lang.org/en/) programming language.
However, it is not necessary to know Ruby as the syntax is simple and the [documentation](https://developer.hashicorp.com/vagrant/docs/vagrantfile) explains all of the available options.

Defining the virtual machines in plain text has a number of advantages over distributing disk images.

- Can be checked into version control
- Small size makes them easy and fast to share
- Users can reproducibly build the environment themselves
- Can potentially work across multiple hypervisors (like VirtualBox, VMWare, libvirt)

In combination, these attractive qualities address the goals of Vagrant.
A project can maintain its development environment alongside the source code and every contributor can build and use the environment with minimal barriers.

### The Vagrant CLI

You will most likely use vagrant through the command line interface.
The CLI can be used to

- manage machines with commands like `vagrant up`, `vagrant halt` and `vagrant destroy`.
- connect to machines with `vagrant ssh` and `vagrant powershell`
- get, package and publish boxes
- create minimal Vagrantfile with `vagrant init`

Full documentation for all commands can be found [here](https://developer.hashicorp.com/vagrant/docs/cli)

### Syncing Data

Vagrant can help sharing data between the host and the virtual machine by syncing directories.
By default, the directory containing the Vagrantfile is mounted at `/vagrant` on the guest.
Therefore, if you keep a Vagrantfile in the root of a git repository, when you use the Vagrant environment you will find your project at `/vagrant`.
This makes it convenient to develop, build and test your project within the environment.

Additional shared directories can be declared as explained in [the documentation](https://developer.hashicorp.com/vagrant/docs/synced-folders/basic_usage).

Some boxes may not have any shared directories, so it is best to explicitly define any that you want in your Vagrantfile.
In particular, the 'generic' images built by [Roboxes](https://roboxes.org/) do not have any mounts by default.
These boxes are popular as they cover a wide variety of distributions and support a multiple hypervisors.
