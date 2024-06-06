(er-ethical-argument-patterns)=
# Ethical Argument Patterns

So far we have looked at assurance cases—individual arguments that justify how some goal has been assured on the basis of a set of claims and associated evidence.
However, goals—such as safety, accountability, fairness, and explainability—are widely seen as important in the context of data-driven technologies.
As such, we can expect that many project teams will need to assure how such goals have been realised over the lifecycle of their project.
This is where *argument patterns* come in.

Argument patterns are templates that provide reusabke solutions to common assurance needs.
For instance, if the same four strategies are used when arguing for the fairness of a predictive algorithm deployed in the context of healthcare, along with a similar set of related property claims, then they can be built into an argument pattern to save time when developing new assurance cases.

```{note} Example of a Software Pattern
:class: dropdown
If this concept of an argument pattern seems familiar to software engineers or developers, it's for a good reason.
The concept is closely connected to the idea of *software patterns*, also known as design patterns, which are also reusable solutions to common problems that arise during the design and development of software systems.
Like argument patterns, they provide a proven approach to addressing specific challenges while also helping to improve the quality, maintainability, and efficiency of software applications.

There are many common software patterns.
Let's consider a widely used on: the factory pattern.

First, imagine you own a cafe that makes and sells different kinds of baked good: cakes, cookies, and muffins.
Instead of having to guess how many goods you need to produce at the start of the day, and to minismise waste, you decide to purchase a robot chef.
Now, each time an order comes in you simply say, "I need a cake," and a cake is made automatically.
If you say, "I need a cookie," a cookie is made automatically, and so on.

The factory pattern in software works in a similar way.
Instead of creating objects (like cakes, cookies, and muffins) directly in different parts of your program, you have a special "factory" class that handles creating these objects for you.
This makes it easier to manage and change the way objects are created without having to modify the code everywhere an object is needed.

Now, exactly how this pattern is *implemented* will depend on the specific context of your software project, as well as details such as the programming language you are using.
However, regardless of whether you are using Python, Javascript, Go, or Rust, the general pattern remains the same at some level of abstraction.
```

## Creating Argument Patterns

There are several ways that argument patterns can be produced.
Let's consider two:

1. Top-down or prescriptive approaches
2. Bottom-up or generalised approaches

In the case of the first, a pattern could be produced by an expert or group of experts (e.g. a commitee).
Assuming, these experts have sufficient experience with either the goal, the context of use, or the range of solutions (e.g. those that have been empirically validated and proven), this top-down approach can be highly effective.
The resulting pattern will distill a lot of wisdom, and help to form consensus around the major risks and opportunities associated with the relevant goal (e.g. assuring safety of autonomous vehicles).
In such cases, we can also assume that the experts, where recognised as such by a relevant community, also serve as representatives of the community of practice in which they are located.

However, there are also drawbacks to this approach.
For instance, how do we judge whether someone is sufficiently expert?
How should we judge expertise when dealing with novel challenges (e.g. assurance of robustness for large language models or frontier AI systems)?
How do we ensure the experts views are sufficiently representative of the diverse needs and challenges faced by a group, community, or society?

This is where we can turn the second, complementary, approach. 

Bottom-up approaches take a set of assurance cases and solutions and seek to identify patterns that already exist.
In other words, they generalise based on the similarities that exist within a community of practice.

For instance, if several assurance cases, which focus on a goal such as security, all contain a strategy and related claims that deal with access rights for users, then this suggests its a common problem for which the community have already developed a sufficient solution (or set of solutions).

This addresses some of the drawbacks of the first approach.
For instance, it provides a more distributed approach to expertise—a sort of wisdom of the crowds.
And, in principle, this distributed approach can enable a greater diversity and representation of techniques or solutions.

However, it is also not without its own drawbacks:

1. How do we differentiate high-quality from low-quality cases to ensure patterns are only developed based on the best standards?
2. How can we promote open knowledge sharing of assurance cases to enable greater diversity of examples, which can then be used to generalise patterns from?

In short, both approaches are needed and should, ideally, mutually complement and support one another.
In other words, we look to converge somewhere in the middle between the more narrow "expert-led" approach and the broader "community-grounded" approach.
