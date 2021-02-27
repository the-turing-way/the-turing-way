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

## Project Maintenance

An open source project allows many people to make contributions in the form of [issues](https://help.github.com/en/github/managing-your-work-on-github/about-issues) and [pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).
Community members can also perform [reviews](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews) and provide feedback [comments](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request) on the ideas and changes which they or others have suggested.
These ideas and discussions lead to a better quality of resources that are developed collaboratively and bring new perspectives regarding a particular feature.
Such a review process is a common practice in small tech companies or start-ups where different teams work together to develop high-quality production level code or resources.
The major role of a maintainer is to provide support with keeping the existing code updated by keeping track of new contributions.
Whenever a new feature is added or a new idea is proposed in a project, the corresponding changes must be made in relevant resources in the project and the documentation.
It requires [opening](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue),[deleting](https://help.github.com/en/github/managing-your-work-on-github/deleting-an-issue) and [linking](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue) important issues, [reviewing](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/reviewing-proposed-changes-in-a-pull-request), [labelling](https://help.github.com/en/github/managing-your-work-on-github/labeling-issues-and-pull-requests), [changing the stages](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/changing-the-stage-of-a-pull-request), [merging](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/merging-a-pull-request) and [closing](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/closing-a-pull-request) important pull requests.
A common understanding of version control systems, [markdown](https://guides.github.com/features/mastering-markdown/) and open source [workflow](https://guides.github.com/introduction/flow/) helps to a great extent in carrying out all these tasks.

## Ownership and Permissions
In any team or organisation owned project, there are different contributors.

Owners of a project are individuals or teams who generally start a project, or join it at the time of project creation with a defined vision and goals.
The owners have the right to give different [levels of permission](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization) to outside contributors.

In Github, there are five levels of permissions: read, triage, write, maintain, and admin.
Readers are non-code contributors who are read the content or join discussions on GitHub issues.
With triage permission, contributors can manage issues and pull requests without write access.
Write permission allows contributors to push changes to the project.
Maintain permission is for project managers but have no access to sensitive or destructive actions (such as project deletion).
Admins are people who have full access to the project, including sensitive and destructive actions, and are responsible for granting permission to make other contributors.
These roles are often defined in a project file such as a [CODEOWNERS file](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners) or a Ways of Working file (see _The Turing Way_'s [Ways of Working](https://github.com/alan-turing-institute/the-turing-way/blob/master/ways_of_working.md) as an example).
These files provide insight into the core project team and members responsible for maintenance roles in the project.

In this chapter, anyone with triage, write and maintain permission is referred to as maintainers.
Maintainers are involved with creating issues and pull requests whenever required.
They keep the codebase or project updated and help in reviewing contributions.
They can often approve and merge pull requests.
They can also request reviews from someone else.

*For more information on permission level, please see this [documentation on GitHub](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization).*

## Reviewing process
In a project or codebase, a set of changes must be reviewed before merging it to the main repository.
If the project is co-owned by many people, the review process handled by [code review assignment](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/managing-code-review-assignment-for-your-team) in which certain members of the team are assigned this task.
Reviewers are often automatically suggested on GitHub pull requests based on a similar activity by other members on the same or different files in the project.
However, often a project managers request other maintainers for the review of a particular pull request based on their availability, willingness, or expertise.

The assigned or willing maintainers can review the pull request by checking the [changes locally](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/checking-out-pull-requests-locally) or on the online repository and suggest changes required.
When the review process is completed, the reviews can be approved without any change, or [with required changes](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/approving-a-pull-request-with-required-reviews) or [dismissed](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/dismissing-a-pull-request-review) according to the quality of the contribution.

## Merging changes
Pull requests made by contributors can be approved or merged by maintainers after the review.
There are different ways of merging a pull request:
- *Merge pull request*: Merges all commits to base branch.
It keeps all commits made in the PR as separate and merges them as they are, through a single merge commit to the base branch.
- *Squash and merge*: Squashes all commits created in the pull request into one commit and merges them as a single commit (with the help of a merge commit) to the base branch (see this [blog for details](https://github.blog/2016-04-01-squash-your-commits/)).
- *Rebase and merge*: Rebases all commits individually to base branch (integrating changes from one branch to other) before merging.
In the prompt message, the maintainer can provide a merge message along with comments(if any) and then press the “confirm merge” button.

## Guidelines for Review Process and Maintenance
For project collaboration on GitHub, it is important to follow a defined guideline with best practices for maintaining a particular project.
The maintenance process can be executed smoothly with the help of the following:

1. *Documenting the process*: A comprehensive documentation on how contributors can get started with the project and how they can make meaningful contributions is the first step to be taken while maintaining an open source project.
These details should throw light on what the project is all about, why was it created in the first place, who maintains the project, what is the community culture looks like, and who can provide guidance to new contributors.

These three documents are a good start towards building these documents:
- A project should contain a {ref}`README.md file<rr-github-readme>` that provides the important details and links to resources that one must know to become a member of the project.
- A Code of Conduct (see _The Turing Way_ [Code of Conduct](https://github.com/alan-turing-institute/the-turing-way/blob/master/CODE_OF_CONDUCT.md)) must be provided in every project to establish that a welcoming and safe environment for community members while collaborating.
- A well-written contribution guideline (see _The Turing Way_ [Contributing file](https://github.com/alan-turing-institute/the-turing-way/blob/master/CONTRIBUTING.md)) is extremely important when the collaboration is done remotely on any project to ensure clear communication between contributors and maintainers.

2. *Effective communication*: The conversations regarding any contribution can be made public for others to join for a discussion while working on small features and ideas.
This will involve more people and ensure transparency in open source work.
It is important to write messages and comments on the issue and pull requests, in a clear and easy to understand manner while doing a review to help the contributors in understanding the requirements so that they can make better commits to their pull requests.
It is better to mention important links in the messages if required.

3. *Mentored contributions*: The maintainer's role is to make the contribution a process as easy as possible.
Open source contributions can be intimidating for a lot of new contributors.
Guiding people by making friendly and encouraging conversations can make the onboarding process for new contributors comfortable.
It is better to create descriptive issues to resolve.
For significant contributions to be made, it is better to create different issues before resolving them with pull requests.
Labeling issues and pull requests will help in getting more contributors involved in various tasks with different skill requirements.
Labeling seemingly easy issues as ["good first issue"](https://help.github.com/en/github/building-a-strong-community/encouraging-helpful-contributions-to-your-project-with-labels) will help new contributors to pick up easy tasks like minor changes in code and content, bug and typo fixes and small design issues.

4. *Maintaining the pull requests*: The maintenance of already existing pull requests on a project involves labeling them, reviewing them, changing their stages, merging and closing them.
Maintenance of pull requests can be done by giving the right review at the right time.
On GitHub there are various ways to provide feedback while reviewing such as by giving feedback as a comment on the pull request, suggesting changes while reviewing, directly proposing changes in the branch of the contributors or discussing on the pull request how the contributions can be improved (see this [GitHub post for details](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews)).
Maintainers may communicate a timescale within which they review and merge pull requests for an active project, for example, one week.
The labels can be changed over time and phases to correctly reflect the status of a feature under development.

5. *Acknowledging other's work and respecting time*: Welcoming people who contribute to a project is one of the keys to make a collaborative project a success.
Whenever a meaningful contribution is made and a PR is merged, maintainers should acknowledge it.
A small message saying "Thank you" is often enough, especially for newbies in open source spaces.
It is always a good gesture to give credit to contributors in open source by adding them to the contributor's list.
The best way to do that is to create a dedicated file where all the contributors are mentioned with their contributions made in the projects.
If the project contributors are based in different parts of the world, the maintainers should be respectful towards their time and schedule work accordingly.
In case someone is not able to discuss ideas because of their schedule, maintainers and contributors should try to cooperate as much as possible.
It is also a good practice to actively ask contributors who are very busy to take a break and come back later or involve others from the community to keep track of their ongoing contributions.

## What to learn next

[Community communications for open source](https://the-turing-way.netlify.app/open-source-comms/intro.html) has some relevant information for getting involved with this community-driven project.

## Further reading

* [GitHub help](https://help.github.com/en)- a great resource to know about almost everything concerning collaborating on a GitHub project.
* [Guide to Open Source](https://opensource.guide/)- Guides available related to Open Source, be it maintaining or contributing- most of the topics have been covered here.
* [An article on using Open source research tools](https://opensource.com/education/15/11/tools-analyze-collaborate-share-research)
* [A guide on Pull requests](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)
* [How to guide to workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
* [A Blog on Open source and academia](https://opensource.com/article/19/9/how-open-source-academic-work)
