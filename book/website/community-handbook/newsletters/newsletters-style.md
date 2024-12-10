(ch-newsletters-style)=
# Newsletter Style Guide

In the previous subchapter, we described the process of drafting, reviewing and publishing _The Turing Way_'s monthly newsletters.

In this document, we have listed some guidelines to maintain consistency across all the newsletters.

- **File format**: Draft the newsletter in [Markdown](https://en.wikipedia.org/wiki/Markdown)
- **Filename**: Create a filename with the "newsletter_serial_MMYYYY.md " format, where "serial" should be replaced by the (numerical) serial number of the newsletter, the month should be replaced by the short name of the month and YYYY with the year as a number.
- **File location on _The Turing Way_ GitHub**: The newsletters are currently stored in the path `the-turing-way/communications/newsletters/`.
    - This location also consists of a "README.md" file that has a table for all the published newsletters that are updated after each release.
    - This location has a folder called "images" that centrally holds all the images and links to the corresponding newsletters.
- **Dates**: "DD Month YYYY" format
    - use it consistently in the entire document
    - To reflect a range, use "from DD to DD Month YYYY" format.
    - Even if the sentences have reference to a day as in "yesterday", "today" or "tomorrow", provide the exact date inside parenthesis so that it still makes sense if someone reads a newsletter in the future.
- **Time**: Use time in [Greenwich Mean Time](https://greenwichmeantime.com/what-is-gmt/) (GMT) or [British Summer Time](https://greenwichmeantime.com/uk/time/british-summer-time/) (BST), followed by a link from [arewemeetingyet.com](https://arewemeetingyet.com/#form) to check the time in relative time zones.
- **Links**: Use the Markdown formatting for link like this, `[text that needs to be linked](full HTTP link)`.
    - Provide links wherever useful, for example, [HackMD for Collaboration Café](https://hackmd.io/@KirstieJane/CollabCafe), [GitHub issue](https://github.com/the-turing-way/the-turing-way/issues), [registration pages](https://www.eventbrite.co.uk/) and [see details](https://github.com/the-turing-way/the-turing-way).
    - Create links for email addresses using this Markdown syntax - ``[real-email-address](mailto:real-email-address)``.
    - [Too many links](https://intelligentcontacts.com/7-tips-to-keep-your-emails-out-of-the-spam-filter/) can trigger the spam filter on a recipient's inbox. try to keep them to a mimumum if you can.
- **Quoting others**: Use greater than (>) symbol followed by a space before the quoted sentence. For example:
    `> This is my legendary quote.` will appear as:
    > This is my legendary quote.
- **Header and styling**: The newsletter title is the top header.
    - Different sections as suggested in the newsletters are second-level headers and the sub-sections are third-level headers.
    - Use bold letters, italics, hyperlinked texts and quotations wherever applicable
    - The project name, _The Turing Way_, should be italicised.
    - Use line breaks for each line consistent with _The Turing Way_ writing format.
    - Leave at least one line space after each section and subsection.
- **Language and tone**: Keep the overall language simple and jargon-free, see [_The Turing Way_ style guide](https://github.com/the-turing-way/the-turing-way/blob/main/CONTRIBUTING.md#style-guide) for reference.
    - The tone should be welcoming, friendly and preferably informal.
    This can be personal to the author's writing style.
    - Ask more than one person to review your draft to make sure that its content is easy to understand and written clearly.
    - If using content from a language or culture different from your own, ask people with that language or culture to review your draft to make sure that the content is not misrepresented.
- **Use of emojis**: It is encouraged to use emoji (*show your personality*) 😇, but keep it simple, neutral and positive.
    - Be aware that ambiguous emojis can be misinterpreted by different readers.
    - When in doubt, ask someone to review your draft.
- **Use of images**: Only use relevant images linked to the news item in the newsletter.
    - Make sure that the images are available under a CC-BY license or approved to be reused by the owners.
    - Avoid using memes, images with political or sexual innuendo, or anything that is not directly related to the community.
    - When drafting the newsletter in a HackMD, drag-n-drop an image into the editor or copy-paste an image to automatically upload the image to [Imgur](https://en.wikipedia.org/wiki/Imgur).
    - When drafting the newsletter on GitHub, upload the images in the folder `the-turing-way/communications/newsletters/`.
    - The file naming convention for images is `short-name-monthYYYY.png`, where the short-name should be replaced with the identifiable short name of the image, the month should be replaced by the short name of the month and YYYY should be replaced by the year.
    - File extension can be `.jpg`, `.png` or others with compatible image file types.
    - Use Markdown syntax to link the images in the newsletter: `![](image/path)`.
    - As suggested in [_The Turing Way_ style guide](https://book.the-turing-way.org/community-handbook/style/style-figures.html), create an alt text for the image: `![Alt: Description of the image - this is not the title but actual explanation of the image](image/path)`
    - Below the image, write a short descriptive title for the image followed by an empty line.
    Link the title to the source such as a tweet or related event.
    - When using multiple images as panels in one collective image, number each image clearly (this can be done in any photo or text editor) and provide a numbered title for each image.
    See an example [here](https://github.com/the-turing-way/the-turing-way/blob/main/communications/newsletters/newsletter_14_May2020.md#tweets-from-the-community).
