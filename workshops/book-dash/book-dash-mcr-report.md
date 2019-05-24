# The Turing Way | Book Dash - Manchester


* Intro to Book Dash MCR slides: https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/book-dash/IntroBookDashMCR.pdf
* HackMD: http://bit.ly/book-dash-mcr

## The participants

![/figures/book_dash_mcr_group.jpg](/figures/book_dash_mcr_group.jpg)
*Back row, left to right: Jez Cope, Will Hulme, Oliver Clark, Jade Pickering, Rosie Higman, Alex Clarke. Middle row, left to right: Clare Liggins, Beth Montague-Hellen, Patricia Herterich, Tania Allard, Kirstie Whitaker, Tarek Allam Jr. Front row, left to right: Matthew Kemp, Greg Kiar, Yo Yehudi, Rosti Readioff, Rachael Ainsworth, Javier Moldon.*

* Rachael Ainsworth [@rainsworth](https://github.com/rainsworth/)
* Tarek Allam Jr [@tallamjr](https://github.com/tallamjr)
* Tania Allard [@trallard](https://github.com/trallard)
* Oliver Clark [@OliJimbo](https://github.com/OliJimbo)
* Alex Clarke [@informationcake](https://github.com/informationcake/)
* Jez Cope [@jezcope](https://github.com/jezcope)
* Joe Fennell [@joe-fennell](https://github.com/joe-fennell)
* Patricia Herterich [@pherterich](https://github.com/pherterich)
* Rosie Higman [@rosiehigman](https://github.com/rosiehigman)
* Will Hulme [@wjchulme](https://github.com/wjchulme) 
* Greg Kiar [@gkiar](https://github.com/gkiar) 
* Clare Liggins [@ClareLiggins](https://github.com/ClareLiggins)
* Javier Moldon [@jmoldon](https://github.com/jmoldon)
* Beth Montague-Hellen [@AlfAWolf140](https://github.com/AlfAWolf140)
* Jade Pickering [@jspickering](http://www.github.com/jspickering)
* Rosti Readioff [@RostiReadioff](https://github.com/RostiReadioff)
* Kirstie Whitaker [@KirstieJane](https://github.com/KirstieJane/)
* Yo Yehudi [@yochannah](http://www.github.com/yochannah)


## Our report

### What did we do?

Our goal for the book dash was to bring together participants enthusiastic about reproducibility to contribute to and improve *The Turing Way* book during a one day collaborative event. 
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

During the dash, we set out to build upon the [Collaborations Workshop Hackday experience](https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/collabw19/hackdayreport_20190403.md): we wanted to enhance the first version of *The Turing Way* book and ensure that contributing to the project is as straightfoward as possible.
We had a mixture of contributions including curating and editing existing content, expanding existing content and writing entirely new content:
* Many of the pull requests below have been approved and published already!
* New content includes chapters on
  * Reproducible Data Analysis Pipelines for Machine Learning
  * Credit for Reproducible research
  * Code Styling for Reproducibility
* Improved the ease of contributing to the project through enhanced pull request/issue templates, search functionality and  continuous integration within the book.

Specifically:

* Greg Kiar [@gkiar](https://github.com/gkiar): 
  * Issue: [Expanding on FAIR Principles for Tools](https://github.com/alan-turing-institute/the-turing-way/issues/471)
    * Currently only in the data management section but actually FAIR can apply to a bunch of different aspects of data science (tools, business management etc). 
Greg couldn't FIND FAIR in the first place which lead to a contribution to the jupyter book repository to add a search bar on each page. 
(When the day started there was only a way to go to a master search page rather than search from a page that you were reading.) 
  * Issue: [Adding a search bar?](https://github.com/alan-turing-institute/the-turing-way/issues/472)
  * PR to Jupyter Book: [Adding search button on Jupyter Book](https://github.com/jupyter/jupyter-book/pull/196)
  * Reviewed a PR too :smile: 

* Yo Yehudi [@yochannah](http://www.github.com/yochannah): 
  * Centralise figure directories and move to the `content` directory. ([Pull request #507](https://github.com/alan-turing-institute/the-turing-way/pull/507))
  * Reviewed a PR from Chanuki ([Pull request #449](https://github.com/alan-turing-institute/the-turing-way/pull/449)).
  * gGrammar/typo tweak for the book build README ([Pull request #484](https://github.com/alan-turing-institute/the-turing-way/pull/484)) [merged]

* Clare Liggins [@ClareLiggins](https://github.com/ClareLiggins)
  * Issue: [Adding links to prerequisities](https://github.com/alan-turing-institute/the-turing-way/issues/435) [closed]
  * Added a link to the version control prerequisite ([Pull request #478](https://github.com/alan-turing-institute/the-turing-way/pull/478)) [merged]
  * Adding in prerequisite links to rest of the chapters ([Pull request #492](https://github.com/alan-turing-institute/the-turing-way/pull/492)) [merged]
  * proofreading chapter 5: Collaborating on GitHub ([Pull request #509](https://github.com/alan-turing-institute/the-turing-way/pull/509)) [merged]
  * proofreading chapter 7: Reproducible Environments ([Pull request #523](https://github.com/alan-turing-institute/the-turing-way/pull/523))
  * "Fixing mostly little typos and grammar mistakes that are easy to miss when you're writing. Much easier to see after the fact."

* Beth Montague-Hellen [@AlfAWolf140](https://github.com/AlfAWolf140): 
  * Editing RDM chapter -Formatting fixed ([Pull request #473](https://github.com/alan-turing-institute/the-turing-way/pull/473)) [merged]
  * Editing Version control chapter to aid understanding for novice users ([Pull request #500](https://github.com/alan-turing-institute/the-turing-way/pull/500))
  * Generalising the version control chapter so that it includes more background rather than just focusing on git 

* Rosti Readioff [@RostiReadioff](https://github.com/RostiReadioff)
  * First Pull request!!! :bell::bell::bell:
    * Edits to Chapter 2 Summary to include definition [Pull request #479](https://github.com/alan-turing-institute/the-turing-way/pull/479) [merged]
  * Reviewed/edited Chapter 3 -  reviewed up to line number 547 (Open source hardware processes and practices) ([Pull request #511](https://github.com/alan-turing-institute/the-turing-way/pull/511)).
  * Add link to citations ([Issue #495](https://github.com/alan-turing-institute/the-turing-way/issues/495))

* Jade Pickering [@jspickering](http://www.github.com/jspickering):
  * First Pull request!!! :bell::bell::bell:
    * Restructured the Open Research chapter ([Pull request #482](https://github.com/alan-turing-institute/the-turing-way/pull/482)) [merged]
    * Breaking down into smaller sub pages.....and then updating the table of contents so that these changes actually showed up.
  * Added a Patient and Public Involvement section under the "Open Scholarship" header ([Issue #497](https://github.com/alan-turing-institute/the-turing-way/issues/497), [Pull request #510](https://github.com/alan-turing-institute/the-turing-way/pull/510))
     * Related to citizen science but a little more specific.

* Will Hulme [@wjchulme](https://github.com/wjchulme): 
  * adding content on *data organisation in spreadsheets* to the RDM chapter, ([Issue #481](https://github.com/alan-turing-institute/the-turing-way/issues/481)) [closed], ([Pull request #499](https://github.com/alan-turing-institute/the-turing-way/pull/499)) [merged]
    * First iterative review experience in a pull request (previously had been really simple).
  * adding content on synthetic data, ([Issue #506](https://github.com/alan-turing-institute/the-turing-way/issues/506))
    * To be written
  * regularly -> frequently ([Pull request #475](https://github.com/alan-turing-institute/the-turing-way/pull/475)) [merged]

* Kirstie Whitaker [@KirstieJane](https://github.com/KirstieJane/): 
  * update PR template ([Pull request #489](https://github.com/alan-turing-institute/the-turing-way/pull/489)) [merged]
  * Reviewed a bunch of PRs and added some templates
  * Alphabetise the contributors ([Pull request #508](https://github.com/alan-turing-institute/the-turing-way/pull/508)) [merged]
  * Acknowledge contributors ([Pull request #494](https://github.com/alan-turing-institute/the-turing-way/pull/494)) [merged]

* Rosie Higman [@rosiehigman](https://github.com/rosiehigman): 
  * Restructured the Risk Assessment chapter ([Pull request #503](https://github.com/alan-turing-institute/the-turing-way/pull/503))
  * Reviewed PRs
  * Added guidance on relative links in Contributing Guidelines ([Issue #487](https://github.com/alan-turing-institute/the-turing-way/issues/487), [Pull request #493](https://github.com/alan-turing-institute/the-turing-way/pull/493)) [closed, merged]
  * Helped lots of folks with github weirdneses

* Jez Cope [@jezcope](https://github.com/jezcope): 
  * Drafted [chapter on credit for reproducible research](https://deploy-preview-485--the-turing-way.netlify.com/credit/credit.html) ([Pull request #485](https://github.com/alan-turing-institute/the-turing-way/pull/485))
  * Looking for reviewers and there are lots of different to do notes to myself.

* Oliver Clark [@OliJimbo](https://github.com/OliJimbo): 
  * Started Chapter on style guides and linting ([Issue 124](https://github.com/alan-turing-institute/the-turing-way/issues/124), [Pull Request #498](https://github.com/alan-turing-institute/the-turing-way/pull/498))
  * Message of the chapter: "Do as you wish, but try to be consistent."
  * Examples in R and Python.

* Alex Clarke [@informationcake](https://github.com/informationcake/), Joe Fennell [@joe-fennell](https://github.com/joe-fennell), Tarek Allam Jr [@tallamjr](https://github.com/tallamjr), Javier Moldon [@jmoldon](https://github.com/jmoldon):
  * Chapter outline: Reproducible data analysis pipelines for machine learning ([Issue #483](https://github.com/alan-turing-institute/the-turing-way/issues/483), [Pull request # 477](https://github.com/alan-turing-institute/the-turing-way/pull/477))
  * Sketched out in notes, lots of post its! Collaboratively written across all 4 team members.
  * Looking for reviewers.
  
* Tarek Allam Jr [@tallamjr](https://github.com/tallamjr):  
  * Updating Github templates ([Issue #476](https://github.com/alan-turing-institute/the-turing-way/issues/476), [Pull request #488](https://github.com/alan-turing-institute/the-turing-way/pull/488)) [merged]
  * Updating 'about' key as this required by Github ([Pull request #502](https://github.com/alan-turing-institute/the-turing-way/pull/502)) [merged]

* Tania Allard [@trallard](https://github.com/trallard):
  * Continuous integration for the website to test for alt tags on the images (for better accessibility) and making sure that the links resolve ([Issue #486](https://github.com/alan-turing-institute/the-turing-way/issues/486), [Pull request #513](https://github.com/alan-turing-institute/the-turing-way/pull/513)) [closed, merged]

* Patricia Herterich [@pherterich](https://github.com/pherterich), Rachael Ainsworth [@rainsworth](https://github.com/rainsworth/):
  * Reviewed pull requests. 
  * Had a fright when Netlify got overwhelmed with all our different PRs. 
  * Added contributors.
  * Opened some new issues so the team have them written down for future work :smile: 

* Matt:
  * Drew all these pictures!
  * Favourite was the community garden - nurturing everyone so that all the collaborative work can grow :heart_eyes:
  ![https://pbs.twimg.com/media/D6zGuPiW4AI3m8s?format=jpg&name=4096x4096](https://pbs.twimg.com/media/D6zGuPiW4AI3m8s?format=jpg&name=4096x4096)


## What did we learn?

There's also an issue for feedback - any comments on what we can do better at future events are appreciated: https://github.com/alan-turing-institute/the-turing-way/issues/505

* 2 first pull requests!! :bell: :bell:
* When adding participants as collaborators to the project on GitHub, let them know and make sure they are aware of the email they've received and added functionality that comes with it.
* Add explicit guidance on putting GitHub handles into the intro presentation and trying to make sure this happens in the initial brain storming session to keep track of contributors.
* Feedback from [Pluses and deltas](https://hackmd.io/9IIQpagHQoOGlwUnY98xQA)
  * Pluses: really supportive and inclusive environment, good organisation, brilliant icebreaker and really enjoyed having the artist in residence!
  * Deltas: needed more time, friendlier introduction to Git/GitHub and more guidance on what tasks to take up.
* Beth Montague-Hellen [@AlfAWolf140](https://github.com/AlfAWolf140) wrote a blog post about her experience: https://montaguehellen.wordpress.com/2019/05/20/the-turing-way-and-a-return-to-github/

