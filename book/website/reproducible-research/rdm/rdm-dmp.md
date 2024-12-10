(rr-rdm-dmp)=
# Data Management Plan

A Data Management Plan (DMP), or Output Management Plan, is a document that describes how your research outputs will be generated, stored, used and shared within your project. 
A DMP is a living document, which can be updated throughout the research project as needed. 

A Data Management Plan is a roadmap for you to manage your data efficiently and securely. 
This can prevent data loss or breaches. 
Planning ahead on how to manage your data consistently can save you time later on! It can also make it easier to {ref}`share<rr-rdm-sharing>` your data with others and therefore make the data more {ref}`FAIR<rr-rdm-fair>`

```{figure} ../../figures/data-management-plan.*
---
name: data-management-plan
alt: There are two women in the illustration. The left one is looking distressed and says 'Oh no, my computer crashed! I lost all the data!' The right woman is holding a map which says DMP (Data Management Plan) and is looking happy. She is saying 'Good thing I had a plan! The data is all backed up! 

---
Data Management Plan. _The Turing Way_ project illustration by Scriberia. Zenodo. [http://doi.org/10.5281/zenodo.3332807](http://doi.org/10.5281/zenodo.3332807)
```


## A Data Management Plan should provide information on six main topics:

### 1. Roles and Responsibilities
* It is important to discuss who is responsible for different tasks during the life-cycle of a research project. 
Defining who is responsible for the management of the data and code can prevent confusion/miscommunication later in the project.
* You should check the DMP recommendations and requirements of your institute and funder. 
The library research support team of your institute and the website of your funder are usually good places to find information and help. 
Some of the funders require you to use their DMP template. 
You can check if your funder or institute has a DMP using [DMPonline](https://dmponline.dcc.ac.uk/).

### 2. Type and size of data collected and documentation/metadata generated
* Here, you can list the file formats you will use to collect, process and present your data. 
If you want to share your research outputs later, standard file formats that can be openly used without a particular license for a software programme are preferred.
To ensure this, you should adapt your files or start working in these formats early on. 
* A distinction can be made between different types of data that can be described in the plan separately: 
    * Raw/primary data: data collected from the source (always keep a read-only version of raw data so you can come back to it later!)
    * Processed data: a version of the data that has been modified for analysis or visualisation
    * Finalised data: data that is ready to be shared in a publication or data repository (see {ref}`Sharing and archiving data section <rr-rdm-sharing>` for more information). 
Some data repositories, such as [Zenodo](https://zenodo.org/), allow versioning of datasets so that you can update your finalised dataset if you want to release another version.
* All of these types of data will have to be described to be placed into context by using metadata (see the {ref}`Documentation and metadata section<rr-rdm-metadata>`) and adequate documentation which will allow future you, and anyone in your team, to interpret the data. 
* It is helpful to know the approximate size (in the range of MB, GB, TB or PB) of the data in these various stages because this will affect the storage solutions available for you (discussed in the next point). 

### 3. Type of data storage used and back up procedures that are in place
* Check the {ref}`data storage and organisation section<rr-rdm-storage>` for storage and back-up solutions and ways to organise your files 
* Keeping track of who made specific changes in your data/code will be important, particularly for code.
See the {ref}`Version Control chapter<rr-vcs>` for more information.
* Determine who has access to the data and who grants access. 
At least one other person should have access to your data, such as your supervisor/PI/head of the department. 
If you're managing personal/commercially sensitive data, access should only be given to individuals that have to work with the data. 

### 4. Preservation of the research outputs after the project
* Consider whether your research outputs can be made publicly available. 
Personal data or research outputs needed to apply for patents cannot be publicly shared, see the {ref}`Open data section<rr-open-data>`
If data cannot be made publicly available you will still have to preserve it for several years, depending on the policies of your country, institute and funder.
* You can outsource long term preservation of your data to a data repository. 
You can find more information on how to select an appropriate repository in {ref}`sharing and archiving data<rr-rdm-sharing>` section
    * Select repositories using, for example, [FAIRsharing](https://fairsharing.org/) or [Nature's recommended repository list](https://www.springernature.com/gp/authors/research-data-policy/repositories/12327124), that provide a persistent identifier such as a DOI for your research output. 

A repository should have a preservation policy that specifies how long your outputs will be curated. 
When in doubt, contact your library Research Data Support Team for more information about data repositories.

* For digital preservation, ensure that the research data can be discovered, accessed, used and understood now and in future. 
This requires that you address the technological changes, changing user behavior and new requirements on the computer-aided processing of research data as well as evolving organisational.

### 5. Reuse of your research outputs by others
* Select a license when you make your output available on a repository (see the Licensing subchapters on {ref}`data<rr-licensing-data>` and {ref}`software<rr-licensing-floss>` for more information).
By selecting a license you tell others how they can reuse your data. 
If you do not select a license others will not be able to reuse your data without asking you for permission. 
* You can put your research outputs into context using and introduction text, such as a README.txt file
    * See the {ref}`documentation and metadata section<rr-rdm-metadata>`

### 6. Costs
* Check if there are any costs associated with your project
    * Preferred storage solution (during and after the project, see #3-4)
    * Personnel costs (if you need a data manager to manage more sensitive or large quantities of data)
    * Software licenses (such as Electronic Lab Notebooks, see the {ref}`Open notebooks section<rr-open-notebooks>`
    * You can use this [checklist for costs](https://www.ukdataservice.ac.uk/media/622368/costingtool.pdf) as a guidance

You can use this [checklist](https://ukdataservice.ac.uk/learning-hub/research-data-management/plan-to-share/checklist/) to see if you have everything covered in your Data Management Plan. 

(rr-rdm-dmp-tools)=

## DMP tools 
There are several platforms or tools that you can use to set up your Data Management Plan: 

* [ARGOS](https://argos.openaire.eu/home)
* [DMPonline](https://dmponline.dcc.ac.uk)
* [DMPtool](https://dmptool.org)

See [activeDMPs](https://activedmps.org/) for a full overview.

## Additional Resources

- [UK Data Services data management information](https://ukdataservice.ac.uk/learning-hub/research-data-management/)
- [TU Delft Research Data Management portal](https://www.tudelft.nl/en/library/research-data-management)
- [Research Data Management](https://www.scienceeurope.org/our-priorities/research-data/research-data-management/) by Science Europe
- Books
   - {cite:ps}`Briney2015dmp`
- Articles
   - {cite:ps}`Briney2020dmp`
   - {cite:ps}`Hart2016dmp`
   - {cite:ps}`Michener2015dmp` 
- Videos
   - [Videos (3-7 min) on data management by Kristin Briney](https://www.youtube.com/watch?v=K5_ocBG5xek&list=PLEor4jq8YPgK_sgEiAcpHZLw-62mufXus)
   - Video on [elements of a DMP](https://commons.esipfed.org/node/1442).
   - [3 min video on Roles and Responsibilities](https://www.youtube.com/watch?v=Ry0OA9mDTCc )
   - [DMPs by DTU Bibliotek](https://www.youtube.com/watch?v=tvs5_X5rn8w) (20 minutes)
   - [Areas of a Data Management Plan](https://www.youtube.com/watch?v=L3LPv2sB-IE) (7 minute video by Moore Library)
- Definition of [Long Term Preservation](https://www.gesis.org/en/research/research-data-management/long-time-preservation) from the Leibniz Institute of Social Science.
- Planning by [DataOne](https://dataoneorg.github.io/Education/bp_step/plan/) & [USGS](https://www.usgs.gov/data-management/planning)


