# Creating a newsletter

This document provides an overview of a process we use in _The Turing Way_ for drafting, reviewing and publishing newsletters.
Though written for _The Turing way_, these steps can be adapted for documenting newsletters for any project.

We only suggest using these recommendations as guides.
These should not be considered as a set of fixed rules or the "only" way one should create newsletters.
As individual authors, you should allow your personality to show in your newsletter drafts.
After all, these newsletters land in someone's personal mailbox and most likely they know you (or your community).

## Steps for drafting _The Turing Way_ newsletters

### Create a GitHub issue to collect items

Create a new GitHub issue where throughout the month you and other community members can suggest news items as a comment.
For example, in [this issue](https://github.com/the-turing-way/the-turing-way/issues/1037), several members could suggest news items to include in the next newsletter, in this case for June 2020.
Such GitHub issues can be published in the current newsletter inviting contributions from readers and community members for the next month.

### Start a draft

There are several ways to start a draft for a _The Turing Way_ newsletter:

1. Create a new branch of _The Turing Way_ [GitHub repository](https://github.com/the-turing-way/the-turing-way/) within the appropriate directory (explained in the next subchapter on {ref}`newsletter's style guide <ch-newsletters-style>`).

You can work on this GitHub branch locally or online through a pull request (PR).
If working online, please keep the draft mode on for your PR or add "[WIP]" (work in progress) in the title.

2. Create the first draft on a shared HackMD when working with others to collaboratively write your draft before you transfer them to a GitHub branch.

Here are two examples of HackMDs:
- Malvika's first draft: https://hackmd.io/@malvikasharan/tw-newsletter
- Anne's first draft (April 2022): https://hackmd.io/@aleesteele/ttw-newsletter-apr-22.

### Collect items for the newsletter as bullet points

Based on what we currently publish, collect information from the listed resources for the topics described below (they can be presented in a format agreed with *The Turing Way* staff):

* **Community meetings**: review the [community calendar](https://calendar.google.com/calendar/embed?src=theturingway%40gmail.com&ctz=Europe%2FLondon) for upcoming events such as Collaboration Cafés, book dashes and workshops.

* **News from the community**:
  - Check X (formerly Twitter) for updates on the [official account](https://twitter.com/turingway) and the [#TuringWay Hashtag](https://twitter.com/hashtag/TuringWay?src=hashtag_click)
  - Check Mastodon for updates on the [official account](https://fosstodon.org/@turingway) and the [#TuringWay Hashtag](https://fosstodon.org/tags/turingway)
  - See the Github repository for [issues](https://github.com/the-turing-way/the-turing-way/issues) for ongoing discussions, recently [merged PRs](https://github.com/the-turing-way/the-turing-way/pulls?q=is%3Apr+is%3Aclosed+sort%3Aupdated-desc) and new chapters.
  - You can also ask in the [Slack channel](https://theturingway.slack.com) if someone would like to add something to the newsletter.
In this part, also highlight any important milestones in the project that were either established or achieved over the last month.

* **Relevant resources and events for the community**: check X, Slack and online posts for any recent publication and events from community members, resources for training or opportunities for skill-building or any other materials like blog posts or articles published in the network that could be useful for others.

* **Sections for acknowledgements and celebrations of community members**: this is the place to give shout-outs to our members who have given talks, workshops or helped *The Turing Way* in some way, celebrate personal milestones and highlight any relevant announcements from community members. 
  * To identify talks and presentations, please scan *The Turing Way* accounts for GitHub issues, X, Slack and the [Zenodo Community](https://zenodo.org/communities/the-turing-way) page (for DOI).
Since 2023, *The Turing Way* core team maintains all information about events and activities on their [centralised event page](https://docs.google.com/spreadsheets/d/1C-VZvmFL4PnSBsv_G9ZD3dwjIYLno3NyL7oHvbplnWs/edit#gid=577525947).
  * This is also a place to share tweets from the community or mention other online interactions such as posts from recent meetings where someone talked about _The Turing Way_.

* **In The Turing Way Orbit**: this section is an addition from 2022, which allows a dedicated section for sharing events, resources and opportunities for jobs, funding, collaboration and more from our collaborators, partners and broader research network.

The newsletter should provide relevant information about or from contributing and new members acknowledging them openly.
There should also be opportunities for folks who have never engaged before, or may not have the capacity to actively engage but still want to stay informed.
This can include Tips & Tricks for new contributors, recent conversations in community spaces, new chapters, ideas where support is needed or resources in the project that can make new members learn ways to engage, identify paths to get started as contributors and find relatable contents like impact stories of existing members, contributor's profiles or other community-related aspects.


### Collect images associated with the news item

Following the recommendations on {ref}`style guide for community<ch-style>` and {ref}`style guide for newsletters<ch-newsletters-style>` for using images, collect a few images (maximum 2 per section).
Make sure that these images are available under a free license (like CC-BY), collected with the link of their sources, and named clearly as suggested in the style guide.

For X mentions, there is no fixed number of screenshots, but 4-6 tweets looks less crowded in the newsletter.
They can be edited together in one image (explained in the newsletter's style guide).

### Write about each news item

Based on the bullet points collected for each news item, create 1-2 small paragraphs using the recommendations for the language and format described in the next subchapter.

Provide links when useful, give credit fairly to the community members who might be associated with the news item and end the paragraph with a sentence and link to more information.

### Proofreading your draft

Before sharing your draft you should do a proofread for grammar and typos.
An online app like [Ginger Grammar Checker](https://www.gingersoftware.com/grammarcheck), [Grammarly](https://app.grammarly.com) free version, [GrammarCheck](https://www.grammarcheck.net/editor/) or [Reverso Speller](https://www.reverso.net/spell-checker/english-spelling-grammar/) can help correct any grammatical and spelling errors.

You should also double-check to make sure that the links mentioned in the draft are not broken.
You can use online tools such as the [W3C link checker](https://validator.w3.org/checklink) or the free version of [Dr. Link Check](https://www.drlinkcheck.com/).

If possible, get your draft reviewed by 1-2 members.

### Updating your draft to the online repository

If you have drafted your newsletter in a local branch, before creating a PR, please add all the images mentioned in the newsletter to the right location: `the-turing-way/communications/newsletters/images`.
More details about using images have been discussed in the next subchapter, {ref}`style guide<ch-newsletters-style>`.

If you are working on a PR on GitHub, upload all the images and check if they are linked properly.

If you have created your newsletter draft in a HackMD, then copy-paste the content to create/update your GitHub PR and upload all the linked images.

When ready, mark your PR as "Ready for Review" and tag a few contributing members, preferably those who have been mentioned in the draft so that they can review and approve your text.

### Review process

The reviewers for the newsletter can review the text for language, relevance, typos, accuracy (fact-check), appropriateness of the use of images and the overall tone.

Reviewers can provide constructive feedback on the newsletter draft, add any missing items that they would like to highlight, suggest appropriate changes and approve the PR when ready for the draft to be published.

After the review process, each reviewer's name can be added under the special mentions section by the author to acknowledge their work.

### Publication process

We are currently using [Buttondown](https://buttondown.email/) to publish our newsletters.
TinyLetter is a subsidiary of [MailChimp](https://mailchimp.com/), that offers a simplified interface based free service for setting up an email newsletter and sharing it with subscribers.

Here are the steps for publishing the newsletter draft online and sending it by email to the subscribed members:

- Convert the Markdown content of the newsletter draft to HTML using [browserling.com](https://www.browserling.com/tools/markdown-to-html) by copy-pasting the Markdown content to the text box in the web application and pressing "Convert to HTML button".
- If authorised, log in to the TinyLetter account and click the “Write A Newsletter” button.
- Paste the HTML content of your draft generated by browserling.
- Make sure that the subject is written in the correct text box.
- Click “Preview” to see how the rendered version of your message will look.
- Upload images separately to the TinyLetter platform (the quality of photos significantly degrades if copied automatically).
- Adjust formatting as needed.
- Send a preview version to your email or _The Turing Way_ email (theturingway@gmail.com) to check if everything looks OK.
- Once confirmed for its format and content, the newsletter is sent to the registered members by clicking “Send to all”.
- The [online newsletters](https://buttondown.email/turingway/) are shareable by link and can be read by non-subscribed members as well.

*(Learn to make your newsletter [here](https://www.sitepoint.com/how-start-a-newsletter-in-minutes-with-tinyletter/).)*

 **It's published, now what?**

- Update the index table in the [README.md file](https://github.com/the-turing-way/the-turing-way/blob/main/communications/newsletters/README.md) with the details of the newly published newsletter.
- Tweet about it from [@turingway](https://twitter.com/turingway).
- Send a notification on [Gitter](https://gitter.im/the-turing-way/the-turing-way) and [Slack](https://theturingway.slack.com) channels.
- Do a celebratory dance! (This is mandatory! 💃)
