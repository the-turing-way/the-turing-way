(er-what-is-tea)=
# What is Trustworthy and Ethical Assurance?

Let's begin with a definition:

> Trustworthy and ethical assurance is a process of using structured argumentation to clearly demonstrate how a set of claims about some goal of a system are warranted, given the available evidence.

There are several concepts in this definition that ought to be teased out.
First, there is the notion of a *structured argument*.
This idea builds on the work of the philosopher, Stephen Toulmin, who explored different uses of argumentation as practiced in everyday or professional usage (e.g. a lawyer presenting an argument in court). {cite}`toulmin1958uses`
While approaches in formal logical approaches had sought to model arguments as they *ought* to be presented (e.g. classic deductive syllogisms), Toulmin was interested in how arguments *are* presented, while stil aiming to reconstruct their underlying structure. 

This structured approach is important in the context of data science and AI, because novel data-driven technologies can make use of structured data to do a variety of interesting things.
Having a *shared* structure is also important for communication and collaboration.

```{note}
It is important to note that Trustworthy and Ethical Assurance prioritises a shared **structure**, rather than being overtly prescriptive in the **content** of ethical argumentation.
Ethical practices vary across context, and so we need a framework that is permissive and flexible enough to accomodate this variation.
```

The structured argumentation at the heart of TEA is known as *argument-based assurance* and has been used in safety-critical domains for several decades. {cite}`bloomfield2009safety`
*Safety cases*, therefore, are already widely used in many sectors (e.g. aviation, energy, infrastructure).
In short, the idea behind a *safety case* is to provide a clear and accessible argument that shows how a given system is *safe to operate* within a specified context or environment, based on a set of claims that substantiate the argument and the evidence that grounds these claims.
But what about other goals?

Safety is important, but it's not the only goal that should be pursued when designing, developing, and deploying a system or technology.
What about transparency and explainability, security and privacy, fairness and equity, sustainability and efficiency?
These goals also matter—in some cases, they may matter more than safety (e.g. operation of remote surveillance that is unlikely to cause any physical harm but violates a community's expectations of privacy and trust).

Trustworthy and ethical assurance extends the concept of a safety case to a more inclusive set of ethical principles (or goals).
Because TEA does not only deal with safety cases, we generalise the concept to *assurance* cases more broadly.  
Let's look at what an assurance case is and how we can build one.

(er-building-an-assurance-case)= 
## Building an Assurance Case

To build an assurance case we need some core building blocks.
Let's start with the simplest case—the following three elements:

1. A Goal Claim: a claim that serves to direct the process of developing an assurance case
towards some value or principle that is desirable or significant.
2. Property Claim: a claim about some property or a project or the technology/system the project seeks to build, which is deemed to be salient to the parent goal claim.
3. Evidence: a document or some artefact that supports (or justifies) a linked property claim (i.e. serves to establish the validity of the linked claim).

Consider the following example.

<!--- Insert image --->

Here, we have a goal claim, supported by three separate property claims, which each have their own linked evidence.

The top-level element, 'The AI system is explainable', sets out a goal that we can assume this hypothetical project team are attempting to justify (i.e. the *explainaibility* of their system).
The set of property claims that are linked to the goal claim do a few things:

1. They help to specify the meaning of the goal, by providing additional information about how the project team have operationalised the concept, 'explainability' within their project (or organisation).
2. They provide specific propositions (i.e. claims) that can be individually verified or falsified.
3. Collectively, the set of property claims should build confidence that the top-level goal claim is justified.

We can see, on the basis of this simple example, how the property claims and evidence provide the basis of the central argument, while the top-level goal claim serves to focus the overall assurance case.

```{note} Further Resources
Additional information about the Trustworthy and Ethical Assurance framework, including additional explanations and examples is available on our documentation site: https://alan-turing-institute.github.io/AssurancePlatform/guidance
```

But how does a team identify the relevant claims and evidence in the first place, and how should those reading an assurance case evaluate its validity or completeness?

(er-evaluating-claims)
## Evaluating Claims and Evidence

The focus of a TEA case is the top-level goal claim.
This is important, because it serves to direct a project team's attention on the over-arching purpose or value they seek to achieve by designing, developing, and deploying a system or technology (e.g. a predictive model used in healthcare for diagnosis, an autonomous vehicle in transportation, a chatbot used in education to promote self-directed learning).
Having a goal in place at the start of an argument, means that evidence is sought out to support or justify the goal claim.
The alternative would be a *post hoc* construction of an argument in support of a goal that fits existing evidence. 

Therefore, by beginning with a goal claim and progressively identifying requirements for a project to ensure this goal is achieved, a project team can judiciously seek out (or generate) evidence that supports their goal.

```{warning} Goal-Structuring Notation and Bias
There are many standards for argument-based assurance. One of these is the *Goal Structuring Notation* standard. {cite}`gsn2021` As the name suggests, this standard also prioritises 'goals' as key elements in the *focused* development of an assurance case.

However, they also warn of the risk of confirmation bias when project teams are incentvisied to seek out evidence that confirms a goal. Although this may help build a strong argument, it can also prevent teams from addressing competing evidence or investigating avenues that undermine their primary goal.

This is an active area of research, which we will not expand on here, but address in our [open documentation](https://github.io/AssurancePlatform). 
```

