# Contributing to _The Turing Way_

:tada::balloon::cake: **Welcome to _The Turing Way_ repository!** :cake::balloon::tada:

:dizzy::hatched_chick::sunny: _We're excited that you're here and want to contribute._ :sunny::hatched_chick::dizzy:

We want to ensure that every user and contributor feels welcome, included and supported to participate in _The Turing Way_ community.
We hope that the information provided in this document will make it as easy as possible for you to get involved.

We welcome all contributions to this project via GitHub issues and pull requests.
Please follow these guidelines to make sure your contributions can be easily integrated into the projects.
As you start contributing to _The Turing Way_, don't forget that your ideas are more important than perfect pull requests. :heart:

If you have any questions that aren't discussed below, please let us know through one of the many ways to [get in touch](#get-in-touch).

## Table of contents

Been here before? Already know what you're looking for in this guide? Jump to the following sections:

- [Joining the community](#joining-the-community)
- [Inclusivity](#inclusivity)
- [Get in touch](#get-in-touch)
- [Contributing through GitHub](#contributing-through-github)
- [Writing in Markdown](#writing-in-markdown)
- [Where to start: issues](#where-to-start-issues)
  - [Issue labels](#issue-labels)
- [Making a change with a pull request](#making-a-change-with-a-pull-request)
  - [1. Comment on an existing issue or open a new issue referencing your addition](#1-comment-on-an-existing-issue-or-open-a-new-issue-referencing-your-addition)
  - [2. Fork _The Turing Way_ repository to your profile](#2-fork-the-turing-way-repository)
  - [3. Make the changes you've discussed](#3-make-the-changes-youve-discussed)
  - [4. Submit a pull request](#4-submit-a-pull-request)
- [The process of writing chapters](#the-process-of-writing-chapters)
- [Style Guide](#style-guide)
- [Representing _The Turing Way_](#representing-the-turing-way)
- [Recognising Contributions](#recognising-contributions)

## Joining the community

_The Turing Way_ is a community-led and collaboratively developed project.
We, therefore, require that all our members and their contributions **adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) (CoC)**.
Please familiarize yourself with our [CoC](CODE_OF_CONDUCT.md) that lists the expected behaviours.
We have also provided details for CoC reporting and enforcement, which can be read in our [Community Handbook](https://book.the-turing-way.org/community-handbook/coc.html).

## Inclusivity

_The Turing Way_ aims to be inclusive to people from all walks of life and to all research fields.
These intentions must be reflected in the contributions that we make to the project.

In addition to the CoC, we encourage intentional, inclusive actions from contributors to _The Turing Way_.
Here are a few examples of such actions:

- use respectful, gender-neutral and inclusive language (learn more about inclusive writing on page 22 of [University of Leicester Study Skills pdf](https://www2.le.ac.uk/projects/oer/oers/ssds/oers/study-skills/studyskills.pdf), also available as a [zipped html](https://www2.le.ac.uk/projects/oer/oers/ssds/oers/study-skills/studyskills_HTML.zip)).
- aim to include perspectives of researchers from different research backgrounds such as science, humanities and social sciences by not limiting the scope to only scientific domains.
- make sure that the colour palettes are accessible to colour-blind readers and contributors.
See the blogpost [Designing Scientific Figures for Colour Blindness](https://www.lewismackenzie.science/updates-1/2017/2/9/designing-scientific-figures-for-colour-blindness) for an example of how somebody improved one of their diagrams, including links to recommended colour palettes and a colour-blindness simulator. for an example of how somebody improved one of their diagrams, including links to recommended colour palettes and a colour-blindness simulator.

## Get in touch

There are many ways to get in touch with _The Turing Way_ team!

- GitHub [issues](https://github.com/the-turing-way/the-turing-way/issues) and [pull requests](https://github.com/the-turing-way/the-turing-way/pulls)
  - Join a discussion, collaborate on an ongoing task and exchange your thoughts with others.
  - Can't find your idea being discussed anywhere?
    [Open a new issue](https://github.com/the-turing-way/the-turing-way/issues/new/choose)! (See our [Where to start: issues](#where-to-start-issues) section below.)
- [Slack Channel](https://join.slack.com/t/theturingway/shared_invite/zt-fn608gvb-h_ZSpoA29cCdUwR~TIqpBw)
  - For structured discussion and sustained engagement with the community members.
  - We will also provide notifications on upcoming events and share useful resources on Slack.
  - You can also ping us on [Gitter channel](https://gitter.im/the-turing-way/the-turing-way) (open source option).
- Contact the Community Manager of _The Turing Way_ project – Anne Lee Steele – by email at [asteele@turing.ac.uk](mailto:asteele@turing.ac.uk)
- Contact the co-leads of _The Turing Way_ project - Kirstie Whitaker - by email at [kwhitaker@turing.ac.uk](mailto:kwhitaker@turing.ac.uk) and Malvika Sharan - by email at [masharan@turing.ac.uk](mailto:masharan@turing.ac.uk).

### Receiving Updates

- [@turingway](https://twitter.com/turingway) on Twitter
    - Follow us for regular updates
- [Our mailing list](https://buttondown.email/turingway): Receive monthly project updates in a newsletter
- [Fireside Chat Series](https://hackmd.io/@turingway/fireside-chats): Every month, The Turing Way Fireside chat will feature experts, champions and their projects from across different international communities in reproducibility, open research, ethics, collaboration and everything in between. This will be an incredible opportunity for catalysing cross-community collaboration and knowledge sharing.
- **Useful links**: other links to our resources along with announcements are shared via this HackMD: [hackmd.io/@turingway/demo-intro](https://hackmd.io/@turingway/demo-intro)

### Coworking and Real-Time Collaboration

- [Bimonthly Collaboration Cafe](https://book.the-turing-way.org/community-handbook/coworking/coworking-collabcafe.html): Every first and third Wednesday (15:00 - 17:00 London time)/. This is an **online collaboration and coworking event** that engage anyone interested in learning and discussing research best practices and sharing them on The Turing Way book: https://book.the-turing-way.org*. Shared notes with joining links: https://hackmd.io/@turingway/collaboration-cafe.
- [Weekly Coworking Calls](https://book.the-turing-way.org/community-handbook/coworking.html): Every Monday (11:00 - 12:00 London time)/. This is a synchronous collaborative space to either discuss your ideas or quietly work in an accountable space with _The Turing Way_ team members. Shared notes with joining links: https://hackmd.io/@turingway/coworking-call.
- [Book Dash Events](https://book.the-turing-way.org/community-handbook/bookdash.html) take place 1-2 times a year for a more engaged sprint for collaboration, networking and development either in person 1-2 days, or online for a week for flexible participation. Announcements are made via mailing list, Twitter, Slack and presentations.

## Contributing through GitHub

[Git][git] is a really useful tool for version control.
[GitHub][github] sits on top of Git and supports collaborative and distributed working.

We know that it can be daunting to start using Git and GitHub if you haven't worked with them in the past, but _The Turing Way_ maintainers are here to help you figure out any of the jargon or confusing instructions you encounter! :heart:

In order to contribute via GitHub, you'll need to set up a free account and sign in.
Here are some [instructions](https://help.github.com/articles/signing-up-for-a-new-github-account/) to help you get going.
Remember that you can ask us any questions you need to along the way.

## Writing in Markdown

GitHub has a helpful page on [getting started with writing and formatting on GitHub](https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github).

Most of the writing that you'll do will be in [Markdown][markdown].
You can think of Markdown as a few little symbols around your text that will allow GitHub to render the text with a little bit of formatting.
For example, you could write words as **bold** (`**bold**`), or in _italics_ (`_italics_`), or as a [link][rick-roll] (`[link](https://youtu.be/dQw4w9WgXcQ)`) to another webpage.

Also when writing in Markdown, please [start each new sentence on a new line](https://book.the-turing-way.org/community-handbook/style.html#write-each-sentence-in-a-new-line-line-breaks).
Having each sentence on a new line will make no difference to how the text is displayed, there will still be paragraphs, but it makes the [diffs produced during the pull request](https://help.github.com/en/articles/about-comparing-branches-in-pull-requests) review easier to read! :sparkles:

## Where to start: issues

Before you open a new issue, please check if any of our [open issues](https://github.com/the-turing-way/the-turing-way/issues) cover your idea already.
If you open a new issue, please follow our basic guidelines laid out in our [issue templates](https://github.com/the-turing-way/the-turing-way/issues/new/choose).
There are 3 issues templates to choose from.:
1. New Chapter Template ([preview here](https://github.com/the-turing-way/the-turing-way/issues/new?assignees=&labels=book&projects=&template=new_chapter.yml&title=%5BNEW+CHAPTER%5D+-+%3CTOPIC%3E)):  This issue is a place to discuss matters relating to writing a new chapter on a new topic or adding a subchapter in an already existing chapter.
2. General ([preview here](https://github.com/the-turing-way/the-turing-way/issues/new?assignees=&template=ISSUE_TEMPLATE.md)):  Use this template for a general issue related to the book, community, process or ideas.
3. Bug Report ([preview here](https://github.com/the-turing-way/the-turing-way/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D)): With this template, create an issue report that can help others repair something that is currently broken.
This can be used for reporting errors like typos and broken links.
The issue template will automatically be rendered in the comment section of the new issue page, so all you need to do is edit the "_Lorem ipsum_" sections.

### Issue labels

The list of labels for current issues can be found [here][turing-way-labels] and includes:

- [![approval-request](https://img.shields.io/badge/-approval%20request-8bd82d.svg)][labels-approval-request] _When a bug or minor changes have been made, contributors can label their PR along with "bug fixed"._

- [![binderhub](https://img.shields.io/badge/-binderhub-F37726.svg)][labels-binderhub] _These issues relate to documentation and resources around building a BinderHub._

- [![book-build](https://img.shields.io/badge/-book--build-8d7aef.svg)][labels-book-build] _These issues are related to the build of the book using Jupyter-book. They are also related to the-turing-way book repo._

- [![book-dash-feb20](https://img.shields.io/badge/-book--dash--feb20-006b75.svg)][labels-book-dash-feb20] _These are to be used on issues and PR during/for the book dash in Feb 2020._

- [![book-dash-ldn19](https://img.shields.io/badge/-book--dash--ldn19-e0b61f.svg)][labels-book-dash-ldn19] _These are issues related to contributions made during the London Book Dash in 2019._

- [![book-dash-mcr19](https://img.shields.io/badge/-book--dash--mcr19-f2a9c1.svg)][labels-book-dash-mcr19] _These are issues related to contributions made during the Manchester Book Dash in 2019._

- [![Bug](https://img.shields.io/badge/-bug-d73a4a.svg)][labels-bug] _These issues are reporting a problem or a mistake in the project._

  The more details you can provide the better!
  If you know how to fix the bug, please open an issue first and then submit a pull request :sparkles:

- [![bug-fixed](https://img.shields.io/badge/-bug%20fixed-cef298.svg)][labels-bug-fixed] _These are bugs that have been fixed and only need approval._

- [![collaboration-book](https://img.shields.io/badge/-collaboration--book-c877ff.svg)][labels-collaboration-book] _These issues relate to the content of the collaboration book._

- [![Comms](https://img.shields.io/badge/-comms-15c4b2.svg)][labels-comms] _These issues discuss how we as a project interact with other initiatives._

- [![communication-book](https://img.shields.io/badge/-communication--book-52d8d8.svg)][labels-communication-book] _These issues relate to the content of the communication book._

- [![Community](https://img.shields.io/badge/-community-8605c1.svg)][labels-community] _These issues relate to building and supporting the Turing Way community._

  This is all about collaborating, so please let us know how we can best support you as a community member.

- [![conflicting-file-error](https://img.shields.io/badge/-conflicting--file--error-a00819.svg)][labels-conflicting-file-error] _These issues mark issues and pull requests with conflicting files and errors._

- [![dependencies](https://img.shields.io/badge/-dependencies-0366d6.svg)][labels-dependencies] _These issues relate to pull requests that update a dependency file._

- [![Enhancement](https://img.shields.io/badge/-enhancement-84b6eb.svg)][labels-enhancement] _These issues are suggesting new features that can be added to the project._

  If you want to ask for something new, please try to make sure that your request is distinct from any others that are already in the queue (or part of _The Turing Way_).
  If you find one that's similar but there are subtle differences please reference the other enhancement in your issue.

- [![ethics-book](https://img.shields.io/badge/-ethics--book-5e6fbc.svg)][labels-ethics-book] _These issues relate to the content of the ethics book._

- [![events](https://img.shields.io/badge/-events-100570.svg)][labels-events] _These issues relate to coordinating workshops, book dashes and any other events._

- [![good-first-issue](https://img.shields.io/badge/-good%20first%20issue-1b3487.svg)][labels-firstissue] _These issues are particularly appropriate if it is your first contribution to _The Turing Way_, or to GitHub overall._

  If you're not sure about how to go about contributing, these are good places to start. You'll be mentored through the process by the maintainers team.
  If you're a seasoned contributor, please select a different issue to work from and keep these available for the newer and potentially more anxious team members.

- [![help-wanted](https://img.shields.io/badge/-help%20wanted-159818.svg)][labels-helpwanted] _These issues contain a task that a member of the team has determined we need additional help with._

  If you feel that you can contribute to one of these issues, we especially encourage you to do so!

- [![idea-for-discussion](https://img.shields.io/badge/-idea--for--discussion-a2f29b.svg)][labels-idea-for-discussion] _These issues can be used for inviting discussion from collaborators or community in general._

- [![newsletter](https://img.shields.io/badge/-newsletter-81e2c4.svg)][labels-newsletter] _These issues contain items that can be added to the newsletter._

- [![outreach](https://img.shields.io/badge/-Outreach-fcbae8.svg)][labels-outreach] _These issues relate to topics to reach out to the community._

- [![good-first-PR-review](https://img.shields.io/badge/-good--first--PR--review-C992E0.svg)][labels-good-first-PR-review] _These pull requests are for the new members of _The Turing Way_ community who want to start with reviewing and approving some simple pull requests._

If you are a new member of _The Turing Way_ and are looking for opportunities to start as a reviewer of contributions made on our Github repository, these pull requests are a great starting point for you. Issues like small modifications, typo errors and minor bug fixes are resolved by these PRs which are easy to review as a beginner.

- [![pr-draft](https://img.shields.io/badge/-PR%3A%20draft-6a737d.svg)][labels-pr-draft] _These issues relate to draft pull requests._

- [![pr-merged](https://img.shields.io/badge/-PR%3A%20merged-6f42c1.svg)][labels-pr-merged] _These issues relate to pull requests that have been merged._

- [![pr-partially-approved](https://img.shields.io/badge/-PR%3A%20partially--approved-7E9C82.svg)][labels-pr-partially-approved] _These issues relate to pull requests that have been partially approved._

- [![pr-reviewed-approved](https://img.shields.io/badge/-PR%3A%20reviewed--approved-0e8a16.svg)][labels-pr-reviewed-approved] _These issues relate to pull requests that have been approved by a reviewer._

- [![pr-reviewed-changes-requested](https://img.shields.io/badge/-PR%3A%20reviewed--changes--requested-c2e0c6.svg)][labels-pr-reviewed-changes-requested] _These issues relate tp pull requests for which a reviewer has requested changes._

- [![pr-unreviewed](https://img.shields.io/badge/-PR%3A%20unreviewed-fbca04.svg)][labels-pr-unreviewed] _These issues relate to pull requests that have not been reviewed yet._

- [![project-design-book](https://img.shields.io/badge/-project--design--book-3982cc.svg)][labels-project-design-book] _These issues relate to the content of the project design book._

- [![project-management](https://img.shields.io/badge/-project%20management-bfd86c.svg)][labels-project-management] _We like to model best practice, so _The Turing Way_ itself is managed through these issues.
  These issues help us to coordinate some logistics._

- [![question](https://img.shields.io/badge/-question-cc317c.svg)][labels-question] _These issues contain a question that you'd like to have answered._

  There are [lots of ways to ask questions](#get-in-touch) but opening an issue is a great way to start a conversation and get your answer.

- [![ready-for-merge](https://img.shields.io/badge/-ready%20for%20merge-32a320.svg)][labels-ready-for-merge] _These issues can be used after approving a pull request to let the author know that they can merge it._

- [![reproducibility-book](https://img.shields.io/badge/-reproducibility--book-c5bcff.svg)][labels-reproducibility-book] _These issues relate to the content of the reproducibility book._

- [![research-related-theory](https://img.shields.io/badge/-research--related--theory-72dbff.svg)][labels-research-related-theory] _These issues relate to the theoretical side of research best practices._

- [![review-request](https://img.shields.io/badge/-review%20request-ed0602.svg)][labels-review-request] _These relate to pull requests for urgent review requests, for example, to approve a report, abstract, and newsletter._

- [![software-skills](https://img.shields.io/badge/-software--skills-ed886f.svg)][labels-software-skills] _These relate to issues and pull requests that may need some software development, design, or troubleshooting skills._

- [![Tools](https://img.shields.io/badge/-tools-a3e07d.svg)][labels-tools] _These issues discuss the tools we use for collaboration_

  If you feel that we should try new tools or some aspects of the collaboration could be improved by using tools, please let us know.

- [![translation](https://img.shields.io/badge/-translation-e1ed3d.svg)][labels-translation] _These issues relate to translating the reproducibility book into other languages._

- [![Travel](https://img.shields.io/badge/-travel-0f42fc.svg)][labels-travel] _These issues are mainly for the attention of core project members to plan travel to face to face meetings_

- [![typo-fix](https://img.shields.io/badge/-typo--fix-ff54d4.svg)][labels-typo-fix] _These issues relate to fixing typos and broken links._

- [![work-in-progress](https://img.shields.io/badge/-work--in--progress-e08f72.svg)][labels-work-in-progress] _These issues are work in progress._

## Making a change with a pull request

We appreciate all contributions to _The Turing Way_.
**THANK YOU** for helping us build this useful resource. :sparkles::star2::dizzy:

All project management, conversations and questions related to _The Turing Way_ project happens here in [_The Turing Way_ repository][turing-way-repo].
This is also where you can contribute directly to writing or editing chapters of [the book](https://book.the-turing-way.org)!

The following steps are a guide to help you contribute in a way that will be easy for everyone to review and accept with ease :sunglasses:.

### 1. Comment on an [existing issue](https://github.com/the-turing-way/the-turing-way/issues) or open a new issue referencing your addition

This allows other members of _The Turing Way_ team to confirm that you aren't overlapping with work that's currently underway and that everyone is on the same page with the goal of the work you're going to carry out.

[This blog](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) is a nice explanation of why putting this work in upfront is so useful to everyone involved.

Remember, if you open a new issue, please follow our basic guidelines laid out in our [issue template](https://github.com/the-turing-way/the-turing-way/blob/main/.github/ISSUE_TEMPLATE/ISSUE_TEMPLATE.md).
The issue template will automatically be rendered in the comment section of the new issue page so all you need to do is edit the "_Lorem ipsum_" sections.

### 2. [Fork][github-fork] [_The Turing Way_ repository][turing-way-repo]

This is now your own unique copy of _The Turing Way_.
Changes here won't affect anyone else's work, so it's a safe space to explore edits to the code!

Make sure to [keep your fork up to date][github-syncfork] with the main repository, otherwise, you can end up with lots of dreaded [merge conflicts][github-mergeconflicts].
If you prefer working in the browser, [these instructions](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser) describe how to sync your fork to the original repository via GitHub.

### 3. Make the changes you've discussed

Try to keep the changes focused.
If you submit a large amount of work all in one go it will be much more work for whoever is reviewing your pull request.
[Help them help you.][jerry-maguire] :wink:

While making your changes, commit often and write good, detailed commit messages.
[This blog](https://chris.beams.io/posts/git-commit/) explains how to write a good Git commit message and why it matters.
It is also perfectly fine to have a lot of commits - including ones that break code.
A good rule of thumb is to push up to GitHub when you _do_ have passing tests then the continuous integration (CI) has a good chance of passing everything. 😸

If you feel tempted to "branch out" then please make a [new branch][github-branches] and a [new issue][turing-way-issues] to go with it. [This blog](https://nvie.com/posts/a-successful-git-branching-model/) details the different Git branching models.

Please do not re-write history!
That is, please do not use the [rebase](https://help.github.com/en/articles/about-git-rebase) command to edit previous commit messages, combine multiple commits into one, or delete or revert commits that are no longer necessary.

Are you new to Git and GitHub or just want a detailed guide on getting started with version control? Check out our [Version Control chapter](https://book.the-turing-way.org/version_control/version_control.html) in _The Turing Way_ Book!

### 4. Submit a [pull request][github-pullrequest]

We encourage you to open a pull request as early in your contributing process as possible.
This allows everyone to see what is currently being worked on.
It also provides you, the contributor, feedback in real-time from both the community and the continuous integration as you make commits (which will help prevent stuff from breaking).

When you are ready to submit a pull request, you will automatically see the [Pull Request Template](https://github.com/the-turing-way/the-turing-way/blob/main/.github/PULL_REQUEST_TEMPLATE.md) contents in the pull request body.
It asks you to:

- Describe the problem you're trying to fix in the pull request, reference any related issue and use fixes/close to automatically close them, if pertinent.
- List of changes proposed in the pull request.
- Describe what the reviewer should concentrate their feedback on.

By filling out the "_Lorem ipsum_" sections of the pull request template with as much detail as possible, you will make it really easy for someone to review your contribution!

If you have opened the pull request early and know that its contents are not ready for review or to be merged, add "[WIP]" at the start of the pull request title, which stands for "Work in Progress".
When you are happy with it and are happy for it to be merged into the main repository, change the "[WIP]" in the title of the pull request to "[Ready for review]".

A member of _The Turing Way_ team will then review your changes to confirm that they can be merged into the main repository.
A [review][github-review] will probably consist of a few questions to help clarify the work you've done.
Keep an eye on your GitHub notifications and be prepared to join in that conversation.

You can update your [fork][github-fork] of _The Turing Way_ [repository][turing-way-repo] and the pull request will automatically update with those changes.
You don't need to submit a new pull request when you make a change in response to a review.

You can also submit pull requests to other contributors' branches!
Do you see an [open pull request](https://github.com/the-turing-way/the-turing-way/pulls) that you find interesting and want to contribute to?
Simply make your edits on their files and open a pull request to their branch!

What happens if the continuous integration (CI) fails (for example, if the pull request notifies you that "Some checks were not successful")?
The CI could fail for a number of reasons.
At the bottom of the pull request, where it says whether your build passed or failed, you can click “Details” next to the test, which takes you to a CI run log site.
If you have the write access to the repo, you can view the log or rerun the checks by clicking the “Restart build” button in the top right.
You can learn more about CI in the [Continuous Integration chapter](https://book.the-turing-way.org/reproducible-research/ci.html)!

GitHub has a [nice introduction][github-flow] to the pull request workflow, but please [get in touch](#get-in-touch) if you have any questions :balloon:.

## The process of writing chapters

- Fork the repository from [`the-turing-way/the-turing-way`](https://github.com/the-turing-way/the-turing-way) if you have not done so already.
  - On your fork create a branch with the name as the chapter to be written and create a markdown file on it.
- If you are a contributor to the project repository, you can also create a branch on the main repository with the same name as the chapter to be written without creating a fork (or a local copy).
- Copy the relevant part of the [chapter template](https://github.com/the-turing-way/the-turing-way/tree/main/book/templates/chapter-template) into the markdown file, and commit.
- Make a pull request to _The Turing Way_ version of the chapter branch.
  The title of this request should have the form "[WIP] Write Chapter_name chapter".
  WIP indicates the chapter is a Work In Progress and not yet ready for review.
- On your branch add material to the chapter and commit.
  The goal of this project is to collate and build on the many good resources already available about good practice in data science.
  As such this material should primarily be drawn from outside sources.
  Note the link and (if available) license of the source.
- Once a significant amount of material has been amassed, work (preferably with others) to develop a chapter outline.
- Edit the amassed material into a coherent chapter, adding more material if gaps become apparent.
- Edit the chapter for style.
- Once the first draft of the chapter is complete change [WIP] in the pull request title to [Ready for review].
- Add a comment on the pull request indicating that this chapter is ready for high-level review, i.e discussion of changes of the scale of a paragraph or larger such as adding material and restructuring sections.
- Discuss and make these high-level changes on this pull request. Once this is complete merge the chapter into The _The Turing Way_'s version of the chapter branch.
- Make another pull request from your fork's version of the branch to _The Turing Way_'s version of the branch. Title this "[Ready for review] Chapter_name chapter- low-level reviews".
- Discuss and make low-level changes to the chapter on this pull request, such as rewording sentences, typos and the like.
- This division of the pull requests into high and low-level changes stops discussion threads from becoming unmanageable.
- Once this is complete merge the pull request into _The Turing Way_'s version of the chapter branch.
- Merge _The Turing Way_'s version of the chapter branch into _The Turing Way_'s main branch.
- DO not delete the branch as the chapter may continue to undergo improvement and development in the future.

## Local development

You can build and host the book website locally. The steps are:

### To build book locally

1. Install the required software to build the book, optionally in a [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments):

   ```
   pip install -r book/website/requirements.txt
   ```

2. You can now build or refresh the book using:

   ```
   cd ./book/website
   jupyter-book build .
   ```

## Style Guide

In _The Turing Way_'s [Community Handbook](https://book.the-turing-way.org/community-handbook/community-handbook.html), we have developed a style guide for the project.

[_The Turing Way_ style guide](https://book.the-turing-way.org/community-handbook/style.html) will provide guidance and supporting resources for ensuring consistency, readability and accessibility for all our users.

You are welcome to contribute to the style guide by opening [a new issue](https://github.com/the-turing-way/the-turing-way/issues/new/choose).

## Representing _The Turing Way_

We would LOVE people to give talks about the project or represent _The Turing Way_ in other ways!
We have created a [promotion pack](https://github.com/the-turing-way/the-turing-way/tree/main/communications/promotion-pack) for you to reuse.
You will find useful details about the project, a list of frequently asked questions, slide decks, and contact details.

If you would like to represent the project in your network, please open an issue and ping @aleesteele, @malvikasharan and @KirstieJane so
that they can do their best to support you.

We would appreciate if you could share a short abstract and your presentation by adding them to the
[conferences folder](/conferences) and some info in the [conferences README.md](/conferences/README.md).

## Recognising Contributions

We welcome and recognise all kinds of contributions, from fixing small errors, to developing documentation, maintaining the project infrastructure, writing chapters or reviewing existing resources.
In the [community handbook](https://book.the-turing-way.org/community-handbook/community-handbook.html), you can read how your contributions will be acknowledged and recorded in _The Turing Way_.
_The Turing Way_ follows the [all-contributors][all-contributors] specifications.
The all-contributors bot usage is described [here](https://allcontributors.org/docs/en/bot/usage).
You can see a list of current contributors [here](https://github.com/the-turing-way/the-turing-way/blob/main/contributors.md). 😍

To add yourself or someone else as a contributor, comment on the relevant Issue or Pull Request with the following:

```
@all-contributors please add <username> for <contributions>
```

You can see the [Emoji Key (Contribution Types Reference)](https://allcontributors.org/docs/en/emoji-key) for a list of valid `<contribution>` types and examples of how we've run this command in [this issue](https://github.com/the-turing-way/the-turing-way/issues/274).
The bot will then create a Pull Request to add the contributor and reply with the pull request details.

**PLEASE NOTE: Only one contributor can be added with the bot at a time!**
Add each contributor in turn, merge the pull request and delete the branch (`all-contributors/add-<username>`) before adding another one.
Otherwise, you can end up with dreaded [merge conflicts][github-mergeconflicts].
Therefore, please check the open pull requests first to make sure there aren't any [open requests from the bot](https://github.com/the-turing-way/the-turing-way/pulls/app%2Fallcontributors) before adding another.

What happens if you accidentally run the bot before the previous run was merged and you got those pesky merge conflicts?
(Don't feel bad, we have all done it! 🙈)
Simply close the pull request and delete the branch (`all-contributors/add-<username>`).
If you are unable to do this for any reason, please let us know on [Slack](https://tinyurl.com/jointuringwayslack), the [Gitter channel](https://gitter.im/the-turing-way/the-turing-way) or by opening an issue, and _The Turing Way_ team members will be very happy to help!

Finally, don't forget to add yourself to the list of contributors [here](https://github.com/the-turing-way/the-turing-way/blob/main/contributors.md)!

---

_These Contributing Guidelines have been adapted from the [Contributing Guidelines](https://github.com/bids-standard/bids-starter-kit/blob/master/CONTRIBUTING.md) of the [BIDS Starter Kit](https://github.com/bids-standard/bids-starter-kit)! (License: CC-BY)_

[turing-way-repo]: https://github.com/the-turing-way/the-turing-way/
[turing-way-book-repo]: https://github.com/the-turing-way/the-turing-way-book/
[turing-way-issues]: https://github.com/the-turing-way/the-turing-way/issues
[turing-way-labels]: https://github.com/the-turing-way/the-turing-way/labels
[git]: https://git-scm.com
[github]: https://github.com
[github-branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[github-fork]: https://help.github.com/articles/fork-a-repo
[github-flow]: https://guides.github.com/introduction/flow
[github-mergeconflicts]: https://help.github.com/articles/about-merge-conflicts
[github-pullrequest]: https://help.github.com/articles/creating-a-pull-request
[github-review]: https://help.github.com/articles/about-pull-request-reviews
[github-syncfork]: https://help.github.com/articles/syncing-a-fork
[issue-template]: https://github.com/the-turing-way/the-turing-way/blob/main/ISSUE_TEMPLATE.md
[labels-link]: https://github.com/the-turing-way/the-turing-way/labels
[labels-approval-request]: https://github.com/the-turing-way/the-turing-way/labels/approval%20request
[labels-binderhub]: https://github.com/the-turing-way/the-turing-way/labels/binderhub
[labels-book-build]: https://github.com/the-turing-way/the-turing-way/labels/book%2Dbuild
[labels-book-dash-feb20]: https://github.com/the-turing-way/the-turing-way/labels/book%2Ddash%2Dfeb20
[labels-book-dash-ldn19]: https://github.com/the-turing-way/the-turing-way/labels/book%2Ddash%2Dldn2019
[labels-book-dash-mcr19]: https://github.com/the-turing-way/the-turing-way/labels/book%2Ddash%2Dmcr2019
[labels-book]: https://github.com/the-turing-way/the-turing-way/labels/book
[labels-bug]: https://github.com/the-turing-way/the-turing-way/labels/bug
[labels-bug-fixed]: https://github.com/the-turing-way/the-turing-way/labels/bug%20fixed
[labels-collaboration-book]: https://github.com/the-turing-way/the-turing-way/labels/collaboration%2Dbook
[labels-communication-book]: https://github.com/the-turing-way/the-turing-way/labels/communication%2Dbook
[labels-community]: https://github.com/the-turing-way/the-turing-way/labels/community
[labels-comms]: https://github.com/the-turing-way/the-turing-way/labels/comms
[labels-conflicting-file-error]: https://github.com/the-turing-way/the-turing-way/labels/conflicting%2Dfile%2Derror
[labels-dependencies]: https://github.com/the-turing-way/the-turing-way/labels/dependencies
[labels-enhancement]: https://github.com/the-turing-way/the-turing-way/labels/enhancement
[labels-ethics-book]: https://github.com/the-turing-way/the-turing-way/labels/ethics%2Dbook
[labels-events]: https://github.com/the-turing-way/the-turing-way/labels/events
[labels-firstissue]: https://github.com/the-turing-way/the-turing-way/labels/good%20first%20issue
[labels-helpwanted]: https://github.com/the-turing-way/the-turing-way/labels/help%20wanted
[labels-idea-for-discussion]: https://github.com/the-turing-way/the-turing-way/labels/idea%2Dfor%2Ddiscussion
[labels-good-first-PR-review]: https://github.com/the-turing-way/the-turing-way/labels/good%2Dfirst%2PR%2review
[labels-jupyter]: https://github.com/the-turing-way/the-turing-way/labels/jupyter
[labels-project-management]: https://github.com/the-turing-way/the-turing-way/labels/project%20management
[labels-newsletter]: https://github.com/the-turing-way/the-turing-way/labels/newsletter
[labels-outreach]: https://github.com/the-turing-way/the-turing-way/labels/Outreach
[labels-pr-draft]: https://github.com/the-turing-way/the-turing-way/labels/PR%3A%20draft
[labels-pr-merged]: https://github.com/the-turing-way/the-turing-way/labels/PR%3A%20merged
[labels-pr-partially-approved]: https://github.com/the-turing-way/the-turing-way/labels/PR%3A%20partially%2Dapproved
[labels-pr-reviewed-approved]: https://github.com/the-turing-way/the-turing-way/labels/PR%3A%20reviewed%2Dapproved
[labels-pr-reviewed-changes-requested]: https://github.com/the-turing-way/the-turing-way/labels/PR%3A%20reviewed%2Dchanges%2Drequested
[labels-pr-unreviewed]: https://github.com/the-turing-way/the-turing-way/labels/PR%3A%20unreviewed
[labels-project-design-book]: https://github.com/the-turing-way/the-turing-way/labels/project%2Ddesign%2Dbook
[labels-question]: https://github.com/the-turing-way/the-turing-way/labels/question
[labels-ready-for-merge]: https://github.com/the-turing-way/the-turing-way/labels/ready%20for%20merge
[labels-reproducibility-book]: https://github.com/the-turing-way/the-turing-way/labels/reproducibility%2Dbook
[labels-research-related-theory]: https://github.com/the-turing-way/the-turing-way/labels/research%2Drelated%2Dtheory
[labels-review-request]: https://github.com/the-turing-way/the-turing-way/labels/review%20request
[labels-software-skills]: https://github.com/the-turing-way/the-turing-way/labels/software%2Dskills
[labels-tools]: https://github.com/the-turing-way/the-turing-way/labels/tools
[labels-translation]: https://github.com/the-turing-way/the-turing-way/labels/translation
[labels-travel]: https://github.com/the-turing-way/the-turing-way/labels/travel
[labels-typo-fix]: https://github.com/the-turing-way/the-turing-way/labels/typo%2Dfix
[labels-work-in-progress]: https://github.com/the-turing-way/the-turing-way/labels/work%2Din%2Dprogress
[labels-workshops]: https://github.com/the-turing-way/the-turing-way/labels/workshops
[markdown]: https://daringfireball.net/projects/markdown
[rick-roll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[jerry-maguire]: https://media.giphy.com/media/uRb2p09vY8lEs/giphy.gif
[all-contributors]: https://github.com/kentcdodds/all-contributors#emoji-key
