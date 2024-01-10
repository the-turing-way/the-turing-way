(rr-rdm-elns)=
# Electronic Lab Notebooks

An Electronic Laboratory Notebook (commonly known as an ELN or a digital lab notebook) is a software system designed to help you document and maintain reproducibility of your research and share information more easily.
ELNs enable researchers to organize and store experimental procedures, protocols, plans, notes, data, and even unfiltered interpretations using their computer or mobile device.
They can be a digital analogue to the paper notebook most researchers keep.
ELNs can offer several advantages over the traditional paper notebook in documenting research during the active phase of a project, including; searchability within and across notebooks, secure storage with multiple redundancies, remote access to notebooks, and the ability to easily share notebooks among team members and collaborators.
ELNs make the practice of {ref}`open notebooks <rr-open-notebooks>` [{term}`def<Open Notebooks>`] practical in a way that it is not for paper lab books.
However, it is important when choosing an ELN solution to avoid giving up the advantages offered by a paper lab notebook.

(rr-rdm-elns-procon)=
## Quick Pros & Cons of ELNs

Electronic Lab Notebooks may provide, among other things, the following **functionalities**:

* A text editor with similar functions as a paper notebook
* A search function
* Secure storage and back up (with distinct failure modes from paper notebooks)
* Tools for working with tabular data (calculations and formatting of tables and graphs)
* Templates for documenting standard procedures
* Built-in Laboratory Inventory Management Systems (LIMS) functionality for managing and documenting samples, reagents, and apparatus, or integration with separate dedicated LIMS.
* Collaboration tools for sharing experimental information
* Some ELNs will allow you to comply with standards and regulations because of their certification processes

ELNs also have their **limitations**: 

* **Costs**: Most ELN solutions can only be used through paid plans, or the free plans have reduced functionalities in the number of users, storage space or file sizes.
Your lab may also not have access to tablets or pens that would make the use of ELNs easier.
Check if your institution is offering a solution that you can use without additional costs.
* **File format**: Always check if files can be exported in your preferred file formats to avoid format lock-in.
Some ELNs also have API's that allow integration with other software and workflows. 
* **Vendor-lock-in**: Once you're using a certain solution you may become dependent on it.
Always have an exit strategy in case the solution is no longer offered or if you're moving institutions and you no longer have access.
* **Sustainability**: Choose a solution that has a larger chance of being around for a long time.
* **Drawing**: Not all solutions have the tools or capabilities to include drawings or integration with drawing software.
* **Security**: Before using an ELN solution you should check any backup plans and data security measures, especially if you're working with sensitive data.
* **Laboratory situation**: Your lab may not have an internet connection or electronic tools could affect samples, reagents or magnets in the lab. 
* **Learning curve**: ELNs have a longer learning curve than paper notebooks and it takes time to learn how to use them.
User-friendliness and flexibility are important to accommodate the widely varying workflows of each lab member.

(rr-rdm-elns-choosing)=
## Choosing an ELN solution

If you are in a position to choose an ELN to use, or are making a choice on behalf of an organisation there are some factors to consider:

(rr-rdm-elns-choosing-importance)=
### Importance of getting it right

Many organisations offer software that purports to solve the problem of ELNS.
So choosing a suitable solution can be a major headache and responsibility.
The choice of ELN is an incredibly important decision, and one that your organisation will likely have live with for years, or even decades.
You are putting the record of your research into the hands of the tool that you choose, and entering into a long-term relationship with the provider of your ELN solution.
You are also making a choice about a tool that many of the people in your organisation will interface with closely every day.
Having to use a tool that is not well fit to its function on a daily basis can be a major problem for productivity and morale.
Conversely, a tool that is a good fit gets out of people's way and makes their jobs easier can be a major boost to productivity and morale.

(rr-rdm-elns-choosing-failure-modes)=
### Failure modes in user adoption of ELNs

Incomplete or inflexible ELN solutions which increase friction in workflows can cause issues.
People will avoid using ill-fitting tools that they perceive them to be getting in their way, especially scientists.
They are creative, stubborn, resourceful, and impatiently focused on anwsering their research questions with watever tools are available to them. 
Finding software with the flexibility, capability, and scope to keep up is not easy and if it doesn't researchers won't use it - at least not as you intended.

