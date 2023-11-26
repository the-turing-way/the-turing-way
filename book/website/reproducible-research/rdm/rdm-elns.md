(rr-rdm-elns)=
## Electronic Lab Notebooks

An Electronic Laboratory Notebook (commonly known as an ELN or a digital lab notebook) is a software system designed to help you document and maintain reproducibility of your research and share information more easily.

Electronic lab notebooks provide the following **functionalities**:

* A text editor with similar functions as a paper notebook
* A search function
* Secure storage and back up (especially in comparison to paper notebooks)
* Tools for working with tabular data (calculations and formatting of tables and graphs)
* Templates for documenting standard procedures
* Laboratory inventories for managing and documenting samples, reagents and apparatus
* Collaboration tools for sharing experimental information
* Some ELNs will allow you to comply with standards and regulations because of their certification processes

ELNs also have their **limitations**: 

* **Costs**: Most ELN solutions can only be used through paid plans, or the free plans have reduced functionalities in the number of users, storage space or file sizes.
Your lab may also not have access to tables or pens that would make the use of ELNs easier.
Check if your institution is offering a solution that you can use without additional costs.
* **File format**: Always check if files can be exported in your preferred file formats to avoid format lock-in.
Some ELNs also have API's that allow integration with other software and workflows. 
* **Vendor-lock-in**: Once you're using a certain solution you may become dependent on it.
Always have an exit strategy in case the solution is no longer offered or if you're moving institutions and you no longer have access.
* **Sustainability**: Choose a solution that has a larger chance of being around for a long time.
* **Drawing**: Not all solutions have the tools or capabilities to include drawings or integration with drawing software.
* **Security**: Before using an ELN solution you should check any backup plans and data security measures, especially if you're working with sensitive data.
* **Laboratory situation**: Your lab may not have an internet collection or electronic tools could affect samples, reagents or magnets in the lab. 
* **Learning curve**: ELNs have a longer learning curve than paper notebooks and it takes time to learn how to use them.
User-friendliness and flexibility are important to accommodate the widely varying workflows of each lab member.

