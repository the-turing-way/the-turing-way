(cl-github-novice-motivation)=
# Motivation for Using GitHub

| Prerequisite | Importance |
| -------------|------------|
| {ref}`Version control<rr-vcs>` | Helpful |

GitHub is an online web interface for collaborating, developing, sharing and using {ref}`Git<rr-vcs-git>` ({ref}`version control<rr-vcs>`).
It's designed to be easily accessible (you do not need to be a coder!) to share your work and (if you want) allow other people to test, modify, remix and reuse it.
It also provides space and tools for collaboration and maintenance.

GitHub is not the only available development platform, but it hosts this book and is widely used across disciplinary and private-public boundaries.
Thus, this chapter is tailored towards GitHub and its resources, though other platforms have some similar and/or analogous functions.

Some key things to know about GitHub:

- It provides an easy-to-use interface for {ref}`version control<rr-vcs>` that allows all activities to be recorded so you can revisit past versions and you know who made each contribution to the project.
- It has project management features - [issues](https://github.com/features/issues), [pull requests](https://github.com/features/code-review), and [discussions](https://github.com/features/discussions) - providing a social platform and communication tools that help a group of people to work together effectively.
- It can be used to store documentation, data and make web pages for projects - not just code!
- It has many options for automating repeated project management tasks including continuous integration testing and deployment.
- It can work entirely in your web browser, you do not need to install anything

In this chapter we outline some of the ways that you can benfit from using GitHub for your collaborative projects.

## Version Control

GitHub provides an interactive user interface that makes {ref}`version control<rr-vcs>` more accessible and intuitive.
It can be useful for those unfamiliar with command-line {ref}`git<rr-vcs-git>`.

Through the GitHub repository webpage, you can:
* View a project's detailed history of changes to each file.
* Revisit old versions of files and track contributions made.
* Roll back to previous versions of files if needed.
* Visualize helpful, color-coded "diffs" that highlight what has changed between different versions of the same file.
  * This helps during code review and makes it easy to identify how the file has changed, line by line.

<!-- These bullet points above need links to resources in The Turing Way if they exist, or externally if not -->

## Project Management

You can manage your project by creating project boards that include to-do lists and issues (problems or tasks that need to be done).
Discussion forums and flexibility in user permissions mean you can give team members (and/or the general public) the appropriate levels of access.

The Insights menu shows project stats, such as a list of all contributors and how often they contribute each week.

<!-- Need links for: guide to project management, project boards, discussion forums, user permissions, insights menu, list of all contributors -->

## Collaboration and Community

The combination of pathways to leverage version control and project management tasks makes GitHub a great place build a community around your work.

Its tools allow for clear communication and task allocation.
Multiple people can work on the same files at the same time, and git can track the changes and resolve any conflicts.

* Work on different versions of the project using branches
* Suggest changes using pull requests, which are then reviewed and accepted
* Track bugs and feature requests using documented {ref}`issues<cm-os-comms-issue-tracking>`
* Hold discussions with other collaborators
* Roadmap new tasks and receive feedback from others

<!-- Need links for: branches, pull request, discussion forums, user permissions, insights menu, list of all contributors -->

## Reproducibility

Sharing your project on GitHub helps improve {ref}`reproducibility<rr-overview>`, transparency, and verifiability, all key principles in research.
By providing open access to your work, others can understand your methods, build upon your work, and accurately replicate your results.
Many researchers {ref}`include<cm-citable>` GitHub links in their publications to share analyses with instructions to reproduce their results.
You can also integrate your project with [Zenodo](https://zenodo.org/) to generate a Digital Object Identifier (DOI) for {ref}`citation<cm-citable-linking>`.
This ensures your work is preserved and easier to reference.

## Publishing and Outreach

<!-- Can you add a sentence here to clarify the difference between collaboration - above - and publishing / outreach? They're both types of communication but serve different purposes. Maybe this is a good section to link to the Communications guide? -->

Projects on GitHub can be set to either public (visible to anyone) or private (only accessible by you or your team).
There are a few benefits that come with making your project public:

* Broader reach as anyone can access and contribute to your project.
* Increased visibility through GitHub's Explore feature.
* Others can "star" (bookmark) or "watch" your project for updates.
* Share your project through a trustworthy GitHub.com link with others, as the platform is widely known.
* Use GitHub pages to create a clean, professional {ref}`webpage<cm-personal-websites>` for your project
* Add a {ref}`README file<pd-project-repo-readme>` to act as your project's landing page, where you can welcome visitors, explain your work, and provide {ref}`documentation<rr-documentation-code>`.

## Releases

<!-- I think this section needs to be clearer about what a release is (do we have somewhere in the book to link to?) and why a tagged version is different to "just" version controlling your work with git (described above). The points about CI and CD are great - but I don't think they fit under the heading "releases" - so maybe this sub title should be "Testing and Release Management" something like that? -->

GitHub can help publish new versions of your project.
You can create releases that bundle your files, provide detailed release notes, and host files for download.
GitHub can also integrate with {ref}`Continuous Integration (CI)<rr-ci>` and Continuous Delivery / Deployment (CD) tools.
You can use this to automatically test new changes, ensuring everything still works as expected, streamlining development.

## Sustainability and Preservation

<!-- Needs a better title - maybe "distributed backup" - maybe adjust the next sentence to rephrase? -->
GitHub serves as a distributed backup for your work.
* A copy of your work is stored online, not just on one device.
* If you lose your local files, such as due to hardware failure, you can still recover everything from GitHub.
* The use of GitHub decentralizes the project, and project responsibility can be shared.
* If you stop maintaining a project, others can still view, cite or fork it to continue development.

## Education

<!-- What about "role modelling for others" ? -->

Choosing to set your project as public allows others to learn from your work.
By viewing your files, learners can see how you approached problems and implemented solutions.
This is especially helpful for beginners looking for real examples to study.
Your project might even encourage new contributors or inspire others to create their own projects.

## Easy to use

You can use GitHub directly in your web browser or download it to your computer.
Most instructions about how to use GitHub will start with you downloading it to your computer.
However, there is no need to download GitHub onto your computer; it is much simpler to use it in a web browser.

<!-- I don't think we should overly convolve "easy to use" with "no command line" - I think that misses the point that the command line isn't as hard as people might think! So maybe there's a combination of the "easy to use" and "markdown" sections that emphasise "easy to get started" ?> Also - GitHub is NOT infact all that easy to use :sweat_smile: -->
## Markdown

In order to use GitHub, you do not need to be a computer coder!
To format text, you only need to learn a very simple type of file formatting syntax called markdown.
Again, you do not need to download a markdown editor as it can all be written directly in GitHub in your web browser.
Markdown syntax [{term}`def<Syntax>`] is designed to be human readable even if it isn’t rendered [{term}`def<Rendered Output>`].
This allows you to format your text into a nice-looking document, including adding in links, pictures, tables and web links.
In most cases, GitHub even provides a "preview" option that allows you to see what your rendered document will look like.

For example, if you want to put a heading in markdown you use a ‘#’ (hash symbol) followed by a space and the title.
Like this `# heading 1`, this will produce the first level header style for that text.

### Resources to help you learn Markdown:

* How to write faster, better & longer: [the ultimate guide to Markdown](https://ghost.org/changelog/markdown/)
* [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Markdown guide: [Basic syntax](https://www.markdownguide.org/basic-syntax/)

How and when you use Markdown formatting in your file will become clearer as you go through this chapter.

<!-- the chapter needs to end with flagging what comes next and where to find additional resources-->