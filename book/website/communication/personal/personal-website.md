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

(cm-personal-website-basics)=
# Basic elements of Web Development: Processes and Tools

Web development is the entire process of creating and maintaining websites and web applications.

It involves iterative ideation and implementation. The core phases associated with web development are analysis, design, development, testing & review, deployment, and maintenance.

(cm-personal-website-analysis)=
## Analysis 

The goal of the analysis phase is to gain a deep understanding of the problem that a website is trying to solve so that the best solution can be found. By taking the time to carefully analyse the requirements of a website, people (researcher, web developer, programmer, and more) can ensure that the final product is effective and meets its users' needs.

(cm-personal-website-design)=
## Design

In this phase, the website structure plus the visual components and content, including activity layouts, navigation panels, images, and videos, are added to provide a feature-rich audio-visual experience to the users. The design stage is crucial since it directly impacts the UI/UX of the website. It is important that the design of the website is responsive, highly intuitive, and easy to navigate.

(cm-personal-website-development)=
## Development

The development (& coding) phase of the web development process is when the actual content (in case of low-code/no-code frameworks) and/or code (in case of high-code frameworks) for the website is written. For high-code framwworks, this can be done using a variety of programming languages, depending on the functionalities required in the website. This is where the developer takes all of the designs, wireframes, and other elements from the previous phases and turns them into a working website.

In some cases, the entire site may be coded from scratch, but developers usually prefer using pre-existing tools or frameworks to speed up the process. Some of the commonly used frameworks are mentioned in the [Frameworks](cm-personal-website-frameworks) section below.

(cm-personal-website-test-review)=
## Testing and review

The next stage in the process involves testing the website comprehensively to remove any bugs or errors before it goes live. This is a critical stage. There are different testing methods and techniques that are utilised to ensure that the website is performing as expected at optimum levels.

The testing phase can be divided into two main categories:

(cm-personal-website-test-functional)=
### Functional testing: 
Functional testing focuses on verifying that the website performs its intended tasks.

(cm-personal-website-test-non-functional)=
### Non-functional testing: 

Non-functional testing assesses the website's performance, security, and usability.

(cm-personal-website-deployment)=
## Deployment

This is the process of putting the website or application live to be viewed by public. This usually involves transferring the code from a development or staging server to a production server, that is, from a local repository to a remote repository. Once the site or application is live, it needs to be monitored and maintained to ensure that it remains accessible and performant.

(cm-personal-website-maintenance)=
## Maintenance

The maintenance phase entails regular monitoring of the website's performance and delivering regular updates for enhanced features and functionality. Website maintenance might include various tasks such as updating software, backing up data, monitoring web traffic, and checking for security vulnerabilities. 

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

(cm-personal-website-frameworks-no-low-code)=
### No-Code/Low-Code frameworks

* [Canva](https://www.canva.com/design-school/resources/how-to-make-website-with-canva-step-by-step-guide)
* [Ghost](https://ghost.org/resources/building/)
* [GitHub profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-profile)
  * The repository [`rzashakeri/beautify-github-profile`](https://github.com/rzashakeri/beautify-github-profile) has instructions and advice to customise your GitHub profile.
* [Squarespace](http://squarespace.com)
* [Wix](https://learnxinyminutes.com/)
* [Wordpress](https://wordpress.com/blog/2025/01/02/personal-website/)

(cm-personal-website-frameworks-high-code)=
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

(cm-personal-website-high-customise)=
## Highly Customisable Websites

For highly customisable websites (usually, high-code websites), there are two major aspects to web development: frontend and backend. These form the backbone of web development, and each plays a crucial role in creating seamless, functional web experiences.

The techology stack needed for the web development process can be majorly divided into two categories: front-end and back-end development tech stack.

(cm-personal-website-frontend)=
## Frontend development:

This is the process that includes builing the UI/UX i.e. the client or the user side of the website/web application. Some of the most popular programming languages use Hyper Text Markup Language (HTML), Cascading Style Sheets (CSS), and JavaScript (JS).

(cm-personal-website-backend)=
## Backend development:

The back-end includes the server that processes all of the website's files, the database that stores the website's data, and the application that runs the website. Some of the most popular programming languages use JavaScript (JS), PHP, Python, Java, C#, Golang, and more. 
