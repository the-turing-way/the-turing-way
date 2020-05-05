# Version Control

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| -------------|----------|------|
|[Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Helpful |  |
| Recommended skill level | beginner-intermediate | Depends on the tools |

### Summary 

Version control is a systematic approach to record changes made in a file or set of files over time so that you and your collaborators can track their history and review the changes.
Management of changes or revisions to any types of information made in a file or project is called version.

In this chapter, we discuss the best practices that are relevant regardless of tools.
This practice mainly comes from managing changes in the code repositories, but in reality, you can use version control for nearly any type of file on a computer.
For example, when writing a paper with multiple collaborators, version control can help track what changed, who changed them and what updates were made.

Different version control systems can be used through a desktop, web browser-based applications or command-line tools. 
We have all seen a simple file versioning approach where different versions of a file are stored with a different name.
Tools such as Google Drive and Dropbox offer platform to collaboratively update files and share them with others in real-time.
More sophisticated version control system exists within the tools like [Google docs](https://docs.google.com/) or [HackMD](http://hackmd.io/) which allows collaborators to update files simultaneously while storing each version in its version history (we will discuss this in detail).
Advanced version control systems (VCS) such as [Git](https://en.wikipedia.org/wiki/Git), [Mercurial](https://www.mercurial-scm.org/) and [SVN](https://subversion.apache.org/) provide much more powerful tools.

This chapter aims to cover the general principles underpinning all the advanced version control systems and best practice which applies for all such systems.
We discuss many tools and features, however, we encourage readers to use features that are useful for their work and tools they are comfortable with.
Most instructions given in this chapter will also be geared towards Git, which is most commonly used by researchers, and its web-based version, [GitHub](https://github.com/), which facilitate online collaborations.

Later in this chapter, we also discuss version control for data, which is applied to keep track of revisions of large amounts of data, especially when working collaboratively. 
It is useful to know that data can be volatile and versioning them can improve the reproducibility of your scientific analyses.

## How version control is helpful

Researchers deal with a large array of file types containing code, data, figures and documentation that they update but also store past versions of for reference.
This process is often informal and haphazard, where multiple revisions of papers, code, and datasets are saved as duplicate copies with uninformative file names.
For example, one may save different versions of a file by adding v0, v1, v2 and so on to the original file name or python script called my_code.py as my_code_2.py my_code_2a.py, my_code_2b.py and so on to indicate different versions with different updates.
Many of you might be familier with such changes introduced in a manuscript based on new data and feedback provided by different collaborators and reviewers. 
Maintaining those versions and merging changes from version to others can result in an unmanageable proliferation of files.
It is also incredibly error-prone when it is not apparent what different files contain.
This leads to a great deal of time wasted in figuring out what updates were made at what stage, what specific changes correspond to each file and how to reproduce accidentally overwritten files.

Use a formal VCS offers several advantages as listed below.

**Track the history and evolution of a project**

Version control allows you to track the history of your documents, revert your file back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified a file, find where and when an error was introduced, and more. 
Access to the past versions of a project makes it possible to track its entire evolution, making the outputs far more reproducible.

**Accessing all the past versions of a project**

Previous working versions of the codes can always be accessed regardless of how complex or how many changes are made in the current version.
VCS does this in a neat and powerful way, which can save researchers a great deal of time on reproducing their analysis.
Furthermore, if you introduce bugs, overlook errors or lose files, you can recover the last error-free version of the file with the help of VCS.
This feature of VCS gives researchers more freedom to try things out and experiment by eliminating the risk 'breaking' the code entirely.

**Makes collaborations more effective**

VCS can maintain the history of a collaborative document by recording the what changes were made, who proposed them, when in the project was it decided and what were the reasons for those update.
This feature of VCS makes collaboration easier, safer and transparent.

**Developing and combining different versions**

VCS allows different copies of a project to develop independently into different versions (either two versions written by the same person, or versions from many people).
VCS can help compare and combine these multiple versions of the project, tasks which are often time-consuming and confusing when done manually.
