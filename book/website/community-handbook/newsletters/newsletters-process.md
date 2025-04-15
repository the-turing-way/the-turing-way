# Creating a newsletter

This document provides an overview of a process we use in _The Turing Way_ for drafting, reviewing and publishing newsletters.
Though written for _The Turing way_, these steps can be adapted for documenting newsletters for any project.

We only suggest using these recommendations as guides.
These should not be considered as a set of fixed rules or the "only" way one should create newsletters.
As individual authors, you should allow your personality to show in your newsletter drafts.
After all, these newsletters land in someone's personal mailbox and most likely they know you (or your community).

## Steps for drafting _The Turing Way_ newsletters

### Create a GitHub issue to collect items

Create a new GitHub issue on [GitHub repository for newsletters](https://github.com/the-turing-way/newsletter/) where throughout the month you and other community members can suggest news items as a comment.
For example, in [this issue](https://github.com/the-turing-way/newsletter/issues/29), several members could suggest news items for a newsletter before it was drafted.

### Start a draft

There are several ways to start a draft for a _The Turing Way_ newsletter:

Create a new branch of _The Turing Way_ [GitHub repository for newsletters](https://github.com/the-turing-way/newsletter/) (find detailed process in {ref}`newsletter's style guide <ch-newsletters-style>`).

You can work on this GitHub branch locally or online in a pull request (PR).
If working online, please keep the PR in draft mode or add "[WIP]" (work in progress) in the title.

You might also use online editors like HackMD, Framapad or Google Doc to allow others to review or contribute to the draft before content is transferred to a GitHub branch.

### Collect items for the newsletter as bullet points

Based on what we currently publish, collect information from the listed resources for the topics described below (they can be presented in a format agreed with *The Turing Way* staff):

* **Community meetings**: review the [community calendar](https://calendar.google.com/calendar/embed?src=theturingway%40gmail.com&ctz=Europe%2FLondon) for upcoming events such as Collaboration Cafés, book dashes and workshops.

* **News from the community**:
  - Check social platforms (Bluesky, Linkedin, Mastodon or Slack channels) for find updates. For example, checkupdates on the [Linkedin](https://www.linkedin.com/company/the-turing-way/?viewAsMember=true) and the [#TuringWay Hashtag](https://fosstodon.org/tags/turingway)
  - See the Github repository for [issues](https://github.com/the-turing-way/the-turing-way/issues) for ongoing discussions, recently [merged PRs](https://github.com/the-turing-way/the-turing-way/pulls?q=is%3Apr+is%3Aclosed+sort%3Aupdated-desc) and new chapters.
  - You can share GitHub issues on Slack channels or community calls, inviting contributions from readers and community members for the next month.
In this part, also highlight any important milestones in the project that were either established or achieved over the last month.

* **Highlighting relevant resources and events for the community**: From recent posts,publication and events from community members identify resources for training, opportunities for skill-building and any other materials like blog posts or articles published in the network that could be useful for others.

* **Sections for acknowledgements and celebrations of community members**: this is the place to give shout-outs to our members who have given talks, workshops or helped *The Turing Way* in some way, celebrate personal milestones and highlight any relevant announcements from community members. 
  * To identify talks and presentations, please scan *The Turing Way* accounts for GitHub issues, Slack and the [Zenodo Community](https://zenodo.org/communities/the-turing-way) page (for DOI).
Since 2023, all information about events and activities are maintained in a centralised event page, where any event attended by team or community can be added in advance.

* **In The Turing Way Orbit**: this section is an addition from 2022, which allows a dedicated section for sharing events, resources and opportunities for jobs, funding, collaboration and more from our collaborators, partners and broader research network.

The newsletter should provide relevant information about or from contributing and new members acknowledging them openly.
There should also be opportunities for folks who have never engaged before, or may not have the capacity to actively engage but still want to stay informed.
This can include Tips & Tricks for new contributors, recent conversations in community spaces, new chapters, ideas where support is needed or resources in the project that can make new members learn ways to engage, identify paths to get started as contributors and find relatable contents like impact stories of existing members, contributor's profiles or other community-related aspects.

### Collect images associated with the news item

Following the recommendations on {ref}`style guide for community<ch-style>` and {ref}`style guide for newsletters<ch-newsletters-style>` for using images, collect a few images (maximum 1 per section).
Make sure that these images are available under a free license (like CC-BY), collected with the link of their sources, and named clearly as suggested in the style guide.

If there are several images that you want to highlight, such as from an event or reports, you can edit them together in one image (explained in the newsletter's style guide).
Keep accessibility and alt text in mind when selecting images.

### Write about each news item

Based on the bullet points collected for each news item, create 1-2 small paragraphs using the recommendations for the language and format described in the next subchapter.

Provide links when useful, give credit fairly to the community members who might be associated with the news item and end the paragraph with a sentence and link to more information.

### Proofreading your draft

Before sharing your draft you should do a proofread for grammar and typos.
Online apps like [Grammarly](https://app.grammarly.com) free version, [GrammarCheck](https://www.grammarcheck.net/editor/) or [Reverso Speller](https://www.reverso.net/spell-checker/english-spelling-grammar/) can help correct any grammatical and spelling errors.

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
It offers a simplified interface where text in Markdown can be pasted wihout requiring any formatting.

Here are a few steps for publishing the newsletter draft online and sending it by email to the subscribed members:

- Draft or export your newsletter draft in Markdown format.
- If authorised, log in to the Buttondown account and click“email" -> "new" button.
- Paste the Markdown content of your draft. 
- Make sure that the subject is written in the correct text box.
- Follow instructions about [drafting email/newsletter](https://docs.buttondown.com/sending-your-first-email#draft-your-first-newsletter) [formating images](https://docs.buttondown.com/uploading-images).
- Follow the instructions for [previewing your draft](https://docs.buttondown.com/draft-send) to check how the rendered version of your message will look.
- Adjust formatting as needed.
- Send a preview version to your email or _The Turing Way_ email (theturingway@gmail.com) or to the team members involved in drafting the newsletter to double check if everything looks OK.
- When ready and happy with the format and content, the newsletter can be [sent to the subscribed members](https://docs.buttondown.com/sending-via-email). You can also [schedule it ahead of time](https://docs.buttondown.com/scheduling-an-email).
- The [online newsletters](https://buttondown.email/turingway/archive) are shareable by link and can be read by non-subscribed members as well.

 **It's published, now what?**

- Update the index table in the [README.md file](https://github.com/the-turing-way/newsletter/blob/main/README.md) with the details of the newly published newsletter.
- Send a notification on [Slack](https://theturingway.slack.com) and social platforms.
- Do a celebratory dance! (This is mandatory! 💃)
