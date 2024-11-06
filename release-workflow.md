# Workflow for Releasing Different Versions

We release the latest versions of the main repository including the content from _The Turing Way_ book on Zenodo (DOI for all versions: [10.5281/zenodo.3233853](https://doi.org/10.5281/zenodo.3233853)).
In this document, we describe the process for making a release on Zenodo through GitHub.

We don't describe how to connect a GitHub account/repository to a Zenodo account.
To learn more about that, please read the details in [the GitHub documentation](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).

## Updating release information

- Update [`CITATION.cff`](https://github.com/the-turing-way/the-turing-way/blob/main/CITATION.cff) file:
  - Update `version: 1.0.1` (currently in line 6), `date-released: "2021-11-10"` (currently in line 12)
- Validate the file locally on your computer using `cffconvert` (here we assume that the user knows how to use their terminal)
  - Step 1: Please install cffconvert using the following command: `python3 -m pip install --user cffconvert` (details here: https://pypi.org/project/cffconvert/)
  - Step 2: Run the following command: `cffconvert --validate`
  - Step 3: Once validated, create `.zenodo.json` file using the following command: `cffconvert --format zenodo > .zenodo.json`
  - Step 4: Create the pull request with the change -> review and merge it in the repository
  
Please note that we have currently left out individual names from the CITATION file, however, this is open for discussion if we will add all the authors manually or have some other automated ways to do that.

## Drafting release on GitHub

- Click on [the release option](https://github.com/the-turing-way/the-turing-way/releases) on GitHub main repository
- Draft a [new release](https://github.com/the-turing-way/the-turing-way/releases/new)
- Click 'Choose a tag', provide a new version name (such as v1.0.1, v1.02, ...) and click the 'create a new tag on release' option
- A note on when we consider a version to be [major, minor or patch](https://semver.org/):
  - patch: Small additions to chapters are patch such as bug fixing, editing or minor contributions between the Book Dashes
  - minor: Significant number of the new content & new chapters such as during a Book Dash
  - major: Major changes such as major re-arranging of chapters into different guides or addition of a new guide
- Create a release title such as 'v1.0.1 The Turing Way: 2021 release'
- Add details similar to what we have provided below that summarises what changes are in this version and provide a short sentence under the release log:

```
The Turing Way is an open source community-driven guide to reproducible, ethical, inclusive and collaborative data science. The Turing Way book is collaboratively developed by its diverse community of researchers, learners, educators, and other stakeholders.

The Turing Way project is openly developed and any questions, comments and recommendations are welcome at our GitHub repository: https://github.com/the-turing-way/the-turing-way. In 2020, the project underwent a major overhaul categorising chapters into 5 guides on reproducible research, project design, collaboration, communication and ethical research. Additionally, we added a community handbook to document all the practices designed and implemented towards the development of the project and community.

This release in 2021 includes additional chapters developed by our contributors across five guides and the community handbook. In addition, all the project documents from the project are provided as they appear on The Turing Way GitHub repository including the Zenodo metadata: https://github.com/the-turing-way/the-turing-way.

Release log:

    v1.0.1: Zenodo metadata information and additional chapters.
    v1.0.0: Five guide expansion of The Turing Way with a community handbook.
    v0.0.4: Continuous integration chapter merged to master.
    v0.0.3: Reproducible environments chapter merged to master.
    v0.0.2: Version control chapter merged to master.
    v0.0.1: Reproducibility chapter merged to master.

Full Changelog: v1.0.0...v1.0.1 (Previous release: v0.0.3...v1.0.0)
```
- Save draft

## Ready to Release

- When you are ready (and have double-checked the details), click 'Publish release'
- After a few seconds, you can see a new version appear at [https://doi.org/10.5281/zenodo.3233853](https://doi.org/10.5281/zenodo.3233853)

This is the workflow we have recently used and would work towards automating this process.
Meanwhile, to suggest any improvements, please contact _The Turing Way_ team by emailing [theturingway@gmail.com](mailto:theturingway@gmail.com).
