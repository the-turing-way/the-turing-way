(cl-shared-ownership-defaults)=
# Nudging for a Better Default

Research has shown that humans making decisions have a strong tendency to go along with the status quo or default option (See the [Nudge Theory](https://www.imperial.ac.uk/nudgeomics/about/what-is-nudge-theory/) by {cite:ps}`ThalerSunstein2009Nudge`).
In the absence of an actively defined default, the prevailing cultural or institutional norm becomes the de-facto option of choice.
And hence, the default options for ongoing and new projects should nudge strongly towards adopting a shared ownership model.

The minimum default for an open source project should include the following documents:
1. Select an open source license (whenever you can).
2. Acknowledging contributors visibly.
3. Set standards for shared ownership.

## Open Source License

More awareness around open licensing is required as many researchers who currently own code might not be completely aware of how open source licenses can protect the openness and identity of a project.
More code might be licensed if researchers were given a basic introduction into how different open licenses work (for example, copyleft vs permissive) and which to choose, although this will only help projects that are maintained enough for a license to be added (see {ref}`rr-licensing`) for reference).
There should be a push for code to be openly licensed by default.
This can be applied by many stakeholders in the research ecosystem. Funders can require that code produced by a grant is openly licensed and, similarly, publishers can require that code associated with a publication is openly licensed (open research _data_ is already required by funders for example, [in the UK](https://www.ukri.org/about-us/policies-standards-and-data/good-research-resource-hub/open-research/), this could easily be extended to cover software).
The companies that host repositories can - as some do - make it easy to add a license, and gently encourage users to do so by adding a license by default.

**Call to action: Select a license for your project**

Plan your project from the beginning to be open throughout the lifecycle of your research.
When using personal or identifiable data, clearly state what measures are taken to ensure privacy and data security.
For everything else in your work, choose an open source license and add it to your repository (see https://choosealicense.com/).
You can read more about it in the {ref}`Licensing<rr-licensing>` chapter.

## Meaningful Acknowledgement of Contributors

Ownership should be more accurately shared with contributors by ensuring that the ways of working, contributing and recognising contributions are properly defined in the project.
Details on people and practices should be transparently documented and communicated so that not only existing contributors can build a sense of ownership but new contributors can also identify what pathways they can take in the project.
There are many kinds of contributions possible in open source projects that go beyond writing code or documentation.
Each of these contributions should be acknowledged transparently and fairly.
For example, we can learn from open source metrics like [CHAOSS](https://chaoss.community/) or [CRediT - Contributor Roles Taxonomy](https://casrai.org/credit/), recognise the hidden labour using frameworks defined by [HiddenREF](https://hidden-ref.org/) or as described in {ref}`The Turing Way Acknowledge chapter<ch-acknowledgement>`, allow people to capture their contributions in a way that is most meaningful for them.
A more structured programme can be developed that recognises, rewards and incentivise contributors who are crucial for your project's sustainability.

**Call to action: Acknowledging contributors visibly**

Recognising contributors by recording their names in visible locations (like a contributors file) should be added to the admins’ or maintainers’ workflows.
Announce and celebrate all kinds of work by communicating them openly in official community forums and channels.
You can use GitHub actions, bots or a continuous integration pipeline to automate the process.
To take another easier approach, you can install the all-contributors bot by [https://allcontributors.org](https://allcontributors.org) to your repository, which can help you recognise contributions including those that don’t involve pushing code.
See it working on [_The Turing Way_ repository](https://github.com/the-turing-way/the-turing-way#contributors).

## Sharing Project Ownership with the Community

In the case of shared ownership, a collective community builds the project and hence should be attributed as such.
To make it a default we need to make it easy to practice across different open source projects.
One way to do it is to have essential community documents demonstrating the commitment to fairly acknowledge and share ownership of the project with all contributors.
These documents should not only be shared but kept open for feedback, contributions and update to make them meaningful for the community.
Community policy and norms should be communicated from the start to facilitate open, safe and respectful dialogue among the community members.

**Call to action: Set standards for shared ownership**

Describe explicitly who is considered the project owner.
You should share credit with the community of contributors instead of only attributing individuals administering the project.
For example, when citing the project, use “Community” as the first author {ref}`as practised in The Turing Way<fw-cite>`.
Contribution guidelines, Code of Conduct (see Open Source Guide for reference) and other community pages on your project repository can help in setting the tone for the culture you want to promote in the community, and how contributors are supported in their participation.
