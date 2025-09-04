(ch-gardening)=
# GitHub Gardening

Managing a open source community and maintaining its infrastructure, like [code repositories](#rr-vcs) and {term}`issue trackers <Issue Tracking>`, takes time an effort.
In the free and open source community this work is often called maintenance.
This work is difficult and requires strong technical skills as well as excellent interpersonal skills.
It can often seem that this work goes unappreciated, but it is critically important for the health of an open source project.

In _The Turing Way_ we call this work gardening, because that is an analogy for how this kind of activity is about tending to the community, keeping it healthy and helping it grow.
This page has [instructions](#ch-gardening-checklists) and guidelines for our gardeners to help them work.

## Guiding principles

### Maintain quality

Gardening work plays an important role in maintaining the quality of a project.
[Continuous integration processes](#rr-ci) and [code review](#rr-reviewing) help to ensure the quality of contributions as they are merged.
However, there are many other aspects of the community where gardeners can help.

You should focus on keeping the quality of issues, discussions and pull requests high.
You shouldn't be afraid to close items or ask for changes.
Gardening work makes items higher quality, which improves the chances they will be seen, have engagement and get completed.

### Be a mentor

Gardeners can mentor community members, teaching them new skills and encouraging best practice.
You should look to share your knowledge and teach others.
However, don't feel you have to personally fix problems or that you have to take on work when you ask for changes.

### Use your knowledge

Contributing to a project as a new community member can be intimidating.
There is a lot of institutional knowledge that is difficult to learn or share.
Gardeners should use their experience to help contributors, for example, recommending people who would be interested in a pull request or pointing to style conventions in the [](#ch).

### Be a human

In the process of gardening, you may have to take actions that might be difficult for others.
For example, closing an issue as "will not fix" or requesting large changes to a contribution.
You may also find taking this kind of action difficult yourself.

You should remember to be kind to other.
If you have to say anything that may be difficult to accept or understand, take some time to explain.
Remember to be welcoming, a project can only survive with contributors, and everyone starts as a new contributors.

## GitHub item usage

To help keep items findable, we use GitHub features for different purposes.

(gh-gardening-items-issues)=
### Issues

An issue is a task, for example a bug to fix or a feature to add.
A good issue should,

- be of a reasonable size for one person
- or, to coordinate large pieces of work, be a list of sub-issues
- have a clear "definition of done"

Examples of bad issues could be,

- Too much work for one person or a single pull request
- No clear work to be done, a question or a discussion

(gh-gardening-items-discussions)=
### Discussions

Discussions are used for conversations which are not necessarily tied to a specific task.
They are often broader than issues.

Examples of good discussions are,

- Questions about the project
- Proposals and new ideas
- Polling the community
- Discussing the options before opening an issue

### Pull requests

Pull requests are proposals to merge one branch into another.

We encourage people to open pull requests early.
This helps make their work visible and get early feedback.
Pull requests should be marked as drafts while they are work in progress.
They should be marked as ready for review when the author feels it is ready to be merged.

## Gardening stages

These stages correlate roughly with how _mature_ an item is.
They are not law but they are intended to help us understand what stage an item is at and what we should be aiming to do to help contributors at each stage.

### Sowing

Sowing is for new items.
The sowing tasks are initial actions to ensure the best chance of success.

### Fertilising

Fertilising is for in progress items.
These tasks are to help push them over the line, so that contributions can be made.

### Pruning

Pruning is for items which have gone {term}`stale <Stale>`.
This step keeps the repository clean, closing inactive or completed work while leaving the option for it to be continued in the future.

(ch-gardening-checklists)=
## Checklists

### Issues

#### Sowing

- [] Ensure it is in the correct repository?
    - If not, move to a more appropriate repository
- [] Ensure it is [an issue](#gh-gardening-items-issues)?
    - Move to [a discussion](#gh-gardening-items-discussions) if appropriate
- [ ] Ensure there is a definition of done
    - Ask the author to find one if this isn't clear
    - Move to a discussion if there needs to be a discussion to find one
    - Close as unfixable if one cannot be found
- [ ] Assign appropriate labels
- [ ] Tag (or assign) community members who may be interested or who can help

#### Fertilising

- [ ] Ensure issue is in action
    - Check who is working on the issue and assign
- [ ] Understand progress and challenges
    - Check what support contributors need to fix the issue
- [ ] Support assignees
    - Tag community members who can help
    - Invite to post a Slack message
    - Invite to collaboration cafe

#### Pruning

- [ ] Handle {term}`stale <Stale>` issues
    - If there is no stale label, mark as stale and leave a message
    - If there is a stale label and 30 days have passed, close the issue as stale

### PRs

#### Sowing

- [ ] Is this a PR
- [ ] Assign appropriate labels
- [ ] Convert to "Draft" or "Ready for review" as appropriate
- [ ] Assign reviewers
    Or tag people who may be interested

#### Fertilising

- Getting the PR "over the line"
    - [ ] Reach out to the contributor.
        - How close are they to finished?
        - What support do they need to finish?
        - Do they have the time to complete this PR?
    - [ ] Suggest(?) actions
        - Invite to post a Slack message
        - Invite to collaboration cafe
        - Link with another community member
        - Arrange for someone to adopt the PR

#### Pruning

- Is there a realistic chance this PR will be merged?
  Are the contributors still engaged?
  Is the branch still well in sync with main?
  - [ ] Reach out to draw attention to these issues
  - [ ] Close the PR

:::{warning}
Closing a PR may delete the branch which could result in loss of the commits on that branch.
:::
