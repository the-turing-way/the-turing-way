(aw-glossary)=

# Glossary

## A

```{glossary}
acceptance testing
: A level of the software testing process where a system is tested for acceptability. The purpose of this test is to evaluate the system's compliance with the project requirements and assess whether it is acceptable for the purpose.

acknowledgements
: Where contributions to a project that don't qualify as authorship are written. It records the contributors name and the contribution that they made is described.

add
: Command used to add files to the staging area. Allows the user to specify which files or directories to include in the next commit.

adversarial learning
: A process under which learning systems are exposed to negative stimuli, such as the addition of purposefully manipulated data samples, in order to obtain potentially-beneficial effects. Examples of this technique may include the addition of additional learning objectives which penalise unwanted characteristics of a learning system, for example the ability to distinguish between data records based on inappropriate demographic attributes.

artificial intelligence
: The ability of synthetic computational systems to perform tasks and activities usually associated with biological, especially human, mental and intellectual capabilities.
  Also the field of study associated with imbuing synthetic systems with these capabilities.
  See also {term}`machine learning`

authors
: Authors in this context are the contributors to _The Turing Way_ project who have made a substantial contribution to the project such as writing a subchapter, facilitating community interactions, maintaining project’s infrastructure and supporting the participation of others through mentored-contributions. All authors are named co-authors on the book as a whole.
```

---

## B

```{glossary}
Binder
: A web-based service which allows users to upload and share fully-functioning versions of their projects in an environment they define.

BinderHub
: A service which generates binders. The most widely-used is mybinder.org, which is maintained by the Binder team. It is possible to create other BinderHubs which can support more specialised configurations. One such configuration could include authentication to enable private repositories to be shared amongst close collaborators.

binderize
: To make a Binder of a project.

branch
: A parallel version of a repository. Although it is contained within the same repository it allows you to develop it separately and then merge changes back into the ‘live’ repository or with other branches when appropriate.

bug
: This is an error, flaw or fault in a computer program or system that causes it to produce an incorrect or unexpected result, or to behave in unintended ways.

build
: A group of jobs. For example, a build might have two jobs, each of which tests a project with a different version of a programming language. A build finishes when all of its jobs are finished.
```

---

## C

```{glossary}
checkout
: Git command to switch to a specific file, branch, or commit. Allows you to activate older versions of files or commits or switch between active branches.

citizen science
: The inclusion of members of the public in scientific research.

clone
: Copy of an existing Git repository, normally from some remote location to your local environment. When you clone a repo you copy its entire history as well as all branches.

code coverage
: A measure which describes how much of the source code is exercised by the test suite.

code of conduct
: Guidelines that establish the kind of behaviour encouraged in the community, outline the process by which problems or violations of the guidelines will be addressed and who will be in charge of enforcing them.

code review
: An additional way of testing code quality. Code review gets another programmer to look over the new code and assess it. The goal is to point out strengths and also potential areas of improvement.

coercive authorship
: When a senior researcher forces a junior researcher to include a gift or guest author.

commit
: Snapshot of project history. A commit can be made after changes of a single file or a range of files and directories.

commit message
: A message the user can attach to a commit to explain what it contains.

communication channel
: The method of communication established for projects that might include mailing lists, community forums, chats and/or social media.

community member
: People who use the project. They might be active in conversations or express their opinion on the project’s direction.

computational environment
: Features of a computer which can impact the behaviour of work done on it, such as its operating system, what software it has installed, and what versions of software packages are installed.

conda
: A commonly used package management system.

consortia authorship
: A collective or community group authorship model. All members of the consortium are considered authors and are usually required to be listed in the published article although sometimes the article is published in the groups name. If not all members of the consortium agree to the responsibilities of authorship, the members that are authors will be listed separately from those who are not.

container
: Lightweight files that can encapsulate an entire computational environment including its operating system, customised settings, software and files.

continuous delivery
: It automates and runs the steps required to build and test a project.

continuous deployment
: It automatically deploys each time a code change is made.

continuous integration
: A development practice where changes are automatically, and rapidly, integrated into the development branch.
  This approach helps ensure the development code works and helps avoid large conflicts between feature branches.
  The term is strongly associated with tools which support this way or working, such as automated building and testing, which are often called continuous integration tools.
Commonly abbreviated to CI.

contributing guidelines
: Guidelines outlining how a person should go about contributing to an open source project.

contributors
: Everyone who has contributed something back to the project. These are members of a research project that have done some work that has made a contribution to the overall completion of the research. This could be a small contribution such as fixing a bug in software or a much larger contribution such as writing an academic article.

corresponding author
: The person who administers an academic article for the research group. They are responsible for receiving the reviewers comments, the proofs, corresponding with the editors and their details are printed on the final version of the published article.

creative commons
: Creative commons licenses provide standard language with which to place a creative work into the commons by providing simple terms under which others can reuse it.
  This is necessary as in almost all legal regimes by default authors reserve all rights to works even if they make them publicly available unless they explicitly provide a license stipulating otherwise.
  You can read more about copyright and licensing in {ref}`the chapter on licensing<rr-licensing>`.
  The 'CC0' is a public domain dedication waiving the copyright and anyone to use the work as they see fit.
  There are a number of variants on the creative license which use the copyright on the work to stipulate terms on which it can be re-used.
  The variants add or modify terms of the license, such as requiring attribution (BY), prohibiting commercial reuse (NC), prohibiting derivative works (ND), and requiring that any derivative works be shared under equivalent terms (SA).
  The organisation [Creative Commons (CC)](https://web.archive.org/web/20240704044626/https://creativecommons.org/) is a non-profit (501(c)(3)) based in the USA with a number of international affiliates.

CRediT
: CRediT is a high-level taxonomy, including 14 roles, that can be used to represent the roles typically played by contributors to scientific scholarly output. The roles describe each contributor’s specific contribution to the scholarly output. These details are becoming increasingly required by journals as well as authors meeting authorship criteria.
```

