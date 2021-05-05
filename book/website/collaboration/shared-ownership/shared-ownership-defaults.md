(cl-shared-ownership-defaults)=
# Nudging for a better default

Research has shown that humans making decisions have a strong tendency to go along with the status quo or default option (See the [Nudge Theory](https://www.imperial.ac.uk/nudgeomics/about/what-is-nudge-theory/) by {cite}`ThalerSunstein2009Nudge`).
In the absence of an actively defined default, the prevailing cultural or institutional norm becomes the de-facto option of choice.
And hence, the default options for ongoing and new projects should nudge strongly towards adopting a shared ownership model.

The minimum default for an open source project should include the following documents:
i. defining the open source license,
ii. describing ways to support contributions and acknowledge contributors, and
iii. visibly sharing ownership with the community of contributors.

## Open Source License by default

More awareness around open licensing is required as many researchers who currently own code might not be completely aware of how open source licenses can protect the openness and identity of a project.
More code might be licensed if researchers were given a basic introduction into how different open licenses work (for example, copyleft vs permissive) and which to choose, although this will only help projects that are maintained enough for a license to be added (see {ref}`rr-licensing`) for reference).
There should be a push for code to be openly licensed by default.
This can be applied by many stakeholders in the research ecosystem. Funders can require that code produced by a grant is openly licensed and, similarly, publishers can require that code associated with a publication is openly licensed (open research _data_ is already required by funders for example, [in the UK](https://www.ukri.org/about-us/policies-standards-and-data/good-research-resource-hub/open-research/), this could easily be extended to cover software).
The companies that host repositories can - as some do - make it easy to add a license, and gently encourage users to do so by adding a license by default.

## Ways to acknowledge contributions:

Ownership should be more accurately shared with contributors by ensuring that the ways of working, contributing and recognising contributions are properly defined in the project.
Details on people and practices should be transparently documented and communicated so that not only existing contributors can build a sense of ownership but new contributors can also identify what pathways they can take in the project.
There are many ways to acknowledge all contributors, including those who do not code or write documentation.
For example, we can learn from open source metrics like [CHAOSS](https://chaoss.community/) or [CRediT - Contributor Roles Taxonomy](https://casrai.org/credit/), recognise the hidden labour using frameworks defined by [HiddenREF](https://hidden-ref.org/) or as described in {ref}`The Turing Way Acknowledge chapter<ch-acknowledgement>`, allow people to capture their contributions in a way that is most meaningful for them.

## Sharing project ownership with the community

In the case of shared ownership, a collective community builds the project and hence should be attributed as such.
To make it a default we need to make it easy to practice across different open source projects.
One way to do it is to have essential community documents demonstrating the commitment to fairly acknowledge and share ownership of the project with all contributors.

Below, we list a few action points that each of us can take within our open source projects.

**Call to actions!**

### Contributors documents

Adding a contribution guideline and Code of conduct have become a standard practice in the open source community projects (see [Open Source Guide for reference](https://opensource.guide/building-community/)).
Additionally, a ‘contributors’ page must be added to the project repository to display the names of all the contributors.
See the [contributors.md](https://github.com/alan-turing-institute/the-turing-way/blob/master/contributors.md) and {ref}`Contributors Record<contributors-record-highlights>` in _The Turing Way_.

### Describe how to cite the project

We can explicitly describe how someone can cite an open source project by giving credit to the community of contributors instead of attributing individuals administering the project.
For example, we can use “Community” as the first author as described in _The Turing Way_ {ref}`welcome` page.

### Make recognising contributors part of the process

Recognising contributors by recording their names in visible locations (like contributors file) can be added to the admins or maintainers workflows.
To automate the process, GitHub actions or bots can be set up.
For example, you can install the all-contributors bot by [https://allcontributors.org](https://allcontributors.org) to your repository, which can help you recognise contributions including those that don’t involve pushing code to your repository.
See it working on [_The Turing Way_ repository](https://github.com/alan-turing-institute/the-turing-way#contributors).
