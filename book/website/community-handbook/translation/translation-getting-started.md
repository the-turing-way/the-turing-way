(ch-translation-localisation-journey)=
# Embark on Your Localisation Journey


## Overview of the translation workflow

By translation workflow, we do not refer only to the phases that contributors should follow during the translation process.
Instead, we refer to a set of aspects that can lead to a successful and sustainable translation project.


Our current Translation Management System is Crowdin.
All translations are stored in a fork of _The Turing Way_ repository inside [TWTranslation](https://github.com/TWTranslation), a GitHub Organisation account.
This fork is updated regularly to fetch new content and Crowdin adds it automatically and starts an automatic translation based on machine translation and translation memory. 
The automatic translations need review and approval before being accepted.

People in the team complete and review these automatic translations, according to the translation guidelines of each team.
New translated and approved files are sent back automatically to the translation fork and will generate a PR to be added to the repository as shown in the figure below.

Most of this process is done automatically, translators do not need to interact with GitHub in any way.

```{figure} ../../figures/workflow-crowdin.*
---
name: create-account-crowdin
width: 80%
alt: The workflow used in Crowdin.
---
The Translation workflow, which is located on a fork of _The Turing Way_ repository inside the [TWTranslation](https://github.com/TWTranslation) GitHub Organisation account.
```


## Join the Translation Team in Crowdin

- **Create an account in our Crowdin project** through [this link](https://accounts.crowdin.com/register?domain=turingway&continue=%2Fturing-way).

```{figure} ../../figures/create-account-crowdin.*
---
name: create-account-crowdin_
width: 90%
alt: Sign up in Crowdin or log in before you start the translation. You can also log in using your GitHub or Google account.
---
```

You can either create an account in Crowdin by filling the requested details or through sign up using your GitHub, Facebook, X (formerly Twitter), GitLab or Google account.

```{warning}
_The Turing Way_ is using [Crowdin Enterprise](https://crowdin.com/enterprise), which is not connected to [crowdin.com](https://crowdin.com/) and needs a separate account.
If you have an account in [crowdin.com](https://crowdin.com/), you will still need to sign up again in [Crowdin Enterprise](https://crowdin.com/enterprise) using [this link](https://accounts.crowdin.com/register?domain=turingway&continue=%2Fturing-way).  
```


- **Read the landing page of _The Turing Way_** and README to understand the vision and mission of _The Turing Way_ Book.

```{figure} ../../figures/README.gif
---
name: explore-readme-crowdin
width: 90%
alt: Crowdsourcing page in Crowdin which has three tabs, one showing the languages, the 2nd one showing the names of the managers and the third one showing the README file.
---
```

- **Review the Translation Guidelines.**
  - What should *not* be translated for consistency and structural integrity.
  - They are essential to harmonise and standardise translations.
  Make sure you read them before you start translating for the first time.
  If you are starting a new language, please make sure you create a repository in the GitHub organisation with your language guidelines. 
  Feel free to comment on these guidelines and suggest new terms anytime. This can be done in the corresponding repositories or in _The Turing Way_ issues.

- **Choose the language you want to contribute to.** We have currently 4 languages with active contributors, which are Spanish, Arabic, Portuguese and Chinese.   

```{admonition} Add A New Language
:class: tip
If your language is not in the list, please feel free to contact one of the managers and ask for a new language through Crowdin or Slack.
```

```{figure} ../../figures/add-language-crowdin.gif
---
name: add-language
width: 90%
alt: You can add a new language by contacting one of the managers.
---
```

- **Start Translating chapters from the translation priorities list.**
  - Each language has a Translation Priorities list, which you can find in the README file. 
  Choose one of the high priority files.
  - You can view the translation priorities list in the task tab in Crowdin, they are also marked with a red arrow. The same list is copied below:
    - **Urgent** (Welcome, afterword)
    - **Priority +++** (Overview of the guide of reproducible research, open research)
    - **Priority ++** (Research data Management, Research Compendia, Licensing)
    - **Priority +** (Version Control, Overview of Project Design, Creating Project Repositories)
    - **Intermediate** (Overview of the Guide for Communication, Making Research Objects Citable, Communications in Open Source Projects, Getting Started With GitHub, Research Infrastructure Roles, Introduction to Research Ethics)

    - In order to navigate to the tasks tab inside Crowdin, you need to click in "Go to the Console" at the top right and navigate back to _The Turing Way_ project which will direct you to a similar interface but with additional tabs on the left.
    One of these is the task tab.
    In the Tasks, we assign tasks to get files translated or proofread by the community or set the due dates and receive notifications about the changes and updates in tasks.

```{figure} ../../figures/tasks-crowdin.gif
---
name: tasks-crowdin
width: 90%
alt: You can add a new task to Crowdin by clicking on the console at the top and then navigating to the task tab at the side.
---
```

- Once you decide which file you will work on, you can type its name in the search bar and click on it. 
  This will direct you to the Crowdin Editor, you will learn more about it in the next chapter.

```{admonition} Top Tip
:class: tip
The arrow icons next to the high priority files are always pointing up and coloured red!  
```

```{figure} ../../figures/choose-file-crowdin.gif
---
name: choose-file-crowdin
width: 90%
alt: Use the search box to look into the file that you would like to start translating.
---
```  

You are now all set up to start translating _The Turing Way_. 
In the next chapter, you will learn how to take advantage of the Crowdin editor to translate strings, proofread or add comments.
