(cl-new-community-guide)=
# Guide to Planning a Community

What if you started a project with a thought like, “I have this great idea that I want to try on this public data!”?
There is nothing to worry about if you’re the only one working on it.
However, if you want to develop this project - you become responsible for making people feel included in your project.

As a 'project lead', you want to set up a welcoming and inclusive environment and create the first set of visions and goals for your collaborators.
You cannot assume that everyone you collaborate with knows what is expected of them when they start to work with others on your project.
Therefore, it’s important to set the right expectations from the beginning for your community, even though you might not have planned on having one (see more details: {cite:ps}`Sharan2020Apr`).

(cl-new-community-guide-checklist)=
## A Checklist for Planning Collaboration in Your Project

The checklist below will help you in making the process of establishing collaboration in your research project thoughtfully in a structured manner.

The practices listed here are derived from and limited by the experiences of the authors who participate in several successful Open Research communities and lead community-driven projects such as [The Carpentries](https://carpentries.org), [Mozilla Open Leaders](https://mozilla.github.io/open-leadership-training-series/), [Open Life Science](https://openlifesci.org/) and _The Turing Way_.
While reading this chapter, please be aware that you may need to make adjustments for projects that may be very different in nature (for example, not entirely open source).

(cl-new-community-guide-checklist-comms-platform)=
### 1. Choose a Communication Platform

- When leading an open project, use collaborative and open platforms such as [GitHub](http://github.com/) or [GitLab](https://about.gitlab.com/).
- Evaluate the need for any real-time communications, such as if a text chat system like [Slack](https://slack.com) or [Element/Matrix](https://element.io/get-started) will be useful or if a mailing list will be sufficient (read details {ref}`Communication Channels <cm-os-comms-channels>`).
  - Consider a separate internal communication platform for your community members and an external one for showing what you’ve done to the rest of the world.
- An [X account](https://x.com) (formerly Twitter) or a simple website (such as on [GitHub pages](https://pages.github.com/)) can be useful external platforms.
- Make sure that the choices of these platforms are made to ensure that there is a low barrier to join them.

(cl-new-community-guide-checklist-proj-summary)=
### 2. Provide a Project Summary File:

- The first document in your project should be a project summary file, which in a GitHub repository will be a [README.md file](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes).
- This will provide basic information about your project so that people can evaluate why your project will be interesting for them.
  - Here is [a template](https://github.com/PurpleBooth/a-good-readme-template) by the GitHub user [PurpleBooth](https://github.com/PurpleBooth).
- In this file, include what your project vision and goals are, why the project is useful, what the possible milestones are in the project, how a contributor or user can get started, who can they reach out to for help, and what is currently missing in the project in terms of stakeholders, skills, or scope.
- You can use emojis, GIFs, videos, or your personal narrative to make your project relatable.
  - See [The Atom project](https://github.com/atom/atom) for example.

(cl-new-community-guide-checklist-code-conduct)=
### 3. Select a Code of Conduct:

- Add an Open Source Project [Codes of Conduct](https://opensourceconduct.com/) to your project.
- This document should not be used as a token, it is very important to put intentional effort into it.
- When using GitHub, you can add a “CODE_OF_CONDUCT.md” file on your GitHub repository.
- List the expected and unacceptable behaviors, describe the reporting and enforcement process, explicitly define the scope, and use an inclusive tone  (see [GitHub instructions here](https://help.github.com/en/github/building-a-strong-community/adding-a-code-of-conduct-to-your-project)).
- Whenever you update your code of conduct, invite comments from your members to ensure that their concerns are addressed.
  - This can be done on [GitHub issues](https://help.github.com/en/github/managing-your-work-on-github/about-issues), or [Pull Requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).

(cl-new-community-contrib-guidelines)=
### 4. Provide Contribution Guidelines and Interaction Pathways:

- A thoughtful guideline helps people decide which pathway they can choose to contribute to your project, or if they want to be in your community at all.
- Make sure that your community interactions and different pathways to contribute are open, inclusive, and clearly stated.
  - If people can’t figure out how to contribute they will drop off without helping.
- Value different types of contributions - coding projects are not only about code, therefore list documentation and other management skills as well.
- You can use the {ref}`Persona Creation Tool<pd-persona-creation>` or the [Personas and Pathways exercise](https://mozillascience.github.io/working-open-workshop/personas_pathways/) to brainstorm who could be your possible community members.
- Here is a [template of community guideline](https://gist.github.com/PurpleBooth/b24679402957c63ec426) provided by the GitHub user [PurpleBooth](https://gist.github.com/PurpleBooth).
  - See [_The Turing Way_'s contributing file](https://github.com/the-turing-way/the-turing-way/blob/main/CONTRIBUTING.md) for reference.

(cl-new-community-leadership)=
### 5. Create a Basic Management/Leadership Structure:

- A leadership structure in an open project should aim to empower others and develop agency and accountability in your community.
- You can start by listing different tasks within your project and inviting your members to lead those tasks.
- Provide appropriate incentives and acknowledgment for the contributions made by your community members.
- Create opportunities for members to share some leadership responsibilities with you in the project.
- When inviting suggestions and ideas from the community, provide the first set of plans where your community can develop from.
- See this document from [Open Source Guides](https://opensource.guide/leadership-and-governance/) for reference.

(cl-new-community-contact)=
### 6. Provide Contact Details Wherever Useful:

- Clarifying responsibilities for different members will allow people to reach out to the right person with any query.
- Add details of the designated contact persons for technical problems, leadership questions, or any report on the Code of Conduct.
- This will be particularly useful if something needs immediate resolution.

(cl-new-community-approaches)=
### 7. Identify Failed Approaches, and Stop Them:

- Development happens in an iterative manner, therefore, revisit your plans and ideas in regular intervals and involve your members in the process.
- Check if there are parallel developments or multiple approaches that should be merged or changed.
- Fail fast, fail informatively - recognize what isn’t working for your project and stop it from continuing.
- Document them and share why you failed and how you change your project or approaches going forward.
- For Open Research communities you can maintain transparency when discussing failures and successes but refrain from singling out or blaming others.
- This iterative approach comes from Agile Practices, see these short posts for reference:
  - [The agile concept fail fast gets bad press but is misunderstood](https://www.information-age.com/agile-concept-fail-fast-gets-bad-press-misunderstood-123460434/)
  - [The Beginner’s Guide To Scrum And Agile Project Management](https://blog.trello.com/beginners-guide-scrum-and-agile-project-management)

(cl-new-community-documentation)=
### 8. Have Documentation and Dissemination Plans for Your Project:

- With new members joining your project, they must be able to find the information they need without asking you.
- Investing in documentation plans will free you from many communication-related challenges by sharing general information regarding past decisions or the decision making process your project uses.
- A good place to store the documentation is [wiki](https://en.wikipedia.org/wiki/Wiki) or similar platforms (like GitHub) where information can be shared transparently and updated by your community members democratically.
- To disseminate outputs of your project, you should use persistent identifiers that can be shared and cited, for example, [digital object identifier (DOI)](https://www.doi.org/).
  - [Figshare](https://figshare.com/) and [Zenodo](http://zenodo.org) are good examples of platforms that can provide you with DOI for all your shareable data.

Two more points are crucial for ensuring the effectiveness of a collaborative project: addressing technical issues and valuing the importance of diversity in team building.

We have explained them in the next subchapters on {ref}`Addressing Technical Issues<cm-new-community-techissue>` and {ref}`Valuing Diversity and Differences<cl-new-community-differences>`.
