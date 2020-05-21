### The basic workflow

Version control is a systematic approach to record changes made in a file or set of files over time so that you and your collaborators can track the history, see what changed and recall specific versions later when needed.
A typical procedure for using version control is as follows:

1. Create files - these may contain text, code or both.
2. Work on these files, by changing, deleting or adding new content.
3. Create a snapshot of the file status (also known as version) at this time.

This process of creating a snapshot, which is described differently in different version control software.
For example, Git describes it as "a commit", a few systems call it "a timepoint" or "a checkpoint", and this is simply referred to as "saving your work" in other cases such as in [Google docs](https://docs.google.com/) or [HackMD](http://hackmd.io/).

As you keep saving your work by adding changes, you make more and more snapshots.
You can think of these as saving versions of these files while documenting their history.
If you need to go back to the version of a file in a specific point in time because of a mistake, or if you changed your mind about a previous update, you can access the file in your preferred version, or return your entire project to a past state.

An illustration of this is shown below.

![master_branch](../../figures/master_branch.png)

In many version control systems, you will be able to add a comment every time you save a new version.
These comments should be clear and concise to make it easy to understand what changes were proposed and what updates were made in a version.
This ensures that it is easy to find what you are looking for when you need to go back to a past version.
Your collaborators will thank you, but so will future versions of yourself.

### Other features offered by version control

So you have your project and you want to add something new or try something out before reflecting the changes in the main project folder.
To add something new, you can continue editing your files and save changes with the proposed changes.
If you want to try something without reflecting the changes in the main repository first, you can use the "branching" feature of more advanced version control systems such as Git.
A branch creates a local copy of the main repository where you can work and try new changes.
Any work you do on your branch will not be reflected on your main project (referred to as your master branch) so it remains secure and error-free while you test your ideas and troubleshoot in a local branch.

When you are happy with the new changes, you can introduce them to the main project.
The merge feature in Git allows the independent lines of development in a local branch to get integrated into the master branch.

![one_branch](../../figures/one_branch.png)

You can have more than one branch off of your master copy, and if one of your branches ends up not working you can either abandon it or delete it without impacting the master branch of your project.

![two_branches](../../figures/two_branches.png)

If you want you can even create branches off of branches (and branches off of those branches and so on).

![sub_branch](../../figures/sub_branch.png)

No matter how many branches you have you can access past versions you made on any of them.

## Why should you use version control?

As explained in the earlier section, version control helps us understand what changes we made in the past or why we did a certain analysis in the way we did it, even weeks or months later.
With the help of comments and commit messages, each version can explain what changes it contains compared to the previous versions.
This is helpful when we share our analysis (not only data), and make it auditable -- more generally, **reproducible**, which is good scientific practice.

A version control system stores all your changes neatly away so while it is still easy to access them your working directory is not cluttered by the debris of versions past that it is necessary to keep just in case.
Similarly, with version control there is no need to leave chunks of code commented should you ever need to come back to an old version again.

Finally, version control is invaluable for collaborative projects where different people work on the same code simultaneously and build on our work.
It allows the changes made by different people to be tracked, and can automatically combine people's work while saving a great deal of painstaking effort to do so manually.
Moreover, version control hosting websites, such as GitHub, provides a way to communicate in a more structured way, such as in code reviews, about commits and about issues.
