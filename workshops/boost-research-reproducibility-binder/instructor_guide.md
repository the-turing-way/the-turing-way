# Instructor guide to running a 'Boost your research reproducibility with binder' workshop

## Target audience
This workshop is aimed at researchers and others who are:
* Interested in reproducibility, containers, Docker or continuous integration;
* Already familiar with R Markdown or Jupyter notebooks;
* Looking to communicate their research more effectively.
There is no requirement to be familiar with the command line.
The [workshop advert](workshop_advert.md) has more details about why people should attend the workshop.
The workshop is designed for 20-25 participants with 4-5 helpers and instructors.

## Venue requirements
This workshop works best in a room with small tables so that participants can support each other during the practical session.
The other key requirements are a projector, reliable wifi and plenty of plug points.

## Before the workshop
Information should be sent out to participants one week before the workshop with instructions to get a GitHub account, bring a small sample of code and data to 'binderise', and guidance on getting to the venue.
Participants should be reminded to bring a laptop with them (unless computers are provided at the venue).
There are [example emails](before_workshop.md) which were sent out to participants for the workshops run by *The Turing Way* in Manchester and London in March 2019.

## On the day
There are two sample agendas detailed below.
The workshop was originally designed as a full day workshop, but it can be fitted into a shorter 3 hour (half day) schedule.

Throughout the workshop participants were encouraged to use the Carpentries' [post-it note system](https://software-carpentry.org/blog/2015/03/teaching-tips.html) to indicate when they had completed a task (with a green post it) and when they were struggling and needed help (with a red post-it).
Participants were also encouraged to help each other with problems that they might be experiencing in order to create a more supportive atmosphere.

