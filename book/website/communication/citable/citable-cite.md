(cm-citable-cite)=
# Citing Research Objects

You should cite research objects directly in the paper in places where it is relevant.
This is a commonly practised way of citing publications and is valid for citing other research components like data and software.
A citation includes the following information:
- Author
- Title
- Year of publication
- Publisher (for data, this is often the data repository where it is housed),
- Version (if indicated)
- Access information (a URL or DOI)

A citation style is a specific arrangement, order and formatting of information necessary for a citation.
For instance, the MLA style was developed by Modern Language Association (originally used in the humanities) and the APA style was developed by American Psychological Association (originally used in psychology and the social sciences).
- MLA citation style uses the following format:
`Author. "Title of the Source." Title of the Container, Other contributors, Version, Number, Publisher, Publication date, Location.`
- APA citation style uses the following format:
`Author. (Year). Title of data set (Version number). [Retrieved from] ***OR*** [DOI]`

See [Scribbr Citation Styles Guide](https://www.scribbr.com/citing-sources/citation-styles/).
See also [FORCE11 resource](https://www.force11.org/node/4771).

(cm-citable-cite-data)=
## Citing Data

When sharing a dataset, use dedicated DOIs and add a **data availability statement** at the end of the paper or in online repository details (similar to the acknowledgement section).

You can find examples of these statements in the publishers' (research data) author policies.

### Data availability statement examples:

**Using the Digital Object Identifier (DOI):**
“The data that support the findings of this study are openly available in [repository name] at http://doi.org/[doi].”

**If no DOI is issued:**
- “The data that support the findings of this study are openly available in [repository name] at [URL], reference number [reference number].”

**When there is an embargo period you can reserve your DOI and still include a reference to the dataset in your paper:**
- “The data that support the findings will be available in [repository name] at [URL / DOI] following a [6 month] embargo from the date of publication to allow for the commercialisation of research findings.”

**When data cannot be made available:**
- “Restrictions apply to the data that support the findings of this study.
[Explain nature of restrictions, for example, if the data contains information that could compromise the privacy of research participants] Data are available upon reasonable request by contacting [name and contact details] and with permission of [third party name].”
-  “The data that support the findings of this study are available upon request.
Access conditions and procedures can be found at [URL to restricted access repository such as [EASY](https://easy.dans.knaw.nl/ui/home).]”

**More Data Availability Statement examples:**

You can find more examples on the [Manchester's Data Access Statements page](https://www.library.manchester.ac.uk/using-the-library/staff/research/research-data-management/sharing/data-access-statements/), the [Cambridge Data Availability Statement examples](https://www.cambridge.org/core/services/authors/open-data/data-availability-statements), the [AMS Data Availability Statement examples](https://www.ametsoc.org/index.cfm/ams/publications/author-information/formatting-and-manuscript-components/data-availability-statement-examples/), or [Nature's Tips for writing a dazzling Data Availability Statement](https://researchdata.springernature.com/posts/tips-for-writing-a-dazzling-das-data-availability-statement).

(cm-citable-cite-software)=
## Citing Software

A software citation has a lot of the same elements as a data citation, described above, and are described in more detail in the [Software Citation Principles](https://www.force11.org/software-citation-principles).
When using others software, it is vital to cite and attribute it properly.

To make your code citable, you can use the integration between [Zenodo](https://zenodo.org/) and GitHub.

- Create a file to tell people how to cite your software. Use this [handy guide](https://citation-file-format.github.io/cff-initializer-javascript/) to format the file.
- Link your GitHub account with a Zenodo account. This guide explains [how](https://guides.github.com/activities/citable-code/).
- You can tell Zenodo what information or metadata you want to include with your software by adding a `zenodo.json` file, described [here](https://guide.esciencecenter.nl/citable_software/making_software_citable.html).
- On Zenodo, flip the switch to the 'on' position for the GitHub repository you want to release.
- On GitHub, click the *Create a new release* button.
Zenodo should automatically be notified and should make a snapshot copy of the current state of your repository (just one branch, without any history), and should also assign a persistent identifier (DOI) to that snapshot.
- Use the DOI in any citations of your software and tell any collaborators and users to do the same!
