(rr-rdm-metadata)=
# Documentation and Metadata

Having data available is of no use if it cannot be understood.
For example, a table of numbers is useless if there are no headings that describe what the columns/rows contain.
Therefore you should ensure that open datasets include consistent metadata, that is information about the data, so that the data is fully described.
This requires that all documentation accompanying data is written in clear, plain language, and that data users have sufficient information to understand the source, strengths, weaknesses, and analytical limitations of the data so that they can make informed decisions when using it.

- The level of documentation and metadata [{term}`def<Metadata>`] will vary according to the project, and the range of people the data needs to be understood by.
- Variables should be defined and explained using [data dictionaries](https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary).
- Data should be stored in logical and hierarchical folder structures, with a README file used to describe the structure.
The README file is helpful for others and will also help you find your data in the future {cite:ps}`Fuchs2018documentation`.
See the [README template from Cornell](https://cornell.app.box.com/v/ReadmeTemplate) for an example.
- It is best practice to use recognised community metadata standards to make it easier for datasets to be combined.

(rr-rdm-metadata-standards)=
## Community Standards - Metadata

The use of community-defined standards for metadata is vital for reproducible research and allows for comparison of heterogeneous data from multiple sources, domains and disciplines.
Metadata standards include content and structural standards.
The content standards explain what information should be recorded when describing a particular type of resource and how that information should be recorded. 
While the structural standards define what the fields are and what types of information should be recorded in them.
Metadata standards are discipline specific.
For example, for brain data, the [Brain Imaging Data Structure](https://doi.org/10.25504/FAIRsharing.rd1j6t) is the standard to use.
Not every discipline may use metadata standards, however.
You can see if your discipline uses metadata standards through [FAIRsharing](https://fairsharing.org/), a resource to identify and cite the metadata or identifier schemas, databases or repositories that exist for your data and discipline.
