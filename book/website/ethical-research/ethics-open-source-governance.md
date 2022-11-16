(er-ethics-open-source-governance)=
# Ethical Considerations when Choosing an Open Source Governance Model

(er-ethics-open-source-governance-summary)=
## Summary

Open source projects should be rooted in ethical principles. 
Sharing the code so that anyone can use it, welcoming contributors and creating communities around specific projects are the core of open source. 
But open source communities also have the responsibility to ensure they build a safe and inclusive environment, understand who might be affected by their projects or check that their tools are not being misused. 
Therefore, Open Source Governance Models, which provide a structure for decision making and community feedback in open source projects, should embed those ethical considerations within their structure, but the framework to do so is far from well-established. 
This chapter discusses some of the key points to take into consideration when designing and implementing ethical guidelines in governance models.


```{note}
**What does ethics in governance mean?**

*Ethical behaviour in governance is defined as the way in which stakeholders try to manage collective action from the perspective, and in the interest, of the majority, thus avoiding damaging behaviours, and through a better control of the power and responsibilities of the leaders. In the area of governance, therefore, ethics aims at raising awareness of the others' rights and common needs, by imposing some principles of minimum requirement.*

Source: Dessain, V., Meier, O., & Salas, V. (2011). {cite}`Corporate Governance and Ethics<Dessain2011governance>`.
```

(er-ethics-open-source-governance-motivation)=
## Motivation and Background

When setting up open source projects, it is important to pick a structure for organising the community that takes into account ethical considerations.
The way that your governance model is designed has a significant impact on the ethics, diversity and inclusion in your project.
Critically examining the implied ethics of a particular structure is a crucial part of the process of selecting one. 
However, it is difficult to know where to start when planning governance structure for your open source projects.
It can be even more challenging when considering if a particular governance model align with ethical framework of your project.
Therefore, we have designed this chapter to offer some starting points to consider. 

*This chapter is adapted a speedblog from the Collaborations Workshop 2022, authored by  Yo Yehudi,
Arielle Bennett, Gemma Turon, Declan Bays, Sarah Gibson, Stephan Druskat, Yadira Sanchez, Sophia Batchelor, which is published under a CC-BY license. Read the original article on Software Sustainability Institute's Blog page: [Ethical Considerations for Your Open Source Governance](https://software.ac.uk/blog/2022-07-07-ethical-considerations-your-open-source-governance)* 

(er-ethics-open-source-governance-selfreflection)=
## Ethical Governance Starts with Self-Reflection 

The process of interrogating the ethics of a governance model starts with {ref}`er-self-reflection` on the nature and intention of your project. 
Take things right back to first principles and ask yourself (and the project team):
* Why are you doing this project? 
* Who is the project for?
* Who creates and maintains it? 
* How will project be used? 

These questions may not always be captured in a general document such as the README page, however by scoping the impact and influence of a project before it begins, a team can lay an ethical foundation from the outset. 

