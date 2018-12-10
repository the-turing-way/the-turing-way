# Version Control



## Why would you use version control software and hosting (such as GitHub)?


From [here](https://guide.esciencecenter.nl/best_practices/version_control.html). **Creative Commons Attribution 4.0 International License**

- **Reproducability** By using version control, you never lose previous versions of the software. This also gives you a log of changes and allows you to understand what happened.
- **Backup** Version control is usually pushed to an external a shared server, which immediately provides a backup.
- **Integration** Version control software and host makes it more easy to integrate with other software that support modern software development, such as testing (continuous integration ,automatically run tests, build documentation, check code style, integration with bug-tracker, code review infrastructure, comment on code).
- **Easier to collaborate** Version control makes it easier to work on the same code simultaneously, while everyone still has a well defined version of the software (in contrast to a google-docs or shared file system type of system). Moreover, version control hosting websites such as Github provide way to communicate in a more structed way, such as in code reviews, about commits and about issues.

--------




## Git

### Commits & commit messages

### Commits

From [here](http://who-t.blogspot.com/2009/12/on-commit-messages.html). **No License, but blog still active, could reach out**

A commit should contain exactly one logical change. A logical change includes adding a new feature, fixing a specific bug, etc. If it's not possible to describe the high level change in a few words, it is most likely too complex for a single commit. The diff itself should be as concise as reasonably possibly and it's almost always better to err on the side of too many patches than too few. As a rule of thumb, given only the commit message, another developer should be able to implement the same patch in a reasonable amount of time.

Don't do:

- Per-file commits. More often than not a logical change affects more than one file and it should not be split up into two commits.
- Two changes in one patch. Something like "Fixed bug 2345 and renamed all foo to bar". Unless bug 2345 required the renaming, fixes whould be split it up into multiple patches. Others may have to take one of those bug fixes and apply it to a stable branch but not the other one. Picking bad patches apart into useful chunks is one of the most time-consuming and frustrating things I've done since it doesn't actually add any value to the project.
- Whitespace changes together with code changes. Needle in a haystack is a fun game, but not when you're looking at patches. It's a great way to introduce bugs, though because almost no-one will spot the bug hidden in hundreds of lines that got reindented for fun and profit.
- The ever-so-lovely code drops. Patches with hundreds of lines of code to dump a new feature into the code while at the same time rewriting half the existing infrastructure to support this feature. As a result, those hundreds of lines of code need to be reviewed every time a bug is discovered that is somehow related to that area of code.
It's easier and less time consuming to first rework the infrastructure one piece at a time, then plug the new feature on top. As a side-effect, if a project relies on code dumps too often it's discouraging outside developers. Would you like to contribute to a project where the time spent filtering the signal from the noise outweighs the actual contribution to the code?
- Unrelated whitespace changes in patches. A reviewer needs to get the big picture of a patch into their brains. Whitespace-only hunks just confuse, a reviewer has to look extra hard to check if there's a real change or whether it can be ignored. That's not so bad for empty lines added or removed,it's really bad for indentation changes.

----

#### Commit messages


From [here](https://guide.esciencecenter.nl/best_practices/version_control.html). **Creative Commons Attribution 4.0 International License**

Commit messages are the way for other developers to understand changes in the codebase. In case of using GitHub flow model, commit messages can be very short but pull request comments should explain all the changes. It is very important to explain the why behind implementation choices.

-----

From [here](http://who-t.blogspot.com/2009/12/on-commit-messages.html). **No License, but blog still active, could reach out**

Any software project is a collaborative project. It has at least two developers, the original developer and the original developer a few weeks or months later when the train of thought has long left the station. This later self needs to reestablish the context of a particular piece of code each time a new bug occurs or a new feature needs to be implemented. Re-establishing the context of a piece of code is wasteful. We can't avoid it completely, so our efforts should go to reducing it to as small as possible. 

A good commit message should answer three questions about a patch:

- **Why is it necessary?** It may fix a bug, it may add a feature, it may improve performance, reliabilty, stability, or just be a change for the sake of correctness.
- **How does it address the issue?** For short obvious patches this part can be omitted, but it should be a high level description of what the approach was.
- **What effects does the patch have?** (In addition to the obvious ones, this may include benchmarks, side effects, etc.)

These three questions establish the context for the actual code changes, put reviewers and others into the frame of mind to look at the diff and check if the approach chosen was correct. A good commit message also helps maintainers to decide if a given patch is suitable for stable branches or inclusion in a distribution.

A patch without these questions answered is mostly useless. The burden for such a patch is on each and every reviewer to find out what the patch does and how it fixes a given issue. Given a large number of reviewers and a sufficiently complex patch, this means many man-hours get wasted just because the original developer did not write a good commit message. Worse, if the maintainers of the project enforce SCM discipline, they will reject the patch and the developer needs to spend time again to rewrite the patch, reviewers spend time reviewing it again, etc. The time wasted quickly multiplies and given that a commit message only takes a few minutes to write, it is simply not economically viable to omit them or do them badly. 

Don't describe the code, describe the intent and the approach. And keep the log in a present tense.


-----
By [Thom Holwerda](http://www.osnews.com/story/19266/WTFs_m). **Says anyone can do whatever, attribution nice but not compulsory**

*Maybe include this somewhere else but have it somewhere*

![wtf_per_min](http://www.osnews.com/images/comics/wtfm.jpg)



## Github
