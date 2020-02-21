## Release

Releases are a way to mark or point to a particular milestone in software development. This is useful for users and collaborators, e.g. I found a bug running version x. For publications that refer to software, refering to a specific release enhances the reproducability. 

[Apache foundation](http://www.apache.org/) describes their [release policy](http://www.apache.org/dev/release.html).

Release cycles will depend on the project specifics, but in general we encourage quick agile development: *release early and often*

### Semantic versioning

Releases are identified by a version number.
[Semantic Versioning (semver)](http://semver.org/) is the most accepted and used way to add numbers to software versions.
It is a way of communicating impact of changes in the software on users.

A version number consists of three numbers: major, minor, and patch, separated by a dot: _2.0.0_.
After some changes to the code, you would do a new release, and increment the version number.
Increment the:
* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards-compatible manner, and
* PATCH version when you make backwards-compatible bug fixes.

Very often package managers depend on `semver` and will not work as expected otherwise.

### Releasing code on github

Github makes it easy to do a release straight from your repositories website.
See [github releases](https://help.github.com/categories/releases/) for more information.

### CHANGELOG.md

A change log is a way to communicate notable changes in a release to the users and contributors.
It is typically a text file at the root of your repository called *CHANGELOG.md*.
Every release should have relevant entry in change log.

See [Keep a CHANGELOG](http://keepachangelog.com/) for some best practices.

### One command install

To not scare away users and (potential) collaborators, installing the software should be easy, a one command process.
The process itself typically includes installing dependencies, compiling, testing, and finally actual installation, and can be quite complex.
The use of a proper build system is strongly recommended.

### Package in package manager

If your software is useful for a wider audience, create a package that can be installed with a package manager. Package managers can also be used to install dependencies quickly and easily.
* For Python use [pip](https://pypi.python.org/pypi/pip)
* For Javascript use [npm](https://www.npmjs.com/package/npm)
* C, C++, Fortran, ... use packages from your distributions official repository. List your actual dependencies in the *INSTALL.md* or *README.md*

Some standard solutions for building (compiling) code are:
* The Autotools: _autoconf_, _automake_, and _libtool_. See the [Autotools Documentation](https://www.gnu.org/software/automake/manual/html_node/Autotools-Introduction.html), or an [introductionary presentation by Thomas Petazzoni](https://elinux.org/images/4/43/Petazzoni.pdf)
* [CMake](https://cmake.org/)
* [Make](https://www.gnu.org/software/make/)

### Release quick-scan by other engineer

A check by a fellow engineer to see if the documentation is understandable? can the software be installed? etc.

Think of it as a kind of code review but with focus on mechanics, not code. The reviewer should check if:
(i) there is easily visible or findable documentation,
(ii) download works, (iii) there are instructions on how to (iv) install and (v) start using software,
some of the things in this *scan* could be automated with continuous integration.

### Citeable

Create a DOI for each release see [Making software citable](../citable_software/making_software_citable.html).

### Dissemination

When you have a first stable release, or a subsequent major releases, let the world know!
Inform your coordinator and our Communications Advisor (Lode) so we can write news item on our site, add it to the annual report, etc.
