## Merge conflicts

### The problem

When changes to made to the same file on different branches sometimes those changes may be incompatible.
This most commonly occurs in collaborative projects, but it happens in solo projects too.
Let's say there's a project and it contains a file with this line of code:

```
print('hello world')
```

Lets say one person, on their branch, decides to pep it up a bit and changes this line to:

```
print('hello world!!!')
```

while someone else on another branch instead decides to change `print('hello world')` to:

```
print('Hello World')
```

They continue doing work on their respective branches and eventually decide to merge.
Their version control software then goes through and combines their changes into a single version of the file, *but* when it gets to the hello world statement it doesn't know which version to use.
This is a merge conflict: incompatible changes have been made to the same file.

### The solution

When a merge conflict arises it will be flagged during the merge process.
Within the files with conflicts the incompatible changes will be marked so you can fix them:

```
<<<<<<< HEAD
print('hello world!!!')
=======
print('Hello World')
>>>>>>> master
```
`<<<<<<<`: Indicates the start of the lines that had a merge conflict.
The first set of lines are the lines from the file that you were trying to merge the changes into.

`=======`: Indicates the break point used for comparison.
Breaks up changes that user has committed (above) to changes coming from merge (below) to visually see the differences.

`>>>>>>>`: Indicates the end of the lines that had a merge conflict.

### How to do it

You resolve a conflict by editing the file to manually merge the parts of the file that Git had trouble merging.
This may mean discarding either your changes or someone else's or doing a mix of the two.
You will also need to delete the `<<<<<<<`, `=======`, and `>>>>>>>` in the file.
So in this project the users may decide in favour of one `hello world` over another, or they may decide to replace the conflict with:

```
print('Hello World!!!')
```

Once you have fixed the conflicts commit the new version.
You have now resolved the conflict.
If, during the process, you need a reminder of which files the conflicts are in you can use `git status` to find out.

If you find there are particularly nasty conflicts and you want to abort the merge you can using:
```
git merge --abort
```

### Good practice

Before you start trying to resolve conflicts **make sure you fully understand the changes and how they are incompatible**. If you do not you risk making things more tangled.
Once you do and you go about fixing the problem **be careful, but do not be afraid**; the whole point of version control is your past versions are all safe.
Nevertheless merge conflicts can be intimidating to resolve, especially if you are merging branches that diverged a great many commits ago which may now have many incompatibilities.
This is why it is good practice to **merge other's changes into your work frequently**.

There are **tools** available to assist in resolving merge conflicts, some are free, some are not.
Find and familiarise yourself with one that works for you.
Commonly used merge tools include [KDiff3](http://kdiff3.sourceforge.net/), [Beyond Compare](https://www.scootersoftware.com/), [Meld](http://meldmerge.org/), and [P4Merge](https://www.perforce.com/products/helix-core-apps/merge-diff-tool-p4merge).
To set a tool as your default do:

```
git config --global merge.tool name_of_the_tool
```

and launch it with:

```
git mergetool
```

Fundamentally the best way to deal with merge conflicts is to, so far as is possible, **ensure they do not happen in the first place**.
You can improve your odds on this by **keeping branches clean and focused on a single issue, and involving as few files as possible**.
Before merging make sure you know what's in both branches, and if you are not the only one that has worked on the branches then **keep the lines of communication open** so you are all aware of what the others are doing.

