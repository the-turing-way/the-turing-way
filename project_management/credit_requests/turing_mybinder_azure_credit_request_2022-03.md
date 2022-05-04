# Turing Binder Federation Membership - Credit Request

## Project Title

Turing membership of the International Binder Federation

## Project PI

Callum Mole; cmole@turing.ac.uk
Malvika Sharan; msharan@turing.ac.uk

## Existing Subscription

Yes: `turing-mybinder`

## Credit Request

£28,004.08



## Start/End dates for allocation

- Begin: 11 March 2022 (ASAP)
- End: 31 March 2023

## Platform Justification

A BinderHub (https://binderhub.readthedocs.io) is a computational infrastructure that requires resources which are readily available as a service on the Azure cloud platform (see the "Computational
Requirements" section for a detailed description). A different computing platform would likely not have these services
in place. 

mybinder.org is already hosted by four cloud platforms: Microsoft Azure, Google Cloud, OVH.com (a European cloud provider), and an on-prem service GESIS Notebooks hosted by the Leibniz Institute.

This diversity of hosts consolidates Project Binder's status as a cloud-neutral, open source project. As a substantial contributor to the service, we are propagating knowledge related to maintaining a BinderHub on Azure into the wider Binder community and contributing to a sustainable and resilient open infrastructure by decentralising resources and knowledge throughout the Federation.

## Research Justification

The Binder Federation (https://blog.jupyter.org/the-internationalbinder-federation-4f6235c1537e) is an experiment in open infrastructure for data science and beyond. It is a community of scientists and open source developers dedicated to scientific reproducibility, communicating ideas through interactive computing, and providing real-time access to results and analyses. mybinder.org serves a global community of researchers and users, and in 2021 served sessions to over 60,000 unique github repositories, serving individuals from every single country in the world.

The Federation running mybinder.org has grown to hosting ~200k user sessions per week which range in purpose from research, to teaching and workshops, and beyond. Turing currently hosts about 25% of the computational capacity of mybinder.org (see https://mybinder.readthedocs.io/en/latest/about/status.html). The ongoing contribution at this level increases the robustness of mybinder.org my reducing over-reliance on individual clusters that can fail due to either funding (see https://github.com/jupyterhub/team-compass/issues/463) or technical issues. Turing's infrastructure currently costs around £2k monthly ($2658). 

In addition to a production cluster, in 2021 Turing deployed a staging cluster where Binder can test deployments before moving into production. The presence of the staging cluster is vital to ensure the robustness and reliability of the federation. It is expected that use of the staging cluster will increase in 2022. 

Both contributions to the Binder project places Turing as a leader in open infrastructure and reproducible research, on a global scale. Continuing to be a member of the Federation promotes all three of the Institute's goals: advancing world-class research on real-world problems in academic, government and industry settings; providing interactive training materials for the next generation of data science leaders; and leading the public conversation on modular, interoperable, community owned and run infrastructure. Our goal shared with Project Binder is to democratise access to artificial intelligence and data science for all.


In addition to supporting the international binder federation there are two Turing-specific reasons to support this request:

1) The Turing cluster also hosts the Turing's internal binder deployment, `Hub23`. In March 2022 Callum Mole, Luke Hare, and Lydia France began an Open Life Science project to improve the deployment and to promote the use of binder and reproducible practices across the Turing. Increased use of `Hub23` across the institute will promote open science and reproducibility in our project. 
 
The Turing project Scivision (https://github.com/alan-turing-institute/scivision) is an example use-case for `Hub23`. Scivision aims to be a well-documented and generalisable Python framework for applying computer vision (CV) methods to a wide range of scientific imagery. Moreover, the project hopes to foster an open source community around the tool. In order to effectively promote scivision, the REG team and three postdocs involved in the project are working on a gallery of example notebooks which clearly demostrate scivision's functionality, via the use-cases of the postdoc's own research fields. These examples should be hosted on binder so they can be linked to from the main scivision GitHub page and easily run. The models being used for these examples require compute resources to run that exceed what is availaible on the default Binder servers (but is available on `Hub23`).
    
2) The Turing cluster supports zero-to-binder workshops that teach researchers how to use binder for their own reproducible research.

## The Computational Requirements

The resource required to continue current efforts are as follows:

**Production Cluster**
-  A managed Kubernetes cluster composed of Standard D4s v3 virtual machine nodes. These VMs have 4 vCPUs and 16 GB RAM. Currently there are two node pools: core (2 nodes) and user (6 nodes). 
- A Virtual Network. This allows us to manage how users can connect with the cluster and monitor how much data is transferred.
- Standard SSD Managed Disk 64 GB
- An Azure DNS zone to host the Public IP addresses of the service.
- A Key Vault to securely store information related to the deployment of the infrastructure.

**Staging Cluster**
- A Managed Kubernetes cluster composed of Standard_D2s_v3. 3 Nodes.

**Hub23**
- An Azure DNS zone to host the Public IP addresses of the service.
- A Key Vault to securely store information related to the deployment of the infrastructure.


## List of people who require access

the existing setup, plus:
- Callum Mole: cmole@turing.ac.uk
- Luke Hare: lhare@turing.ac.uk
- Lydia France: lfrance@turing.ac.uk

## Costing breakdown

The Turing Cluster is running low on credits so here I budget for 13 months to cover the rest of March 2022, up until April 2023. 

In Dec 2021 the capacity of the Turing cluster was increased to reduce the Binder federation's over-reliance of the federation on the GKE cluster. January 2022 is therefore a representative month of the budget required to continue the current resource. The cost breakdown of Jan 2022 was:

Virtual Machines: £1,272.22   
Other (security, storage, virtual network etc.): £688.94     
Total: £1,961.16   

We include in the final estimate a 10% buffer for robustness (e.g. technical issues with other clusters):  
Resource Needs: 1,961.16 * 13 = £25,495.08   
Credits Requested: £25,495.08 * 1.1 = £28,004.08
 

The above estimate is under the pay-as-you-go model. If you reserve the instances you get a discount (1 year = 36%; 3 year = 56%) on the Virtual Machines. 

1 year discounted needs: £1503.16 * 13 = £19,541.09   
1 year credit request: £19,541.09 * 1.1 = £21,495.20   

3 year discounted needs: £1248.72 * 13 = £16,233.32   
3 year credit request: £16,233.32 * 1.1 = £17,856.65  

Note that we request credits every year to add to the turingmybinder subscription. For long-term sustainability of the Turing's role in the Binderhub federation I recommend we pursue to reserve instances for 3 years. If that option is available I would be tempted to guard against the rising usage of mybinder.org (which has steadily risen year on year) and revise the estimate to increase the node count on the turing kubernetes service.
