(rr-vcs-git-summary)
# Summary Table of Git Commands

| Command                       | Use                                                                      |
| ----------------------------- | ------------------------------------------------------------------------ |
| `git init`                      | Initialises a Git repository in that directory                           |
| `git add .`                     | Adds all changes to the staging area to be committed                      |
| `git add file_name`             | Adds changes to the specified file to the staging area to be committed    |
| `git commit`                    | Commits staged changes and allows you to write a commit message          |
| `git checkout SHA`              | Checks out a past commit with the given SHA                                 |
| `git checkout SHA -- file_name` | Checks out the past version of a file from the commit with the given SHA      |
| `git checkout -b branch_name`   | Creates and switches to a new branch                                        |
| `git checkout branch_name`      | Switches to the specified branch                                             |
| `git merge branch_name`         | Merges the branch you are on into the specified branch                    |
| `git log`                       | Outputs a log of past commits with their commit messages                  |
| `git status`                    | Outputs status, including what branch you are on and what changes are staged  |
| `git diff`                      | Outputs the differences between the working directory and most recent commit       |
| `git diff thing_a thing_b`      | Outputs the differences between two things, such as commits and branches       |
| `git clone URL`                 | Makes a clone of the repository at the specified URL                     |
| `git remote add origin URL`     | Links a local repository and an online repository at the specified URL               |
| `git push origin branch_name`   | Pushes local changes to the specified branch of the online repository      |
| `git pull origin branch_name`   | Pull changes from the online repository into local repository      
