# Checklist

- Have a project that you collaborate on with at least one other person
- Put the project on GitHub
- Have project members regularly commit their work to this central repository
- That project should have at least some tests
- Write a `.travis.yml` file which:
  - Sets out the operating system the project is run on
  - Defines the programming language and version of that language to run the project with
  - Includes code to install any dependencies required to run the project in a before_install step
  - Contains a script to run the project tests
- Commit the `.travis.yml` file to the project's GitHub repository
- Go to [travis-ci.com](https://travis-ci.com/) and sign in with GitHub
- Activate Travis on your project repository
- Each time a new commit is pushed Travis will run the tests and return the results. If these report that a commit causes test/tests to fail then find and fix the problem as soon as possible
