### Task management

Content/draft for issue https://github.com/alan-turing-institute/the-turing-way/issues/1436

TODO some text here on why this is important for reproducible data science teams. 


## Contents

* What is a task - levels of abstraction
* What is a good format and size of a task
* Where should tasks "live"
* Systems like GTD, Kanban
* Planning, setting priorities (and avoiding overwhelm)
* How to communicate this with team members

There are some similarities here to creating Github issues, but this idea is more general and focuses more on conventions/agreements with team members, than on working with specific tools.

__Most of the text below is needs to be reorganized__.


## What is a task 

There are different levels at which tasks exist - at the lowest level tasks can be done in a few minutes, and at the highest level tasks are actually projects, which again have tasks. Some good ways to think about tasks are:

* Use a verb when defining a task. Rather than "literature review", add "read 5 papers" to your list. 
* Define what it means to be done with a task. Rather than "read 5 papers", you could use "write 100-word summaries for 5 papers"
* If you do not think you could finish a particular task if you just start it and give yourself a couple of hours to do it, you probably need to break it down into smaller tasks

If you are creating tasks for yourself, it is tempting to skip some of these steps because "you know what you mean" when you write down "literature review". But even if you are not working in a team, it can help you if you are crystal clear. Your current "manager" self can delegate tasks to your future "maker" self, who only has to do the task without having to figure out where to start.  


### Sorting tasks 

If you are good at capturing tasks that need to be done, you will probably end up with a lot of tasks. To avoid getting overwhelmed and doing everything at the same time, you will need to decide if, and when, to do the tasks you have captured. There are several ways to help you think about this, but most of of them can be seen as assigning different tags to each task. These tags can be related to:

* A specific date that the task must be complete
* A priority. The Einsenhower matrix is a tool to categorize each task into four categories: urgent & important, not urgent & important, urgent & not important, not urgent & not important. The caveat is to only end up doing the urgent tasks, but not creating time for the "not urgent & important ones". 
* How long you estimate the task will take (minutes/hours/...) 
* Context-dependent things you need to do the task, such as being at the office.  
* How much energy you need to do the task. 

### Kanban

Not a system but more a philosophy. Kanban principle, originates from building cars. The idea behind Kanban is to “manage work by balancing demands with available capacity” (Wikipedia). The goal is to not do too many things at the same time, and finish first what you started working on. 

Tasks progress from left to right in time, for example: 

* Backlog/ideas - things to maybe do in the future
* Next - tasks you will do the next day, or the next week
* Doing - tasks you have started - this column needs to have as few tasks as possible! 
* Done - tasks that are done
* Dropped / "won't fix" - tasks which you decide do not need to be done

The same principle can be applied on the level of projects. For example if you are involved in co-authoring multiple papers, you might want to focus on two papers first and submitting them before moving onto others, rather than contributing to five in parallel. 

__TODO more on not urgent & important__

### Doing tasks

Now you should have a clearer picture of what needs to be done next. In a scrum setting, you could pick several tasks to do in the next sprint. You could also plan the tasks as appointments on your calendar. Next to already blocking out the time you need to do the task, this can help you get better at estimating how long each task should take. An alternative to planning each individual task on your calendar, is having some themed days or time blocks. For example you can block every Wednesday morning for writing tasks, and spend that time period on any "next" writing tasks that need to be done. 

In a team, likely everybody will have tasks they need to work on individually, vs meetings with with others. It might be efficient to designate different days or times as "meeting times" vs "deep work" times, so that everybody can have uninterrupted blocks of time. 

"Deep work" times can be done in a group too - shared pomodoro? With cuckoo clock

## Systems / project "pulse"

Switching between managing and doing - assuming you are a team member yourself. How often do you check in with the whole team, when do you plan things, when do you evaluate results. 

### GTD

Getting Things Done by David Allen, approach to task management initially intended for individuals, although the principles can be applied more broadly. Overall it comes down to two steps:

