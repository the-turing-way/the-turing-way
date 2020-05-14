## Open source software

### What is open source software?

When a project is open source anybody can view, use, modify, and distribute the project for any purpose.
These permissions are enforced through an open source licence.
Open source is powerful because it lowers the barriers to adoption, allowing ideas to spread quickly.
In its most basic form, open sourcing your software simply means putting your code online where it can be viewed and reused by others.

Many of the most widely used research software is open source.
Perhaps the paradigmatic example is the scikit-learn Python package for machine learning (Pedregosa et al., 2011), which, in the space of just over five years, has attracted over 500 unique contributors, 20,000 individual code contributions, and 2,500 article citations.
Producing a comparable package using a traditional closed-source approach would likely not be feasible, and would, at the very least, have required a budget of tens of millions of dollars.
While scikit-learn is clearly an outlier, hundreds of other open source packages that support much more domain-specific needs depend in a similar fashion on unsolicited community contributions, for example, the NIPY (neuroimaging in Python) group of projects in neuroimaging (Gorgolewski et al., 2016).
Importantly, such contributions not only result in new functionality from which the broader community can benefit, but also regularly provide their respective authors with greater community recognition, and lead to new project and employment opportunities.

Researchers that make use of open source software often make changes to them such as adding features they need for their own research, or fixing bugs.
They can then contribute these improvements back to the main project so the wider community can take advantage of them.

### How running and contributing to open source software projects benefits you

- Improve existing skills: Whether it is coding, user interface design, graphic design, writing, or organizing, if you are looking for practice, there is a task for you on an open source software project.
Further, open source necessitates cleaner, more maintainable code to enable collaboration between potentially thousands of people who may never meet.
This helps to build and maintain good coding habits.
Not to be underestimated are the people skills you can develop on open source software projects.
Open source offers opportunities to practice leadership and management skills, such as resolving conflicts, organising teams of people, and prioritising work.
- Advance your career: By definition, all of your open source work is public and this presents opportunities:
  - Demonstrate technical ability: Technical interviews traditionally involve working on a simulated problem that can be tackled in a set amount of time with little additional context.
  Such simulations, by definition, are not real world use cases, nor do they show what working with an applicant would be like.
  Open source provides visibility into both how a candidate solves problems, and how they work with others.
  You make a much more appealing employee if an employer can see the quality of your work and see you working with others over a long period of time rather than taking a chance on a single short, high-stress case which may not play to your strengths.
  - Reputation: Becoming an active member of the open source community can gain you a positive reputation which may bolster future job prospects.
- Meet people with similar interests: Open source software projects with warm, welcoming communities keep people coming back for years and many people form lifelong friendships through their participation in open source.
- Find mentors and teach others: Working with others on a shared project means you will have to explain how you do things, as well as ask other people for help. The acts of learning and teaching can be a fulfilling activity for everyone involved.

#### Making your own work open source

- Re-usability: Making your work openly available for re-use makes it easier for others to incorporate into their own research. If you make your software citeable, for example via a [DOI](doi_system) this can increase your citations.
- When you write closed source software, the only developers that can potentially detect, diagnose, triage, and resolve software bugs are those that have a copy of the code.
If your project is open the number of potentially contributing developers and thus the potential knowledge pool is orders of magnitude larger.
- Feedback: Making your work open enables you to get feedback and improve your project in way you may never have thought of alone.
- Accountability: There is an argument that any software developed using government money should be open source by default; if the public has paid for its development they have a right to make use of it.
If your work is government funded making it open is a step you can take towards government openness and accountability.

#### Contributing to others' open source software projects

- It is empowering to be able to make changes, even small ones: You do not have to become a lifelong contributor to enjoy participating in open source.
Have you ever seen a typo on a website, and wished someone would fix it?
On an open source software project, you can do just that.
Open source helps people feel agency over their lives and how they experience the world, and that in itself is gratifying.
- It is fun:
Open source provides an endless, ever-changing set of Rubix cubes for you to solve on weekends. Just like puzzles, both crossword and jigsaw, open source provides bite-sized intellectual escapes.

### How open source software benefits research

Open source software projects primarily benefit research by allowing researchers to take advantage of each others' work. This enables researchers to apply their efforts to high-value work.
It is sometimes said that "all the easy problems have already been solved".
Blogging, content management, and operating systems are all problems with established (and mainstream) open source solutions, to name a few.
While developers could spend their time reinventing wheels that the open source community have already perfected, it is highly preferable to use the world's best wheel, especially when that wheel comes at no cost to you.
This frees researchers up to work on yet-unsolved challenges.
This reduces duplication of effort and allows researchers to focus on the work they're actually interested in.

