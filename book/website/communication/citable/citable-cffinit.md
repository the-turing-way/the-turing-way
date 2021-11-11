(cm-citable-cffinit)=
# (WIP) Create a `CITATION.cff` using CFFinit

Go to [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) and click on the "Create" button at the bottom.

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

On the first page of the application, enter the title of your work, write a message to indicate how you want your software to be mentioned, and select whether you are creating a `CITATION.cff` file for a software or dataset.

```{figure} ../../figures/cffinit-1.jpg
---
name: cffinit-1
width: 80%
alt: First page of the application, for Title, Message and Type. Fields are empty.
---
First page of the application, for Title, Message and Type. CC-BY-SA.
```

You can see the preview of the generated `CITATION.cff` file on the right.

If there are issues in any of the fields, an error message will be shown in red text, and the preview widget will have a red border around it.

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
Fill the relevant fields for authors. Adding their ORCID is recommended.

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