---

## D

```{glossary}
data repository
: A storage place on the internet where resources (data, software, publications or anything else) can be stored and accessed. Often data repositories provide long term preservation and persistent identifiers for the research objects stored. A data repository is the container for data and metadata, whereas a database is the structure that is used to store and manage that data.

differential privacy
: A strategy to provide quantifiable privacy guarantees when working with datasets containing personal information. The idea is that if the effect of making a single arbitrary substitution of a single record within the dataset on an aggregated query is below a specific threshold, then the result of any such query would not reveal substantial information about any individual member.

DMP
: Data Management Plan.

DNS
: Domain Name System.
  The system which translates domain names, for example book.the-turing-way.org, to the IP addresses used by computer networks.

Docker container
: An active computational environment executed from a Docker image.

Docker compose
: A tool that makes it easier define and run multi-container Docker applications in a reproducible manner. Through a YAML file, you can declaratively specify your deployment including containers, networks, and volumes. You can then deploy all resources with a single command.

Dockerfile
: A file used for creating Docker images

Docker image
: A machine-readable set of instructions to create a specified computational environment.

Docker registry
: A storage and distribution system for named Docker images. The registry allows Docker users to pull images locally, as well as push new images to the registry (given adequate access permissions when applicable). Such systems are often hosted in the cloud for ease of access.

digital object identifier
: A digital object identifier (DOI) is a persistent identifier or handle used to identify objects uniquely, standardized by the International Organization for Standardization (ISO). An implementation of the Handle System, DOIs are in wide use mainly to identify academic, professional, and government information, such as journal articles, research reports, data sets, and official publications. However, they also have been used to identify other types of information resources, such as commercial videos.
```

---

## E

```{glossary}
end to end test
: A test that runs the program from beginning to end and verifies that the output is correct.

epistemology
: Theory of knowledge and deals with how knowledge is gathered and from which sources.
  In research terms your view of the world and of knowledge strongly influences your interpretation of data and therefore your philosophical standpoint should be made clear from the beginning {cite}`brownEpistemology2015`.

equitable, diverse and inclusive practices
: Ensuring scholarship is open to anyone without barriers based on factors such as race, background, gender, and sexual orientation.

ethical source software
: These licenses were created as 'traditional' {term}`open source <Open Source Software>` licenses make no restrictions on the uses to which the software can be put including unethical uses.
  These licenses require that software is used in ways that respect fundamental human rights.
  This can be thought of as relaxing the hardline 'freedom to run software for any purpose' stipulation required for software to qualify as free / libre or open source by the conventional definitions.
  Whilst these licenses sought to be considered {term}`open source <Open Source Software>`, their terms place restrictions on the uses to which the software can be put so that anyone using the software in a way the licenses consider unethical would potentially expose themselves to liability.
  Use restrictions are prohibited by conventional definitions of open source so ethical source license could be thought of as a form of {term}`source available<Source Available>` license.
  See: {ref}`Ethical Source<rr-licensing-ethical>` for more.
```

