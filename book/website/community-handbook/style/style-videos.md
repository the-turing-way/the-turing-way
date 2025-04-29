(ch-style-videos)=
# Videos

## Hosted videos

If your video is hosted on a platform like YouTube or Vimeo you can use the [`iframe` directive](https://mystmd.org/guide/figures#youtube-videos) to embed it.
For example,

````
::: {iframe} https://www.youtube.com/embed/MdOS6tPq8fc
:width: 100%
:align: center
:label: example-video
How to build a Jupyter Book!
:::
````

renders as,

::: {iframe} https://www.youtube.com/embed/MdOS6tPq8fc
:width: 100%
:align: center
:label: example-video
How to build a Jupyter Book!
:::

and can be referenced with `[](#example-video)` [](#example-video).
