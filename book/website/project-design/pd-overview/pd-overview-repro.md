(pd-overview-repro)=
# Collaborative project documentation

Good communication and collaboration practices are complementary to research reproducibility, and often it is hard to separate these concepts from each other.
In _The Turing Way_, we consider these essential for reproducible research and provide separate guides for {ref}`communication<cm>` and {ref}`collaboration<cl>`.

In this page, we highlight some of the most important recommendations for collaboration and communication to ensure that you, and everyone else in your project, understand what the project is about, who the stakeholders are and how they can participate.
You can visit specific chapters to gain an in-depth understanding and selection of practices that meet the specific requirements in your project.

## Minimal documentation

Your open source project should at a minimum provide a license together with a README file with all the basic, general information a newcomer needs to get oriented.
The license to apply will depend on your type of research output (text, data, software, hardware, reagents to name a few).
See the license chapter {ref}`rr-licensing`
It should contain a **recognizable name** for your project, as well as a **declaration of the licensing terms** under which it may be distributed (see the {ref}`rr-licensing-hardware` chapter).

Documentation should be shared via centralised, findable and accessible platforms.

## Documenting project plans and processes
 
Document the **current state**, **ongoing development**, and/or any **future plans** for the project.
Add information on available resources and recommended practices to ensure everyone is on the same page (literally!).
It may also be important to make it clear what your project is not meant to be.

In addition to the above, it is interesting to document the *principal need* for your project, especially for software and hardware project: what problem are you trying to solve ?
That includes a **problem description** of whatever issue sparked the project, a **functional description** of how your project is meant to address it, and a **context description** of the users and environment your project is targeting. 

It is particularly important to share the **vision, mission, and milestones** clearly. 
Provide sufficient information for what the expected outcomes and deliverables are.


Provide overarching as well as short-term goals and describe expected outcomes to help contributors move away from focusing on a single idea of the feature.
Describe the possible expansion of features in pre-determined and agreed on ways at stages beyond the initial implementation.

## Project's "Who-is-Who"

Include a **list of contributors**, **contribution guidelines**, and information on **contact points** where to ask for help.
In addition, 
- Create an overview of  the putative "personas" {ref}`pd-persona` (people and organisations) and how they may interact with the project. 

Describe what opportunities for collaboration different members will have.
When possible, such as in an open source project, provide these details for those outside the current group, especially when you want to encourage people outside the project to be involved.
Communicate the work culture that you want to promote and policies that ensures the safety and security of both your data and people.


Provide resources on ways of working to ensure fair participation of contributors who collaborate on short- and long-term milestones within the project.
It reduces or addresses concerns about the project's progress towards meeting goals and prevents potential fallout between project contributors.