---

## F

```{glossary}
FAIR
: Findable, Accessible, Interoperable and Reusable.

FAIR code
: A software licensing model where code is commercially restricted by it's authors but the source code is generally available and can be freely distributed and modified but with limits on how and if it can be used commercially.
  The model is described at [faircode.io](https://web.archive.org/web/20240621082333/https://faircode.io/), examples include the [Business Source License](https://web.archive.org/web/20240608005051/https://mariadb.com/bsl11/) and the [Elastic License 2.0](https://web.archive.org/web/20240625130857/https://www.elastic.co/licensing/elastic-license).
  A number of attempts have been made to make licenses with a similar intent, this space is somewhat controversial in free and open source software spaces, where restrictions on the ways in which software can be used disfavoured.
  Fair-code can be considered a subset of {term}`source available<Source Available>` code.

federated learning
: A design paradigm for information processing technologies in which the processing of information is decentralized and local data samples are not exchanged in full with a central entity.
  Used in machine learning to denote a system where learning is carried out via multiple nodes through the exchange of parameter values or other learning products rather than data samples directly.

first author
: The most prominent position in academic authorship. It conveys this person's position as the researcher who has made the greatest contribution to the research.

free or libre software
: The [Free Software Foundation (FSF)](https://web.archive.org/web/20240619064659/https://www.gnu.org/philosophy/free-sw.html) states that: "'Free software' means software that respects users' freedom and community. Roughly, it means that the users have the freedom to run, copy, distribute, study, change and improve the software.", refer to their website for a lengthier definition, see also the [Debian Free Software Guidelines](https://web.archive.org/web/20240517221908/https://wiki.debian.org/DebianFreeSoftwareGuidelines).
  Free software does not have to be monetarily free (gratis) you can buy and sell copies.
  Its chief concern is liberty not price, hence the use of 'libre software' as the word free in english does not distinguish these concepts.
  Notably almost all {term}`open source software<Open Source Software>` is also 'free' and the different terms reflect philosophical differences largely in the motivation for advocating for these freedoms.

free cultural works
: A list of conditions under which a work must be shared in order to be considered 'free' meaning that anyone is free to use, modify and distribute the work including derived works for any purpose.
  For a full description see: [freedomdefined.org](https://web.archive.org/web/20240630025334/https://freedomdefined.org/Definition)
  This is a generalisation of the 'four freedoms' originally developed to define {term}`free software<Free or Libre Software>`
```

---

## G

```{glossary}
generalisable
: Combining replicable and robust findings allow us to form generalisable results. Note that running an analysis on a different software implementation and with a different dataset does not provide generalised results. There will be many more steps to know how well the work applies to all the different aspects of the research question. Generalisation is an important step towards understanding that the result is not dependent on a particular dataset nor a particular version of the analysis pipeline.

Git
: Version control system that GitHub is built around. It is a widely used open source distributed version control system developed by the author of Linux.

Github
: An online code hosting and version control service. It has a great many features to aid collaboration between users, and hosts a large number of open source projects.

GitLab
: GitLab is a web-based DevOps lifecycle tool that provides a Git-repository manager providing wiki, issue-tracking and continuous integration and deployment pipeline features, using an open-source license, developed by GitLab Inc.

ghost author
: It is a person who writes an academic article without having carried out the research. It could be a professional writer. They would often not qualify as an author under the ICMJE criteria for authorship.

gift author
: People who are listed as authors but who did not make significant contributions to the research. This is also known as a guest author.

group authorship
: Some journals permit the use of group names but many require contributors to be listed and/or the writing group to be named. This is the same as shared authorship.

guarantor
: As well as fulfilling criteria for being a named author, some journals require one or more authors that take responsibility for the integrity of the work as a whole from inception to the published article.
```

