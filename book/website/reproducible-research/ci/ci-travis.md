(rr-ci-travis)=
# Continuous Integration with Travis

## Overview of Travis

In this chapter we will focus on [Travis](https://travis-ci.org/) because it's free (if your code is openly available), widely used, and well integrated with the version control platform [GitHub](https://github.com/).

To use Travis you will need to add a file to your project called `.travis.yml` which describes the computational environment to run the project in, and includes a script to run your tests.
See the chapter on reproducible computational environments for more information on them, including writing `.yml` files to specify them.
See the chapter on testing for information on writing and automating tests.
The `.travis.yml` file has a number of other capabilities, which will be described [later](#After_success) along with more [detailed instructions](#Setting_up_the_computational_environment) for writing these files.

Once Travis has been set up on a project then each time a commit is made it:

- Clones a copy of project
- Generates a copy of the computational environment specified in the `.travis.yml` file in a brand new virtual environment
- Builds the project within that environment
- Runs the tests by following the script specified in the `.travis.yml` file
- Reports the results
  - Travis will output the results of every step of building the environment and running the script as a log viewable in your account on the [Travis site](https://travis-ci.org/) (the dark grey box in the figure below).
  - Travis will attach a badge to the results, green if all steps in the script (which run the tests) pass, red if not. The badge will be yellow whilst Travis is still running. If Travis is unable to generate the computational environment described in the `.travis.yml` file then it will not proceed further and the badge will be grey. See the figures below which show the passing build badge and failing build badge in the readme of a GitHub repository.
  - Travis will also report the results via email (notification settings can be adjusted).

Here's what the Travis dashboard of a repository looks like:

```{figure} ../../figures/travis-build.png
---
name: travis-build
alt: A screenshot of what a Travis dashboard looks like when Travis has been set up on a project.
---
An example of a Travis dashboard.
```

Everything's green because the build is passing. Note the "build passing" badge at the top.
If you click that you will get a popup with a dropdown menu where you can select a way of copying the badge.
If you select "markdown" and copy and paste the code snippet it outputs into a markdown file in the project, then GitHub will display the badge in that file:

```{figure} ../../figures/travis-badge-pass.png
---
name: travis-badge-pass
alt: Travis badge showing a passed build.
---
The Travis badge is used as an indicator when the all the tests have passed.
```

If I deliberately create a bug and commit it then Travis automatically runs, the tests fail, and this badge automatically updates to "build failing":

```{figure} ../../figures/travis-badge-fail.png
---
name: travis-badge-fail
alt: Travis badge showing a failed build.
---
The Travis badge shows build error when any of the tests has failed.
```

You can use Travis to test your project in multiple computational environments my specifying them in the `.travis.yml` file.
A quick note on Travis vocabulary:

- Job - an automated process that clones your repository into a virtual environment and then carries out a series of phases such as compiling your code and running tests. A job fails if the return code of the script encounters an error.
- Build - a group of jobs.
For example, a build might have two *jobs*, each of which tests a project with a different version of a programming language.
A build finishes when all of its jobs are finished.
