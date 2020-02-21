# Translation Guide

## How to join a translation team?

Go to [Transifex](https://www.transifex.com/theturingway/theturingway/) and click "Help Translate TheTuringWay" (button in blue).
<!-- TODO Screenshots to be added -->

## How to start a new translation?

- Clone [`po4jupyterbook`](https://github.com/tonyyzy/po4jupyterbook) to the root directory of the project  
    `git clone https://github.com/tonyyzy/po4jupyterbook`
- In `book/content` the `po` folder contains the POT and PO files. POT files are generated from the Markdown files and contains the original strings of the book; PO files contain the original string and their translations.
- To start a new language
    - add the [language's ISO](https://www.transifex.com/explore/languages/) code to `book/content/po/LINGUAS`
        - also add the language code to the `keep_files` list of [`book/website/_config.yml`](book/website/_config.yml)
    - Copy all the POT files to make corresponding PO files.  
        `for i in *.pot; do echo $i; cp $i ${i::-4}.<LANG>.po; done`
    - To compile the POs to translated Markdown files, you are required to fill in the header section of the PO files. Please see existing PO files for an example of dummy data. The compilation process will fail if the header information is not filled in. The PO files submitted by Transifex should have these filled in.
- When the Markdown files are updated, you will need to update the POT files for the new strings to show up in Transifex.  
  Under `book/content` run `../../po4jupyter/create.sh`
    - This will update the POT files to track the modified Markdown files. Because there are timestamps in the POT files, git will always show there is something to commit even all the marterial is the same. To make this CI-able, we can remove the timestamp from the `po4jupyterbook` code. We shall only update the POT files manually when we know for sure there are changes for now.


## Implementation details

The philosophy behind the implementation is to make translation work without impacting the existing build process. Jupyterbook builds by copying the Markdown files to the `_build` directory under `book/website` with some parts added. Jekyll builds by compiling the Markdown files to HTML files in the `_site` directory.

The shell script that handles building of the translations is in [`book/website/scripts/multilingual_make.sh`](book/website/scripts/multilingual_make.sh)

A rundown of steps taken by `multilingual_make.sh`:
- clone `po4jupyterbook` to the root directory of the repository  
- compile the translated markdown files to `book/content/locale`  
- copy and make a config file for Jupyterbook to build the translations  
- for each language in [`book/content/po/LINGUAS`](book/content/po/LINGUAS)  
    - make specific table of content file for this language by adding the language code to the start of the URL  
    - `jupyter-book build` copys Markdown files to the `_build` directory and adds some boilderplate parts  
    - use `find` and `sed` to substitute all the `../figures` to `../../figures` so the figures can be directed corretly  
    - Jekyll build  
    - remove the Markdowns from the `_build` directory so they don't get built by Jekyll again in another language build  
- Restore the table of content file to the original version for the English version build  

### Transient files during the build process

The table of content for (`toc.yml`) contains the book structure and controls the urls of the book. We only need to maintain one version of the file as the table of content for each language is generated during the build process by adding the language code to the urls.

The configuration file for Jupyterbook (`_config.yml`) points to where to find the book content Markdown files. 

### Translation of pictures

We hope that pictures and illustrations can be translated as well. Those pictures can be stored in the same place as the original ones with language code added.

