## Version Control for data

Version controlling the components of evolving projects can help to make work more organized, efficient, collaborative, and reproducible.
Many scientific projects, however, do not only contain code, manuscripts, or other small sized files, but also larger files such as (input) data or analysis results.
In order to have comprehensive and reproducible scientific projects, it is beneficial if these contents are version controlled, just as project's code or manuscript.
Because just as code or scientific manuscripts, data can change, too, and in order to be reproducible, scientific projects need to keep track of which subset or version of data an analysis or result is based on.
Depending on the size of the data and the modifications it undergoes, however, version control tools such as Git may not be suitable.


### Why is version controlling data relevant

Some scientists think of the data they use for analysis as static:
Once it is acquired, it does not change, but serves as input for their analyses and the backbone of their scientific results.
However, data is only rarely invariant.
For example, throughout a scientific project, data sets can be extended with new data, reorganized to new naming schemes or file hierarchies, or updated when errors are detected and fixed.
These dynamic processes are good and beneficial for science as they ensure that data is usable and up-to-date, but they can be detrimental if they aren't properly documented.
If one bases their research on a data set, develops their code against this data set, and computes and communicates their results from the data, all aspects of the project are at risk should the underlying data change without version control.
If data sets are extended with new data or fixed data files under new file names, the results of an analysis may be outdated.
If original data files are renamed to reflect underlying changes (just as in the example of `version_1.py` and `version_2.py`), the data can become unorganized and code may need to be adjusted to not break.
And if original data gets replaced with new data with no version control in place, the original results of the analysis may not reproduce.
Therefore, version controlling data and other large files just as code or manuscripts can help to ensure the reproducibility of projects and help to capture the provenance of results, namely "which precise subset and version of data did this result originate from?".


### What is difficult about version controlling data?

