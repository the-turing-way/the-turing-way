# Best Practices and Recommendations

```{figure} ../../figures/continuous-integration-may19.jpg
---
name: continuous-integration-may19
alt: Illustration of continuous integration showing the lifecycle of continuous integration to plan, create and incorporate changes and updates to data. The image shows these four steps in the lifecycle arranged in a circle and connected by arrows.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

## Table of contents

  - [Small, iterative changes](#Small_iterative_changes)
  - [Trunk-based development](#Trunk_based_development)
  - [Keep the building and testing phases fast](#Keep_the_building_and_testing_phases_fast)
  - [Computational expense](#Computational_expense)
  - [Dependencies tracking](#Dependencies_tracking)
  - [Consistency throughout the pipeline](#Consistency_throughout_the_pipeline)

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
