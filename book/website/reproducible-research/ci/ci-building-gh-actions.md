(rr-ci-building-gh-actions)=
# Building a Block of a Github Actions

As described previously, workflow files use YAML syntax, which has either a `.yml` or `.yaml` file extension.
If you're new to YAML and want to learn more, {ref}`see our section about YMAL<rr-renv-yaml>`.
This workflow files must be stored in the `.github/workflows` directory of your repository.

Each workflow is defined in a separate YAML. We will introduce the building block of a workflow using Hello World Example:

```
name:
    Hello World package
on:
  push:
    branches: [ main ]
Jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
```  

**1. name**

This is the name of the workflow and it is optional. GitHub will use this name to be displayed on the repository's actions page.
```
name:
    Hello World package
```

**2. on**

The `on` field tells GHA when to run. For example, we can run the workflow anytime there's a `push` or a `pull` on the `main` branch.
```
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```
There are many events which can be used to trigger a workflow. You can explore them [here](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions).

**3. jobs and steps**

This block defines the core component of an Action workflow. Workflows are made of `jobs`.
Every job also needs a specific host machine on which to run, the `runs-on:` field is how we specify it.
The template workflow is running the `build` job in the latest version of Ubuntu, a Linux-based operating system.

```
jobs:
  build:
  runs-on: ubuntu-latest
```

We can also separate the `build` and `test` functions of our workflow into more than one job that will run when our workflow is triggered. Jobs are made of `steps`.
These allow you define what to run in each job.
There are three ways to define steps.

- With `uses`
- With `run`
- With `name`

```

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
  test:
    steps:
    - name: npm install
      run: |
        npm install
        npm test
```

The most basic action is `actions/checkout@v3`.
This uses a GitHub provided action called [`checkout`](https://github.com/actions/checkout) to allow the workflow to access the contents of the repository.
All the steps of a job run sequentially on the runner associated with the job.
By default, if a step fails, the subsequent steps of the job are skipped. Each run keyword represents a new process and shell in the runner environment.
When you provide multi-line commands, each line runs in the same shell.

Providing a comprehensive guide of all the available options is beyond the scope of this overview, and instead, we would urge you to study [official reference documentation](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions) and/or the CI configuration open-source projects references in the previous section.