* Capture - as soon as something comes up, put it inside your system 
* Process - sort and organize your tasks so that you know what you need to focus on next. This can be done at different levels, but an important one is every week, also called weekly review, during which you sit down and go through a checklist.  


### Scrum

Type of process frequently used in software development (more background here). Traditionally in this process, a team is working on the same project. Sprint every two weeks, plan tasks, do tasks using scrum board. Every day stand-up to see if there are any issues, who needs to help whom, 15 minutes. Retrospectives to evaluate. 

In a research setting this might be less applicable if each person is working on their own project, and the timing might be slower due to experiments, for example. However principles can still be adapted to a research setting, examples:  

* http://www.cs.umd.edu/~mwh/papers/score.pdf
* https://psyarxiv.com/zg4ub
* https://veronikach.com/phd-advice/organizing-student-projects-with-scrum/




## Tools 

You need:

* Task list
* Calendar
* Reference
* Communication channel __TODO:__ check with communication chapter to reduce overlap

Having specific places you use for each of these, is helpful in getting everybody up to speed on what is happening, and to avoid any confusions. It also helps to avoid duplication of effort. For example, a shared task list can help to avoid questions like "I thought you were supposed to do that". A shared reference folder can help you to avoid reading the same documents twice, or asking the same "frequently asked questions". Finally, a designated communication channel can reduce the time spent searching for various bits of information.  

###  Shared task list

Everybody knows what is needed to complete the project (or even individual projects!) and thus what is everybody working on. This can be managed via a variety of apps such as Todoist, Notion, Trello or Github.

For software projects, a natural way to manage the todo list might be via Github issues. This set of slides gives more background on how to do this: https://merely-useful.github.io/mrsp/02-workflow.html#1

If you prefer a Kanban-like todo list, Github issues can be imported as cards under the Projects tab in Github. Here you can add both existing issues, and "simple" cards. You can use these simple cards (which do not have functionality like milestones, tags and so forth) for tasks which do not have to do with the software part of your project, for example buying beans for the coffee machine. 

### Shared calendar

Similar to the task list, it can be helpful to have one or more shared calendars:

* Group meetings - rather than inviting everyone each time, have people subscribe to a shared calendar. It should be clear from the calendar, or the how-to guide to use it, which meetings are required for whom. 
* "Maybe" calendar - events which might be interesting to the team, but presence is not expected. For example, webinars people can sign up for. 
* "Away" calendar - when you are NOT available (deadline, conference), add a whole day event so you are not disturbed. This should not be done in the same calendar as group events, so these can be toggled on and off. 
* Time slot reservations. People who have multiple one-on-one meetings can have recurrent time slot meetings, which others can edit to sign up for a meeting. 

Outlook and Google Calendar are popular choices for calendars, but notoriously difficult to combine together. Tools like Calendly can facilitate time slot reservations in a calendar, and integrate with either system. 


### Shared reference / knowledge base

The idea of a shared reference system is to give everybody access to the same information, and to avoid duplication. Things you might want to have in such a system:

* Code of conduct
* Safety guidelines
* Onboarding, how to setup various software
* A guide how to use the shared systems 
* Manuals for any hardware
* (Summaries of) important papers to read in your field
* Technical reports produced by the lab
* ... 

An example of using Evernote to share research papers (and notes) with a team of students can be found here: https://veronikach.com/habits-productivity/how-to-share-papers-with-your-students-in-evernote/

Again, there are a lot of places you could keep such information. In Github you could do this via markdown documents or the Wiki tab. Storing notes or PDFs in Evernote, Notion, Google Drive and others could also work depending on your project. 

### Tool conflicts

Various apps integrate one of more of these functionalities. However different team members might already be using other systems, which can cause forgetting tasks or calendar conflicts. To circumvent this problem, it is good to know that many apps allow integrations with others. For example, if the shared system is in Todoist, but somebody prefers Google Tasks, an integration to sync these can be set up. If there is no "ready made" integration, often it is possible to set up via IFTTT (IF This Than That https://ifttt.com/home) or Zapier (https://zapier.com/). 

