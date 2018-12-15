# Version Control

## General thoughts

*Thoughts here and throughout will be in italics*

*Might be worth having a summarising table with commands and what they do.*

*Should at least mention version control software other than git.*

*For [creative commons](https://tldrlegal.com/license/creative-commons-attribution-4.0-international-(cc-by-4) you can do whatever but you must give credit to the original author of the work, including a URI or hyperlink to the work, this Public license and a copyright notice.*

------

## *Structure*

*Things that have already been done are ~~crossed out~~

*I'm thinking we order subsections as*
*1. State the problem e.g. can't retrieve past versions (commits), don't have anywhere safe to do work (branches) etc.*
*2. Description of the version control facility that solves that problem.*
*3. Explanation of how to actually do it.*
*4. Best practice for actually doing it.*

*I think the best practise sections should have a different background colour/be in boxes so someone who already knows about version control but wants to know more about best practise can find it easily. Also given the thrust of this project is good practise I think really highlighting those sections is meritted.*

*Want to make sure people understand VC fist before we explain collaborative VC*

- *Summary*
  - *Worry about this last*
- *~~What is version control~~*
  - *~~Should keep this high level, include the diagram, go over the very basics of branches and merging~~*
- *Why you should use version control*
  - *First paragraph, core benefits focusing on how it helps the USER, convince people this is something they should invest time in to help thier research in the long term. Keeps versions safe and recoverable, keeps things tidy*
  - *Say it enables collaboration*
  - *How it benefits science, reproducibility etc. Maybe not that relevant here, maybe more open source's thing?*
- *~~Prerequisites / recommended skill level~~*
- *Definitions/glossary*
- *How to use version control for your own project and how to use it well*
  - *Intro*
    - *Say in terms of how to do it we're going to give the actual commands to do all this in git because widely used, but the info on good practise, i.e. how to do it well, is still relevant even if you're using other VC software like mercurial.*
    - *~~Set up a repo, git init. Don't talk about putting it online yet.~~*
  - *Commits*
    - *Problem = want to access past versions*
    - *Say how to add files, say how git status tells you what's been added. Git diff to see the difference. How to make a commit and how to get files/whole project back to past commit. Say git log gives log of past commits. Git diff to see what changed between two commits.*
    - *Best practice for committing, e.g. keep bitesized, don't do per-file commits, whitespace changes together with code changes, or code drops*
  - *Commit messages*
    - *Problem = when you've been working on a project for a while different versions stack up, hard to remember what does what. Having something is no good if you can't find/understand it, and figuring it out can take valuable time.*
    - *Say what commit messages are.*
    - *Explain that when you commit (regardless(???) of what VC software you're using) you can give a commit message, say show up in git log.*
    - *How to give a commit message.*
    - *Best practise for commit messages. e.g. make them meaningful, cover why the change is necessary, how it addresses the issue, and what effects the change has. Also don't describe the code, describe the intent and the approach. And keep the log in a present tense.*
  - *Branches*
    - *Problem = if you're working on something it could screw up your working version*
    - *Describe in detail what branches are and how they fix the problem, mention can do branches from branches*
    - *Say how to make branches and switch between them. Git status to find ou which branch you're on.*
    - *Best practise for branches, i.e. make changes on them, keep master clean., try to limit one feature being added per branch, not a whole mess of things which may be completed at different times.*
  - *Merging*
    - *Problem = once you've got your changes working you want to combine them into your main thing*
    - *VC lets you merge changes in*
    - *How to merge*
    - *Best practice for merging, e.g. don't put half finished stuff in.*
  - *Merge conflicts*
    - *Problem = May have made changes to master (or whatever sub-branch you're merging to (overcomplicating?)) since you started the branch. When you go to merge may be incompatible.*
    - *VC will highlight those changes and let you sort them out*  
    - *How to resolve merge conflicts*
    - *Best practise for preventing and dealing with merge conflicts, e.g. merge from upstream often, keep branches and commits focused on limited changes, etc.*
- *Using version control to collaborate.*
  - *Introduction*
    - *Science is becoming increasingly collaborative. If you have a lot of people working on the same codebase all changing it things can get messy and tangled very fast. Also how a lot of major open source projects are run by this.*  
    - *Say should understand how to use it for your own project before trying to understand how to do it with other people, if reading this section need to read (or already understand) previous one.*
  - *Divide into if it's your project people are collaborating on, and collaborating on someone else's?*
  - *I could use some help from those more familiar with gitHUB and using git to collaborate for this section.*
- *Checklist*
- *What to learn next?*
- *Recommended reading*
- *Other useful links*
- *What is version control*

------

## Summary


## How this is helpful


## Prerequisites / recommended skill level
No prerequisites. Recommended skill level: beginner - intermediate. Version control has a great deal of useful features, but total mastery is not necessary to achieve a great deal with it. Even a beginner utilising a few of the simplest features well can save themselves a great deal of time and drastically improve the reproducibility of their work. Naturally, we encourage readers to make use of the entire chapter, but readers should not be discouraged from using some tools they feel comfortable with if they are not comfortable with *all* the tools available.

### Definitions/glossary



## What is version control?

What is “version control”, and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. It is typically applied to managing changes in code, though in reality you can do this with nearly any type of file on a computer.

The typical procedure for using version control is as follows:

1. Have some files
2. Do some work- you will now have made changes. Maybe you've modified one or more files, added new ones, or deleted old ones, it doesn't matter.
3. Make a commit. This means you take a snapshot of your work at this point in time.

Keep doing work and making more and more commits. You can kind of think of commits as checkpoints. If you ever need to go back to any past checkpoint to get a file as it was then, or just return your entire project to a past state you can. An illustration of this is shown in the figure below.  

*Should definitely have a diagram, couldn't find one I liked so I made these. We could replace them with better ones later*

![master_branch](figures/master_branch.png)

Every time you make a commit you can tag it with a commit message explaining what this snapshot of your project is doing. This makes it very easy to find what you're looking for when you need to go back to a past version.

So you have your project and you want to add new or something or try something out. With version control you can make a branch to do this work on. Any work you do on your branch won't be present on your main project (referred to as your master branch) so it remains nice and safe and you can continue to work on it. Once you're happy with your New Thing you can 'merge' your branch back into your master copy.

![one_branch](figures/one_branch.png)

You can have more than one branch off of your master copy, and if one of your branches ends up not working you can either abandon it or delete it without the master branch of your project ever being impacted.

![two_branches](figures/two_branches.png)

If you want you can even have branches off of branches (and branches off of those branches and so on).

![sub_branch](figures/two_branches.png)

No matter how many branches you have you can access past commits you made on any of them.

## Why would you use version control?

People working on data science may have a large array of files (code, data, figures, notes) that they update
but want to keep every version. This process is often informal and haphazard, where multiple revisions of papers, code, and datasets are saved as duplicate copies with uninformative file names (e.g. my_code.py my_code_2.py my_code_2a.py, my_code_2b.py). As authors receive new data and feedback from peers and collaborators, maintaining those versions and merging changes can result in an unmanageable proliferation of files. It is also incredibly error prone. It is easy to forget what different files contain, or to copy over files you don’t mean to. This leads to a great deal of time wasted on figuring out what files contain and reproducing accidently overwritten files.

One solution to these problems would be to use a formal Version Control System (VCS), which have long been used in the software industry to manage code.
Version control allows you to do this and to revert files you select back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more. Using a version control system also generally means that if you screw things up or lose files, you can easily recover. In addition, you get all this for very little overhead. Many people have felt the horror of loosing days if not weeks of work when changes to a code break it irretrievably and with this lies the key reasons to use version control **it removes risk and saves time.**

Further, commit messages help you understand why in the past you made certain changes, why you did a certain analysis in the way you did it.
You yourself understand what the saved file does, even weeks or months later when you've long since forgotten what changes you made.
Commit messages also help others working on the same project to more easily understand what you did. This is helpful should you want to share your analysis (not only your data), and/or make it auditable--more generally, reproducible, which is good scientific practice.

*Should say somewhere also keeps your working directory neat, don't have multiple versions of the same file/ blocks of commented out code "Keeping all that code around makes it harder for you when you revisit the code. "*








There are numerous tools for versioning, and the best know one is git and its web-based version, Github.


----


From [here](https://guide.esciencecenter.nl/best_practices/version_control.html). **Creative Commons Attribution 4.0 International License**

- **Reproducibility** By using version control, you never lose previous versions of the software. This also gives you a log of changes and allows you to understand what happened.
- **Backup** Version control is usually pushed to an external a shared server, which immediately provides a backup.
- **Easier to collaborate** Version control makes it easier for different people to work on the same code simultaneously, while everyone still has a well defined version of the software (in contrast to a google-docs or shared file system type of system). Moreover, version control hosting websites such as Github provide way to communicate in a more structed way, such as in code reviews, about commits and about issues.
- **Integration** Version control software and host makes it more easy to integrate with other software that support modern software development, such as testing (continuous integration ,automatically run tests, build documentation, check code style, integration with bug-tracker, code review infrastructure, comment on code).

--------

From [here](https://homes.cs.washington.edu/~mernst/advice/version-control.html) **No license reached out 13/12/18**

A version control system serves the following purposes, among others.

- Version control enables multiple people to simultaneously work on a single project. Each person edits his or her own copy of the files and chooses when to share those changes with the rest of the team. Thus, temporary or partial edits by one person do not interfere with another person's work.
- Version control gives access to historical versions of your project. This is insurance against computer crashes, data lossage, or code being broken in the course of future changes. If you make a mistake, you can roll back to a previous version. You can reproduce and understand a bug report on a past version of your software. You can also undo specific edits without losing all the work that was done in the meanwhile. For any part of a file, you can determine when, why, and by whom it was ever edited.

### Getting Started

This is important to know, but it isn't that exciting. To start using version control for your project you just go into the directory that contains all of your files (subdirectories will be included) and run

```
git init
```

in the terminal to create the git repository (often called "repo" for short). This just needs to be done once per project.

Just think of the repository as a place where the history is being stored. A lot happens behind the scenes but who cares. (Maybe you care, but only after you really know how to use it.)

Next add and commit your files to the repository by running

```
git add .
git commit
```

We'll talk in more detail about these commands later, but for now just know if you run them then congratulations, you have finished setting up you repository!

### Commits


From [here](https://githowto.com/undoing_committed_changes). **creative commons Attribution-NonCommercial-ShareAlike 4.0 International**

 Commits serve as checkpoints where individual files or an entire project can be safely reverted to when necessary.

To cancel the commit, we need to create a commit that deletes the changes saved by unwanted commit.

RUN:
```
git revert HEAD
```

-------

From [here](https://homes.cs.washington.edu/~mernst/advice/version-control.html) **No license, reached out 13/12/18**

#### Good practise for commits

- **Each commit should have a single purpose and should completely implement that purpose.** This makes it easier to locate the changes related to some particular feature or bug fix, to see them all in one place, to undo them, to determine the changes that are responsible for buggy behavior, etc. The utility of the version control history is compromised if one commit contains code that serves multiple purposes, or if code for a particular purpose is spread across multiple different commits.
- **Avoid indiscriminate commits** As a rule, do not commit without supplying specific files to commit. If you supply no file names, then every change will be committed. You may have changes you did not intend to make permanent (such as temporary debugging changes).
- **Don't commit generated files** Version control is intended for files that people edit. Generated files should not be committed to version control, as a rule, you should only commit the source files from which the files are generated.
Generated files are not necessary in version control; each user can re-generate them from the source files.
Further, generated files are prone to conflicts. They may contain a timestamp or in some other way depend on the system configuration. It is a waste of human time to resolve such uninteresting conflicts.
Generated files can bloat the version control history (the size of the database that is stored in the repository). A small change to a source file may result in a rather different generated file. Eventually, this affects performance of the version control system.


### Commit messages

From [here](https://guide.esciencecenter.nl/best_practices/version_control.html). **Creative Commons Attribution 4.0 International License**

Commit messages are the way for other developers to understand changes in the codebase. In case of using GitHub flow model, commit messages can be very short but pull request comments should explain all the changes. It is very important to explain the why behind implementation choices.

-----

By [Thom Holwerda](http://www.osnews.com/story/19266/WTFs_m). **Says anyone can do whatever, attribution nice but not compulsory**

*Maybe include this somewhere else but have it somewhere*

![wtf_per_min](figures/wtf_per_min.jpg)

## Branches

*Think we should go over deleting branches before we go over merging. Deleting's quicker and easier to explain.*

From [here](https://opensource.com/article/18/5/git-branching) **Creative Commons license**
The main reasons for having branches are:

- If you are creating a new feature for your project, there's a reasonable chance that adding it could break your working code. This would be very bad for active users of your project, even if the only active user is you. It's better to start with a prototype, which you would want to design roughly in a different branch and see how it works, before you decide whether to add the feature to the master branch.
- Another, probably more important, reason is version control systems are regularly used for collaboration. If everyone starts programming on top of the master branch, it will cause a lot of confusion. Some people may write faulty/buggy code or simply the kind of code/feature others may not want in the project. Using branches allows you to contributions to be verified and reviewed before being added to the main project.

-------

From [here](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches) **GNU GENERAL PUBLIC LICENSE Version 3**

Create the branch on your local machine and switch in this branch :
```
$ git checkout -b [name_of_your_new_branch]
```

Change working branch :
```
$ git checkout [name_of_your_new_branch]
```

Push the branch on github :
```
$ git push origin [name_of_your_new_branch]
```

You can see all branches created by using :
```
$ git branch
```

Add a new remote for your branch :
```
$ git remote add [name_of_your_remote] [name_of_your_new_branch]
```

Push changes from your commit into your branch :
```
$ git push [name_of_your_new_remote] [url]
```

Update your branch when the original branch from official repository has been updated :
```
$ git fetch [name_of_your_remote]
```

Delete a branch on your local filesystem :
```
$ git branch -d [name_of_your_new_branch]
```

To force the deletion of local branch on your filesystem :
```
$ git branch -D [name_of_your_new_branch]
```

Delete the branch on github :
```
$ git push origin :[name_of_your_new_branch]
```

-------









## Merging

From [here](https://githowto.com/merging). **creative commons Attribution-NonCommercial-ShareAlike 4.0 International**

Merging brings changes from two branches into one. Let us go back to the style branch and merge it with master.

RUN:
```
git checkout style
git merge master
git hist --all
```

RESULT:
```
$ git checkout style
Switched to branch 'style'
$ git merge master
Merge made by recursive.
 README |    1 +
 1 files changed, 1 insertions(+), 0 deletions(-)
 create mode 100644 README
$ git hist --all
*   5813a3f 2011-03-09 | Merge branch 'master' into style (HEAD, style) [Alexander Shvets]
|\  
| * 6c0f848 2011-03-09 | Added README (master) [Alexander Shvets]
* | 07a2a46 2011-03-09 | Updated index.html [Alexander Shvets]
* | 649d26c 2011-03-09 | Hello uses style.css [Alexander Shvets]
* | 1f3cbd2 2011-03-09 | Added css stylesheet [Alexander Shvets]
|/  
* 8029c07 2011-03-09 | Added index.html. [Alexander Shvets]
* 567948a 2011-03-09 | Moved hello.html to lib [Alexander Shvets]
* 6a78635 2011-03-09 | Add an author/email comment [Alexander Shvets]
* fa3c141 2011-03-09 | Added HTML header (v1) [Alexander Shvets]
* 8c32287 2011-03-09 | Added standard HTML page tags (v1-beta) [Alexander Shvets]
* 43628f7 2011-03-09 | Added h1 tag [Alexander Shvets]
* 911e8c9 2011-03-09 | First Commit [Alexander Shvets]
```

------

From [here](https://homes.cs.washington.edu/~mernst/advice/version-control.html) **No license, reached out 13/12/18**

Incorporate others' changes frequently
Work with the most up-to-date version of the files as possible.

When two people make conflicting edits simultaneously, then manual intervention is required to resolve the conflict. But if someone else has already completed a change before you even start to edit, it is a huge waste of time to create, then manually resolve, conflicts. You would have avoided the conflicts if your working copy had already contained the other person's changes before you started to edit.

Share your changes frequently
Once you have committed the changes for a complete, logical unit of work, you should share those changes with your colleagues as soon as possible. So long as your changes do not destabilize the system, do not hold the changes locally while you make unrelated changes. The reason is the same as the reason for incorporating others' changes frequently.

Coordinate with your co-workers to avoid conflicts as best as you can.


### Merge conflicts

From [here](https://homes.cs.washington.edu/~mernst/advice/version-control.html) **No license, reached out 13/12/18**

A version control system lets multiple users simultaneously edit their own copies of a project. Usually, the version control system is able to merge simultaneous changes by two different users: for each line, the final version is the original version if neither user edited it, or is the edited version if one of the users edited it. A conflict occurs when two different users make simultaneous, different changes to the same line of a file. In this case, the version control system cannot automatically decide which of the two edits to use (or a combination of them, or neither!). Manual intervention is required to resolve the conflict.

"Simultaneous" changes do not necessarily happen at the exact same moment of time. Change 1 and Change 2 are considered simultaneous if:

- User A makes Change 1 before User A does an update that brings Change 2 into User A's working copy, and
- User B makes Change 2 before User B does an update that brings Change 1 into User B's working copy.


------

From [here](https://githowto.com/resolving_conflicts). **creative commons Attribution-NonCommercial-ShareAlike 4.0 International**

RUN:

```
git checkout style
git merge master
```

RESULT:
```
$ git checkout style
Switched to branch 'style'
$ git merge master
Auto-merging lib/hello.html
CONFLICT (content): Merge conflict in lib/hello.html
Automatic merge failed; fix conflicts and then commit the result.
```
If you open the lib/hello.html you will see:

FILE: LIB/HELLO.HTML
```
<!-- Author: Alexander Shvets (alex@githowto.com) -->
<html>
  <head>
<<<<<<< HEAD
    <link type="text/css" rel="stylesheet" media="all" href="style.css" />
=======
    <!-- no style -->
>>>>>>> master
  </head>
  <body>
    <h1>Hello,World! Life is great!</h1>
  </body>
</html>
```
The first section is the version of the current branch (style) head. The second section is the version of master branch.

02 Resolution of the conflict

You need to resolve the conflict manually. Make changes to lib/hello.html to achieve the following result.

FILE: LIB/HELLO.HTML
```
<!-- Author: Alexander Shvets (alex@githowto.com) -->
<html>
  <head>
    <link type="text/css" rel="stylesheet" media="all" href="style.css" />
  </head>
  <body>
    <h1>Hello, World! Life is great!</h1>
  </body>
</html>
```
03 Make a commit of conflict resolution

RUN:
```
git add lib/hello.html
git commit -m "Merged master fixed conflict."
```

RESULT:
```
$ git add lib/hello.html
$ git commit -m "Merged master fixed conflict."
Recorded resolution for 'lib/hello.html'.
[style 645c4e6] Merged master fixed conflict.
```

------

From [here](http://genomewiki.ucsc.edu/index.php/Resolving_merge_conflicts_in_Git) **["You are granted a limited license to copy anything from this site"](http://genomewiki.ucsc.edu/index.php/Genomewiki:General_disclaimer)**

#### Two ways git merge/git pull can fail
There are 2 ways in which git merge (or a git pull, which is a git fetch and then a git merge) can fail:

1.  Git can fail to start the merge
This occurs because git knows there are changes in either your working directory or staging area that could be written over by the files that you are merging in. If this happens, there are no merge conflicts in individual files. You need to modify or stash the files it lists and then try to do a git pull again. The error messages are as follows:

```
error: Entry '<fileName>' not uptodate. Cannot merge. (Changes in working directory)
```
or
```
error: Entry '<fileName>' would be overwritten by merge. Cannot merge. (Changes in staging area)
```

2. Git can fail during the merge
This occurs because you have committed changes that are in conflict with someone else's committed changes. Git will do its best to merge the files and will leave things for you to resolve manually in the files it lists. The error message is as follows:

```
CONFLICT (content): Merge conflict in <fileName>
Automatic merge failed; fix conflicts and then commit the result.
```

#### Common questions for when git fails during the merge

How do I know which files have conflicts in them?
If your merge failed to even start, there will be no conflicts in files. If git finds conflicts during the merge, it will list all files that have conflicts after the error message. You can also check on which files have merge conflicts by doing a 'git status'.

Example:

```
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)

  	modified:   <Some file>

   Changed but not updated:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)

  	unmerged:   <file>

```
"Changes to be committed": All committed changes to files that are not affected by the conflict are staged.

"Changed but not updated ... unmerged": All files that have conflicts that must be resolved before repository will be back to working order.

How do I find conflicts within the file itself?
Conflicts are marked in a file with clear line breaks:

```
 <<<<<<< HEAD:mergetest
 This is my third line
 =======
 This is a fourth line I am adding
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```
'<<<<<<<': Indicates the start of the lines that had a merge conflict. The first set of lines are the lines from the file that you were trying to merge the changes into.

'=======': Indicates the break point used for comparison. Breaks up changes that user has committed (above) to changes coming from merge (below) to visually see the differences.

'>>>>>>>': Indicates the end of the lines that had a merge conflict.

How do I resolve a merge conflict in a file?
You resolve a conflict by editing the file to manually merge the parts of the file that git had trouble merging. This may mean discarding either your changes or someone else's or doing a mix of the two. You will also need to delete the '<<<<<<<', '=======', and '>>>>>>>' in the file.

What do I do after I've resolved conflicts in all affected files?
git add the file(s), git commit and git push (Push only for branches tracked.)

(Note added by Chin - need to commit everything, not just the resolved conflict file.)

#### Tools to help you resolve both types of merge conflicts
The following git tools below can help you resolve both simple and more complicated git merges.

General tools
```
git diff
```

git diff: a command that helps find differences between states of a repository/files. Useful in predicting and preventing merge conflicts.

git diff origin/master <fileName>: Find the differences between the current index (HEAD) of fileName and what is in the central repository (origin/msater)

```
diff --git a/mergetest b/mergetest
index 9be56b9..0aeffac 100644
--- a/mergetest
+++ b/mergetest
@@ -1,3 +1,4 @@
 hello
+I am also editing this line
 This is a test
-This is my third line
+This is a fourth line I am adding
```
Changes coming from origin/master are marked with +, while changes that are in your local repository (HEAD) are marked with -. This syntax does not notify which lines are added are deleted but just which lines originate in which state of the file.

git diff FETCH_HEAD <fileName>: Will provide the same output as above except is limited to the index of the last fetch that the user did. This may not be latest revision in the central repository.

```
git status
```
git status: a command provides an overview of all files that have been modified and are in conflict at the time of the merge.

Example:
```
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

   	modified:   <Some file>

    Changed but not updated:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

   	unmerged:   <file>

```
"Changes to be committed": All changes to files that are not affected by the conflict are staged.
"Changed but not updated ... unmerged": All files that have conflicts that must be resolved before repository will be back to working order.
Tools specifically for when git refuses to start merge

```
git stash
```
IMPORTANT: Do not use git stash if git went through with the merge and there were merge conflicts! Only use git stash if git refused to merge because it foresees there being conflicts.

git stash: stashes away any changes in your staging area and working directory. This command is useful in saving all changes not ready to be committed and the user wants to have an updated repository.

git stash save "<Save Message>": Save changes to files in working directory and staging area that git is aware of

```
 git stash save "Saved changes for stash example"
 Saved working directory and index state "On master: Saved changes for stash example"
 HEAD is now at 4e2b407 Added second file for example.
```
git stash pop: Removes the most recent stash or any stash specified and applies changes as a merge. If merge fails the stash is not removed from the list and must be removed manually.

```
git checkout
```
git checkout <fileName>: Can be used to trash changes in the working directory so as to allow a git pull.

```
git reset --mixed
```
git reset --mixed: Can be used to unstage files so as to allow a git pull.

#### Tools specifically for when git conflicts arise during a merge
```
git reset
```
git reset --hard: reset repository in order to back out of merge conflict situation. git reset, particularly with the --hard option can be used to back out of merge conflict (click here for more information).

IMPORTANT: Do not use any other options other than --hard for reset when resolving a situation where git failed during the merge, as they will leave conflict line markers in file and you can end up committing files with conflict markers still present.

#### Scenarios

Git refuses to start a merge/pull

Error Messages:

```
error: Entry '<fileName>' not uptodate. Cannot merge. (Changes in working directory)
error: Entry '<fileName>' would be overwritten by merge. Cannot merge. (Changes staged, but not commited)
```
Steps toward Resolution:

- git stash save "<Message that describes what is being Saved>" (Stashes away any changes in your staging area and working directory in a separate index.) OR git checkout <file> (throws out your changes so that you can do a merge)
- git status (Verify all changes are staged)
- git pull or git merge (Bring in changes from central repository or another branch)
- Only if did a 'git stash' in step 1: git stash pop (Will repopulate your changes into your working directory, may have to resolve merge conflicts)

#### Git is unable to resolve a merge/pull

Error Message:

```
CONFLICT (content): Merge conflict in <fileName>
Automatic merge failed; fix conflicts and then commit the result.
```

Steps toward Resolution:

- git status (Shows all files that are in conflict as unmerged changed in working directory.)
- Resolve merge conflicts
- git add <files>
- git commit -m "<Informative commit message>"

#### A GitHub test repository to experiment with conflicts
You can experiment with resolving a git conflict with this repository: https://github.com/brianleetest/testGit/blob/master/README.md

You will need a GitHub account and be added as a collaborator to push your changes.
Create two separate directories, gitClone and gitCloneLeader in two different terminals and locations. The leader can be the first to push changes (requires being a collaborator).
Do the first "Group Member" steps up until WAIT in the gitClone directory.
Then do all of the "Group Leader" steps in the gitCloneLeader directory (push required to cause conflict).
Continue the "Group Member" steps (first git pull since cloning the repository and editing the file).

## Forks

## Git

*I think this section should go over the command line nitty-gritty. The explanation of what branches are etc should all be done before that because that's common to all VC, this section is git specific, and command line specific*


*Very detailed how to [here](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter).* **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.**


## Github

*I think this section should go over how to do this in the browser/gui nitty-gritty. Again, the explanation of what branches are etc should all be done before.*

## What to learn next?

## Recommended reading

## Other useful links

### Materials used in this chapter

[This](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Controls) **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License**
[This](https://link.springer.com/article/10.1186/1751-0473-8-7). **Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0)** *Other useful stuff in this paper, could use their into as part of the book's intro*
[This](http://crlionline.net/node/198). **Permission to use given by the author (Peter Reimann) 54/12/18**
[This](https://tonysyu.github.io/source-control-for-scientists-and-soloists.html#.XA6Q3mj7RPY). **Permission given by the author (Tony Yu) 15/12/18**
