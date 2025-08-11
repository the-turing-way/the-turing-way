(cl-github-novice-motivation)=
# Motivation for Using GitHub

| Prerequisite | Importance |
| -------------|------------|
| [Version control](#rr-vcs) | Helpful |

GitHub is an online web interface for collaborating, developing, sharing and using [git](#rr-vcs-git) ([version control](#rr-vcs)).
It's designed to be easily accessible (you do not need to be a coder!) to share your work and (if you want) allow other people to test, modify, remix and reuse it.
It also provides space and tools for collaboration and maintenance.

GitHub is not the only available development platform, but it hosts this book and is widely used across disciplinary and private-public boundaries.
Thus, this chapter is tailored towards GitHub and its resources, though other platforms have some similar and/or analogous functions.

Some key things to know about GitHub:

- It provides an easy-to-use interface for [version control](#rr-vcs) that allows all activities to be recorded so you can revisit past versions and you know who made each contribution to the project.
- It has project management features - [issues](https://github.com/features/issues), [pull requests](https://github.com/features/code-review), and [discussions](https://github.com/features/discussions) - providing a social platform and communication tools that help a group of people to work together effectively.
- It can be used to store [documentation](#rr-project-documentation), [data](#rr-vcs-data) and make [web pages](https://cassgvp.github.io/github-for-collaborative-documentation/docs/tut/4-2-Make-your-Pages-site.html) for projects - not just code!
- It has many options for automating repeated project management tasks including [continuous integration testing](#rr-ci) and deployment.
- It can work entirely in your web browser, you do not need to install anything

In this chapter we outline some of the ways that you can benefit from using GitHub for your collaborative projects.

## Version Control

GitHub provides an interactive user interface that makes [version control](#rr-vcs) more accessible and intuitive.
It can be useful for those unfamiliar with command-line [git](#rr-vcs-git).

Through the GitHub repository webpage, you can:
* View a project's detailed [history of changes](#rr-vcs-workflow) to each file.
* Revisit old versions of files and track contributions made.
* [Roll back](#rr-vcs-versions-retrieving) to previous versions of files if needed.
* Visualize helpful, color-coded "[diffs](#rr-vcs-versions-comparing)" that highlight what has changed between different versions of the same file.
  * This helps during [peer review](#cm-peer-review) and makes it easy to identify how the file has changed, line by line.

## Project Management

You can [manage](#pd) your project by creating [project boards](#cl-event-tools) that include to-do lists and issues (problems or tasks that need to be done).
[Discussion forums](https://github.com/features/discussions) and flexibility in [user permissions](#cl-maintain-review-permissions) mean you can give team members (and/or the general public) the appropriate levels of access.

The [Insights](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects) menu shows project stats, such as a [list of all contributors](#ch-acknowledgement-record) and how often they contribute each week.

## Collaboration and Community

The combination of pathways to leverage version control and project management tasks makes GitHub a great place to build a community around your work.

Its tools allow for clear [communication](#cm-os-comms-channels) and task allocation.
Multiple people can work on the same files at the same time, and git can track the changes and resolve any conflicts.

* Work on different versions of the project using [branches](#rr-vcs-workflow-branches)
* Suggest changes using [pull requests](https://docs.github.com/articles/about-pull-requests), which are then reviewed and accepted
* Track bugs and feature requests using documented [issues](#cm-os-comms-issue-tracking)
* Hold [discussions](https://github.com/features/discussions) with other collaborators
* [Roadmap](#rr-project-documentation) new tasks and receive feedback from others

## Reproducibility

Sharing your project on GitHub helps improve [reproducibility](#rr-overview), transparency, and verifiability, all key principles in [research](#rr-vcs-git4research).
By providing open access to your work, others can understand your methods, build upon your work, and accurately replicate your results.
Many researchers [attach](#cm-citable) GitHub links in their publications to share analyses with instructions to reproduce their results.
You can also integrate your project with [Zenodo](https://zenodo.org/) to generate a Digital Object Identifier (DOI) for [citation](#cm-citable-linking).
This ensures your work is preserved and easier to reference.

## Publishing and Outreach

Sharing your project on GitHub is not only useful for [collaboration](#cl), but also for [communication](#cm) - reaching a wider audience and increasing the impact of your work.

Projects on GitHub can be [set to either public or private](#https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility) (visible to anyone or only accessible by you or your team).
There are benefits that come with making your project public:

* Broader reach as anyone can access and contribute to your project.
* Increased visibility through GitHub's [Explore](https://github.com/explore) feature.
* Others can "[star](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars)" (bookmark) or "[watch](https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-subscriptions-for-activity-on-github/viewing-your-subscriptions)" your project for updates.
* Share your project with others through a trustworthy [GitHub.com](https://github.com) link, as the platform is widely known.
* Use [GitHub Pages](https://pages.github.com) to create a clean, professional [webpage](#cm-personal-websites) for your project.
* Add a [README file](#pd-project-repo-readme) to act as your project's landing page, where you can welcome visitors, explain your work, and provide [documentation](#rr-documentation-code).

## Testing and Release Management

Once your project reaches a stable point, you may want to package it and share it with others.
[Tagging](#rr-rdm-metadata-tagging) allows you to mark a specific point in your project's history, often used for major updates or official versions.
For example, you might mark a specific set of features with a tag called "v1.0.0" to represent your project's official "Version 1" release.
After tagging, you can create a [release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) on GitHub.
A release is a packaged version of your project that includes detailed release notes, a contributor list, and links to download files.
This makes it easier for users to find, cite, or download a specific version of your work.

GitHub can also integrate with [Continuous Integration (CI)](#rr-ci) and Continuous Delivery / Deployment (CD) tools.
These tools automatically test new changes, help catch errors, and can even automate the process of creating releases.
This integration ensures your project still works as expected with each change, and makes development more efficient.

## Distributed Backup

Hosting your project on GitHub serves as a safety net that can be accessed from anywhere.
* A copy of your work is stored online, not just on one device.
* If you lose your local files, such as due to hardware failure, you can still recover everything from GitHub.
* The use of GitHub decentralizes the project, and [project responsibility](#cl-leadership) can be shared.
* If you stop maintaining a project, others can still view, [cite](#cm-citable-linking) or [fork](https://docs.github.com/articles/fork-a-repo) it to continue development.

## Role Modeling for Others

Choosing to set your project as public allows others to learn from your work.
By viewing your files, learners can see how you approached problems and implemented solutions.
This is especially helpful for beginners looking for real examples to study.
Your project might even encourage new contributors or inspire others to create their own projects.

## Easy to get started

GitHub makes it easy for anyone to get started with version control and collaboration.
Compared to the command line, GitHub's graphical interface lowers the barrier for new users and offers an alternative method of interfacing with Git.
You can use GitHub directly in your web browser without installing any other necessary software.
Most version control steps can be done in the browser, such as editing files, committing changes, and viewing file diffs.

This is not to understate the value of the command line and git.
The command line is a powerful tool and with a little practice, is not as difficult as it may seem.
Experienced users will likely find the command line more convenient and efficient for advanced workflows.
You can choose the best approach for you, whether that is clicking through menus or typing commands.

## Markdown

In order to use GitHub, you do not need to be a computer coder!
To format text, you only need to learn a very simple type of file formatting syntax called Markdown.
Again, you do not need to download a Markdown editor as it can all be written directly in GitHub in your web browser.
Markdown syntax is designed to be human readable even if it isn’t rendered.
This allows you to format your text into a nice-looking document, including adding in links, pictures, tables and web links.
In most cases, GitHub even provides a "preview" option that allows you to see what your rendered document will look like.

For example, if you want to put a heading in markdown you use a ‘#’ (hash symbol) followed by a space and the title.
For example, `# heading 1`, will produce first level header style for that text.

### Resources to help you learn Markdown

* How to write faster, better & longer: [the ultimate guide to Markdown](https://ghost.org/changelog/markdown/)
* [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Markdown guide: [Basic syntax](https://www.markdownguide.org/basic-syntax/)

How and when to use Markdown formatting in your file will become clearer as you go through this chapter.

## Next steps

Keep reading this chapter for detailed GitHub tutorials.
The next subchapter, [](#cl-github-novice-firststeps), will walk you through creating your own GitHub project.

For more GitHub information and learning materials, visit [GitHub.com](https://github.com).

You can also explore [The Turing Way's home page](https://book.the-turing-way.org) for additional guides, reading, and resources.
