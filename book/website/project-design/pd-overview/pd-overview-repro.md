(pd-overview-repro)=
# Communication and Collaboration for Reproducibility

Good communication from collaboration practices are complementary to research reproducibility, and often it is hard to separate these concepts from each other.
In _The Turing Way_, we consider essential for research reproducibility and provide separate guides for {ref}`communication<cm>` and {ref}`collaboration<cl>`.
You can visit specific chapters to gain in-depth understanding and evaluation which practices meet the specific requirements in your project.

Here, we provide a non-exhaustive list of ways to ensure that you, and everyone else, understands (and communicate about) what the project is about, who the stakeholders are and they can collaborate.

- Document all practices to ensure everyone is on the same page (literally!).
Provide all documentation in a centralised, findable and accessible location.
- State vision, goals and milestones clearly. Provide what the expected outcomes and deliverables are.
- Highlight different stakeholders with their roles, skills, interest and contact (when possible)
- Describe what opportunities for collaboration different members will have.
If possible (such as in open source project), encourage people to be involved in the project.
- Provide details for those outside the current group who you might want to invite.
Describe how new members from a variety of different backgrounds and skills can start contributing
  - Provide clear ways for contributions, review, management, mentoring and support.
- Provide an overview of how different contributions or resources are connected and how new contributions fit smoothly into existing material.
  - Describe possible expansion of features in pre-determined and agreed ways at stages beyond the initial implementation.
- Provide a decision-making framework to facilitate discussions and reaching to a common conclusion.
In the context of software, coding projects are as much about communication as it is about coding (if not more).
  - Allow informed discussions when a particular project design has reached the end or when it is useful to update it for efficiency and sustainability
- Provide an overarching as well as short-term goals and describe expected outcomes to help contributors move away from focusing on a single idea of feature.
- Provide resources on ways of working to ensure fair participation of stakeholders who collaborate on short- and long-term milestones within the project.
  - It reduce or address concerns about project's progress towards meeting goals and prevent potential fallout between project stakeholders.
- Communicate the work culture that you want to promote and policies that ensures safety and security of both your data and people.
- Describe how your research work is or will be made available and how different stakeholders will be recognised.
  - It helps everyone feel recognised for their contribution to the overall vision.

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

(pd-overview-repro-mistakes)=
## Bonus Section: Learning from Mistakes

> “Building takes many, many mistakes.”
> ― Becky Chambers, [The Long Way to a Small, Angry Planet](https://www.goodreads.com/work/quotes/42270825)

Learning about past design mistakes can give us insight on what we can do differently in the future.
We asked a group of researchers to share what they consider their project design regrets, which we have summarised here:

- Not advocating for clearer goals and success criterion from the beginning.
- Not communicating the project vision clearly/often enough to the other team members. Getting distracted by side shoots.
- Not ensuring that all stakeholders were fully aware of the nature of the project.
- Not understanding that project design is about people first. Designs motivate stakeholders, and allow collaboration and inclusion.
- I guess I wrote these as actions I wish I had done better - Setting short- and long-term milestones, communicating and enforcing norms for collaborator engagement, delegating work and project management tasks.
- Not having documentation besides final reports. When being asked the code or dataset (raw and process), step by step process from preparing data to getting the results, lack of documented guidance in one places made it hard to trace the project with all team members (classic problem).
- Not properly taking into account the degree to which requirements will change throughout a project - which happens a lot in academia - and the effect this has on designs that then also need to change.
- Trying to plan too much at the beginning and never getting started.
- Feeling like I am always taking an ad hoc approach to planning a project and then feeling like I am spending too much time on the organisation side of the project because I don’t have a set workflow to handle project planning and design. Also, not knowing how does project planning fit into project design.
- Using a very messy excel to store/process data, the shame!
- Over-engineering a design for features that didn’t end up being implemented (in life before academia!)
- Not implementing Git flow from the start, and not teaching collaborators how to use Git flow.
- Not developing tests until after a significant amount of code was written.  
- Not doing code reviews.
- Not defining use scenarios for the software from the beginning, meaning we didn’t pay enough attention in data input and output.  
- Agonising too long before switching to objectively better design (particularly translating from a largely functional codebase to more object-oriented)    
- Going with options that team members are ‘comfortable’ with rather than teaching team members new skill. For example, using outdated languages or platform-dependent compilers  Makes life more difficult in the long run.
- Defining governance at different stages of the project or potential scenario planning for how governance might change as project scales up/down/gains new users and so on.
- Not thinking about community from the start, starting with a Code of Conduct, thinking about a Contributor License Agreement (intellectual property), what processes will be used and how they will work, how they will impact future contributors and the overall project.

```{note}
**I work alone, do I need to think about project design?**

It is really hard for a project to move from practices that were designed for one person to practices that work for a team.
Therefore, it is essential to document and use practices that enable collaboration ensuring good team practices that describe: how will work be split, how will it be reviewed, how will decisions be made, and so on.

A little work and time investment early on in project design saves a lot of time later when any circumstances that demand change.
Project design would not ensure that everything will go as planned or there will be no unexpected challenge.
However, it helps prepare in advanced for risk management and adapt for changes better.
Learn how agile methodologies help adapt to changes and see “The cost of change curve” in the context of Software Engineering.
```

*_This chapter summarises participants' notes from a short workshop called "Good Practices for Designing Software Development Projects (The Turing Way)" at the [Collaboration Workshop 2021](https://www.software.ac.uk/cw21)  hosted by [Software Sustainability Institute](https://www.software.ac.uk). The workshop was delivered by Malvika Sharan, Emma Karouns and Batool Almarzouq on 31 March 2021. You can  Zenodo. [DOI: [10.5281/zenodo.4650221](https://doi.org/10.5281/zenodo.4650221)._
