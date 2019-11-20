## Merging

### The problem

Once you've finished up some work on a branch you need to integrate it to your main project (or any other branch).

### The solution

Merge the branch with your work on into your target branch.
You can also use merging to combine work that other people have done with your own and vice versa.

### How to do it

To merge some branch, branch_A, into another branch, branch_B, switch to branch_A via `git checkout branch_A` and merge it into branch_B by:

```
git merge branch_B
```

Merging will not be possible if there are changes in either your working directory or staging area that could be written over by the files that you are merging in.
If this happens, there are no merge conflicts in individual files.
You need to commit or stash the files it lists and then try again.
The error messages are as follows:

```
error: Entry 'your_file_name' not uptodate. Cannot merge. (Changes in working directory)
```

or

```
error: Entry 'your_file_name' would be overwritten by merge. Cannot merge. (Changes in staging area)
```

### Good practice

First and foremost your **master branch should always be stable**, only merge work that is finished and tested into it.
If your project is collaborative then it is a good idea to **merge changes that others make into you own work frequently**.
If you do not it is very easy for merge conflicts to arise (next section).
Similarly, share your own changes with your collaborators often.