As long as the files to version control as small in size, tools such as [Git](https://git-scm.com/) are appropriate.
Therefore, if research involves data that can be stored a few `csv` files, Git and similar tools can handle it well.
But if you work, share, and collaborate on large, potentially [binary](https://en.wikipedia.org/wiki/Binary_file) files, you need to think about ways to version control this data with specialized tools.
This is because most version control tools - among them Git - are not well suited to handle large [binary](https://en.wikipedia.org/wiki/Binary_file) data, such as many scientific data formats.
As a Git repository stores every version of every file that is added to it, large files that undergo regular modifications can inflate the size of a·project significantly.
If others try to clone your repository or fetch/pull updates from it, it will take longer to do this the more large files it contains and the more modifications are done to these large files.

What is especially inconvenient is that repository hosting services such as GitHub impose maximum file sizes on users (at least in their free versions).
For example, if a single file in your repository exceeds 100MB, you will not be able to push this file to a GitHub repository.
And if a large file was accidentally added to a repository, removing the file from the repository can be tedious, as this file needs to be [purged](https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository).
These shortcomings can make version controlling files tedious and slow, impede collaborations on repositories with large data, and prevent data or projects with data from being shared on platforms like GitHub.

### Tools for version controlling data

A number of tools are available to handle version controlling and sharing large files.
Most of them integrate very well with Git and extend Gits functionality or the repository's capabilities to version control large files.
With these tools, large data can be added to a repository, version controlled, reverted to previous states, or updated and modified collaboratively, just as small-sized files with Git.

###### Git LFS
One of these tools is [Git LFS](https://git-lfs.github.com/).
It comes with a command line extension to Git and allows you to treat files of any size alike, using standard Git commands.
A major shortcoming, however, is that Git LFS is a _centralized_ solution.
Large files are not distributed, but stored on a remote server.
This usually requires setting up your own server or paying for a service - which can make it very inaccessible.

###### git-annex
An alternative is [git-annex](https://git-annex.branchable.com/), a distributed system that can manage and share large files independent from a central service or server.
`git-annex` manages all file _content_ in a separate directory in the repository (`.git/annex/objects`, the so-called _annex_).
It places only file _names_ and some metadata into version control by Git.
When a Git repository with an annex is pushed to a web-hosting service such as GitHub, the contents stored in the annex are not uploaded.
Instead, they can to be pushed to a storage system (such as a web server, but also third party services such as Dropbox, Google Drive, Amazon S3, box.com, and many more).
If a repository with an annex is cloned, the clone will not contain the _contents_ of all annexed files by default, but display only file names.
This makes the repository small, even if it tracks many hundreds GBs of data, and cloning fast, while file contents are stored in one or more free or commercial external storage solutions.
On demand, any file content can then be obtained with a `git-annex get` command from the external file storage.

###### DataLad
Yet another tool, [DataLad](https://www.datalad.org/), builds up on Git and git-annex.
Just as `git-annex` it allows to version control data and share it via third party providers, but tries to simplify and extend its functionality.
In addition to sharing and version controlling large files, it allows recording, sharing, and using software environments, recording and re-executing commands or data analyses, and operate seamlessly across a hierarchy of repositories.



### An interview with Adina on DataLad

**Kirstie**: Hi Adina, thank you for contributing the chapter on version control for data!
I know you are a developer for DataLad, and I'm excited to learn more about the project.
Can you start by telling me who you are and what you are working on?

**Adina**: Hey Kirstie, thanks a lot for providing a space for the topic of version controlling data!
I'm a PhD student in neuroscience, and I am part of the lab that develops DataLad.
Apart from working on neuroscientific questions, I also work on data management challenges that are typical for my field, such as "I have 300GB of data, how can I possibly version control or share this?", or "How can I link my analyses to the version of data I have used?".
As a neuroscientist I'm privileged to work in a field with many fantastic, open data sets, but it is also challenging to handle, share, and keep track of data that can easily be several hundred GB in size.

**Kirstie**: Fab, so how does DataLad help with your work?

**Adina**: DataLad lets me version control and share data of any size, and I use this to attach data in precise versions to code and manuscripts I create.
When doing data analyses and the underlying data is modified, I can update my repositories and recompute my scripts.
This helps me to assess if my results are replicable.
And just as Git, it is a great memory aid for remembering what I did to my data.
It has some cool functions for provenance capture, and I can just check my Git history to find out from which data a particular figure was created, for example.


**Kirstie**: Cool, so what makes DataLad better suited for what you do than other tools that version control data?

**Adina**: I personally like DataLad, because on top of the functionality that Git and `git-annex` provides, it makes linking and reusing modular parts of my research easy.
When I work on an analysis, I publish the data, the code + results, and the manuscript as separate, version controlled Git repositories to GitHub.
But these repositories are linked together so that someone who reads my manuscript could backtrace every step that was undertaken to create this result, back to the original data.
I can share my analysis on GitHub and can have data, code, and even software environments all together, to allow others to reproduce my results, and I find that to be a very powerful feature.

TODO: figure on Provenance by Sam

**Kirstie**: And as a part of the DataLad team, how do you contribute to the software?

**Adina**: My main motivation is to make the software accessible for users of all backgrounds.
If scientists receive no formal training in version control or research data management, it can be hard to work reproducibly.
I believe if software is easy to use and well-documented it can help scientists to do better science.
Software-wise, I therefore work on help-features, and documentation-wise, I work on tutorials that are suitable to users independent of skill level or background.

**Kirstie**: What is the journey of DataLad and how did you get to be a part of it?

**Adina**: DataLad was originally created by Michael Hanke and Yarik Halchenko in 2014.
They wanted to have a tool that allowed them to install data just as easily as software packages and keep track of how data changes.
`git-annex` already existed at this point, but they wanted to build up on it to make it easier to use.
Over the years, the tool became a joint version control and data management tool to facilitate data sharing, revision tracking, and reproducible computations.
I joined the lab almost two years ago as a Master's student in Clinical Psychology, excited for open and reproducible science, but a complete newbie technology-wise:
I had never heard of version control, no programming experience, and the idea that data is dynamic was insightful but completely new to me.
Naturally, when I started using DataLad, I was completely overwhelmed.
Luckily, there were many people to help me get started and give me the necessary background information.
I know, however, that such a learning environment is not the default, so when I started my PhD, I actually created the resource that I would have needed to get started as a student: [The DataLad Handbook](http://handbook.datalad.org)

**Kirstie**: Thanks a lot for telling us about this tool. Where can people find out more, if they want?

**Adina**: I would point them to [The Datalad Handbook](http://handbook.datalad.org).

