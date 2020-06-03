# Collaborating as a maintainer

## Prerequisites / recommended skill level
> 

| Prerequisite | Importance | 
| -------------|----------|
| [Experience with version control](/version_control/version_control) | Helpful | 

## Summary
For any open source project, the most difficult job is to work on an idea and make suitable changes. There are many tasks which are very well carried out by the project maintainer/owner or the maintaining/owning team. 
The following chapter throws light on some of the most important tasks of the admins and maintainers of the project such as carrying on discussions, mentoring contributors, creating, reviewing and merging Pull Requests (PRs) and handling issues on a collaborative GitHub project. It also provides the best practices to be used while contributing to a project as a maintainer.

**_NOTE_**: It does not show "how to" guides to these tasks and gives an introductory knowledge about what are the major responsibilities of a maintainer and how these responsibilities should ideally be carried out.

## How this will help you/ why this is useful 
The maintenance and review work is important for the people who are interested in maintaining _The Turing Way_ GitHub repository and can review contributions. 
>The Git workflow is difficult to understand, especially when collaborating with a group of contributors for a project. Hence, it is very important that the reviews to all these contributions are properly done.

## Reviewing and Maintainance- What is it?
An open source project allows many people to make contributions in the form of [issues](https://help.github.com/en/github/managing-your-work-on-github/about-issues) and [pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).
Community members can also perform [reviews](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews) and provide feedback [comments](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request) on the ideas and changes which they or others have suggested.
These ideas and discussions lead to better quality code and opens new perspectives regarding a particular feature. The reviews are done to make high quality production level code.  
Maintenance deals with keeping the existing code updated. It requires that whenever a new feature is added or whenever a new idea is accepted, the corresponding changes must be made in existing codebase (if required) and the documentation.  
It requires [opening](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue),[deleting](https://help.github.com/en/github/managing-your-work-on-github/deleting-an-issue) and [closing/linking](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue) important issues, [reviewing](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/reviewing-proposed-changes-in-a-pull-request), [labelling](https://help.github.com/en/github/managing-your-work-on-github/labeling-issues-and-pull-requests), [changing the stages](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/changing-the-stage-of-a-pull-request), [merging](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/merging-a-pull-request) and [closing](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/closing-a-pull-request) important pull requests.  
Knowing the working of Version control systems, [markdown](https://guides.github.com/features/mastering-markdown/) and open source [workflow](https://guides.github.com/introduction/flow/) helps to a great extent in carrying out all these tasks.

## Ownership and Permissions 
In any team or organization owned project, there are different contributors. 

- Some start the project and are generally, the owners of the project. The Codeowners who have the rights over who can make reviews and suggest changes to contributions. The individuals or teams who are codeowners for a certain project may be specified at the time of project creation in a file of the project.  
An example of this could be the [CODEOWNERS file](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners) or the [Ways of Working file](https://github.com/alan-turing-institute/the-turing-way/blob/master/ways_of_working.md) of _The Turing Way_ which provides an insight about the core project team responsible for creating and maintaining the project.   
They can make other contributors as maintainers, reviewers or members working on the project. They can also involve other codeowners and are responsible for granting permissions. 

- Maintainers are involved with creating issues and pull requests whenever required. They keep the codebase updated and help in reviewing contributions. They can merge pull requests.  
They can also request reviews from someone else. There are various [levels of permissions](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization) for a project in GitHub.

## Reviewing process
- Any code base or set of changes must be reviewed before merging. If the project is co-owned by many people, the review process is done by handling it in the form of a [code review assignment](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/managing-code-review-assignment-for-your-team) in which certain members of the team are chosen for the review.  
This member subset of team is selected with the help of algorithms after reviewing is enabled and review assignment is configured for a particular project.  
- The review process is dependent on the testing of a particular pull request by a maintainer or admin. The admins can easily [test](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/checking-out-pull-requests-locally) the changes made in their local systems and suggest changes required.  
- After this any set of changes through pull requests can be reviewed. When the review process is completed the reviews are [approved](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/approving-a-pull-request-with-required-reviews) or [dismissed](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/dismissing-a-pull-request-review) according to the outcome. 

## Merging changes
Pull requests created by contributors can be easily merged by maintainers after the review. There are different ways of merging a PR:
- Merge pull request- Merges all commits to base branch. This keeps all commits made separated. 
- Squash and merge- Squashes all commits into one and then merges the pull request. 
- Rebase and merge- Rebases all commits individually to base branch before merging.  
In the prompt message, the maintainer can provide a merge message along with comments(if any) and then press the “confirm merge” button.

## Guidelines for Review Process and Maintainance
For project collaboration on GitHub, it is very important to follow certain guidelines and best practices while maintaining a particular project. These guidelines become extremely important when the collaboration is done remotely on any project where the contributors and the maintainers might experience communication gaps due to various reasons. In such situations, contributing and maintenance can be done smoothly by the help of the following:

1. Documenting the process- Writing down a guide on how contributors can get started with the project and how they can make meaningful contributions is the first step to be taken while maintaining any open source project.  
A project's [README](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes) file should throw light on what the project is all about, why was it created in the first place, who maintains the project and who can provide guidance to new contributors.

2. Effective communication- The conversations regarding any contribution can be made public for others to join for a discussion while working on small features and ideas. This will involve more people and ensure transparency in the open source work.  
It is important to write messages and comments, in a clear and easy to understand manner while doing a review to help the contributors in understanding the requirements so that they can make better commits to their pull requests.  
It is better to mention important links in the messages if required.

3. Mentorship and descriptions- The maintainer's job is to make contribution a process as easy as possible. Open source contributions can be intimidating for a lot of people.  
Guiding people by making friendly and encouraging conversations can make the onboarding process for new contributors comfortable. It is better to create descriptive issues to resolve. For significant contributions to be made, it is better to create different issues before resolving them with PRs.  
Labelling issues and PRs will help in getting more contributors involved in various tasks with different skill requirements. Labelling seemingly easy issues as ["good first issue"](https://help.github.com/en/github/building-a-strong-community/encouraging-helpful-contributions-to-your-project-with-labels) will help new contributors to pick up easy tasks like minor changes in code and content,bug and typo fixes and small design issues.

4. Maintaining the PRs- The maintenance of already existing PRs on a project involves labelling them, reviewing them, changing their stages, merging and closing them. Maintenance of PRs can be done by giving the right review on the right time.  
It is ideal for any maintainer to review a contribution in the form of a PR within one week for an active project and provide labels as soon as possible.

5. Being grateful and respecting time- Welcoming people who contribute to a project is one of the keys to make a collaborative project a success. Whenever a meaningful contribution is made and a PR is merged, maintainers should value it.   A small message saying "Thank you" is more than enough, especially for newbies in Open-source. It is always a good gesture to give credit to contributors in open source. Making a page or a file where all the key contributors are mentioned is a great way to do this.  
If the project contributors are based in different parts of the world, the maintainers should try to be respectful towards their time and schedule work accordingly. In case someone is not able to discuss ideas because of their schedule, maintainers and contributors should try to cooperate with each other as much as possible. 

## What to learn next
[Community communications for open source](https://the-turing-way.netlify.app/open-source-comms/intro.html) has some relevant information with respect to getting involved with this community driven project.

## Further reading
* [GitHub help](https://help.github.com/en)- a great resource to know about almost everything with respect to collaborating on a GitHub project.
* [Guide to Open Source](https://opensource.guide/)- Guides available related to Open Source, be it maintaining or contributing- most of the topics have been covered here.
* [An article on using Open source research tools](https://opensource.com/education/15/11/tools-analyze-collaborate-share-research)
* [A guide on Pull requests](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)
* [How to guide to workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
* [A Blog on Open source and academia](https://opensource.com/article/19/9/how-open-source-academic-work)

## Definitions/glossary
* **Repository or Project**- this is similar to a directory on the local system. Any contributor can put in programs, files and folders in it so that the project will be safely stored on a GitHub account.
* **Commit(s)**- these are the changes which are made in a file of a project remotely. The local changes can be pushed to a remote repository with the help of a commit along with a message.
* **Issues**- GitHub provides the feature of creating issues on a repository. Issues which are hindering the project to work smoothly or an issue which contains an idea to be added on a project can be created with this feature.
* **Pull request**- after creating changes a request is created for the maintainer or the owner of the organisation or projct to review. The owner or maintainer can review it and comment on these pull requests, and then the requests can be merged.
* **Owners and Maintainers**- the project creators, maintainers and owners, who have a higher level of access when compared to all other members or contributors working together on a GitHub project.
* **Review**- suggesting changes or asking for committing something to an already created PR.
* **Merging**- merging a PR means merging changes which have been reviewed by a maintainer or an admin to a project for making it better.
