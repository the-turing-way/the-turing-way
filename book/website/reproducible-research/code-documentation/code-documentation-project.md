(rr-project-documentation)=
## Project documentation

Project documentation describes aspects of a software project that are important for managing and tracking the development of software. And also aspects such as licensing and citations. 

Project documentation should include the following:

### README

A readme file is 
*"a text file that introduces and explains a project. It contains information that is commonly required to understand what the project is about."* 
The [make a readme](https://www.makeareadme.com/) website provides guidance on how to write a good readme file.

### Contributing Guidelines

A contributing file describes how people can contribute to the development of software. 
Contributing guidelines are very important in open-source software projects. 
The [collaboration chapter](https://the-turing-way.netlify.app/collaboration/collaboration) provides information on the many aspects levant for contributing guidelines, 
and this is a [template for a contributing file](https://github.com/jessesquires/.github/blob/main/CONTRIBUTING.md) used in GitHub.

### Roadmap

A roadmap provides an overview of the current and future development plans. 
Letting potential users know about the development plan is essential because they can be aware of when to expect new features,
what functionality is expected to be removed, 
and how changes are being made to the software actively. 
For developers, a roadmap is essential because they can quickly identify parts of the software they can work on without duplicating efforts and what tasks are a priority.

### Changelog

A changelog is a plain text file that contains a record of what *notable* changes are made between versions of software.  
The [keep a changelog](https://keepachangelog.com/en/1.1.0/) website provides a detailed explanation of what a change log is, 
and this [changelog template](https://gist.github.com/juampynr/4c18214a8eb554084e21d6e288a18a2c) is a good starting point for 
creating change log files. 

### Licensing

Choosing or writing a license for software is of the utmost importance. 
It lets users know under what legal conditions they are allowed to use the software. 
The section on [licensing](https://the-turing-way.netlify.app/reproducible-research/licensing) provides excellent detail on open-source licensing.

### Code of Conduct

When collaboration is an important aspect of a software project,
defining a *code of conduct* is necessary to create and maintain a collaboration environment that promotes participation and fosters the exchage of ideas, 
while fostering respect among developers. 

The [contributor's covernant](https://www.contributor-covenant.org/) describes a code of conduct for open source software, 
and this [template](https://github.com/jessesquires/.github/blob/main/CODE_OF_CONDUCT.md) can be used as is or be adapted for a software project.

### Software Citation

Let people know how to cite your software using a `CITATION.cff` file. The citation file contains metadata to make software citable. The tool [CFFINIT](https://citation-file-format.github.io/cff-initializer-javascript/#/) helps you to create a citation file that you can include as part of the project documentation. 
The section on [software citation](https://the-turing-way.netlify.app/communication/citable/citable-cff.html?highlight=recognition) provides greater detail on why and how to edit `cff` files. 
