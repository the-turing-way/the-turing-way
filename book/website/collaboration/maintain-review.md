(cl-maintain-review)=
# Maintainers and Reviewers on GitHub

## Prerequisites / recommended skill level

| Prerequisite | Importance |
| -------------|----------|
| {ref}`Experience with version control<rr-vcs>` | Helpful |

## Summary
For any open source project, one of the most challenging tasks for a new contributor is to identify ways to get involved by making online contributions to propose appropriate changes.
Contribution guidelines of open source projects outline how community members can make such a contribution, but it often does not explain how one can the project by taking up a maintainer's role.
Dedicated project maintainers from the project's core team or volunteer community often take up the role of supporting such contributions by other contributors.

This subchapter sheds light on the role and tasks of such project maintainers who manage or coordinate community discussions, mentor contributions, support resource development, help in issue triaging, and review Pull Requests or PRs on an online collaborative GitHub project.
It also provides the best practices to be used while contributing to a project as a maintainer.

### This subchapter covers:

This chapter will be particularly useful for the community members who want to provide support in maintenance and review work in _The Turing Way_  repository and or similar projects online.

The Git workflow is difficult to understand, especially when collaborating with a group of contributors for a project.
Hence, this chapter aims to guide the review processes so that all the contributions made on a GitHub project are regularly and properly done.

### This subchapter does not cover:

Please note that it is not a "how-to" guide to how to make contributions but lists the major responsibilities of a project maintainer and how these responsibilities should ideally be carried out when working in online and collaborative projects.




## Merging changes
Pull requests made by contributors can be approved or merged by maintainers after the review.
There are different ways of merging a pull request:
- *Merge pull request*: Merges all commits to base branch.
It keeps all commits made in the PR as separate and merges them as they are, through a single merge commit to the base branch.
- *Squash and merge*: Squashes all commits created in the pull request into one commit and merges them as a single commit (with the help of a merge commit) to the base branch (see this [blog for details](https://github.blog/2016-04-01-squash-your-commits/)).
- *Rebase and merge*: Rebases all commits individually to base branch (integrating changes from one branch to other) before merging.
In the prompt message, the maintainer can provide a merge message along with comments(if any) and then press the “confirm merge” button.


## What to learn next

[Community communications for open source](https://the-turing-way.netlify.app/open-source-comms/intro.html) has some relevant information for getting involved with this community-driven project.

## Further reading

* [GitHub help](https://help.github.com/en)- a great resource to know about almost everything concerning collaborating on a GitHub project.
* [Guide to Open Source](https://opensource.guide/)- Guides available related to Open Source, be it maintaining or contributing- most of the topics have been covered here.
* [An article on using Open source research tools](https://opensource.com/education/15/11/tools-analyze-collaborate-share-research)
* [A guide on Pull requests](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)
* [How to guide to workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
* [A Blog on Open source and academia](https://opensource.com/article/19/9/how-open-source-academic-work)
