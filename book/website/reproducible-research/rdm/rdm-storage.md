(rr-rdm-storage)=
# Data Storage and Organisation

Data loss can be catastrophic for your research project and can happen often. 
You can prevent data loss by picking suitable storage solutions and backing your data up frequently.

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

To organise your data, you can create a folder structure, or re-use a previous structure (see an example below), to ensure that you can find your files.

-	Make sure you have enough (sub)folders so that files can be stored in the right folder and are not scattered in folders where they do not belong, or stored in large quantities in a single folder.
-	Use a clear folder structure. 
You can structure folders based on the person that has generated the data/folder, chronologically (month, year, sessions), per project (as done in the example below), or based on analysis method/equipment or data type.

(rr-rdm-storage-organisation-examples)=
### Data Organisation Examples

- Download [this](http://nikola.me/folder_structure.html) folder structure by Nikola Vukovic
- You can pull/download folder structures using GitHub: 
[This template](https://github.com/bvreede/good-enough-project) by Barbara Vreede, based on [cookiecutter](https://github.com/cookiecutter/cookiecutter), follows recommended practices for scientific computing by [Wilson et al. (2017)](https://doi.org/10.1371/journal.pcbi.1005510).
- See [this template](https://osf.io/4sdn3/) by Chris Hartgerink for file organisation on the [Open Science Framework](https://osf.io/).

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

You can explain the file naming convention in a README.txt file so that it will also become apparent to others what the file names mean.

(rr-rdm-storage-backups)=
## Backups

To avoid losing your data, you should follow good backup practices.

- You should have 2 or 3 copies of your files, stored on
- at least 2 different storage media,
- in different locations.

The more important the data and the more often the datasets change, the more frequently you should back them up.
If your files take up a large amount of space and backing up all of them proves to be challenging or expensive, you may want to create a set of criteria for when you back up the data.
This can be part of your data management plan (DMP).
