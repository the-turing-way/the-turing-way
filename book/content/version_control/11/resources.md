## Checklists

### Make use of Git
- [ ] Make your project version controlled by initialising a Git repository in its directory using `git init`.
- [ ] Add and commit all your files to the repository using `git add .` then `git commit`.
- [ ] Continue to add and commit changes as your project progresses. Stage the changes in specific files to be committed with `git add filename`, and add messages to your commits.
  - [ ] Each commit should make one simple change.
  - [ ] No generated files committed.
  - [ ] Commit messages are meaningful, with a ~50 character summary at the top.
  - [ ] Commit messages are in the present tense and imperative.
- [ ] Develop new features on their own branches, which you can create via `git checkout -b branch_name` and switch between via `git checkout branch_name`.
  - [ ] Branches have informative names.
  - [ ] Master branch is kept clean.
  - [ ] Each branch has a single purpose and only changes related to that purpose are made on it.
- [ ] Once features are complete merge their branches into the master branch by switching to the feature branch and running `git merge master`.
  - [ ] Merge other's changes into your work frequently.
  - [ ] When dealing with merge conflicts make sure you fully understand both versions before trying to resolve them.

### Put your project on GitHub
- [ ] Create a GitHub account.
- [ ] Create a repository on GitHub with the same name as your project.
- [ ] Attach your local and online repositories via `git remote add origin repository_url`.
- [ ] Put the files in your local version of the project online via `git push -u origin master`.
- [ ] Continue to push changes you make on your computer to the GitHub version via `git push origin branch_name`.
- [ ] Pull any changes made on GitHub to your local version via `git pull origin branch_name`.
- [ ] Include a license.
- [ ] Include a readme.
- [ ] Set expectations for how collaborators are expected to behave via a code of conduct and or ways of working document.
- [ ] Use issues to track and discuss modifications to the project.

### Contribute to someone else's project
- [ ] Clone their project's repository from GitHub `git clone repository_url`.
- [ ] Make and commit changes.
- [ ] Push your changes to you GitHub version of the project.
- [ ] Make use of issues to discuss possible changes to a project.
- [ ] Make pull requests on GitHub to share your work.
  - [ ] Clearly explain the changes you've made and why in your pull request.


## What to learn next

Look into best practice for writing good quality code (for example, good naming conventions, informative comments, modular code structure).
Many such skills are either also applicable for using version control well, for example, for writing good commit messages, or make using version control easier by keeping changes neat and localised.

## Further reading

- A free and very in depth book on Gits myriad of features can be found [here](https://Git-scm.com/book/en/v2).
- A useful Git cheat sheet can be found [here](https://services.GitHub.com/on-demand/downloads/GitHub-Git-cheat-sheet.pdf).
- Interactive tutorials for familiarising yourself with GitHub can be found at [https://lab.github.com/](https://lab.github.com/).

## Definitions/glossary

- **Add:** Command used to add files to the staging area. Allows the user to specify which files or directories to include in the next commit.
- **Branch:** A parallel version of a repository. Although it is contained within the same repository it allows you to develop it separately and then merge changes back into the 'live' repository or with other branches when appropriate.
- **Checkout:** Git command to switch to a specific file, branch, or commit. Allows you to activate older versions of files or commits or switch between active branches.
- **Clone:** Copy of an existing Git repository, normally from some remote location to your local environment. When you clone a repo you copy its entire history as well as all branches.
- **Commit:** Snapshot of project history. A commit can be made after changes of a single file or a range of files and directories.
- **Commit message:** A message the user can attach to a commit to explain what it contains.
- **Git:** Version control system that GitHub is built around. It is a widely used open source distributed version control system developed by the author of Linux.
- **GitHub:** An online hosting and version control service which centres around the version control software Git. It has a great many features to aid collaboration between users.
- **HEAD:** the latest commit on the branch which is currently checked out
- **Issues:** Bug tracking system for GitHub. Collaborators can use issues to report bugs, request features, or set milestones for projects. Issues are tracked, reported, and closed by collaborators during the development process. They’re a great way of communicating with your team and reporting progress.
- **Master:** the repository’s main branch. Depending on the work flow it is the one people work on or the one where the integration happens.
- **Merge:** The process of combining branches. Changes made on one or more branches are applied to another.
- **Merge conflict:** Incompatibilities between branches being merged.
- **Pull request:** Proposed changes to a remote repository. Collaborators without write access can send a pull request to the administrator with the changes they've made to the repo. The administrator can then approve and merge or reject the changes to the main repository. For open source projects pull requests can be sent by anyone that has forked a project.
- **Push:** Sending changes to a remote repo. The remote repository is updated with the changes pushed and now mirrors the local repo.
- **Repository:** Refers to a project folder that is being tracked by Git and containing project files. Also called 'repo' for short they can be local as well as hosted on GitHub.
- **SHA:** Unique string of numbers of letters used to identify every commit or node in the repository.
- **Staged:** Changes that will be included in the next commit.

## Bibliography

- [1.](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Controls) **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License**
- [2.](https://link.springer.com/article/10.1186/1751-0473-8-7) **Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0)** *Other useful stuff in this paper, could use their into as part of the book's intro*
- [3.](http://crlionline.net/node/198) **Permission to use given by the author (Peter Reimann) 15/12/18**
- [4.](https://tonysyu.github.io/source-control-for-scientists-and-soloists.html#.XA6Q3mj7RPY) **Permission given by the author (Tony Yu) 15/12/18**
- [5.](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter) **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.**
- [6.](https://githowto.com/undoing_committed_changes) **creative commons Attribution-NonCommercial-ShareAlike 4.0 International**
- [7.](https://www.atlassian.com/git/tutorials/saving-changes/git-diff) **Creative Commons Attribution 2.5 Australia License.**
- [8.](http://sethrobertson.github.io/GitBestPractices/) **Creative Commons Attribution-ShareAlike 3.0 Generic**
- [9.](https://guide.esciencecenter.nl/best_practices/version_control.html) **Creative Commons Attribution 4.0 International License**
- [10.](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project) **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License**
- [11.](https://opensource.com/article/18/5/git-branching) **Creative Commons license**
- [12.](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches) **GNU GENERAL PUBLIC LICENSE Version 3**
- [13.](http://genomewiki.ucsc.edu/index.php/Resolving_merge_conflicts_in_Git) **["You are granted a limited license to copy anything from this site"](http://genomewiki.ucsc.edu/index.php/Genomewiki:General_disclaimer)**
- [14.](https://githowto.com/resolving_conflicts) **creative commons Attribution-NonCommercial-ShareAlike 4.0 International**
- [15.](https://opensource.com/article/18/1/step-step-guide-git) **Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**
- [16.](https://kbroman.org/github_tutorial/pages/init.html) **Attribution 3.0 Unported (CC BY 3.0)**
- [17.](https://opensource.com/article/18/2/how-clone-modify-add-delete-git-files) **Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**
- [18.](https://thejunkland.com/blog/how-to-write-good-readme.html) **Creative Commons Attribution-NonCommercial 2.5 License**
- [19.](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) **MIT**
- [20.](https://commons.wikimedia.org/wiki/Taj_Mahal#/media/File:Taj_Mahal_in_March_2004.jpg) **GNU Free Documentation License**
- [21.](https://juristr.com/blog/2013/04/git-explained/) **Creative Commons Attribution-ShareAlike 4.0 International License**
- [22.](http://simpleprimate.com/github-for-web-designers/glossary.html) **Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**
