(cm-pr-code)=

# Guidance on Code Review

Code review can help increase the accuracy of results, improve usability and maintainability of code, and is a great opportunity to learn.

The most important questions during code review are: 
- Are all the files available? If not, ask the editor to request the data/code from the authors.
- Does it run? 
- Is it easy to understand? 
- If it is not just a script underlying a publication but part of software infrastructe: how easy is it to maintain? 

[Code does not have to be perfect](https://google.github.io/eng-practices/review/reviewer/standard.html) - it has to work, be accompanied with sufficient documentation and be maintainable if this is needed.

## [Code review in ReproHack style](https://annakrystalli.me/n8cir-reprohacks/slides/#24)

1. Access
- How easy is it to access the materials? Can you access all the materials?
  - Is the data stored in a seperate directory or data repository? Is there a persistent identifier associated with the data/code?

2. Installation
- Are you able to install everything, did you run into any problems and how did you solve these?

3. Documentation
Does the documentation contain information on:
- how to install necessary software and dependencies?
- how to use materials to reproduce the paper?
- how to cite the materials, ideally in a form that can be copy and pasted?
Provide suggestions on how to improve the documentation of the code if needed.

4. Reproduction
- Were you able to fully reproduce the paper? 
- How automated was the process of reproducing the paper?
- How easy was it to link analysis code to the plots it generates and sections in the manuscript in which it is described and results reported

If you are not able to reproduce the article: 
- Were there missing dependencies? 
- Was the computational environment not adequately described / captured? 
- Were there bugs in the code? 
- Does the code handle errors properly? Where could this be improved?
- Did code run but results (such as model outputs, tables, figures) differ to those published? By how much?

5. User perspective
- What did you find easy / intuitive? (for example: file structure, file naming, analysis workflow, documentation?)
- What did you find confusing / difficult? Identify pressure points and provide constructive suggestions
- What did you enjoy? Identify aspects that worked well.

6. Acknowledge the effort from authors and give them feedback in good faith. It is the code that is being reviewed, not the authors.



   
[blog post from Ariel Rokem](https://uwescience.github.io/neuroinformatics/2017/10/08/code-review.html) is a good first introduction. 
 The [online sustainability evaluation](https://www.software.ac.uk/resources/online-sustainability-evaluation) or [Research Software Health Check](https://www.software.ac.uk/programmes-and-events/research-software-healthcheck) provided by the Software Sustainability Institute might be further helpful resources particularly focusing on issues that affect the sustainability of your software.


[How to do a code review](https://google.github.io/eng-practices/review/reviewer/)


# Resources

## General
* Petre and Wilson 2014 (https://arxiv.org/abs/1407.5648)
* [How to do a code review](https://google.github.io/eng-practices/review/reviewer/)

## Journal, conference and archive guidelines
*	[rOpenSci Software Peer Review](https://ropensci.org/software-review/) contains the guidelines used by rOpenSci before they get added to the rOpenSci suite of packages.
* [Journal of Open Source Software review criteria](https://joss.readthedocs.io/en/latest/review_criteria.html) and [checklist](https://joss.readthedocs.io/en/latest/review_checklist.html)
* [Journal of Open Research Software review form](https://openresearchsoftware.metajnl.com/about/editorialpolicies/)
* [AGILE reproducible guidelines 2020](https://doi.org/10.17605/OSF.IO/CB7Z8)

## Teaching Code Review
*	[Teaching Code Review to University Students](https://www.eduflow.com/blog/teaching-code-review-to-university-students)
* Tips and Tricks for Reproducing and Reviewing by Anna Krystalli ([slides 24-37 on reviewing](https://annakrystalli.me/n8cir-reprohacks/slides/#24))

## Sharing Code Review Experiences
* [’ve code reviewed over 750 pull requests at Amazon. Here’s my exact thought process](https://curtiseinsmann.medium.com/ive-code-reviewed-over-750-pull-requests-at-amazon-here-s-my-exact-thought-process-cec7c942a3a4) - by Curtis Einsmann
* [Identifying and overcoming obstacles to adopting code review](https://www.software.ac.uk/blog/2022-08-17-identifying-and-overcoming-obstacles-adopting-code-review)
