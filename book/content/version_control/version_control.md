# Version Control

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| -------------|----------|------|
|[Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Helpful | It is possible to use version control through desktop and web browser based tools. These are discussed towards the end of this chapter, but the general principles and best practice discussed in the preceding sections are relevant regardless of whether the command line or a GUI is used. |

Recommended skill level: beginner - intermediate. Version control has a great deal of useful features, but total mastery is not necessary to achieve a great deal with it.
Even a beginner utilising a few of the simplest features well can save themselves a great deal of time and drastically improve the reproducibility of their work.
Naturally, we encourage readers to make use of the entire chapter, but readers should not be discouraged from using some tools they feel comfortable with if they are not comfortable with *all* the tools available.

## Summary

Version control keeps track of different versions of a project and allows past versions to be accessed easily.
It also allows different versions of a project to be merged with minimal input from the user.  
Version control is often associated with writing code, but it can also be used with writing projects.
For example, if you are writing a paper with collaborators then version control is really important in helping you to see who has changed what.  
Version control is used to some extent within many different programs, including ones you are likely to already be familiar with such as Word or Wordpress.
There are numerous tools available for version control such as [Mercurial](https://www.mercurial-scm.org/) and [SVN](https://subversion.apache.org/).  
The best know one is Git (and its web-based version, [GitHub](https://github.com/), which aids collaboration between researchers) which the instructions given in this chapter will be geared towards.
There are a large number of detailed tutorials available online discussing the features and mechanics of how to use such systems (see the "[Further reading](#further-reading)" section at the end of the chapter).
This chapter aims to cover the general principles underpinning all version control systems, and best practice which applies for using all such systems.

## How version control is helpful

Researchers often have a large array of files (code, data, figures, notes) that they update but that they want to keep past versions of for reference.
This process is often informal and haphazard, where multiple revisions of papers, code, and datasets are saved as duplicate copies with uninformative file names (for example, my_code.py my_code_2.py my_code_2a.py, my_code_2b.py).
As authors receive new data and feedback from peers and collaborators, maintaining those versions and merging changes can result in an unmanageable proliferation of files.
It is also incredibly error prone.
It is easy to forget what different files contain, or to copy over files you do not mean to.
This leads to a great deal of time wasted on figuring out what files contain and reproducing accidently overwritten files.

One solution to these problems would be to use a formal Version Control System (VCS).
A formal version is often a better solution than the lightweight version control that is often provided by text editing software packages.
These systems have long been used in the software industry to manage code.
Version control allows you to revert files you select back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified a file, find where and when a bug was introduced, and more. Using a version control system also generally means that if you screw things up or lose files, you can easily recover.
In addition, you get all of this for very little overhead.
Many people have felt the horror of losing days if not weeks of work when changes to a code break it irretrievably and can not be unpicked, and with this lies the key reasons to use version control: **it removes risk and saves time.**

Keeping past versions of a project stored and accessible makes it possible to track its entire evolution, making the outputs far more reproducible.
Version control software does this in a neat and powerful way, and it often saves researchers a great deal of time on reproducing lost code or analysis.
Further, version control gives researchers more freedom to try things out and experiment.
It does this by eliminating the risk of subsequent changes irrevocably 'breaking' the code as previous working versions will remain accessible regardless of how complex or how many changes are made.

Another benefit of version control is that it makes collaboration easier, safer, and allows what changes have been made, when, why, and by who to be tracked.
It does this by allowing different versions of a project (either two versions written by the same person, or versions from many people) to be worked on separately.
It also has facilities to automatically compare and combine versions of a project, tasks which are often both fiddly and time-consuming when done manually.

