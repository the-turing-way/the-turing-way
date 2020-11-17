(rr-ci-github-actions)=
# Continuous integration with GitHub Actions
GitHub Actions is a task automation system fully integrated with GitHub. It is not explicity used for continuous integration (CI) but it can make makes it easier than ever to incorporate CI into the repositories. 

## Getting started with GitHub Action
If you want to get started with GitHub Actions, you canstart by clicking the "Actions" tab in the repository where you want to create a workflow.


## GitHub related Vocab
<!-- (I'll explain each vocab separately using diagrams made with adobe illustrator) -->

1. WorkFlow
<!-- needs paraphrasing -->
The workflow is an automated procedure that you add to your repository. 
Workflows are made up of one or more jobs and can be scheduled or triggered by an event. 
The workflow can be used to build, test, package, release, or deploy a project on GitHub.


2. Action
<!-- needs paraphrasing -->
An action is a specific activity that triggers a workflow. For example, activity can originate from GitHub when someone pushes a commit to a repository or when an issue or pull request is created. You can also use the repository dispatch webhook to trigger a workflow when an external event occurs. For a complete list of events that can be used to trigger workflows, see Events that trigger workflows.


3. Steps 
<!-- needs paraphrasing -->
A step is an individual task that can run commands in a job. A step can be either an action or a shell command. Each step in a job executes on the same runner, allowing the actions in that job to share data with each other.


## Building a block of a WorkFlow
1. name
2. on
3. env
4. jobs
5. steps

## Use Cases