---

## H

```{glossary}
hazard
: Inherent qualities or characteristics of something that make it potentially harmful.

head
: The latest commit on the branch which is currently checked out.

Helm
: A package manager for Kubernetes applications.

honorary authorship
: This is when an individual becomes a named author even though they have not made a substantial contribution and/or met authorship criteria.

hosting
: A service which makes data, such as a website, available on the internet.
  It is possible to self-host, using your own infrastructure.
  However, it is common to use a third-party, often commercial, hosting provider.

human readable
: A human readable medium or human readable format is any encoding of data or information that can be naturally read by humans. Some human readable formats, such as PDF, are not machine readable as they are not structured data, such as the representation of the data on disk does not represent the actual relationships present in the data.
```

---

## I

```{glossary}
identifier
: An identifier is a key or name used as label or the identity of a unique class of objects, representing an idea or physical objects. Also see: Persistent Identifier, Digital Object Identifier.

image
: Files used for generating containers.

inner source
: Inner source is the use of open source software development best practices (open collboration, open communication and peer review practices) and the establishment of an open source-like culture within an organisation for the development of a non-open source output.

integration testing
: A level of software testing where individual units are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units.

intersectionality
: The way in which a person's identities (gender, race, class, sexual orientation, physical ability and others) can overlap and intersect to form a unique experience of social status, discrimination or oppression. This term was coined by Professor Kimberlé Crenshaw.

issues
: Bug tracking system for GitHub. Collaborators can use issues to report bugs, request features, or set milestones for projects. Issues are tracked, reported, and closed by collaborators during the development process. They’re a great way of communicating with your team and reporting progress.

issue tracking
: The process of tracking current issues on the project, such as bug fixing, rolling out new features or community engagement plans.
```

---

## J

```{glossary}
job
: An automated process that clones your repository into a virtual environment and then carries out a series of phases such as compiling your code and running tests. A job fails if the return code of the script encounters an error.

JupyterHub
: A multi-user server for Jupyter Notebook instances.
```

---

## K

```{glossary}
Kubernetes
: Autonomous computational cluster manager.
```

---

## L

```{glossary}
license
: This is a legal document that sets out the permissions for creative and academic work. It explains copyright, ensures proper attribution and sets out how others can copy, distribute and make use of the works.
  See the chapter: {ref}`Licensing<rr-licensing>`

last author
: Usually the person in the research team with a supervisory role such as a PhD supervisor or Principal investigator. This is discipline dependent as sometimes the last author is the person that has made the smallest contribution to the research.
```

---

## M

```{glossary}
machine learning
: Methods which allow computational systems to extract regularities from data which permit them to perform tasks such as prediction and categorisation in a way that is at least superfially analogous to how biological systems learn.
  A broad sub-field of {term}`artificial intelligence` (AI) generally distinct from symbolic artificial intelligence, also know as GOFAI (good old fashioned AI), which focuses on programmed systems which perform logical reasoning.
  Machine learning is sometimes used interchangeably with artificial intelligence, but often employed to differentiate concrete or extant systems and algorithms from broarder and more speculative approaches to synthetic intelligent systems.

machine readable
: Machine readable refers to documents, data or other digital outputs whose content can be readily processed by computers. Such documents are distinguished from machine readable data by virtue of having sufficient structure to provide the necessary context to support the business processes for which they are created. Machine readable data can be defined as data in a format that can be easily processed by a computer without human intervention while ensuring no semantic meaning is lost.

main
: The repository’s main branch. Depending on the workflow, it is the one people work on or the one where the integration happens. This used to be called ‘Master’ in Github.

maintainers
: Contributors who are responsible for driving the vision and managing the organizational aspects of the project. They may also be authors and/or owners of the project.

Makefile
: A text file that contains the configuration for the build.

Markdown
: A lightweight markup language with plain-text-formatting syntax.
  Its design allows it to be converted to many output formats, but the original tool by the same name only supports HTML.
  Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.
  There are various flavors of Markdown which extend the original Markdown with additional features or syntax changes.
  Some popular flavors are [Myst Markdown](https://mystmd.org/), [CommonMark](https://commonmark.org/), [GitHub flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [GitLab flavored Markdown](https://docs.gitlab.com/user/markdown) and [pandoc Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown).  

merge
: The process of combining branches. Changes made on one or more branches are applied to another.

merge conflict
: Incompatibilities between branches being merged.

metadata
: Data used to describe other data. For example (35, 33, 27, 30, 33) is data but the units (miles per hour) and the fact these are the speeds of cars on a certain stretch of road is metadata.

mock test
: Replace a real object with a pretend one to use when running tests.
```

