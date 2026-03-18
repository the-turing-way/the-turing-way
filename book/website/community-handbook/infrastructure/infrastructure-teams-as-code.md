(ch-infrastructure-teams-as-code)=
# Teams as Code

_The Turing Way_ uses [GitHub Teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams) to organise its members and manage access/permissions to various repositories, most notably [Working Groups](#subprojects-working-groups).
However, as the community grows and we create more teams and repositories, they will become more difficult to manage.
Also, a bottleneck will be created if only the GitHub organisation owners and/or the [Infrastructure Working Group](subprojects-infra-wg) have the ability to manage the teams.
Therefore, a repository has been setup using [infrastructure-as-code principles](https://en.wikipedia.org/wiki/Infrastructure_as_code) specifically targeting teams management: [the-turing-way/teams-as-code#README.md](https://github.com/the-turing-way/teams-as-code/blob/HEAD/README.md)

In this repository, YAML files are used to build human-readable definitions of our GitHub Teams, their members, which repositories they have access to, and at what permission level.
The workflows in this repository use a tool called [opentofu](https://opentofu.org/) to create and reflect the structure defined by the YAML files in _The Turing Way's_ GitHub organisation.
Therefore, any additions, changes, or deletions made to the YAML files will be automatically applied to the organisation when the edits have been merged.
This will allow easier management and control of teams, their members, and permissions throughout the organisation.

As well as this ease of management, we have chosen this approach because it will also make the teams easier to audit since who made what changes will be captured in the git history of the repository.
All of this information is now centralised and transparent in a single place and easy-to-read format.
The bottleneck on the [Infrastructure Working Group](subprojects-infra-wg) and/or GitHub org admins will be removed since those with write access (the teams themselves) will be able to raise, review, and merge their own Pull Requests against this repository.
We have implemented a [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) file that makes each GitHub team responsible for their own YAML file defining it (or a good enough approximation where necessary).

Please see the [teams-as-code repository](https://github.com/the-turing-way/teams-as-code) for more information.
