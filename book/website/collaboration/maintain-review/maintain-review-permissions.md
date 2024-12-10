(cl-maintain-review-permissions)=
# Ownership and Permissions
In any team or organisation owned project, there are different contributors.

Owners of a project are individuals or teams who generally start a project, or join it at the time of project creation with a defined vision and goals.
The owners have the right to give different [levels of permission](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization) to outside contributors.

In Github, there are five levels of permissions: read, triage, write, maintain, and admin.
* Readers are non-code contributors who are read the content or join discussions on GitHub issues.
* With triage permission, contributors can manage issues and pull requests without write access.
* Write permission allows contributors to push changes to the project.
* Maintain permission is for project managers but have no access to sensitive or destructive actions (such as project deletion).
* Admins are people who have full access to the project, including sensitive and destructive actions, and are responsible for granting permission to make other contributors.

These roles are often defined in a project file such as a [CODEOWNERS file](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners) or a Ways of Working file (see _The Turing Way_'s [Ways of Working](https://github.com/the-turing-way/the-turing-way/blob/main/ways_of_working.md) as an example).
These files provide insight into the core project team and members responsible for maintenance roles in the project.

In this chapter, anyone with triage, write and maintain permission is referred to as maintainers.
Maintainers are involved with creating issues and pull requests whenever required.
They keep the codebase or project updated and help in reviewing contributions.
They can often approve and merge pull requests.
They can also request reviews from someone else.

*For more information on permission level, please see this [documentation on GitHub](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization).*
