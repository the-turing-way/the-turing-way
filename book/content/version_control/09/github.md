## GitHub

### The problem

When multiple people work on the same project (which is becoming more and more common as research becomes increasingly collaborative) it becomes difficult to keep track of what changes have been made and by who.
It is also often difficult and time-consuming to manually incorporate the different participant's work into a whole even if all of their changes are compatible.  

### The solution

Hosting the project on a distributed version control system such as GitHub.
Collaborators can then clone the project and work on that copy making commits, branches, etc without impacting the original. 
Collaborators can then *push* their work to each other, and *pull* other's work into their own copy.
In this way it is easy to keep everyone up to date and to track what has been done and by who.
GitHub also has numerous other handy features such as the ability to raise and assign issues, discuss the project via comments, and review each other's changes.

Making the entire project and its history available online in this was also has two major benefits for research:

1. Other researchers can re-use the work more easily.
Rather than writing their own code to do what has already been written they can just use the original, which saves time.
This also benefits the project's original authors as other researchers are much more likely to build on the work (and cite it) if a great deal of the work has already been done.   
2. The research will be much more reproducible if the entire history of the project can be tracked. This enables results to be verified more easily, which benefits science.

### How to do it

There are a number of GitHub tutorials available such as [this one](https://guides.GitHub.com/activities/hello-world/), or if you prefer you can follow along here.

First make an account on [GitHub](https://GitHub.com/), and create a repository on it.
To do this click the + sign dropdown menu in the upper right hand of the screen.
Enter a name for the repository (ideally the same name as the project folder on your computer) and click Create Repository. 
Now you just need to link the project on your computer to this online repository.
If your project is not already version controlled then make it so by running `git init` and making a commit.
In the terminal on your computer use:

```
git remote add origin https://GitHub.com/your_username/repository_name
```

then *push* all the files on your computer to the online version so they match via:

```
git push -u origin master
```

You can the go on and make more commits on your computer.
When you want to push them to your online version similarly you do:

```
git push origin branch_you_want_to_push_to
```

Others can then clone the repository to their computer by using:

```
git clone https://GitHub.com/your_username/repository_name.Git
```

They can make and commit changes to the code without impacting the original, and push their changes to *their* online GitHub account using:

```
git push -u origin master
```

Naturally the exact same procedure applies to you if you want to clone someone else's repository.

#### Pull requests

So everyone's got a copy of the code and they're merrily working away on it, how do collaborators share their work?
Pull requests.
A pull request is a request for a person to *pull* someone else's changes into their version on the project.
Say person A has made changes they want to share with person B.
On GitHub Person A needs to go to person B's copy of the project and click the "New pull request" button.
From there they can indicate which of their branches they would like person B to pull changes from, and which branch they want the changes pulled to.
If person B accepts then person A's changes will be merged into their repository by GitHub.
They can discuss the request in comments, and make further commits to the request before it is accepted if necessary.

When person B is setting up the pull request GitHub will automatically check whether there would be any merge conflicts if they accept, and highlight them if there are.
These can then be resolved in further commits before the request is accepted, keeping the merge clean and painless.

Once the request is accepted GitHub will merge person A's changes into person B's online copy of the repository.
Person B can the *pull* those changes down to the copy on their computer using:

```
git pull origin master
```

It is also possible to make pull requests via the command line.
A guide on how to do so is available [here](https://Git-scm.com/docs/Git-request-pull).

### Good practice

In your GitHub repository you should **include a license** to allow others to re-use your work legally.
GitHub makes this very easy, simply click the "Create new file" button, name it "License.md" and a drop down menu will appear offering you a selection to choose from. The legalese can seem intimidating however [this](https://choosealicense.com/) website offers a very simple mechanism to help you pick the best license for your project.

You should also **include a readme file** where you include useful information about what the project is, how to use it and how to contribute to it.
Switching between projects in your work is common, let alone that you might need to poke at your own previous projects from time to time.
This information will also assist you collaborators, and your future employer might want to check your existing GitHub projects.

There are plenty of readme templates available online, pick one you like, but here is a list of the main things a readme should include:

- The project name and what it is: This will greatly help the random prospective contributor to get an idea of the project. 
Include a few key points that describe the main features of the project and what are the main features you are implementing.
This helps to quickly compare other projects with yours and to give an idea that why the project exists in the first place.
- Instructions on how to install the project: The installer might be a collaborator, someone that comes across and is interested in the project, or even you if you get a new machine and need to re-install your project.
Nevertheless, it's a total waste of both of your resources to start figuring out how to just get started with the project. 
This should also include any prerequisites that will be needed to run the project.
The best thing you can do is to just write up the installation instructions when you first do them yourself, and you will quickly save hours of work in the future.
- Instructions for how to run the project and any associated tests: If you have been working on your project it may seem obvious how to run it, but this will likely not be the case for someone coming across it for the first time.
- Links to related material.
- List of authors/contributors to the project, possibly with contact information.
- Acknowledgements.

It can be a good idea to **include documents outlining a code of conduct, agreed ways of working, and contributing guidelines**, though depending on the level of detail you want to provide the latter two can also work as sections within the readme.
These documents make explicit expectations for those working on/contributing to the project, making life easier for everyone. 
Similarly depending on the scope of your project you may wish to **provide templates for how contributors should make pull requests or raise issues**.

You can also **make use of one of GitHub's major features- issues**.
Anyone can raise an issue with the project and discuss it.
By making issues for any significant changes a record can be kept of the history of the project.
GitHub has a myriad of other features such a milestones and project boards which may also be of use.

In pull requests you should **clearly explain what the changes you've made are and why you made them**.
If your changes address and issue that has been raised reference it directly.
If your request fixes and issue and you include "will fix #the_issue_number >" in the pull request, if the pull request is merged it will automatically close the referenced issue, keeping the issue queue nice and clean!
This also works for using commit messages to close issues too.