---

## N

---


## O

```{glossary}
open access
: Making all published outputs freely accessible for maximum use and impact.

open access publishing (gratis)
: The practice of making research publications available to anyone to read without charge.

open access publishing (libre)
: Libre open access is gratis, meaning the research is available free of charge, but it goes further by granting users the right to copy, reuse, and remix the publication.

open core
: A model for the monetisation of software where the 'core' components are {term}`open source<Open Source Software>` but there are additional features and/or hosted software as a service versions of, or extensions to, the software which are proprietary and paid for.

open data
: Documenting and sharing research data openly for reuse.

open educational resources
: Making educational resources publicly available to be re-used and modified.

open license
: A license is a document that specifies what can and cannot be done with a work.
  It grants permissions and states restrictions.
  Broadly speaking, an open license is one that grants permission to access, reuse and redistribute a work with few or no restrictions.
  (See {ref}`licensing<rr-licensing>` for more details)

open notebooks
: An emerging practice, documenting and sharing the experimental process of trial and error (see {ref}`Open Notebooks <rr-open-notebooks>`).

open project
: *Same as Open Science or Open Research Projects*.
  A project in which a significant amount of collaboration between the core or leadership team and the wider community takes place in the form of online interactions.
  Community interactions should maintain transparency and openness of the project to facilitate the growth of your community.

open scholarship
: This is a concept that extends open research further.
  It relates to making other aspects of scientific research open to the public such as open educational resources, having inclusive practice and citizen science.

Open source
: [opensource.com](https://web.archive.org/web/20240618150233/https://opensource.com/resources/what-open-source) describes open source as:
  "Something people can modify and share because its design is publicly accessible".
  The concept of 'open source' is now often extended beyond the context of its original coinage, {term}`software<open source software>`,
  to other forms of cultural or creative output, such as {term}`hardware<open source hardware>` and {term}`educational resources<open educational resources>`.
  Referring to something as 'open source' generally means that it is available under an {term}`open license`.
  The term can also extend to an {term}`open project` philosophy of collaboration beyond the mere availability and open licensing of the project's source materials.
  The term tends to, but need not, be applied in contexts where there is some 'source' material that is processed or synthesised into an output.
  For example an image created with a simple bitmap editor might be referred to as 'open source' despite lacking something that can be considered a 'source'.
  In such cases the notion of a '{term}`creative commons`' or '{term}`free cultural works`' may better apply as these do not as obviously emphasise the availability source materials but rather end products,
  though they may include source materials.
  There are also a number adjacent concepts which most often question the conventional open source prohibtion on restricting the uses to which open source things can be put, examples include: '{term}`ethical source<ethical source software>`' and '{term}`FAIR Code`'.

open source hardware
: Hardware whose design is made publicly available so that anyone can study, modify, distribute, make, and sell the design or hardware based on that design.

open source software
: Broadly, users of the software must able to inspect, modify and redistribute the source code of the software as they see fit, and not restrict the uses to which the code can be put or by whom it can be used.
  The [Open Source Initiative (OSI)](https://opensource.org/) offers a widely used definition of Open Source Software: The [Open Source Definition (OSD)](https://web.archive.org/web/20240619054907/https://opensource.org/osd) which is comprised of 10 criteria with which the terms of distribution of software must comply to meet their definition.
  The OSI maintains a list of licenses which have gone through their review process and been approved.
  Open source software should not be confused with {term}`source available<Source Available>` software it is not sufficient for the source code to be made available for a project to be considered open source.
  Almost all open source software is also {term}`Free / Libre Software<Free or Libre Software>`.
  For more details see: {ref}`Licensing<rr-licensing>` and {ref}`Open Source Software<rr-open-source>`.

ORCID
: Open Researchers and Contributor iD. It is a long lasting unique identifier for you as a researcher.
  A persistent digital identifier for researchers' that can be used on publications to ensure fair credit is given for all the researchers works.

owner
: The person/s who has administrative ownership over the organization or repository (not always the same as the original author).
```

