(cm-citable-cffinit)=
# Create a `CITATION.cff` using `cffinit`

`cffinit` is a web application which helps users create a `CITATION.cff` file.
The application provides guidance for each field of the [CFF schema](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md) and does the validation automatically.
When there are issues, `cffinit` will provide a visual feedback on relevant fields.

In the following sections you can find details about each step of the process.

To get started, visit [`cffinit`](https://citation-file-format.github.io/cff-initializer-javascript/) and click on the "Create" button to continue to the **Start** screen.

```{figure} ../../figures/gifs/cffinit-0.gif
---
name: cffinit-0
width: 80%
alt: Landing page of cffinit.
---
Landing page of cffinit. [^cffinitversion]
```

[^cffinitversion]: All screen captures in this section refer to `cffinit` v2.0.0.

## Start

On the first page of the application, enter the title of your work, write a message to indicate how you want your software to be mentioned, and select whether you are creating a `CITATION.cff` file for software or a dataset.

```{figure} ../../figures/gifs/cffinit-1.gif
---
name: cffinit-1
width: 80%
alt: First page of the application, for Title, Message and Type. Fields are empty.
---
First page of the application, for Title, Message and Type. [^cffinitversion]
```

You can see the preview of the generated `CITATION.cff` file on the right.

If there are issues in any of the fields, they will be highlighted and error messages will be shown in red.
When the generated `CITATION.cff` file is not valid, the preview widget will have a red border.

```{note}
As title, message and author are required fields by the schema, these fields will be highlighted until you provide them.
```

Click next to continue to the **Authors** screen.

```{figure} ../../figures/gifs/cffinit-1-filled.gif
---
name: cffinit-1-filled
width: 80%
alt: First page of the form, for Title, Message and Type. Fields are filled.
---
First page of the form, for Title, Message and Type. Fields are filled. [^cffinitversion]
```

## Authors

The CFF schema requires at least one author in the `CITATION.cff` file.
Click the "Add author" button to open a form to do so.
Fill the relevant fields for authors.
Adding ORCID for authors is highly recommended.
See {ref}`cm-citable-orcid` to learn more about ORCID.

```{figure} ../../figures/gifs/cffinit-2.gif
---
name: cffinit-2
width: 80%
alt: Second page of the form, for Authors.
---
Second page of the form, for Authors. [^cffinitversion]
```

```{figure} ../../figures/gifs/cffinit-2-add-author.gif
---
name: cffinit-2-add-author
width: 80%
alt: Second page of the form, for Authors. Author addition in progress.
---
Second page of the form, for Authors. Author addition in progress. [^cffinitversion]
```

After adding one author, you have the minimum required information for a valid `CITATION.cff` file.
Add more authors as needed.
Click next afterwards to continue.

```{figure} ../../figures/gifs/cffinit-2-filled.gif
---
name: cffinit-2-filled
width: 80%
alt: Second page of the form, for Authors. One author filled.
---
Second page of the form, for Authors. One author filled. [^cffinitversion]
```

## Minimal `CITATION.cff` file

Well done!
Now your `CITATION.cff` file meets the minimum requirements.
In this screen you can download the generated file or copy it from the preview widget.
We highly recommend that you add more information.
Click the "Add more" button to add more fields to your citation file to make it even better.

```{figure} ../../figures/gifs/cffinit-3.gif
---
name: cffinit-3
width: 80%
alt: Last page of the minimal form.
---
Last page of the minimal form. [^cffinitversion]
```

## Additional fields

All additional fields are optional, but it is recommended that you fill the most relevant for your work.

```{note}
If you decide not to continue further, you can press the "Finish" button to skip all remaining steps and go to the final screen.
```

On this screen, you will see new steps in the stepper.
Here is a brief description of the additional screens:
- Identifiers: Add DOIs, URLs, and Software Heritage identifiers;
- Related resources: URLs of repositories related to the work and its website;
- Abstract: A short summary of the work;
- Keywords: Keywords describing the work;
- License: The license under which the work is available;
- Version specific: Information about a specific release or commit, including the date of the release.

```{figure} ../../figures/gifs/cffinit-3-advanced.gif
---
name: cffinit-3-advanced
width: 80%
alt: Third page of the form. More options appear on the left.
---
Third page of the form. More options appear on the left. [^cffinitversion]
```

Click next to start adding additional fields.

## Final screen

Great that you made it to the final screen!
After adding all the relevant information, you will have a validated `CITATION.cff` file.
Download or copy it and add it to your public repository to get the credit you deserve!

```{figure} ../../figures/gifs/cffinit-final.gif
---
name: cffinit-final
width: 80%
alt: Last page of the complete form.
---
Last page of the complete form. [^cffinitversion]
```
