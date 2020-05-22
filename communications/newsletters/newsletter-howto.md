:notebook: Template  
---

# The Turing Way Newsletter: DD Month YYYY

# A catchy title that sums the main points

Hello Turing Way friends!

This month ...

Shout out ...

Events ...

Find more details on these topics below 👇


## Community meetings

    <About events like Collaboration Café, book dash, other meetings>

## News from the community

    <Any news from the team, community members, and new chapters>

## Relevant resources

    <Any useful resources like relevant publication, training items, and materials from collaborators>

## Tips & Tricks for new contributors

    <Any material that helps the new contributor to relate to the project like impact statement, story, and contributor in focus>

## Acknowledgments and celebrations

    <Shout out and wishes to celebratory news from members, recent meetings where someone talked about Turing Way, Tweets and other online mentions from people other than the team members>

## Special mentions

    <Shout out to the reviewers for this newsletter other than the team members>

## Connect with us!

- [About the project](https://www.turing.ac.uk/research/research-projects/turing-way-handbook-reproducible-data-science)
- [_The Turing Way_ book](https://the-turing-way.netlify.com)
- [GitHub repository](https://github.com/alan-turing-institute/the-turing-way)
- [Gitter chat room](https://gitter.im/alan-turing-institute/the-turing-way)
- [YouTube Videos](https://www.youtube.com/channel/UCPDxZv5BMzAw0mPobCbMNuA)
- [Twitter channel](https://twitter.com/turingway)

You are welcome to contribute content for the next newsletter by
emailing [Malvika Sharan](mailto:msharan@turing.ac.uk).

*Did you miss the last newsletters?*
*Check them out [here](https://tinyletter.com/TuringWay/archive).*

---
:construction: Style guide
---

- **File format**: Draft the newsletter in [Markdown](https://en.wikipedia.org/wiki/Markdown)
- **Filename**: Create a filename with the "newsletter_serial_MonthYYYY.md " format, where "serial" should be replaced by the serial number (in numerical) of the newsletter, the month should be replaced by the short name of the month and YYYY with the year in numerical.
- **File location on _The Turing Way_ GitHub**: The newsletters are currently stored in the path "the-turing-way/communications/newsletters/". 
    - This location also consists of a "README.md" file that has a table for all the published newsletters that are updated after each release.
    - This location has a folder called "images" that centrally holds all the images and linked to the corresponding newsletters.
- **Dates**: "DD Month YYYY" format
    - use it consistently in the entire document
    - To reflect a range, use "from DD to DD Month YYYY" format.
    - Even if the sentences have reference to a day in "yesterday", "today" or "tomorrow", provide the exact date inside parenthesis so that it still makes sense if someone reads a newsletter in the future.
- **Time**: Use time in [Greenwich Mean Time](https://greenwichmeantime.com/what-is-gmt/) (GMT) or [British Summer Time](https://greenwichmeantime.com/uk/time/british-summer-time/) (BST), followed by a link from [arewemeetingyet.com](https://arewemeetingyet.com/#form) to check time in relative time zones
- **Links**: Use the Markdown formatting for link like this, `[text that needs to be linked](full http link)`
    - Provide links wherever useful, for example [HackMD for Collaboration Café](https://hackmd.io/@KirstieJane/CollabCafe), [GitHub issue](https://github.com/alan-turing-institute/the-turing-way/issues), [registration pages](https://www.eventbrite.co.uk/) and [see details](https://github.com/alan-turing-institute/the-turing-way).
    - Create link for email ids using this Markdown syntax - ``[real-email-id](mailto:real-email-id)``
- **Quoting others**: Use smaller than (>) symbol followed by a space before the quoted sentence. For example:
    `> This is my legendary quote.` will appear as:
    > This is my legendary quote.
- **Header and styling**: The newsletter title is the top header. 
    - Different sections as suggested in the newsletters are second-level headers and the sub-sections are third-level headers.
    - Use bold letters, italics, hyperlinked texts and quotations wherever applicable
    - The project name, _The Turing Way_, should be italicised.
    - Use line breaks for each line consistent with _The Turing Way_ writing format.
    - Leave at least one line space after each section and subsection.
- **Use of language**: Keep the overall language simple and jargon-free. 
    - The tone should be welcoming, friendly and preferably informal. This can be personal to the author's writing style. 
    - Ask more than one person to review your draft to make sure that its content is clearly written. 
    - If using content from a language or culture different from your own, ask people with that language or culture to review your draft to make sure that contents are not misrepresented.
- **Use of emoji**: It is highly encouraged to use emoji! :smile: 
    - Be aware that the emoji can be misinterpreted by people from different cultures, hence keep it simple, neutral and positive. 
    - When in doubt, ask someone to review your draft.
- **Use of images**: Only use relevant images linked to the news item in the newsletter.
    - Make sure that the images are available under CC-BY license or approved to be reused by the owners. 
    - Avoid using memes, images with political or sexual innuendo, or anything that is not directly related to the community.
    - When drafting the newsletter in a HackMD, drag-n-drop an image into the editor or copy-paste an image to automatically upload the image to [imgur](https://en.wikipedia.org/wiki/Imgur).
    - When drafting the newsletter on the GitHub, upload the images in the folder "the-turing-way/communications/newsletters/".
    - File naming convention for the images is "short-name-monthYYYY.png", where the short-name should be replaced with the identifiable short name of the image, the month should be replaced by the short name of the month and YYYY should be replaced by the year.
    - File extension can be '.jpg', '.png' or other with compatible image file type. 
    - Use Markdown syntax to link them in the newsletter. Example syntax, `![Alt: Description of the image - this is not the title but actual explanation of the image](image/path)` 
    - Below the image, write a short descriptive title for the image followed by an empty line. Link title to the source such as a tweet or related event.
    - When using multiple images as panels in one collective image, number each image clearly (this can be done in any photo or text editor) and provide a numbered title for each image. See example [here](https://github.com/alan-turing-institute/the-turing-way/blob/master/communications/newsletters/newsletter_14_May2020.md#tweets-from-the-community).
    
:pencil: Process of drafting a newsletter
---

1. **Starting a document for the newsletter**

    - You can start drafting the newsletter on a branch of _The Turing Way_ [GitHub repository](https://github.com/alan-turing-institute/the-turing-way/) within the appropriate directory (see the style guide).
    - You can work on your GitHub branch with the draft mode on and the [WIP] (work in progress) tag in your issue or pull request title.
    - Alternatively, you can use this HackMD (with the copy of template) to write your draft before you transfer them on a GitHub branch: https://hackmd.io/@malvikasharan/tw-newsletter
    
2. **Start collecting items for the newsletter as bullet points**

    - For community meetings, scan community calendar and GitHub issues for Collaboration Café, book dash, workshops or other meetings.
    - For news from the community, scan the Twitter account, recently merged pull requests for chapters, issue for newsletter item or ask in the Gitter chat room if someone would like to share something in the newsletter. 
    - This is also the place to highlight any milestone for the project that was either established or achieved over the last month.
    - To collect relevant resources, scan the Twitter channel for any recent publication from the community members, resources for training or skill-building or any other materials like blog posts or articles published in the network.
    - Tips & Tricks for new contributors should include any resource from the project that can make new members learn ways to engage, identify ways to get started as contributors and find relatable contents like impact stories of other members, contributor's profiles or other community-related aspects.
    - Acknowledgments and celebrations section gives a shout-out to our members, celebrates news from members, and highlight tweets, other online mentions or post from recent meetings where someone talked about _The Turing Way_.
    - The newsletter should highlight only noteworthy content from _The Turing Way_ core members and focus more on the contributing and new members.
    
3. **Collect images associated with the news item**

    - Following the recommendations on style guide for using images, collect a few (zero to maximum 2 per section) images.
    - For the twitter mention, there is no set number limit but recommended to use unto 6 tweets in different panels of the same image (explained in the style guide).
    - Make sure that these images are available under a free license (like CC-BY), collected with the link of their sources, and named clearly as suggested in the style guide.
    
4. **Write about each news item**

    - Based on the bullet point collected for each header, create a small paragraph(s) for each news item using the recommendations in the style guide for the language and format.
    - Provide links when useful, give credit to the community members who might be associated with the news item and end the paragraph with a sentence and link to more information.

5. **Create a pull request (PR)**

    - Before opening your PR on the GitHub for review, make sure you have uploaded the linked images on GitHub repository in the appropriate folder within your branch (see the style guide for detail).
    - Run a quick grammar or typo check by an app like [Grammarly](https://app.grammarly.com) and double-check that the links are not broken.
    - When ready, open the PR and tag a few contributing members, preferably those who have been mentioned in the draft so that they can review and approve your text.
    
6. **Review process**

    - The reviewers for the newsletter can review for language, typos, the relevance of the contents, appropriateness of the use of images and emojis, and the tone.
    - They can add constructive suggestions in the newsletter draft, add any missing item that they would like to highlight and approve the PR.
    - After the review process, each reviewer's name will be added under the special mentions section by the author.
    
7. **Publication process**

    - Convert Markdown file to HTML for TinyLetter using  [browserling.com](https://www.browserling.com/tools/markdown-to-html) by copy-pasting the Markdown content to the text box in the web application and pressing "Convert to HTML button".
    - The HTML content of the _The Turing Way_ newsletter is published online via [TinyLetter](https://tinyletter.com/TuringWay/). 
    - _The Turing Way_ account in the TinyLetter is accessible by the project lead, who sends a preview version to _The Turing Way_ email (theturingway@gmail.com) to check if everything looks OK and that the errors are fixed.
    - Once confirmed for its format and content, the newsletter is sent to the registered members.
    - The [online newsletters](https://tinyletter.com/TuringWay/) are shareable by links and can be read by non-subscribed members as well.
    - Update the index table in the [README.md file](https://github.com/alan-turing-institute/the-turing-way/blob/master/communications/newsletters/README.md) with the details of the newly published newsletter.
