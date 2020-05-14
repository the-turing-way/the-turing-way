## Best practice

<a name="Be_nice"></a>
### Be nice!

As with all open-source and collaborative enterprises, good internet etiquette makes the whole process go more smoothly. Perhaps most importantly, always assume good faith on both sides of the review interaction, and always be constructive. These principles are true for the review process beyond almost any other project aspect, since it necessarily involves criticism, potentially between two complete strangers. If you're the coder, don't waste your reviewer's time. If you're the reviewer, listen to what the coder is telling you in reply, and work collaboratively with them to make the code better.

### Avoid being subjective
Code reviews should strive to be as objective as possible. Of course, subjective coding preferences may come up in any project. However, such preferences wherever possible should be decided at the project level beforehand. Thus, one can avoid the situation where an opinion might be passed of as fact. Instead suggestions can be supported by pointing to documented preferences that have been set up in advance. If you do come across undocumented preferences, discuss them with the team again and agree if you would like to add the preference to the checklist of your code review process. 

### Specify crucial versus optional changes
You might want to differentiate between changes that are crucial and changes that are nice to have. For example, comments that begin "You might..." could be used to express suggestions the reviewers want the coder to consider but are not essential. These can be particularly useful to guide inexperienced coders to write better code while not being too nitpicky. The coder can then decide to ignore these non-crucial comments if they don't agree. Reviewers could use comments that begin "You must..." to specify those that are not optional.


<a name="Keep_it_collaborative"></a>
### Keep it collaborative
Unlike traditional, "academic-style" peer review, most code review systems have a number of advantages: they're rarely anonymous, they're public-facing, and without the middleman of an editor, contact between reviewer and review-ee can be direct and rapid. This means code review is typically a fast, flexible, and interactive process. Good peer review will be fully collaborative, where once a potential query has been flagged by a reviewer, the two involved parties can work forward together to find a solution. It's also not atypical for third parties to chime in during the discussion threads that can grow under more gnarly review comments, either voluntarily or by request. This is all to the good.

### Review code in small chunks and quickly
Reviewing code in small chunks incrementally as the project is developing can help make the code review process a lot more efficient. It is a lot more difficult to review an enormous codebase once significant mistakes have been introduced. If mistakes can be spotted early in the process, they are much easier to fix and this will help with the overall code development process.

### Be okay with taking the discussion offline
Sometimes, with more complex code reviews, online communication can lead to unproductive conversations. Setting up an in-person meeting can help to resolve some of the trickier issues in a more collaborative and friendly manner.

<a name="Who_reviews"></a>
### Who reviews?

Individual large-scale development projects will likely have existing, concrete rules for how reviewers are allocated to individual pull requests. These rules serve to balance the group workload and to maximise the various benefits of the process to the project and its participants. The very largest projects may even have dedicated staff - or teams of staff - to act as reviewers. In contrast, within small-scale projects where the developers all typically already know each other, typical practice is for the coder to tag someone in the group who they feel will have enough knowledge of this part of the code to do a good job in a reasonable amount of time. In practice, the point of transition between the structured and unstructured models will become very obvious within a growing project - typically when certain members of the core personnel start to complain about the uneven workload for reviewing they are under!

For projects where multiple rounds of review on similar material are likely and long development cycles are anticipated, a degree of strategic thinking on who completes reviews is sensible. A single reviewer is likely to be able to make comments on code they have reviewed before much more efficiently. However, letting reviewer-coder pairs like this ossify is generally a bad idea, as it can lead to the same kinds of groupthink that the review process is designed to avoid in the first place. Individual projects will tend to find this balance for themselves.

Typically, code reviews can only be performed by an authorised subset of contributors within larger projects.
