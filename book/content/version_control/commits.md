## Commits

### The problem

When working on a project you will make numerous changes to your files as you progress. Sometimes you may need to undo changes, take another look at past versions, or compare versions.
Saving each version individually (version_1.py, version_2.py etc) is messy and quickly becomes impractical.

### The solution

By making commits you can save versions of your code and switch between them/compare them easily without cluttering up your directory.
Commits serve as checkpoints where individual files or an entire project can be safely reverted to when necessary.

### How to do it

When you have made a series of changes and you want to commit them you fist add these changes to your staging area using `git add`.
You can add all your changes using:

```  
git add .
```

or you can add the changes to specific files via:

```  
git add your_file_name
```

If you are ever unsure what files have been added, what files have been changed, what files are untracked etc you can run the following to find out:

```
git status
```

When you're ready you can commit everything in your staging area by running

```
git commit
```

It's that easy.

You can see a log of your previous commits using

```
git log
```

In this log you'll see that each commit is automatically tagged with a unique string of numbers and letters called a SHA which you can use to access and compare them.

#### Retrieving past versions

To cancel your latest commit run
```
git revert HEAD
```

which automatically makes a new commit that undoes those changes. You may want to retrieve a version form weeks or months ago. To do this first use `git log` to find the SHA of the version you want to retrieve. To reset your entire project to this version do

```
git checkout SHA_of_the_version
```

 You may just want the old version of a single file though, and not the previous version of the whole project. To retrieve this use

 ```
 git checkout SHA_of_the_version -- your_file_name
 ```

### Good practice

Commits should be 'atomic'. That is, **they should do one simple thing and they should do it completely**. For example, adding a new function or renaming a variable. If a lot of different changes to your project are all committed together then if something goes wrong it can be hard to unpick what in this set of changes if causing the problem, and undoing the whole commit may throw away valid and useful work along with the bug. That said **you do not necessarily need to do per-file commits**. For example if I add a figure to this chapter here, let's choose something to catch the attention of someone skimming through:

![flipped_taj_mahal](../figures/flipped_taj_mahal.png)

then when I do this two files are changed:

1. The figure file has been added.
2. I have added a reference to this figure in the chapter so it will be displayed.

So two files are affected, but "Add figure to version control chapter" is a single, *atomic* unit of work, so only one commit is necessary.

To aid in making atomic commits it is good practice to **specify the files to be committed**, that is, adding files to the staging area by name (`git add your_file_name`) rather than adding everything (`git add .`). This prevents you from unintentionally bundling different changes together, for example if you have made a change to file A while primarily working on file B you may have forgotten this when you go to commit, and with `git add .` file A would be brought along for the ride.

Finally, **do not commit anything that can be regenerated from other things that were committed unless it is something that would take hours to regenerate**. Generated files just clutter up your repository and may contain features such as timestamps that can cause annoying merge conflicts (see [below](#merge-conflicts)). On a similar note you should not commit configuration files, specifically configuration files that might change from environment to environment. You can instruct Git to ignore certain files by creating a file called `.Gitignore` and including their names in it.
