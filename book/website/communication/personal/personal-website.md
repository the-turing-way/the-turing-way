(cm-personal-websites)=
# Personal Websites

(cm-personal-websites-prerequisites)=
## Prerequisites

| Prerequisite | Importance | Skill Level | Notes |
| -------------|----------|------|----|
| [](#rr-open) | Helpful | Beginner | An understanding of open research practices is useful for creating a personal website. |
| [](#cm-blogs) | Helpful | Beginner | Blogs for research communication can be part of a personal website. |

(cm-personal-websites-summary)=
## Summary

This section explores the importance and benefits of a personal website for researchers.
Then, coding and non-coding website generators with different levels of complexity are discussed, explaining their features and differences.
Several deployment options and maintenance strategies are also presented, helping researchers to choose the best solution for their needs.

(cm-personal-websites-motivation)=
## Motivation and Background

A personal website is an online space where researchers can share their work and additional interests with a broad audience.
It can serve as a platform to present research findings, projects, talks, publications, CV or resume, and other professional information.
But this space is not necessarily limited to academic content; it can also be a place to share personal interests, hobbies, and other activities.
As a result, this website can be customised to express the individual's unique identity and values.
This online presence can help researchers expand their visibility, engage with a wider audience, connect with potential collaborators, and even create new career opportunities.

(cm-personal-website-frameworks)=
# Frameworks

(cm-personal-website-frameworks-what)=
## What is a framework?

In website development, a framework is a set of pre-written code, tools, and
libraries that help developers build and maintain websites more efficiently.
Frameworks provide a structured foundation, offering reusable code modules,
common design patterns, and guidelines, which help streamline the development
process and promote best practices. They essentially "frame" the development by
managing basic functionalities and allowing developers to focus on the unique
aspects of their projects rather than repetitive tasks.

(cm-personal-website-frameworks-benefits)=
## Benefits of using a framework

Frameworks provide several benefits in website development:

* **Code Reusability**: Common functions are built-in, which
reduces redundancy.
* **Efficiency**: They allow faster development by eliminating the need
to code every component from scratch.
* **Scalability**: Frameworks provide a solid structure that can grow with the
website.
* **Security**: Many frameworks come with built-in security features and
updates, which help mitigate vulnerabilities.

(cm-personal-website-frameworks-list)=
## Popular frameworks

Here, we list some commonly used frameworks. They have been
divided into two categories depending upon whether person wants to create a
website using low-code or high-code options.

### No-Code/Low-Code frameworks
* [Canva](https://www.canva.com/design-school/resources/how-to-make-website-with-canva-step-by-step-guide)
* [Ghost](https://ghost.org/resources/building/)
* [GitHub profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-profile)
  * The repository [`rzashakeri/beautify-github-profile`](https://github.com/rzashakeri/beautify-github-profile) has instructions and advice to customise your GitHub profile.
* [Squarespace](http://squarespace.com)
* [Wix](https://learnxinyminutes.com/)
* [Wordpress](https://wordpress.com/blog/2025/01/02/personal-website/)

### High-Code frameworks

#### Static website generator

* [Academic pages](https://github.com/academicpages/academicpages.github.io)
* [Blogdown](https://bookdown.org/yihui/blogdown/) (R)
* [Fast Html](https://fastht.ml/) (Python)
* [Hugo](https://gohugo.io/)
* [Jekyll](https://jekyllrb.com/)
* [Pure HTML/CSS/Javascript](https://pure-css.github.io/start/)
* [Quarto](https://quarto.org/docs/gallery/#websites) (R/Python/Julia)

#### Dynamic website generator

* [Django](https://www.djangoproject.com/)

# Building an academic website with Quarto

Quarto is a powerful open-source scientific and technical publishing system that
enables researchers to create dynamic and interactive websites, documents, and
presentations using a combination of markdown and code. It supports multiple
programming languages, including R, Python, and Julia, making it a versatile tool
for researchers across various disciplines.

## Why use Quarto for academic websites?
Using Quarto for building academic websites offers several advantages:
* **Ease of Use**: Quarto's markdown-based syntax is user-friendly, allowing researchers to create content without extensive web development knowledge.
* **Integration with Code**: Quarto seamlessly integrates code and data, enabling researchers to include dynamic visualizations, analyses, and interactive elements directly within their websites. It allows you to mix text, code, and outputs in a single document. Similar to R Markdown, you can create documents that combine narrative text with code chunks that generate figures, tables, and other outputs.
* **Integraton with Latex**: Quarto has robust support for LaTeX, making it easy to include mathematical equations and scientific notation in your website content.
* **Customizability**: Quarto provides a range of themes and templates. This allows academics to customize their website. 
* **Reproducibility**: Quarto promotes reproducible research by allowing researchers to document their workflows and analyses alongside their content.
* **Open Source**: Quarto is open-source software, which means it is freely available and can be modified to suit individual needs.

## Getting Started with Quarto
To get started with Quarto, follow these steps:
1. **Install Quarto**: Download and install Quarto from the official website (https://quarto.org/).
2. Choose your preferred IDE (for example, RStudio, VS Code) for editing Quarto files. We recommend RStudio for R users and VS Code for Python and Julia users. This tutorial will use VS Code.
3. **Install VS Code**: Download and install Visual Studio Code from the official website (https://code.visualstudio.com/).
4. **Install Quarto Extension**: In VS Code, go to the Extensions view (Ctrl+Shift+X), search for "Quarto", and install the Quarto extension.
5. **Set Up Git and GitHub**: If you plan to host your website on GitHub Pages, ensure you have Git installed on your computer and create a GitHub account if you don't have one already.

## Creating a Quarto Website
1. **Set Up a New Project**: Create a new Quarto project. You can do this by opening VS Code, and typing `Ctrl+Shift+P` to open the command palette. Then, type "Quarto: Create New Project" and select it. Choose "Website" as the project type and specify a folder for your project. In the next step, you willbe promted to give your project a name. 

This step creates the basic structure of your Quarto website, including necessary files and folders. Let's have a look at them.

![The file structure of a newly create Quarto project](book/figures/file_structure_quarto_project.png)

First, we see the `_quarto.yml` file. This is the main configuration file for your Quarto website. It contains metadata about your site, such as the title (which you can change immediately, if you want), information about the location of the navbar (in this case, left) and the theme. You should also see that two pages are already created for you: `index.qmd` and `about.qmd`. From these two examples, you cans see that there are two ways to link content to the navbar: either by specifying the file name directly (as in the case of `about.qmd`) or by providing a title and a file name (as in the case of `index.qmd`). In the latter case, the title specified ("text") will be displayed in the navbar instead of the title from the file itself.

You can open these files to see their content. The `index.qmd` file is the homepage of your website, while the `about.qmd` file contains information about you or your research.

2. **Customize Your Website**: Open the `_quarto.yml` file and modify the title to reflect your personal information. You can also customize the theme and layout of your website by exploring the Quarto documentation (https://quarto.org/docs/websites/).

::: {.callout-note title="About qmd files"}
.qmd files are Quarto markdown files. They are similar to .Rmd files used in R Markdown but are more versatile as they support multiple programming languages, including R, Python, and Julia. These files allow you to combine narrative text with code chunks that can generate figures, tables, and other outputs, making them ideal for creating dynamic and interactive content. 
:::



