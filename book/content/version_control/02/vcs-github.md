## Version control using GitHub

As research becomes increasingly collaborative and multiple people work on the same project, it becomes difficult to keep track of changes made by others if not done systematically.
Moreover, it is time-consuming to manually incorporate the work of different participants in a project, even when all of their changes are compatible.
Hosting the project on an online distributed version control system like GitHub is beneficial to make collaborations open and effective.
If you are new to collaboration through [GitHub](https://github.com), please follow a comprehensive guide in the collaboration section.

In this section we will discuss how to use Git commands to work on GitHub repository.

### Create a local copy of an online repository

There are some GitHub features that can be accessed via command-line Git tool.
For example, one can create an independent local copy of the project using the following Git command:

```
git clone <insert GitHub link of the repository here>
```

Collaborators can update their local version of an online repository or *pull* other's work into their own copy using the command:
```
git pull
```
Similarly, they can edit files locally and stage their updates (`git add .`), commit changes to a new version (`git commit`) and *push* changes to the remote online repository using the Git command:
```
git push
```

### Link a local project on your computer to an online repository

To link a project on your computer to a new GitHub repository (preferably with the same name) you need to follow the standard workflow for creating a Git repository (described in the [version control chapter](/version_control/01/vcs_workflow)) by using the following set of commands in the terminal one by one:

```
cd <your project folder>
git init
git add .
git commit
```
Assuming that you have a GitHub repository that you want want to commect with this project, run the following command

```
git remote add origin <GitHub repository link for your project>
```

Then, *push* all the files on your computer to the online version so they match via:

```
git push -u origin master
```

You can the go on and make more commits on your computer.
When you want to push them to your online version similarly you do:

```
git push origin branch_you_want_to_push_to
```

You can also make changes directly on the GitHub by editing the online repository, and *pull* those changes locally by using the Git commans `git pull`

Others can then clone the repository to their computer by using:

```
git clone https://GitHub.com/your_username/repository_name.Git
```

They can make and commit changes to the code without impacting the original, and push their changes to *their* online GitHub account using:

```
git push -u origin master
```

The exact same procedure applies to you if you want to clone someone else's repository.

#### Pull requests

If you are working on a personal branch and meanwhile if some other changes were made in the master branch, you can *pull* those changes down to your branch using the Git command:
```
git pull origin master
```

When everyone's has a copy of the project on their personal branch (checkout to your branch with `git checkout branch-name`), they can *push* their changes to their branch by using the following command:

```
git push origin branch-name
```

However, if you can not directly edit the repository (when you are not an owner of admin of the project), you will be able share your work with the help of *pull requests*.
A pull request allows a contributor get their proposed changes from their personal branch or repository integrated in their master branch of the project.
It is also possible to make pull requests via the command line (see the GitLab documentation [here](https://git-scm.com/docs/git-request-pull)), but we have discussed this in detail in the collaborating with GitHub chapter in this book.

### Contributing to other projects

When you create a local copy of a repository, you only keep the versions of the files that are in the repository at the time of creating that copy.
If there are any changes made in the original repository afterwards, your copy will get out of sync out of sync.
This can lead to problems like conflicting file contents when making a pull request or merging changes from your branch to the main repository.
Therefore, when working on different branches or forks of a repository, it's a good practice to keep them updated frequently with the master repository and keep them in sync with the original repository.

#### A workflow to contribute to others GitHub projects via `git`: 

Using the fork botton on the GitHub repository you wish to contribute, create a personal copy of the repository in your account.
The master repository that you forked will be referred as "upstream" repository.

You can now work on your personal copy using commandline using following steps.

1. clone it to your local machine:

```
git clone git@github.com/your_username/forked_repository.git
```

2. Add the 'upstream' repository to list of remote repositories using a similar command as below (replace the upstream repository's users id and original repository name)

```
git remote add upstream https://github.com/upstream_user's_username/original_repository.git
```

3. Verify the new remote 'upstream' repository

```
git remote -v
```

4. Whenever you want to update your fork with the latest upstream changes, you'll need to first fetch the upstream repository's branches and latest commits to bring them into your repository:

```
git fetch upstream
```

5. View all branches, including those from upstream

```
git branch -va
```

Make sure that you are on your master branch locally, if not, then checkout your master branch using the command `git checkout master`

6. Now you can keep your fork update by merging those commits (fetched from the upstream) to your own local master branch.

```
git merge upstream/master
```

Now, your local master branch is up-to-date with everything modified upstream.
If there are no unique commits on the local master branch, git will simply perform a fast-forward. 

*Note: The upstream/master is the original repository's master which you wish to contribute to, whereas origin/master refers to the repository you cloned in your local machine after it was forked on GitHub.*

Once your fork is in sync with upstream master repository, you can always keep your local cloned repository in sync with origin (fork in this case) by using:

```
git checkout master
git pull origin master
```

The git pull command combines two other commands, git fetch and git merge. 
When using fetch, the resulting commits are stored as the remote branch allows you to review the changes before merging.

Similarly, if you have created more branches other than master, you can also keep them in sync with your master, once it is in sync with the upstream repository.

```
git checkout my-other-branch
git pull origin my-other-branch
```

When everything is  up-to-date, you can work on your branch and commit changes. 

When you are ready to push your local commits to your forked repository (origin), use the following command.

```
git push origin forked_repository
```

Now you can make a pull request!

#### Good practice

Before you create a branch, make sure you have all the upstream changes from the origin/master branch.

Word of caution on `rebase` command: While trying to keep your branches in sync, you may come across `rebase` command.
It tends to rewrite history and could be troublesome if not communicated with others working on the same branch, therefore try to avoid using `rebase` command, and instead use `pull` or `fetch`+`merge` as discussed in this sectoon.
You can find more details about Merging vs Rebasing [here](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

#### Further reading
- An article on syncing a fork of a repository to keep it up-to-date with the upstream repository can be found [here](https://help.github.com/en/articles/syncing-a-fork).
- If you wish to do it all in the browser itself, instructions to do so can be found [here](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser).

## Summary of key Git commands specific to GitHub

| Command                       | Use                                                                      |
| ----------------------------- | ------------------------------------------------------------------------ |
| git clone URL                 | Makes a clone of the repository at the specified URL                     |
| git remote add origin URL     | Links local repository and repository at the specified URL               |
| git push origin branch_name   | Push local changes to the specified branch of the online repository      |
| git pull origin branch_name   | Pull changes to online repository into local repository                  |


<!---MOVE THIS SECTION BELOW TO THE COLLABORATION SECTION

## Using GitHub for effective collaboration

**[GitHub](https://GitHub.com/) is online web interface**, it’s designed to share your work, and allow others to create an independent copy of your work to test, modify, remix and reuse it without impacting the original repository.
GitHub has many useful features that allows us to visually track changes made on a file, acknowledge contributors for their contributions and keep projects up to date.

There are many features of [version control system](LINK THIS) that can be accessed via GitHub web interface, for example, creating new files, updating them, reviewing others work and tracking different versions.

Some GitHub features can be accessed through 'Git',(as), but, many project management and communication related features can be accessed only via its web interface.
For example, opening or raising an issue related to the project, involve collaborators in discussing those issue via comments, request help and review each other's changes online.
GitHub can help maintain transparency and effective communication among the various stakeholders by making the entire history of the project traceable online, which adds to the reusability aspects of research.

### Getting started with GitHub

First, let's create an account (if your don't have one already) by signing up on [GitHub](https://GitHub.com/).

| ![a screengrab of the GitHub home page for creating an account](../../figures/github-account.png)         |
| ------------------------------------------------------------------------------------ |
| A screenshot of the GitHub home page, that shows how you can create or sign into your account  |

To test its features properly, let's create a new repository for your project by clicking the plus sign on the dropdown menu in the upper right hand of the screen.
Enter a name for your project repository, check box for "Initialize this repository with a README" and click "Create Repository".

In this chapter we will create a test repo called "friendly-github-lesson", as shown in th image below.

| ![screengrab showing how to create a new repo](../../figures/github-repo.png) |
| ------------------------------------------------------------------------------------ |
| A screenshot from the GitHub profile, showing how a new repository can be created for a project called "friendly-github-lesson" |

Congratulations! You just created your GitHub repository.
You will find your repository with a README.md file, which is currently empty as we haven't yet added any information there.
A README file in a landing page for the repo which should give information about your project, list names and contact details for your team, point to the way for new collaborators to get involved, invite others with specific skills.
We will discuss in detail how to write a good README file later, but for now, let's start by adding a couple of sentences about your project.
Open the file by clicking on the file name, click on the edit (pen symbol) button to start writing and scroll down to save your file, which is called "commit" in Git and GitHub (see the image below).

| ![screengrab showing how to edit a file on GitHub](../../figures/github-readme.png) |
| ------------------------------------------------------------------------------------ |
| An illustration showing how to edit files on GitHub and "commit" changes |

Every time you save your file you "commit" the proposed changes and create a new version.
A "commit message" allows you to add a comprehensive description on what is being updates.
You can learn more about commit and commit message in the [version control chapter](/version_control/01/vcs_workflow).

To create a new file, click on "create new file" button on your repository.
Similarly, to open a new file inside a new folder, start by writing the folder name followed by a forward slash, followed by the file name as shown in the image below.


| ![screengrab showing how to create files on GitHub](../../figures/github-readme.png) |
|:------------------------------------------------------------------------------------ |
| An illustration showing how to create new files and folders on GitHub                |

### Styling with markdown

Add MarkDown tutorial here of link out to the appropriate document

### Pull requests

Say person A has made changes they want to share with person B.
On GitHub Person A needs to go to person B's copy of the project and click the "New pull request" button.
From there they can indicate which of their branches they would like person B to pull changes from, and which branch they want the changes pulled to.
If person B accepts then person A's changes will be merged into their repository by GitHub.
They can discuss the request in comments, and make further commits to the request before it is accepted if necessary.

When person B is setting up the pull request GitHub will automatically check whether there would be any merge conflicts if they accept, and highlight them if there are.
These can then be resolved in further commits before the request is accepted, keeping the merge clean and painless.

Once the request is accepted GitHub will merge person A's changes into person B's online copy of the repository.
Person B

### Good practice

In your GitHub repository you should **include a license** to allow others to re-use your work legally.
GitHub makes this very easy, simply click the "Create new file" button, name it "License.md" and a drop down menu will appear offering you a selection to choose from. The legalese can seem intimidating however [this](https://choosealicense.com/) website offers a very simple mechanism to help you pick the best license for your project.

You should also **include a readme file** where you include useful information about what the project is, how to use it and how to contribute to it.
Switching between projects in your work is common, let alone that you might need to poke at your own previous projects from time to time.
This information will also assist you collaborators, and your future employer might want to check your existing GitHub projects.

There are plenty of readme templates available online, pick one you like, but here is a list of the main things a readme should include:

- The project name and what it is: This will greatly help the random prospective contributor to get an idea of the project.
Include a few key points that describe the main features of the project and what are the main features you are implementing.
This helps to quickly compare other projects with yours and to give an idea that why the project exists in the first place.
- Instructions on how to install the project: The installer might be a collaborator, someone that comes across and is interested in the project, or even you if you get a new machine and need to re-install your project.
Nevertheless, it's a total waste of both of your resources to start figuring out how to just get started with the project.
This should also include any prerequisites that will be needed to run the project.
The best thing you can do is to just write up the installation instructions when you first do them yourself, and you will quickly save hours of work in the future.
- Instructions for how to run the project and any associated tests: If you have been working on your project it may seem obvious how to run it, but this will likely not be the case for someone coming across it for the first time.
- Links to related material.
- List of authors/contributors to the project, possibly with contact information.
- Acknowledgements.

It can be a good idea to **include documents outlining a code of conduct, agreed ways of working, and contributing guidelines**, though depending on the level of detail you want to provide the latter two can also work as sections within the readme.
These documents make explicit expectations for those working on/contributing to the project, making life easier for everyone.
Similarly depending on the scope of your project you may wish to **provide templates for how contributors should make pull requests or raise issues**.

You can also **make use of one of GitHub's major features- issues**.
Anyone can raise an issue with the project and discuss it.
By making issues for any significant changes a record can be kept of the history of the project.
GitHub has a myriad of other features such a milestones and project boards which may also be of use.

In pull requests you should **clearly explain what the changes you've made are and why you made them**.
If your changes address and issue that has been raised reference it directly.
If your request fixes and issue and you include "will fix #the_issue_number >" in the pull request, if the pull request is merged it will automatically close the referenced issue, keeping the issue queue nice and clean!
This also works for using commit messages to close issues too.
--->
