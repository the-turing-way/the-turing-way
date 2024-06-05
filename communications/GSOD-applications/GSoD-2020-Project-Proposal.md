# GSoD 2020 Project Proposal

- Title: Embedding accessibility in The Turing Way open source community guidance 
- Mentors:  Malvika Sharan, Kirstie Whitaker

## Proposal by _The Turing Way_ Team and GSoD applicant

The Turing Way is an Open Source and community-led book project on research reproducibility and best practices in data science. 
This project involves contributors from all around the world in developing learning resources, guidance and recommendations that form chapters for the books on reproducible research, project design, collaboration, communication and ethics in data science. 
At the time of writing this application, The Turing Way community has around 200 contributors who are data scientists, academics, teachers, students, policy-makers and other stakeholders in research of varying technical backgrounds. 
The Turing Way is hosted and developed online on GitHub (https://github.com/alan-turing-institute/the-turing-way) and the book is hosted as a JupyterBook (https://github.com/jupyter/jupyter-book) on Netlify at https://book.the-turing-way.org.

In 2020, The Turing Way experienced its first major turn over in membership of the core contributor community. 
The project received a new phase of funding and pivoted from a focus on computational reproducibility to a much broader scope covering project design, scientific communication, ethical data science, and the skills needed to collaborate in diverse and distributed teams. 
The Turing Way community members are curating information that is already available in blogs and within the documentation of other open source projects to make it easier for new contributors to any project to effectively join community-led projects around the world. 
The expansion has greatly improved the potential impact of The Turing Way but has also introduced inconsistencies in the way that the existing chapters have been written. 
The original authors no longer contribute to the project and it can be confusing for new members to follow updated style guides that existing chapters do not follow themselves.

In association with The Turing Way mentors, I have set 3 major technical writing goals for my GSoD application:
1. Retrospective consistency across the entire book to create a coherent feel and style.
2. Contributing towards future maintenance by developing user documentation and guiding resources to support its contributors and maintainers.
3. Improving an overall accessibility of the online book to improve access to information and its user-friendliness.

## Current State of the project

Since its launch in April 2019, this project has attracted enormous interest from the research community. 
Over 20 chapters were collaboratively written within a year by more than 150 contributors that cover important research practices, tools and methods for reproducibility. 
These resources have been developed by different contributors to different domain expertise, from around the world. This has also introduced several inconsistencies in the book in terms of language, chapter structure, cross-referencing, and in general how the chapters appear in the online book. 
I will focus on improving the consistency of content that is already in The Turing Way in order to make the book accessible for readers from diverse backgrounds.

Many contributors have also started conducting subprojects such as translation of The Turing Way book, collection of case-studies that applied the skills mentioned in The Turing Way and developing tutorials. 
These independent efforts also present a need to create detailed guidelines that explain the process and workflow to new contributors. 
Although the project has more contributor documentation than many projects, there are major sections that are missing or out of date. 
I will focus on maintaining consistency of content in The Turing Way in order to make contributions to the project more accessible for new community members.

The chapters and contents in a Jupyter Book can be browsed online using an index and simple filtering through the search option. However, the filtering of chapters in The Turing Way is not yet possible. 
This makes the book hard to navigate for new and occasional readers and users of this book: the community members who could benefit the most from The Turing Way material. 
I will focus on improving the accessibility of the material as it grows by adding an advanced filtering option to allow browsing its content by topics, relevance, or skill level.

## Project Goals

The goals identified for my application to GSoD have been discussed with the mentors Kirstie Whitaker, the project lead of The Turing Way, and Malvika Sharan, the community manager. 
Based on my interest in improving user experience and accessibility, we narrowed down my focus to the following three goals:
 
**1. Retrospective consistency:** review the previous contributions made in the project to make sure that the book that already exists is internally consistent. 
This will include updating the style guide to conform to accessibility standards, fixing outdated features caused by the major update (such as broken links, using images, cross-referencing between the chapters, and redirecting to pages that have moved), and bringing coherent feel and style in the book in general.
 
**2. Contributing to future maintenance:** build a set of templates for different kinds of contributions in the project, which will ensure that current and future contributors maintain this consistency as the project grows and evolves over time.
 
**3. Improving the overall accessibility to information:** work on the page tags and filters to make it easier for people to find information in the book. 
This will be an important work towards improving the user-friendliness of the online resources and give easy access to relevant information searched by the readers.

## Project goals and process in detail

This section explains the project goals in detail, provides examples of tasks that each goal will involve and a description of the process that will be applied to achieve them.

### 1. Achieving retrospective consistency

I will focus on improving the consistency of content that is already in The Turing Way in order to make the book accessible for readers from diverse backgrounds by:

i. Ensuring structural consistency across the entire book: By identifying the points that are inconsistent in the book at the moment I will identify a list of structural consistencies to ensure that the chapters across the book follow a uniform pattern, and thus enhance the readability for the users. 
I will introduce appropriate changes to each chapter to enhance the overall readability of The Turing Way’s book chapters. 
These changes will include using correct and consistent heading levels to structure a page. 
Validated headings allow users to read the book using an assistive technology device like a screen reader. 
I will also ensure that the citations and references are consistent throughout to appropriately cite and provide access to further reading on the Turing Way chapter content.

ii. Fixing features that are no longer supported: In June 2020 The Turing Way was updated to a new version of JupyterBook that is a complete rewrite of the publishing software. 
There are many features that are no longer compatible and lead to inconsistencies in the book including broken links and unclear formatting. 
For example, the previous version of JupyterBook supported HTML tags and a mix of Markdown and HTML formatting, which is no longer supported in the current pure python version. 
Broken links for cross-referenced chapters or sections make navigating between pages in the book difficult. 
I will use the new feature of unique labels to define headers and subheaders to make it easier for readers to access information that is available across The Turing Way chapters.

### 2. Contributing to future maintenance

I will focus on maintaining consistency of content in The Turing Way in order to make contributions to the project more accessible for new community members.

i. Ensuring future consistency: I will develop templates to guide authors as they write new content or modify existing chapters. 
The current template is outdated and does not reflect the style of communication that The Turing Way community has developed over time. 
The new templates will make improving the book more accessible by helping new contributors write interoperable content from the start. 
The material will need less effort to edit and review and will ensure readers benefit from easy searching, smooth navigation, and a better understanding of the technical content. 
The templates will be accompanied by guidelines for authors who want to develop chapter-specific content or to incorporate assessments for the readers to self-evaluate concepts covered in the chapter. 
This effort will bolster asynchronous collaboration among authors when writing content for a chapter ensuring that there is a cohesive narrative when it is written by a diverse group of authors from around the world.

ii. Capturing the ongoing process and workflow within the community: As a community-developed project, The Turing Way allows anyone to contribute to their project based on their availability. 
Volunteers carry out initiatives including creating tutorials, documenting case studies, and translating the book into different languages. 
These efforts have grown organically and are being led by different individuals in an independent manner. 
Their processes are not well documented making it difficult for new community members to join their work. 
I will maintain the accessibility and consistency of the project by supporting core contributors to document their workflows and link to them from the main user documentation and style guide.

### 3. Improving the overall accessibility of the online book

I will focus on improving the accessibility of the material as it grows by adding an advanced filtering option to allow browsing its content by topics, relevance, or skill level by:

i. Creating templates for authors that ensures the user-friendliness of online resource they build: The goal of The Turing Way is to transform data science practices to be more collaborative and inclusive. 
This means the information in the book must be accessible to everyone across different skill levels, application domains, and personal characteristics including disabilities such as visual impairment. 
The guidelines and templates I develop will ensure authors write accessible content from the start.
Accessible web content can be read consistently from different digital platforms, can be optimized as per the user’s requirement, and is understood clearly by a broad range of readers. 
I will improve the accessibility of The Turing Way book by designing and developing a responsive layout for when it is accessed on a smartphone or a tablet. 
The images in the book will adapt to the screens of mobile devices. 
I will add keyboard navigation support to the book for people who find it hard to use the mouse trackpad and need to navigate the book using a keyboard. 
These changes will help make the book accessible to a wider audience.

ii. Providing advanced search capacity to relevant information: Most users visit The Turing Way with a certain question related to data science in mind. 
I will enhance the current search feature by developing a standardised vocabulary to support the quick discovery of desired content in the book. 
This feature will facilitate grouping of related content, both in terms of the material that already exists and new content that will be written in the future. 
The controlled vocabulary will be developed based on the criteria of how relatively popular a search topic or phrase is and how they relate to the different skill levels. 
Making sure that the work can be quickly accessed by readers as they look for the answers to the question will make The Turing Way as useful as possible around the open source and data science ecosystems.

## Motivation and background for my proposal

<Removed to keep the personal information of the applicant secure>

## Timeline
*Not included in the application due to word limit*

1. Continue as a contributor (before 16 August 2020)
- Become more familiar with the project on GitHub.
- Understand expectations in this project by connecting with the project lead, community manager and community members.
- Continue engaging in the project and review others' contributions to get used to working with the community.
- Become more familiar with the supporting tools (like Jupyter Book, Sphinx, Markdown, Netlify) used in the context of the project.
- Attend coworking calls and collaboration cafes to participate in the project’s community discussions.

2. Preparation period (17 August - 13 September 2020)
- Learn about community-driven subprojects, guidelines for which are not yet defined in the user documentation.
- Understand the overall vision and goal of the project and set priorities with the help of the mentors.
- Discuss the proposed strategy for the improvement of the user documentation with the mentors to set realistic expectations.
- Collaboratively develop a checklist for creating consistency across different chapters.
- With the help of the mentors, I will brainstorm designs, ideas and outlines for the chapter templates that will be developed during the documentation phase.
- Set up a communication protocol for providing project’s tasks updates, for refining and aligning goals, and for revisiting tasks priorities.

3. Documentation Period (14 September - 30 November 2020)

September 2020: Create consistency across the entire book
- Open an issue in the project’s GitHub repository to invite community members to share what “workflows and processes” they have developed while working on the subprojects in the community.
- Using the checklist developed during the preparation period, I will apply consistency across different chapters.
- This month I will aim to work on one chapter every day (20 chapters in a month) and systematically apply the desired consistency.
- This work will also help me take notes of the exceptions that exist in the book and any point that can be added to the user documentation including the style guide of this project.

October 2020: Develop processes to maintain consistency in future contributions
- Using the template ideas developed during the preparatory phase, I will develop new chapter templates for the book.
- The notes developed from the previous months will be used for enhancing the style guide and contributions guidelines.
- The input received on the GitHub issue for workflows and processes will be captured to create guidelines for ongoing efforts in the community and documented in the community handbook.

November 2020: Improve accessibility of the online contents
- The last month of my GSoD participation will focus on the technical aspects of the online book to make it's content user-friendly for most readers.
- I will work on adding the advanced search capacity of the online book by introducing ‘tags’ to the existing content. This will include defining predefined tags and designing and integrating mapping and search functionalities.
- I will develop a responsive layout for the book with the support of my mentors. This will require tweaking the stylesheet of the book to make it responsive. Similarly, I will make current images responsive.
- These technical work will also result in feeding back the guidelines and information of newly added features into the user documentations

## List of important resources and references

### The Turing Way
- GitHub repository: github.com/alan-turing-institute/the-turing-way.
- Contribution guideline: github.com/alan-turing-institute/the-turing-way/blob/main/CONTRIBUTING.md
- The online book: https://book.the-turing-way.org/welcome
- The style guide: book.the-turing-way.org/community-handbook/style.html
- Zenodo community collection: https://zenodo.org/communities/the-turing-way

### The JupyterBook project
- Books with Jupyter: jupyterbook.org/intro.html.
- GitHub repository: Executable books by JupyterBook: github.com/executablebooks/jupyter-book.
- Jupyter Notebook Tools for Sphinx — nbsphinx version 0.7.1., nbsphinx.readthedocs.io/en/0.7.1.

### Netlify 
- "Netlify: All-in-one platform for automating modern web projects." Netlify, www.netlify.com.

### Markdown
- Markdown Guide, Matt Cone and contributors. www.markdownguide.org.

### Web Accessibility
- W3c Web Accessibility Initiative. "Accessibility Fundamentals Overview." Web Accessibility Initiative (WAI), 1 July 2020, www.w3.org/WAI/fundamentals. 
- W3c Web Accessibility Initiative. "Writing for Web Accessibility – Tips for Getting Started." Web Accessibility Initiative (WAI), 1 July 2020, www.w3.org/WAI/tips/writing.

## Proposal by the GSoD applicant: Paul Owoicho

The increasing popularity of Data Science and the versatility of its applications has made it an appealing domain for students, researchers, industry experts, and professionals across various fields and levels of expertise. To foster growth in the field, it is paramount that Data Science research is - and remains - accessible to the wider community of Data Science enthusiasts. One way this goal can be achieved is through guides on conducting reproducible, reusable, and collaborative Data Science research.

The Turing Way is one such guide, with a mission of “ensuring that reproducible data science is ‘too easy not to do’.” Currently, The Turing Way contains content that covers reproducible research, project design, communication, collaboration, and ethical research. However, as the scope of The Turing Way expands, editorial support would be needed to incorporate newly created content into the existing body of work.

### Project Goals

At a high level, my job as a Technical Writer on this project is to make The Turing Way more accessible for the Data Science community by:
Reviewing existing chapters of The Turing Way, looking for ways to improve its language and structure,
Incorporating new content into the existing body of work while keeping the overall style and tone of The Turing Way consistent, and
Contributing new content in the form of new chapters, interactive tutorials, and/or case studies.

### Timeline

If my application is successful, I propose to complete the project in the following manner:

- By August 17: Make contributions to The Turing Way where possible (fixing typos etc.)
Familiarize myself with the current information contained in The Turing Way
Improve my writing and editorial skills while getting up to speed with the tools I would be working with

- Community Bonding Phase (August 17 - September 23): Engage proactively with the team/community behind The Turing Way and learn more about the project
Establish and maintain channels of communication with mentors
Refine and finalise project goals with input from mentors and the community at large

- Week 1 (September 14 - September 19): The first week will be spent getting the necessary tools set up properly to ensure my productivity.
Furthermore, I discovered some typos while reading through The Turing Way. Though I intend to rectify these errors before August 17 as I contribute to the project. I propose to spend the first few weeks going through existing chapters of the book to ensure that its grammar, spelling, and tone are correct, consistent, and appealing to the project’s target audience. I will begin the proofreading stage with the chapter titled Guide for Reproducible Research.

- Week 2 (September 20 - September 26): Proofreading and editing the chapter titled Guide for Project Design as well as any new content and recommend changes as needed.

- Week 3 (September 27 - October 3): Proofreading and editing the chapter titled Guide for Communication

- Week 4 (October 4 - October 10): Proofreading and editing the chapter titled Guide for Collaboration, and working on new content.

- Week 5 (October 11 - October 17): Proofreading and editing the chapter titled Guide for Ethical Research, and working on new content.

- Week 6 (October 18 - October 24): Proofreading and editing the chapter titled Guide for Project Design, and working on new content.

- Week 7 (October 25 - October 31): Brainstorm ideas for new content for The Turing Way with input from the mentors of the project. This new content could be in the form of a new chapter, a tutorial, or a case study. For example, I am currently working on developing methods for podcasts retrieval and understanding as part of my dissertation. I could document this experience and my learning outcomes as a case study.

- Weeks 8 to 10 (November 1 - November 28): Write and edit new content contributions while proofreading the new content created by others.

- Week 12 (November 29 - December 5): I will finetune the written content to ensure factuality, accuracy and consistency. I will also create and submit my reflections on the project’s success and an evaluation of my mentors.

### Why The Turing Project

As a current Data Science Master’s student, I appreciate the need for reproducible Data Science. Not only does it help facilitate growth in the field, as one’s work can be built upon, it is also useful in business scenarios where a project might need to be repeated with different parameters or handed off to an engineering team for production.

To bring it home, I would be working on my dissertation over the summer with a focus on ongoing data challenges in NLP, Search, and Dialogue. Part of my work would involve reproducing results from previous projects and building upon them - this would not be possible if these projects were not reproducible, to begin with. Given this, The Turing Way project appeals to me because of its significance to the field of Data Science.

Furthermore, in the near future, I intend to pursue a PhD with a focus in Data Science. As I aspire to become part of the Data Science research community, I would relish any opportunity that allows me to make a contribution ahead of time.

### Why I am the right person

I believe that I am the right candidate for this project because:
As a budding Data Scientist, I appreciate the need for The Turing Way and foresee the impact it will have on the Data Science community. I will also be able to contribute authentic content to The Turing Way based on my experiences.
In my previous role as a Research Analyst at Guaranty Trust Bank in Nigeria, I gained significant experience in creating and maintaining documentation for projects my team was responsible for. I created customer-facing user-manuals for an app called Orange Books and another called Zumi the SKS Robot. Though these manuals were distributed in print, the final versions can be accessed online.
I currently freelance (remotely) as a Medical Writer where I write articles and research papers on a wide range of topics, most of which I have no prior knowledge of before starting on the topics. Not only has this experience improved my writing and research skills, but it has also helped me appreciate the value of collaboration and teamwork.
