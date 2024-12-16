(cm-pr-code)=

# Guidance on Code Review

Code review can help increase the accuracy of results, improve usability and maintainability of code, and is a great opportunity to learn. For a more detailed overview of motivations for Code Review, please see the {ref}`Code Reviewing Process <rr-reviewing-motivation>`.

The most important questions during code review are: 
- Are all the files available? If not, ask the editor to request the data/code from the authors.
- Does it run? 
- Is it easy to understand? 
Or is it more complex than it should be?
- If it is not just a script underlying a publication but part of software infrastructure: how easy is it to maintain? 

[Code does not have to be perfect](https://google.github.io/eng-practices/review/reviewer/standard.html) - it has to work, be accompanied with sufficient documentation and be maintainable if this is needed.

The [online sustainability evaluation](https://www.software.ac.uk/resources/online-sustainability-evaluation) provided by the Software Sustainability Institute can help address issues that affect the sustainability of the software.

## Code review in [ReproHack style](https://annakrystalli.me/n8cir-reprohacks/slides/#24)

*This is more applicable when you're reviewing the code underlying a research article.*

**1. Access**
- How easy is it to access the materials? 
Can you access all the materials?
  - Is the data stored in a separate directory or data repository? 
Is there a persistent identifier associated with the data/code?

**2. Installation**
- Are you able to install everything, did you run into any problems and how did you solve these?

**3. Documentation**
Does the documentation contain information on:
- how to install necessary software and dependencies?
- how to use materials to reproduce the paper?
- how to cite the materials, ideally in a form that can be copy and pasted?
Provide suggestions on how to improve the documentation of the code if needed.
- Are the inline comments in the code helpful and necessary?
Comments should explain why some code exists, not what the code is doing. [If the code isn’t clear enough to explain itself, then the code should be made simpler](https://google.github.io/eng-practices/review/reviewer/looking-for.html#comments). 
- Is the code following applicable style guides? (for example, [Google Style Guide](http://google.github.io/styleguide/)

**4. Reproduction**
- Were you able to fully reproduce the paper? 
- How automated was the process of reproducing the paper?
- How easy was it to link analysis code to the plots it generates and sections in the manuscript in which it is described and results reported

If you are not able to reproduce the article: 
- Were there missing dependencies? 
- Was the computational environment not adequately described / captured? 
- Were there bugs in the code? 
- Does the code handle errors properly? 
Where could this be improved? 
If there are any tests, check if they are correct, sensible, and useful.
- Did code run but results (such as model outputs, tables, figures) differ to those published? 
By how much?
Was this to be expected (for example, because of use of random numbers in the method)?

**5. User perspective**
- What did you find easy / intuitive? 
(For example: file structure, file naming, analysis workflow, documentation?)
- What did you find confusing / difficult? 
Identify pressure points and provide constructive suggestions
- What did you enjoy? Identify aspects that worked well.

**6. Acknowledge the effort from authors** and give them feedback in good faith. 
Also tell them what they did well!

## CODECHECK
[CODECHECK](https://codecheck.org.uk/) provides a workflow, guidelines and tools to evaluate computer programs underlying scientific papers. 
If you want to get involved as a codechecker in the community, or if you want to apply the CODECHECK principles in your journal or conference, please take a look at the [Get Involved page](https://codecheck.org.uk/get-involved/).

## Code Review of research software

Please see the {ref}`Code Reviewing Process chapter <rr-reviewing>` for more details when reviewing software as a primary research output, which includes a {ref}`checklist for code review process <rr-checklist-for-code-review>`


# Resources

## Journal, conference and archive guidelines
*	[rOpenSci Software Peer Review](https://ropensci.org/software-review/) contains the guidelines used by rOpenSci before they get added to the rOpenSci suite of packages.
* [Journal of Open Source Software review criteria](https://joss.readthedocs.io/en/latest/review_criteria.html) and [checklist](https://joss.readthedocs.io/en/latest/review_checklist.html)
* [Journal of Open Research Software review form](https://openresearchsoftware.metajnl.com/about/editorialpolicies/)
* [AGILE reproducible guidelines 2020](https://doi.org/10.17605/OSF.IO/CB7Z8)
* [Journal of Open Source Education review criteria](https://openjournals.readthedocs.io/en/jose/review_criteria.html/)
* [pyOpenSci Software Peer Review](https://www.pyopensci.org/peer-review-guide/) contains the guidelines used by pyOpenSci, an initiative promoting open peer review process in the scientific Python ecosystem. Different to JOSS, pyOpenSci aims to followup with the maintainer to ensure that the package is maintained over time.

## Teaching Code Review
*	[Teaching Code Review to University Students](https://www.eduflow.com/blog/teaching-code-review-to-university-students)
* Tips and Tricks for Reproducing and Reviewing by Anna Krystalli ([slides 24-37 on reviewing](https://annakrystalli.me/n8cir-reprohacks/slides/#24))

## Sharing Code Review Experiences
* [I’ve code reviewed over 750 pull requests at Amazon. Here’s my exact thought process](https://curtiseinsmann.medium.com/ive-code-reviewed-over-750-pull-requests-at-amazon-here-s-my-exact-thought-process-cec7c942a3a4) - by Curtis Einsmann
* [Identifying and overcoming obstacles to adopting code review](https://www.software.ac.uk/blog/2022-08-17-identifying-and-overcoming-obstacles-adopting-code-review)
