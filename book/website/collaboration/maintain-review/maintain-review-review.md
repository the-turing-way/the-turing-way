(cl-maintain-review-reviewing)=
# Reviewing Contributions

## Reviewing process
In a project or codebase, a set of changes must be reviewed before merging it to the main repository.
If the project is co-owned by many people, the review process handled by [code review assignment](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/managing-code-review-assignment-for-your-team) in which certain members of the team are assigned this task.
Reviewers are often automatically suggested on GitHub pull requests based on a similar activity by other members on the same or different files in the project.
However, often a project manager requests other maintainers for the review of a particular pull request based on their availability, willingness, or expertise.

The assigned or willing maintainers can review the pull request by checking the [changes locally](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/checking-out-pull-requests-locally) or on the online repository and suggest changes required.
When the review process is completed, the reviews can be approved without any change, or [with required changes](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/approving-a-pull-request-with-required-reviews) or [dismissed](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/dismissing-a-pull-request-review) according to the quality of the contribution.

## Guidelines for Review Process and Maintenance
For project collaboration on GitHub, it is important to follow a defined guideline with best practices for maintaining a particular project.
The maintenance process can be executed smoothly with the help of the following:

1. *Documenting the process*: A comprehensive documentation on how contributors can get started with the project and how they can make meaningful contributions is the first step to be taken while maintaining an open source project.
These details should throw light on what the project is all about, why was it created in the first place, who maintains the project, what the community culture looks like, and who can provide guidance to new contributors.

These three documents are a good start towards building these documents:
- A project should contain a {ref}`README.md file<pd-project-repo-readme>` that provides the important details and links to resources that one must know to become a member of the project.
- A Code of Conduct (see _The Turing Way_ [Code of Conduct](https://github.com/the-turing-way/the-turing-way/blob/main/CODE_OF_CONDUCT.md)) must be provided in every project to establish that a welcoming and safe environment for community members while collaborating.
- A well-written contribution guideline (see _The Turing Way_ [Contributing file](https://github.com/the-turing-way/the-turing-way/blob/main/CONTRIBUTING.md)) is extremely important when the collaboration is done remotely on any project to ensure clear communication between contributors and maintainers.

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
