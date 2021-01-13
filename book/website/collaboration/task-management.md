# Task management with teams

Content/draft for issue https://github.com/alan-turing-institute/the-turing-way/issues/1436


## Contents

* Project pulse - some systems to keep a project going
* Tasks - planning and setting prioerities
* Tools - what you need to set this up
There are some similarities here to creating Github issues, but this idea is more general and focuses more on conventions/agreements with team members, than on working with specific tools.


## Systems & project "pulse"

When planning a project, we might be tempted to use phases like "data collection" or "method development" which neatly follow each other. This might not always be a useful paradigm for data science projects, and/or projects where you are supervising junior contributors.

Instead, it might be useful to define a system or "project pulse" which ensures who checks in with whom, and at what time intervals, and what happens at these time points. This will probably lead to more frequent check-ins than traditional milestones, but will ensure that tasks are more adaptive, and progress is being made on the project. Having such a system in place will also set clear expectations for who is responsible for what. 

There are various systems and paradigms on how to set up such systems, but two relatively general ones that can be adapted for many projects are Scrum and Getting Things Done (GTD) which we cover here. 


### Scrum

Scrum is a system frequently used in software development. Traditionally in this process, a team is working on the same project. The "pulse" is defined by two-week intervals called sprints. In short, every sprint starts with the team planning tasks for the two week period. The team proceeds with tasks, and has a 15 minute check-in called stand-up every day, to see if there are any issues. 

In a research setting this might be less applicable if each person is working on their own project, and the timing might be slower due to experiments, for example. However principles can still be adapted to a research setting, here are some examples:  

* http://www.cs.umd.edu/~mwh/papers/score.pdf
* https://psyarxiv.com/zg4ub
* https://veronikach.com/phd-advice/organizing-student-projects-with-scrum/
* Weekly meetings with Github https://github.com/WhitakerLab/WhitakerLabProjectManagement/ 


### Getting Things Done

Getting Things Done (GTD) is a system introduced by David Allen. This is an approach to task management initially intended for individuals, but it is possible to apply the principles more broadly. Overall it comes down to two types of actions:

* Capturing tasks, where you add a task, idea or note to your GTD app (apps and tools are discussed later in this chapter) as soon as it comes up.
* Processing tasks, where you sort and organize all items in your GTD app so that you know what you need to focus on next. You usually do this every week during a meeting called the weekly review. 

Here are some examples of how different people implement GTD:  

* Week review template: https://ihavesomanyideas.com/art-week-review-free-template/
* GTD with Evernote: https://medium.com/@sandoche/how-to-build-a-productive-system-with-evernote-to-get-things-done-7b3305ad4be3
* GTD with Evernote and Todoist: https://veronikach.com/habits-productivity/how-im-implementing-gtd-with-todoist-evernote-and-google-calendar-part-1/
* GTD for academics: http://rtalbert.org/gtd-for-academics-weekly-review/


## Tasks

Next to having a system or project pulse, it is worthwhile to think about how you define tasks, especially since this definition may vary across team members. What some people consider a task, might actually be an entire project with many tasks of its own. If person A defines such a project-task for person B to execute, person B might not know where to get started, or take an different approach than what person A had in mind. Defining tasks together (such as during sprint planning or a weekly review) can help to avoid such misunderstandings. 

Here are a few simple rules to think about tasks: 

* Use a verb when defining a task. Rather than "literature review", add "read 5 papers" to your list. 
* Define what it means to be done with a task. Rather than "read 5 papers", you could use "write 100-word summaries for 5 papers"
* If you do not think you could finish a particular task if you just start it and give yourself a couple of hours to do it, you probably need to break it down into smaller tasks

If you are creating tasks for yourself, it is tempting to skip some of these steps because "you know what you mean" when you write down "literature review". But even if you are not working in a team, it can help you if you are crystal clear. This way you can spend some extra time planning your tasks, so that at a later date, your future self can just go into "execution mode" without figuring out where to start. 


