(cm-citable-linking)=

# Linking Research Objects

Linking your data, code and article will ensure that you receive **credit** for your work and it will increase the visibility of your research outputs.
There are several different ways to do this.
You can decide to:

1) Open up your Research Object publicly, at the same time as, for example, the **preprint** of your article, or

2) Keep the Research Object closed until the article is published.

(cm-citable-linking-open)=
## 1. Open the Research Objects

The easiest way to connect your dataset to your publication is to publish the dataset first (for example, at the same time as the **preprint**).
This will provide you with the correct information for your **Data Availability Statement** and your references (see {ref}`Citing Data<cm-citable-cite-data>`), and will allow reviewers to include the dataset in their review.
If any adjustments are needed based on the review process you can often upload a new version of the dataset (see for example [Zenodo](https://zenodo.org/), [Figshare](https://figshare.com/), [4TU.ResearchData](https://data.4tu.nl/)). This will provide you with a new DOI for the latest version, and some repositories (such as Zenodo) allow you to have a canonical DOI that will always point to the latest version of the dataset). See {ref}`cm-citable-steps-doi` for more information about DOIs. 
Remember that the contributors and date of deposition are publicly available, making it unlikely that others will 'scoop' you.
But if you are hesitant about opening up your dataset before the article is published, you can either publish the dataset under restricted access, under embargo, or reserve a DOI in advance and publish the Research Object later.

(cm-citable-linking-closed)=
## 2. Keep the Research Objects closed

### Publish the Research Objects under restricted access

Publishing your data under restricted access means that the data is uploaded to the repository, but you're only providing access to individuals that request access or you can provide access through sharing a private link.

* You decide with whom to share the private link and whether individuals that request access will obtain access.
    * You can share the data with reviewers.
* Your metadata (information about the data) is publicly available.
* You can provide the correct DOI in the paper's **Data Availability Statement** and in the reference list (see {ref}`Citing Data<cm-citable-cite-data>`).
* After your article is published:
    * Add the DOI of the publication to the dataset;
    * Change the access permission rights to public (see for example [Zenodo](https://zenodo.org/)).

### Publish the Research Objects under embargo

An embargo means that you have already uploaded the data to the repository, but are not providing access to the data until a certain date.

* No one has access to your data until the embargo period has expired (you can define this period), or until you changed the access permissions yourself.
    * You cannot share the data with reviewers.
* Your metadata (information about the data) is publicly available.
* You can provide the correct DOI in the paper's **Data Availability Statement** and in the reference list (see {ref}`Citing Data<cm-citable-cite-data>`).
* After your article is published:
    * Add the DOI of the publication to the dataset;
    * Change the access permission rights if the embargo has not yet expired (see for example [Zenodo](https://zenodo.org/)).

(cm-citable-linking-reserve-doi)=
### Reserve a DOI and publish later

Several data repositories, such as [Zenodo](https://zenodo.org/) and [Figshare](https://figshare.com/), allow you to reserve a DOI.
Reserving a DOI means you are not required to upload your data yet, but you will need to provide some metadata (title, author/contributors) to complete the DOI reservation. The reserved DOI will be in use after you actually uploaded the data and decide to publish the data.

* No one has access to your data or the metadata yet, because the landing page of your dataset is not working yet.
    * Your data is not available to reviewers.
* You can provide the correct DOI in the paper's **Data Availability Statement** and in the reference list (see {ref}`Citing Data<cm-citable-cite-data>`).
* After your article is published:
    * Upload the dataset to your reserved DOI;
    * Add the DOI of the publication to the dataset;
    * Publish your dataset.

# Check the data DOI in your publication

Whichever route you decide to take, it is important to double-check the proof of your article.
The DOI for your dataset should be correctly listed in the **Data Availability Statement** and in the reference list.
For more information see {ref}`Citing Data<cm-citable-cite-data>`.

(cm-citable-linking-metadata)=
## Connection Metadata: Creating Rich Linkages

The strategies above describe when and how to publish research outputs, but there's another crucial aspect: connection metadata.
This is structured, machine-readable information that formally links your research outputs together through their persistent identifiers.

When you "add the DOI of the publication to the dataset" (see {ref}`Reserve DOI<cm-citable-linking-reserve-doi>`), you're creating connection metadata.
But where exactly does this information go, and how do you create these links?
This section provides practical guidance on using connection metadata to build a connected scholarly record.

For background on persistent identifiers and the infrastructure that makes these connections possible, see our {ref}`chapter on PIDs<rr-rdm-pid>`.

(cm-citable-linking-related)=
## Linking Research Outputs

When you have multiple related research outputs (a dataset, the code that analyzes it, the paper that describes it), you can formally link them in the PID metadata, for example, in DataCite metadata schema, this information is captured in the **relatedIdentifier** field.

### Why Link Through Metadata?

You might wonder: isn't it enough to mention the DOI in the paper text or README file?
While that's helpful, formal metadata links provide additional benefits:

- **Machine-readable**: Automated systems can discover all outputs related to a paper or dataset
- **Bidirectional**: Both resources show the connection, not just one
- **Typed relationships**: The metadata specifies what kind of relationship exists
- **Aggregatable**: Citation databases and metrics systems can trace the full impact
- **Discoverable**: Finding one output helps users discover all related outputs

### Types of Relationships

PID metadata schema uses standardized **relationship types** to describe how resources relate to each other.
Examples from the DataCite schema include:

| Relationship Types | Use Case | Example |
|-------------------|----------|---------|
| IsSupplementTo / IsSupplementedBy | When one output supplements another | A dataset *IsSupplementTo* the paper that describes it |
| IsDerivedFrom / IsSourceOf | When one output is derived from another | A cleaned dataset *IsDerivedFrom* the raw data |
| Cites / IsCitedBy | Formal citation relationships | A paper *Cites* a methodology it uses |
| IsPartOf / HasPart | When outputs are components of a larger whole | Individual datasets *IsPartOf* a data collection |
| References / IsReferencedBy | General references | Documentation *References* a protocol |
| IsVersionOf / HasVersion | Connections between versions | A is a version of B |
| IsNewVersionOf / IsPreviousVersionOf | Specific version succession | Version 2 *IsNewVersionOf* version 1 |
| Compiles / IsCompiledBy | When code or workflows produce outputs | An analysis script *Compiles* a figure |

For a complete list, see [DataCite's relatedIdentifier documentation](https://support.datacite.org/docs/datacite-metadata-schema-v44-recommended-and-optional-properties#102-relatedidentifier).

### How to Add Related Identifiers

The specific process depends on which repository you're using, but the general approach is similar:

#### During initial deposit:
1. When uploading your research output, look for fields like:
   - "Related identifiers"
   - "Related works"
   - "Linked resources"
   - "Relations"
2. Add the DOI of the related resource
3. Select the appropriate relationship type from a dropdown menu
4. Specify the direction if needed

#### After initial deposit:
1. Contact the repository's support team or use the metadata update form
2. Provide the DOI of your resource and the related DOI
3. Specify the relationship type
4. The repository will update the metadata

### Repository-Specific Examples

::::{tab-set}
:::{tab-item} Zenodo
:sync: tab1
- When creating or editing a record, scroll to "Related identifiers/works"
- Click "Add related identifier"
- Enter the identifier (DOI, arXiv ID, and so on)
- Choose relationship type from dropdown
- Choose resource type of the related item
- The interface shows both sides (for example, "this dataset *is supplement to* that publication")
:::
:::{tab-item} Figshare
:sync: tab2
- In the item editor, find the "Links" or "Related items" section
- Add the DOI of related resources
- Select relationship type
- Figshare may have limited relationship type options compared to full DataCite schema
:::
:::{tab-item} OSF
:sync: tab3
- In a project or component, use the "Links" widget
- Add external links including DOIs
- Describe the relationship in the link description
- OSF's native connections between project components are automatic
:::
:::{tab-item} Dryad
:sync: tab4
- During submission, there's a "Related Works" section
- Add manuscript DOIs automatically if submitting through journal integration
- Add additional related resources manually with relationship types
:::
::::


**For institutional repositories:**
- Check your repository's documentation or contact repository staff
- They can add related identifier metadata even if there's no self-service option

### Best Practices for Linking Outputs

- **Link early**: Add relationships when you first deposit outputs, or update metadata as soon as related outputs are published
- **Link bidirectionally**: If a dataset supplements a paper, add the link from both sides if possible
- **Be specific**: Use the most precise relationship type (IsSupplementTo is more specific than References)
- **Link comprehensively**: Connect all related outputs (data, code, paper, protocols, presentations)
- **Update when publishing**: If you reserved a DOI for a paper, update data/code metadata once the paper has its final DOI

### Example: Connecting a Complete Research Project

The Implementing FAIR Workflows project is registered with a project ID (https://doi.org/10.60581/zaev-6p15), which links to the ORCIDs of the project team members, the ROR ID of partner organizations, and the outputs of the project - registeration, datasets, software, reports, etc. - are openly shared with DOI. DataCite Commons, the DOI metadata discovery portal aggregates the metadata of all project related resources and present a full overview: https://commons.datacite.org/doi.org/10.60581/zaev-6p15


(cm-citable-linking-versions)=
## Managing Versions Through PIDs

Research outputs often evolve over time: you might fix errors in a dataset, improve code, or update protocols.
Persistent identifiers provide structured ways to handle versioning while maintaining clear connections between versions.

### Version DOIs vs. Concept DOIs

Some repositories (notably [Zenodo](https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning)) implement a two-level DOI system:

Version DOI
: A version DOI points to one specific version of a resource and never changes. Use this when you want to cite a specific version for reproducibility. For example: `10.5281/zenodo.3332807` (version 1.0).

Concept DOI
: A concept DOI points to the resource as a whole, across all versions, and always resolves to the latest version. Use this when you want to cite the work in general. For example: `10.5281/zenodo.3332806` (concept, always latest).

The concept DOI creates an umbrella that links all versions together.
When you publish a new version, it gets a new version DOI, but the concept DOI remains the same.

### When to Create a New Version vs. New Resource

You should create a new version when the fundamental resource remains the same but has been improved or corrected. This includes situations like fixing errors or bugs, adding new data points to an existing dataset, improving documentation or metadata, or making minor methodological adjustments. The key characteristic of a new version is that it represents an evolution or refinement of the original resource rather than a fundamentally different output.

In contrast, you should create an entirely new resource when the changes are substantial enough that the output could stand alone independently. This applies when you're collecting fundamentally different data, completely redesigning a protocol, or making major methodological changes that alter the nature of the work. These situations call for a new DOI rather than a new version because the new output represents distinct scholarly work.

When in doubt, ask yourself: "Would citing the old version still be valid and useful?" If yes, create a new version. If no, create a new resource.

### How to Publish New Versions

::::{tab-set}
:::{tab-item} Zenodo
:sync: tab1
1. Go to your published record
2. Click "New version"
3. Zenodo creates a copy with a new reserved DOI
4. Update files and metadata as needed
5. Publish the new version
6. The concept DOI automatically updates to point to the latest version
7. Both version DOIs remain active and independently citable
:::
:::{tab-item} Figshare
:sync: tab2
1. Edit your existing item
2. Upload new files
3. Figshare versioning happens automatically
4. Each version is preserved and accessible through the item history
:::
:::{tab-item} OSF
:sync: tab3
1. Update files in your project or component
2. OSF maintains version history automatically
3. The DOI always points to the current state
4. Previous versions are accessible through the interface
:::
:::{tab-item} Other repositories
:sync: tab4
1. Check specific repository documentation
2. Some may require creating a new record and linking with IsNewVersionOf relationship
3. Contact repository support for guidance
:::
::::


### Version Metadata Links

Whether or not your repository has automatic version handling, you can explicitly link versions through connection metadata.


### Best Practices for Versioning

- **Document changes**: Include a changelog or version notes explaining what changed
- **Preserve old versions**: Don't delete previous versions - persistence is the point of PIDs
- **Update related resources**: If you publish a new dataset version, consider whether related code or documentation needs updating too
- **Cite specific versions in papers**: For reproducibility, cite the exact version used, not the concept DOI
- **Use concept DOIs for general reference**: When recommending a resource (in documentation, teaching), use the concept DOI so people get the latest version
- **Communicate updates**: If others have cited your work, consider contacting them about significant improvements

(cm-citable-linking-funding)=
## Connecting Research to Funding

Research outputs can be formally linked to the grants that funded them through **fundingReference** metadata.
This creates a traceable connection from funding organizations through researchers to the resulting outputs.

### Why Cite Funding?

You might already acknowledge funding in your papers, but structured funding metadata provides additional benefits:

- **Funder reporting**: Automated systems can discover all outputs from a grant
- **Impact tracking**: Funders can measure return on investment
- **Transparency**: The public can see how research funds are used
- **Credit**: Proper attribution for funding sources
- **Discovery**: Others researching similar topics can find related funded work

### Acknowledgment vs. Citation

There's an important distinction:

#### Acknowledgment (text-based):
- Written in the acknowledgments section of a paper
- Example: "This work was supported by grant ABC-123 from the Example Foundation"
- Not machine-readable
- Not standardized
- Often inconsistent across outputs from the same grant

#### Citation (structured metadata):
- Included in the PID metadata using fundingReference fields
- Machine-readable and standardized
- Searchable and aggregatable
- Links to persistent identifiers for the funder and potentially the grant

Both are valuable, but citation through metadata enables much more powerful tracking and discovery.

### Components of Funding Metadata

Complete funding metadata includes:

**Funder Information:**
- **Funder Name**: The organization providing funding
- **Funder Identifier**: A persistent identifier for the funder (usually from Crossref Funder Registry)
  - Example: National Science Foundation = `https://doi.org/10.13039/00000001`
  - Example: Wellcome Trust = `https://doi.org/10.13039/00000035`

**Grant Information:**
- **Award Number**: The specific grant identifier
  - Example: "NE/X012345/1" or "R01-GM12345"
- **Award Title**: The title of the funded project (optional but helpful)
- **Award URI**: A persistent identifier for the grant itself, if available

### How to Add Funding Information

**During deposit:**
1. Most repositories have a "Funding" section in their upload forms
2. Start typing the funder name - many repositories auto-complete from the Funder Registry
3. Add the grant/award number
4. Add grant title if there's a field for it
5. Repeat for additional funders (many projects have multiple funding sources)

**After deposit:**
1. Contact the repository to update metadata
2. Provide complete funding information:
   - Funder name (and Funder ID if you know it)
   - Grant number
   - Grant title

**Repository-specific guidance:**

::::{tab-set}
:::{tab-item} Zenodo
:sync: tab1
- "Funding" section during upload
- Type-ahead search of Funder Registry
- Add multiple funders
- Fields for grant number and details
:::
:::{tab-item} Figshare
:sync: tab2
- "Funding" field in metadata editor
- Free text, but try to match official grant information
:::
:::{tab-item} Dryad
:sync: tab3
- "Funding information" during submission
- Connected to journal submission data when available
:::
:::{tab-item} OSF
:sync: tab4
- Not currently supported in core OSF metadata
- Can include in project description/wiki
- Supported in some OSF-integrated services
:::
::::

### Best Practices for Funding Citation

- **Add funding to all outputs**: Not just papers - include in data, code, protocols, and other outputs
- **Use official grant numbers**: Match the funder's format exactly
- **Include all funders**: If multiple organizations contributed, cite them all
- **Add early**: Include funding information when you first deposit outputs
- **Be consistent**: Use the same grant number format across all outputs from that grant
- **Check with your funder**: Some funders have specific requirements for how grants should be cited

### Example Funding Metadata

A dataset might include:
```
Funder: UK Research and Innovation
Funder Identifier: https://ror.org/001aqnf71
Award Number: MR/V012345/1
Award Title: Understanding Climate Change Impacts on Grassland Ecosystems

Funder: Natural Environment Research Council
Funder Identifier: https://ror.org/02b5d8509
Award Number: NE/X067891/1
```

:::{note}
A project might list both the parent organization (UKRI) and the specific council (NERC) if both provided funding or if the specific council should be credited.
:::

(cm-citable-linking-people)=
## People and Organizations in Metadata

Just as research outputs have persistent identifiers, so do people and organizations.
Including these identifiers in your research output metadata creates a rich network of connections.

### ORCID: Persistent Identifiers for Researchers

{abbr}`ORCID (Open Researcher and Contributor ID)` provides unique identifiers for researchers that distinguish them from everyone else, even people with identical names.

For comprehensive guidance on ORCID, see our {ref}`dedicated ORCID chapter<cm-citable-orcid>`.

**Key points for connection metadata:**
- Include your ORCID when depositing research outputs
- Add ORCIDs for all co-authors when possible
- The ORCID connects all your outputs across different repositories and publications
- Your ORCID profile can automatically collect works that cite your ORCID

**Format:** ORCIDs are 16-digit numbers formatted as `0000-0001-2345-6789`
As URLs: `https://orcid.org/0000-0001-2345-6789`

### ROR: Persistent Identifiers for Organizations

{abbr}`ROR (Research Organization Registry)` provides unique identifiers for research institutions.

**Uses in metadata:**
- Author/creator affiliations
- Contributor affiliations
- Institution hosting the research
- Partner organizations in collaborations

**Format:** ROR IDs are URLs like `https://ror.org/013meh722` (University of Cambridge)

**How to add:**
- Some repositories support ROR ID fields for affiliations
- When creating or editing records, look for organization/affiliation fields
- Search the [ROR Registry](https://ror.org/) to find your institution's ID

### Benefits of Including People and Organization Identifiers

**For researchers:**
- All your work is connected, regardless of name changes or institutional moves
- Easier to prove your contributions for promotion, tenure, or grant applications
- Automatic collection of citations and reuse
- Proper disambiguation from others with similar names

**For institutions:**
- Track all research outputs from the institution
- Demonstrate research impact and productivity
- Support reporting requirements
- Identify collaboration networks

**For the research community:**
- Discover all work by a researcher or institution
- Understand collaboration patterns
- Track research mobility
- Measure impacts more accurately

### Building a Fully Connected Scholarly Record

When you combine all these types of connection metadata, you create a rich, queryable network:

A **dataset** (DataCite DOI) can be connected to:
- The **researchers** who created it (ORCIDs)
- Their **institutions** (ROR IDs)
- The **grants** that funded it (Funder IDs + award numbers)
- The **paper** describing it (Crossref DOI)
- The **code** that analyzes it (DataCite DOI)
- The **protocol** used to collect it (DataCite DOI)
- **Previous and new versions** of itself (version relationships)

This interconnected graph enables:
- Comprehensive discovery (find all related materials)
- Complete attribution (credit all contributors)
- Impact measurement (trace outputs from funding to reuse)
- Reproducibility (access all components needed)
- Trust (transparent provenance and connections)

For more on the infrastructure enabling these connections, see our {ref}`chapter on persistent identifiers<rr-rdm-pid>`.

## More resources:

* [How to disclose data for double-blind review and make it archived open data upon acceptance](https://ineed.coffee/5205/how-to-disclose-data-for-double-blind-review-and-make-it-archived-open-data-upon-acceptance/)
* [Anonymous data sharing using the Open Science Framework](https://help.osf.io/hc/en-us/articles/360019930333-Create-a-View-only-Link-for-a-Project)
* [Anonymous GitHub](https://anonymous.4open.science/)
