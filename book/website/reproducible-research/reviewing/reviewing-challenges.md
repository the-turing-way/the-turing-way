(rr-reviewing-challenges)=
# When Code Review Goes Wrong

As is discussed in the {ref}`Motivation<rr-reviewing-motivation>` section, code reviews are important and beneficial for the overall health of a project.
Nonetheless individual reviews can be challenging and are often a source of tension.
Ensuring code review is effective and enriching for those involved relies on the author and reviewers approaching it in a certain way, and avoiding some of the many pitfalls involved.

When author and reviewers are working together and in collaboration, the exercise of reviewing can be both enjoyable and beneficial.
When reviews become antagonistic they can cause immense harm.

```{figure} ../../figures/first-pull-request.*
---
width: 630px
name: code-review-good-and-bad
alt: Two panes, both show two rowers in a boat. In the top pane both row in the same direction and the boat makes good progress. In the bottom pane they row in opposite directions and the boat travels in circles. This represents how the review process is best when authors and reviewers work with each other rather than against each other.
---
PLACEHOLDER IMAGE. Code review flow and frustration. _The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

In this section we discuss some of the common pitfalls and reasons why code review can be problematic.

## Power struggles

The effectiveness of code review is highly susceptible to power imbalances between the participants.
If the author is more senior than a reviewer, or the other way around, it can lead to reviews that are ineffective and disempowering.

Power imbalance during code review doesn't necessarily have to be a product of seniority in a project.
It can also be the result of different roles and permissions.
For example, if only the reviewer has the ability to merge a pull request, this can lead to the situation where the reviewer has total power over whether a pull request is accepted or not.
This is a common situation.

Situations in which the reviewer has seniority can lead to a form of "development by proxy", where the reviewer is essentially making their own changes to a piece of code or document through the medium of GitHub comments; the author acts simply as a scribe.
This is disempowering for the author and also an ineffective use of time.

If a reviewer is forcing a complete restructure or rewrite of a piece of code in this way, preferable approaches are to either reject the PR and discuss the changes outside of a review, or to accept the changes but also with an associated issue created to specify the other changes required.

Situations in which the author has seniority can lead to a situation where all review comments are dismissed out of hand without explanation or even just ignored completely.
This is disempowering for the reviewer and leads to disenchantment with the process.

Power imbalances that can lead to these situations should be avoided as far as possible by aligning processes and selecting reviewers in order to avoid this.
However in many projects, especially open source projects, this may not be possible: core developers always have the final say on what gets merged.

Where such power imbalances cannot be avoided it falls to the more senior contributor to act appropriately.
For example, it can be helpful for them to use supportive rather than accusative language, to be more forgiving of others' language, and to take special care to encourage consensus rather than dictating an outcome.

## The infinite wait

Reviewing pull requests is time-consuming and can be seen as less productive than generating new content.
In open source projects where there is no pre-existing relationship between the submitter of a pull request and the core team reviewing it, it can be easy for pull requests to get ignored.

This is especially true for pull requests that are controversial, or which are of high quality but making changes that the project does not see as a priority internally.

A common outcome is that a pull request will be left in the queue for months or even years without being addressed.
This is almost guaranteed to alienated potential members of the community who might otherwise make more contributions.

It's crucial that reviews are tackled in a timely manner.
For an open source project, it is the responsibility of the project maintainers, and a sign of good stewardship, if pull requests are reviewed in good time.

Allowing stale pull requests to build up can cause drag on a project.

If a project isn't ready to accept a pull request or doesn't have the capacity to review it, it is beneficial to make this clear, either by rejecting the pull request, or by engaging with the author to explain the situation.

## The infinite review

If a reviewer doesn't like a piece of code, it's not unusual for them to simply leave a review incomplete, rather than tackle the thorny issues it raises.
This may be especially the case if a reviewer is having difficulty articulating what they dislike about a proposed change.

Leaving pull requests half reviewed, from the side of the author or reviewer, can feel disrespectful to other parties who have worked on it.

If there is any uncertainty about the benefits or purpose of a particular change, it is better to make this clear through a comment, emphasising that you're looking to better understand.

If a change is ultimately not going to be merged, it is more respectful to reject explicitly than to leave the review incomplete.
When rejecting a change it is essential that the reason is explained for the benefit of the author.

Remember that not everything has to be resolved in a single pull request.
If it looks like it's going to be hard to come to a decision on something, create a new issue to deal with it, rather than allow it to block the code merge.

## Bad contributions are better than no contributions

As a reviewer it may be necessary to accept the code in a form that you're not happy with.
In this case, create an issue to fix parts of it that may be problematic in a separate issue.
It can sometimes be quicker to fix an issue yourself rather than work through someone else to make the change.

This is especially true early on in a project when a community is still being built up around it.
Contributors who make poor submissions now, with help and encouragement, may turn into the driving force of a project in the future.
Reviews should always be encouraging and especially in the early stages, it can be better to err on the side of accepting rather than alienate potential collaborators.

## The weight of responsibility

When performing a review it can be helpful to have an appreciation of who is ultimately responsible for the changes.
Reviewers who feel overly responsible are liable to spend too much time and be too critical in their reviews.

The author of the code is ultimately responsible for its quality, not the reviewer.
This is the defacto position because in the majority of projects, if an error is found to trace back to a particular commit later in a project's life, it is invariably the author of the commit who will be first in line to fix it.

This shouldn't be a question of blame, despite the fact `git blame` is your go-to command for finding out who write a piece of code.
In practice, the person who wrote a piece of code tends to be the person with the most context, and who can most efficiently find a fix.

## Impulsive reactions

Some review systems will send an email or alert every time a new comment is added to a review.
It can be tempting, as either an author or reviewer, to respond to these comments immediately.
This urge can be especially strong if you disagree with a comment.

In practice the comment is likely to be part of a larger and more considered response that spans the entire set of changes in a pull request.

Whether as a reviewer responding to changes, or an author responding review feedback, it can be helpful to wait for the entire set of comments to arrive before deciding on a response.
Replying immediately not only starves you of the full context, it may also interrupt the flow of the reviewer, who may also be receiving immediate notifications following a reply.

Resist the urge to reply to all comments immediately.
Wait for the full response and then think carefully about how best to respond.

The GitHub reviewing tools encourage this approach by allowing you to build up all of your comments in your review before submitting them in a single batch.
This has many advantages:

1. The recipient receives a single notification for the entire review, rather than many smaller notifications, which can be disruptive.
2. The relevance of changes earlier in a pull request may not become clear until later in a pull request.
   Batching up your responses gives you the opportunity to amend them in retrospect in case you discover that a comment doesn't apply after all.
3. The approach encourages you to think holistically about a change, rather than pedantically criticising every small and insignificant detail.
4. It discourages overly-hasty and impulsive reactions.


