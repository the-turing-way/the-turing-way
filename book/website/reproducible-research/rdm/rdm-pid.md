(rr-rdm-pid)=
# Persistent Identifiers

Persistent identifiers (PIDs) are long-lasting references to digital resources that remain valid even if the resource's location changes.
They are fundamental to making research findable, accessible, and citable in the long term.
Throughout this book, you'll see recommendations to "assign a DOI" or use persistent identifiers - this chapter explains what PIDs are, how they work, and how they enable FAIR and open research practices.

```{figure} ../../../../figures/placeholder.*
---
name: persistent-identifiers
alt: Illustration showing how persistent identifiers connect research outputs, researchers, organizations, and funding sources in an open scholarly infrastructure ecosystem.
---
Persistent identifiers create connections across the research ecosystem.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: 10.5281/zenodo.3332807.
```

(rr-rdm-pid-what)=
## What are Persistent Identifiers?

A persistent identifier is a unique string of characters that reliably points to a specific digital resource.
Unlike a web address (URL) that can break when a website is reorganized or shut down, a PID is designed to remain functional indefinitely.

### The Link Rot Problem

Research outputs shared online face a significant challenge: **link rot**.
Studies have shown that up to 50% of URLs in scientific papers become inaccessible within just a few years.
When a dataset moves from one repository to another, or when a university reorganizes its web infrastructure, ordinary web links break.
This makes it impossible for other researchers to find and verify the original work.

### How PIDs Solve This