## Participation and contribution process

 In order to make your project discoverable, you may add a machine-readable metadata file, such as an [Open-Know-How manifest](https://www.internetofproduction.org/openknowhow).

Considering the variety of different backgrounds and skills your members bring, describe how they can participate and start contributing.
You should also **think about your audience**. Your project might be reused by people with different skills, roles, objectives, and socio-economic and cultural environments.


Provide clear opportunities for contributions, review, management, mentoring, and support.
Provide an overview of how different contributions or resources are connected and how new contributions will fit into existing materials.
You may also include an index of all the project's documentation, so people can easily find what they are looking for.

Provide a decision-making framework to facilitate discussions and reaching a shared conclusion.
In the context of software and hardware, open source projects are often as much about communication as they are about coding or building (if not more).
Allow informed discussions when a particular project design has reached the end or when it is useful to update it for efficiency and sustainability.
 
Describe how your research objects are available or will be published and how different contributors will be recognised.
It helps when everyone feel appreciated and acknowledged for their contribution to the overall vision.

<!--
(pd-overview-repro-turingway)=
## _The Turing Way_ Chapter for Communication and Collaboration

We recommend reading the following chapters to understand effective communication and collaboration for project design.

### Basic Requirements
- {ref}`<>`
- {ref}`<>`
- {ref}`<>`

### Advanced Requirements
- {ref}`<>`
- {ref}`<>`
-->
<!--
(this section moved to one of the landing pages instead) 
(pd-overview-repro-mistakes)=
## Bonus Section: Learning from Mistakes

> “Building takes many, many mistakes.”
> ― Becky Chambers, [The Long Way to a Small, Angry Planet](https://www.goodreads.com/work/quotes/42270825)

Learning about past design mistakes can give us insight into what we can do differently in the future.
We asked a group of researchers to share what they consider their project design regrets, which we have summarised here:

- Not advocating for clearer goals and success criteria from the beginning.
- Not communicating the project vision clearly/often enough to the other team members.
- Not ensuring that all stakeholders were fully aware of the nature of the project.
- Not understanding that project design is about people first. Designs motivate stakeholders and allow collaboration and inclusion.
- I guess I wrote these as actions I wish I had done better - Not setting short- and long-term milestones, communicating and enforcing norms for collaborator engagement, delegating work and project management tasks.
- Not having documentation besides final reports. When being asked about the code or dataset (raw and process), step by step process from preparing data to getting the results, lack of documented guidance in one place made it hard to trace the project with all team members (classic problem).
- Not properly taking into account the degree to which requirements will change throughout a project - which happens a lot in academia - and the effect this has on designs that then also need to change.
- Trying to plan too much at the beginning and never getting started.
- Feeling like I am always taking an ad hoc approach to planning a project and then feeling like I am spending too much time on the organisation side of the project because I don’t have a set workflow to handle project planning and design. Also, not knowing how project planning fits into project design.
- Using a very messy excel to store/process data, the shame!
- Over-engineering a design for features that didn’t end up being implemented (in life before academia!)
- Not implementing Git flow from the start, and not teaching collaborators how to use Git flow.
- Not developing tests until after a significant amount of code was written.  
- Not doing code reviews.
- Not defining use scenarios for the software from the beginning, meaning we didn’t pay enough attention to data input and output.  
- Agonising too long before switching to objectively better design (particularly translating from a largely functional codebase to more object-oriented).    
- Going with options that team members are ‘comfortable’ with (for example, using outdated languages or platform-dependent compilers), rather than teaching team members new skills. Makes life more difficult in the long run.
- Defining governance at different stages of the project or potential scenario planning for how governance might change as the project scales up/down/gains new users and so on.
- Not thinking about community from the start, starting with a Code of Conduct, thinking about a Contributor License Agreement (intellectual property), what processes will be used and how they will work, how they will impact future contributors and the overall project.
-->

### Preparing for Change

```{note}
**I work alone, do I need to think about project design?**

The short answer is 'yes'.
The project design will allow you to manage your work well for yourself (see the section: {ref}`Getting Started Checklist<pd-checklist>`).

A little work and time investment early on in project design saves a lot of time later when any circumstances arise that demand change.
```

It is really hard for a project to move from practices that were designed for one person to practices that work for a team.
Therefore, it is essential to document and use practices that will enable collaboration if and when you have to involve others in your project.
Considering good team practices even for a project run by an individual makes it easy for them to effectively accomplish their goals.
For example, you can define goals in your project and identify tasks by asking questions like: 
how can my work be split, how will it be reviewed, how will decisions be made, and so on.
Learn how [agile methodologies](http://www.agilenutshell.com/) help adapt to changes.
Learn about good team practices in our {ref}`section on teamwork<cl-new-community-teamwork>`.

Project design does not ensure that everything will always go as planned or there will be no unexpected challenges.
However, it helps you prepare in advance for risk management and to adapt to changes better.
Also, see [The cost of change curve](http://www.agilemodeling.com/essays/costOfChange.htm) in the context of Software Engineering.

_This chapter summarises participants' notes from a short workshop called "Good Practices for Designing Software Development Projects (The Turing Way)" at the [Collaboration Workshop 2021](https://www.software.ac.uk/cw21)  hosted by [Software Sustainability Institute](https://www.software.ac.uk). The workshop was delivered by Malvika Sharan, Emma Karoune and Batool Almarzouq on 31 March 2021. Zenodo. DOI: [10.5281/zenodo.4650221](https://doi.org/10.5281/zenodo.4650221)._
