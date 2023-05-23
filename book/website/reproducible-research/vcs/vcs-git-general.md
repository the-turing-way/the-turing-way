(rr-vcs-git-general)=
# General information about git

Git is a successful version control software (see [wikipedia](https://en.wikipedia.org/wiki/Git) for detailed information).
It was created in 2005 and got rapidely adopted by software developers, especially because it is very fast and scalable. 
Its functions allows for parallel development and maintenance of large projects,like linux development.

(rr-vcs-gitpros)=
## Why everyone is using git

While developed for software, git has been used for many different kind of projects.
Some think the development of git platforms (GitHub, GitLab, Gogs, Gitlea and others), were a critical enabler.
Indeed, these platforms brought project management tools into the git workflow, facilitating community building about project like this book. 
Sometimes, users of these platform do not even know about git. 
Indeed, different workshop and training are teaching the use of the platform, before even mentioning the possibility to `clone` the repository and work with git.

(rr-vcs-git-limitations)=
## git limitation

Git is not magic and it is good to know of its limitation.
Especially, git works best with small text files, but start to be impracticable when too many files are present,  or when the repository becomes too big (1 TB is about the limit of practicability).
As a Git repository stores every version of every file that is added to it, large files that undergo regular modifications can inflate the size of a·project significantly.
In research projects, datasets often contains thousands of filesand/or contain (very) large files.
While one can use of git for non-software application, one needs to plan to use specific worlkflows and/or additional tools to be able to use git tools.
It is particularly problematic because everything will work fine in the beginning and it is very difficult to solve issues when the project is ongoing.
It is therefore important to plan ahead, and try to avoid big repositories.
For instance, one can split the files into different repositories and save binary files outside of git.
There are tools allowing that while keeping git at the core of the version control (git-annex and submodules are possible technologies,  see section {ref}`data version control<rr-vcs-data>`  and {ref}`research projects<rr-vcs-git4research>`)



(rr-vcs-git-usecases)=
## How one uses git

If you ever made modification of files in Github, you have probably used git without even realising it.
When you push the `commit changes` button on a Git platform,git was acting in the background to `add` the changes to the index,
`commit` them with a message, and push it to the repository.

Several software allows to use git without using the command line, locally.
Here is a non-exhaustive list of software one can also use, please refer to their own documentation:

- Rstudio
- Sourcetree
- Gitkracken
- [Visual Studio code](https://en.wikipedia.org/wiki/Visual_Studio_Code)


In many cases, one still needs to use the command lines for complex matters, and we present the main git functions usage in this book (see {ref}`Getting Started with Git<rr-vcs-git>`). 