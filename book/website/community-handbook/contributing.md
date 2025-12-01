(ch-contributing)=
# Contributing to _The Turing Way_

🎉🎈🍰 **Welcome to _The Turing Way_!** 🍰🎈🎉

💫 _We're excited that you're here and want to contribute._ 💫

We want to ensure that every user and contributor feels welcome, included and supported to participate in _The Turing Way_ community.
We hope that the information provided in this document will make it as easy as possible for you to get involved.

We welcome all contributions to this project via {term}`GitHub` {term}`issues` and {term}`pull requests <pull request>`.
Please follow these guidelines to make sure your contributions can be easily integrated into the projects.
As you start contributing to _The Turing Way_, don't forget that your ideas are more important than perfect {term}`pull requests <pull request>`. ❤️

If you have any questions that aren't discussed below, please let us know through one of the many ways to [get in touch](#ch-contributing-join).

## Guiding Principles and Code of Conduct

_The Turing Way_ is a community-led and collaboratively developed project.
We, therefore, require that all our members and their contributions **adhere to our [guiding principles](#guiding-principles) and {term}`CoC <Code of Conduct>`**.
Please familiarize yourself with [our guiding principles](#guiding-principles), which underpin all our activities, and [our {term}`CoC <Code of Conduct>`](#ch-coc), which lists the expected behaviours and explains reporting and enforcement.

## Inclusivity

_The Turing Way_ aims to be inclusive to people from all walks of life and to all research fields.
These intentions must be reflected in the contributions that we make to the project.

In addition to the {term}`CoC <Code of Conduct>`, we encourage intentional, inclusive actions from contributors to _The Turing Way_.
For example, you should:

- Use respectful, gender-neutral and inclusive language.
- Aim to include perspectives of researchers from different research backgrounds.
- Make sure that the colour palettes are accessible to colour-blind readers and contributors.
  See the blog post [Designing Scientific Figures for Colour Blindness](https://www.lewismackenzie.science/updates-1/2017/2/9/designing-scientific-figures-for-colour-blindness) for an example of how somebody improved one of their diagrams, including links to recommended colour palettes and a colour-blindness simulator.

(ch-contributing-join)=
## Join the Community

There are many ways to engage with the community!
We maintain a set of useful resources and announcements at [the-turing-way.org](https://the-turing-way.org).

### Slack

We use [Slack](https://slack.the-turing-way.org) for more informal and rapid communication.
There are channels for working groups, asking for support, and community discussion.
There are also off-topic channels for socialising with other community members.
Slack is also a good place to receive notifications for upcoming events.

### Newsletter

You can sign up to our [newsletter](https://news.the-turing-way.org) to receive monthly project updates.

### GitHub

_The Turing Way_ is developed on [GitHub](https://git.the-turing-way.org).
We use {term}`GitHub` [discussion](https://github.com/orgs/the-turing-way/discussions), [issues](https://github.com/the-turing-way/the-turing-way/issues) and [pull requests](https://github.com/the-turing-way/the-turing-way/pulls) to organise ideas and contributions.
[](#ch-contributing-github) and [](#ch-contributing-pull-request) explain how to use these features.

### Coworking and Real-Time Collaboration

_The Turing Way_ hosts synchronous events using video conferencing for focused collaboration.
These include working group meetings, regular [collaboration cafes](#ch-community-calls-collabcafe) and week-long [Book Dash](#ch-bookdash) sprint events.
These events can be found on the [community calendar](https://calendar.the-turing-way.org).

### Email

You can also contact the Community Management Working Group and the Steering Committee by emailing [theturingway@gmail.com](mailto:theturingway@gmail.com).

(ch-contributing-github)=
## Collaborating on GitHub

[Git](https://git-scm.com) is a really useful tool for version control.
[GitHub](https://github.com) sits on top of {term}`Git` and supports collaborative and distributed working.
It can be daunting to start using {term}`Git` and {term}`GitHub` if you haven't worked with them in the past.
We are here to help if you encounter problems! ❤️

In order to contribute via {term}`GitHub`, you'll need to create a free account.
Read the [GitHub documentation](https://help.github.com/articles/signing-up-for-a-new-github-account/) for instructions.

## Issues and Discussions

Look through open items first; join discussions, collaborate on an ongoing tasks and exchange your thoughts with others.
If you can't find an open item related to your idea, you can open a new one.
Open and discussion if you have a question, or an idea to talk about with the community.
Open an {term}`issue <issues>` if you have a specific task like fixing a bug or editing part of the book.
Our [issue templates](https://github.com/the-turing-way/the-turing-way/issues/new/choose) guide you to add the important information.

### Good First Issues

We mark {term}`issues` suitable for first contributions with the [good first issue](https://github.com/the-turing-way/the-turing-way/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) label.

### Good First Pull Requests

If you would like opportunities to {term}`review` others' contributions, we mark good {term}`pull requests <pull request>` for new reviewers with the [good first PR review](https://github.com/the-turing-way/the-turing-way/pulls?q=is%3Aopen+is%3Apr+label%3A%22good+first+PR+review%22) label.

## Writing Markdown

_The Turing Way_ is written almost entirely in {term}`Markdown`.
In particular, it is written in a flavour of {term}`Markdown` called [MyST Markdown](https://mystmd.org/).

The [Style Guide](#ch-style) section of the Community Handbook explains our conventions and recommendations for writing {term}`Markdown`.
You can also read the [Authoring section of the MyST Markdown Guide](xref:myst-guide) for the complete set of features and {term}`syntax`.

(ch-contributing-pull-request)=
## Making Changes with a Pull Request

Changes to the book are always made through {term}`pull requests <pull request>`.
We encourage all contributors to work on their own fork of the repository.
Pull requests should be self-contained and as small as possible.

Pull request should be marked as drafts until there are ready for {term}`review`.

We follow the [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) workflow:

1. Create a feature branch on your fork.
2. Commit changes.
3. Open a {term}`pull request` to _The Turing Way_'s repository.
  - Open a draft {term}`pull request` if the work is still in progress.
  - Open a {term}`pull request` if you feel the work is ready for {term}`review`.
  - Complete the {term}`pull request` template to provide information useful for reviewers.
4. Iterate on changes in response to {term}`continuous integration` and reviewer comments.
5. Merge when all {term}`issues` are addressed and changes are approved.

### Best Practice

Here are some tips for best practice working with git:

- [Keep your fork up to date](https://help.github.com/articles/syncing-a-fork) with the main repository
- Try to keep changes focused.
  If you submit many changes at once it will be much more difficult to {term}`review`.
- Make small {term}`commits <commit>` often.
- Write [good {term}`commit` messages](https://chris.beams.io/git-commit).
- Do not re-write history!
- Open draft {term}`pull requests <pull request>` soon, to get early feedback.

(ch-contributing-low-effort)=
### Low Effort or Engagement

An important part of our community is putting in effort to mentoring contributors, particularly those new to open source.
However, we also need to protect our maintainers' time so they do not get burned out reviewing poor quality contributions or trying to mentor unengaged contributors.
And so, pull requests may be closed if we feel they are unlikely to result in a _tangible improvement_ to the book, or the maintainer investment required would not match the value of the contribution.

:::{important}
There is no size threshold for contributions to be accepted.
For example, single typo fixes are great contributions.
:::

Features that mark a contribution as low effort include:

- Mostly or entirely superficial changes, such as whitespace changes or replacing words with synonyms.
- Ignoring book structure and the [style guide](#ch-style), such as not updating the table of contents, or ignoring directory structure.
- Apparently machine-generated contributions with little or no human effort to review and edit.
  This may be apparent in comments as:
    - Irrelevant, unclear text.
    - Disconnection between {term}`pull request` comments describing changes and actual changes made to the  files.
    - Hallucinated references.
  And in code/contributions as:
    - Verbose and vague text.
    - Long sections of plain text lacking, for example, cross-references, citations, figures, admonitions.
    - Hallucinated references.

Features that mark a contribution as low engagement include:

- Not responding to reviewers.
- Ignoring reviewers and instead making unrelated changes.

### Chapter Templates

If you are writing a new chapter, make use of the [chapter template](https://github.com/the-turing-way/the-turing-way/tree/main/book/templates/chapter-template).

### Local development

You can build the book locally during development.
This is the quickest way to see how you changes affect the book.
The steps are described in [](#ch-local-build).

(ch-contributing-recognising)=
## Recognising Contributions

We welcome and recognise all kinds of contributions, from fixing small errors, to developing documentation, maintaining the project infrastructure, writing chapters or {term}`reviewing <review>` existing resources.
The [community handbook](#ch-acknowledgement) explains how contributions will be acknowledged and recorded in _The Turing Way_.

To add yourself or someone else as a {term}`contributor <contributors>`, comment on the relevant {term}`issue <issues>` or pull request with the following:

```none
@all-contributors please add <username> for <contributions>
```

You can see the [Emoji Key (Contribution Types Reference)](https://allcontributors.org/docs/en/emoji-key) for a list of valid `<contribution>` types and examples of how we've run this command in [this issue](https://github.com/the-turing-way/the-turing-way/issues/274).
The bot will then create a {term}`pull request` to add the contributor and reply with the pull request details.

:::{warning} Please only add one contributor at a time with the bot!
Add each contributor in turn, merge the pull request and delete the branch (`all-contributors/add-<username>`) before adding another one.
Otherwise, the {term}`pull requests <pull request>` will tend to have merge conflicts.
Therefore, please check the open {term}`pull requests <pull request>` first to make sure there aren't any [open requests from the bot](https://github.com/the-turing-way/the-turing-way/pulls/app%2Fallcontributors) before adding another.
:::

Finally, don't forget to add yourself to the [list of contributors](#contributors-record)!
