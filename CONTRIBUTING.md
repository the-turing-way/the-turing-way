# Contributing to the Turing Way

:tada::balloon::cake: **Welcome to the Turing Way repository!** :cake::balloon::tada:

:dizzy::hatched_chick::sunny: *We're so excited you're here and want to contribute.* :sunny::hatched_chick::dizzy:

The point of this guide is to **welcome new users and contributors to the Turing Way community**. We hope that these guidelines are designed to make it as easy as possible to get involved. Don't let trying to be perfect get in the way of being good - we welcome all contributions and would love it if you could follow these guidelines to make sure your contributions can be easily integrated but exciting ideas are more important than perfect pull requests. :heart:


If you have any questions that aren't discussed below, please let us know through one of the many ways to [get in touch](#get-in-touch).

## Table of contents

Been here before? Already know what you're looking for in this guide? Jump to the following sections:

* [Joining the community](#joining-the-community)
* [Inclusivity](#inclusivity)
* [Get in touch](#get-in-touch)
* [Contributing through GitHub](#contributing-through-github)
* [Where to start: issues](#where-to-start-issues)
* [Making a change with a pull request](#making-a-change-with-a-pull-request)
* [Become a maintainer](#become-a-maintainer)
* [The process of writing chapters](#the-process-of-writing-chapters)

## Joining the community

The Turing Way is a community-oriented and -led project.
We therefore require that all contributions **adhere to our [Code of Conduct](CODE_OF_CONDUCT.md)**.

## Inclusivity

This project aims to be inclusive to people from all walks of life and to all research fields.
This should be taken into account in contributions.

The following are examples of inclusive actions that we encourage from contributors to the Turing Way:

* Refer to "open research" rather than "open science" so that we do not exclude members of the humanities and social sciences from our community.
* Make sure colour pallettes are accessible to colour-blind readers and contributors.
  Here's a useful blog post on [tips for designing scientific figures for color blind readers](http://www.somersault1824.com/tips-for-designing-scientific-figures-for-color-blind-readers) by Luk at [Somersulat 1824](http://www.somersault1824.com).

## Get in touch

Ping us in our [gitter channel](https://gitter.im/alan-turing-institute/the-turing-way).
You can also contact the PI of the Turing Way project - Kirstie Whitaker - by email at kwhitaker@turing.ac.uk.

## Contributing through GitHub

[Git][git] is a really useful tool for version control. [GitHub][github] sits on top of Git and supports collaborative and distributed working.

We know that it can be daunting to start using Git and GitHub if you haven't worked with them in the past, but the The Turing Way maintainers are here to help you figure out any of the jargon or confusing instructions you encounter! :heart:

In order to contribute via GitHub you'll need to set up a free account and sign in. Here are some [instructions](https://help.github.com/articles/signing-up-for-a-new-github-account/) to help you get going. Remember that you can ask us any questions you need to along the way.

## Writing in Markdown

GitHub has a helpful page on [getting started with writing and formatting on GitHub](https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github).

Most of the writing that you'll do will be in [Markdown][markdown].
You can think of Markdown as a few little symbols around your text that will allow GitHub to render the text with a little bit of formatting.
For example you could write words as **bold** (`**bold**`), or in *italics* (`*italics*`), or as a [link][rick-roll] (`[link](https://https://youtu.be/dQw4w9WgXcQ)`) to another webpage.
Also when writing in Markdown, please start each new sentence on a new line.
While this formats in the same way as if the new line wasn't included, it makes the diffs produced during the pull request review easier to read! :sparkles:

## Where to start: issues

Before you open a new issue, please check if any of the open issues covers your idea already.
If you open a new issue, please follow our basic guidelines laid out in our [issue template](https://github.com/alan-turing-institute/the-turing-way/blob/master/.github/ISSUE_TEMPLATE.md).

### Issue labels

The list of labels for current issues can be found [here][turing-way-labels] and includes:

* [![help-wanted](https://img.shields.io/badge/-help%20wanted-159818.svg)][labels-helpwanted] *These issues contain a task that a member of the team has determined we need additional help with.*

    If you feel that you can contribute to one of these issues, we especially encourage you to do so!

* [![question](https://img.shields.io/badge/-question-cc317c.svg)][labels-question] *These issues contain a question that you'd like to have answered.*

    There are [lots of ways to ask questions](#get-in-touch) but opening an issue is a great way to start a conversation and get your answer.

* [![good-first-issue](https://img.shields.io/badge/-good%20first%20issue-1b3487.svg)][labels-firstissue] *These issues are particularly appropriate if it is your first contribution to the Turing Way, or to GitHub overall.*

    If you're not sure about how to go about contributing, these are good places to start. You'll be mentored through the process by the maintainers team.
    If you're a seasoned contributor, please select a different issue to work from and keep these available for the newer and potentially more anxious team members.

* [![Enhancement](https://img.shields.io/badge/-enhancement-84b6eb.svg)][labels-enhancement] *These issues are suggesting new features that can be added to the project.*

    If you want to ask for something new, please try to make sure that your request is distinct from any others that are already in the queue (or part of the Turing Way).
    If you find one that's similar but there are subtle differences please reference the other enhancement in your issue.

* [![Community](https://img.shields.io/badge/-community-8605c1.svg)][labels-community] *These issues relate to building and supporting the Turing Way community.*

     This is all about collaborating, so please let us know how we can best support you as a community member.

* [![Bug](https://img.shields.io/badge/-bug-d73a4a.svg)][labels-bug] *These issues are reporting a problem or a mistake in the project.*

    The more details you can provide the better!
    If you know how to fix the bug, please open an issue first and then submit a pull request :sparkles:

* [![Book](https://img.shields.io/badge/-book-c5bcff.svg)][labels-book] *These issues cover everything around the process of writing the book.*

* [![workshops](https://img.shields.io/badge/-workshops-c1663c.svg)][labels-workshops] *These issues help us organise our workshops.*

* [![project-management](https://img.shields.io/badge/-project%20management-bfd86c.svg)][labels-project-management] *We like to model best practice, so the Turing Way itself is managed through these issues.
These issues help us to coordinate some logistics.*

* [![jupyter](https://img.shields.io/badge/-jupyter-F37726.svg)][labels-jupyter] *Everything related to building a BinderHub*

* [![Tools](https://img.shields.io/badge/-tools-a3e07d.svg)][labels-tools] *These issues discuss tools we use for collaboration*

    If you feel that we should try new tools or some aspects of the collaboration could be improved by using tools, please let us know.

* [![Travel](https://img.shields.io/badge/-travel-0f42fc.svg)][labels-travel] *These issues are mainly for the attention of core project members to plan travel to face to face meetings*

* [![Comms](https://img.shields.io/badge/-comms-15c4b2.svg)][labels-comms] *These issues discuss how we as a project interact with other initiatives.*



## Making a change with a pull request
> Still needs to cover:
> - Open pull requests early
> - Use the WIP marker if you're not ready for the review
> - You can submit pull requests to the OTHER PERSON'S BRANCH.

*This section has been adapted from the [Contributing Guidelines](https://github.com/bids-standard/bids-starter-kit/blob/master/CONTRIBUTING.md) of the [BIDS Starter Kit](https://github.com/bids-standard/bids-starter-kit)! (License: CC-BY)*

We appreciate all contributions to the Turing Way.
**THANK YOU** for helping us build this useful resource. :sparkles::star2::dizzy:

All project management, conversations and questions related to the Turing Way project happens here in the [Turing Way repository][turing-way-repo].
If you want to contribute directly to writing or editing chapters of the book, please head over to the Turing Way [book repository][turing-way-book-repo]!

The following steps are a guide to help you contribute in a way that will be easy for everyone to review and accept with ease  :sunglasses:.


#### 1. Comment on an existing issue or open a new issue referencing your addition

This allows other members of the Turing Way team to confirm that you aren't overlapping with work that's currently underway and that everyone is on the same page with the goal of the work you're going to carry out.

[This blog](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) is a nice explanation of why putting this work in up front is so useful to everyone involved.

#### 2. [Fork][github-fork] the [Turing Way repository][turing-way-repo] to your profile

This is now your own unique copy of the Turing Way.
Changes here won't affect anyone else's work, so it's a safe space to explore edits to the code!

Make sure to [keep your fork up to date][github-syncfork] with the master repository, otherwise you can end up with lots of dreaded [merge conflicts][github-mergeconflicts].
If you prefer working in the browser, [these instructions](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser) describe how to sync your fork to the original repository via GitHub.

#### 3. Make the changes you've discussed

Try to keep the changes focused.
If you submit a large amount of work all in one go it will be much more work for whomever is reviewing your pull request.
[Help them help you.][jerry-maguire] :wink:

While making your changes, commit often and write good, detailed commit messages.
[This blog](https://chris.beams.io/posts/git-commit/) explains how to write a good Git commit message and why it matters.
It is also perfectly fine to have a lot of commits - including ones that break code.
A good rule of thumb is to push up to GitHub when you *do* have passing tests then the continuous integration (CI) has a good chance of passing everything. 😸

If you feel tempted to "branch out" then please make a [new branch][github-branches] and a [new issue][turing-way-issues] to go with it. [This blog](https://nvie.com/posts/a-successful-git-branching-model/) details the different Git branching models.

Are you new to Git and GitHub or just want a detailed guide on getting started with version control? Check out our [Version Control chapter](https://the-turing-way.netlify.com/version_control/version_control.html) in the Turing Way Book!

#### 4. Submit a [pull request][github-pullrequest]

When you are ready to submit a pull request, will automatically see the [Pull Request Template](https://github.com/alan-turing-institute/the-turing-way/blob/master/.github/PULL_REQUEST_TEMPLATE.md) contents in the pull request body.
It asks you to:
* Describe the problem you're trying to fix in the pull request, reference any related issue and use fixes/close to automatically close them, if pertinent.
* List of changes proposed in the pull request.
* Describe what the reviewer should concentrate their feedback on.

A member of the Turing Way team will then review your changes to confirm that they can be merged into the main repository.

A [review][github-review] will probably consist of a few questions to help clarify the work you've done.
Keep an eye on your GitHub notifications and be prepared to join in that conversation.

You can update your [fork][github-fork] of the Turing Way [repository][turing-way-repo] and the pull request will automatically update with those changes.
You don't need to submit a new pull request when you make a change in response to a review.

GitHub has a [nice introduction][github-flow] to the pull request workflow, but please [get in touch](#get-in-touch) if you have any questions :balloon:.


## The process of writing chapters

- Fork the repository form the alan turing version if you have not done so already.
- On the alan turing version create a branch with the same name as the chapter to be written.
- On your fork create a branch with the same name and create a markdown file on it.
- Copy the chapter template in the templates directory into the markdown file, and commit.
- Make a pull request to the turing way version of the chapter branch.
The title of this request should have the form "[WIP] Write Chapter_name chapter".
WIP indicates the chapter is a Work In Progress and not yet ready for review.
- On your branch add material to the chapter and commit.
The goal of this project is to collate and build on the many good resources already available about good practise in data science.
As such this material should primarily be drawn from outside sources.
Note the link and (if available) license of the source.
- Once a significant amount of material has been amassed, work (preferably with others) to develop a chapter outline.
- Edit the amassed material into a coherent chapter, adding more material if gaps become apparent.
- Edit the chapter for style.
- Once the first draft of the chapter is complete change [WIP] in the pull request title to [Ready for review].
- Add a comment on the pull request indicating that this chapter is ready for high level review, i.e discussion of changes of scale of a paragraph or larger such as adding material and restructuring sections.
- Discuss and make these high level changes on this pull request. Once this is complete merge the chapter into the alan turing intitute's version of the chapter branch.
- Make another pull request from your fork's version of the branch to the alan turing institute's version of the branch. Title this "[Ready for review] Chapter_name chapter- low level reviews".
- Discuss and make low level changes to the chapter on this pull request, such as rewording sentences, typos and the like.
- This division of the pull requests into high and low level changes stops discussion threads becoming unmanagably long.
- Once this is complete merge the pull request into the alan turing intitute's version of the chapter branch.
- Merge the alan turing intitute's version of the chapter branch into the alan turing master branch.
DO not delete the branch as the chapter may continue to undergo improvement and development in the future.


## Style Guide
### Writing style
To ensure all text can be read easily by all (including screen readers and non-native english speakers), follow Gov.uk guidance on e.g., i.e., and etc. (1)
That is, do not use them:

eg can sometimes be read aloud as ‘egg’ by screen reading software. Instead use ‘for example’ or ‘such as’ or ‘like’ or ‘including’ - whichever works best in the specific context.

etc can usually be avoided.
Try using ‘for example’ or ‘such as’ or ‘like’ or ‘including’.
Never use etc at the end of a list starting with these words.

ie - used to clarify a sentence - is not always well understood.
Try (re)writing sentences to avoid the need to use it. If that is not possible, use an alternative such as ‘meaning’ or ‘that is’.

1. https://www.gov.uk/guidance/style-guide/a-to-z-of-gov-uk-style#eg-etc-and-ie


### Sentences
When writing all sentences should go on a new line.
This will make no difference to how the text is displayed, there will still be paragraphs, but it will mean that any pull requests will be easier to check; the changes will be on a single line instead of somewhere in a paragraph. Consider the example below.

```
Today you are you, that is truer than true. There is no one alive who is youer than you. - Dr Seuss
```
A pull request on this correcting it to have a ‘.’ after Dr would show as a change to the whole paragraph.
Contrast this with the next example which will be displayed online in the exact same way, but would see a change to a single line.

```
Today you are you, that is truer than true.
There is no one alive who is youer than you.
- Dr Seuss
```

### Opinions
The Turing Way book is intended to be only lightly opinionated.
Whilst more opinionated content is allowed, such content should be clearly marked.
The best way to do this is by displaying it in a quote box.
This can be done by either prefixing every line with the greater than symbol ```>```.
Note, that the formatting will be retained, so we can split each sentence to a new line as recommended before.

```
> I will not eat them in a house,
> i will not eat them with a mouse,
> i will not eat them in a box i will not eat them with a fox,
> i will not eat them here of there i will not eat them anywhere,
> I do not like green eggs and ham i do not like them sam i am
```

### Figures
To make things look cleaner, it is advised that all figures be encapsulated in a table with a caption.
This can be done simply as:

```
| ![A dish with Green Eggs and Ham](green_eggs_ham.jpg)         |
| ------------------------------------------------------------------------------------ |
| Try them, try them, and you may! Try them and you may, I say.  |
```

### Referencing and Citing

To Be Done.


## Recognising contributions

The Turing Way follows the [all-contributors][all-contributors] specification, so we welcome and recognise all contributions from documentation to testing to writing chapters.
You can see a list of current contributors [here](https://github.com/alan-turing-institute/the-turing-way/blob/master/contributors.md). 😍




[turing-way-repo]: https://github.com/alan-turing-institute/the-turing-way/
[turing-way-book-repo]:https://github.com/alan-turing-institute/the-turing-way-book/
[turing-way-issues]: https://github.com/alan-turing-institute/the-turing-way/issues
[turing-way-labels]: https://github.com/alan-turing-institute/the-turing-way/labels
[git]: https://git-scm.com
[github]: https://github.com
[github-branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[github-fork]: https://help.github.com/articles/fork-a-repo
[github-flow]: https://guides.github.com/introduction/flow
[github-mergeconflicts]: https://help.github.com/articles/about-merge-conflicts
[github-pullrequest]: https://help.github.com/articles/creating-a-pull-request
[github-review]: https://help.github.com/articles/about-pull-request-reviews
[github-syncfork]: https://help.github.com/articles/syncing-a-fork
[issue-template]: https://github.com/alan-turing-institute/the-turing-way/blob/master/ISSUE_TEMPLATE.md
[labels-link]: https://github.com/alan-turing-institute/the-turing-way/labels
[labels-book]: https://github.com/alan-turing-institute/the-turing-way/labels/book
[labels-bug]: https://github.com/alan-turing-institute/the-turing-way/labels/bug
[labels-community]: https://github.com/alan-turing-institute/the-turing-way/labels/community
[labels-comms]: https://github.com/alan-turing-institute/the-turing-way/labels/comms
[labels-enhancement]: https://github.com/alan-turing-institute/the-turing-way/labels/enhancement
[labels-firstissue]: https://github.com/alan-turing-institute/the-turing-way/labels/good%20first%20issue
[labels-helpwanted]: https://github.com/alan-turing-institute/the-turing-way/labels/help%20wanted
[labels-jupyter]: https://github.com/alan-turing-institute/the-turing-way/labels/jupyter
[labels-project-management]: https://github.com/alan-turing-institute/the-turing-way/labels/project%20management
[labels-question]: https://github.com/alan-turing-institute/the-turing-way/labels/question
[labels-tools]: https://github.com/alan-turing-institute/the-turing-way/labels/tools
[labels-travel]: https://github.com/alan-turing-institute/the-turing-way/labels/travel
[labels-workshops]: https://github.com/alan-turing-institute/the-turing-way/labels/workshops
[markdown]: https://daringfireball.net/projects/markdown
[rick-roll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[jerry-maguire]: https://media.giphy.com/media/uRb2p09vY8lEs/giphy.gif
[all-contributors]: https://github.com/kentcdodds/all-contributors#emoji-key
