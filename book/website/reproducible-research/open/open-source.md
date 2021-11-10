(rr-open-source)=
# Open Source Software

(rr-open-source-whatis)=
## What Is Open Source Software?

When a project is open-source [{term}`def<Open Source Software>`], anybody can view, use, modify, and distribute the project for any purpose.
These permissions are enforced through an open-source licence.
Open source is powerful because it lowers the barriers to adoption, allowing ideas to spread quickly.
In its most basic form, open-sourcing your software means putting your code online where it can be viewed and reused by others.

Many of the most widely used research software is open source.
Perhaps the paradigmatic example is the scikit-learn Python package for machine learning (Pedregosa et al., 2011), which, in the space of just over five years, has attracted over 500 unique contributors, 20,000 individual code contributions, and 2,500 article citations.
Producing a comparable package using a traditional closed-source approach would likely not be feasible.
It would, at the very least, require a budget of tens of millions of dollars.
While scikit-learn is an outlier, hundreds of other open-source packages that support much more domain-specific needs depend similarly on unsolicited community contributions; for example, the NIPY (neuroimaging in Python) group of projects in neuroimaging (Gorgolewski et al., 2016).
Notably, such contributions not only result in new functionality from which the broader community can benefit, but also regularly provide their respective authors with greater community recognition, and lead to new project and employment opportunities.

Researchers that make use of open-source software often make changes to them, such as adding features they need for their research, or fixing bugs.
They can then contribute these improvements back to the main project so the wider community can take advantage of them.

(rr-open-source-benefitsyou)=
## How Running and Contributing to Open-Source Software Projects Benefits You

- _Improve existing skills_: Whether it is coding, user interface design, graphic design, writing, or organizing, if you are looking for practice, there is a task for you on an open-source software project.
Further, open source necessitates cleaner, more maintainable code to enable collaboration between potentially thousands of people who may never meet.
This helps to build and maintain good coding habits.
Not to be underestimated are the people skills you can develop on open source software projects.
Open source offers opportunities to practice leadership and management skills, such as resolving conflicts, organising teams of people, and prioritising work.
- _Advance your career_: By definition, all of your open source work is public, and this presents opportunities:
  - _Demonstrate technical ability_: Technical interviews traditionally involve working on a simulated problem that can be tackled in a set amount of time with little additional context.
  Such simulations, by definition, are not real-world use cases, nor do they show what working with an applicant would be like.
  Open source provides visibility into both how a candidate solves problems, and how they work with others.
  You make a much more appealing employee if an employer can see the quality of your work and see you working with others over a long period rather than taking a chance on a single short, high-stress case which may not play to your strengths.
  - _Reputation_: Becoming an active member of the open source community can gain you a favourable reputation which may bolster future job prospects.
- _Meet people with similar interests_: Open source software projects with warm, welcoming communities keep people coming back for years, and many people form lifelong friendships through their participation in open source.
- _Find mentors and teach others_: Working with others on a shared project means you will have to explain how you do things, as well as ask other people for help. The acts of learning and teaching can be a fulfilling activity for everyone involved.

### Making Your Work Open Source

- _Re-usability_: Making your work openly available for re-use makes it easier for others to incorporate into their research.
If you make your software citeable, via a DOI [{term}`def<Digital Object Identifier>`] for example, this can increase your citations.
- _Contribution_: When you write closed source software, the only developers that can potentially detect, diagnose, triage, and resolve software bugs are those that have a copy of the code.
If your project is open, the number of potential contributing developers and thus the potential knowledge pool is orders of magnitude larger.
- _Feedback_: Making your work open enables you to get feedback and improve your project in a way you may never have thought of alone.
- _Accountability_: There is an argument that any software developed using government money should be open source by default; if the public has paid for its development they have a right to make use of it.
If your work is government-funded, making it open is a step you can take towards government openness and accountability.

### Contributing to Others' Open Source Software Projects

- _It is empowering to be able to make changes, even small ones_: You do not have to become a lifelong contributor to enjoy participating in open source.
Have you ever seen a typo on a website, and wished someone would fix it?
On an open source software project, you can do just that.
Open source helps people feel agency over their lives and how they experience the world, and that in itself is gratifying.
- _It is fun_:
Open source provides an endless, ever-changing set of Rubix cubes for you to solve on weekends. Just like puzzles, both crossword and jigsaw, open source provides bite-sized intellectual escapes.

(rr-open-source-benefitsresearch)=
## How Open Source Software Benefits Research

There are several ways in which open-source software benefits research:

(rr-open-source-benefitsresearch-reusable)=
### Re-usable

Open source software projects allow researchers to take advantage of each others’ work.
This enables researchers to apply their efforts to high-value work.
It is sometimes said that “all the easy problems have already been solved”.
Blogging, content management, and operating systems are all problems with established (and mainstream) open-source solutions, to name a few.
While developers could spend their time reinventing wheels that the open-source community has already perfected, it is highly preferable to use the world’s best wheel, especially when that wheel comes at no cost to you.
This reduces duplication of effort and allows researchers to focus on yet-unsolved challenges.

