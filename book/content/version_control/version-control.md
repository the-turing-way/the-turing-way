# Version Control

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| -------------|----------|------|
|[Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Helpful |  |
| Recommended skill level | beginner-intermediate | Depends on the tools |

### Summary

Version control is a systematic approach to record changes made in a file or set of files over time so that you and your collaborators can track their history and review the changes.
Management of changes or revisions to any types of information made in a file or project is called versioning.

In this chapter, we discuss the best practices that are relevant regardless of tools.
This practice mainly comes from managing changes in the code repositories, but in reality, you can use version control for nearly any type of file on a computer.
For example, when writing a paper with multiple collaborators, version control can help track what changed, who changed them and what updates were made.

Different version control systems can be used through a program with a graphical user interface, web browser-based applications or command-line tools.
We have all seen a simple file versioning approach where different versions of a file are stored with a different name.
Tools such as Google Drive and Dropbox offer platform to collaboratively update files and share them with others in real-time.
More sophisticated version control system exists within tools like [Google docs](https://docs.google.com/) or [HackMD](http://hackmd.io/) which allow collaborators to update files simultaneously while storing each version in its version history (we will discuss this in detail).
Advanced version control systems (VCS) such as [Git](https://en.wikipedia.org/wiki/Git), [Mercurial](https://www.mercurial-scm.org/) and [SVN](https://subversion.apache.org/) provide much more powerful tools.

This chapter aims to cover the general principles underpinning all the advanced version control systems and best practice which applies for all such systems.
We discuss many tools and features, however, we encourage readers to use features that are useful for their work and tools they are comfortable with.
Most instructions given in this chapter will also be geared towards Git, which is most commonly used by researchers, and its web-based version, [GitHub](https://github.com/), which facilitate online collaborations.

Later in this chapter, we also discuss version control for data, which is applied to keep track of revisions of large amounts of data, especially when working collaboratively.
It is useful to know that data can be volatile and versioning them can improve the reproducibility of your scientific analyses.
