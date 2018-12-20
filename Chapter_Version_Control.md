## *This chapter is still a work in progress, but enough work has been completed that reviews/contributions are welcome*

# Version Control

## General thoughts

*Thoughts here and throughout will be in italics*

*Might be worth having a summarising table with commands and what they do.*

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
  - *~~First paragraph, core benefits focusing on how it helps the USER, convince people this is something they should invest time in to help thier research in the long term. Keeps versions safe and recoverable,~~ keeps things tidy*
  - *Say it enables collaboration*
  - *How it benefits science, reproducibility etc. Maybe not that relevant here, maybe more open source's thing?*
- *~~Prerequisites / recommended skill level~~*
- *Definitions/glossary*
- *How to use version control for your own project and how to use it well*
  - *Intro*
    - *~~Say in terms of how to do it we're going to give the actual commands to do all this in git because widely used, but the info on good practise, i.e. how to do it well, is still relevant even if you're using other VC software like mercurial.~~*
    - *~~Set up a repo, git init. Don't talk about putting it online yet.~~*
  - *~~Commits~~*
    - *~~Problem = want to access past versions~~*
    - *~~Say how to add files, say how git status tells you what's been added. Git diff to see the difference. How to make a commit and how to get files/whole project back to past commit. Say git log gives log of past commits. Git diff to see what changed between two commits.~~*
    - *~~Best practice for committing, e.g. keep bitesized, don't do per-file commits, whitespace changes together with code changes, or code drops~~*
  - *~~Commit messages~~*
    - *~~Problem = when you've been working on a project for a while different versions stack up, hard to remember what does what. Having something is no good if you can't find/understand it, and figuring it out can take valuable time.~~*
    - *~~Say what commit messages are~~.*
    - *~~Explain that when you commit (regardless(???) of what VC software you're using) you can give a commit message, say show up in git log.~~*
    - *~~How to give a commit message.~~*
    - *~~Best practise for commit messages. e.g. make them meaningful, cover why the change is necessary, how it addresses the issue, and what effects the change has. Also don't describe the code, describe the intent and the approach. And keep the log in a present tense.~~*
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

Branch
Commit
Commit message
git
GitHub   *say online, aids collaboration*
HEAD
Master branch
Merge
Merge conflict
Repository
SHA
Staging area






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

![sub_branch](figures/sub_branch.png)

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








There are numerous tools available for version control such as Mercurial and SVN. The best know one is Git (and its web-based version, Github) which the instructions in this chapter will be geared towards. There are a large number of detailed tutorials available online discussing the features and mechanics of how to use such systems (see the "Additional material" section at the end of the chapter.) This chapter aims to cover the general principles underpinning all version control systems, and best practise applies for using such systems.


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

Just think of the repository as a place where the history is being stored.
Each file in your working directory can be in one of two states: tracked or untracked by your repository. In short, tracked files are files that Git knows about. Untracked files are everything else — any files in your working directory that were not in your last snapshot. When you first initialise a repository with `git init` all of your files will be untracked because your repository it doesn't *have* a previous snapshot yet, so it doesn't know about any of your files. Therefore your next step is to add your files to the repository using

```
git add .
```

This puts your changes into what's called the "staging area". When you next commit any changes stored in your staging area will be recorded in your repository.

![change_stage_repo](figures/change_stage_repo.png)

The full stop after `git add` above adds all changes to your staging area. So now all your files are staged commit them using

```
git commit
```

We'll talk in more detail about these commands later, but for now just know if you run them then congratulations, you have finished setting up you repository!

### Commits

**The problem:** when working on a project you will make numerous changes to you files as you progress. Sometimes you may need to undo changes, take another look at past versions, or compare versions. Saving each version individually (version_1.py, version_2.py etc) is messy and quickly becomes impractical.

**The solution:** by making commits you can save versions of your code and switch between them/compare them easily without cluttering up your directory. Commits serve as checkpoints where individual files or an entire project can be safely reverted to when necessary.

**How to do it:** when you've made a series of changes and you want to commit them you fist add these changes to your staging area using `git add`. You can add all your changes using

```  
git add .
```

or you can add the changes to specific files via

```  
git add your_file_name
```

If you're ever unsure what files have been added, what files have been changes, what files are untracked etc you can running

```
git status
```

To find out. When you're ready you can commit everything in your staging area by running

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

You may want to retrieve a version form weeks or months ago. To do this first use `git log` to find the SHA of the version you want to retrieve. To reset your entire project to this version do

```
git checkout SHA_of_the_version
```

 You may just want the old version of a single file though, and not the previous version of the whole project. To retrieve this use

 ```
 git checkout SHA_of_the_version -- your_file_name
 ```

#### Comparing files/commits/branches

In short: `git diff`.

Diffing is a function that takes two input data sets and outputs the changes between them. `git diff` is a multi-use Git command that when executed runs a diff function on Git data sources. These data sources can be commits, branches, files and more.

By default `git diff` will show you any uncommitted changes since the last commit. If you want to compare two specific things the syntax is

```
git diff thing_a thing_b
```

For example if you want to compare how a file has changed between two commits use `git log` to get the SHAs of those commits and run

```
git diff SHA_a:your_file_name SHA_b:your_file_name
```

Or if you wanted to compare two branches it would be

```
git diff branch_name other_branch_name
```

#### Good practise for commits

Commits should be 'atomic' i.e **they should do one simple thing and they should do it completely**. If a lot of different changes to your project are all committed together then if something goes wrong it can be hard to unpick what in this set of changes if causing the problem, and simply undoing the whole commit may throw away valid and useful work along with the bug. That said **you don't necessarily need to do per-file commits**. For example if I add a figure to this chapter here, let's choose something to catch the attention of someone skimming through:

![flipped_taj_mahal](figures/flipped_taj_mahal.png)

then when I do this two files are changed:

1. The figure file had been added
2. I've added a reference to this figure in the chapter so it will be displayed.

So two files are affected, but "Add figure to version control chapter" is a single, *atomic* unit of work, so only one commit is necessary.

To aid in making atomic commits it's good practise to **specify the files to be committed**, i.e. adding files to the staging area by name (`git add your_file_name`) rather than adding everything (`git add .`). This prevents you from unintentionally bundling different changes together, for example if you've made a change to file A while primarily working on file B you may have forgotten this when you go to commit, and with `git add .` file A would be brought along for the ride.

Finally, **don't commit anything that can be regenerated from other things that were committed unless it is something might take hours to regenerate**. Generated files just clutter up your repository and make contain features such as timestamps that can cause annoying merge conflicts (see below). On a similar note you should not commit configuration files, specifically configuration files that might change from environment to environment. You can instruct git to ignore certain files by creating a file called `.gitignore` and including their names in it.

### Commit messages

**The problem:** as you work on you project you will make more and more commits. Without any other information it can be hard to remember which version of your project is in which.

**The solution:** When you commit you have the chance to write a commit message describing what the commit is and what it does, and you should always, *always,* **_always_** do so.  A commit message gets attached to the commit so if you look back at it (e.g via `git log`) it will show up. Creating insightful and descriptive commit messages is one of the best things you can do to get the most out of version control. It lets people (and your future self when you've long since forgotten what you were doing and why) quickly understand what changes a commit contains without having to carefully read code and waste time figuring it out. Good commit messages improve your code quality by drastically reducing its WTF/min ratio:

![wtf_per_min](figures/wtf_per_min.jpg)

**How to do it:** when you commit, instead of using `git commit` instead do

```
git commit -m "Your commit message"
```

**Good practise for commit messages**

The number one rule is: **make it meaningful**. A commit message like "Fixed a bug" leaves it entirely up to the person  looking at the commit (again, this person may very well be you a few mnths in the future when you've forgotten what you were doing) to waste time figuring out what the bug was, what changes you actually made, and how they fixed it. As such a good commit message should explain what you did, why you did it, and what is impacted by the change.

**Summarise the change** the commit contains in the first line (50-72 characters).
It’s also a good practise to **use the imperative present tense** in these messages. In other words, use commands. Instead of "I added tests for" or "Adding tests for" use "Add tests for".

Here's a good example of commit message structure:

```
Short (50 chars or less) summary of changes

More detailed explanatory text, if necessary.  Wrap it to
about 72 characters or so.  In some contexts, the first
line is treated as the subject of an email and the rest of
the text as the body.  The blank line separating the
summary from the body is critical (unless you omit the body
entirely); tools like rebase can get confused if you run
the two together.

Further paragraphs come after blank lines.

  - Bullet points are okay, too

  - Typically a hyphen or asterisk is used for the bullet,
    preceded by a single space, with blank lines in
    between, but conventions vary here
```

## Branches

**The problem:** if you are creating a new feature for your project, there's a reasonable chance that adding it could break your working code. This would be very bad for active users of your project, even if the only active user is you. It's better to start with a prototype, which you would want to design roughly in a different branch and see how it works, before you decide whether to add the feature to the master branch. Also version control systems are regularly used for collaboration. If everyone starts programming on top of the master branch, it will cause a lot of confusion. Some people may write faulty/buggy code or simply the kind of code/feature others may not want in the project. Using branches allows you to contributions to be verified and reviewed before being added to the main project. There needs to be a way allow new work to be done on a project whilst protecting work that has already been done.

**The solution:** branches. At the start of this chapter an overview was given of the concept of branches, but let's recap. You have a project, and you make commits on it. By default you have one branch, called 'master'. Making a
branch essentially makes a copy of your code which you can work on and continue to make commits to. Meanwhile your master branch is untouched by these changes, and you can continue to make commits on it too. Once you're happy with whatever you were working on on a branch you can merge it into your master branch (or indeed any other branch). Merging will be covered in the next section. If your work on a branch doesn't work out you can delete or abandon it (e.g. Feature B in the diagram below) rather than spending time unpicking your changes if you were doing all your work on the master copy. You can have as many branches off of branches as you desire (e.g. Feature C).

![sub_branch](figures/sub_branch.png)


**How to do it:** You can create a branch and switch to it using:
```
git checkout -b name_of_your_new_branch
```

To change between branches:
```
$ git checkout name_of_the_branch
```

though you much commit any work you have in progress before you will be able to switch. You can see all branches of your project simply using
```
$ git branch
```
which will output a list with an asterix next to the branch you're on. You can also use `git status` if you've forgotten which branch you're on.

If you decide to get rid of a branch you can delete it with
```
$ git branch -D name_of_the_branch
```

**Good practice for branches**

Branches should be used to **keep the master branch clean**. Similarly you should try to keep individual branches as clean as possible by **only adding one new feature per branch**, because if you are working on several features some may be finished and ready to merge into master while others are stull under development. Give your branches **sensible names**, "new_feature" is all well and good until you start developing a newer feature on another branch.

## Merging

**The problem:** once you've finished up some work on a branch you need to add it to your main project (or any other branch).

**The solution:** merge the branch with your work on into your target branch. You can also use merging to combine work that other people have done with your own.

**How to do it:** to merge some branch, branch_A, into another branch, branch_B, switch to branch_A via `git checkout branch_A` and merge it into branch_B by

```
git merge branch_B
```

Merging will not be possible if there are changes in either your working directory or staging area that could be written over by the files that you are merging in. If this happens, there are no merge conflicts in individual files. You need to commit or stash the files it lists and then try again. The error messages are as follows:

```
error: Entry 'your_file_name' not uptodate. Cannot merge. (Changes in working directory)
```
or
```
error: Entry 'your_file_name' would be overwritten by merge. Cannot merge. (Changes in staging area)
```

**Best Practise for merging**

First and foremost your **master branch should always be stable**, only merge work that is finished and tested into it. If your project is collaborative then it's a good idea to **merge changes that others make into you own work frequently**. If you don't it's very easy for merge conflicts to arise (next section). Similarly, share your own changes with your collaborators often.


### Merge conflicts

**The problem:** when changes to made to the same file on different branches sometimes those changes may be incompatible. This most commonly occurs in collaborative projects, but it happens in solo projects too. Let's say there's a project and it contains a file with this line of code:

```
print('hello world')
```

Lets say one person, on their branch, decides to pep it up a bit and changes this line to

```
print('hello world!!!')
```

while someone else on another branch instead decides to change `print('hello world')` to

```
print('Hello World')
```

They continue doing work on their respective branches and eventually decide to merge. Their version control software then goes through and combines their changes into a single version, *but* when it gets to the hello world statement it doesn't know which version to use. This is a merge conflict: incompatible changes have been made to the same file.

**The solution:** when a merge conflict arises use `git status` to find out which files the conflicts are in. Within those files the incompatible changes will be marked so you can fix them:

```
<<<<<<< HEAD
print('hello world!!!')
=======
print('Hello World')
>>>>>>> master
```
'<<<<<<<': Indicates the start of the lines that had a merge conflict. The first set of lines are the lines from the file that you were trying to merge the changes into.

'=======': Indicates the break point used for comparison. Breaks up changes that user has committed (above) to changes coming from merge (below) to visually see the differences.

'>>>>>>>': Indicates the end of the lines that had a merge conflict.

**How to do it:** you resolve a conflict by editing the file to manually merge the parts of the file that git had trouble merging. This may mean discarding either your changes or someone else's or doing a mix of the two. You will also need to delete the '<<<<<<<', '=======', and '>>>>>>>' in the file. So in this project the users may decide in favour of one `hello world` over another, or they may decide to replace the conflict with

```
print('Hello World!!!')
```

Once you've fixed the conflicts commit the new version. You've now resolved the conflict.

If you find there are particularly nasty conflicts and you want to abort the merge you can using
```
git merge --abort
```


**Good practise for resolving merge conflicts**

Before you start trying to resolve conflicts **make sure you fully understand the changes and how they are incompatible**. If you don't you risk making things more tangled. Once you do and you go about fixing the problem **be careful, but don't be afraid**; the whole point of version control is your past versions are all safe. Nevertheless merge conflicts can be intimidating to resolve especially if you are merging branches that diverged a great many commits ago which may now have many incompatibilities. This is why it is good practise to merge other's changes into your work frequently.

There are **tools** available to assist in resolving merge conflicts. Find and familiarise yourself with one that works for you. To set a tool as your default do

```
git config --global merge.tool name_of_the_tool
```

and launch it by

```
git mergetool
```

Fundamentally the best way to deal with merge conflicts is to, so far as is possible, **ensure they don't happen in the first place**. Keep branches clean and focused on a single issue and involve as few files as possible. Before merging make sure you know what's in both branches, and if you are not the only one that has worked on the branches then keep the lines of communication open so you are all aware of what the others are doing.

## GitHub

**The problem:** when multiple people work on the same project (which is becoming more and more common as research becomes more collaborative) it becomes difficult to keep track of what changes have been made and by who. It is also often difficult and time-consuming to manually incorporate the different participant's work into a whole even if all of their changes are compatible.  

**The solution:** hosting your project on a distributed version control system such as GitHub. Collaborators can then clone the project and work on that copy where they can still make commits, branches, etc. Collaborators can then *push* their work to each other, and *pull* other's work into their own copy. In this way it is easy to keep everyone up to date and to track what has been done and by who. GitHub also has numerous other handy features such as the ability to raise and assign issues, discuss the project via comments, and review each other's changes.

Making your entire project and its history available online in this was also has two major benefits for research:

1. Other researchers can re-use your work more easily. Rather than writing their own code to do what you already have they can just use yours, which saves time. This also benefits you as researchers are much more likely to build on your work (and cite you) if a great deal of the work has already been done.   
2. Your work will be much more reproducible if the entire history of the project can be tracked. This enables results to be verified more easily, which benefits science.

**How to do it:** first make an account on [GitHub](https://github.com/), and create a repository on it. To do this click  the + sign dropdown menu in the upper right hand of the screen. Enter a name for your repository (ideally the same name as your project folder on your computer) and click Create Repository. Now you just need to link the project on your computer to this online repository. If your project is not already version controlled then make it so by running `git init` and making a commit. In the terminal on your computer use
```
git remote add origin https://github.com/your_username/repository_name
```

then *push* all the files on your computer to the online version so they match via
```
git push -u origin master
```

You can the go on and make more commits on your computer. When you want to push them to your online version similarly you do
```
git push origin branch_you_want_to_push_to
```

Others can then clone your repository to their computer by using
```
git clone https://github.com/your_username/repository_name.git
```

They cam make and commit changes to the code without impacting the original, and push their changes to *their* online GitHub account using   
```
git push -u origin master
```

Naturally the exact same procedure applies to you if you want to clone someone else's repository.

So everyone's got a copy of the code and they're merrily working away on it, how do collaborators share their work? Pull requests. A pull request is a request for a person to *pull* your changes into their version on the project. Say person A has made changes they want to share with person B. On GitHub Person A needs to go to person B's copy of the project and click the "New pull request" button. From there they can indicate which of their branches they would like person B to pull changes from, and which branch they want the changes pulled to. If person B accepts then person A's changes will be merged into their repository by GitHub. They can discuss the request in comments, and make further commits to the request before it is accepted if necessary.

When person B is setting up the pull request GitHub will automatically check whether there would be any merge conflicts if they accept, and highlight them if there are. These can then be resolved in further commits before the request is accepted, keeping the merge clean and painless.

Once the request is accepted GitHub will merge person As changes into person B's online copy of the repository. Person B can the *pull* those changes down to the copy on their computer using

```
git pull origin master
```


**Best practise**

In your GitHub repository you should **include a license** to allow others to re-use your work legally. GitHub makes this very easy, simply click the "Create new file" button and name it "License.md" and a drop down menu will appear offering you a selection to choose from. The legalese can seem intimidating however [this](https://choosealicense.com/) website offers a very simple mechanism to help you pick the best license for your project.

You should also **include a readme file** where you include useful information about what the project is, how to use it and how to contribute to it. Switching between projects in your work is common, let alone that you might need to poke at your own previous projects from time to time. This information will also assist you collaborators, and your future employer might want to check your existing Github projects.

There are plenty of readme templates available online, pick one you like, but here's a list of the main things a readme should include:

- The project name and what it is. This will greatly help the random prospective contributor to get an idea of the project. Include a few key points that describe the main features of the project and what are the main features you're implementing.
This helps to quickly compare other projects with yours and to give an idea that why the project exists in the first place.
- Instructions on how to install the project. The installer might be a collaborator, someone that comes across and is interested in the project, or even you if you get a new machine and need to re-install your project. Nevertheless, it's a total waste of both of your resources to start figuring out how to just get started with the project. This should also include any prerequisites that will be needed to run the project.
The best thing you can do is to just write up the installation instructions when you first do them yourself, and you'll quickly save hours of work in the future.
- Instructions for how to run the project and any associated tests. If you've been working on your project it may seem obvious how to run it, but this will likely not be the case for someone coming across it for the first time.
- Links to related material
- List of authors/contributors to the project, possibly with contact information
- Acknowledgements



code of conduct
pull request/issue templates
ways of working

## What to learn next?

## Additional materials

### Recommended reading

- A free and very in depth book on gits myriad of features can be found [here](https://git-scm.com/book/en/v2)
- A useful git cheat sheet can be found [here](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)

### Materials used in this chapter

[This](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Controls) **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License**
[This](https://link.springer.com/article/10.1186/1751-0473-8-7). **Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0)** *Other useful stuff in this paper, could use their into as part of the book's intro*
[This](http://crlionline.net/node/198). **Permission to use given by the author (Peter Reimann) 15/12/18**
[This](https://tonysyu.github.io/source-control-for-scientists-and-soloists.html#.XA6Q3mj7RPY). **Permission given by the author (Tony Yu) 15/12/18**
[This](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter).* **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.**
[This](https://githowto.com/undoing_committed_changes). **creative commons Attribution-NonCommercial-ShareAlike 4.0 International**
[This](https://www.atlassian.com/git/tutorials/saving-changes/git-diff) **Creative Commons Attribution 2.5 Australia License.**
[This](http://sethrobertson.github.io/GitBestPractices/) **Creative Commons Attribution-ShareAlike 3.0 Generic**
[This](https://guide.esciencecenter.nl/best_practices/version_control.html). **Creative Commons Attribution 4.0 International License**
[Taj Mahal Figure](https://commons.wikimedia.org/wiki/Taj_Mahal#/media/File:Taj_Mahal_in_March_2004.jpg)**GNU Free Documentation License**
[This](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project) **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License**
[This](https://opensource.com/article/18/5/git-branching) **Creative Commons license**
[This](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches) **GNU GENERAL PUBLIC LICENSE Version 3**
[This](http://genomewiki.ucsc.edu/index.php/Resolving_merge_conflicts_in_Git) **["You are granted a limited license to copy anything from this site"](http://genomewiki.ucsc.edu/index.php/Genomewiki:General_disclaimer)**
[This](https://githowto.com/resolving_conflicts). **creative commons Attribution-NonCommercial-ShareAlike 4.0 International**
[This](http://genomewiki.ucsc.edu/index.php/Resolving_merge_conflicts_in_Git) **["You are granted a limited license to copy anything from this site"](http://genomewiki.ucsc.edu/index.php/Genomewiki:General_disclaimer)**
[This](https://opensource.com/article/18/1/step-step-guide-git) **Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**
[This](https://kbroman.org/github_tutorial/pages/init.html) **Attribution 3.0 Unported (CC BY 3.0)**
[This](https://opensource.com/article/18/2/how-clone-modify-add-delete-git-files) **Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**
[readme](https://thejunkland.com/blog/how-to-write-good-readme.html) **Creative Commons Attribution-NonCommercial 2.5 License**
[readme template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) **MIT**
### Other useful links
