(ch-style-blocks)=
# Special Content Blocks

When writing a new chapter or revising an existing one, you may wish to add notes that do not fit in with the rest of the chapter's narrative but may be useful to the readers and help them understand the chapter better.

(ch-style-blocks-admonitions)=
## Admonitions

Jupyter Book allows the use of special content blocks, called admonitions or call-outs, to highlight a piece of text that needs to stand out from the rest the content on a page.
This visually separates the block of text from the rest of the page, and ensures that it easily captures the reader's attention.

There are a number of built-in, named call-outs.
Each of these have different styling suitable to their purpose.
These are,

- note
- important
- hint
- seealso
- tip
- attention
- caution
- warning
- danger
- error

To add a call-out to your page, use the named directive.
For example, to create a note,

````
```{note}
This is a sample note!
```
````

which renders as follows,

```{note}
This is a sample note!
```

If you wanted to warn the reader about something, you may make a warning block using the following directive,

````
```{warning}
This is a stern warning!
```
````

Notice this call-out has a different title, icon, and colour to the note above,

```{warning}
This is a stern warning!
```

You can modify an admonitions title, and make the block dropdown like this,

````
```{hint} A call-out hint!
:class: dropdown
You can make a call-out dropdown by adding the dropdown class!
```
````

which renders as,

```{hint} A call-out hint!
:class: dropdown
You can make a call-out dropdown by adding the dropdown class!
```

You can read more about call-outs in the [MyST Markdown documentation](https://mystmd.org/guide/admonitions).

(ch-style-blocks-tables)=
## Tables

You can create tables using the `table` directive.
The tables themselves are written using [GitHub Flavoured Markdown](https://github.github.com/gfm/#tables-extension-).
Using the table directive lets you add a label so you can cross-reference the table.

For example,

````
```{table} My table
:label: example-table
:align: center
| Name       | Job                  |
| ---        | ---                  |
| Sam Spade  | Private investigator |
| Harry Lime | Smuggler             |
```
````

which renders as,

```{table} My table
:label: example-table
:align: center
| Name       | Job                  |
| ---        | ---                  |
| Sam Spade  | Private investigator |
| Harry Lime | Smuggler             |
```

and can be references with `[](#example-table)` [](#example-table).

You can read about other ways to write tables in the [MyST Markdown documentation](https://mystmd.org/guide/tables).

(ch-style-blocks-code)=
## Code and literal text

You can write blocks of literal text using three backticks.
For example,

````
```
hello
```
````

renders as,

```
hello
```

You can ensure that any code (or Markdown) chunks you have in the guide have the code syntax highlighted by mentioning the language in question.
As an example, if you want to have some R code, when you open the chunk with three backticks you can add the language name immediately after it,

````
```R
x <- c(1:21)
```
````

renders as,

```R
x <- c(1:21)
```
