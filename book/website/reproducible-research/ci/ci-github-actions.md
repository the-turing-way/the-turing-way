(rr-ci-github-actions)=
# Continuous integration with GitHub Actions

## Getting started with GitHub Action
GitHub Actions is a task automation system fully integrated with GitHub.

## GitHub related Vocab
<!-- (I'll explain each vocab separately using diagrams made with adobe illustrator) -->
1. GitHub Action


2. WorkFlow
<!-- needs paraphrasing -->
This is the task (or tasks) you want to run automatically when triggered. A workflow is defined in a YAML file and contains all the steps that need to be run along with other information, such as the OS to run the job on and any dependencies that need installing. Another advantage of GitHub Actions over other CI vendors is that you can define as many workflow files as your project requires. Instead of one file that does lots of things, you can have a workflow file per task with it's own specific triggers.

3. Action
<!-- needs paraphrasing -->
An "action" is some code for a particular step that has been packaged up in such a way that it can be imported into your workflow. An example of an action is "Build and Push" from Docker. If you need to build a Docker image and push it to a registry during deployment, you can import this action to manage that process for you instead of installing docker and executing the build and push commands separately. Actions are available on GitHub Marketplace and are provided by official sources and third party developers. Creating your own action is also a possibility if you can't find one to suit your needs.

## Building a block of a WorkFlow (the practical part)
1. name
2. on
3. env
4. jobs
5. steps

## Use cases
