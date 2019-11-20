## Getting Started

This is important to know, but it is not that exciting.
Instructions for installing Git on linux, windows and mac machines are available [here](https://Git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Once installation is complete, to start using version control for your project you just go into the directory that contains all of your files (subdirectories will be included) and run:

```
git init
```

in the terminal to create the Git repository (often called "repo" for short).
This only needs to be done once per project.

Think of the repository as a place where the history is being stored.
Each file in your working directory can be in one of two states: tracked or untracked by your repository.
In short, tracked files are files that Git knows about.
Untracked files are everything else — any files in your working directory that were not in your last snapshot.
When you first initialise a repository with `git init` all of your files will be untracked because your repository it does not *have* a previous snapshot yet, so it doesn't know about any of your files.
Therefore your next step is to add your files to the repository using:

```
git add .
```

This puts your changes into what is called the "staging area".
When you next commit any changes stored in your staging area will be recorded in your repository.

![change_stage_repo](../figures/change_stage_repo.png)

The full stop after `git add` above adds all changes to your staging area. So now all your files are staged commit them using:

```
git commit
```

We will talk in more detail about these commands [later](#adding), but for now just know if you run them then congratulations, you have finished setting up you repository!
