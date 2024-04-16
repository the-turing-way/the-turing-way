(ch-style)=
# Style Guide

To ensure that the book can be read easily by everyone, including screen readers and non-native English speakers, we have compiled a set of guidelines to keep a consistent style across all chapters of the book.

We follow the [GOV.UK guidance](https://www.gov.uk/guidance/content-design/writing-for-gov-uk) to improve accessibility of the resources in _The Turing Way_.

## Write each sentence in a new line (line breaks)

Please write all sentences in the markdown file on separate lines.
Having each sentence on a new line will make no difference to how the text is displayed, there will still be paragraphs, but it will mean that any pull requests will be easier to check; the changes will be on a single line instead of somewhere in a paragraph.
Consider the example below.

 ```markdown
Today you are you, that is truer than true. There is no one alive who is youer than you. - Dr Seuss
```

A pull request on this correcting it to have a ‘.’ after Dr would show as a change to the whole paragraph.
Contrast this with the next example which will be displayed online in the exact same way, but would see a change to a single line.

 ```markdown
Today you are you, that is truer than true.
There is no one alive who is youer than you.
- Dr Seuss
```

### A note on bullet points

If you want to add multiple sentences inside a bullet point, we recommend indenting the sentences following the initial sentence with two spaces.
Consider the example below.

```markdown
Dr Seuss said:
- Today was good. Today was fun. Tomorrow is another one.
- The more that you read, the more things you will know. The more that you learn, the more places you'll go.
```

Similarly to the example in the section above, we should change this to have the sentences on separate lines:

```markdown
Dr Seuss said:
- Today was good.
  Today was fun.
  Tomorrow is another one.
- The more that you read, the more things you will know.
  The more that you learn, the more places you'll go.
```

This will render the same as the example with all sentences in one bullet point line, but will make it easier to see changes in pull requests.

## Opinions are welcome, but ...

_The Turing Way_ book is intended to be only *lightly* opinionated.
Whilst more opinionated content is allowed, such content should be clearly marked.
The best way to do this is by displaying it in a quote box.
This can be done by either prefixing every line with the greater than symbol `>`.
Note, that the formatting will be retained, so we can split each sentence to a new line as recommended before.

```markdown
> I will not eat them in a house,
> i will not eat them with a mouse,
> i will not eat them in a box i will not eat them with a fox,
> i will not eat them here of there i will not eat them anywhere,
> I do not like green eggs and ham i do not like them sam i am
```

## Avoid Latin Abbreviation

Please do not use Latin abbreviations.
See the [Gov.uk recommendations](https://www.gov.uk/guidance/style-guide/a-to-z-of-gov-uk-style#eg-etc-and-ie) for details.

Some of these abbreviations are:

```{figure} ../figures/latin-abbreviation.*
---
height: 400px
name: latin-abbreviation
alt: an image with a list of 3 latin abbreviations
---
A list of latin abbreviations for *exempli gratia* (for example), *et-cetera* (so on), and *id est* (that is).
Screenshot of part of the [list of Common Latin Abbreviations for APA Style](https://blog.apastyle.org/files/apa-latin-abbreviations-table-2.pdf).
We use a screenshot instead of plain text to comply with continuous integration tests (see below).
```

Instead of the first abbreviation in the table for *exempli gratia*, which can sometimes read aloud as ‘egg’ by screen reading software, please use ‘for example’ or ‘such as’ or ‘like’ or ‘including’ - whichever works best in the specific context.

Instead of the second abbreviation in the table for *et-cetera* to indicate open ended list, please start the list with words like ‘for example’ or ‘such as’ or ‘like’ or ‘including’.

Instead of third abbreviation in the table for *id est* that is often used to clarify a sentence, try (re)writing sentences to avoid the need to use it.
If that is not possible, use an alternative such as ‘meaning’ or ‘that is’.

Any chapter containing a Latin abbreviation will fail the continuous integration (CI) workflow of the _The Turing Way_ GitHub repository from passing successfully, which is tested by this [Python script](https://github.com/the-turing-way/the-turing-way/blob/main/tests/no-bad-latin.py).

*To avoid CI from failing, even in this chapter we have avoided to write those abbreviations and instead used an image to illustrate the above examples.*

## Tips

### Indentation

Indent the content following each item of a numbered list.
If the content is unindented, the list numbering will be reset.

For instance, please avoid:
1. First list item
```markdown
This content belongs to the first list item.
```
2. Second list item

Instead, the following is recommended:
1. First list item
   ```markdown
   This content belongs to the first list item.
   ```

2. Second list item


### External links

Write external links using "https://" instead of "www". This ensures they are correctly recognised as hyperlinks.

### Chunks with code or special text

You can ensure that any code (or Markdown) chunks you have in the guide have the code syntax highlighted by mentioning the language in question.
As an example, if you want to have some R code, when you open the chunk with three backticks you can add the language name immediately after it (<code>\`\`\`</code> becomes <code>\`\`\`R</code>).

Markdown source:

```
    ```R
    x <- c(1:21)
    ```
```

HTML output:

```R
x <- c(1:21)
```
