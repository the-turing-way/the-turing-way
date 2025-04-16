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

Note the new title, icon, and colour scheme,

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
