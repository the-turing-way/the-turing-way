# Limitations and best practices

## Table of contents

- [Limitations of CI](#Limitations_of_CI)
- [Best practise for continuous integration](#Best_practise_for_continuous_integration)
  - [Small, iterative changes](#Small_iterative_changes)
  - [Trunk-based development](#Trunk_based_development)
  - [Keep the building and testing phases fast](#Keep_the_building_and_testing_phases_fast)
  - [Computational expense](#Computational_expense)
  - [Dependencies tracking](#Dependencies_tracking)
  - [Consistency throughout the pipeline](#Consistency_throughout_the_pipeline)

<a name="Limitations_of_CI"></a>
## Limitations of CI

CI does have its limitations. Firstly it is only as effective at finding bugs as the tests provided to it. If a project contains few or poor tests then it is entirely possible the project will contain bugs the tests do not catch and Travis will report the build as successful.

Secondly, depending on the nature of your project there may be security considerations to think about.

Travis CI obfuscates secure environment variables and tokens displayed in the user interface. The [documentation about encryption keys](https://docs.travis-ci.com/user/encryption-keys/) outlines the build configuration required to set this up. However, if secret information is outputted in the course of running a script (for example in an error message) it may be included in Travis's build logs which may be accessible by others. To prevent leaks like this, secure environment variables and tokens that are longer than three characters are automatically filtered at runtime, effectively removing them from the build log, displaying the string `[secure]` instead. Nevertheless you should rotate your tokens and secrets regularly.

 However there are still many ways in which secure information can accidentally be exposed. These vary according to what tools you are using and the settings enabled. Some things to look out for are:

- Settings which duplicate commands to standard output, such as `set -x` or `set -v` in your bash scripts
- Displaying environment variables, by running `env` or `printenv`
- Printing secrets within the code, for example `echo "$SECRET_KEY"`
- Git commands like `git fetch` or `git push` may expose tokens or other secure environment variables
- Settings which increase command verbosity

Preventing commands from displaying any output is one way to avoid accidentally displaying any secure information. If there is a particular command that is using secure information you can redirect its output to `/dev/null` to make sure it does not accidentally publish anything, as shown in the following example:
```
git push url-with-secret >/dev/null 2>&1
```

If your project is set up such that each time a pull request is made on GitHub Travis tests that pull request there is an additional concern. If your tests require authentication credentials someone could make a pull request with malicious code to expose them. Therefore it is a good idea not to allow pull requests to automatically trigger Travis if you have such authentication requirements.

<a name="Best_practise_for_continuous_integration"></a>
## Best practise for continuous integration

<a name="Small_iterative_changes"></a>
### Small, iterative changes

One of the most important practices when adopting continuous integration is to encourage project members to make and commit small changes. Small changes minimise the possibility and impact of problems cropping up when they're integrated, which minimises the time and effort cost of integration.

<a name="Trunk_based_development"></a>
### Trunk-based development

With trunk-based development, work is done in the main branch of the repository or merged back into the shared repository at frequent intervals. Short-lived feature branches are permissible as long as they represent small changes and are merged back as soon as possible.

The idea behind trunk-based development is to avoid large commits that violate of concept of small, iterative changes discussed above. Code is available to peers early so that conflicts can be resolved when their scope is small.

<a name="Keep_the_building_and_testing_phases_fast"></a>
### Keep the building and testing phases fast

Because the build and test steps must be performed frequently, it is essential that these processes be streamlined to minimise the time spent on them. Increases in build time should be treated as a major problem because the impact is compounded by the fact that each commit kicks off a build.

When possible, running different sections of the test suite in parallel can help move the build through the pipeline faster. Care should also be taken to make sure the proportion of each type of test makes sense. Unit tests are typically very fast and have minimal maintenance overhead. In contrast, automated system or acceptance testing is often complex and prone to breakage. To account for this, it is often a good idea to rely heavily on unit tests, conduct a fair number of integration tests, and then back off on the number of later, more complex testing.

### Computational expense

Some software will require significant compute resource to build and/or run. Examples include weather and climate models. This can make the use of continuous integration impractical as the tests either take too long or use too much resource. Therefore, a compromise needs to be found to balance the risk of incomplete testing against a usable development process.

One approach is to use different levels of testing, with different subgroups being required depending on what is being changed. A common broad subgroup can be used in every case, with additional ones being invoked to test certain areas in more detail. This introduces an element of judgement to the testing process, but can be applied successfully.

<a name="Dependencies_tracking"></a>
### Dependencies tracking

Checking for dependency updates should be done regularly. It can save a lot of time, avoiding bugs due to code dependent on deprecated functionality. Services such as [David](https://david-dm.org/) are available for dependency management.

<a name="Consistency_throughout_the_pipeline"></a>
### Consistency throughout the pipeline

A project should be built once at the beginning of the pipeline, the resulting software should be stored and accessible to later processes without rebuilding. By using the exact same artefact in each phase, you can be certain that you are not introducing inconsistencies as a result of different build tools.

Also, the environment defined by the `.travis.yml` file should reflect the actual environment the code is run in. If that environment is modified don't forget to update the `.travis.yml` file, otherwise the results Travis returns will not be trustworthy.
