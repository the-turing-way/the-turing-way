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

```{figure} ../../figures/virtual-machine.*
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

```{figure} ../../figures/vm-create-machine.*
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

```{figure} ../../figures/vm-start-machine.*
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

```{figure} ../../figures/vm-export-machine.*
---
name: vm-export-machine
alt: A screenshot showing how to export a Virtual Machine.
---

```

Someone that has access to this file and VirtualBox installed just needs to click `File` in the top left, then `Import` to select that file.
Once it is imported, they can start the VM as described before, by selecting it from the menu clicking the green start arrow at the top.
