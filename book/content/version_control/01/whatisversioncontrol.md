## Version control: What it is and how it can be used to manage an evolving project

### What it is

What is "version control" and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.
It is typically applied to managing changes in code, though in reality you can do this with nearly any type of file on a computer.

### The basic workflow

The typical procedure for using version control is as follows:

1. Create some files - these may be text or code.
2. Work on these files, changing, deleting or adding new content.
3. Create a snapshot of the work at this time.
This will be described differently in different software.
Git will ask you to make a commit, other systems make ask you to make a timepoint or checkpoint or just to save your work.

Keep doing work and making more and more snapshots.
You can think of these as savepoints - if you need to go back to any point in time because of a mistake, or changing your mind about a decision, you can go back to get a file as it was then, or just return your entire project to a past state.
An illustration of this is shown in the figure below.  

![master_branch](../figures/master_branch.png)

In lots of version control systems you will be able to add a comment explaining what changes have been made in this version. 
These comments should be as clear as possible and make it easy to understand which version is which.
This ensures that it is easy to find what you are looking for when you need to go back to a past version.
Your collaborators will thank you, but so will future versions of yourself.

### Other facilities offered by version control

So you have your project and you want to add something new or try something out.
With some of the more advanced version control systems (for example Git) you can make a branch to do this work on.
Any work you do on your branch will not be present on your main project (referred to as your master branch) so it remains nice and safe and you can continue to work on it.
Once you are happy with your New Thing you can 'merge' your branch back into your master copy.

![one_branch](../figures/one_branch.png)

You can have more than one branch off of your master copy, and if one of your branches ends up not working you can either abandon it or delete it without the master branch of your project ever being impacted.

![two_branches](../figures/two_branches.png)

If you want you can even have branches off of branches (and branches off of those branches and so on).

![sub_branch](../figures/sub_branch.png)

No matter how many branches you have you can access past savepoints you made on any of them.

