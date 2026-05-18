(ch-gardening)=
# GitHub Gardening

Managing a open source community and maintaining its infrastructure, like [code repositories](#rr-vcs) and {term}`issue trackers <Issue Tracking>`, takes time an effort.
In the free and open source community this work is often called maintenance.
This work is difficult and requires strong technical skills as well as excellent interpersonal skills.
It can often seem that this work goes unappreciated, but it is critically important for the health of an open source project.

In _The Turing Way_ we call this work gardening, because that is an analogy for how this kind of activity is about tending to the community, keeping it healthy and helping it grow.
This page has [instructions](#ch-gardening-checklists) and guidelines for our gardeners to help them work.

(ch-gardening-principles)=
## Guiding principles

### Maintain quality

Gardening work plays an important role in maintaining the quality of a project.
[Continuous integration processes](#rr-ci) and [code review](#rr-reviewing) help to ensure the quality of contributions as they are merged.
However, there are many other aspects of the community where gardeners can help.

Gardeners should focus on keeping the quality of issues, discussions and pull requests high.
Gardeners shouldn't be afraid to close items or ask for changes.
Gardening work makes items higher quality, which improves the chances they will be seen, have engagement and get completed.

### Be a mentor

Gardeners can mentor community members, teaching them new skills and encouraging best practice.
Gardeners should look to share their knowledge and teach others.
However, gardeners shouldn't feel they have to personally fix problems or take on work when they ask for changes.

### Use your knowledge

Contributing to a project as a new community member can be intimidating.
There is a lot of institutional knowledge that is difficult to learn and share.
Gardeners should use their experience to help contributors.
For example, recommending people who would be interested in a pull request or pointing to style conventions in the [](#ch).

(ch-gardening-principles-human)=
### Be a human

Gardeners must remember to be kind to others.
If gardeners need to say anything that may be difficult, they should take some time to explain.
They should remember to be welcoming; a project can only survive with contributors, and everyone starts as a new contributors.
Gardeners may also find taking this kind of action difficult, and so, we have collected some [example responses fragments](#ch-gardening-example-responses) to help build clear, firm and polite comments.

## GitHub item usage

To help keep items findable, we use GitHub features for different purposes.

(ch-gardening-items-issues)=
### Issues

An issue is a task, for example a bug to fix or a feature to add.
A good issue should,

- be of a reasonable size for one person
- or, to coordinate large pieces of work, be a list of sub-issues
- have a clear "definition of done"

Examples of bad issues could be,

- Too much work for one person or a single pull request
- No clear work to be done, a question or a discussion

(ch-gardening-items-pull-requests)=
### Pull requests

Pull requests are proposals to merge one branch into another.

We encourage people to open pull requests early.
This helps make their work visible and get early feedback.
Pull requests should be marked as drafts while they are work in progress.
They should be marked as ready for review when the author feels it is ready to be merged.

(ch-gardening-items-discussions)=
### Discussions

Discussions are used for conversations which are not necessarily tied to a specific task.
They are often broader than issues.

Examples of good discussions are,

- Questions about the project
- Proposals and new ideas
- Polling the community
- Discussing the options before opening an issue

## Gardening stages

These stages correlate roughly with how _mature_ an item is.
They are not law but they are intended to help us understand what stage an item is at and what we should be aiming to do to help contributors at each stage.

### Sowing

Sowing ensures new items have the best chance of success.
It makes sure items are visible and well defined.

### Fertilising

Fertilising helps push in-progress items over the line, so that contributions can be finalised.
We help keep contributors engaged and support them to overcome challenges.

### Pruning

Pruning manages the end of life for items which have gone {term}`stale <Stale>`.
This step keeps the repository clean, closing inactive or completed work while leaving the option for it to be continued in the future.

(ch-gardening-checklists)=
## Checklists

### Issues

#### Sowing

- [ ] Ensure it is in the correct repository
    - If not, move to a more appropriate repository
- [ ] Ensure it is [an issue](#ch-gardening-items-issues)
    - Move to [a discussion](#ch-gardening-items-discussions) if appropriate
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

### Pull requests

#### Sowing

- [ ] Ensure it has the [correct status](#ch-gardening-items-pull-requests)
    - Convert to "Draft" if it is still work in progress
    - Convert to "Ready for review" if it is ready for final reviews
- [ ] Assign appropriate labels
- [ ] Assign or tag potential reviewers

#### Fertilising

- [ ] Check progress with the authors
    - Ask how close are they to finished
    - Understand what support they need
- [ ] Support assignees
    - Tag community members who can help
    - Invite to post a Slack message
    - Invite to collaboration cafe
    - Arrange for someone to adopt the PR if the author no longer has time

#### Pruning

- [ ] Merge if it is ready, passes tests and has accepted reviews
- [ ] Close if the pull request is an example of [low quality or low engagement](#ch-contributing-low-effort)
- [ ] Close if there is no realistic chance of a merge.
  For example if the authors are not engaged or the branch is very far behind main
- [ ] If the PR was closed and it was from a branch on the main repo, make sure the branch is deleted, too.
  It is easier to deal with stale branches at the time the last action was made on them rather than in a future triage session.
:::{warning}
Closing a PR from a branch on _The Turing Way_'s repository will delete that branch and could result in loss of the commits.
Closing a PR will not delete a branch on a fork.
:::

### Discussions

#### Sowing

- [ ] Ensure it is [a discussion](#ch-gardening-items-discussions)
- [ ] Ensure there is a clear focus
    - If it is a question, make sure it is well defined
    - If it is a discussion, suggestion, poll or similar, make sure the topic is clear
- [ ] Tag community members who can help

#### Fertilising

- [ ] Check progress
    - Ask what hasn't been resolved
- [ ] Support discussions
    - Tag community members who can help
    - Suggest advertising in Slack
    - Invite to collaboration cafe

#### Pruning

- [ ] Close discussions when they have concluded
    - If the discussion is a Q&A, mark an accepted answer
- [ ] Close as outdated if it is {term}`stale <Stale>`

(ch-gardening-example-responses)=
## Writing good comments as a gardener

In their work, gardeners may have to take actions that might be difficult for others to accept or understand.
For example, closing an issue as "will not fix" or requesting large changes to a pull request.
It is therefore important to be [clear and kind when giving feedback](#ch-gardening-principles-human) to contributors.

Here, we have a basic outline to a comment, with optional, modular fragments that you can include or exclude as appropriate.
You _do not_ have to use this template, but we encourage you to use it if it is helpful.
We also recommend that you remix the suggestions here in your own voice as it helps to show our personalities and prevent gardeners appearing robotic.

When first engaging with someone, it is good to start with a salutation,

- Hi, thanks for opening this PR/issue.
- Hello, we are exciting you are contributing to The Turing Way!

Explain any issues clearly, and without blame or accusation,

- Your changes do not match the PR or issue description
- Your changes deviate strongly from our [Style Guide](#ch-style).
- Your changes are only making superficial additions or changes.
  Our contribution guidelines mention that all contributions should improve the contents of the book.
- It looks like a significant portion of your changes are written using generative AI without taking care to review its output.
- You have added/changed a significant amount of content in the book without any discussion or consultation of community members.
  Our book is collaboratively written and we encourage you to reach out to the community with such significant changes before adding it to the book.

Describe any action you are taking,

- I will close this issue as a duplicate.
- I will close this PR as I think it is unlikely it will be ready to merge in the foreseeable future.
- I will close this PR as what you are proposing won't improve the book.

And, in cases where we can reach a good outcome, leave some guidance and encouragement,

- Please re-request a review from me, or tag me in a comment, once you have made changes.
- It would be great if you could join a [collaboration café](#ch-community-calls-collabcafe) to talk about this idea.
