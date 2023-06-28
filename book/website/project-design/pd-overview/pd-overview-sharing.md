(pd-overview-sharing)=
# Sharing Your Research Work

In order to make sure that (most) research outputs are available to everyone interested in analysing or reusing them, let's take some time to learn about how to share them.
Science can only progress when we build on each other's work.
Different digital research outputs or {ref}`research objects<cm-ro>`, such as data, software and code, protocols, reagents, and hardware, can be shared as open results on the web.
They should come with specific information such as licenses, documentation and source code (repository, online index or archive).

Sharing online is not enough - you should make sure that knowledge discovery and navigation process is clearly described.
You need to make sure that your research objects are **F**indable, **A**ccesible, **I**nteroperable and **R**eusable.
This is referred to as {ref}`FAIR Principles<rr-rdm-fair>` that provides guidelines to improve the Findability, Accessibility, Interoperability and Reusability of digital assets; all of which support research reproducibility.

This aspect is already considered when developing your {ref}`Data Management Plan (DMP)<rr-rdm-dmp>` (see {ref}`pd-overview-planning-dmp`).
Therefore, it is important to revisit your DMP to make sure that the guidelines are applied when making your results available.
You can learn more about this in a chapter on {ref}`making data FAIR<rr-rdm-fair>`).

(pd-overview-sharing-archive)=
## Share your data

When legally possilbe, your data should be archived in an open place, where people can access them.
If you have sensitive data, you will not be able to share the raw data, but there may be some data you can share.
A repository is a good place to store your data.

An overview of some repositories available for archiving your data can be found in [re3data.org](https://www.re3data.org/).

Another good resource where you can read more about this topic is the chapter on {ref}`Sharing and Archiving Data<rr-rdm-sharing>`.

(pd-overview-sharing-protocols)=
## Share your Protocols

One of the reasons to do reproducible research is to provide others with the tools to build on top of it.
If the details of the protocols are not shared, researchers can spend months optimizing them before being able to start with their projects.

A tool that can be used to avoid this is [protocols.io](https://www.protocols.io/).
It provides a way to ensure that your protocols are openly available, allowing you to update them while keeping track of the changes.
Furthermore, having your protocols online makes them easier to share, creating opportunity for contributing.

## Share Analysis Scripts and Research Software

If you have been using a version control system with a public repository (see the {ref}`Version Control<rr-vcs>` chapter), you have already done most of the work.
You should now consider putting a snapshot of your code in a repository, so you can be sure it gets archived for a relatively long time, and it become citable.
Indeed, there is no guarantee that the repository will stay available for a long time.


You can integrate your version control system with a general-purpose repository.
For example, when integrating GitHub or Gitlab with Zenodo (see {ref}`cm-citable-cite-software`), you can get Digital Object Identifiers or DOIs for your software.
This automatically makes it easier to share and makes it citable.
You can read about DOIs in the chapter on {ref}`Making Research Components Citable<cm-citable>`.



## Share Research Hardware

In absence of better solution, you may deal with your hardware documentation with the smae strategy as with your software: using version control  repositories during its development, and zenodo integration for archiving.
If your documentation is in the form of a website, try to provide a independent html build that can run without a server.

## Share reagents

Depending on your research domain, you may have produced reagents (genetic material or tissue for example). 
If there is a specific bank for these products that can share them widely, you may consider using them. 
Make sure a persistent identifier is given, an that the description of your reagents have enough metadata to make sharing useful.

## Collecting your Research

Once you are done with your research you may want to collect all the digital parts of your project in one place.
This is called a research compendium.
Publishing your paper along with a research compendium allows the full extent of your research: from the design of the project, through the data recollection and analysis and the resulting outputs.

This has endless advantages. It makes your work shareable and reproducible, others can build upon it and gives you more visibility.

You can read how to set up your research compendia, {ref}`this chapter<rr-compendia>`.

(pd-overview-sharing-License)=
## Add License to Research Outputs

Even if you got a license at the beginning of the project you need to think about it again when sharing your outputs and final results - this allows people to have the information about how your research should be reused and shared.

If you want more information about how to choose and add a license to your project you can check the {ref}`Licensing Chapter<rr-licensing>`.

(pd-overview-citation)=
## Receive Citations

All this hard work will have its reward. Having published all your research from the design to the results adds visibility to your work and more opportunity to get credit.

Not only can your results can be cited, but your methods and protocols can be reused and your design can be shared.

Read {ref}`this chapter on ORCID<cm-citable-orcid>` for more information about how you can collect different research outputs in one place using ORCID and highlight them to get fair credit for your work.
