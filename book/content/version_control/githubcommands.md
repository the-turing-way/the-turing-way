## Summary of key Git commands

| Command                       | Use                                                                      |
| ----------------------------- | ------------------------------------------------------------------------ |
| git init                      | Initialises a Git repository in that directory                           |
| git add .                     | Add all changes to the staging area to be committed                      |
| git add file_name             | Add changes to the specified file to the staging area to be committed    |
| git commit                    | Commits staged changes and allows you to write a commit message          |
| git checkout SHA              | Check out past commit with the given SHA                                 |
| git checkout SHA -- file_name | Check out past version of a file from the commit with the given SHA      |  
| git checkout -b branch_name   | Create and switch to a new branch                                        |
| git checkout branch_name      | Switch to a specified branch                                             |
| git merge branch_name         | Merge the branch you are on into the specified branch                    |
| git clone url                 | Makes a clone of the repository at the specified url                     |
| git remote add origin url     | Links local repository and repository at the specified url               |
| git push origin branch_name   | Push local changes to the specified branch of the online repository      |
| git pull origin branch_name   | Pull changes to online repository into local repository                  |
| git log                       | Output a log of past commits with their commit messages                  |
| git status                    | Output status including what branch you're on & what changes are staged  |
| git diff                      | Output difference between working directory and most recent commit       |
| git diff thing_a thing_b      | Output difference between two things e.g. commits, branches              |                     