PIDs use a **resolution service** that acts as a lookup system:
1. The PID (for example, `10.5281/zenodo.3332807`) doesn't change even if the resource moves
2. When someone uses the PID, it is sent to a **resolver** (like [https://doi.org](https://doi.org))
3. The resolver looks up where the resource currently lives and redirects the user to the correct location
4. If the resource moves, only the resolver's records need updating - the PID itself stays the same

This is similar to how a phone number can stay the same even if you move to a new address.

(rr-rdm-pid-ecosystem)=
## Open Scholarly Infrastructure Ecosystem

Modern research relies on an ecosystem of interconnected PID systems.
These systems work together to create a **connected scholarly graph** where research outputs, people, organizations, and funding can all be reliably identified and linked.

### PIDs for Research Outputs

[DataCite](https://datacite.org/) and [Crossref](https://www.crossref.org/) are the two main providers of Digital Object Identifiers (DOIs) for research:

DataCite specialises in assigning DOIs to diverse research outputs including:

- Datasets
- Software and code
- Preprints and working papers
- Protocols and methods
- Presentations and posters
- Data Management Plans
- Physical samples
- Workflows and computational notebooks

Crossref primarily handles:

- Journal articles and book chapters
- Published conference proceedings
- Dissertations and theses
- Reports and standards documents

Both systems use the same DOI infrastructure (the Handle System), so all DOIs work the same way regardless of which organization issued them.
The main difference is in their communities and the types of metadata they specialize in collecting.

When you use a **trusted repository** (see our [chapter on data repositories](rr-rdm-repository)), it will typically assign a DOI through one of these providers automatically.
You don't usually need to choose between DataCite and Crossref yourself - the repository or publisher handles this for you.

### PIDs for People

[ORCID (Open Researcher and Contributor ID)](https://orcid.org/) provides unique identifiers for researchers.
An ORCID iD is a 16-digit number that distinguishes you from every other researcher, even those with identical names.

For comprehensive guidance on ORCID, see our [dedicated chapter on ORCID](communication-citable-orcid).

Key benefits:
- Collect all your research outputs in one place, regardless of where they're published
- Link your work across name changes or institutional moves
- Automatically populate author information when submitting to journals and funders
- Ensure proper attribution when others cite your work

### PIDs for Organizations

[ROR (Research Organization Registry)](https://ror.org/) provides identifiers for research institutions.
Every university, research institute, and funding organization can have a unique ROR ID.

Examples:
- The Alan Turing Institute: `https://ror.org/03f0awy98`
- Max Planck Society: `https://ror.org/01hhn8329`
- Stanford University: `https://ror.org/00f54p054`

ROR IDs appear in research output metadata to indicate:
- Where researchers are affiliated
- Which institutions collaborated on a project
- Where research was conducted

### PIDs for Funders

The Crossref Funder Registry and ROR provides identifiers for funding organizations.
These enable researchers to formally cite the grants that supported their work, not just acknowledge them in text.

This creates a traceable connection between:
- The grant that funded the research
- The researchers who received funding
- The research outputs that resulted

For more on citing funding, see the section on [connection metadata in linking research outputs](rr-rdm-pid-connecting-funding).

### How These Systems Work Together

These PID systems don't operate in isolation - they're designed to interconnect:

- A **dataset** (DataCite DOI) can be linked to:
  - The **researchers** who created it (ORCIDs)
  - Their **institutions** (ROR IDs)
  - The **grants** that funded it (Funder IDs)
  - The **article** that describes it (Crossref DOI)
  - The **software** used to analyze it (DataCite DOI)

This creates a rich, queryable network of relationships that makes research more discoverable and its impacts more measurable.
Funders, institutions, and researchers can trace the full story of research from funding to outputs to reuse.

(rr-rdm-pid-fair)=
## PIDs and FAIR Principles

Persistent identifiers are not just convenient - they're fundamental to making research FAIR (Findable, Accessible, Interoperable, and Reusable).
See our [chapter on FAIR principles](rr-rdm-fair) for a comprehensive overview.

### Findable

**PIDs make research objects findable in multiple ways:**

- **Unique identification**: Every research output gets a globally unique identifier that can't be confused with anything else
- **Metadata harvesting**: PID providers collect standardized metadata that can be searched across millions of research outputs
- **Search engines**: Services like [DataCite Metadata Search](https://search.datacite.org/), [Google Dataset Search](https://datasetsearch.research.google.com/), and [BASE](https://www.base-search.net/) aggregate PID metadata to enable discovery
- **Discipline-specific discovery**: PIDs allow community repositories to expose their holdings to broader search systems

When you assign a PID to a dataset, it becomes discoverable not just on the repository where it lives, but across the entire scholarly ecosystem.

### Accessible

**PIDs point to access methods, even for restricted resources:**

- PIDs resolve to a **landing page** that describes the resource and how to access it
- Even if data cannot be openly shared (for example, due to privacy concerns), the metadata describing it can be
- Landing pages explain access conditions, embargo periods, or application processes
- The PID remains valid even if access conditions change over time

This aligns with the principle that data should be "as open as possible, as closed as necessary."
See our chapters on [open data](rr-open-data) and [sharing data](rr-rdm-sharing) for guidance on when and how to share research outputs.

### Interoperable

**PIDs use standard systems that work across platforms:**

- All DOIs use the same resolution infrastructure, regardless of who issued them
- Standardized PID metadata formats enable automatic data exchange between systems
- PIDs can be embedded in other metadata formats, citations, and databases
- Relationship types (see [linking research outputs](communication-citable-linking)) allow expressing connections in machine-readable ways

This means tools and services can be built on top of PID infrastructure, creating value beyond what any single repository could provide.

### Reusable

**PIDs enable persistent citation and credit:**

- Formal citation of research outputs beyond traditional publications
- Track reuse and impact through citation networks
- Clear attribution enables ethical reuse
- Versioning through PIDs allows citing specific versions while maintaining connections to the conceptual work

When combined with open licenses (see our [licensing chapter](rr-licensing)), PIDs make it clear what can be reused and by whom.

(rr-rdm-pid-metadata)=
## PID Metadata

When a PID is created, it's accompanied by **metadata** - structured information about the resource the PID identifies.
This metadata is what makes research discoverable and understandable.

### What is PID Metadata?

PID metadata is:
- **Machine-readable**: Formatted so computers can automatically process and exchange it
- **Standardized**: Uses common field names and structures across all resources
- **Cross-domain**: Works for any type of research output, not just one discipline
- **Publicly accessible**: Available even if the resource itself has restricted access

### Core PID Metadata Properties

While different PID providers have their own schemas, core properties typically include:

**Essential (usually required):**
- **Identifier**: The PID itself (for example, DOI)
- **Creator**: Who created the resource
- **Title**: What the resource is called
- **Publisher**: Who is making it available (often the repository)
- **Publication Year**: When it was made available
- **Resource Type**: What kind of output it is (Dataset, Software, Preprint, and so on)

**Important for discoverability:**
- **Description**: What the resource is about (abstract or summary)
- **Subject/Keywords**: Topics covered
- **Rights**: License and reuse terms
- **Version**: Which version this is
- **Language**: What language(s) it's in

**For linking and attribution:**
- **Related Identifiers**: Links to other research outputs (papers, data, code)
- **Funding References**: Grants that supported the work
- **Contributors**: Others who contributed (with ORCID iDs)
- **Affiliation**: Institutional affiliations (with ROR IDs)

For comprehensive guidance on metadata, see our [chapter on documentation and metadata](rr-rdm-metadata).

### Relationship to Domain-Specific Metadata

It's important to understand that PID metadata and domain-specific metadata serve different but complementary purposes:

**PID metadata enables discovery:**
- Works across all research domains
- Optimized for search engines and aggregators
- Minimal barrier to entry
- Focus on core bibliographic information

**Domain-specific metadata enables reuse:**
- Follows community standards for a specific field (for example, Brain Imaging Data Structure for neuroscience)
- Contains detailed technical specifications
- May include specialized vocabularies or ontologies
- Critical for understanding and working with the data

**Both are needed:**
Think of PID metadata as the catalog card that helps someone find a book in a library, while domain-specific metadata is the detailed table of contents and index inside the book.

Our [metadata chapter](rr-rdm-metadata) discusses community standards like [FAIRsharing](https://fairsharing.org/) that help you find the right domain-specific standards for your field.
When you deposit in a repository, you'll typically provide both:
1. Core PID metadata through the repository's submission form
2. Domain-specific metadata as part of your documentation and data files

### Metadata Completeness: Minimal vs. Rich

While some fields are required to create a PID, providing **rich metadata** substantially increases the value of your research outputs:

**Minimal PID metadata** (required fields only) allows:
- Basic discovery through search
- Formal citation in references
- Persistent access to the resource

**Rich PID metadata** (many optional fields completed) enables:
- More precise search and filtering
- Understanding context without accessing the resource
- Automated connections to related work
- Better assessment of relevance and reusability
- Tracking funding impact and institutional contributions

**Example of minimal vs. rich metadata:**

Minimal:
```
Title: Field Survey Data
Creator: J. Smith
Publisher: Generic Repository
Year: 2024
Type: Dataset
```

Rich:
```
Title: Soil Carbon Content Survey Data from Temperate Grasslands 2022-2023
Creators: Jane Smith (ORCID: 0000-0002-1234-5678)
          Alex Johnson (ORCID: 0000-0003-8765-4321)
Affiliations: University of Example (ROR: 02abcdef9)
Publisher: Field Science Data Repository
Year: 2024
Type: Dataset
Description: Soil samples collected monthly from 15 grassland sites in
             Oxfordshire, UK, analyzed for total organic carbon using
             loss-on-ignition method. Part of the Grassland Carbon
             Monitoring project.
Subjects: Soil Science; Carbon Cycle; Grassland Ecology
Related Identifiers:
  - IsSupplementTo: doi:10.1234/example-paper (the paper)
  - IsCompiledBy: doi:10.5281/zenodo.1234567 (the analysis code)
Funding: Natural Environment Research Council (Grant NE/X012345/1)
Rights: Creative Commons Attribution 4.0 International
Version: 1.0
Geolocation: Oxfordshire, UK (51.7°N, 1.2°W)
```

The rich metadata tells a much more complete story and enables many more discovery pathways.

### How Repositories Generate PID Metadata

When you deposit research outputs in a **trusted repository** (see [our chapter on repositories](rr-rdm-repository)), the repository handles PID creation and much of the metadata collection automatically:

1. **You provide information** through the repository's upload form (title, description, creators, and so on)
2. **The repository generates** a PID (usually a DOI) through its relationship with DataCite or Crossref
3. **The repository constructs** properly formatted PID metadata from your information
4. **The repository registers** the PID and metadata with the PID provider
5. **The PID provider makes** the metadata publicly searchable through their services
6. **The metadata is harvested** by aggregators and discovery services

This automated process is one of the key benefits of using established repositories rather than just hosting files on a personal or institutional website.

The repository also typically creates a **landing page** for your PID that displays the metadata in human-readable format and provides access to the resource itself.

(rr-rdm-pid-practical)=
## Practical Guidance

### When to Create PIDs for Your Research Outputs

PIDs are valuable for nearly any research output that you want others to be able to find, access, and cite.
Consider creating PIDs when:

**During research planning:**
- Data Management Plans that you want to cite in reports
- Registered protocols or preregistrations (see [registered reports](communication-reg))
- Experimental or computational protocols

**During research execution:**
- Raw datasets collected
- Processed or cleaned datasets
- Interim analysis results
- Computational notebooks documenting analysis steps
- Software or code developed for the project

**When preparing publications:**
- Preprints of articles
- Final datasets supporting publications
- Analysis code to reproduce results
- Presentations or posters about the work

**After publication:**
- Updated versions of datasets or code
- Educational materials derived from your research
- Null results or negative findings

PIDs are not just for "final" outputs - see our [chapter on research objects](communication-research-objects) for more on sharing throughout the research lifecycle.

### Repository-Based vs. Direct PID Minting

There are two main ways to obtain PIDs:

**Repository-based (recommended for most researchers):**
- **How it works**: Upload your output to a trusted repository, which creates the PID automatically
- **Advantages**:
  - Simpler - repository handles all technical details
  - Includes storage and preservation
  - Repository maintains the PID even if you move institutions
  - Established community trust
- **Examples**: Zenodo, Figshare, Dryad, OSF, institutional repositories

See our [chapter on selecting repositories](rr-rdm-repository) for guidance on choosing the right one.

**Direct minting (for specialized cases):**
- **How it works**: Your institution or organization registers PIDs directly with a PID provider
- **Advantages**:
  - More control over the process
  - Can integrate with custom systems
  - Useful for large-scale automated workflows
- **Considerations**:
  - Requires institutional infrastructure and expertise
  - Your institution must be a member of the PID provider
  - You're responsible for maintaining the PID and hosting the resource
  - May use services like [DataCite Fabrica](https://doi.datacite.org/)

For most researchers, repository-based PID creation is the appropriate choice.

### Understanding DOI Resolution

When you or someone else uses a DOI, here's what happens:

1. **A DOI is shared** (in a citation, link, or reference): `doi:10.5281/zenodo.3332807`
2. **It's formatted as a URL** to make it clickable: `https://doi.org/10.5281/zenodo.3332807`
3. **The doi.org resolver** looks up where the resource currently lives
4. **You're redirected** to the resource's current location (the landing page at Zenodo, in this example)
5. **The landing page** shows metadata and provides access to the resource itself

This is why DOIs should always be expressed as full URLs in online contexts:
- ✓ Good: `https://doi.org/10.5281/zenodo.3332807`
- ✗ Less useful: `10.5281/zenodo.3332807` (not clickable)
- ✓ Also good in text: `doi:10.5281/zenodo.3332807` (clear it's a DOI)

### Maintaining PIDs

One of the key advantages of using repository-based PIDs is that you don't need to maintain them yourself.
The repository ensures:

- **The PID continues to resolve** even if the repository's website is redesigned
- **The metadata stays accurate** and can be updated if needed
- **The resource remains accessible** according to the preservation policies
- **The landing page is maintained** with current access information

If you need to update metadata (for example, to add a link to a publication that cites your data), contact the repository where the resource is hosted.
Most repositories provide forms or help systems for metadata updates.

### What if a Resource Truly Disappears?

In rare cases, a resource may need to be removed (for example, if it's found to contain sensitive data that shouldn't have been shared).
Even then, the PID is not deleted:

- The PID continues to resolve to a **tombstone page**
- The tombstone explains why the resource is no longer available
- Any remaining metadata that can be safely shared is displayed
- This preserves the scholarly record and explains what happened

This is much better than a link that simply returns "404 Not Found" - it provides context and maintains the integrity of the citation network.

(rr-rdm-pid-connecting)=
## Connecting Research Through PIDs

PIDs are most powerful when they're used to connect related research outputs together.
For detailed guidance on how to link your research outputs, versions, and funding through PID metadata, see our [chapter on linking research objects](communication-citable-linking).

Key connections you can make:
- Link datasets to the papers that describe them
- Connect different versions of the same resource
- Tie research outputs to the grants that funded them
- Associate outputs with related resources like protocols or analysis code

(rr-rdm-pid-resources)=
## Additional Resources

### Learn More About PIDs

- [PIDforum community](https://www.pidforum.org/) - News and discussions about persistent identifiers
- [DataCite Support](https://support.datacite.org/) - Technical documentation and help
- [Crossref Resource Center](https://www.crossref.org/documentation/) - Documentation for Crossref services
- [ORCID Support](https://support.orcid.org/) - Help with ORCID iDs

### PID Services and Tools

- [doi.org](https://doi.org) - The main DOI resolver
- [DataCite Metadata Search](https://search.datacite.org/) - Search across millions of research outputs with DataCite DOIs
- [Crossref Metadata Search](https://search.crossref.org/) - Search publications with Crossref DOIs
- [ORCID Registry](https://orcid.org/) - Look up researchers and their works
- [ROR Registry](https://ror.org/) - Search for research organizations

### Related Chapters in The Turing Way

- [Making Research Objects Citable](communication-citable) - How to cite and get credit for all your research outputs
- [FAIR Principles](rr-rdm-fair) - Making research Findable, Accessible, Interoperable, and Reusable
- [Data Repositories](rr-rdm-repository) - Choosing where to deposit research outputs
- [Documentation and Metadata](rr-rdm-metadata) - How to describe your research effectively
- [Research Objects](communication-research-objects) - Sharing research throughout the lifecycle
- [Linking Research Objects](communication-citable-linking) - Creating connections between related outputs

:::{note}
Funding: This chapter was originally contributed as part of the dissemination efforts by the [Implementing FAIR Workflows project](https://doi.org/10.54224/20568), funded by [Templeton World Charity Foundation](https://www.templetonworldcharity.org/).
:::