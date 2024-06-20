# Technical Improvements to enhance the usability of The Turing Way chapters by different user groups

## Contact details : 

**Full name**: Arya A 
**Neurostars ID**: @arya
**Location**: India

**Portfolio**: [https://a-r-y-aa.github.io/](https://a-r-y-aa.github.io/)
**GitHub**: [https://github.com/arya1302](https://github.com/arya1302)


## Project details

[The Turing Way](https://book.the-turing-way.org/index.html) is an open source, open collaboration and community-led handbook on data science. The project is developed online on [GitHub repo](https://github.com/alan-turing-institute/the-turing-way/tree/main/book) using open source solutions. The main infrastructure used for hosting the book is [JupyterBook](https://jupyterbook.org/en/stable/intro.html) and the content of the book utilizes the MyST flavour of Markdown. The Turing Way content for the book is hosted online in a browsable format at[ https://book.the-turing-way.org/](https://book.the-turing-way.org/)<span style="text-decoration:underline;">. </span>Over the last four years, the book has massively expanded with contributions from over 400+ international contributors who have authored 260+ chapters across five guides. With this scale, the content in the book is difficult to navigate, especially for new users – who are some of the most important target audiences for the project. 

In 2022, the team developed a [Python Package](https://github.com/alan-turing-institute/bio-Turing-Way/tree/main/pathways) to improve the usability of The Turing Way by allowing different entry points or as defined by them as ‘different pathways’ to the book based on the user profile or persona (see reference for [persona and pathways](https://book.the-turing-way.org/project-design/persona.html)). For example, the screenshot below shows four pathways for users who attend a Data Study Group or are PhD Students, Group Leaders or Life Scientists.

<!--![alt_text](images/image1.png "image_tooltip")-->


### The project defined for the GSoC is to improve the Python Package (developed on the GitHub repository, and tested on The Turing Way) and integrate that in the book. These resources were provided in The Turing Way [GitHub issue for GSoC 2023](https://github.com/alan-turing-institute/the-turing-way/issues/2978).

* Python Package:[ https://github.com/alan-turing-institute/bio-Turing-Way/tree/main/pathways](https://github.com/alan-turing-institute/bio-Turing-Way/tree/main/pathways)
* Demo of this code on The Turing Way book:[ https://github.com/alan-turing-institute/bio-Turing-Way/tree/main/master](https://github.com/alan-turing-institute/bio-Turing-Way/tree/main/master)
* Online test book when deployed:[ https://the-turing-way-personas.netlify.app/welcome](https://the-turing-way-personas.netlify.app/welcome)


## My Application in detail


In my application, I focus on the technical improvement of a Python Package developed for enhancing the accessibility of The Turing Way. Emphasizing of the user experience and how the content of the book is served to them based on the ‘persona’ or profile they choose to browse curated content (defined as Pathway), I have described my ideas in the following three steps: 

1. **Making the browsing experience less confusing** by modifying chapter links and profile tag based on a selected ‘pathway’, rather than displaying all tags associated with a chapter (which is the current problem). 
2. **Adding a feature to provide a description for each pathway** (associated with the user profiles) which will improve user experience allowing meaningful use of books by all profile types. 
3. **Implementing the solutions proposed in this application** and integrating them to The Turing Way via the open source framework (collaborative development on a GitHub branch, pull request to invite code review and merging the changes in agreement with the project leads/mentors).


## Minimum set of deliverables

**Technical Improvements to make browsing experience less confusing**

### <span style="text-decoration:underline;">Problem:</span> 

When you visit a chapter within a profile-specific page, you will see all profile tags/labels/shields where this chapter is selected (the same chapter can be curated for multiple profiles). All tags/labels/shields appear on the top of the page. It will be helpful to have only the original profile (where the user clicked) on the top, and the rest could be hidden to avoid confusion. This may need some planning and development of a new Python Class.

**Approach & Basic Idea** 

When a user visits a profile page, all hyperlinks corresponding to the chapters of the selected profile will be modified by adding the selected profile details (name, colour) as a  search parameter of the hyperlink. When a user visits any of the chapters, the search parameter is retrieved and the details of the profile are used for modifying the profile tag.

<!--![alt_text](images/image2.png "image_tooltip")-->


**Implementation details**

This can be implemented with the help of JavaScript. Jupyter Notebook Markdown allows us to use raw HTML in Markdown cells hence we can include JavaScript.

**Step 1: Modifying the chapter links**

 The write_content function in the LandingPage class ( landing_page.py file) is modified by adding js code as a multiline string. The LandingPage class uses mdutils (python library) to create and manipulate markdown formatted text. By using the .write() method of mdutils we can add the raw code to the corresponding markdown files. 

<!--![alt_text](images/image3.png "image_tooltip")-->


The JavaScript code above selects all the links on the page and retrieves the current url path. It then extracts the last part of the url, replaces html extension and hyphens with spaces to get the selected profile name. Finally, it modifies each chapter link by adding a search parameter called pathway having the extracted profile name as its value. 

**Step 2: Modifying the profile tag/labels to fix the issue**

The badge.py file handles all badge-related functionalities.  In the "generate_shields_link" function, the URL of the badge is modified by replacing the message=landing name with message=text. This will create a sample badge element.   

<!--![alt_text](images/image4.png "image_tooltip")-->

<!--![alt_text](images/image5.png "image_tooltip")-->


Then the  insert_badges function is modified by adding the JavaScript code as a multiline string. By using f.write we can add the code to all the markdown files specified.The code will get executed and we will get the desired result.

<!--![alt_text](images/image6.png "image_tooltip")-->


The above js code selects all the img tags having src  equals to "[https://img.shields.io/static/v1?label=pathway&message=text](https://img.shields.io/static/v1?label=pathway&message=text)". Then using URLSearchParams it gets the value of the search parameter pathway. Then it loops through each selected img tag and modifies the src attribute with a new url having the value of the pathway parameter. 


1. **Adding a feature to provide a description for each pathway (making it attractive)**

**Step 1:  The first step is to add a description in profiles.yml (master/profile.yml)**

<!--![alt_text](images/image7.png "image_tooltip")-->

Here I have added a dummy description for each profile in profiles.yml.

**Step 2: Modify the Python files needed to implement this functionality (main.py, landing_page.py)**

The generate_landing_page function in main.py and LandingPage class in landing_page.py  is modified by adding one more parameter called Description:

<!--![alt_text](images/image8.png "image_tooltip")-->

<!--![alt_text](images/image9.png "image_tooltip")-->


The pathways function in main.py is modified by adding profile[“description”]. Using profile[“description”] we will get the value of the description. 

<!--![alt_text](images/image10.png "image_tooltip")-->


The write_content function is modified by adding the following code 

**_self.md_file.new_paragraph(self.description)_**

The code snippet uses the new_paragraph() method of mdutils class to add a new paragraph to the markdown. The self.description is added as an argument to the new_paragraph() method so that the value of self.description will be included as the text of the new paragraph. 

Finally, we will get this UI. Here I have used a dummy text. More UI enhancements such as reducing the size of the heading “Table Of Contents” can also be added 

<!--![alt_text](images/image11.png "image_tooltip")-->

2. **Integrate the changes in The Turing Way Book**

To integrate the changes that I will have made as described in this application, I will create a pull request following a reference provided by The Turing Way mentors ([https://github.com/alan-turing-institute/the-turing-way/pull/2246](https://github.com/alan-turing-institute/the-turing-way/pull/2246)). I will include a detailed description of the changes I have  made, the issues I've addressed, and the improvements I have implemented.


## Additional ‘if time allows’ deliverables 


There are a few more ideas I would like to implement if the time allows, some of which are mentioned below. 

* During the exploration phase I noticed that there are repetitions of badges. This seems like an error from the testing phase, which can be easily fixed by making changes to the badge.py file. I plan to fix this with a pull request.

<!--![alt_text](images/image12.png "image_tooltip")-->

* Another issue I noticed is that if a visitor doesn't select any pathway and proceeds to read a chapter, the pathways badge shows null. I'm considering displaying all the pathways of a chapter in this situation. I think this could be a good idea to prompt users to look at or help improve the current pathways. However, this will need more time to implement.
* Another contribution idea includes describing and bringing consistency to how one can select the colour of the badge and associated links for each pathway.


## Detailed timeline

**Community Bonding Period**

Continue as a contributor (before April 2023)

* Become more familiar with the project on GitHub.
* Understand expectations in this project by understanding the details of the GSoC project, and connecting with the project mentors.
* Become more familiar with the underlying tools (like Jupyter Book, Markdown, and Netlify) and explore the Python Package where I will make the improvements.
* Discuss ideas with the mentors on Slack and GitHub.

Application Preparation period (until 4 April 2023)

* Document what I have worked on
* Describe my ideas by sharing information about how I have tested the viability of my ideas (such as by prototyping my solution)
* Invite a review of my ideas with the mentors.

Share prototype with the mentors (until May 29)

* During this period, I will engage with the community by attending their Collaboration Cafe and engaging via Slack
* I will also engage with the project such as by creating new issues, fixing small bugs and reviewing small Pull Requests on the GitHub repository to get used to working with the community.
* I will share code developed for testing my ideas with my mentors and ask for their feedback to improve upon

**Let the coding begin! (May 29 onwards)**


### **May 29 - June 10**

I will officially start working on the first two steps described in my application:

* **Making the browsing experience less confusing** by modifying chapter links and profile tags based on a selected ‘pathway’, rather than displaying all tags associated with a chapter (which is the current problem). 
* **Providing better, more understandable description for each pathway** and their landing pages (associated with the user profiles), which will improve user experience allowing meaningful use of books by all profile types. 

### **July 10 - July 14**

* I will gather feedback from my mentors during this stage
* I will draft my work in a report for submitting midterm evaluations

### **July 14 - August 21**

* I will integrate changes as discussed with my mentors
* I will convert prototype ideas into implementation for pathways described for at least two user profiles
* I will then implement the solutions created from my contributions and integrate them into The Turing Way via the open source framework (collaborative development on a GitHub branch, pull request to invite code review and merging the changes in agreement with the project leads/mentors).

### **August 21 - 28 - 18:00 UTC**

* Final week: I will submit my final work in a report for my mentor’s evaluation
* If time allows, I will also test some additional ideas described in this application

### **August 28 - September 5**

* (Initial results of Google Summer of Code 2023 announced)

### **September 4 - November 6**

* If an extension would be required, I will catch up on any backlog from the previously described timeline


## Plan for communication with mentors: 

I would be regularly updating my mentors about my work and progress. I will be joining community coworking calls with Malvika Sharan (Co-Lead and Mentor), Johanna Bayer (Mentor), and Anne Lee Steele (Community Manager). 

I have also applied to attend their biannual event, Book Dash and hoping to learn how the team works with the community. 


## About Me : 

**_Short summary of my past experience  _**

I am an undergraduate, currently pursuing a bachelor of technology in computer science engineering with a specialization in artificial intelligence. I am skilled in Python, HTML, CSS, JavaScript and React. I have worked on various projects related to web development. Also, I have worked with Jupyter notebooks as a part of my Machine Learning Projects. 

I was a web developer intern at [Traboda](https://traboda.com/) ([certificate](https://drive.google.com/file/d/1TU8DJQocJWlBh483ID9hkxikkwKx_Zrl/view?usp=share_link)) where I worked with a major focus on front end web development. My experience with [Traboda](https://traboda.com/) helped me in improving my web development skills. I was also an active member of an open source club at my college called [amFOSS](https://amfoss.in/). My experience with amFOSS helped me in gaining knowledge about git, open source. I have participated in hackathons and coding competitions as well which gave me a good foundation on software development. 

**_Motivation - why do I want to do this project_**

The aim of The Turing Way is to make data research accessible to a wider research community. The project enables experts in various domains to share their knowledge. I would like to be part of a community focused on sharing knowledge and if I could make improvements which enhance the experience of its users, I would be happy to do so.                    

Moreover, this project involves improving a Python package which could improve the user experience of The Turing Way book website. I have a huge interest in web development,  improving user interfaces and enhancing the user experience. The project based on the proposed idea requires the use of JavaScript and Python. Both these tech stacks are familiar to me. Doing this project will give me an opportunity to expand my knowledge of these tech stacks as well.

**_Match - the project I've worked on in the past that would make me a good candidate for this project_**

Being a student learning AI. I have to use Python a lot and I have used Python for implementing various machine learning projects. I also contributed to the development of a Python-based desktop application 

- link to Github repo:  [https://github.com/arya1302/Data-Compression-LZW](https://github.com/arya1302/Data-Compression-LZW)

I worked as a web developer intern at [Traboda](https://traboda.com/) which is an organization focused on building cybersecurity ed-tech platforms. During my internship at [Traboda](https://traboda.com/),  I implemented new UI features for the Cyber Fundamentals Learning Platform (Academy) and fixed certain bugs on the CTF hosting platform (Arena). The experience helped me in gaining sufficient knowledge to enhance the user interface using JavaScript. 

**_You can apply for up to three projects. Is this the only project that you will apply for?_**

_ _Yes this is the only project I am applying for. I would like to focus on this particular project as it matches my interests.

**_Working time - how many hours per week do you plan to work, and how will you divide your time?_**

I will work after my college university classes. On weekends I will get more time to work on the project. 

My end-semester exams will be starting from May 29th onwards. It will last about two weeks. I will try my best to finish the work before the start of my end semester exams and if I am still faced with some pending work, I will be able to catch up and manage my work after the exams by putting in more time and effort. 