### Sorting tasks 

If you are good at capturing tasks that need to be done, you will probably end up with a lot of tasks. To avoid getting overwhelmed and doing everything at the same time, you will need to decide if, and when, to do the tasks you have captured. You can for example do this during the weekly review. There are several ways to do this, but most of them can be seen as adding more meta-data to each task, such as: 

* A specific date that the task must be complete.
* A priority, such as "urgent" and/or "important" (based on the Eisenhower matrix).
* How long you estimate the task will take. 
* How much energy you need to do the task. 
* Context you need to do the task, such as being at the office.  

Given this information, ideally you want to plan which tasks you will do when, based on the priority and resources (such as time) available. A caveat with the way we often choose which task to do next, is to spend all time focusing on the urgent tasks, but to forget the "not urgent and important ones". If you have a dedicated planning session ahead of time, you can be mindful that you also allocate some time to this category.  

The best way to ensure that you don't overplan the tasks, is to plan the tasks on your calendar. Next to already blocking the time you need, this can help you get better at estimating how long each task should take. It may also be useful to have "themed" days or time blocks. For example you can block every Wednesday morning for writing tasks, and spend that time period on any "next" writing tasks that need to be done. In a team, you might assign some days to be "meeting days", and some days to be "focused work days".

Here are some examples of planning tasks on the calendar:

* Planning tasks on calendar: https://www.macsparky.com/blog/2018/2/hyper-scheduling-mechanics
* Planning on calendar: https://blog.usejournal.com/calendar-in-stead-of-to-do-lists-9ada86a512dd?gi=ffa2a66947a4 


### Focusing on a few tasks

Another caveat is to plan too many tasks at the same time, which requires switching attention often, and increases the total time until each individual task is complete. When there are interdependencies between tasks, this can delay the completion of a project. 

A way to counteract this is the Kanban principle, which originates from assembling cars as efficiently as possible. The idea is to focus on a few things, and first finish what you started, before picking up the next task. A good visual way to illustrate this principle, is a board where each task is a card/post-it, and there are several vertical sections into which tasks are divided: 

* Backlog/ideas - tasks you might want to do in the future
* Next - tasks you will do the next day, or the next sprint
* Doing - tasks you have started
* Done - tasks that are done

Any ideas should go into "Backlog", which is similar to the capture part of Getting Things Done. Then, every planning session you can select which tasks need to be done by moving them to "Next". When a team member picks up a task, it is moved into "Doing". The goal is to have as few as possible tasks in the "Doing" category. Only after a team member moves a task to "Done", they can start on another task from "Next". Other ideas that come up have to go in "Backlog" and discussed in the next planning session first. 

The same principle can also be applied on the level of projects. For example if you are involved in co-authoring multiple papers, you might want to focus on one or two papers first and submitting them before moving onto others, rather than contributing to five in parallel. 

Here are some examples of the Kanban principle in research projects:

* Kanban project management for PhD: https://www.linkedin.com/pulse/kanban-project-management-stem-phd-research-part-2-how-duc-phan/
* Kanban for research projects overall: https://veronikach.com/habits-productivity/keeping-track-of-your-research-projects-with-kanban/
* Kanban for research projects 2: https://md.ekstrandom.net/blog/2017/02/productivity-the-wall 



### Doing tasks

Now you should have a clearer picture of what needs to be done next and you have a task on your calendar (or several tasks in a themed day or time block). Perhaps this already takes away the biggest barrier from completing the task. If it is not enough, there are several strategies you can use to "just do it". 

A simple method for completing tasks is called the Pomodoro technique, based on a timer that is shaped like a tomato. The original idea is to set a timer for 25 minutes in which you work on one task, then have a 5 minute break. After several such Pomodoros, you can take a longer break. It is easy to adapt this method to other time intervals. 

An advantage of the Pomodoro technique is that you can do it in a group, even if everybody is working on different tasks, which creates some (social) pressure to focus. There are also various apps which can block distracting websites, helping you to concentrate.  