ELNs can be software that is specifically build as an ELN, such as RSpace or you can combine workflows such as Atom and the Open Science Framework to take notes digitally.
There are many solutions to choose from: [How to pick an electronic laboratory notebook](https://doi.org/10.1038/d41586-018-05895-3) by {cite:ps}`Kwok2018eln` or [2019 Review of the Best Electronic Laboratory Notebooks](https://app.scientist.com/blog/2019/04/05/2019-review-of-the-best-electronic-laboratory-notebooks) may help you to find your solution!


Electronic Lab Notebooks (ELNs) enable researchers to organize and store experimental procedures, protocols, plans, notes, data, and even unfiltered interpretations using their computer or mobile device.
They can be a digital analogue to the paper notebook most researchers keep.
ELNs can offer several advantages over the traditional paper notebook in documenting research during the active phase of a project, including; searchability within and across notebooks, secure storage with multiple redundancies, remote access to notebooks, and the ability to easily share notebooks among team members and collaborators.
However, it is important when choosing an ELN solution to avoid giving up the advantages offered by a paper lab notebook.

Open notebook [{term}`def<Open Notebooks>`] research is simply the practice of making such notebooks openly available, usually online.
Some researchers choose to keep their notebooks open from the very beginning of their projects.
Rather than wait months, or years, to share their research through journal publication as is the current practice, this allows researchers to post their experimental data and protocols online and in real-time.
Sharing research in this open and timely manner helps to reduce duplication of work, helps foster new collaborations, and cultivates a more open dialogue with others.
It also helps researchers avoid exploring dead ends and making mistakes that may have already been covered by their colleagues but went unpublished because of lack of scientific interest.

Open notebooks have the further benefit of increasing the quality of scientific outputs by forcing researchers to be careful, thorough, and explicit.
Making research open has the added benefit of increasing the likelihood that any errors made in an investigation will be spotted quickly, instead of down the line.
Immediate fixes will have much less impact on a research project, which will save research time, lab money, and pride.

Ideally, every scientist should maintain an open notebook, which would encompass all aspects of their research, in real-time.

patents, prior publication

However, fears about dealing with complete open access, conflicts with ~~intellectual property~~ and publications, and ?online data overload? hamper this movement.

To combat this, practitioners encourage any form of open notebook research ("make open what you can") even if that means uploading some information for a project from many years ago that never saw the light of day.

(rr-open-notebooks-choosing-an-eln)=
## Choosing an ELN solution

The choice of ELN may have been made for you by your organisation.
In this case you may have to live with the consequences of their choice, for good or ill.
If you are in a position to choose an ELN to use, or are making a choice on behalf of an organisation here are some factors to consider.

There are an immense and baffling array of options in the Electronic Lab Notebook space.
Many organisations offer software that purports to solve the proplem of electronic lab notebooks.
So choosing a suitable solution can be a major headache.
The choice of ELN is an incredibly important decision, and one that your organisation will likely have live with for years, or even decades.
You are putting the record of your research into the hands of the tool that you choose, and entering into a long-term relationship with the provider of your ELN solution.

Consider the differences between a paper copy of a lab notebook and an electronic copy.
Consider also which are the properties of a paper copy that it is important that you are able to retain when adopting an electronic alternative.

A paper lab notebook is physically under your control.
You (or more likely your organisation) own it.
You can control access to it physically.
Your physical possession of this resource means that it would be difficult for anyone to prevent you from accessing it.
You are not dependent on the functioning of any complex systems like computer networks in order to be able to use your paper lab notebook.
You do not need any specialist tools in order to access its contents.
There is no reason why you might have to pay a 3rd party a fee in order to continue using it.
You do not have to agree to a 'terms of service' or 'end-user license agreement' with a 3rd party, the terms of which may be subject to unilateral alteration by that 3rd party, in order to use and retain access to your lab book.

If your provider of paper lab books goes out of business it has almost no bearing on your ability to continue doing your work.
One paper notebook is much like another, finding a new provider is pretty easy.
Changing providers does not impact on your ability to access your past notebooks or to continue operating with the same workflow in future ones.
This is not necessarily true of ELNs.

Few active measures are needed to maintain the data in your paper notebooks, they are vulnerable as they exist in only one copy but as long as they are kept in a cool, dry and dark spot for example a fireproof safe they will likely last decades.
Electronic data requires much more active upkeep
Electronic data can if manged properly be more resilient to physical threats such as fire and flooding as it can frequently be backed up in multiple locations.
A hard drive or even a solid state drive however cannot be left in a draw for a decade or more and have a high likelihood of working without some amount of bitrot or compatability issue when plugged back in.

Lab notebooks perform an archival function and proprietary formats are antithetical to this as they assume the institution which can act as a gatekeeper to the use of the proprietary format will outlive the need to archive the material.
When choosing an archival format one seeks to maximize the likelihood that one can recover the relevant information from that format.
Using a proprietary solution is talking a needless risk with the future of your data.
Your data's fate can become tied to that of the company, or project, that develops and operates the software that you use to store your lab notes.

When looking for any critical piece of software for long term use the first questions to ask are:
- Is there an Libre / open-source solution to this problem?
- If it is a web app: Could I host my own fully featured instance, should I need to?
- Is there a large/active community using the project, does it have some institutional backing of some kind? 
  This might take the form of a company which sells service contracts, or offers paid hosting ideally with   feature parity with a self-hosted option. 
  Or perhaps a foundation or other non-profit/academic organisation with robust funding.
- What are the data export options and formats?

Open solutions provide you with the assurance that if you do the appropriate preparatory work you should be able to access all of your data in it's native form by running the ELN application in a virutual machine or similar reproducible computational environment in the future should you need to.
Even if the tools are no longer maintained and in a state that can be used in production.
They can still be used to read the data and interact with it in (mostly) the same way.
The data will also likely be stored in an open format from which it can relatively easily be extracted and ported to a new format.
This may still be a lot of work but it is much more attainable than reverse engeering a proprietary format for which these is no documentation or worse still dealing with encrypted files.
Most propritary or open tools will permit you to export your data in one format or another, however the quality of this export is critical to scrutinise.
The ability to save all your lab books as PDFs is fine but if it's the only option you may loose a lot of metadata, and the ability to import your data into a new solution. 
Migration may cost you much of your data's structure.
Propritary solutions are incentivised to attempt to lock-in their customers so that the cost of switching to a competitor is high so be especially wary of poor export options.
Note that this can change over time.
Mendeley for example began [encrypting their local database](https://www.zotero.org/support/kb/mendeley_import#mendeley_database_encryption) making it impossible to migrate your local library to different reference managers without going through their online library feature.
Many open tools on the other hand have very robust exort and import options, as they are not subject to this incentives trap, though this is far from garunteed.
This might include a complete database export that would let you seemlessly migrate to a different deployment of the tool. 
Or an archive of files organised by a JSON file representation of your notes and files that retain most or all of the metadata and organisational information of your ELN.

Harvard Longwood Medical Area Research Data Management Working Group
Electronic Lab Notebook Comparison Matrix
https://doi.org/10.5281/zenodo.4723753
(nicely formatted google sheet version for convenience: https://docs.google.com/spreadsheets/d/1ar8fgwagOh30E31EAPL-Gorwn_g6XNf81g3VDQnQ_I8/edit#gid=0)

This recent review {ref}`@higgins2022` (https://doi.org/10.1038/s41596-021-00645-8) provides a good overview of considerations when adopting an ELN solution. 
It cover such things a regulatory compliance that I have not touched on here.
It does occasionally appear to conflate open-source solutions with self-hosted ones which need not necessarily be the case.
This [guide on choosing an ELN from Simon Bungers of Labfolder](https://labfolder.com/electronic-lab-notebook-eln-research-guide/) is also worth a read.

Some companies will let you host proprietary apps on premises and you can pay for 3rd party hosting and administration of open source applications.

This is important as if you don't have the expertise or internal resources to administer a self-hosted instance of an open-source ELN solution you can still pay a 3rd party to do this for you in which case you get the benefits of professional support and the reassurance of an open solution.

You should still take regular local backups of exports from your hosting provider from which you could restore your ELN system with different hosting.
This means that you retain the option to change providers as the hosting and support are no longer vertically integrated parts of the software as a service (SaaS) experience for you.


> note on potential for integration with instrumentation through APIs that would permit direct deposition of data from connected instruments into ELNs.


```{note}
The ELN function is also frequently combined with a LIMS (Laboratory information/inventory management system) solution as the two are often closely interrelated.
They are however distinct functions and you may wish to pick different tools for these functions.
```


__Select Open Infrastructure ELN Options__

They are each quite different but have many of the same core features.
For example rich text editing in a web browser.
The ability to upload files.
Sharing and permissions based on roles/groups.

-  [eLabFTW](https://www.elabftw.net/) {#sec-elabftw}

    -   Laboratory resource scheduling feature for booking things like hoods and microscopes, automatic mol file previews for molecules and proteins & support for free-hand drawing.

    -   The eLabFTW [site](https://www.elabftw.net/) and [documentation](https://doc.elabftw.net/) there is also a [demo](https://demo.elabftw.net/login.php) deployment that you can try out

    -   Self-hosting is *relatively* simple [according to the documentation](https://doc.elabftw.net/install.html).
    There is also a [paid support tier](https://www.deltablot.com/elabftw/) which would be recommend for any larger deployment to support the ongoing development of the project.

    -   [Paid cloud hosting](https://www.deltablot.com/elabftw/) is available from the developer in a geographical region suited to your needs, a more expensive tier with hosting in France compliant with additional security and privacy certifications is available.

- [openBIS](https://openbis.ch/) {#sec-openbis}

    -   Good features for integrated metadata management e.g. linking to ontologies / controlled vocabularies.
    This is based in a flexible object system for making similar entries.

    -   openBIS has an API and can integrate with jupyterhub for electronic lab notebooks.

    -   Very feature rich LIMS system with optional integration of stores management with protocols and experiments including keeping track of bar-coded stocks.

    -   You can get a feel for it in the [demo](https://openbis-eln-lims.ethz.ch/openbis/webapp/eln-lims/) deployment.

    -   openBIS is a bit more complex to administer [based on its documentation](https://openbis.ch/index.php/docs/admin-documentation/).
    It's a slightly older and more complex project than the others on this list, meaning it is very featureful and well tested against the needs of the groups at ETH Zurich.

    -   Developed at ETH Zurich openBIS can be hosted for you under the openRDM service operated by ETH Zurich scientific IT services.
    No fixed pricing is available cost would be dependent on your specific needs

- [OSF](https://osf.io/) {#sec-osf}

    -   OSF is oriented towards sharing and collaborating on your work, including the ability to generate DOIs and host pre-prints directly on the main instance.

    -   It is free to use OSF at the main instance at [osf.io](https://osf.io/) so you can try it out there directly.
    For larger data you must provide your own additional [storage addons, available from a number fo cloud storage providers](https://help.osf.io/article/395-storage-add-ons).

    -   Whilst OSF can be hosted yourself this is presented by the project as for the purposes of development, and is not directly available as a paid service.

    -   Strong sharing features, makes it easy to take your ELN and make it, or parts of it, public.

```{tip}
Notes Beyond ELNs

There are additional sections covering the management of types on information which don't necessarily fit into an ELN solution for more general, personal or informal notes see the sort section on Personal Knowledge management @sec-personal-knowledge-management, for bibliographic information management the section on Zotero @sec-zotero, and for passwords the section on @sec-bitwarden.
```


### Additional ELN resources
* [Electronic lab notebooks: can they replace paper?](https://doi.org/10.1186/s13321-017-0221-3) by {cite:ps}`Kanza2017eln`
* [Electronic Lab Notebooks](https://datamanagement.hms.harvard.edu/collect-analyze/electronic-lab-notebooks) by Harvard Medical School


