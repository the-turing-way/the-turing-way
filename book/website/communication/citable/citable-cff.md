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

## How to create a CITATION.cff file and use it (Faruk)
 - mention cffinit
 - use https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files

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