-   Shadow IT/notebooks
    -   People using their own unsactioned solutions which may be a compliance issue and introduce risks that you have not accounted for.
-   Infrequent updates
    -   People dump a copy of their work into the ELN only as often as necessary for compliance.
-   Consistency issues
    -   If there are paper and potentially multiple electronic copies of some information - what happens when it does not agree? What is the source of truth?
-   Partial adoptions can lead to information which was previous predictably structured in lab notebooks being spread across multiple IT systems and physical copies
-   Practical use and interface issues
    -   Laptops or tablets can introduce interface barriers 
        -   Lab gloves may hamper the use of touchscreens and track pads.
        -   Free-hand drawing or use of notation not easily represented in simple text such as mathematical and chemical notation
        -   Performant native applications for devices are not always available, notebooks only accessible through web apps can have performance issues that make their interfaces frustrating to use
        -  No spatial memory, whereas in a physical book people may remember where they wrote things and can open it roughly on the right page.

-   Lack of sufficiently available training on more complex aspects of the ELN solution leading to poor, mis-use, or under-use of ELN features.
    -   Extra expense, maintenence & procurement issues with hardware suitable for use in your research environment

(rr-rdm-elns-choosing-compare-to-paper)=
### Always compare to paper notebooks

When picking an ELN remember to always compare the ELN to a paper notebook and not just to other ELNs.
It is likely paper that you are replacing so this is the benchmark against which to compare.
Consider the differences between a paper copy of a lab notebook and an electronic copy.
Consider also which are the properties of a paper copy that it is important that you are able to retain when adopting an electronic alternative.

-   A paper lab notebook is physically under your control.
-   You (or more likely your organisation) own it.
-   You can control access to it physically.
-   Your physical possession of this resource means that it would be difficult for anyone to prevent you from accessing it.
-   Conversely it must be physically stolen to be accessed by a malicious third party.
-   On the other hand, ELNs - like all software - have security vulnerabilities.
-   You are not dependent on the functioning of any complex systems like computer networks in order to be able to use your paper lab notebook.
-   You do not need any specialist tools in order to access its contents.
-   There is no reason why you might have to pay a third party a fee in order to continue using it.
-   You do not have to agree to a 'terms of service' or 'end-user license agreement' with a third party to use and retain access to your lab book. These terms may be subject to unilateral alteration by that third party.

If your provider of paper lab books goes out of business it has almost no bearing on your ability to continue doing your work.
One paper notebook is much like another, finding a new provider is pretty easy.
Changing providers does not impact on your ability to access your past notebooks or to continue operating with the same workflow in future ones.
This is not necessarily true of ELNs.

(rr-rdm-elns-choosing-archival)=
### Archival function of notebooks

Few active measures are needed to maintain the data in your paper notebooks. 
The primary vulnerability of paper lab books is that there is only one copy. 
Nevertheless, as long as they are kept in a cool, dry and dark spot (for example a fireproof safe) they will likely last decades.

Electronic data requires much more active upkeep.
Electronic data can *if managed properly* be more resilient to physical threats such as fire and flooding as it can frequently be backed up in multiple locations.
A hard drive, or even a solid state drive, however, cannot be left in a draw for a decade or more and have a high likelihood of working without some amount of bit-rot or compatibility issue when plugged back in.

Lab notebooks perform an archival function and proprietary formats are antithetical to this as they assume the institution which can act as a gatekeeper to the use of the proprietary format will outlive the need to archive the material.
When choosing an archival format one seeks to maximize the likelihood that one can recover the relevant information from that format.
Using a proprietary solution for archival purposes is taking a needless risk with the future of your data.
Your data's fate can become tied to that of the company, or project, that develops and operates the software that you use to store your lab notes.

(rr-rdm-elns-choosing-lockin)=
### Lock-in

Most proprietary or open tools will permit you to export your data in one format or another.
The quality of this export is critical to scrutinise.
The ability to save all your lab books as PDFs is fine but if it is the only option you may lose a lot of metadata, and the ability to import your data into a new solution. 
The ability to export your data and retain it's structure is very important to evaluate.

