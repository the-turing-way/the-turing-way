(cm-citable-cff)=
# Software citation with CITATION.cff

## What is CITATION.cff (Abel)

The [Citation File Format](https://citation-file-format.github.io) lets you provide citation metadata for software or datasets in plaintext files that are easy to read by both humans and machines.
To provide this metadata, write a `CITATION.cff` file and ship it with your software or dataset.
A `CITATION.cff` file aggregates the information in a key-value format that can be easily interpreted and updated by humans, and easily parsed and converted with existing tools.

A `CITATION.cff` looks like the following (this examples is from [GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)):
```
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
- family-names: "Lisa"
  given-names: "Mona"
  orcid: "https://orcid.org/0000-0000-0000-0000"
- family-names: "Bot"
  given-names: "Hew"
  orcid: "https://orcid.org/0000-0000-0000-0000"
title: "My Research Software"
version: 2.0.4
doi: 10.5281/zenodo.1234
date-released: 2017-12-18
url: "https://github.com/github/linguist"
```
The complete list of fields is described in the [CFF specification](https://citation-file-format.github.io/specification/), but keep reading to find out which tools can help you create and use the `CITATION.cff` file.

## Why use CITATION.cff (Stephan)

When you do this, great things may happen:

- Users of your software can easily cite it using the metadata from CITATION.cff!
- If your repository is hosted on GitHub, they will show the citation information in the sidebar, which makes it easy for visitors to cite your software or dataset correctly.
- When you publish your software on Zenodo via the GitHub-Zenodo integration, they will use the metadata from your CITATION.cff file.
- People can import the correct reference to your software into the Zotero reference manager via a browser plugin.

## How to create a CITATION.cff file (Faruk)

The `CITATION.cff` is basically a `YAML` file with its own schema definition. The schema defines the rules for each field and which fields are required and which ones are optional. User needs to follow these rules to create a valid `CITATION.cff` file.

A minimal example of a valid CITATION.cff file, that contains only the required keys, would look like this:

```yaml
authors:
  - family-names: Druskat
    given-names: Stephan
cff-version: 1.2.0
message: "If you use this software, please cite it using these metadata."
title: "My Research Software"
```

However, adding more fields can help you have a more descriptive metadata of your software. The example below also provides important information of software such as version, release date, DOI, license, keywords.

```yaml
abstract: "This is my awesome research software. It does many things."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: "https://orcid.org/0000-0003-4925-7248"
cff-version: 1.2.0
date-released: "2021-07-18"
identifiers:
  - description: "This is the collection of archived snapshots of all versions of My Research Software"
    type: doi
    value: 10.5281/zenodo.123456
  - description: "This is the archived snapshot of version 0.11.2 of My Research Software"
    type: doi
    value: 10.5281/zenodo.123457
keywords:
  - "awesome software"
  - research
license: Apache-2.0
message: "If you use this software, please cite it using these metadata."
repository-code: "https://github.com/citation-file-format/my-research-software"
title: "My Research Software"
version: 0.11.2
```

### Steps to have your `CITATION.cff`

There are three steps:

#### 1. Creating the `CITATION.cff` file

There are two ways of creating a `CITATION.cff` file.
1. Editing the file manually in your favorite code editor. Disadvantage of this will be understanding relatively long error messages.
2. Using [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) which guides you through the process of creating your citation file.

#### 2. Validating your `CITATION.cff` file

Once the developer has `CITATION.cff` file, it needs to be validated to make sure there are no issues. You can validate your `CITATION.cff` file on the command line with the [`cffconvert` Python package](https://pypi.org/project/cffconvert/).

```shell
cffconvert --validate
```

If you prefer to use Docker, you can use the [`cffconvert` Docker image](https://hub.docker.com/r/citationcff/cffconvert):

```bash
cd <directory-containing-your-CITATION.cff>
docker run --rm -v ${PWD}:/app citationcff/cffconvert --validate
```

If you get error messages, look for the relevant validation error and fix it.

#### 3. Adding your `CITATION.cff` to a public code repository

After creating the `CITATION.cff` file you will need to add it to your GitHub repository so that GitHub can recognize it. For instructions please see [GitHub guide on software citation.](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

## How to cite using CITATION.cff (Abel)

You have found a software or dataset that contains a `CITATION.cff` that you want to cite in your publication.
You can, naturally, just copy the information on the file to whatever format you use, like BibTex or EndNote.
However, you can also use one of the tools or integrations available to do that automatically.

If the software or dataset you are using is available on GitHub, for instance, you can use GitHub's integration to just copy the information you need.

```{figure} ../../figures/github-cff-integration.png
---
name: github-cff-integration
alt: Button on GitHub that provides automatically conversion of the CITATION.cff file to APA's and BibTex's format.
---
"Cite this repository" automatically converts the `CITATION.cff` file to APA's and BibTex's format.
```

Alternatively, you can use external tools to convert the CITATION.cff file into the format you want.
See the next section for more information.

## Available tools for CITATION.cff (Abel and Faruk)

### cffinit

### cffconvert

### cff-validator GitHub Action

### Complete list of tools
https://github.com/citation-file-format/citation-file-format#tools-to-work-with-citationcff-files-wrench
