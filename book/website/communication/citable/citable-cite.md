(cm-citable-cite)=
# Citing your own Research Objects

When citing your own research objects, it is important to consider the type of research object you are referring to. 
Here, we provide explanations for citing data, physical samples, and software.

(cm-citable-cite-data)=
## Citing Data
When sharing a dataset, use the assigned DOI (from the data repository) and add this to your data availability statement at the end of the paper (similar to the acknowledgement section). 
It is important to also cite your dataset in the references themselves, as only the citations in the reference section will contribute to citation counts.
Data citation is important because it facilitates access, transparency and potentially reproducibility, reuse, and credit for researchers, and might be required when data is shared under a license that requires citation (for example, CC-BY). For more information check the chapter about {ref}`rr-licensing`.

Data citation also provides recognition and visibility for the repositories that share data.

You can find examples of these statements in the publishers' (research data) author policies.

### Data availability statement examples:

**Using the Digital Object Identifier (DOI):**
- “The data that support the findings of this study are openly available in [repository name] at http://doi.org/[doi].”

**If no DOI is issued:**
- “The data that support the findings of this study are openly available in [repository name] at [URL], reference number [reference number].”

**When there is an embargo period you can reserve your DOI and still include a reference to the dataset in your paper:**
- “The data that support the findings will be available in [repository name] at [URL / DOI] following a [6 month] embargo from the date of publication to allow for the commercialisation of research findings.”

**When data cannot be made available:**
- “Restrictions apply to the data that support the findings of this study.
[Explain nature of restrictions, for example, if the data contains information that could compromise the privacy of research participants] Data are available upon reasonable request by contacting [name and contact details] and with permission of [third party name].”
-  “The data that support the findings of this study are available upon request.
Access conditions and procedures can be found at [URL to restricted access repository such as [EASY](https://easy.dans.knaw.nl/ui/home).]”

**When code is shared:**
- "Data and code to reproduce the results shown in the paper can be obtained from The Turing Way (2023) at Zenodo ([https://zenodo.org/doi/10.5281/zenodo.3233853](https://zenodo.org/doi/10.5281/zenodo.3233853)) and GitHub ([https://github.com/the-turing-way/the-turing-way](https://github.com/the-turing-way/the-turing-way)). We used R version 4.2.2 (*use citation() to check the suggested citation*) and the following R packages: ggplot2 ([Wickham 2016](https://cran.r-project.org/web/packages/ggplot2/citation.html)), another example (*and citation added to the references!*)." 

**More Data Availability Statement examples:**

You can find more examples on the [Manchester's Data Access Statements page](https://www.library.manchester.ac.uk/services/research/research-data-management/sharing/data-access-statements/), the [AMS Data Availability Statement examples](https://www.ametsoc.org/index.cfm/ams/publications/author-information/formatting-and-manuscript-components/data-availability-statement-examples/), or [Nature's Tips for writing a dazzling Data Availability Statement](https://researchdata.springernature.com/posts/tips-for-writing-a-dazzling-das-data-availability-statement).

(cm-citable-cite-samples)=
## Citing Physical Samples

When sharing results related to physical samples (such as archaeological material, genomics samples), ideally a persistent identifier is assigned to track the samples and their associated data. 
As with [data citation](#cm-citable-cite-data), you include a citation in the references and a more detailed explanation in the data availability statement. 
To learn more about how to cite physical samples and to check out examples, see the [Scientific Author Guide for Publishing Open Research Using Physical Samples](https://doi.org/10.6084/m9.figshare.24669057.v1) by {cite:ps}`Damerow2024physical`.

(cm-citable-cite-software)=
## Citing Software

A software citation has a lot of the same elements as a data citation, described above, and are described in more detail in the [Software Citation Principles](https://www.force11.org/software-citation-principles).
Depending on the journal, you may also include a Software/Code Availability Statement. In such section, you can describe where the code developed during the research presented in the paper can be found, similar to how you would provide information about data availability.
For an example you can look at the [Data and Code Availability Statements - Sample text](https://social-science-data-editors.github.io/guidance/Requested_information_dcas.html) or [Availability Statement Templates](https://www.agu.org/publish-with-agu/publish/author-resources/data-and-software-for-authors).

::::{tab-set}
:::{tab-item} GitHub
:sync: github_tab
To make your code citable, you can use the integration between [Zenodo](https://zenodo.org/) and GitHub.

- Create a file to tell people how to cite your software. Use this [handy guide](https://citation-file-format.github.io/cff-initializer-javascript/) to format the file.
- Link your GitHub account with a Zenodo account. This guide explains [how](https://guides.github.com/activities/citable-code/).
- You can tell Zenodo what information or metadata you want to include with your software by converting your `CITATION.cff` file to `zenodo.json`.

    ```bash
    pip install cffconvert
    cffconvert --validate
    cffconvert --format zenodo --outfile .zenodo.json
    ```

- Add `.zenodo.json` to your repository.
- On Zenodo, flip the switch to the 'on' position for the GitHub repository you want to release.
- On GitHub, click the *Create a new release* button.
Zenodo should automatically be notified and should make a snapshot copy of the current state of your repository (just one branch, without any history), and should also assign a persistent identifier (DOI) to that snapshot.
- Use the DOI in any citations of your software and tell any collaborators and users to do the same!

:::
:::{tab-item} GitLab
:sync: gitlab_tab



To make your code citable, through an automated publication of your Gitlab repository to [Zenodo](https://zenodo.org/):

- Create a file to tell people how to cite your software. Use this [handy guide](https://citation-file-format.github.io/cff-initializer-javascript/) to format the file.
- Convert your `CITATION.cff` file to `.zenodo.json`.
This file tells Zenodo what information or metadata you want to include with your software.

    ```bash
    pip install cffconvert
    cffconvert --validate
    cffconvert --format zenodo --outfile .zenodo.json 
    ```

- Add `.zenodo.json` to your repository.
- Use the [gitlab2zenodo](https://gitlab.com/sbeniamine/gitlab2zenodo) package to publish a snapshot of your repository to your Zenodo instance.
By following the installation and setup instructions of this package, you will get a workflow on your {ref}`CI <rr-ci-options>` that will take care of the publication to Zenodo.
- Use the DOI in any citations of your software and tell any collaborators and users to do the same!

```{note}
If you don't have a Zenodo record for your software yet when you attempt to publish it for the first time, you may encounter an error due to the undefined `ID`. 
To address this issue, we recommend manually creating a record on Zenodo and updating the value of the {ref}`CI <rr-ci-options>` variable `zenodo_record`. 
Detailed instructions for this process can be found in the [gitlab2zenodo](https://gitlab.com/sbeniamine/gitlab2zenodo) installation and setup instruction.
```

:::
::::
