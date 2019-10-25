## Comparing versions

### The problem

At some point it is likely you will need/want to compare versions of a project, for example to see what version was used to generate a certain result.

### The solution

In short: `git diff`.

Diffing is a function that takes two input data sets and outputs the changes between them.
`git diff` is a multi-use Git command that when executed runs a diff function on Git data sources.
These data sources can be commits, branches, files and more.

### How to do it

By default `git diff` will show you any uncommitted changes since the last commit.
If you want to compare two specific things the syntax is

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

### Good practice

**Use it**.
With a little familiarity `git diff` becomes an extremely powerful tool you can use to track what files have changed and exactly what those changes are.
This is extremely valuable for unpicking bugs and comparing work done by different people.
Be careful to **understand what exactly is being compared** and where possible **only compare the relevant files** for what you are interested in to avoid large amounts of extraneous information.

