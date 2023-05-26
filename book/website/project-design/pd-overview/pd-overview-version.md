(pd-overview-version)=
# Version Control and Documentation

Once the project is designed, it is important to keep track of all the changes.
This will save you a lot of time and can help others understand and reuse your research - you have a record of what worked best and information to understand why.

(pd-overview-version-experiments)=
## Experimental Work

It is necessary to write down all the details about your experimental work.
This allows future readers, a colleague and your future self to understand and reproduce all the experimental work related to your project.

A useful tool to do this is {ref}`Electronic Lab Notebooks<rr-open-notebooks>` (ELNs).
ELNs are digital versions of paper notebooks, with the added advantage of searchability, secure storage and remote access.
They also are easy to share among team members and collaborators.

It is important to document and share the methodology, analysis and procedures used, as well as data specific information.

(pd-overview-version-comp)=
## Computational Work

In the active phase of a project it is important to keep consistency in your code (read this chapter on {ref}`code quality<rr-code-quality>`), as well as documenting and creating tests for it.

Documenting your code will help others understand your work.
Some tools that can be used to document your code more easily are:
- "Docstring" in R or Python
- "Javadoc" format in Java
- Integrated software development (RStudio, Eclipse, VS Code) facilitate the comment writing process and the generation of documentation.

Creating tests helps to save time and money.
By providing a way to know if your code works, mistakes can be easily addressed by you and others.

To read more about code testing go to the {ref}`Code Testing chapter<rr-testing>`.

(pd-overview-version-vcs)=
## Version Control

Recording all the changes made while researching is a principal part of doing reproducible research.
It helps you and others understand the decisions made and makes the work reproducible - you will have all the information about the steps taken.

If working on a collaborative project, this will also help to keep track of who performed each change.

The added advantage is that everything will be neatly organized, with easy access to the current version of your project and ways to look for changes made in the past.

Some systems for controlling versions are:
- Git
- Mercurial
- Subversion

There is an extensive chapter about {ref}`Version Control System<rr-vcs>` in the Guide for Reproducible Research that can be helpful at this stage.
