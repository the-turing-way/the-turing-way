# Turing Binder Federation Membership - Credit Request

## Project Title

Turing membership of the International Binder Federation

## Project PI

Kirstie Whitaker

## Existing Subscription

Yes: `turing-mybinder`

## Credit Request

$25,000

## Start/End dates for allocation

- Begin: 1st August 2020 (ASAP)
- End: 30th September 2021

## Platform Justification

A BinderHub (https://binderhub.readthedocs.io) is a computational infrastructure that requires resources which are readily available as a service on the Azure cloud platform (see the "Computational Requirements" section for a detailed description). A different computing platform would likely not have these services in place.

mybinder.org is already hosted by four cloud platforms: Microsoft Azure, Google Cloud, OVH.com (a European cloud provider), and an on-prem service GESIS Notebooks hosted by the Leibniz Institute. This diversity of hosts consolidates Project Binder's status as a cloud-neutral, open source project. We are propagating knowledge related to maintaining a BinderHub on Azure into the wider Binder community and we are contributing to a sustainable and resilient open infrastructure by decentralising resources and knowledge throughout the Federation.

## Research Justification

The Binder Federation (https://blog.jupyter.org/the-international-binder-federation-4f6235c1537e) is an experiment in open infrastructure for data science and beyond. It is a community of scientists and open source developers dedicated to scientific reproducibility, communicating ideas through interactive computing, and providing real-time access to results and analyses. The Federation running mybinder.org has grown to hosting ~140k user sessions per week which range in purpose from research, to teaching and workshops, and beyond. Continuing to be a member of the Federation promotes all three of the Institute's goals: advancing world-class research on real-world problems in academic, government and industry settings; providing interactive training materials for the next generation of data science leaders; and leading the public conversation on modular, interoperable, community owned and run infrastructure. Our shared goal is to democratise access to artificial intelligence for all.

This increase to $25k in Azure credits will allow the Turing to scale up the proportion of mybinder.org we support and facilitate continuous contributions to the improvement, reliability and promotion of the service.

## The Computational Requirements

- A managed Kubernetes cluster composed of Standard D4s v3 virtual machine nodes. These VMs have 4 vCPUs and 16 GB RAM. This is roughly half the size of the VMs in the GKE cluster and similar in size to those in the OVH cluster. Since first launching the Turing Binder cluster, we have increased the proportion of traffic we share with the Federation and hence the cluster has scaled out to accommodate extra users.
- A Virtual Network. This allows us to manage how users can connect with the cluster and monitor how much data is transferred.
- An Azure DNS zone to host the Public IP addresses of the service.
- A Key Vault to securely store information related to the deployment of the infrastructure.

## List of people who require access

Unchanged from previous setup.

## Costing breakdown

The following breakdown was estimated using the [Azure Pricing Calculator](https://azure.microsoft.com/en-gb/pricing/calculator/).

| Service type | Region | Description | Estimated monthly cost per unit ($) | Number of units | Estimated monthly cost ($) | Estimated allocation cost ($) |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| Azure Kubernetes Service (AKS) | West Europe | D4s (4 vCPU, 16 GB RAM) nodes | 167.90 | 10 | 1,679.00 | 21,827.00 |
| Virtual Network | | 500 GB data transfer within West Europe region | 10.00 | 1 | 10.00 | 130.00 |
| Azure DNS | West Europe | 1 hosted DNS zone | 0.90 | 1 | 0.90 | 11.70 |
| Key Vault | West Europe | | 0.00 | 1 | 0.00 | 0.00 |
| | | | | | | |
| | | | | | Subtotal | 21,968.70 |
| | | | | Additional budget for autoscaling and testing | 13.8% | 3,031.30 |
| | | | | | **Total** | 25,000.00 |

---

The RCWG asked for clarification as follows:

> What is the plan for sustainability?
> What happens after the $25k of Azure credits has been used up?
> How will the contributions and improvements to the mybinder.org be sustained (without coming back for more Azure credits)?

Response:

> To clarify, without these credits we cannot continue to run the infrastructure set up as part of the Binder Federation.
> I think the important nuance that may have been lost in the application is that the Turing's donation of these credits/infrastructure is acknowledged on the mybinder.org homepage and the Federation page (https://binderhub.readthedocs.io/en/latest/federation/federation.html#members-of-the-binderhub-federation) which in turn grants us certain privileges both internally and externally.
>
> Externally, the Turing will be seen as a major contributor to open infrastructure, reproducible research and decentralisation of knowledge.
> We also gain ourself a seat at the table in terms of involvement in decision-making regarding the roadmap of mybinder.org.
> Internally, we can learn skills from an established community on large-scale project management and workflows for reproducible research that we can leverage to benefit other Turing projects.
>
> Since Kirstie and I are core contributors to Project Binder, we can still support the sustainability of mybinder.org in terms of day-to-day operations of the Google cluster (which is also currently trying to find credits for the next year!) and leadership roles within the project.
> However, I don't think that's as strong a show of support from the Turing as donating computational resources would be.
>
> I hope this helps answer your questions.
