(cm-new-community-techissue)=
# Addressing Technical Issues

Make sure that you also have plans in place for people who want to contribute to your project but might deviate from your original goals very fast without supervision or guidance.
If specific skills or practices are required for someone to contribute to your project, you should be able to point people to relevant resources so that they can engage with your project effectively.

Here are some recommendations to prepare your project for addressing technical issues that your team or community members can most likely face.

## Setup tools to enable collaboration

When writing up research either of the final report or for sharing preliminary findings, there should be a conscious decision about what software you are using to write out your result.
This decision affects how collaboration will look like in your project.
To avoid any potential barriers to collaboration, take the following aspects into considerations:
* **Availability of software**: Ensure that all of the collaborators have access to the software and platform you are using, for example, paid subscription or licence to use proprietary software.
* **Technical skills**: Ensure that all of the collaborators are comfortable using the software, for example, they are confident to edit a file written in a programming or mark-up language.

Context-specific issues may appear depending on the roles and responsibilities shared within a team.
Therefore, potential solutions can be planned to address these issues including providing short tutorials (see the next point).
Being aware of the potential barriers that the software we use may create can lead to choosing tools and solution that works for all our collaborators.

## Provide short and concise tutorials

In most of the research projects, we work on what is urgent right now, which might mean that we may overlook what is important in the long term.
For example, we might want to test several algorithms on our data but don’t pay attention to recording the outcome systematically in a central platform that others access.
Offering training or short pre-recorded videos on recommended practices can enable your community members to work using a standard workflow or take over some tasks from others.

## Testing is important

To err is human! And when working under pressure, they might be more frequent.

Test your codes and encourage your community to review and test each other's code.
In addition to writing code that solves problems, you should teach and promote the practice of [unit testing](http://softwaretestingfundamentals.com/unit-testing/) to test if the individual units/components of software work as expected.

You can also set up a {ref}`Continuous Integration<rr-ci>` environment to help automate testing in your workflow.

See the {ref}`testing <rr-testing>` section in the Guide for Reproducible Research for more information.

## Reproducibility is even more important

A great thing for less involved team members to do is constantly test the reproducibility of any code/environment.
Do this from the start and it won’t be a surprise later when it doesn’t work on somebody else’s computer.

Reach out to the experts, especially when dealing with legacy code.
Reach out to other communities with specific expertise to save effort and time that can be invested in other tasks. For example, a lot of the scientific knowledge is built on top of results from FORTRAN, C, and Java code that isn't maintained any longer and, probably, isn't documented. Finding someone with the knowledge and experience of the legacy code to answer questions that other developers have will be a huge time saver.

See the {ref}`Guide for Reproducible Research <rr>` chapter for more information.

## Share code (and data) early on

Developers must share their code in a public version-controlled repository (like GitHub and GitLab) and coordinate who is working on what feature or fix.
Especially, when running on urgent projects against the clock, it is crucial not to waste time at the end of your project in compiling the different components of your research when you can practice doing it from the beginning.

## Take note of the privacy issues

Ask yourself, how can people who need to access this data get to it.
How they can re-use and share the data appropriately.
Choose an appropriate open source license for your data, scripts, and software.
Choose a relevant license ensuring the protection of information that is sensitive such as movement and location data, personal health issues, contact information, names, date of birth, and personal addresses.
Avoid gathering personal information that is not necessary or breaches confidentiality.
