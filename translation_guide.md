# Translation Guide

## How to join a translation team?

Go to [Transifex](https://www.transifex.com/theturingway/theturingway/) and click "Help Translate TheTuringWay" (button in blue).
<!-- TODO Screenshots to be added -->

## How to start a new translation?

- Clone `po4jupyterbook` to the root directory of the project  
    `git clone https://github.com/tonyyzy/po4jupyterbook`
- In `book/content` the `po` folder contains the POT and PO files. POT files are generated from the Markdown files and contains the original strings of the book; PO files contain the original string and their translations.
- To start a new language
    - add the language's ISO code to `book/content/po/LINGUAS`
        - also add the language code to the `keep_files` list of `book/website/_config.yml`
    - Copy all the POT files to make corresponding PO files.  
        `for i in *.pot; do echo $i; cp $i ${i::-4}.<LANG>.po; done`
    - To compile the POs to translated Markdown files, you are required to fill in the header section of the PO files. Please see existing PO files for an example of dummy data. The compilation process will fail if the header information is not filled in. The PO files submitted by Transifex should have these filled in.
- When the Markdown files are updated, you will need to update the POT files for the new strings to show up in Transifex.  
  Under `book/content` run `../../po4jupyter/create.sh`
    - This will update the POT files to track the modified Markdown files. Because there are timestamps in the POT files, git will always show there is something to commit even all the marterial is the same. To make this CI-able, we can remove the timestamp from the `po4jupyterbook` code. We shall only update the POT files manually when we know for sure there are changes for now.


## Implementation details
<!-- TODO: Add details from the issue -->