---

## P

```{glossary}
package management system
: A tool for installing, managing, and uninstalling software packages including specific versions.

persistent identifier
: A long-lasting reference to a document, file, web page, or other digital object for identifying a resource that is unique, and widely understandable by a community. Also see: Digital Object Identifier.

pattern
: A pattern rule is a rule that contains exactly one % character in the target, which can be used to match a part of a filename.

peer review
: A process of evaluating one's work by others working in the same field.

persona
: A persona is the detail of an imaginary user or member, based on real-world observations and understandings of existing members or potential future members.

persona canvas
: The persona canvas can be used to assemble all your responses in one place, share this tangible information of your mental model (abstract concepts from our thoughts) with your colleagues and create a common language to communicate about your community members, users, and contributors.

phony target
: A phony target is one that doesn’t correspond to a file on the filesystem. A target is marked as phony by making it a prerequisite of the .PHONY target.

plain language
: Plain Language (also sometimes referred to as Plain writing or Plain English) is language and communication that your audience can understand the first time they read or hear it. Plain Language is defined by clear, straightforward communication that uses only as many words as are necessary to ensure that your audience understands the message easily. Most newspapers are written using plain language.

positionality
: Differences in social position and power shape identities and access in society. In acknowledging positionality, we also acknowledge intersecting social locations and complex power dynamics (also see: Intersectionality).

power users
: These are people who are already familiar enough with a platform to know the gotchas and tricks that make their experience more efficient.

preprint
: A preprint is a version of a scholarly or scientific paper that precedes formal peer review and publication in a peer-reviewed scholarly or scientific journal. It is usually uploaded by the authors to a public server where it is available openly.

prerequisite
: The prerequisite(s) of a rule correspond to files or other targets in the Makefile that must be up to date before the rule is run.

project design
: An early phase of the project where a project's key features, structure, criteria for success, and major deliverables are all planned out.

pull request
: Proposed changes to a remote repository. Collaborators without write access can send a pull request to the administrator with the changes they’ve made to the repo. The administrator can then approve and merge or reject the changes to the main repository. For open source projects pull requests can be sent by anyone that has forked a project.

push
: Sending changes to a remote repo. The remote repository is updated with the changes pushed and now mirrors the local repo.
```

---

## Q

---

## R

```{glossary}
RDM
: Abbreviation for research data management - see research data management for definition.

README
: A file which contains useful information about a project such as what it is, how to use/install it, how to test it, and how to contribute to it.

recipe
: One or more shell commands that are executed by Make. Usually these commands update the target of the rule.

regression test
: Comparing the result of a test before and after the code has been altered. If the output has changed a problem has been introduced somewhere in the program, and an error is thrown.

replicable
: A result is replicable when the same analysis performed on different datasets produces qualitatively similar answers.

repo2docker
: A tool to build Docker images from code repositories.

repository
: A central location where resources (data, software, publications or anything else) are stored and accessed. This keyword is often shortened to ‘repo’. See Data Repository if this place is long-lived.

reproducible
: A result is reproducible when the same analysis steps performed on the same dataset consistently produces the same answer.

rendered output
: This is what the text will look like on an online page in Github or web page

research compendia
: This is a collection of all digital parts of a research project including data, code, texts (protocols, reports, questionnaires, metadata). The collection is created in such a way that reproducing all results is straight forward.

research data management
: *Acronym: RDM*. Refers to the organisation, storage and preservation of data created during a research project. It covers initial planning, day-to-day processes and long-term archiving and sharing. Shortened to RDM.

research ethics
: Research ethics are the moral principles that govern how researchers should carry out their work. These principles are used to shape research regulations agreed by groups such as university governing bodies, communities or governments. All researchers should follow any regulations that apply to their work.

research objects
: Research objects are living resources aggregating inputs, materials, methods and/or software used in research.

review
: Suggesting changes or asking for committing something to an already created pull request.

risk
: A term that refers to the likelihood and impact of something happening. It's often used in decision-making contexts to evaluate the potential consequences of actions

risk assessment
: This is used to help choose the appropriate sustainable software concepts for your project.

risk matrix
: A risk matrix is a way of quantifying what’s going on with the thing you’re interested in. One axis measures exposure in some way, and the other the impact of a mishap. The further from the origin, the more safeguards are needed to make the risk acceptable.

roadmapping
: This is the creation of a roadmap for your project. It is an outline for the work you need to do. It covers your goals, vision and a timeline for tasks.

robust
: A result is robust when the same dataset is subjected to different analysis workflows to answer the same research question (for example one pipeline written in R and another written in Python) and a qualitatively similar or identical answer is produced. Robust results show that the work is not dependent on the specificities of the programming language chosen to perform the analysis.

rule
: An element of the Makefile that defines something that must be built, usually consists of targets, recipes, and optionally, prerequisites.

runtime test
: Tests embedded within the program which are run as part of it.
```

