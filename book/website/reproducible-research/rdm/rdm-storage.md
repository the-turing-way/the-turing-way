(rr-rdm-storage)=
# Data Storage and Organisation

Data loss can be catastrophic for your research project and can happen often.
You can prevent data loss by picking suitable storage solutions and backing your data up frequently.

```{figure} ../../figures/version-control.*
---
height: 500px
name: version-control
alt: Two images are shown to represent the benefits of using version control. On the left, there is an image of two people rummaging through a blue box on top of a table. The box is full of jumbled documents and the people look confused and frustrated. The documents are named "final 2" and "let this be the final". On the right, the same two people look happy and are searching through files organised clearly in a blue filing cabinet. There are "V1, V2, V3 and V4" separations organising the files.
---
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. [http://doi.org/10.5281/zenodo.3695300](http://doi.org/10.5281/zenodo.3695300)
```

(rr-rdm-storage-where)=
## Where to Store Data

- Most institutions will provide a _network drive_ that you can use to store data.
- _Portable storage media_ such as memory sticks (USB sticks) are more risky and vulnerable to loss and damage.
- _Cloud storage_ provides a convenient way to store, backup and retrieve data.
You should check terms of use before using them for your research data.

Especially if you are handling personal or sensitive data, you need to ensure the cloud option is compliant with any data protection rules the data is bound by.
To add an extra layer of security, you should encrypt devices and files where needed.

Your institution might provide local storage solutions and policies or guidelines restricting what you can use.
Thus, we recommend you familiarise yourself with your local policies and recommendations.

When you are ready to release the data to the wider community, you can also search for the appropriate databases and repositories in [FAIRsharing](https://fairsharing.org/databases), according to your data type, and type of access to the data.
Learn more about this in the {ref}`rr-rdm-sharing` subchapter.

(rr-rdm-storage-organisation)=
## Data Organisation

To organise your data, you should use a clear folder structure to ensure that you can find your files. 
We encourage you to use an existing template.
An open source project created a quite complete one at https://github.com/tonic-team/Tonic-Research-Project-Template 

```{figure}  ../../figures/file-management-manual.jpg
---
name: Folder structure for research data
alt: A protagonist has a file written "readme" on it and bring it to another protagonist who stays in front of a file drawer system. There are  three drawers labelled "data", "code", and "results".
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

-	Make sure you have enough (sub)folders so that files can be stored in the right folder and are not scattered in folders where they do not belong, or stored in large quantities in a single folder.
-	Use a clear folder structure.
You can structure folders based on the person that has generated the data/folder, chronologically (month, year, sessions), per project (as done in the example below), or based on analysis method/equipment or data type.
- Avoid overlapping or vague folder names, and do not use personal data in folder/file names.

(rr-rdm-storage-organisation-examples)=
### Data Organisation Examples

- Download [this](http://nikola.me/folder_structure.html) folder structure by Nikola Vukovic
- You can pull/download folder structures using GitHub:
[This template](https://github.com/bvreede/good-enough-project) by Barbara Vreede, based on [cookiecutter](https://github.com/cookiecutter/cookiecutter), follows recommended practices for scientific computing by [Wilson et al. (2017)](https://doi.org/10.1371/journal.pcbi.1005510).
- See [this template](https://osf.io/4sdn3/) by Chris Hartgerink for file organisation on the [Open Science Framework](https://osf.io/).
- [How to Organize Your Digital Files](https://www.nytimes.com/wirecutter/guides/how-to-organize-your-digital-files/) by Melanie Pinola.
- [Project structure videos by Danielle Navarro](https://www.youtube.com/watch?v=u6MiDFvAs9w&list=PLRPB0ZzEYegPiBteC2dRn95TX9YefYFyy&index=1) (with [slides](https://slides.djnavarro.net/project-structure/#1)).

### More Information on Data Organisation
- [How to organise your data and code](https://renebekkers.wordpress.com/2021/04/02/how-to-organize-your-data-and-code) by Rene Bekkers. 

(rr-rdm-storage-conventions)=
## File Naming Conventions

Structure your file names and set up a template for this.
For example, it may be advantageous to start naming your files with the date each file was generated (such as `YYYYMMDD`).
This will sort your files chronologically and create a unique identifier for each file.
The utility of this process is apparent when you generate multiple files on the same day that may need to be versioned to avoid overwriting.

Some other tips for file naming include:
- Use the date or date range of the experiment: `YYYYMMDD`
- Use the file type
- Use the researcher's name/initials
- Use the version number of file (v001, v002) or language used in the document (ENG)
- Do not make file names too long (this can complicate file transfers)
- Avoid special characters (?\!@\*%{[<>) and spaces
- Avoid personal data in file names

You can explain the file naming convention in a README.txt file so that it will also become apparent to others what the file names mean.

For further guidance on file naming: 
- [Jenny Bryan’s ‘naming things’ presentation](https://speakerdeck.com/jennybc/how-to-name-files) (or watch the [5 minute summary](https://youtu.be/ES1LTlnpLMk))
- [MIT's recommendations on File naming and folder hierarchy](https://libraries.mit.edu/data-management/store/organize/)
- [8 step guide on how to set up your file naming convention](https://resolver.caltech.edu/CaltechAUTHORS:20200601-161923247) 

(rr-rdm-storage-renaming)=
### File renaming tools

If you want to change your file names you have the option to use bulk renaming tools.
Be careful with these tools, because changes made with bulk renaming tools may be too rigorous if not carefully checked!

Some bulk file renaming tools include: 
- [Bulk Rename Utility](http://www.bulkrenameutility.co.uk/Main_Intro.php), [WildRename](http://www.cylog.org/utilities/wildrename.jsp), and [Ant Renamer](http://www.antp.be/software/renamer) (for Windows)
- [Renamer](https://renamer.com/) (for MacOS)
- [PSRenamer](http://www.cylog.org/utilities/wildrename.jsp) (for MacOS, Windows, Unix, Linux)

(rr-rdm-storage-backups)=
## Backups

To avoid losing your data, you should follow good backup practices.

- You should have 2 or 3 copies of your files, stored on
- at least 2 different storage media,
- in different locations.

Backups are ideally done automatically and should take into consideration your institute's guidelines.
The more important the data and the more often the datasets change, the more frequently you should back them up.
If your files take up a large amount of space and backing up all of them proves to be challenging or expensive, you may want to create a set of criteria for when you back up the data.
This can be part of your {ref}`Data Management Plan<rr-rdm-dmp>`.

Watch this video on [Safe data storage and backup](https://www.youtube.com/watch?v=bgbbToXHgW0) from the [TU Delft Open Science MOOC](https://online-learning.tudelft.nl/courses/open-science-sharing-your-research-with-the-world/).



