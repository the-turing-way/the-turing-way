# Version Control

## General thoughts

*Thoughts here and throughout will be in italics*

*Maybe make the principle why you should use this as "Version control removes risk." It's a neat four-word takeaway. Follow up, maybe "Using version control keeps every version of your project stored and safe, so if future changes break you code irretrievably, or something is deleted that you later need it's the matter of seconds to retrieve your past versions. It also keeps your working directory neat..."*

*Should emphasise that version control is also useful when working alone, not just in collaborations*

*Talk about how to get past versions.*

*How should I combine high level explanation of what version control CAN do vs step by step of HOW to do it in git and github? Meshing it together seems like I'm trying to explain too many things at once, and git isn't the only version control software out there. However completly separating the
all the why and all the how means a person who's reading about version control can't follow easily, they'd have to scroll a lot from what is a commit to how do you make one. Hmmm.*    

*Need to mention git status and git log somewhere.*

*Should at least mention version control software other than git.*

------

## *Structure*

- *What is version control*
  - *Should keep this high level, include the diagram, go over the very basics of branches and merging
- *Why you should use version control*
  - *First paragraph, core benefits focusing on how it helps the USER, convince people this is something they should invest time in to help thier research in the long term. Keeps versions safe and recoverable, keeps things tidy, enables collaboration
  - *How it benefits science, reproducibility etc. Maybe not that relevant here, maybe more open source's thing?*
- *How to use version control for your own project and how to use it well*
  - *Say this is split into how to do it and how to do it well. In terms of how to do it we're going to give the actual commands to do all this in git because widely used, but the info on good practise, i.e. how to do it well, is still relevant even if you're using other VC software like mercurial.
  - Set up a repo, git init. Don't talk about putting it online yet.
  - Say how to make a commit
    - Best practice for committing, e.g. keep bitesized
    - Best practise for commit messages. e.g. make them meaningful.
  - Say how to make branches
    - Best practise for branches, i.e. make changes on them, keep master clean.
  - How to merge
    - Resolving merge conflicts
- How to use version control to collaborate. Say should understand how to use it for your own project before trying to understand how to do it with other people, if reading this section need to read (or already understand) previous one.
  - Divide into if it's your project people are collaborating on, and collaborating on someone else's?


## What is version control

*Should definitely have a diagram, couldn't find one I liked so I made this one. We could replace it with a better one later*

![github_diagram](figures/github_diagram.jpg)

*Should explain the concept of branches and merging here while I've got the diagram, but leave the details (e.g merge conflicts, what makes a good commit message) for later.*


## Why would you use version control?


