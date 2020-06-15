# Resources

## What to learn next

If you have not already read the testing chapter it is suggested to do so to learn more about the different kinds of tests and their benefits in order to make the most of CI.

## Further reading

Travis offers a great deal of functionality not described here for automating other processes related to the testing and deployment of projects. Look into these, the Travis [documentation](https://docs.travis-ci.com/user/deployment) offers a good starting point for this.

A list of example Travis builds and tests for various languages/frameworks is available [here](https://github.com/softwaresaved/build_and_test_examples).

Travis's official tutorial is [here](https://docs.travis-ci.com/user/tutorial/). A tutorial focussed on using Travis with R can be found [here](https://juliasilge.com/blog/beginners-guide-to-travis/), tutorials geared towards python can be found [here](https://docs.python-guide.org/scenarios/ci/) and [here](https://docs.travis-ci.com/user/languages/python/).

## Definitions/glossary

**Build:** A group of jobs. For example, a build might have two jobs, each of which tests a project with a different version of a programming language. A build finishes when all of its jobs are finished.

**Computational environment:** The environment where a project is run, including the operating system, the software installed on it, and the versions of both.

**Continuous integration:** The process of regularly combining the work of project members into a centralised version. Also called CI. CI software typically runs tests on the integrated version of a project to identify conflicts and bugs introduced by the integration.

**GitHub:** A widely used version control platform.

**Job:** An automated process that clones your repository into a virtual environment and then carries out a series of phases such as compiling your code and running tests. A job fails if the return code of the script encounters an error.

**Travis:** A commonly used continuous integration platform.

## Bibliography

### Materials used: What is continuous integration?

- [What is CI](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/for-beginners.md) **MIT**
- [SSI blog](https://software.ac.uk/using-continuous-integration-build-and-test-your-software?_ga=2.231776223.1391442519.1547641475-1644026160.1541158284) **Creative Commons Attribution Non-Commercial 2.5 License**
- [The difference between continuous integration, continuous deployment, and continuous delivery](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
- [CI with python](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**

### Materials used: What is Travis and how does it work?

- [Info about how Travis works](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/for-beginners.md) **MIT**

### Materials used: Setting up continuous integration with Travis

- [Light travis tutorial](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/tutorial.md) **MIT**
- [CI with travis](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported**
- [Installing dependencies via yaml](https://github.com/travis-ci/docs-travis-ci-com/edit/master/user/installing-dependencies.md) **MIT**
- [Testing multiple versions of programming languages](https://docs.python-guide.org/scenarios/ci/) **Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)**
- [Using Travis with multiple operating systems](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/multi-os.md) **MIT**
- [Travis docs: customising the build](https://docs.travis-ci.com/user/customizing-the-build/) **MIT**

### Materials used: Limitations of CI

- [Security with Travis](https://github.com/travis-ci/docs-travis-ci-com/blob/master/user/best-practices-security.md) **MIT**

### Materials used: Best practise for continuous integration

- [Continuous integration, continuous deployment and continuous delivery](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment) **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
- [Netherlands eScience Center guide](https://guide.esciencecenter.nl/best_practices/testing.html) **Creative Commons Attribution 4.0 International**

## Acknowledgements

Thanks to David Jones of the University of Sheffield RSE group for useful discussions.
