# Building a Block of a Github Actions

As decribed previosly, Workflow files use YAML syntax, which have either a `.yml` or `.yaml` file extension. If you're new to YAML and want to learn more, [see our section about YMAL here](https://the-turing-way.netlify.app/reproducible-research/renv/renv-yaml.html?highlight=yaml). This workflow is stored in the `.github/workflows` directory of your repository.


**1. name**

This is the name of the workflow. GitHub will use this name to be displayed on the repository's actions page.
```
name:
     test package
```

**3. on**

The `on` field tells GitHub Actions when to run. For exmple, we can run the workflow anytime there's a `push` or a `pull`.
```
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
```
There are many events which can be used to trigger a workflow. You can explore them [here](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions).

**5. jobs**

Any workflow is consisted of one or more jobs. Every job also runs in an environment specified by`runs-on`. These Jobs run in parallel by default but can also be defined to run sequentially.
```
Jobs:
    runs-on: ubuntu-latest
```
This block defines the core component of an Actions workflow. Workflows are made of `jobs`. Every job also needs a specific host machine on which to run, the `runs-on:` field is how we specify it. The template workflow is running the `build` job in the latest version of Ubuntu, a Linux-based operating system.

We can also separate the `build` and `test` functions of our workflow into more than one job that will run when our workflow is triggered.

```

jobs:
  build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v2
  test:
    - name: npm install, and test
    run: |
      npm install
      npm test
    env:
      CI: true
```
**7. steps**

It is the linear sequence of operations that make up a job.
- `uses: actions/checkout@v1`: uses a community action called [`checkout`](https://github.com/actions/checkout) to allow the workflow to access the contents of the repository
- `uses: ./action-a` : provides the relative path to the action we created in the `action-a` directory of the repository
- `with`: is used to specify the input variables that will be available to your action in the runtime environment. In this case, the input variable is `MY_NAME`, and it is currently initialized to `"Mona"`.

Providing a comprehensive guide of all the available options is beyond the scope of this overview, and instead we would urge you to study the CI configuration of well established open source projects.
