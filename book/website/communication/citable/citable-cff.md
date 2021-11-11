(cm-citable-cff)=
# (WIP) Software Citation with CITATION.cff

The [Citation File Format](https://citation-file-format.github.io) lets you provide citation metadata for software or datasets in plaintext files that are easy to read by both humans and machines.
To provide this metadata, create a `CITATION.cff` file and include it with your software or dataset.
A `CITATION.cff` file aggregates the information in a key-value format that can be easily interpreted and updated by humans, and easily parsed and converted with existing tools.

(cm-citable-cff-why)=
## Why Use `CITATION.cff`?

There are great advantages in using a `CITATION.cff` file for the citation information for your software!

It's *easier for you*: When you host your software source code on GitHub and have a `CITATION.cff` in your repository, you can use the Zenodo-GitHub integration to automatically publish new releases of the software. Zenodo will use the information from `CITATION.cff` and show it together with the publication. You don't have to edit this information manually on Zenodo anymore.

It's *easier for the users of your software*:
1. They can directly use the citation information from `CITATION.cff` to cite your software.
2. If your source code is on GitHub, they will show the citation information in the sidebar as a formatted citation, and also in the BibTeX format. Users can copy either, paste it into their manuscripts, and cite your software correctly.
3. If they use the Zotero reference manager, they can import the citation metadata directly from the `CITATION.cff` file in the GitHub repository to their reference manager.

(cm-citable-cff-how-to-create)=
## How to Create a `CITATION.cff` File (Faruk)

The `CITATION.cff` is a `YAML` file with its own schema definition. The schema defines the rules for each field and which fields are required and which ones are optional. The user needs to follow these rules to create a valid `CITATION.cff` file.

A minimal example of a valid `CITATION.cff` file, that contains only the required keys, would look like this:

```yaml
authors:
  - family-names: John
    given-names: Doe
cff-version: 1.2.0
message: "If you use this software, please cite it using the metadata from this file."
title: "My research software"
```

However, adding more fields can help you have more descriptive metadata of your software. The example below also provides important information of software such as version, release date, DOI, license, keywords.

```yaml
abstract: "This is my awesome research software. It does many things."
authors:
  - family-names: John
    given-names: Doe
    orcid: "https://orcid.org/0000-0001-8888-9999"
cff-version: 1.2.0
date-released: "2021-10-13"
identifiers:
  - description: "This is the collection of archived snapshots of all versions of My Research Software"
    type: doi
    value: 10.5281/zenodo.123456
  - description: "This is the archived snapshot of version 0.11.2 of My Research Software"
    type: doi
    value: 10.5281/zenodo.123457
keywords:
  - "amazing software"
  - research
license: Apache-2.0
message: "If you use this software, please cite it using the metadata from this file."
repository-code: "https://github.com/citation-file-format/my-research-software"
title: "My Research Software"
version: 0.11.2
```

The complete list of fields is described in the [CFF schema guide](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md). In the next section you can find out which tools can help you create and use the `CITATION.cff` file.

### Steps to Make Your Software Citable

To make your software citable you need to follow the three steps below.

#### Step 1. Create a `CITATION.cff` File

There are two ways of creating a `CITATION.cff` file.

1. Editing the file manually in your favorite code editor. The disadvantages of this method are installing the required tools on your system and doing the validation yourself. The error messages of the validation can be relatively long and difficult to understand.

2. Using [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) which guides you through the process of creating your citation file. The `cffinit` has a few advantages over manual editing such as

    - no need for installing extra tools;
    - no need for automatic validation;
    - guidance for each fields;
    - visual feedback to indicate issues.

We suggest the second method, which we will describe with more details now.

Go to [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/), click on the "Create" button at the bottom.

```{figure} ../../figures/cffinit-0.jpg
---
name: cffinit-0
width: 80%
alt: Landing page of cffinit.
---
Landing page of cffinit. CC-BY-SA.
```

Below you can find details about each step of the process.

##### Start screen

In the first page of the application, enter the title of your work, write a message to indicate how your software to be mentioned, and select whether you are creating the `CITATION.cff` file for a software or a dataset.

```{figure} ../../figures/cffinit-1.jpg
---
name: cffinit-1
width: 80%
alt: First page of the application, for Title, Message and Type. Fields are empty.
---
First page of the application, for Title, Message and Type. CC-BY-SA.
```

You can see the preview of the generated `CITATION.cff` file on the right.

If there are issues in the fields, the error message will be shown in red text and the preview widget will have a red border around it.

The error message should disappear from this screen after you have filled the required fields, although the border of the generated CFF will remain red until you have filled all the required fields.
Click next to continue to Authors screen.


```{figure} ../../figures/cffinit-1-filled.jpg
---
name: cffinit-1-filled
width: 80%
alt: First page of the form, for Title, Message and Type. Fields are filled.
---
First page of the form, for Title, Message and Type. Fields are filled. CC-BY-SA.
```

##### Authors screen

The CFF schema requires at least one author in the `CITATION.cff` file.
Click the "Add author" button to open a form for adding an author.
Fill the relevant fields for authors. Adding the ORCID is recommended.

```{figure} ../../figures/cffinit-2.jpg
---
name: cffinit-2
width: 80%
alt: Second page of the form, for Authors.
---
Second page of the form, for Authors. CC-BY-SA.
```
```{figure} ../../figures/cffinit-2-add-author.jpg
---
name: cffinit-2-add-author
width: 80%
alt: Second page of the form, for Authors. Author addition in progress.
---
Second page of the form, for Authors. Author addition in progress. CC-BY-SA.
```

After adding one author, you have the minimum required information for a CFF file.
Add more authors as needed.
Click next afterwards to continue.

```{figure} ../../figures/cffinit-2-filled.jpg
---
name: cffinit-2-filled
width: 80%
alt: Second page of the form, for Authors. One author filled.
---
Second page of the form, for Authors. One author filled. CC-BY-SA.
```
##### (TODO: Check the title)

Well done! Now your `CITATION.cff` file meets the minimum requirements. In this screen you can download the CFF file or copy it from the preview widget.
We highly recommend to add more information.
Click the "Add more" button for that.

```{figure} ../../figures/cffinit-3.jpg
---
name: cffinit-3
width: 80%
alt: Last page of the minimal form.
---
Last page of the minimal form. CC-BY-SA.
```

##### (TODO: Check the title)

All additional keys are optional, but it is recommended that you fill the most relevant for your work.

Here is a brief description of each screen:
- Identifiers: Add DOIs, URLs, and Software Heritage identifiers;
- Related resources: URLs of repositories related to the work and its website/landing page;
- Abstract: A short summary of the work;
- Keywords: Keywords describing the work;
- License: The license under which the work is available;
- Version specific: Information about a specific release or commit, including the date of the release.

```{figure} ../../figures/cffinit-3-advanced.jpg
---
name: cffinit-3-advanced
width: 80%
alt: Third page of the form. More options appear on the left. CC-BY-SA.
---
Third page of the form. More options appear on the left.
```

##### (TODO: Check the title)

After adding all the relevant information, or clicking `finish` to skip, you will have the validated CFF file.
Download or copy it and you are ready to use it.

```{figure} ../../figures/cffinit-final.jpg
---
name: cffinit-final
width: 80%
alt: Last page of the complete form.
---
Last page of the complete form. CC-BY-SA.
```
#### Step 2. Validate Your `CITATION.cff` File

```{note}
If you used `cffinit` to create your `CITATION.cff`, then you can skip to [step 3](citable-cff.html#add-your-citation-cff-to-a-public-code-repository).
```

Once you have a `CITATION.cff` file, it needs to be validated to make sure there are no issues. You can validate your `CITATION.cff` file on the command line with the [`cffconvert` Python package](https://pypi.org/project/cffconvert/).

```shell
cd <directory-containing-your-CITATION.cff>
cffconvert --validate
```

If you prefer to use Docker, you can use the [`cffconvert` Docker image](https://hub.docker.com/r/citationcff/cffconvert):

```bash
cd <directory-containing-your-CITATION.cff>
docker run --rm -v ${PWD}:/app citationcff/cffconvert --validate
```

If you get error messages, look for the relevant validation error and fix it.

To make sure that your GitHub repository always has a valid `CITATION.cff` file, you can use the GitHub Action [cff-validator](https://github.com/marketplace/actions/cff-validator).

#### Step 3. Add Your `CITATION.cff` to a Public Code Repository

After creating a `CITATION.cff` file you will need to add it to your GitHub repository so that GitHub can recognize it. GitHub already has instructions to show how to do this.For instructions please see [GitHub guide on software citation.](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

(cm-citable-cff-how-to-cite)=
## How to Cite Using `CITATION.cff` (Abel)

If you have found a software or dataset that contains a `CITATION.cff`, there are a few ways to obtain the reference information to cite it in your publication.

- You can use one of the tools, such as the `cffconvert` command line program, to convert your `CITATION.cff` file to one of the [supported formats](https://github.com/citation-file-format/cff-converter-python#supported-output-formats), such as APA, BibTeX or EndNote.

- Alternatively, if the software or dataset you want to cite is available on GitHub, you can use GitHub's interface to copy the reference in either APA or BibTeX formats, by clicking the "Cite this repository" button (see the green area in the image below).

  ```{note}
  "Cite this repository" button only appears when there is a `CITATION.cff` file on the repository.
  ```

  ```{figure} ../../figures/github-cff-integration.jpg
  ---
  name: github-cff-integration
  alt: Button on GitHub that provides automatically conversion of the `CITATION.cff` file to APA's and BibTex's format.
  ---
  "Cite this repository" automatically converts the `CITATION.cff` file to APA's and BibTex's format.
  ```

(cm-citable-cff-available-tools)=
## Available Tools (Abel and Faruk)

Several tools exist to facilitate the creation and validation of `CITATION.cff` files, as well as the conversion to and from other formats.
See the [table at the repository's specification](https://github.com/citation-file-format/citation-file-format#tools-to-work-with-citationcff-files-wrench) for a list of all known tools.

<!--
Below we list a few of the main ones.

### cffinit

The web application [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) provides an interactive way of creating a `CITATION.cff` file online.
The app provides a simple interface to create your first `CITATION.cff` file.
You can use it to add the bare minimum of information or you can add optional, but very important, fields, like the DOI, code repository, release date, etc.
This approach is recommended due to having validation built-in.

### cffconvert

[cffconvert](https://github.com/citation-file-format/cff-converter-python) is a command line program to validate and convert `CITATION.cff` files.
It can be used to convert to other formats, like BibTex, EndNote, and Zenodo, as well as validate `CITATION.cff` files locally or in GitHub repositories.
-->