Other ideas for getting into the flow include using some background noise such as Coffivity (sound of a cafe), or a playlist that you also listen to during work. 




## Tools 

To implement the principles above with a team you will need the following shared tools:

* Task list
* Calendar
* Reference

Having specific places you use for each of these, is helpful in getting everybody up to speed on what is happening, and to avoid any confusions. It also helps to avoid duplication of effort. For example, a shared task list can help to avoid questions like "I thought you were supposed to do that". A shared reference folder can help you to avoid reading the same documents twice, or asking the same "frequently asked questions". Finally, a designated communication channel can reduce the time spent searching for various bits of information.  

###  Shared task list

A shared task list ensures that everybody knows what is needed to complete the project (or even individual projects!) and thus what is everybody working on. 

For software projects, a natural way to manage the todo list might be via Github issues. This set of slides gives more background on how to do this: https://merely-useful.github.io/mrsp/02-workflow.html#1  

If you prefer a board, Github issues can be imported as cards under the Projects tab in Github. Here you can add both existing issues, and "simple" cards. You can use these simple cards (which do not have functionality like milestones, tags and so forth) for tasks which do not have to do with the software part of your project, for example buying beans for the coffee machine. 

Here are examples for using Github for project management:

* https://everhour.com/blog/project-management-using-github/

If Github is not a logical choice, other todo list apps, such as Todoist, allow shared lists, and have great options for capturing and sorting tasks. Here is an example in Todoist: https://marcjenkins.co.uk/todoist-the-filters-i-use/ 


### Shared calendar

Similar to the task list, it can be helpful to have one or more shared calendars:

* Group meetings - rather than inviting everyone each time, have people subscribe to a shared calendar. It should be clear from the calendar, or the how-to guide to use it, which meetings are required for whom. 
* "Maybe" calendar - events which might be interesting to the team, but presence is not expected, such as interesting webinars. This is to ensure that the group meetings calendar has the essential meetings only.  
* "Away" calendar - when you are NOT available (deadline, conference), add a whole day event so you are not disturbed. This should not be done in the same calendar as group events, so these can be toggled on and off. 
* Time slot reservations. People who have multiple one-on-one meetings can have recurrent time slot meetings, which others can edit to sign up for a meeting. 

Outlook and Google Calendar are popular choices for calendars, and support integrations with todo-list apps. Tools like Calendly can facilitate time slot reservations in a calendar, and integrate with either system. 


### Shared reference system

Although not strictly a part of task planning, it is worth mentioning a shared reference system here. The idea of a shared reference system is to give everybody access to the same information, and to avoid duplication. Some examples of information you might want to include here are:

* A guide how to use the task planning systems 
* How to setup various software
* Manuals for any hardware
* (Summaries of) important papers to read in your field
* Technical reports produced by the lab

On Github you could store such information in the Wiki tab, alternatives are apps like Google Drive, Evernote and others. You might want to ensure that your task list is able to link to these documents. This way, team members could repeat frequently-used lists of tasks, such as everything needed for starting in the team. Here is an example of an onboarding list in Todoist: https://blog.doist.com/how-to-onboard-new-hires-using-todoist-and-twist-b2011753ad0f 


### Tool integrations

Various apps integrate one of more of these functionalities. However different team members might already be using other systems, which can cause forgetting tasks or calendar conflicts. To circumvent this problem, it is good to know that many apps allow integrations with others. For example, if the shared system is in Todoist, but somebody prefers Google Tasks, an integration to sync these can be set up. If there is no "ready made" integration, often it is possible to set up via IFTTT (IF This Then That https://ifttt.com/home) or Zapier (https://zapier.com/). 

Another use case for tool integrations is to automate some task-list-generation processes. For example, if person A is responsible for reviewing some files that person B is going to place in a Google Drive folder, it is possible for a "Review files" to be created automatically on A's todo list, once B updates the folder.   