From [here](https://guide.esciencecenter.nl/best_practices/version_control.html). **Creative Commons Attribution 4.0 International License**

- **Reproducibility** By using version control, you never lose previous versions of the software. This also gives you a log of changes and allows you to understand what happened.
- **Backup** Version control is usually pushed to an external a shared server, which immediately provides a backup.
- **Integration** Version control software and host makes it more easy to integrate with other software that support modern software development, such as testing (continuous integration ,automatically run tests, build documentation, check code style, integration with bug-tracker, code review infrastructure, comment on code).
- **Easier to collaborate** Version control makes it easier to work on the same code simultaneously, while everyone still has a well defined version of the software (in contrast to a google-docs or shared file system type of system). Moreover, version control hosting websites such as Github provide way to communicate in a more structed way, such as in code reviews, about commits and about issues.

--------

From [here](http://crlionline.net/node/198). **No license but active, could reach out**

If you are not ready for this yet, you will be at some time - when you have felt the horror of loosing days if not weeks of work. But versioning is useful for less dramatic purposes as well, not only for backup. For instance, to help you understand why in the past you made certain changes, why you did a certain analysis in the way you did it. Or you simply want to undo a change in your analysis. Or because you want to keep an audit trail of your analysis. Or to share it with others.

You yourself understand what the saved file does, even weeks or months later;
Others can easier understand what you did. This is helpful should you want to share your analysis (not only your data), and/or make it auditable--more generally, reproducible, which is good scientific practice.
This has the additional benefit that you need to understand for yourself what it is you just did.

When you restore from a backup, you are going back in time: I want to restore the last version, or to yesterday's (last week's) version. When you restore from a versioning system, you go back to a decision: I want to restore my former version, or an alternative version (a different branch),  because that one turns out to be the better solution or approach. Backup is a special case of versioning.

There are numerous tools for versioning, and the best know one is git and its web-based version, Github. (They are not really strongly different, in that you can use GitHub as the remote repository for your local git repository).

-----

From [here](http://who-t.blogspot.com/2009/12/on-commit-messages.html). **Creative Commons
Attribution License (http://creativecommons.org/licenses/by/2.0)**

*Other useful stuff in this paper, could use their into as part of the book's intro*

All scientists use version control in one form or another at various stages of their research projects, from the data collection all the way to manuscript preparation. This process is often informal and haphazard, where multiple revisions of papers, code, and datasets are saved as duplicate copies with uninformative file names (e.g. draft 1.doc, draft 2.doc). As authors receive new data and feedback from peers and collaborators, maintaining those versions and merging changes can result in an unmanageable proliferation of files. One solution to these problems would be to use a formal Version Control System (VCS), which have long been used in the software industry to manage code. A key feature common to all types of VCS is that ability save versions of files during development along with informative
comments which are referred to as commit messages. Every change and accompanying notes are stored independent of the files, which obviates the need for duplicate copies. Commits serve as checkpoints where individual files or an entire project can be safely reverted to when necessary. Most traditional VCS are centralized which means that they require a connection to a central server which maintains the master copy. Users with appropriate privileges can check out copies, make changes, and upload them back to the server.

When data are analyzed programmatically using software such as R and Python, code files start out small and often become more complex over time. Somewhere along the process, inadvertent errors such as misplaced subscripts and incorrectly applied functions can lead to serious errors down the line. When such errors are discovered well into a project, comparing versions of statistical scripts can provide a way to quickly trace the source of the problem and recover from them.

Similarly, figures that are published in a paper often undergo multiple revisions before resulting in a final version that gets published. Without version control, one would have to deal with multiple copies and use imperfect information such as file creation dates to determine the sequence in which they were generated. Without additional information, figuring out why certain versions were created (e.g. in response to comments from coauthors) also becomes more difficult. When figures are managed with Git, the commit messages (e.g. “Updated figure in response to Ethan’s comments regarding use of normalized data.”) provide an unambiguous way to track various versions.

### Commits

From [here](http://who-t.blogspot.com/2009/12/on-commit-messages.html). **No License, but blog still active, reached out 11/12/18**

A commit should contain exactly one logical change. A logical change includes adding a new feature, fixing a specific bug, etc. If it's not possible to describe the high level change in a few words, it is most likely too complex for a single commit. It's almost always better to err on the side of too many commits than too few.

Don't do:

- Per-file commits. More often than not a logical change affects more than one file and it should not be split up into two commits.
- Two changes in one commit. Something like "Fixed bug 2345 and renamed all foo to bar". Unless bug 2345 required the renaming you should split these into two commits. If you or a collaborator want to come back to a commit containing multiple changes to modify it or reuse only some of the changes it contains then problems quickly arise. Picking bad commits apart into useful chunks extremely time-consuming and frustrating since it doesn't actually add any value to the project.
- Whitespace changes together with code changes. Needle in a haystack is a fun game, but not when you're looking at commits. It's a great way to introduce bugs, though because almost no-one will spot the bug hidden in hundreds of lines that got reindented for fun and profit.
- Code drops, i.e. commits with hundreds of lines of code which dump in a new feature while at the same time rewriting half the existing infrastructure to support this feature. As a result, those hundreds of lines of code need to be reviewed every time a bug is discovered that is somehow related to that area of code.
It's easier and less time consuming to first rework the infrastructure one piece at a time, then plug the new feature on top. As a side-effect, if a project relies on code dumps too often it's discouraging outside developers. Would you like to contribute to a project where the time spent filtering the signal from the noise outweighs the actual contribution to the code?

----

### Commit messages


From [here](https://guide.esciencecenter.nl/best_practices/version_control.html). **Creative Commons Attribution 4.0 International License**

Commit messages are the way for other developers to understand changes in the codebase. In case of using GitHub flow model, commit messages can be very short but pull request comments should explain all the changes. It is very important to explain the why behind implementation choices.

-----

From [here](http://who-t.blogspot.com/2009/12/on-commit-messages.html). **No License, but blog still active, could reach out**

Any software project is a collaborative project. It has at least two developers, the original developer and the original developer a few weeks or months later when the train of thought has long left the station. This later self needs to re-establish the context of a particular piece of code each time a new bug occurs or a new feature needs to be implemented. Re-establishing the context of a piece of code is wasteful. We can't avoid it completely, so our efforts should go to reducing it to as small as possible.

A good commit message should answer three questions about a patch:

- **Why is it necessary?** It may fix a bug, it may add a feature, it may improve performance, reliability, stability, or just be a change for the sake of correctness.
- **How does it address the issue?** For short obvious patches this part can be omitted, but it should be a high level description of what the approach was.
- **What effects does the patch have?** (In addition to the obvious ones, this may include benchmarks, side effects, etc.)

These three questions establish the context for the actual code changes, put reviewers and others into the frame of mind to look at the diff and check if the approach chosen was correct. A good commit message also helps maintainers to decide if a given patch is suitable for stable branches or inclusion in a distribution.

A patch without these questions answered is mostly useless. The burden for such a patch is on each and every reviewer to find out what the patch does and how it fixes a given issue. Given a large number of reviewers and a sufficiently complex patch, this means many man-hours get wasted just because the original developer did not write a good commit message. Worse, if the maintainers of the project enforce SCM discipline, they will reject the patch and the developer needs to spend time again to rewrite the patch, reviewers spend time reviewing it again, etc. The time wasted quickly multiplies and given that a commit message only takes a few minutes to write, it is simply not economically viable to omit them or do them badly.

Don't describe the code, describe the intent and the approach. And keep the log in a present tense.


-----
By [Thom Holwerda](http://www.osnews.com/story/19266/WTFs_m). **Says anyone can do whatever, attribution nice but not compulsory**

*Maybe include this somewhere else but have it somewhere*

![wtf_per_min](figures/wtf_per_min.jpg)

## Branches

*Think we should go over deleting branches before we go over merging. Deleting's quicker and easier to explain.*

From [here](https://opensource.com/article/18/5/git-branching) **Creative Commons license**
The main reasons for having branches are:

- If you are creating a new feature for your project, there's a reasonable chance that adding it could break your working code. This would be very bad for active users of your project. It's better to start with a prototype, which you would want to design roughly in a different branch and see how it works, before you decide whether to add the feature to the repo's master for others to use.
- Another, probably more important, reason is Git was made for collaboration. If everyone starts programming on top of your repo's master branch, it will cause a lot of confusion. Everyone has different knowledge and experience (in the programming language and/or the project); some people may write faulty/buggy code or simply the kind of code/feature you may not want in your project. Using branches allows you to verify contributions and select which to add to the project. (This assumes you are the only owner of the repo and want full control of what code is added to it. In real-life projects, there are multiple owners with the rights to merge code in a repo.)


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

### Resolving merge conflicts

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

## Forks

## Git

*I think this section should go over the command line nitty-gritty. The explanation of what branches are etc should all be done before that because that's common to all VC, this section is git specific, and command line specific*

*There's a how too [here](https://tonysyu.github.io/source-control-for-scientists-and-soloists.html#.XA6Q3mj7RPY). Basic but something to build on.* **No License, but github still active, could reach out**

*Very detailed how to [here](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter).* **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.**

*Very lightweight guide [here](http://rogerdudler.github.io/git-guide/)* **No license, no activity on github past year**



## Github

*I think this section should go over how to do this in the browser/gui nitty-gritty. Again, the explanation of what branches are etc should all be done before.*

*Detailed guide of how to use github [here](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)* **No visible license could try reaching out**
