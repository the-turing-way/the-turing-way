(ch-style-videos)=
# Videos

## Hosted videos

If your video is hosted on a platform like YouTube or Vimeo you can use the [`youtube` directive](https://mystmd.org/guide/figures#youtube-videos) to embed it.
For example,

````
:::{youtube} MdOS6tPq8fc
:label: example-video
:::
````

renders as,

:::{youtube} MdOS6tPq8fc
:label: example-video
:::

and can be referenced with `[](#example-video)`, which when rendered will appear as: [](#example-video).

For youtube, the link formatting you need to use is just the code at the end of the video URL (`MdOS6tPq8fc` for the above video example).
