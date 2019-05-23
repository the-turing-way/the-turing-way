# Instructor guide to running a 'Boost your research reproducibility with binder' workshop

## Target audience
This workshop is aimed at researchers and others who are:
* Interested in reproducibility, containers, Docker or continuous integration;
* Already familiar with R Markdown or Jupyter notebooks;
* Looking to communicate their research more effectively.
There is no requirement to be familiar with the command line. The [workshop advert](workshop_advert.md) has more details about why people should attend the workshop.
The workshop is designed for 20-25 participants with 4-5 helpers and instructors.

## Venue requirements
This workshop works best in a room with small tables so that participants can support each other during the practical session. The other key requirements are a projector, reliable wifi and plenty of plug points.

## Before the workshop
Information should be sent out to participants one week before the workshop with instructions to get a GitHub account, bring a small sample of code and data to 'binderise', and guidance on getting to the venue. There are [example emails](before_workshop.md) which were sent out to participants for the Turing Way-run workshops in Manchester and London in March 2019.


## On the day
The agenda below reflects the workshops which the Turing Way ran in Manchester and London in March 2019. 
The timings were designed to allow those with caring responsibilities to attend the workshops and to give enough time for participants to work on getting their own code and data into Binder.
Throughout the workshop participants were encouraged to use the Carpentries' [post-it note system](https://software-carpentry.org/blog/2015/03/teaching-tips.html) to indicate when they had completed a task (with a green post it) and when they were struggling and needed help (with a red post-it). Participants were also encouraged to help each other with problems that they might be experiencing in order to create a more supportive atmosphere.
The following resources are needed on the day: 
* Name stickers
* Small stickers to indicate that participants do not want to be photographed (coloured dots were used for the Turing Way workshops)
* Big post-its for the introductory exercise
* Lots of small post-its to be used throughout the day, if possible in red and green, or at least two contrasting colours
* A [HackMD](https://hackmd.io/) file, or similar collaborative document, to allow participants to have discussions and share their working Binders. It is helpful to have the URL for this on posters around the room in case participants miss it during the introductory presentation

### 9.30 - 10.00: Registration, coffee and introductions
As participants arrived they were asked to answer three questions as they signed in:
* Who are you (job role, disciplinary background)?
* Why did you come to the workshop and what are you hoping to get out of the workshop?
* How confident are you feeling about the workshop?
Answers to these questions were written on post-its and added to a white board which everyone could look at. Doing this prompted discussion between participants about their hopes and fears, and helped instructors to pitch the workshop to participants' interests and needs.

### 10.00 - 10.30: Introduction to the workshop and The Turing Way
The workshop begins with an [introductory presentation](/workshop-presentations/PRE_IntroBoostResReproBinder_ATI.pdf) setting out the aims for the day, some background on reproducibility and introducing the [Code of Conduct](https://github.com/alan-turing-institute/the-turing-way/blob/master/CODE_OF_CONDUCT.md). At the end of the introductory presentation participants are given the URL for the HackMD (or similar) file and asked to introduce themselves in the document.

### 10.30 - 12.00: Why you need a reproducible computing environment and how Binder can help
This section involves a [presentation](/workshop-presentations/ReproducibleComputationalEnvironment.pdf) and a small group exercise working through some [paired examples](paired_examples.md). 

The paired examples give participants a chance to see what happens when there are changes in the computational environment and how they can affect the outputs of some simple code. There are 3 examples which use Python and 1 in R, each in their own GitHub repository. Examples 2, 3 and 4 (the R example) all have two branches, with small differences in the computational environment in the different branches.  Participants were given 20 minutes to work through the examples in small groups and there was then a discussion with the whole group about what the differences were between the examples and what changes those differences caused. 

### 12.00 - 1.00: Lunch

### 1.00 - 2.00: Zero to Binder, a guided tour of building a Binder resource
This section has it's own [instructor guide](workshop-presentations/instructor-guide_zero-to-binder.md), [instructions for live coding with participants](workshop-presentations/zero-to-binder.md) and [solo instructions](workshop-presentations/zero-to-binder-solo.md) to help instructors prepare for the workshop.

### 2.00 - 3.30: Build your own Binder (with coffee from 2.00)
In this part of the workshop participants try to build their own Binder using code and data they have bought with them. Helpers should move around the room helping people who indicate that they are having problems with a red post-it on their laptops and checking in with everyone. There is no formal coffee break in the afternoon but participants are encouraged to take a break at times convenient to them - usually whilst their Binder is building!

Just before the end of this session participants are asked to add links to their completed binders in the HackMD file so that they can demonstrate them in the final session.

### 3.30 - 4.00: Demonstrating your Binder, general questions, feedback and close
The last session of the day focuses on participants demonstrating their Binders. The easiest way to do this is to have one laptop connected to the projector with the HackMD file open so that all Binders can be demonstrated without worrying about connectors or wasting time. These demonstrations frequently generate questions and give participants a chance to discuss what they found easy/hard about creating a Binder.

After the demonstration participants are given a chance to ask any general questions and asked to fill out the [feedback form](feedback_form.md), which for the Turing Way workshops were created in Google Forms.


### 4.00 - 5.00: Optional hangout with instructors
When the Turing Way ran the workshops the official close was 4pm but instructors and helpers made themselves available for another hour to fix specific bugs which emerged during the afternoon and discuss specific questions with participants.


## After the workshop
In keeping with the spirit of working openly after each of our workshops we uploaded feedback (with participants' permission) to our [GitHub repository](https://github.com/alan-turing-institute/the-turing-way/tree/master/workshops/boost-research-reproducibility-binder/feedback).

If after running a workshop you have suggestions on how it could be improved please [contribute them back to the Turing Way](https://github.com/alan-turing-institute/the-turing-way)!