Proprietary solutions are incentivised to attempt to lock-in their customers so that the cost of switching to a competitor is high - so be especially wary of poor export options.
Note that this tends to change over time. 
New providers are focused on user aquisition so data portability tends to be good at first but decline after a certain point in time.
Firms tends to follow a pattern of shifting from a user acquisition phase with favourable terms, to a user retention phase with less favourable ones.
Mendeley for example began [encrypting their local database](https://www.zotero.org/support/kb/mendeley_import#mendeley_database_encryption). 
This made it impossible to migrate your local library to different reference managers without going through the Mendeley online library feature.
This occurred after they had reached a high degree of market penetration and had been acquired by Elsevier.

When looking for any critical piece of software for long term use the first questions to ask are:
- Is there an Libre / open-source solution to this problem?
- If it is a web app and/or has a server: Could I host my own fully featured instance, should I need to?
- Is there a large/active community using the project, does it have institutional backing of some kind? 
  This might take the form of a company which sells service contracts, or offers paid hosting ideally with feature parity with a self-hosted option. 
  Or perhaps a foundation or other non-profit/academic organisation with robust funding.
- What are the data export options and formats?

Open solutions provide you with the assurance that if you do the appropriate preparatory work you should be able to access all of your data in its native form.
For example keeping copies of the ELN software that can be run offline in a VM or similar computational environment in the future.
This is typically much easier for open applications and can be impossible for proprietary ones.
Even if the tools are no longer maintained they can still be used to read the data and interact with it in (mostly) the same way.
The data will also likely be stored in an open format from which it can relatively easily be extracted and ported to a new format.
This may still be a lot of work but it is much more attainable than reverse engineering a proprietary format for which there is no documentation, or worse - dealing with encrypted files.

You can pay for third party hosting and administration of open source applications.
This is a solution when you don't have the expertise or internal resources to administer a self-hosted instance of an open-source ELN solution. 
In this case you get the best of both worlds: the benefits of professional support and the reassurance of an open solution.
You should still take regular local backups of exports from your hosting provider from which you could restore your ELN system with different hosting.
This means that you retain the option to change providers.
Conventional Software as a Service (SaaS) platforms are highly vertically integrated: the software development, hosting, and administration are package deal that you must take or leave as is.
Using open tools breaks this up affording you the flexibility to change any of these if the need arises and you have the resources to do so, it puts you in a better bargining position.

(rr-rdm-elns-choosing-automation)=
### Automation and integration

ELNs with APIs have the potential for integration with instruments that would permit direct deposition of data from connected instruments into ELNs or other connected research data management infrastructure.
These sorts of integrations are especially useful in workflows at core facilities. 
For example, bioimaging facilities can automate a substantial part of the image metadata deposition into image data management tools such as [OMERO](https://www.openmicroscopy.org/omero/).

(rr-rdm-elns-standards)=
## ELN standards and Project governance

ELNs offer many advantages over paper notebooks.
Nevertheless, ELNs come with a considerable amount of additional complexity and additional risks - so it is important to have a mitigation plan.
The ELN space is still quite young and rapildy changing.
ELNs represent a key component of digital infrastructure for the future of research.
As such it is important to think about how the academic community wants the ELN infrastructure to be owned and governed in the long run.
An interesting model to consider emulating here is [moodle](https://moodle.com/), an open source electronic learning environment popular with universities.
It offers commercial support and hosting and has a network of developers across the education sector who contribute to the core project, as well as creating custom integrations and extensions to meet their particular needs.
This structure allows institutions to pool resources to fund the development of features that they all need and keeps this infrastructural code in common ownership, avoiding the worst lock-in issues arising from the use of proprietary solutions.
This more open distributed model also allows individuals to work on their own custom extensions and integrations instead of being reliant on the ability and willingness of a company to implement a feature that you need.

Many open tools have very robust export and import options, as they are not subject to the incentives trap faced by proprietary offerings, though this is far from guaranteed.
This might include a complete database export that would let you seemlessly migrate to a different deployment of the tool. 
Or an archive of files organised by a for example a JSON file representation of your notes and files that retain most or all of the metadata and organisational information of your ELN.
There remains the challenge when migrating of finding a tool that can import what your old tool exported, and retain most of all of its structure.
Such a standard would, if properly adhered too, reduces the lock-in risk associated with using using both open and proprietary tools.

(rr-rdm-choosing-elns)=
## Resources for choosing ELNs

- [How to pick an electronic laboratory notebook](https://doi.org/10.1038/d41586-018-05895-3) by {cite:ps}`Kwok2018eln`
- [2019 Review of the Best Electronic Laboratory Notebooks](https://app.scientist.com/blog/2019/04/05/2019-review-of-the-best-electronic-laboratory-notebooks).
- [Guide on choosing an ELN from Simon Bungers of Labfolder](https://labfolder.com/electronic-lab-notebook-eln-research-guide/).
- The Harvard Longwood Medical Area Research Data Management Working Group Constructed an [Electronic Lab Notebook Comparison Matrix](https://doi.org/10.5281/zenodo.4723753) in 2021, for convenience [a nicely formatted google sheet version](https://docs.google.com/spreadsheets/d/1ar8fgwagOh30E31EAPL-Gorwn_g6XNf81g3VDQnQ_I8/edit#gid=0), is also available.
- This recent review {cite:ps}`higgins2022elns` provides a good overview of considerations when adopting an ELN solution. 
  It covers such things a regulatory compliance that is not yet touched on here.
  It does occasionally appear to conflate open-source solutions with self-hosted ones which need not necessarily be the case.
  Some companies will let you host proprietary apps on premises.
  It is also possible to pay for third party hosting and administration of open source applications.

(rr-rdm-eln-open-elns)=
## Select Open Infrastructure ELN Options

The following ELN options are each quite different but have many of the same core features.

*  [eLabFTW](https://www.elabftw.net/) 
    *   Has features such as: Laboratory resource scheduling feature for booking things like hoods and microscopes, automatic mol file previews for molecules and proteins, and support for free-hand drawing.
    *   eLabFTW has a [website](https://www.elabftw.net/), [documentation](https://doc.elabftw.net/) and there is a [demo](https://demo.elabftw.net/login.php) deployment that you can try out.
    *   Self-hosting is *relatively* simple [according to the documentation](https://doc.elabftw.net/install.html).
        There is also a [paid support tier](https://www.deltablot.com/elabftw/) which would be recommend for any larger deployment to support the ongoing development of the project.
    *   [Paid cloud hosting](https://www.deltablot.com/elabftw/) is available from the developer in a geographical region suited to your needs.
        A more expensive tier with hosting in France compliant with additional security and privacy certifications is available.

* [openBIS](https://openbis.ch/)
    *   Robust features for integrated metadata management, for example, linking to ontologies / controlled vocabularies.
    *   openBIS has an API and can integrate with Jupyterhub for Electronic Lab Notebooks.
    *   Complete Laboratory Inventory Nanagement System (LIMS) including stores management integrated with protocols and experiment records, including keeping track of bar-coded stocks.
    *   You can get a feel for it in the [demo](https://openbis-eln-lims.ethz.ch/openbis/webapp/eln-lims/) deployment.
    *   openBIS is a bit more complex to administer [based on its documentation](https://openbis.ch/index.php/docs/admin-documentation/).
    *   As openBIS is developed at ETH Zurich it can be hosted for you under the openRDM service operated by ETH Zurich scientific IT services.
        No fixed pricing is available - cost would be dependent on your specific needs.
    
* [OSF](https://osf.io/)
    *   OSF is oriented towards sharing and collaborating on your work, including the ability to generate DOIs and host pre-prints directly on the main instance.
    *   It is free to use OSF at the main instance at [osf.io](https://osf.io/).
        For larger data you must provide your own additional [storage add-ons, available from a number of cloud storage providers](https://help.osf.io/article/395-storage-add-ons).
    *   Whilst you could deploy your own self-hosted OSF this is not how it is intended to be used (except for development).
    *   The OSF has strong sharing features, making it easy to share parts of your ELN publicly.

When using an open solution it is always important to consider how you can contribute to its ongoing development and maintenance, for example by donating to the project.
If it makes sense given the makeup of your organisation and that of the project you may also be able to contribute developer time to the project.

(rr-rdm-additional-eln-resources)=
## Additional ELN resources

* [Electronic Lab Notebooks: can they replace paper?](https://doi.org/10.1186/s13321-017-0221-3) by {cite:ps}`Kanza2017eln`
* [Electronic Lab Notebooks](https://datamanagement.hms.harvard.edu/collect-analyze/electronic-lab-notebooks) by Harvard Medical School
* [RSpace](https://www.researchspace.com/)

