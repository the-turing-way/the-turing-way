(rr-ci)=
# Continuous integration

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| {ref}`Experience with the command line<rr-overview-resources-commandline>` | Necessary | Continuous integration will follow command line instructions
| {ref}`Version control<rr-vcs>` | Necessary | Continuous integration runs every time a new _commit_ is made to your project |
| {ref}`Reproducible computational environments<rr-renv>` | Necessary | Continuous integration runs your tests on a separate computer (usually in the cloud) so you need to set it up in the same way. |
| {ref}`Testing<rr-testing>` | Very helpful | Continuous integration _tests_ if anything important has changed when you make a change in your project |

## Summary

Continuous integration (CI) is the practice of integrating changes to a project made by individuals into a main, shared version frequently (usually multiple times per day). CI software is also typically used to identify any conflicts and bugs that are introduced by changes, so they are found and fixed early, minimising the effort required to do so. Running tests regularly also saves humans from needing to do it manually. By making users aware of bugs as early as possible researchers (if the project is a research project) do not waste a lot of time doing work that may need to be thrown away, which may be the case if tests are run infrequently and results are produced using faulty code.

```{figure} ../figures/continuous-integration-may19.*
---
height: 500px
name: continuous-integration-may19
alt: A sketch showing how continuous integration helps developers plan, design, integrate code into a shared repository, and then observe the influence of any changes.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

## Motivation and Background

CI has a number of key benefits:

- Helps bugs to be found early, minimising their damage and making them easier to fix
- Keeps project contributors up to date with each other's work so they can benefit from it as soon as possible
- Encourages users to write tests
- Automates running of tests
- Ensures tests are run frequently