For many projects that are community led, this means involving the people that are affected by the project’s outcome in the design, development, and deployment stages.
True co-creation is an active process of inclusion, and there are many levels of engagement that can be tailored to a projects’ individual needs (see the figure - Arnstein's Ladder of Citizen Participation), which a governance model might also need to take into account, for example, how is delegated power dealt with by the project?  


```{figure} ../figures/ladder-of-participation.*
---
name: ladder-of-participation
alt: Colourful graphic of Arnstein's Ladder of Participation (1969) drawn by Juliet Young. A rainbow ladder describes the different types of participation in research - manipulation, educating, informing, consultation, placation, partnership, delegated power and citizen control. 
---
Arnstein's Ladder of Citizen Participation, illustration credit - [@clinical.creative.psychologist (Juliet Young)](https://twitter.com/juliet_young1/status/1384604477697761281)
```

No open source project is an island.
The goal of making projects open source is to explicitly invite the kind of use and collaboration which leads to a community of contributors and collaborators; making the world a better place, one commit at a time.
It's important that the governance model you select provides robust mechanisms for the level of community participation you are hoping to achieve with your project.
Self-reflection is a useful starting point to guide your decision making. 

(er-ethics-open-source-governance-continuous-process)=
## Ethical Governance is a Continuous Process
There are many ways in which your project can (and probably will) change over its lifetime, and some of these changes may be unexpected. 
For example, your software might start being used in domains you have not considered, it might experience a faster growth rate than you have expected, or you may need to decide how to handle an influx of new contributors.

This may also mean that you have to change the way that the project is run, to actively include new parts of the community, deal with a surge in contributions, or face new challenges.
In this scenario, try and reflect the ways in which the governance of your project should evolve to reflect the ethics you commit to.
For instance, is your governance structure built to allow the whole community to participate and influence a project that will in turn influence themselves and their work?

It may feel like a giant leap to go from, a free-form do-ocracy where contributors pitch in according to their personal priorities, to something more structured, or to give up your position of benevolent dictator, or to introduce different voting rules for the steering committee, but if you want your project to reflect your ethics, you will need to allow your ethics to impact the project, and iterate on this process. 
It is a bit like putting debugging checkpoints in the way you run your project: run, but halt to reflect if you encounter a state that is unethical, based on your definition of ethical. 

In short: `if (ethical == true) { // Do stuff } else { // FIXME }`

(er-ethics-open-source-governance-action)=
## Ethics Need Governance to become Actionable
Open source project communities may already have an implicit set of ethics regarding their project in place. 
However, unless these ethics are being made explicit, and inform a structured model of governance, they will remain inconsequential or, as Jo Freeman has put it in her essay {cite}`The Tyranny of Structurelessness<Freeman2012Stuctureless>`, impotent.

To empower your project to act on your ethics, it will need some governance model to adhere to. 
There already exist a number of more-or-less established governance models and you can take a look at the resources section of this chapter for links to more information on them. 
Keep in mind, though, that not all of them may cater well for an ethical framework or the specific ethical framework you have in mind.

(er-ethics-open-source-governance-technology)=
## Do Not Rely on Technology to do Your Ethics for You

In an age of automation, bots, and exceptional investment into AI, you might be inclined to think “This all sounds like a heavy workload - how do I even get started?” You might consider a couple of options - 

1. Do I adopt an existing governance model? 
2. Maybe I should get a computer system to do it for me, or at least help me out?

Pulling a governance system out of the box is a great way to get started, but don’t assume that because a governance system has been in use before - perhaps even successfully - that the governance system has all the ethical solutions worked out, or even all the practical challenges have been considered. 
For instance, the “benevolent dictator for life” (BDFL) open source governance model has practical as well as ethical issues: what if that BDFL has an unexpected health crisis and disappears? 
What if the benevolent dictator begins displaying values that are at odds with those of the wider community?
What if they’re missing viewpoints that were obvious if only the governance committee was more than one person?
Take python as an example. 
Originally set up as a "benevolent dictatorship for life", the BDFL, Guide Van Rossum, [eventually abdicated and transferred power to the community in 2018](https://www.mail-archive.com/python-committers@python.org/msg05628.html), citing burnout as the main reason. 
Benevolent dictatorships for life limit the sustainability of open source projects by tying them too closely to one person, and remove formal paths for intervention when something goes wrong. 

Relying on technology to be your governance is equally risky.
Technology can be an incredible tool, but so long as it’s the only tool you have put in place for making governance decisions, it’s likely to be a potential problem.
This is why it is important to start the process of governance selections with self-reflection, so that you are aware of all the requiremeents in the projects and prepared to implement ethical measures for them.

(er-ethics-open-source-governance-conclusion)=
## Conclusion

By its nature, open source technology can deliver benefits to all societies. 
However, projects started with all the best of intentions can still evolve into something malicious through poor guidance and oversight. 
Such considerations should therefore be noted and addressed through the application of a formal governing structure throughout any such projects, especially in sensitive areas where conflicts are likely to arise. 
While the use of a governance structure doesn’t negate the possibility of bad things from happening, it does however provide a framework which allows us to put such actions into context.
In this chapter, we have provided some ethical pointers for open source project communities to consider when constructing their governance models, to support the continual evolution of open source towards a more just and equitable ecosystem for all contributors and users. 

(er-ethics-open-source-governance-resources)=
## Additional Resources
* [Invest in Open Infrastructure - Resources on Good Community Governance Research + Literature Collection](https://investinopen.org/research/good-community-governance/)
* [Community Rules - Simple Templates for Great Communities](https://communityrule.info/book/)
* [RedHat Blog - Understanding Open Source Governance Models](https://www.redhat.com/en/blog/understanding-open-source-governance-models)
