# The Turing joining the BinderHub Federation - Credit Request

## Project Title

Turing membership of global MyBinder Federation

## Project PI

Kirstie Whitaker

## Existing Subscription

No - please create.
Suggested name: turing-mybinder

## Credit Request

$10,000

## Start/End dates for allocation

Begin: 1st October 2019
End: 30th September 2020

## Platform Justification

A BinderHub (https://binderhub.readthedocs.io) is a computational infrastructure that requires resources which are readily available as a service on the Azure cloud platform (see the "Computational Requirements" section for a detailed description). A different computing platform would likely not have these services in place.

mybinder.org is already hosted by two cloud platforms, Google Cloud (Google Kubernetes Engine, GKE) and OVH.com (a European cloud provider). By adding an Azure host via Microsoft, we will consolidate Project Binder's status as a cloud-neutral, open source project. We can also propagate knowledge relating to maintaining a BinderHub on Azure into the wider Binder community.

## Research Justification

The BinderHub Federation (https://blog.jupyter.org/the-international-binder-federation-4f6235c1537e) is an experiment in open infrastructure for data science and beyond. It is a community of scientists and open source developers dedicated to scientific reproducibility, communicating ideas through interactive computing, and providing real-time access to results and analyses. The BinderHub Federation provides interactive data analytics environments to roughly 10,000 unique repositories via 300,000 launches a month, and it relies on its team of partner BinderHubs to collaborate in providing this service. These Azure credits will allow the Turing to join as the third infrastructure host within the federation, and will significantly contribute to the improvement, reliability and promotion of the service.

Binder is a community within Project Jupyter which received the [ACM Software System Award](https://en.wikipedia.org/wiki/ACM_Software_System_Award) in 2017 for language-agnostic tools which have become "a de facto standard for data analysis in research, education, journalism, and industry" (https://awards.acm.org/award_winners/perez_9039634). 
Binder is a globally established but still growing project. [The Alan Turing Institute](https://www.turing.ac.uk/) will be joining the team when the technology is tried and tested in production _and_ ready to be scaled up to support growing demand for transparent, reproducible, reusable research. 
Joining the BinderHub Federation promotes all three of the Institute's goals: advancing world-class research on real-world problems in academic, government and industry settings, providing interactive training materials for the next generation of data science leaders, and leading the public conversation on modular, interoperable, community-owned and run infrastructure. Our shared goal is to democratise access to artificial intelligence for all.

## The Computational Requirements

* A managed Kubernetes cluster of 3 Standard D4s v3 virtual machines. These VMs have 4 vCPUs and 16 GB RAM. This is roughly half the size of the VMs in the GKE cluster and similar in size to those in the OVH cluster. Based on GKE statistics (using "maximum" pods at https://grafana.mybinder.org/d/nDQPwi7mk/node-activity?panelId=26&fullscreen&orgId=1&from=1565856051535&to=1565873478287&var-cluster=prometheus), we'd expect this cluster to support ~30 users per node at full capacity, subject to RAM limitations.
* An Azure Container Registry with a Premium SKU. The BinderHub builds Docker images and requires access to a container registry for storage. The Premium SKU includes 500 GB of storage in the cost estimate.
* A B1S "burstable" virtual machine to run automated maintenance from. In particular, the container registry is expected to rapidly grow in size as more users are directed to the Azure cluster. The GKE registry usually reaches 50TB and the OVH registry reaches 2TB.

Sarah Gibson, Turing REG team member, has developed an automated script (https://github.com/HelmUpgradeBot/DockerCleanUp) that checks the size of the registry and deletes old (last built more than a customisable number of days ago) or large images since Azure charge $0.003 per GB per day over the included 500 GB. By automatically running this script on an economic VM, we can reduce the likelihood of spending too many credits on the run-away growth of the container registry. We aim to match the 2TB maximum size of the OVH registry.

## List of people who require access

* Sarah Gibson: sgibson@turing.ac.uk, REG data scientist and mybinder.org operator.
* Tim Head: betatim@gmail.com, Core member of mybinder.org maintenance and operating team.

Our justification for having an external collaborator on this project is to ensure that Sarah is not the sole failure point for maintaining the cluster. Tim has extensive experience developing, maintaining and debugging BinderHub clusters and is an expert in this domain. His collaboration will also make it easier to disseminate knowledge about deploying and maintaining BinderHubs on Microsoft's Azure infrastructure into the wider BinderHub community.

Collaborators who do not need access, but who will support Sarah and Tim in Turing's participation in the BinderHub community are Kirstie Whitaker (Turing Research Fellow) and Chris Holdgraf (Berkeley Institute for Data Science fellow, and core Project Jupyter team member).

## Costing breakdown

Resource | Number | Cost ($ per day) | Cost ($ per month) | Cost ($ per year) | Total Cost ($ per year) (Number * Cost per year)
| :--- | ---: | ---: | ---: | ---: | ---: |
Container Registry (Premium SKU) | 1 | 1.667 | | 608.872 | 608.872
Extra Storage (up to 2TB, first 500 GB incl.) | 1 | 4.500 | | 1643.625 | 1643.625
Standard D4s v3 VM | 3 | | 175.50 | 2106.00 | 6318.00
B1S VM | 1 | | 8.76 | 105.12 | 105.12
| | | | | |
| | | | | **Total Cost ($)** | 8675.62

The $10,000 we have asked for includes an approximate 10% buffer to support testing and development requirements. While it is not needed for standard running of the Turing BinderHub, we will use it to experiment with an auto-scaling Kubernetes cluster that will make the BinderHub more cost effective in the long run.

The subscription should **not** be permitted to exceed $10,000 per year.
