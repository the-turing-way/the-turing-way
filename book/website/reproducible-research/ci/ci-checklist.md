# Checklist

- Have a project that you collaborate on with at least one other person
- Put the project on GitHub
- Have project members regularly commit their work to this central repository
- That project should have at least some tests
- Write a `ci.yml` file which:
  - Must be inside `.github/workflows`
  - Define the name of the GitHub event that triggers the workflow using `on` key on the YMAL.
  - Defines a specific host machine on which to run the job using `jobs` and `runs-on`.
  - Includes code to install any dependencies required to run the project in a before_install step
  - Contains a script to run the project tests
- Commit the `ci.yml` file to the project's GitHub repository
- Each time a new commit is pushed Travis will run the tests and return the results. If these report that a commit causes test/tests to fail then find and fix the problem as soon as possible
