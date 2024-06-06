(er-making-tea-fair)=
# Making TEA FAIRer

In this section we will look at the application of the FAIR principles to the TEA platform.
We will discuss why it is important to consider the FAIRness (or FAIRification) of assurance cases, as well as how the FAIR principles can help the TEA platform promote open and reproducible ways of working.

```{note} What are the FAIR principles?
You can find an introduction to the FAIR principles in the [Guide to Reproducible Research]() section of the Turing Way.
In short, the FAIR principles stand for 'findability', 'accessibility', 'interoperability', and 'reusability'.

They serve as a set of guidelines aimed at enhancing the management and governance of data.
Collectively, they emphasise the importance of making data easily and openly available for both human users and computers (e.g. ‘interoperability’ to allow software to effectively interpret, process, and integrate data from various sources).
```

## Why do the FAIR principles matter in the context of the TEA Platform?

The simple answer to this question is as follows:

> Assurance cases are structured data. As such, the FAIR principles apply to them.

However, this initial response ignores some of the more interesting nuances that are worth discussing.

While the FAIR principles were originally developed for the purpose of governing datasets, some within the community have since applied them to broader tools and resources (e.g. the Data Stewardship Wizard for creating Data Management Plans that adhere to FAIR best practices {cite}`dsw2024`).
Such tools can help projects at different stages of a project’s lifecycle, either by helping with the “FAIRification” of data (e.g. automating documentation or consistent metadata), or by enabling teams to answer reflective questions such as “how FAIR are we currently?” {cite}`deutz2020,thompson2020`.

As a result of this wider scope, the FAIR principles can be used to scaffold ongoing design and devlopment of the TEA platform itself.
Let's look at some examples:

````{tab-set}
```{tab-item} Findability
- **Metadata and Standardised Tagging**: Implementing detailed metadata for all fields used in assurance cases can enhance findability. This includes tagging evidence, claims, and arguments with standardised and searchable tags (e.g. claim about ‘bias mitigation’, ‘evidence related to a particular standard’), making it easier to locate relevant information.
- **Open (and Public) Repositories**: Establishing open and public repositories where assurance cases can be shared, stored, indexed, and searched can significantly improve the ability to find necessary information and build shared best practices.
```

```{tab-item} Accessibility
- **Extensibility through APIs**: Developing and maintaining APIs that allow for programmatic access to assurance case data can facilitate automated systems in retrieving and processing this information, and help build extensible platforms that allow the community to build new capabilities based on their own needs.
- **Clear Access Control Policies**: Implementing clear, well-documented access control policies ensures that data is accessible to authorised people or systems while maintaining security and confidentiality where required.
At present, the TEA platform supports basic sharing (e.g. importing/exporting) and can be deployed within an organisation using our source code (or public Docker images). However, further work will be required to ensure access control is fit-for-purpose across different contexts (e.g. in organisations that make use of sensitive information).
```

```{tab-item} Interoperability
- **Standardised Data Formats**: While perhaps an obvious point to make, using standardised data formats (e.g., XML, JSON) for assurance cases ensures that different tools and systems can easily exchange and process this data. Currently, the TEA platform uses JSON as the primary data format, but this diverges from other approaches, such as Structured Assurance Case Metamodel (SACM)—a framework defined by the Object Management Group (OMG) for representing structured assurance cases—that proposes the use of XMI documents that conform with the SACM XML Schema.
- **Common Frameworks and Ontologies**: Related to the previous point, adopting common frameworks and ontologies for assurance cases promotes a shared understanding and compatibility between different systems and organisations. The TEA platform has not, hitherto, aimed for the same expressivity as other frameworks or ontologies (e.g. GSN and SACM), because we have prioritised accessibility of arguments for non-technical stakeholders to promote a more accessible and inclusive assurance ecosystem, which is vital to TEA. However, future research will explore how convergence with other frameworks can be achieved, and how much is desirable.
```

```{tab-item} Resuability
- **Modular Design of Assurance Cases**: Designing assurance cases in a modular fashion, where components like evidence, claims, and argument structures can be reused in different contexts, enhances reusability. 
- **Comprehensive Documentation**: Ensuring comprehensive documentation is vital to ensure that knowledge can be derived from assurance cases and allowing this knowledge to be reused—perhaps in different domains or contexts. This is also an important aspect of building capabilities within the assurance ecosystem and community.
```
````

The above points should, hopefully, demonstrate the value of adopting the FAIR principles as a lens with which to evaluate an in-progress and open project.
