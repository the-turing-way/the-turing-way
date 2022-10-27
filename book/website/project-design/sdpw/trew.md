(pd-sdpw-trew)=
# Working with Trusted Research Environments

This section provides a general overview of things to consider when working with sensitive data in Trusted Research Environments (TREs). 
For a more comprehensive look at this topic, check out [this report](https://zenodo.org/record/5675093#.YoIpXBPMJhH) from The Alan Turing Institute on developing and publishing code and other research outputs for Trusted Research Environments.

(pd-sdpw-trew-what)=
## What are Trusted Research Environments?

TREs are becoming commonly used for the analysis of data from a range of sources, particularly electronic health records (EHRs). 
Data within TREs are kept secure and are only accessible following appropriate approvals and access being granted.

Typically TREs offer researchers collaborating on a project involving sensitive data a computing environment with restrictions on the ingress and egress of code, data and other research outputs appropriate to the level of sensitivity of the data in question.

There are a variety of TREs being used in the real world, which vary from deployable cloud infrastructure such as The Alan Turing Institute's [Data Safe Haven](https://www.turing.ac.uk/research/research-projects/data-safe-havens-cloud) platform, to bespoke environments hosted at a particular University or other institution with access to sensitive data.

You may find TREs also described as "Data Safe Havens" or "Secure Research Environments" or other synonymous names, since the use of such platforms is relatively new and there is no strict consensus on the terminology. 
To learn more about what TREs are, check out [the graphic and video on this page](https://www.hdruk.ac.uk/access-to-health-data/trusted-research-environments/) produced by Health Data Research UK.

(pd-sdpw-trew-conducting)=
## Conducting research with TREs

In general, researchers working in TREs will find that much of the same guidance for working effectively and reproducibly as outlined in the {ref}`Guide for Reproducible Research<rr-overview>` section will be just as relevant as in any other computing environment.

There are however some important questions to consider when working in TREs that will affect the your development workflow for scientific code writing and data analysis:
    
**1) Does the TRE have internet access?**
    
TREs set up for researchers to work on particularly sensitive data will likely lack internet access, in order to prevent a data breach or the accidental disclosure of sensitive data outside the TRE. 
Where this is the case, it is important to understand how the processes particular to your TRE work for things like software ingress (for important software libraries you may require) and code/data egress (to understand what, if anything, can be exported from the TRE). 
These policies will likely be set by those managing the TRE, for example the IT department at your University.
    
**2) Does the TRE have a version control system, such as GitLab?**
    
Without internet access, websites like GitHub are unavailable for the development of research code within TREs. 
Version Control Systems (VCS) like Git can be useful even where access to GitHub is impossible. 
For example, [GitLab](https://about.gitlab.com/) can be used for code developed within the TRE, if it's installed in the environment. 

If the TRE does not have a collaboration/VCS tool such as GitLab installed, it may be preferable to develop the research code outside the TRE, bringing it into the TRE via secure code ingress at appropriate intervals. 
To learn more about version control, consult the {ref}`Chapter on Version Control<rr-vcs>`.

**3) Do you aim to publish research carried out on sensitive data in a TRE?**
    
Developing research code outside the TRE, for example in a public GitHub repository, can also make publishing the research methods for TRE projects simpler. 
Developing code you wish to export from the TRE inside the environment carries risks. 
For example, sensitive data could be committed to the Git repository by mistake, which is impossible when the code has been developed in a separate location. 
The secure egress process and export policy for the TRE in question will necessarily be rigourous in proportion to the sensitivity of the data being analysed. 
It's therefore important to consider the time constraints associated with exporting any research outputs at the end of a project.
    
Developing research code within the TRE may be more appropriate where progress is overly slowed by developing externally, such as when data access is critical for any development. 
As such, it's important to consider the trade-off between developing research code within the TRE and outside of it.
    
**4) Do you aim to use notebooks (such as Jupyter) for analyses carried out in TREs?** 

Notebooks are a fantastic resource for data analysis, and this is no different in the context of working with sensitive data in a TRE. 
However, notebooks are a particularly risky for export from TRE. Jupyter notebook files in particular (.ipynb extension) are JSON documents that include metadata not viewable in the rendered form, which could increase the risk of sensitive data being included in any exported notebook by mistake.
One recommendation when preparing the output of a data analysis carried out in a notebook within a TRE for publication is to convert it to a static format such as PDF.
    
**5) Do you want those without access to the TRE to be able to run the code used in your research?**
    
Another suggestion could be to include a small synthetic dataset alongside any published code, which any publicly available code or notebooks containing the data analysis can be run with in lieu of access to the "real" (non-synthetic data) sensitive data from the TRE. 
    
For additional guidance on publishing the output of TRE research, see [this report on Developing and Publishing Code for Trusted Research Environments: Best Practices and Ways of Working by Ed Chalstrey](https://zenodo.org/record/5675093#.YoIpXBPMJhH).