---

## S

```{glossary}
self archiving
: Placing a publication or other research outputs in a suitable repository, institutional or subject-based, following the possible restrictions posed by the publisher, for example an embargo period, or limits on the allowed version to be deposited in such archives.

self reflection
: Activity of thinking about our thoughts, feelings, emotions, behaviour action, and the reasons that may lie behind them. Taking the time for reflection we can grow our understanding of who we are, what our values are, and why we think, feel, and act the way we do. When we self-reflect and become more conscious of what drives us, we can more easily make changes that help us more easily develop our self or improve our life including the way we conduct research (source: [Berkeley Wellbeing](https://www.berkeleywellbeing.com/what-is-self-reflection.html)).

SHA
: Unique string of numbers of letters used to identify every commit or node in the repository.

shared authorship
: Some journals permit the use of group names but many require contributors to be listed and/or the writing group to be named. This is the same as group authorship.

smoke testing
: Very brief initial checks that ensure the basic requirements required to run the project hold. If these fail there is no point proceeding to additional levels of testing until they are fixed.

source available
: Where the source code of a piece of software is made available but not under the terms of an {term}`open license<Open License>`, you may have to pay to access the source code and agree to terms which prohibit its redistribution, or the code may be generally available and only prohibit commercial redistribution.
  Source available code is proprietary but not closed source.
  Whilst generally used in the context of software it can apply in other contexts such as {term}`open hardware<Open Source Hardware>`.

staged
: Staging the changes that will be included in the next git commit.

stale
: {term}`Issues <issues>` and {term}`pull requests <pull request>` become stale when they have been open for an extended period of time with no progress or engagement.
  This becomes a problem as the chance of these issues being completed reduces, as knowledge and enthusiasm are lost.
  It is also possible that bug reports become so out of date they are no longer relevant, or {term}`pull requests <pull request>` are so far out of sync that merging is difficult.
  There is no canonical definition of stale, however, some progress may use automation to close items after a set period of inactivity.

stochastic code
: Code which, while correct, does not always output the same result. For example a program that outputs ten random numbers will generate a different result each time, despite being correct.

syntax
: The structure of statements in a computer language.

system testing
: A level of the software testing process where a complete, integrated system is tested. The purpose of this test is to evaluate whether the system as a whole gives the correct outputs for given inputs. Also see end to end test.
```

---

## T

```{glossary}
target
: The outcome of a rule in a Makefile. It is usually a file. If it is not a file, it’s a phony target.

test driven development
: A process of code development where unit tests are written before the units themselves.

test stub
: Fake implementations of parts of code which are used in testing to remove dependencies.

test suite
: The tests that have been written for a project.

testing framework
: Tools that make writing and running tests less labour intensive.

Travis
: A commonly used continuous integration platform.
```

---

## U

```{glossary}
unit
: A small piece of code that does one simple thing. It usually has one or a few inputs and usually a single output.

unit testing
: A level of the software testing process where individual units of a software are tested. The purpose is to validate that each unit of the software performs as designed.
```

---

## V

```{glossary}
virtual machine
: A simulated computer that can encapsulate and entire computational environment including its operating system, customised settings, software and files.
```

---

## W

---

## X

---

## Y

```{glossary}
YAML
: A human readable/writable markup language which used by many projects for configuration files.
```

---

## Z
