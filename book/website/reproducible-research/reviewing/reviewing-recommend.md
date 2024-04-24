(rr-reviewing-recommendation)=
# Recommendations and Best Practices

## Who Reviews?

Within small-scale projects where the developers all typically already know each other,
common practice is for the coder to tag someone in the group as the reviewer.

In contrast, large-scale development projects will likely have existing, concrete rules for
how reviewers are allocated to individual pull requests.
These rules serve to balance the group workload and to maximise the various benefits of the process to the project and its participants.
The very largest projects may even have dedicated staff - or teams of staff - to act as reviewers.
Typically, code reviews can only be performed by an authorised subset of contributors within larger projects.

If you are a contributor to a more loosely managed or distributed project, a good rule of thumb is to aim to perform reviews in similar quantities to the material you generate for review.

For projects where multiple rounds of review on similar material are likely and long development cycles are anticipated, a degree of strategic thinking on who completes reviews is sensible.
A single reviewer is likely to be able to make comments on code they have reviewed before much more efficiently.
However, letting reviewer-coder pairs like this persist is generally a bad idea, as it can lead to the same kinds of groupthink that the review process is designed to avoid in the first place.

Open source projects often also have their own dynamics.
Contributions may be split between a set of core maintainers, and a larger set of more dispersed contributors, some of whom may have very limited interactions with a project.
In open source projects it is typically the case that anyone can review a pull request, just as anyone can create one.
Those who have merge privileges, often limited to core maintainers, inevitably have the final say over what gets added to the code, and so also have the largest role when it comes to code review.

(rr-reviewing-recommendation-be-nice)=
## Be Nice!

As with all open source and collaborative enterprises, good internet etiquette makes the whole process go more smoothly.
Perhaps most importantly, always assume good faith on both sides of the review interaction, and always be constructive.
These principles are true for the review process beyond almost any other project aspect, since it necessarily involves criticism, potentially between two complete strangers.

Although the review process is asymmetrical, the challenges go in both directions: reviewees may feel their ideas are being misunderstood or criticised unjustly; reviewer's may feel their input is being ignored.
It's important that all parties in the review process avoid being overly pendantic or territorial.

For an open source project hoping to grow a community it's also important to understand that it can be better to accept poor code contributions than to alienate potential collaborators.

All of this can be very challenging in practice.
We discuss this further in the next section.

## Keep It Collaborative

Unlike traditional, "academic-style" peer review, most code review systems have a number of advantages: they're rarely anonymous, they're public-facing, and without the middleman of an editor, contact between reviewer and reviewee can be direct and rapid.
This means code review is typically a fast, flexible, and interactive process.
Good peer review will be fully collaborative, where once a potential query has been flagged by a reviewer, the two involved parties can work forward together to find a solution.
It's also not atypical for third parties to chime in during the discussion threads that can grow under more gnarly review comments, either voluntarily or by request.
This is all to the good.

## Avoid Being Subjective

Code reviews should strive to be as objective as possible.
Of course, subjective coding preferences may come up in any project.
However, such preferences wherever possible should be decided at the project level beforehand.
Thus, one can avoid the situation where an opinion might be passed off as fact.
Instead suggestions can be supported by pointing to documented preferences that have been set up in advance.
If you do come across undocumented preferences, discuss them with the team again and agree if you would like to add the preference to the checklist of your code review process.

## Specify Crucial Versus Optional Changes

You might want to differentiate between changes that are crucial and changes that are nice to have.
For example, comments that begin "You might..." could be used to express suggestions the reviewers want the coder to consider but are not essential.
These can be particularly useful to guide inexperienced coders to write better code while not being too picky.
The coder can then decide to ignore these non-crucial comments if they don't agree.
Reviewers could use comments that begin "You must..." to specify those that are not optional.

## Review Code in Small Chunks

Reviewing code in small chunks incrementally as the project is developing can help make the code review process a lot more efficient.
It is a lot more difficult to review an enormous codebase once significant mistakes have been introduced.
If mistakes can be spotted early in the process, they are much easier to fix and this will help with the overall code development process.

Here is some general advice on how to integrate code reviews into our working process:

- Take the time, read carefully.
  Review everything, nothing is too short or simple.
- Try to have something else to do, and spread the load throughout your
working day.
  Don't review for more than an hour at a time, after that the success rate drops quite quickly.
- Don't review more than 400 lines of code (LOC) at a time, less than 200 LOC is better.
  Don't review more than 500 LOC/hour.

## Be Okay With Taking the Discussion Offline

Sometimes, with more complex code reviews, online communication can lead to unproductive conversations.
Where possible setting up an in-person meeting can help to resolve some of the trickier issues in a more collaborative and friendly manner.
As an alternative, the development/research team can set regular meetings for doing code reviews with all of the team members.
For example, see the approach taken by a professor organizing [lab meetings for code](http://web.archive.org/web/20210512053038/http://fperez.org/py4science/code_reviews.html).
For many open source projects accepting pull requests from ephemeral contributors across the world neither of these appraoches may be realistic.
In this case being able to tackle difficult situations through the medium of asynchronous review becomes a necessity.