Working openly also allows any number of researchers to collaborate on projects that could not possibly be developed by single researchers/research groups.
Examples include [Linux](https://www.linux.org/) operating systems, Python packages such as [scipy](https://www.scipy.org/) and [numpy](http://www.numpy.org/), and the machine learning library [TensorFlow](https://www.tensorflow.org/).    

### How to run your own open source software project

You can open source an idea, a work in progress, or after years of being closed source.
At the most basic level all you need to do is put your code online somewhere that is likely to last a long time.
You can make your code citeable by assigning it a DOI (as discussed in the section on [making data citeable](#citing_data)).
This helps ensure that you get proper credit if people use or build upon your work.

A popular place to make your code available is GitHub (see the chapter on [version control](/version_control/version_control)). You must include a license file stating that anyone has permission to use, copy, and modify your work. Without this no one can legally use your work and so it isn't open source. The [software license](/licensing/01/softwarelicenses) section will help you to pick the best license for your project. There are also a few other files you should include with your code, as described below.

#### Welcome users by adding information to your README

You should include a readme file where you include useful information about what the project is, how to use it, and how to contribute to it. Here's a list of the main things a readme should include:

- The project name and what it is: This will greatly help someone that comes across it to get an idea of the project. Include a few key points that describe the main features of the project and what are the main features you're implementing.
This helps to quickly compare other projects with yours and to give an idea that why the project exists in the first place.
- Instructions on how to install the project: The installer might be a collaborator, someone that comes across and is interested in the project, or even you if you get a new machine and need to re-install your project.
Nevertheless, it is a total waste of both of your resources to start figuring out how to just get started with the project. This should also include any prerequisites that will be needed to run the project.
The best thing you can do is to just write up the installation instructions when you first do them yourself, and you'll quickly save hours of work in the future.
- Instructions for how to run the code and any associated tests: If you've been working on your project it may seem obvious how to run it, but this will likely not be the case for someone coming across it for the first time.
- Links to related material.
- List of authors/contributors to the project, possibly with contact information.
- Acknowledgements.

If you intend for other people to collaborate on your project (as opposed to just making your code available and considering it complete) then you should include contributing guidelines and most likely a code of conduct.

#### Contributing guidelines

Contributing guidelines tell your audience how to participate in your project. For example, you might include information on:

- How to file a bug report.
- How to suggest a new feature.
- Your roadmap or vision for the project.
- How contributors should (or should not) get in touch with you.

Using a warm, friendly tone and offering specific suggestions for contributions (such as writing documentation, or making a website) can go a long way in making newcomers feel welcomed and excited to participate.
For example, [Active Admin](https://activeadmin.info/index.html) starts its [contributing guide](https://github.com/activeadmin/activeadmin/blob/master/CONTRIBUTING.md) with: "First off, thank you for considering contributing to Active Admin. It’s people like you that make Active Admin such a great tool."

In the earliest stages of your project, your contributing guidelines file can be simple.
You should always explain how to report bugs or file issues, and any technical requirements (like tests) to make a contribution.
Over time, you might add other frequently asked questions here or in your readme file.
Writing down this information means fewer people will ask you the same questions over and over again.
It's also a good idea to link to your contributing guidelines file from your readme, so more people see it.

#### Code of conduct

A code of conduct helps set ground rules for behaviour for your project's participants.
This is especially valuable if you are launching an open source project for a community or company.
A code of conduct empowers you to facilitate healthy, constructive community behaviour, which will reduce your stress as a maintainer.
In addition to communicating how you expect participants to behave, a code of conduct also tends to describe who these expectations apply to, when they apply, and what to do if a violation occurs.

Much like open source licences, there are also emerging standards for codes of conduct, so you don't have to write your own. The [Contributor Covenant](https://contributor-covenant.org/) is a drop-in code of conduct that is used by [over 40,000 open source projects](https://www.contributor-covenant.org/adopters). No matter which text you use, you should be prepared to enforce your code of conduct when necessary.

Keep the file in your project's root directory so it's easy to find, and link to it from your readme.

### How to contribute to other's open source software projects

#### Anatomy of an open source software project

Every open source community is different. That said, many open source software projects follow a similar organizational structure. Understanding the different community roles and overall process will help you get quickly oriented to any new project.

A typical open source software project has the following types of people:

- Author: The person/s or organization that created the project
- Owner: The person/s who has administrative ownership over the organization or repository (not always the same as the original author)
- Maintainers: Contributors who are responsible for driving the vision and managing the organizational aspects of the project. They may also be authors and/or owners of the project.
- Contributors: Everyone who has contributed something back to the project.
- Community members: People who use the project. They might be active in conversations or express their opinion on the project's direction.

Bigger projects may also have subcommittees or working groups focused on different tasks, such as tooling, triage, community moderation, and event organizing. Look on a project’s website for a “team” page, or in the repository for governance documentation, to find this information.

A great many open source projects are hosted on GitHub (see the chapter on version control for more detail), which has facilities such as:

- Issue tracker: Where people discuss issues related to the project.
- Pull requests: Where people discuss and review changes that are in progress.
- Discussion forums or mailing lists: Some projects may use these channels for conversational topics (for example, "How do I..." or "What do you think about..." instead of bug reports or feature requests). Others use the issue tracker for all conversations.
- Synchronous chat channel: Some projects use chat channels (such as Slack or IRC) for casual conversation, collaboration, and quick exchanges.

#### Contribute your changes

Say you have added a feature or fixed a bug and want to contribute this work to the main project.

1. Read the documentation: The main project may have contributing guidelines or information in a readme instructing prospective contributors on how to supply their changes.
2. Make sure your conventions match those of the main project, both in style and structure: For example if all the variables in a project are named in some particular way yours should be too!
Consistent conventions make it much easier for someone who has not seen your piece of the project before to understand it rather than having to figure out your particular set of conventions *and* what the code is doing. The project's conventions may be outlined in its documentation, or may just be evident from inspection of the code itself.
3. Break your changes up into manageable, well-defined chunks: For example, if you have added two separate features don't submit them together. Keeping things "clean" in this way makes your work simpler to understand and review.
4. Test your changes: If the project comes with tests run them, and make sure you're testing against an up to date version of the project as it may have evolved considerably over time. Write specific tests for your changes and submit those too.
5. Do not just submit code, update relevant documentation too: If your changes are incorporated it will have to be updated, if you don not do it someone else will have to.
6. Ask questions: If there are things you are unsure about there's no harm in asking. Many larger projects have dedicated forums or other venues for questions and discussion.
7. Be clear: When you submit your changes clearly describe the changes you have made, why you have made them, and how they have been implemented. This makes it as easier for someone looking at your work and deciding whether to incorporate it into the main project to do so. In the likely case the main project is hosted on GitHub you should put this in the pull request (see the version control chapter for more details).

#### Looking for projects to contribute to and how to contribute to them

You do not need to overthink what exactly your first contribution will be, or how it will look.
Instead, start by thinking about the projects you already use, or want to use.
The projects you will actively contribute to are the ones you find yourself coming back to.
Within those projects, whenever you catch yourself thinking that something could be better or different, act on your instinct. You might scan a readme and find a broken link or a typo.
Or you are a new user and you noticed something is broken, or an issue that you think should really be in the documentation.
Instead of ignoring it and moving on, or asking someone else to fix it, see whether you can help out by pitching in. That is what open source is all about!

You can also use one of the following resources to help you discover and contribute to new projects:

- [Open Source Friday](https://opensourcefriday.com/)
- [First Timers Only](https://www.firsttimersonly.com/)
- [CodeTriage](https://www.codetriage.com/)

If you are not sure how to start here is a few other ways you can go about it such as finding an open issue to tackle or asking if you can help write a new feature.

A common misconception about contributing to open source is that you need to contribute code. In fact, it is often the other parts of a project that are most neglected or overlooked. You will do the project a huge favour by offering to pitch in with these types of contributions! You could:

- Review code on other people's submissions.
- Write and improve the project's documentation.
- Curate a folder of examples showing how the project is used.
- Answer questions about the project on, for example, Stack Overflow,
- Keep things organized, for example, on GitHub by:
    - Linking to duplicate issues.
    - Suggesting new issue labels.
    - Going through open issues and suggesting closing old ones.
    - Ask clarifying questions on recently opened issues to move the discussion forward.

### Closed software

What if you are working with people that do not use the open source model for their software?
This may initially seem an affront to all the principles discussed so far, but there are usually very good reasons for why things are the way they are (for example legal, commercial, or security).
Often, it will still be possible to use and contribute but the details of how might be different.
The kinds of practices used in 'closed' software are generally the same and the concepts and tools you can learn about in the Turing Way still apply.

Sometimes, however, there might not be good reasons for the closed source approach.
Different areas of research have different cultures which run against the grain of open principles and feel very frustrating.
Tackling this barrier can be very tricky as cultures can take years or decades to change.

Working with closed software can offer both opportunities and threats to your research.
In all cases, understanding and respecting other's perspectives offers the greatest chances of success.
