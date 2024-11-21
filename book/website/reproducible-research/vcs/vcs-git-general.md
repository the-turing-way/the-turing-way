(rr-vcs-git-general)=
# General information about git

Git is a successful version control software (see [Wikipedia](https://en.wikipedia.org/wiki/Git) for detailed information).
It was created in 2005 and got rapidly adopted by software developers, especially because it is very fast and scalable. 
Its functions allow for parallel development and maintenance of large projects, like linux development.

(rr-vcs-gitpros)=
## Why everyone is using git

While developed for software, Git has been used for many different kind of projects and platforms such as GitHub, GitLab, Gogs, GitLea and others. 
These platforms brought project management tools into the Git workflow, facilitating community building around projects like the Turing Way book. 
Sometimes, users of these platform do not even know about Git. 

(rr-vcs-git-limitations)=
## Git Limitations

Git is not magic and it is good to know about its limitations.
Especially, Git works best with small text files.
Git starts to be impracticable when too many files are present, or when the repository becomes too big (1 TB is about the limit).
As a Git repository stores every version of every file that is added to it, large files that undergo regular modifications can inflate the size of a·project significantly.
In research projects, datasets often contains thousands of files and/or contain (very) large files.
While one can use Git for non-software application, one needs to plan to use specific workflows and/or additional tools to be able to use Git tools.
It is particularly problematic because everything will work fine in the beginning and it is very difficult to solve issues when the project is ongoing.
It is therefore important to plan ahead, and try to avoid big repositories.
For instance, one can split the files into different repositories and save binary files outside of Git.
There are tools allowing that while keeping git at the core of the version control (git-annex and submodules are possible technologies, see section {ref}`data version control<rr-vcs-data>` and {ref}`research projects<rr-vcs-git4research>`).



(rr-vcs-git-usecases)=
## How one uses Git

If you ever made modification of files in GitHub, you have probably used Git without even realising it.
When you push the `commit changes` button on a Git platform, Git was acting in the background to `add` the changes to the index,
`commit` them with a message, and push it to the repository.

Several software allows to use Git without using the command line, locally.
Here is a non-exhaustive list of software one can also use, please refer to their own documentation:

- [RStudio](https://posit.co/products/open-source/rstudio/)
- [Sourcetree](https://www.sourcetreeapp.com/)
- [Gitkracken](https://www.gitkraken.com/)
- [Visual Studio Code](https://en.wikipedia.org/wiki/Visual_Studio_Code)

Even if you are using a terminal you don't have to use the git command line interface you could use a TUI (terminal user interface) for git such as [lazygit](https://github.com/jesseduffield/lazygit) or [gitui](https://github.com/extrawurst/gitui).

In many cases, one still needs to use the command lines for complex matters, and we present the main Git functions usage in this book (see {ref}`Getting Started with Git<rr-vcs-git>`). 

(rr-vcs-git-understanding)=
## Understanding git

Git's role is different from an autosave feature, it is not a tool for capturing whatever random changes you have made since you last started to work on a project.
Git is a tool for authoring a coherent narrative history of your project, in convenient discrete increments called commits.
Commits should be made with deliberation, considering: 'Is this unit of change a useful one to record in the project history?'
Commits should be granular, with commit messages emphasising why a change was made with perhaps some element of summary description of the changes.

This section aims to provide a high level conceptual understanding of how git works so you have a good working mental modal of git so it is easier for you to reason about.
This comic illustrates that it is is common to learn the basic motions of git without really getting an understanding of it.
The next sections will go into the specific actions and commands that you might use to perform common operations in git.

```{figure} ../../figures/XKCD-1597-git.*
---
name: XKCD 1587 'git' 
alt: >
  One stick figure gestures to a laptop on a desk and say to two others,
  one with a ponytail and the other with short hair: 
  "This is git. It tracks collaborative work on projects through a beautiful distributed graph theory model."
  The stick figure withthe pony tail replies:
  "Cool how do we use it?"
  The stick figure by the laptop responds:
  "No idea. Just memories these shell commands and type them to sync up.
  If you get errors, save your work elsewhere, delete the project, and download a fresh copy."
---
Image Credit [XKCD 1579 'git'](https://xkcd.com/1597) under a [CC-BY-NC 2.5 licence](https://creativecommons.org/licenses/by-nc/2.5/deed.en)
```
At the core of git is a data structure called a hash tree, what is this?

```{figure} ../../figures/git-hash-function-only.*
---
name: Hash Function 
alt: >
  A hash symbol followed by the letter f preceeds a set of curly braces around some files with lines of text on them.
  An equal sign indicates that this is equal to a seemingly random string of four characters and an elipsis.
  Implying that the random looking characters are some function of the contents of the files.
  The same thing is repeated on a second line but a line in one of the files is highlighted showing it has changed.
  The string of characters to which the function is equal has also now changed.
  Implying a change in the contents of the files alters the seemingly random characters.
---
```

A hash function of some file or collection of files produces a statistically unique fixed length output.
Any change to the files results in a different hash value.

```{figure} ../../figures/git-hash-tree-only.*
---
name: Hash Tree
alt: >
  A hash symbol followed by the letter f preceeds a set of curly braces around an orange file.
  An equal sign indicates that this is equal to a seemingly random string of four orange characters.
  Next to this is an orange circle.
  An arrow points from the orange random characters to the a similar line above where the orange characters are repeated,
  this time within the braces along with a turquoise file.
  The hash function on this line is shown to be equal to a string of turquoise characters.
  Next to them is a turquoise circle conected to the orange circle below it by a line.
  This repeats with a third hash function and circle on the line above this time with the turquoise characters added to a blue file as the input to the hash function.
  In summary: Three hash functions where the output of the previous one is added to the input of the next,
  and a representation of this as three circles conntected by lines.  
---

```

A hash tree includes the hash of its 'parent' in the content used to generate its own hash.
This way all nodes know their 'parent' and any changes to their 'parent' or its 'parent' recursively would result in a change to their hash.
This means that the tree can always be reassembled from its individual components, in this case of git 'commits'.
You always know where any changes diverged in the history making it great for ensuring things stay consistent even when working asynchronously.

That's the basics of what the structure that underlies git is and why it's useful in theory, now how is this used in practice?

```{figure} ../../figures/git-tree-overview.*
---
name: git tree 
alt: >
  Diagramatic representation of a git history in a sketch-like art style.
  A series of circles containing seemingly random letters and numbers, their hashes, are  connected by lines starting at the bottom of the page going up.
  The second circle up is a branch point, the tree continues up with two more circles on each branch. The tip of each branch has a label tied around it, one labeled 'main' and the other 'dev'. The labels are tied loosly so they can slide to the tip of the branch as more circles, representing commits, are appended to the branch.
  At the base of the tree another label reading 'tag' is padlocked to one of the commits, illustrating that tags in git are associated with a fixed commit, unlike branch labels.
  A box labeled 'checkout dev' is drawn around the tip of the branch labeled 'dev', illustrating the act of checking out a branch.
  This box points to another labeled 'edit'  in it are representations of some files with lines in them shown to have been changed by a change in their colour.
  This box points to a further box labeled 'stage' where some of the changes have been selected and others not, shown by their different colours.
  This illustrates the staging of the changes that you intend to commit.
  The box labeled 'stage' points to an arrow emerging from the tip of the branch labeled 'dev' pointing to the word commit.
  A box labeled 'checkout 04z' is drawn around a commit in the graph with the hash 04z.
  It points to another box containing a file labeled 'View' showing a file from this point in the git history. 
---
```

A branch name in git is a label for a leaf on the tree, it is always pointed to the tip of a branch and slides along the branch so that is always refers to a leaf as new commits are added.
In contrast a tag is locked to a specific commit, referring to a fixed point in the tree.
A tag simply provides a human readable name for a specific commit, that does not require searching through commit messages.

The directory into which you have cloned a git repository is like a window onto the git tree.
Checking out a branch or commit moves that window to a different point in the tree.

Checking out a commit is intended for viewing only, you should be on a branch if you want to add new things.
You will find that your repository is described a being in a 'headless' state if you checkout a commit as git does not now have a branch to add any new changes to.
You can checkout a commit and create a new branch starting from that point in the history if you want create a new diverging history.

By default you only have one window onto the tree, the directory that contains your git repository.
This means that when you checkout a different part of the tree your working directory needs to be 'clean', meaning free from uncommitted changes.
It can be inconvenient to have to have a clean working directory to change what you have checked out if you don't yet have a unit of work you want to commit be need to change task and work on some other part of the project.
git has two mechanisms for dealing with this:

- Worktrees that let you open multiple windows on the tree by having different branches checked out in different directories (without having to make another copy of the repo).
- Stashing - making a temporary commit that you can 'pop' the changes back out of once you have returned to branch to which you intended to add them

When getting ready to create a commit there you can select which of the changes that you have made you want to include in the commit.
This is called 'staging' the changes.
This is a step where a user interface to git can be especially useful as they can show you what changes you have made add which you are proposing to include in your next commit.

When bringing divergent branches back together in git, a process called merging, there a some different approaches that you can take.

```{figure} ../../figures/git-merge.*
---
name: git merge 
alt: >
  It points to another box containing a file labeled 'View' showing a file from this point in the git history. 
---
```
Merging the branches creating a new 'merge commit'.

`7JA...04Z + 4GW...04Z` 

Or performing a 'fast-forward merge' effectively 'cherry picking' the commits from your development branch and rebasing them on the tip of your main branch.
Because this changes the parent commit of the these new commits they get new hash values.
This effectively replays the changes made in the development branch starting from the last change in main branch instead of starting from where they originally diverged.

`7JA...04Z + WN7...7JA`

This different order of operations can produce different end results but the main difference is in the structure of the history you are left with.
A merge commit retains the two independent histories, the fast forward yields a nice linear history.

In summary: Most everything in git is some kind of operation on this tree.

- Preparing to add to the tree
	- Staging changes
- Editing the tree
	- Merges, cherry picking, re-basing
- Labelling or naming features of the tree
	- Branches & Tags
- Viewing points on the tree
	- Checkouts, Worktrees



