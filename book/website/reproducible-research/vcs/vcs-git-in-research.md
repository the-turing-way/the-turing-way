(rr-vcs-git4research)=
# Git for research projects

## Potentials and issues

The use of a git repository for a research project is very appealing.
If one think of having all files for a project under a single folder, 
which is under git version control, one can solve several 
research data management, project management and collaboration issues,
all at once.
Here is a non-exhaustive list of features that this workflow could bring:

- Backup data by pushing the data to a git platform, toward a public or private repository
- Easily use different computers to work on the same project (with yourself of with collaborators).
- Keep track of contributions.
- Use templates to help with files organisation, see https://gin-tonic.netlify.app/standard/
- Use git platforms tools for project management
- Use git platforms for outreach, even when the repository is private (using the wiki)
- Create associated website 

As described in the  {ref}`general section about git<rr-vcs-git-limitations>`,
git does not work well when there are a lot of data, or when the data are large.
When you expect the project to get large, one needs to set a different tooling
to avoid creating unpractical repositories, see the {ref}`section on data version control<rr-vcs-data>` for a detailed explanation.

## Fictive exemple
 
Max has created a folder following a standard structure (section on data version control), they uses datalad to create submodules for each experiment,
where they will save their datasets.
Using datalad, the git-annex technology is used to save
the file content outside of the git repository at every push.
They got their own GIN platform where the git repository and git-annexed content
is saved, and backed up.
The data analysis code is also set in a submodule,
where git-annex is not allowed. 

After working for a couple of years on the project,
together with their collaborators, 
Max has written a paper where they could link both the data and the analysis code, 
which was made public by archiving the git repositories 
and the git-annexed data on the university library service.


While this use case is already possible,
it requires to use the command line (to use datalad),
and get a GIN instance installed 
(the public GIN instance is meant only for neuroscience data). 



