# The Turing Way | Book Dash - Manchester


* Intro to Book Dash MCR slides: https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/book-dash/IntroBookDashMCR.pdf
* HackMD: http://bit.ly/book-dash-mcr

## The participants

* Rachael Ainsworth [@rainsworth](https://github.com/rainsworth/)
* Tarek Allam Jr [@tallamjr](https://github.com/tallamjr)
* Tania Allard [@trallard](https://github.com/trallard)
* Oliver Clark [@OliJimbo](github.com/OliJimbo)
* Alex Clarke [@informationcake](https://github.com/informationcake/)
* Jez Cope [@jezcope](https://github.com/jezcope)
* Joe Fennell [@joe-fennell](https://github.com/joe-fennell)
* Patricia Herterich [@pherterich](https://github.com/pherterich)
* Rosie Higman [@rosiehigman](https://github.com/rosiehigman)
* Will Hulme [@wjchulme](https://github.com/wjchulme) 
* Greg Kiar [@gkiar](https://github.com/gkiar) 
*  Clare Liggins [@ClareLiggins](https://github.com/ClareLiggins)
* Javier Moldon [@jmoldon](https://github.com/jmoldon)
* Beth Montague-Hellen [@AlfAWolf140](https://github.com/AlfAWolf140)
* Jade Pickering [@jspickering](http://www.github.com/jspickering)
* Rosti Readioff [@RostiReadioff](https://github.com/RostiReadioff)
* Kirstie Whitaker [@KirstieJane](https://github.com/KirstieJane/)
* Yo Yehudi [@yochannah](http://www.github.com/yochannah)




## Our report

### What did we do?

Our goal for the book dash was to bring together participants enthusiastic about reproducibility to contribute to and improve the *Turing Way* book during a one day collaborative event. 
We held a networking event the evening prior to the book dash for participants to get to know each other and promote any projects that they're working on, in order to have an intense 9 to 5 day working on the book.
There was a great diversity of lightning talks which were really fun:
* Rachael talked about the women in data meetup group that she organises in Manchester: HER+Data MCR. :woman_technologist:
* Beth revealed what you can and cannot get away with in roller derby! :women_wrestling:
* Jez spoke about the tradition of Morris dancing and his experience as a Morris dancer. 🕺
* Oli wowed us all with a performance of the *Jabberwocky* poem written by Lewis Carroll. 🐉
* Rosti pitched her Soapbox science plans taking place in Stoke-on-Trent. 🔬
* Alex described his Music and Machine Learning projects, as well as his students' project on using ML to classify Gender of voices (and the complications and biases involved). 🎶
* Greg emphasised that a great way to learn more about a sport is through statistics! 🏀
* Kirstie impressed us with her experiences of dog training. 🐶
* Joe informed us about a bomb detector made from bees. 🐝


During the dash, we set out to build upon the [Collaborations Workshop Hackday experience](https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/collabw19/hackdayreport_20190403.md): we wanted to enhance the first version Turing Way project and ensure that contributing to the project is as straightfoward as possible.
We had a mixture of contributions including curating and editing existing content, expanding existing content and writing entirely new content:
* Many of the pull requests's below have been approved and published already!
* New content includes chapters on
  * Reproducible Data Analysis Pipelines for Machine Learning
  * Credit for Reproducible research
  * Code Styling for Reproducibility
* Improved the ease of contributing to the project through enhanced pull request/issue templates, search functionality and  continuous integration within the book.

Specifically:

* [gkiar](https://github.com/gkiar): 
  * Issue: [Expanding on FAIR Principles for Tools](https://github.com/alan-turing-institute/the-turing-way/issues/471)
    * Currently only in the data management section but actually FAIR can apply to a bunch of different aspects of data science (tools, business management etc). Greg couldn't FIND FAIR in the first place which lead to a contribution to the jupyter book repository to add a search bar on each page. (When the day started there was only a way to go to a master search page rather than search from a page that you were reading.) 
  * Issue: [Adding a search bar?](https://github.com/alan-turing-institute/the-turing-way/issues/472)
  * PR: [Adding search button on Jupyter Book](https://github.com/jupyter/jupyter-book/pull/196)
  * Reviewed a PR too :smile: 
* [yochannah](http://www.github.com/yochannah): Centralise figure directories and move to the `content` directory.
  * Need link to PR: 
      * https://github.com/alan-turing-institute/the-turing-way/pull/507
      * https://github.com/alan-turing-institute/the-turing-way/pull/484
  * Move figures folder to the `content` folder which is a more logical location.
  * Reviewed a PR from Chanuki ([Pull request #449](https://github.com/alan-turing-institute/the-turing-way/pull/449)).
* Clare
  * Issue: [Adding links to prerequisities](https://github.com/alan-turing-institute/the-turing-way/issues/435)
  * Need links to PRs:
      * https://github.com/alan-turing-institute/the-turing-way/pull/478
      * https://github.com/alan-turing-institute/the-turing-way/pull/492
  * proofreading chapter 5: Collaborating on GitHub ([Pull request #509](https://github.com/alan-turing-institute/the-turing-way/pull/509))
  * proofreading chapter 7: Reproducible Environments ([Pull request #523](https://github.com/alan-turing-institute/the-turing-way/pull/523))
  * "Fixing mostly little typos and grammar mistakes that are easy to miss when you're writing. Much easier to see after the fact."
* Beth MH [AlfAWolf140](http://github.com/AlfAWolf140): Editing RDM chapter -Formatting fixed
  * https://github.com/alan-turing-institute/the-turing-way/pull/473 Merged
  * Editing Version control chapter to aid understanding for novice users https://github.com/alan-turing-institute/the-turing-way/pull/500
  * Generalising the version control chapter so that it includes more background rather than just focusing on git 
* [RostiReadioff](https://github.com/RostiReadioff) will review/edit Chapter 3 -  reviewed upto line number 547 (Open source hardware processes and practices)
  * Need link to PRs
      * https://github.com/alan-turing-institute/the-turing-way/pull/479
      * https://github.com/alan-turing-institute/the-turing-way/pull/511
  * First Pull request!!! :bell::bell::bell:
  * Reviewed chapter 3, 500+ lines formatting text into a more accessible format!!
* Jade
    * Restructured the Open Research chapter ([Pull request #482](https://github.com/alan-turing-institute/the-turing-way/pull/482))
      * Breaking down into smaller sub pages.....and then updating the table of contents so that these changes actually showed up.
    * Added a Patient and Public Involvement section under the "Open Scholarship" header ([Pull request #510](https://github.com/alan-turing-institute/the-turing-way/pull/510))
      * Related to citizen science but a little more specific.
* Will: 
  * adding content on *data organisation in spreadsheets* to the RDM chapter, issue [#481](https://github.com/alan-turing-institute/the-turing-way/issues/481), PR [#499](https://github.com/alan-turing-institute/the-turing-way/pull/499)
    * First iterative review experience in a pull request (previously had been really simple).
  * adding content on synthetic data, issue [#506](https://github.com/alan-turing-institute/the-turing-way/issues/506)
    * To be written
* Kirstie: update PR template
  * Reviewed a bunch of PRs and added some templates
* Rosie: restructured the Risk Assessment chapter, Reviewing PRs, adding guidance on relative links
  * Need links to PRs
      * https://github.com/alan-turing-institute/the-turing-way/pull/503
  * Helped lots of folks with github weirdneses
* Jez: drafting [chapter on credit for reproducible research](https://deploy-preview-485--the-turing-way.netlify.com/credit/credit.html)
  * [Pull request #485](https://github.com/alan-turing-institute/the-turing-way/pull/485)
  * Looking for reviewers and there are lots of different to do notes to myself.
* Oli: [Started issue 124 - Chapter on style guides and linting.](https://github.com/alan-turing-institute/the-turing-way/issues/124)
  * [Pull Request #498](https://github.com/alan-turing-institute/the-turing-way/pull/498)
  * Message of the chapter: "Do as you wish, but try to be consistent."
  * Examples in R and Python.
* Alex, Joe, Javier, Tarek
  * Chapter outline: Reproducible data analysis pipelines for machine learning
  * https://github.com/alan-turing-institute/the-turing-way/pull/477
  * Sketched out in notes, lots of post its! Collaboratively written across all 4 team members.
  * Looking for reviewers.
* Tania
  * continuous integration for the website to test for alt tags on the images (for better accessibility) and making sure that the links resolve.
* Patricia & Rachael
  * Reviewed pull requests. Had a fright when Netlify got overwhelmed with all our different PRs. Opened some new issues so the team have them written down for future work :smile: 
* Matt
  * Drew all these pictures!
  * Favourite was the community garden - nurturing everyone so that all the collaborative work can grow :heart_eyes:


## What did we learn?

There's also an issue for feedback - any comments on what we can do better at future events are appreciated: https://github.com/alan-turing-institute/the-turing-way/issues/505


* Blog posts:
    * https://montaguehellen.wordpress.com/2019/05/20/the-turing-way-and-a-return-to-github/
* 
* 
*  
* 
*  


## Pluses and deltas

https://hackmd.io/9IIQpagHQoOGlwUnY98xQA


