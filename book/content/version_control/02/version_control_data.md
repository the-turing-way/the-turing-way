## Version Control for data

Version controlling the components of evolving projects can help to make work
more organized, efficient, collaborative, and reproducible.
Many scientific projects, however, do not only contain code, manuscripts, or
other small sized files, but also larger files such as (input) data or analysis
results.
Because data can change just as code or scientific manuscripts, scientific
projects can improve their chance to stay reproducible if they keep track of
which subset or version of data an analysis or result is based on.

### Why is version controlling data relevant

Some scientists think of the data they use for analysis as static:
Once it is acquired, it does not change, but serves as input for their analyses
and the backbone of their scientific results.
However, data is only rarely invariant.
For example, throughout a scientific project, data sets can be extended with new
data, reorganized to new naming schemes or file hierarchies, or updated when
errors are detected and fixed.
These dynamic processes are good and beneficial for science as they ensure that
data is usable and up-to-date, but they can be detrimental if they aren't
properly documented.
If a dataset that is the basis for computing a scientific result changes without
version control, reproducibility can be threatened:
Results may become invalid, or scripts that are based on file names that change
between versions can break.
Especially if original data gets replaced with new data with no version control
in place, the original results of the analysis may not reproduce.
Therefore, version controlling data and other large files in a similar way to
version controlling code or manuscripts can help to ensure the reproducibility of
projects and help to capture the provenance of results, namely "which precise
subset and version of data did this result originate from?".
Together will all other components of a research project, data identified
in precise versions is part of the of a research result.

![Provenance on which data in which version was underlying which computation is crucial for reproducibility](../../figures/Provenance.jpg)

### What is difficult about version controlling data?

Depending on the size of the data and the modifications it undergoes, version
control tools such as Git may not be suitable.
As long as the files to version control as small in size, tools such as
[Git](https://git-scm.com/) are appropriate.
Therefore, if research involves data that can be stored in a few `.csv` files,
Git and similar tools can handle it well.
But if you work, share, and collaborate on large, potentially
[binary](https://en.wikipedia.org/wiki/Binary_file) files (such as many
scientific data formats), you need to think about ways to version control this
data with specialized tools.
This is because most version control tools - among them Git - are not well
suited to handle large binary data.
As a Git repository stores every version of every file that is added to it,
large files that undergo regular modifications can inflate the size of a·project
significantly.
If others try to clone your repository or fetch/pull updates from it, it will
take longer to do this the more large files it contains and the more
modifications are done to these large files.
What is especially inconvenient is that repository hosting services such as
GitHub impose maximum file sizes on users (at least in their free versions).
For example, if a single file in your repository exceeds 100MB, you will not be
able to push this file to a GitHub repository.
And if a large file was accidentally added to a repository, removing the file
from the repository can be tedious, as this file needs to be
[purged](https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository).
These shortcomings can make version controlling files tedious and slow, impede
collaborations on repositories with large data, and prevent data or projects
with data from being shared on platforms like GitHub.

### Tools for version controlling data

A number of tools are available to handle version controlling and sharing large
files.
Most of them integrate very well with Git and extend Gits functionality or the
repository's capabilities to version control large files.
With these tools, large data can be added to a repository, version controlled,
reverted to previous states, or updated and modified collaboratively, and even
shared via GitHub, just as small-sized files with Git.

###### Git LFS
One of these tools is [Git LFS](https://git-lfs.github.com/).
It comes with a command line extension to Git and allows you to treat files of
any size alike, using standard Git commands.
A major shortcoming, however, is that Git LFS is a _centralized_ solution.
Large files are not distributed, but stored on a remote server.
This usually requires setting up your own server or paying for a service - which
can make it very inaccessible.

###### git-annex
An alternative is [git-annex](https://git-annex.branchable.com/), a distributed
system that can manage and share large files independent from a central service
or server.
`git-annex` manages all file _content_ in a separate directory in the repository
(`.git/annex/objects`, the so-called _annex_).
It places only file _names_ and some metadata into version control by Git.
When a Git repository with an annex is pushed to a web-hosting service such as
GitHub, the contents stored in the annex are not uploaded.
Instead, they can be pushed to a storage system (such as a web server, but also
third party services such as Dropbox, Google Drive, Amazon S3, box.com, and
[many more](https://git-annex.branchable.com/special_remotes/)).
If a repository with an annex is cloned, the clone will not contain the _contents_
of all annexed files by default, but display only file names.
This makes the repository small, even if it tracks many hundreds GBs of data,
and cloning fast, while file contents are stored in one or more free or commercial
external storage solutions.
On demand, any file content can then be obtained with a `git-annex get` command
from the external file storage.

###### DataLad
Yet another tool, [DataLad](https://www.datalad.org/), builds up on Git and
git-annex.
Just as `git-annex` it allows to version control data and share it via third party
providers, but tries to simplify and extend its functionality.
In addition to sharing and version controlling large files, it allows recording,
sharing, and using software environments, recording and re-executing commands or
data analyses, and operate seamlessly across a hierarchy of repositories.
