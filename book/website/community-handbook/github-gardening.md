# GitHub Gardening

Managing a open source community and maintaining its infrastructure, like [code repositories](#rr-vcs) and {term}`issue trackers <Issue Tracking>`, takes time an effort.
In the free and open source community this work is often called maintenance.
This work is difficult and requires strong technical skills as well as excellent interpersonal skills.
It can often seem that this work goes unappreciated, but it is critically important for the health of an open source project.

In _The Turing Way_ we call this work gardening, because that is an analogy for how this kind of activity is about tending to the community, keeping it healthy and helping it grow.
This page has instructions and guidelines for our gardeners to help them work.

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

## GitHub item purpose

### Issues

- An issue is a task
    - Of a reasonable size for one person (or, a list of sub-issues)
    - Which has a clear "definition of done"

### Discussions

- Items for discussion (not necessarily tied to action or implementation)
- General questions
- Ideas

### PRs

- A proposal to merge one branch into another
    - Marked as a draft if it is work in progress
    - Marked as ready to review if you feel it is ready to be merged

## Gardening stages

These stages correlate roughly with how _mature_ an item is.
It isn't a law, but is intended to help us understand what stage an item is at and what we should be aiming to do to help contributors at each stage.

## Sowing

Initial actions to ensure an item has the best chance of success

## Fertilising

Working on active items to help push them over the line

## Pruning

Closing items which have gone stale

## Glossary

Stale issue
: A stale issue is


## Checklists

### Issues

Always leave a welcoming, friendly message to explain what you are doing and why

#### Sowing

- [ ] Is this an issue
    - [ ] Move to a discussion if this is a discussion
    - [ ] If there is no definition of done
        - Ask if we can find one
        - Move to a discussion(?)
        - Close as unfixable
- [ ] Is this issue in the correct repository
- [ ] Assign appropriate labels
- [ ] Tag (or assign) relevant community members

#### Fertilising

- Ensuring issue is "in action"
    - [ ] Post in the issue
        - Is anyone working on the issue, has anyone been assigned? 
        - What support does the contributer need to fix the issue?
    - [ ] Suggest actions
        - Invite to post a Slack message
        - Invite to collaboration cafe
        - Link with another community member

#### Pruning

- If the issue is stale (we should define stale) - I would hope we could automate at least some of this section
    - If there is no stale label
        - [ ] Mark as stale and leave a message
    - If there is a stale label and x days have passed
        - [ ] Close the issue as stale

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
