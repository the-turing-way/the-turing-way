(cm-pr-code)=

# Guidance on Code Review

Code review can therefore help increase the accuracy of results, and furthermore improve usability and maintainability of code, as well as providing a great opportunity to learn.

The importance of data structure selection, accurate abstraction, logical naming and control flow.
The most important questions are: does it work? Is it easy to maintain? Will we be able to understand it 2 years from now?
Approve when the code runs/is good - not perfect. 

Petre and Wilson 2014 (https://arxiv.org/abs/1407.5648)
… scientists appear to have “less concern for maintainability and readability” and that the code was “not written for others to use”. Some also pointed out naive lack of complexity or abstraction, redundancy in the code, inconsistencies in or ignorance of standards in formatting, and unhelpful naming.
…we believe the following should be priorities when scientists start doing code review:
1. Have a goal, a benefit in mind.
2. Start with a conversation: articulate your goals and expectations, build rapport.
3. Choose the right pieces of code for the first re-views. A good starting point is 3–4 pages long, fairly self-contained, and under active development, so that small patches are coming in regularly.
4. Make your code available in a repository with a typical data set and an overview of how the code works.
5. Set up a schedule and commit a little time on a regular basis.
6. Understand that it’s the code that’s being reviewed (not you). Tailor your comments to others on the same terms
7. Make the process reciprocal: be prepared to make as well as receive comments.

Willingness to participate in code review also requires researchers to be okay with others looking critically at their code - which can be daunting. Normalising showing code to peers, such as comparing approaches to short coding challenges, can be a good step towards feeling comfortable with code review. Including inexperienced coders as reviewers, as well as reviewees, can also help code review become standard practice within a group - any reviewer at any level can provide valuable feedback and can learn from conducting a review. To find out more about how to do a review of someone else’s code, this [blog post from Ariel Rokem](https://uwescience.github.io/neuroinformatics/2017/10/08/code-review.html) is a good first introduction. 

 The [online sustainability evaluation](https://www.software.ac.uk/resources/online-sustainability-evaluation) or [Research Software Health Check](https://www.software.ac.uk/programmes-and-events/research-software-healthcheck) provided by the Software Sustainability Institute might be further helpful resources particularly focusing on issues that affect the sustainability of your software.

Bekkers 2020 (https://doi.org/10.31219/osf.io/7ug4w)
A paper that does not provide access to the data analyzed and the code used to produce the results in the paper is not worth your time. If the paper does not provide a link to the data and the analysis script, ask the editor to ask the authors to provide the data and the code. Do not hesitate to ask this.

[How to do a code review](https://google.github.io/eng-practices/review/reviewer/)

# Resources

## Journal, conference and archive guidelines
*	[rOpenSci Software Peer Review](https://ropensci.org/software-review/) contains the guidelines used by rOpenSci before they get added to the rOpenSci suite of packages.
* [Journal of Open Source Software review criteria](https://joss.readthedocs.io/en/latest/review_criteria.html) and [checklist](https://joss.readthedocs.io/en/latest/review_checklist.html)
* [Journal of Open Research Software review form](https://openresearchsoftware.metajnl.com/about/editorialpolicies/)
* [AGILE reproducible guidelines 2020](https://doi.org/10.17605/OSF.IO/CB7Z8)

## Teaching Code Review
*	Teaching Code Review to University Students (https://www.eduflow.com/blog/teaching-code-review-to-university-students)
* Tips and Tricks for Reproducing and Reviewing by Anna Krystalli ([slides 24-37 on reviewing](https://annakrystalli.me/n8cir-reprohacks/slides/#24)) (see also ReproHack author feedback form)

## Sharing Code Review Experiences
* [’ve code reviewed over 750 pull requests at Amazon. Here’s my exact thought process](https://curtiseinsmann.medium.com/ive-code-reviewed-over-750-pull-requests-at-amazon-here-s-my-exact-thought-process-cec7c942a3a4) - by Curtis Einsmann
* [Identifying and overcoming obstacles to adopting code review](https://www.software.ac.uk/blog/2022-08-17-identifying-and-overcoming-obstacles-adopting-code-review)
