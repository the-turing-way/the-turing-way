# Storage and backup

Data loss can be catastrophic for your research project and can happen often. You can prevent data loss by picking
suitable storage solutions and backing your data up frequently.

## Where to store data

- Most institutions will provide a _network drive_ that you can use to store data.
- _Portable storage media_ such as memory sticks (USB sticks) are more risky and vulnerable to loss and damage.
- _Cloud storage_ provides a convenient way to store, back and up and retrieve data.
You should check terms of use before using them for your research data.

Especially if you are handling personal or sensitive data, you need to ensure the cloud option is compliant with any
data protection rules the data is bound by.
To add an additional layer of security, you should encrypt devices and/or
files where needed.

Your institution might provide local storage solutions and policies or guidelines restricting what you can use.
Thus, we recommend you familiarise yourself with your local policies and recommendations.

When you are ready to release the data to the wider community, you can also search for the appropriate [databases and repositories](https://fairsharing.org/databases) in FAIRsharing, according to your data type, and type of access to the data.
Major [publishers are progressively defining clearer recommendations for data deposition and sharing](https://fairsharing.org/recommendations), endorsing specific generics as well as domain-specific databases and repositories.

### Data organisation

To organise your data you can create a folder structure (or re-use a [folder structure](http://nikola.me/folder_structure.html) to ensure that you are able to find your files.

-	Make sure you have enough (sub)folders so that files can be stored in the right folder and are not scattered in folders where they don’t belong or stored in large quantities in a single folder
-	Use a clear folder structure: you can structure folders based on the person that has generated the data/folder, chronologically (month, year, sessions), per project (as done in the example above), or based on analysis method/equipment/type of data.

You can also pull/download folder structures using GitHub.
[This template](https://github.com/bvreede/good-enough-projec) by Barbara Vreede, based on [cookiecutter](https://github.com/cookiecutter/cookiecutter), follows recommended practices for scientific computing by [Wilson et al. (2017)](https://doi.org/10.1371/journal.pcbi.1005510).

### File Naming conventions

Structure your file names and set up a template for this.
 It is very useful to start with the date (when the file was generated: YYYYMMDD) which will sort your files chronologically and also creates a unique identifier for each file.
 This process will be immediately clear if there are multiple files generated on the same day that will have to be given a version number –or “A, B”-, because otherwise overwriting would occur, if you store these files in the proper folder).

Basic tips for file naming:
• Date or date range of experiment: YYYYMMDD
• File type
• Researcher's name/initials
• Version number of file (v001, v002) or language used in the document (ENG)
• Don’t make file names too long (this can complicate file transfers)
• Avoid special characters (?\!@\*%{[<>) and spaces

You can explain the file naming convention in a README.txt file, so that it will also become clear to others what the file names mean.

## Backups

To avoid loosing your data, you should follow good backup practices.

- You should have 2 or 3 copies of your files, stored on
- at least 2 different storage media,
- in different locations.

The more important the data and the more often the datasets change, the more frequently you should back them up.
If your files take up a large amount of space and backing up all of them would be difficult or expensive, you may want to create a set of criteria for when you back up the data. This can be part of your data management plan.
