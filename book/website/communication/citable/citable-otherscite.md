(cm-citable-otherscite)=
# Citing other people's Research Objects
[![](https://img.shields.io/static/v1?label=pathway&message=Research%20Software%20Engineers&color=white)](/research-software-engineers.md)
[![](https://img.shields.io/static/v1?label=pathway&message=Software%20Citation&color=green)](/software-citation.md)

When citing research objects from other people/researchers, ensure you verify when, where, and how to properly cite those research objects.
Below, we provide a brief explanation for each of these three scenarios.

(cm-citable-otherscite-when)=
## When to cite a research object?

As a rule-of-thumb, every research object that plays a significant role in your research project should be cited in you publication or methodology paper. 
For example, when using others software to analyse your research data, it is vital to cite and attribute it properly.
In some cases, the contribution of a research object may be small but critical to your results.
You should always consider about giving credit to others for their work, showing gratitude to them, and try to implement more repeatable science {cite:ps}`LaZerte2021`

If you are unsure about what to cite because you doubt the contribution of a particular research object to your research, you can answer the following questions from {cite:ps}`ShouldICite`
- Does the software ask you to cite it?
- Did the software play a critical part in, or contributed something unique to, your research?
- Did the software manipulate or create your data? This includes storage, visualization, and communication of your data and results.
- Do the authors of the software rely on academic credit for funding? Look for academic institutions in email addresses, URLs.

If the answer to any of these questions is yes, then you must/need to cite that research object.

(cm-citable-otherscite-where)=
## Where to cite a research object?

You should directly cite research objects from others in you publication where relevant.
For example, if specific software was used to process data, it should be cited in the section describing the processing. 
Similarly, if all the figures in a publication are created using the same software, it may be more useful to mention that software in the main text or acknowledgements. 
Another example is when videos or images from others are explicitly mentioned; this as an opportunity to cite those research objects. 
In such cases, these research objects should commonly be included in the reference section. 

However, it is important to note that citation practices may change depending on the publisher's guidelines.
The best practice is to pair citations in the reference section with in-text citations {cite:ps}`Stall2023`.
This approach avoids mentioning datasets or software in footnotes or only in supplementary materials, where clear citations may not be provided.
In cases where a research object was used as a test or pilot but did not play a role in the final publication, it is possible to mention these in the acknowledgements section.
This ensures proper credit is given, even if the object was not ultimately used.

Finally, availability statements should usually be reserved for research objects produced during your project, and not for those created by others.
Therefore, avoid using these statements to refer to the work of others. 

(cm-citable-otherscite-how)=
## How to cite a research object?

Ideally, other people's research objects would have a persistent identifier to make citation easier to others.
In some cases, published research objects may include a statement on how to cite their research objects. 
A common practise of citing other people's work (such as publications) is also valid for citing other research objects (e.g., data, software, images, presentations, workflows, etc.).
A citation includes the following information:
- Author(s)
- Title
- Year/Date of publication
- Publisher or Repository (in repositories you can describe the type of research object, e.g. [Dataset], [Software], [Presentation])
- Version (if indicated)
- Access information (a URL or DOI)

Like a regular citation, citing a research object is done in a specific citation style. 
A citation style is a specific arrangement, order and formatting of information necessary for a citation.
For instance, the MLA style was developed by Modern Language Association (originally used in the humanities) and the APA style was developed by American Psychological Association (originally used in psychology and the social sciences). 
A specific citation style may also be requested by the journal you are publishing in.
- MLA citation style uses the following format:
`Author. "Title of the Source." Title of the Container, Other contributors, Version, Number, Publisher, Publication date, Location.`
- APA citation style uses the following format:
`Author. (Year). Title of data set (Version number). [Retrieved from] ***OR*** [DOI]`

There are many citation styles available (e.g., see [Scribbr Citation Styles Guide](https://www.scribbr.com/citing-sources/citation-styles/)), and fortunately, there are several web interfaces to generate those citations. 
If you have the DOI of the research object, you can use tools like [CiteAs](https://citeas.org/ ) or [DOI2bib](https://www.doi2bib.org/) to directly obtain the citation in a given citation style or as a [BibTex](https://en.wikipedia.org/wiki/BibTeX) format. 

Another approach is to find sources where the citation is already available in BibTex format and then apply the desired style in Latex.
For example, for R packages you can use `citation(PACKAGE_NAME)` to check if the package has a defined citation preference (e.g., a paper instead of a link to the code repository URL), as explained in {cite:ps}`LaZerte2021`. 