The following resources are needed on the day:
* Name stickers
* Small stickers to indicate that participants do not want to be photographed (coloured dots were used for The Turing Way workshops)
* Big post-its for the introductory exercise
* Lots of small post-its to be used throughout the day, if possible in red and green, or at least two contrasting colours
* A [HackMD](https://hackmd.io/) file, or similar collaborative document, to allow participants to have discussions and share their working Binders.
  It is helpful to have the URL for this on posters around the room in case participants miss it during the introductory presentation

The following sections describe the parts of the workshop.
Recommended timings are included in the tables below.

### Registration and introductions
As participants arrived they were asked to answer three questions as they signed in:
* Who are you (job role, disciplinary background)?
* Why did you come to the workshop and what are you hoping to get out of the workshop?
* How confident are you feeling about the workshop?

Answers to these questions were written on post-its and added to a white board which everyone could look at.
Doing this prompted discussion between participants about their hopes and fears, and helped instructors to pitch the workshop to participants' interests and needs.

For the full day workshop, we recommend providing coffee for this informal start to the day.

### Introduction to the workshop and The Turing Way
The workshop begins with an [introductory presentation](workshop-presentations/PRE_IntroBoostResReproBinder_ATI.pdf) setting out the aims for the day, some background on reproducibility and introducing the [Code of Conduct](https://github.com/alan-turing-institute/the-turing-way/blob/master/CODE_OF_CONDUCT.md). At the end of the introductory presentation participants are given the URL for the HackMD (or similar) file and asked to introduce themselves in the document.

### Why you need a reproducible computing environment and how Binder can help
This section involves a [presentation](workshop-presentations/ReproducibleComputationalEnvironment.pdf) and a small group exercise working through some [paired examples](paired_examples.md).

The paired examples give participants a chance to see what happens when there are changes in the computational environment and how they can affect the outputs of some simple code. There are 3 examples which use Python and 1 in R, each in their own GitHub repository. Examples 2, 3 and 4 (the R example) all have two branches, with small differences in the computational environment in the different branches.  Participants were given 20 minutes to work through the examples in small groups and there was then a discussion with the whole group about what the differences were between the examples and what changes those differences caused.

### Lunch

Everyone loves free food :wink:.
But also we recommend using this time to get to know the participants a little more.
Ask them about their research and the specific challenges that they have making it reproducible.

### Zero to Binder, a guided tour of building a Binder resource
This section has it's own [instructor guide](workshop-presentations/instructor-guide_zero-to-binder.md), [instructions for live coding with participants](workshop-presentations/zero-to-binder.md) and [solo instructions](workshop-presentations/zero-to-binder-solo.md) to help instructors prepare for the workshop.

### Build your own Binder
In this part of the workshop participants try to build their own Binder using code and data they have bought with them.
Helpers should move around the room helping people who indicate that they are having problems with a red post-it on their laptops and checking in with everyone.

If you're running the full day workshop we recommend having coffee (and cake) arrive halfway through this session.
Participants are then encouraged to take a break at times convenient to them - usually whilst their Binder is building!

Just before the end of this session participants are asked to add links to their completed binders in the HackMD file so that they can demonstrate them in the final session.

### Demonstrating your Binder and general questions
The last session of the day focuses on participants demonstrating their Binders.
The easiest way to do this is to have one laptop connected to the projector with the HackMD file open so that all Binders can be demonstrated without worrying about connectors or wasting time.
These demonstrations frequently generate questions and give participants a chance to discuss what they found easy/hard about creating a Binder.

### Feedback, group picture and close
At the end of the workshop participants are given a chance to ask any general questions and asked to fill out the [feedback form](feedback_form.md), which for The Turing Way workshops were created in Google Forms.

Before the official close by one of the instructors, try to take a group picture of all participants who want to be in it.
This can be really positive way of sharing the community building aspect of these workshops.

### Optional hangout with instructors
When *The Turing Way* ran the workshops the official close was 4pm to ensure that people with caring responsibilities could finish the workshop and not have to leave early.
Instructors and helpers made themselves available for another hour to fix specific bugs which emerged during the afternoon and discuss specific questions with participants who wanted to stay a little longer.

## Sample agendas

### Full day workshop

The full day workshops were run by *The Turing Way* in Manchester and London in March 2019.
The timings for the full day workshop are designed to allow those with caring responsibilities to attend the workshops and to give enough time for participants to work on getting their own code and data into Binder.

| Time | Activity |
| ---- | -------- |
| 9:30 - 10:00 | [Registration and introductions](#Registration-and-introductions) |
| 10:00 - 10:30 | Introduction to the workshop and The Turing Way](#introduction-to-the-workshop-and-the-turing-way) |
| 10.30 - 12.00 | [Why you need a reproducible computing environment and how Binder can help](#why-you-need-a-reproducible-computing-environment-and-how-binder-can-help)
| 12:00 - 13:00 | [Lunch](#lunch) |
| 13:00 - 14:00 | [Zero to Binder, a guided tour of building a Binder resource](#zero-to-binder-a-guided-tour-of-building-a-binder-resource) |
| 14:00 - 15:30 | [Build your own Binder](#build-your-own-binder) |
| 15:30 - 15:50 | [Demonstrating your Binder and general questions](#demonstrating-your-binder-general-questions-feedback-and-close) |
| 15:30 - 16:00 | [Feedback, group picture and close](#feedback-group-picture-and-close) |
| 16:00 - 17:00 | [Optional hangout with instructors](#optional-hangout-with-instructors)

### Half day workshop

The half day workshop was run by *The Turing Way* at [Carpentry Connect](https://software.ac.uk/ccmcr19) in Manchester in June 2019.
It shortens the introduction and gives less time for participants to Binderise and showcase their own projects, but keeps the core exercises and the worked example project.
The times follow the Carpentry Connect schedule, but can be adjusted as needed.

| Time | Activity |
| ---- | -------- |
| 13:30 - 13:40 | [Registration and introductions](#Registration-coffee-and-introductions) |
| 13:40 - 13:50 | [Introduction to the workshop and The Turing Way](#introduction-to-the-workshop-and-the-turing-way) |
| 13:50 - 14.30 | [Why you need a reproducible computing environment and how Binder can help](#why-you-need-a-reproducible-computing-environment-and-how-binder-can-help)
| 15:00 - 15:30 | Coffee break :coffee: |
| 15:30 - 16:30 | [Zero to Binder, a guided tour of building a Binder resource](#zero-to-binder-a-guided-tour-of-building-a-binder-resource) |
| 16:30 - 16:50 | [Build your own Binder](#build-your-own-binder) |
| 16:50 - 17:00 | [Feedback, group picture and close](#feedback-group-picture-and-close) |

## After the workshop
In keeping with the spirit of working openly after each of our workshops we uploaded feedback (with participants' permission) to our [GitHub repository](https://github.com/alan-turing-institute/the-turing-way/tree/master/workshops/boost-research-reproducibility-binder/feedback).

If after running a workshop you have suggestions on how it could be improved please [contribute them back to The Turing Way](https://github.com/alan-turing-institute/the-turing-way)!
