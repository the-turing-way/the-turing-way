(cm-citable-linking-versions)=
# Managing Versions Through PIDs

Research outputs often evolve over time: you might fix errors in a dataset, improve code, or update protocols.
Persistent identifiers provide structured ways to handle versioning while maintaining clear connections between versions.

## Version DOIs vs. Concept DOIs

Some repositories (notably [Zenodo](https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning)) implement a two-level DOI system:

Version DOI
: A version DOI points to one specific version of a resource and never changes. Use this when you want to cite a specific version for reproducibility. For example: `10.5281/zenodo.3332807` (version 1.0).

Concept DOI
: A concept DOI points to the resource as a whole, across all versions, and always resolves to the latest version. Use this when you want to cite the work in general. For example: `10.5281/zenodo.3332806` (concept, always latest).

The concept DOI creates an umbrella that links all versions together.
When you publish a new version, it gets a new version DOI, but the concept DOI remains the same.

## When to Create a New Version vs. New Resource

You should create a new version when the fundamental resource remains the same but has been improved or corrected. This includes situations like fixing errors or bugs, adding new data points to an existing dataset, improving documentation or metadata, or making minor methodological adjustments. The key characteristic of a new version is that it represents an evolution or refinement of the original resource rather than a fundamentally different output.

In contrast, you should create an entirely new resource when the changes are substantial enough that the output could stand alone independently. This applies when you're collecting fundamentally different data, completely redesigning a protocol, or making major methodological changes that alter the nature of the work. These situations call for a new DOI rather than a new version because the new output represents distinct scholarly work.

When in doubt, ask yourself: "Would citing the old version still be valid and useful?" If yes, create a new version. If no, create a new resource.

## How to Publish New Versions

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

## Version Metadata Links

Whether or not your repository has automatic version handling, you can explicitly link versions through connection metadata.

## Best Practices for Versioning

- **Document changes**: Include a changelog or version notes explaining what changed
- **Preserve old versions**: Don't delete previous versions - persistence is the point of PIDs
- **Update related resources**: If you publish a new dataset version, consider whether related code or documentation needs updating too
- **Cite specific versions in papers**: For reproducibility, cite the exact version used, not the concept DOI
- **Use concept DOIs for general reference**: When recommending a resource (in documentation, teaching), use the concept DOI so people get the latest version
- **Communicate updates**: If others have cited your work, consider contacting them about significant improvements
