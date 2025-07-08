(cm-ro-concepts)=
# Lifecycle
A RO commonly starts its life as an empty Live Research Object. ROs aggregate new objects through their whole lifecycle. This means, a RO is filled incrementally by aggregating new relevant resources such as workflows, datasets, documents that are being created, reused or repurposed. These resources can be modified at any point in time. 

We can copy and keep ROs in time through snapshots which reflect their status at a given point in time. Snapshots can have their own identifiers which facilitates tracking the evolution of a research. At some point in time, a RO can be published and archived (so called Archived Research Object) with a permanent identifier. New Live Research Objects can be derived based on an existing Archived Research Object.

# Typologies
We provide below some list of standard ROs described in the literature and emerging ones:

- Bibliography-centric: includes manuals, anonymize interviews, publications, multimedia (video, songs) and/or other material that support research.
- Data-centric: refers to datasets which can be indexed, discovered and manipulated. For further info of this typology, we suggest to check the section on {ref}`data papers <cm-dif-articles-data>`.
- Executable: includes the code, data and computational environment along with a description of the research object and in some cases a workflow. This type of ROs can be executed and is often used for scripts and/or Jupyter Notebooks.
- Software-centric: also known as “Code as a Research Object”. 
Software-centric ROs include source codes and associated documentation. 
They often include sample datasets for running tests. 
For further info of this typology, we suggest to check the section on {ref}`software papers <cm-dif-articles-software>`.
- Workflow-centric {cite:ps}`Belhajjame-ro-workflow2015`: contains workflow specifications, provenance logs generated when executing the workflows, information about the evolution of the workflow (version) and its components elements, and additional annotations for the workflow as a whole.
