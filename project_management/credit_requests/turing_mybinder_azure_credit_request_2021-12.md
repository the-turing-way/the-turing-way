# Turing Binder Federation Membership - Credit Request

## Project Title

Turing membership of the International Binder Federation

## Project PI

Kirstie Whitaker

## Existing Subscription

Yes: `turing-mybinder`

## Credit Request

$6252.74

£4,734.51

## Start/End dates for allocation

- Begin: 22 December 2021 (ASAP)
- End: 31 March 2022

## Platform Justification

A BinderHub (https://binderhub.readthedocs.io) is a computational infrastructure that requires resources which are readily available as a service on the Azure cloud platform (see the "Computational
Requirements" section for a detailed description). A different computing platform would likely not have these services
in place. 

mybinder.org is already hosted by four cloud platforms: Microsoft Azure, Google Cloud, OVH.com (a European cloud provider), and an on-prem service GESIS Notebooks hosted by the Leibniz Institute.

This diversity of hosts consolidates Project Binder's status as a cloud-neutral, open source project. As a substantial contributor to the service, we are propagating knowledge related to maintaining a BinderHub on Azure into the wider Binder community and contributing to a sustainable and resilient open infrastructure by decentralising resources and knowledge throughout the Federation.

## Research Justification

The Binder Federation (https://blog.jupyter.org/the-internationalbinder-federation-4f6235c1537e) is an experiment in open infrastructure for data science and beyond. It is a community of scientists and open source developers dedicated to scientific reproducibility, communicating ideas through interactive computing, and providing real-time access to results and analyses. mybinder.org serves a global community of researchers and users, and in 2021 has served sessions to individuals from every single country in the world.

The Federation running mybinder.org has grown to hosting ~200k user sessions per week which range in purpose from research, to teaching and workshops, and beyond.

Continuing to be a member of the Federation promotes all three of the Institute's goals: advancing world-class research on real-world problems in academic, government and industry settings; providing interactive training materials for the next generation of data science leaders; and leading the public conversation on modular, interoperable, community owned and run infrastructure. Our goal shared with Project Binder is to democratise access to artificial intelligence and data science for all.

**mybinder.org faces short-term difficulty. Google cloud was the largest provider, hosting 70% of the user sessions per week. However, the funding runs out on 22/12/2022. Turing well placed to uphold its values and step in to cover the short-term capacity shortage**.

In addition to supporting the international binder federation there are two Turing-specific reasons to support this request:
- `turing.mybinder.org` also hosts the Turing's internal binder deployment, `Hub23`. We have an Open Life Science project accepted to develop permissioned binder sessions so that Turing researchers can collaborate on private repositories, and to promote the use of binder and reproducible practices across the Turing.
- `turing.mybinder.org` supports zero-to-binder workshops, that teach researchers how to use binder for their own reproducible research.

## The Computational Requirements

- A managed Kubernetes cluster composed of Standard D4s v3 virtual machine nodes. These VMs have 4 vCPUs and 16 GB RAM. This is roughly half the size of the VMs in the GKE cluster and similar in size to those in the OVH cluster. Since first launching the Turing Binder cluster, we have increased the proportion of traffic we share with the Federation and hence the cluster has scaled out to accommodate extra users.
- A Virtual Network. This allows us to manage how users can connect with the cluster and monitor how much data is transferred.
- An Azure DNS zone to host the Public IP addresses of the service.
- A Key Vault to securely store information related to the deployment of the infrastructure.

## List of people who require access

the existing setup, plus:
- Callum Mole: cmole@turing.ac.uk
- Luke Hare: lhare@turing.ac.uk

## Costing breakdown

The following breakdown was estimated using the Azure Pricing Calculator, budgeting for 99 days.

Items given as follows:
| Service Type | Region | Description | Monthly Cost ($) | Number of Units | Estimated Monthly Cost | Estimated Allocation Cost |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| Azure Kubernetes Service (AKS) | West Europe | D4s (4 vCPU, 16 GB RAM) nodes | 167.90 | 10 | 1,679.00 | 5,464.00 |
| Virtual Network | | 500 GB data transfer within West Europe region | 10.00 | 1 | 10.00 | 30.00 |
| Azure DNS | West Europe | 1 hosted DNS zone | 0.50 | 1 | 0.50 | 1.50 |
| Key Vault | West Europe | | 0.00 | 1 | 0.00 | 0.00 |
| | | | | | Subtotal| 5495.5
| | | | |  |Additional budget for autoscaling and testing @ 13.8% | 758.24
| | | | | | Total | $6252.74
| | | | | | Converted to pounds (1 USD = 0.757159 GBP) | £4,734.51
