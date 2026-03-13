(pd-sdpw-sensitive-files)=

# Keeping sensitive files secure

You will often have files that you do not want Git to add to your repository (or even show as being [untracked](https://howtogit.archive.pieterdedecker.be/concepts/types-of-changes.html)).
These are typically files that are automatically generated (for example `.log` files); however, they may also be files that contain sensitive information.
In such cases, you can use [`.gitignore`](http://git-scm.com/docs/gitignore).

## `.gitignore`

`.gitignore` is not an explicit command.
Instead, it is a plain text file that tells Git which files to ignore.
Below is an example of what a `.gitignore` file might look like:

```
# ignore the file doc/patient_ids.txt
doc/patient_ids.txt

# ignore the file doc/patient_notes.txt, but not doc/anonymised/patient_notes.txt
doc/*.txt

# ignore all .pdf files in the "sensitive/"-directory as well as any of its subdirectories
sensitive/**/*.pdf
```
Each line in the `.gitignore` file specifies a pattern.
These patterns are then checked against the file names in your repository, to determine which of them should be ignored. 

The following rules for writing `.gitignore` file patterns can be found in the [Git Pro book](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring):

* Blank lines or lines starting with # are ignored.
* [Standard glob patterns](https://pymotw.com/2/glob/) work, and will be applied recursively throughout the entire working tree.
* You can start patterns with a forward slash (/) to avoid recursivity.
* You can end patterns with a forward slash (/) to specify a directory.
* You can negate a pattern by starting it with an exclamation point (!).

GitHub also maintains [a collection of .gitignore templates](https://github.com/github/gitignore) to help you get started.

### Creating a `.gitignore` file

To create a `.gitignore` file, open a new file in a text editor of your choosing (for example TextEdit), name the file `.gitignore` (including the `.` at the beginning), and save it in your repository.
Alternatively, you can create a `.gitignore` file through the terminal by first navigating to your repository and then running the command `touch .gitignore`.

To double check that your `.gitignore` file is working as you intended, and the correct files are being ignored, you can run the command `git status --ignored`, which will generate a list of all ignored files.

### Ignoring a file that has already been committed

`.gitignore` only works on files that are untracked.
Files that are already tracked by Git (that is, files that has previously been staged or committed) will not be ignored.
It is therefore often a good idea to create a `.gitignore `file when you set up a new repository, so that you do not accidentally commit files that you do not want to.

It is, nevertheless, possible to ignore files that are already tracked by Git.
To do this, you will first need to delete the file from your repository and then add a new rule to your `.gitignore` file. 

### Committing a file that has previously been ignored

Sometimes, you may want to ignore all but one file that follows a general pattern.
In these instances, you can either 1) force an ignored file to be committed by adding `-f` (or `--force`) when you perform `git add` or 2) define an exception to the pattern within the `.gitignore` file (see example `.gitignore` file above).

### Having multiple `.gitignore` files (and rules)

In most cases (or at least in the simplest of cases), your repository will have a single `.gitignore` file in its root directory.
It is, however, possible to have multiple `.gitignore` files within subdirectories of the same repository.
In such cases, the rules within the `.gitignore` file will only be applied to the subdirectory within which it is located.
This means that different `.gitignore` rules can be applied across the same repository.

(pd-sdpw-sensitive-files-github)=
# What do you do if you inadvertently expose sensitive data on GitHub?

Sometimes - no matter how careful we try to be - we might inadvertently expose sensitive data on GitHub.
Unfortunately, it is not as easy as you might think to remove this data again.

Say that you mistakenly commit a file containing sensitive data to your GitHub repository.
Simply removing the file from the repository, or indeed deleting the entire repository, will not fix the problem, as...

> "*commits may still be accessible in any clones or forks of your repository, directly via their SHA-1 hashes in cached views on GitHub, and through any pull requests that reference them*" [- GitHub Docs: Removing sensitive data from a repository](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
> 

(pd-sdpw-sensitive-files-resources)=
## Further Resources

For more information about`.gitignore`, please check out the following resources:

* Git `.gitignore` [documentation](http://git-scm.com/docs/gitignore)
* Pro Git book's section on [ignoring files](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring)
* GitHub Docs's section on [ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
* Atlassian's [tutorial on `.gitignore`](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)
* freeCodeCamp's blog post [*Gitignore Explained: What is Gitignore and How to Add it to Your Repo*](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/)
* Linuxize's blog post on [*Ignoring Files and Directories in Git (.gitignore)*](https://linuxize.com/post/gitignore-ignoring-files-in-git/)
