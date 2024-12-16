(ch-style-custom-styling)=
# Custom Styling

Although content contributed to _The Turing Way_ should be written in {ref}`Markdown <ch-consistency-formatting-hr-markdown>` where possible, sometimes, `HTML` syntax may be necessary to format your contribution the way you desire.
Already, Jupyter Book converts Markdown syntax to `HTML`, making it possible to have a web version of _The Turing Way_ book.
As a result, writing your own custom `HTML` may introduce some variation in the way your new content appears online compared to the rest of the book.

To minimise this disparity, _The Turing Way_ maintains book-wide [stylesheets](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/_static/book-stylesheet.css) that control the look and feel of the book's content.
When including `HTML` in your contributions, please refer to these stylesheets and add the relevant classes and IDs defined there to your `HTML` elements.
This ensures that your new content fits the overall style of _The Turing Way_ book.

In this subchapter, we provide an explanation of how to leverage the book's stylesheets to style your contributions in sample use-cases.
If you want to improve the style of the book, this subchapter also provides a brief overview of how to do so.

(ch-style-custom-styling-stylesheets)=
## Using the Stylesheets

(ch-style-custom-styling-videos)=
### Videos

While it is possible to embed images and GIFs in your content using Markdown syntax, it is currently only possible to embed videos with `HTML`.
More so, we do not recommend adding videos directly to _The Turing Way's_ Github repository as video files are usually large and will make the book load much slower, especially for readers with slow internet connections.

To add a video to your contribution, first upload it to _The Turing Way's_ Youtube channel, then copy/paste the `HTML` code that is generated when you:
1. Click on the `Share` option underneath the video,
1. And then click on the `Embed` option from the range of options that appear.


The `HTML` code you copy will be an [`iframe`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) element.
For example:

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/MdOS6tPq8fc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

By default, `iframes` are not responsive, meaning that the video you just embedded will be inaccessible to readers on mobile devices.
To fix this, _The Turing Way's_ stylesheets define classes and styling that allow `iframes` to resize and fit the screen the book is read from.

To leverage this custom styling, wrap the `iframe` in `div` tags and give the `div` element a `video-container` class. For example:

```
<div class="video-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/MdOS6tPq8fc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```

The code above then renders as follows:

<div class="video-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/MdOS6tPq8fc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

(ch-style-custom-styling-improvements)=
## Improving _The Turing Way's_ Styling

Jupyter Book works by converting Markdown syntax to `HTML`.
Therefore, to improve the overall styling of the book, `CSS` rules should target the `HTML` elements that Jupyter Book generates.

Before writing any CSS, inspect the book's HTML source code first.
This gives you an idea of what elements to target, and may help you figure out how to structure your CSS rules.

All web browsers allow you to view the source code of websites easily.
On computers running the Windows OS or Linux, this is done using `CTRL + U`.
For computers running Mac OS, this is done using `Option + Command + U`.

Once you have determined the element(s) you want to modify, write your CSS in _The Turing Way's_ [stylesheet file](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/_static/book-stylesheet.css).
If, for example, you wanted to change the `font-family` of the paragraph text across the entire _The Turing Way_ book, then you could add the following CSS rule to the stylesheets which target
all elements with a `<p>` tag:

```
p {
    font-family: georgia, garamond, serif;
}
```

If you think that the styling introduced in _The Turing way_ can be useful for other Jupyter Book users, please consider making an upstream contribution to the project by creating a new GitHub issue and starting a discussion with their maintainers: [https://github.com/executablebooks/jupyter-book/issues](https://github.com/executablebooks/jupyter-book/issues).