The {ref}`rr-code-reuse` provides a more in-depth list of different aspects to consider for making your code more reusable, whether this is a small script or a library.

(rr-open-source-benefitsresearch-checkable)=
### Checkable

Open-source projects allow the broader research community to read and test each others' code.
This way, bugs can be found more quickly, and other researchers can validate results.

(rr-open-source-benefitsresearch-collaborative)=
### Collaborative
Working openly also allows any number of researchers to collaborate on projects that could not possibly be developed by single researchers/research groups.
Examples include [Linux](https://www.linux.org/) operating systems, Python packages such as [scipy](https://www.scipy.org/) and [numpy](http://www.numpy.org/), and the machine learning library [TensorFlow](https://www.tensorflow.org/).

(rr-open-source-run)=
## How to Run Your Open Source Software Project

You can open source an idea, a work in progress, or after years of being closed source.
At the most basic level, all you need to do is put your code online somewhere that is likely to last a long time.
You can make your code citeable by assigning it a DOI [{term}`def<Digital Object Identifier>`] (as discussed in the section on {ref}`rr-rdm-sharing`).
This helps ensure that you get proper credit if people use or build upon your work.

A popular place to make your code available is GitHub [{term}`def<Github>`] (see the chapter on {ref}`rr-vcs`).
You must include a license file stating that anyone has permission to use, copy, and modify your work. Without this, no one can legally use your work, and so it is not open source.
The {ref}`rr-licensing` chapter will help you to pick the best license for your project.
There are also a few other files you should include with your code, as described below.

(rr-open-source-run-readme)=
### Welcome Users by Adding Information to Your README

You should include a README [{term}`def<README>`] file where you include useful information about what the project is, how to use it, and how to contribute to it. Here is a list of the main things a README should include:

- _The project name and what it is_: This will significantly help someone that comes across it to get an idea of the project. Include a few key points that describe the main features of the project and what features you are implementing.
This helps to quickly compare other projects with yours and gives an idea of why the project exists in the first place.
- _Instructions on how to install the project_: The installer might be a collaborator, someone that comes across and is interested in the project, or even you - if you get a new machine and need to re-install your project.
Nevertheless, it is a total waste of your resources to figure out how to get started with the project from scratch.
The instructions should also include any prerequisites that will be needed to run the project.
The best thing you can do is to write up the installation instructions when you first do them yourself, and you will quickly save hours of work in the future.
- _Instructions for how to run the code and any associated tests_: If you've been working on your project it may seem obvious how to run it, but this will likely not be the case for someone coming across it for the first time.
- _Links to related material_
- _List of authors/contributors to the project, possibly with contact information_
- _Acknowledgements_

Suppose you intend for other people to collaborate on your project (as opposed to just making your code available and considering it complete).
In that case, you should include Contributing Guidelines and most likely, a Code of Conduct.

(rr-open-source-run-guidelines)=
### Contributing Guidelines

Contributing Guidelines [{term}`def<Contributing Guidelines>`] tell your audience how to participate in your project. For example, you might include information on:

- How to file a bug report
- How to suggest a new feature
- Your roadmap or vision for the project
- How contributors should (or should not) get in touch with you

Using a warm, friendly tone and offering specific suggestions for contributions (such as writing documentation, or making a website) can go a long way in making newcomers feel welcomed and excited to participate.
For example, [Active Admin](https://activeadmin.info/index.html) starts its [contributing guide](https://github.com/activeadmin/activeadmin/blob/master/CONTRIBUTING.md) with: "First off, thank you for considering contributing to Active Admin. It’s people like you that make Active Admin such a great tool."

In the earliest stages of your project, your Contributing Guidelines file can be simple.
You should always explain how to report bugs or file issues, and any technical requirements (like tests) to make a contribution.
Over time, you might add other frequently asked questions here or in your readme file.
Writing down this information means fewer people will ask you the same questions over and over again.
It is also a good idea to link to your contributing guidelines file from your README, so more people see it.

(rr-open-source-run-conduct)=
### Code of Conduct

A Code of Conduct [{term}`def<Code of Conduct>`] helps set ground rules for behaviour for your project's participants.
This is especially valuable if you are launching an open-source project for a community or company.
A Code of Conduct empowers you to facilitate healthy, constructive community behaviour, which will reduce your stress as a maintainer.
It communicates how you expect participants to behave and describes who these expectations apply to, when they apply, and what to do if a violation occurs.

Much like open source licences, there are also emerging standards for codes of conduct, so you do not have to write your own. The [Contributor Covenant](https://contributor-covenant.org/) is a drop-in Code of Conduct that is used by [over 40,000 open source projects](https://www.contributor-covenant.org/adopters). No matter which text you use, you should be prepared to enforce your Code of Conduct when necessary.

Keep the file in your project's root directory, so it is easy to find, and link to it from your README.

(rr-open-source-contribute)=
## How to Contribute to Other's Open Source Software Projects

(rr-open-source-contribute-anatomy)=
### Anatomy of an Open Source Software Project

Every open source community is different. That said, many open source software projects follow a similar organizational structure.
Understanding the different community roles and the overall process will help you get quickly oriented to any new project.

A typical open source software project has the following types of people:

- _Author_: The person/s or organization that created the project.
- _Owner_: The person/s who has administrative ownership over the organization or repository (not always the same as the original author).
- _Maintainers_: Contributors who are responsible for driving the vision and managing the organizational aspects of the project. They may also be authors and/or owners of the project.
- _Contributors_: Everyone who has contributed something back to the project.
- _Community Members_: People who use the project. They might be active in conversations or express their opinion on the project's direction.

Bigger projects may also have subcommittees or working groups focused on different tasks, such as tooling, triage, community moderation, and event organizing. Look on a project’s website for a “team” page, or in the repository for governance documentation, to find this information.

A great many open source projects are hosted on GitHub (see the chapter on version control for more detail), which has facilities such as:

- _Issue tracker_: Where people discuss issues related to the project.
- _Pull requests_: Where people discuss and review changes that are in progress.
- _Discussion forums or mailing lists_: Some projects may use these channels for conversational topics (for example, "How do I..." or "What do you think about..." instead of bug reports or feature requests). Others use the issue tracker for all conversations.
- _Synchronous chat channel_: Some projects use chat channels (such as Slack or IRC) for casual conversation, collaboration, and quick exchanges.

(rr-open-source-contribute-changes)=
### Contribute Your Changes

Say you have added a feature or fixed a bug and want to contribute this work to the main project.

1. _Read the documentation_: The main project may have contributing guidelines or information in a README instructing prospective contributors on how to supply their changes.
2. _Make sure your conventions match the style and structure of the main project_: For example, if all the variables in a project are named in some particular way yours should be too.
Consistent conventions make it much easier for someone who has not seen your piece of the project before to understand it rather than having to figure out your particular set of conventions *and* what the code is doing.
The project's conventions may be outlined in its documentation, or may just be evident from inspection of the code itself.
3. _Break your changes up into manageable, well-defined chunks_: For example, if you have added two separate features, do not submit them together.
Keeping things "clean" in this way makes your work simpler to understand and review.
4. _Test your changes_: If the project comes with tests, run them.
Make sure you are testing against an up to date version of the project as it may have evolved considerably over time. Write specific tests for your changes and submit those too.
5. _Do not just submit code, update relevant documentation too_: If your changes are incorporated, it will have to be updated. If you do not do it, someone else will have to.
6. _Ask questions_: If there are things you are unsure about, there is no harm in asking. Many larger projects have dedicated forums or other venues for questions and discussion.
7. _Be clear_: When you submit your changes, clearly describe the changes you have made, why you have made them, and how they have been implemented.
This makes it as easier for someone looking at your work and deciding whether to incorporate it into the main project to do so.
In the likely case the main project is hosted on GitHub, you should put this in the pull request (see the chapter {ref}`rr-vcs` for more details).

(rr-open-source-contribute-looking)=
### Looking for Projects to Contribute to and How to Contribute to Them

You do not need to overthink what exactly your first contribution will be, or how it will look.
Instead, start by thinking about the projects you already use or want to use.
The projects you will actively contribute to are the ones you find yourself coming back to.
Within those projects, whenever you catch yourself thinking that something could be better or different, act on your instinct. You might scan a README and find a broken link or a typo.
Alternatively, you could be a new user and notice something is broken, or find an issue that you think should be in the documentation.
Instead of ignoring it and moving on, or asking someone else to fix it, see whether you can help out by pitching in. That is what open source is all about.

You can also use one of the following resources to help you discover and contribute to new projects:

- [Open Source Friday](https://opensourcefriday.com/)
- [First Timers Only](https://www.firsttimersonly.com/)
- [CodeTriage](https://www.codetriage.com/)

If you are not sure how to start, there are a few other ways you can go about it, such as finding an open issue to tackle or asking if you can help write a new feature.

A common misconception about contributing to open source is that you need to contribute code. In fact, it is often the other parts of a project that are most neglected or overlooked. You will do the project a huge favour by offering to pitch in with these types of contributions. You could:

- Review code on other people's submissions.
- Write and improve the project's documentation.
- Curate a folder of examples showing how the project is used.
- Answer questions about the project on, for example, Stack Overflow,
- Keep things organized, for example, on GitHub by:
    - Linking to duplicate issues.
    - Suggesting new issue labels.
    - Going through open issues and suggesting closing old ones.
    - Ask clarifying questions on recently opened issues to move the discussion forward.

(rr-open-source-closed)=
## Closed Software

What if you are working with people that do not use the open source model for their software?
This may initially seem an affront to all the principles discussed so far. However, there are usually very good reasons for why things are the way they are (for example legal, commercial, or security reasons).
Often, it will still be possible to use and contribute, but the details of how might be different.
The kinds of practices used in 'closed' software are generally the same, and the concepts and tools you can learn about in the Turing Way still apply.

Sometimes, however, there might not be good reasons for the closed source approach.
Different areas of research have different cultures which run against the grain of open principles and feel very frustrating.
Tackling this barrier can be very tricky as cultures can take years or decades to change.

Working with closed software can offer both opportunities and threats to your research.
In all cases, understanding and respecting other's perspectives offers the greatest chances of success.
