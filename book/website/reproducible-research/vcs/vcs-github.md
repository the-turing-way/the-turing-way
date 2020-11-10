# Using Git commands to work on Git repositories online

As research becomes increasingly collaborative and multiple people work on the same project, it becomes difficult to keep track of changes made by others if not done systematically.
Moreover, it is time-consuming to manually incorporate the work of different participants in a project, even when all of their changes are compatible.
Hosting the project on an online repository hosting service like GitHub is beneficial to make collaborations open and effective.
If you are new to collaboration through [GitHub](https://github.com), please follow a comprehensive guide in the collaboration section.

In this section we will discuss how to use Git commands to work with online Git repository.

Please note that the commands listed in this chapter (both in the previous and this subchapter) are NOT specific to GitHub.
They are used for collaborative work on any Git repositories and to interact with any repository hosting site/servers, which can be [GitHub](https://github.com/), but also [GitLab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/) or a [self-set-up bare Git repository on a web server](https://opensource.com/life/16/8/how-construct-your-own-git-server-part-6).

For simplicity purpose, we will use GitHub as an example to explain commands that are used for interacting with Git repositories.

## Create a local copy of an online repository

So far, all Git commands introduced in this chapter concerned local, unconnected Git repositories.
In order to collaborate with others, hosting services such as GitHub can store a *clone* (a copy) of your local repository and expose it to others.
Usually, you will have a local repository and a *remote*, web-hosted repository.
Your local repository is connected to the web-based clone.
In technical terms, the web-based clone is a `remote` of the local repository. Usually, this remote is called "origin".
Having a web-based remote allows you to *push* changes of your project online, allows others to obtain their own clone of your repository (a copy of your repository to their local computer), make changes, and submit a *pull request* that allows you to integrate their changes.
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

## Link a local project on your computer to an online repository

To link a project on your computer to a new GitHub repository (preferably with the same name) you need to follow the standard workflow for creating a Git repository (described in the [version control chapter](/version_control/01/vcs_workflow)) by using the following set of commands in the terminal one by one:

```
cd <your project folder>
git init
git add .
git commit
```
Assuming that you have a GitHub repository that you want want to connect with this project, run the following command

```
git remote add origin <GitHub repository link for your project>
```

Then, *push* all the files on your computer to the online version so they match via:

```
git push -u origin master
```

You can then go on and make more commits on your computer.
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

### Pull requests

If you are working on a personal branch and meanwhile if some other changes were made in the master branch, you can *pull* those changes down to your branch using the Git command:
```
git pull origin master
```

When everyone has a copy of the project on their personal branch (checkout your branch with `git checkout branch-name`), they can *push* their changes to their branch by using the following command:

```
git push origin branch-name
```

However, if you can not directly edit the repository (when you are not an owner of admin of the project), you will be able share your work with the help of *pull requests*.
A pull request allows a contributor get their proposed changes from their personal branch or repository integrated in their master branch of the project.
It is also possible to make pull requests via the command line (see the GitLab documentation [here](https://git-scm.com/docs/git-request-pull)), but we have discussed this in detail in the collaborating with GitHub chapter in this book.

## Contributing to other projects

When you create a local copy of a repository, you only keep the versions of the files that are in the repository at the time of creating that copy.
If there are any changes made in the original repository afterwards, your copy will get out of sync out of sync.
This can lead to problems like conflicting file contents when making a pull request or merging changes from your branch to the main repository.
Therefore, when working on different branches or forks of a repository, it's a good practice to keep them updated frequently with the master repository and keep them in sync with the original repository.

### A workflow to contribute to others GitHub projects via `git`:

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
git pull
```

The git pull command combines two other commands, git fetch and git merge.
When using fetch, the resulting commits are stored as the remote branch allows you to review the changes before merging.

Similarly, if you have created more branches other than master, you can also keep them in sync with your master, once it is in sync with the upstream repository.

```
git checkout my-other-branch
git pull origin master
```

When everything is  up-to-date, you can work on your branch and commit changes.

When you are ready to push your local commits to your forked repository (origin), use the following command.

```
git push origin forked_repository
```

Now you can make a pull request!

## Good practice

Before you create a branch, make sure you have all the upstream changes from the origin/master branch.

A word of caution on the `rebase` command: While trying to keep your branches in sync, you may come across `rebase` command.
It tends to rewrite history and could be troublesome if not communicated with others working on the same branch, therefore try to avoid using `rebase` command, and instead use `pull` or `fetch`+`merge` as discussed in this section.
You can find more details about Merging vs Rebasing [here](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

## Further reading
- An article on syncing a fork of a repository to keep it up-to-date with the upstream repository can be found [here](https://help.github.com/en/articles/syncing-a-fork).
- If you wish to do it all in the browser itself, instructions to do so can be found [here](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser).
