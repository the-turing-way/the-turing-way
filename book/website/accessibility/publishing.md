# Publishing Accessible Data Science Reports

Data Science products are often visual and include lots of data. Both can present accessibility challenges which differ from those covered by existing accessibility guidance for application development.

In this guidance we consider four common types of Data Science products:

- Data
  - Usually tabular data presented either as files or queried through a web service or API
- Notebooks
  - Computational notebooks such as Jupyter offer an interactive way to explore data and techniques and present prototypes or reproducible analyses
- Dashboards & web applications
  - Interfaces for production use of where interactivity is needed are often presented as web applications or dashboards
  - Contain a mixture of query forms, visualisations, stats and data
- Written reports
  - Analysis on a particular topic is often presented as a report containing text, tables of data, and charts

Most of the unique accessibility challenges with these are visual, so a lot of the guidance here is related to providing accessible alternatives for visual impairments. Much of the standard guidance applies generally, so please use this alongside […] in addressing accessibility requirements for your work. Notebooks and more complex dashboards will also likely encounter issues with understandability and ease of navigation, particularly for keyboard only navigation.

What do I need to do?

**Process**

Most of this guidance provides practical suggestions to address likely accessibility problems to help make Data Science products as accessible as possible when direct guidance from users with accessibility needs is not available. However, if you're working with customers with particular accessibility needs or if they are in the intended user community, consider inviting them to participate in the design and implementation of the product using co-creation methods. Consider using goal-oriented design in developing the product and where it fits in user workflows. Getting the design right could potentially remove accessibility issues and improve usability without having to address them separately.

It's usually much easier and more effective to consider accessibility from the outset when designing the product than adding it on at the end.

**Table**

Tables defined as HTML elements should be defined semantically and according to […].

- Tables must have headers (for screen-reader navigation)
- Long tables should be paginated (for screen-reader and neurodiverse users)
- Table data should be exportable

**Raw Data**

As a Data Science output, raw data is useful as part of a wider analysis process where the customer may manipulate and integrate the data with other information. Presenting raw or summarised data can also be a good alternative or support to a chart or textual analysis as part of a report. There's no easy answer to data accessibility as there are a large variety of formats and potential issues which might arise from the subject, structure, format or volume of data.

In general, the more easily interpretable and usable data is, and less complex it is in terms of format and structure, the more accessible it should be. Presenting as little data as possible needed to answer the analytic requirements will generally improve both accessibility and general usability. Consider developing the overall requirement for the data to understand what the main goals will be for users and whether there's any opportunity to filter or summarise the raw data to provide replacement or additional datasets which will directly fulfil the main goals with reduced volume and complexity.

Standard tabular formats which can be loaded into Excel, such as csv or excel files are likely to be preferred but this is not an absolute rule if nested structure or relational data needs to be preserved.

Some other suggestions are:

- Use descriptive but brief column headers and avoid too many columns if possible
- Include a description with the data explaining what the data and columns represent, particularly if there is external knowledge which is needed to understand the data.
- Use standard formats for data values
- Address any data quality problems

**Visual elements in user interfaces**

**Images**

Most images should have alt text provided. If an image is purely decorative or does not add understanding beyond what is written in the text, it is best practice to provide an empty string as the alt text. For further clarification check out the [W3C alt text decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/).

The alt-text should describe the meaning that the image is trying to convey and will not necessarily always be a direct description of the image itself. Think of a company logo – if you were trying to describe the contents of the image you should use 'McDonald's logo' and not 'Big golden letter M'.

**Charts**

Wherever possible, charts should be accessible. You should also provide a table alternative to benefit all users (not just those who might not be able to access the chart). Ideally this should be a toggleable option and the table should also be downloadable. It is also recommended that you provide a text summary of the information displayed in the chart if it is appropriate and possible to do so.

Canvas elements are never screen reader accessible as they do not display any content to screen reader users. They are also not suitable for keyboard navigation as they do not take focus. The only way to make a canvas element accessible is to provide a fallback, however it is recommended that canvas elements are avoided as much as possible. They also cannot be enlarged without becoming pixelated, and so they are unsuitable for users who use screen magnification.

Using an SVG element is a better alternative as it's scalable and internal shapes and groups can be traversed by assistive technology. However, most charting libraries are not designed for accessibility so it's unlikely that SVG output will be intuitive for a screen reader by default. A description or summary dataset will likely still be needed as an alternative.

Sonification could be an alternative visualisation technique for some types of data. This displays charts via sound rather than visually. Open-source packages are available.

Charts presenting lots of data can be overwhelming for some users. To minimise these effects, charts should be well-labelled and described.

**Titles**

All charts should have a descriptive title that informs the user of what information they can expect to find in the chart.

**Captions**

A caption should provide some extra context about how the chart should be interpreted. For example, you might include how the data was collected or a basic summary of the information displayed.

**Direct data labels**

Direct labelling of data on the chart can simplify interpretation as the user does not have to keep referring to a legend. This can also improve the experience for colour blind users as they don't have to rely on being able to see the colours of the lines to draw meaning from the chart.

![](RackMultipart20230118-1-oyn34q_html_57ee2717c12b6903.png)

_Image from _[_https://www.storytellingwithdata.com/blog/2018/6/26/accessible-data-viz-is-better-data-viz_](https://www.storytellingwithdata.com/blog/2018/6/26/accessible-data-viz-is-better-data-viz)

**Legend**

If you are using a legend it should clearly identify extra information in the chart.

**Axis labels**

Keep axis labels horizontal and make sure they are descriptive of the data in the chart (not just x and y). You might include the range of the scale as well as units.

**Colours**

**Colour deficiency**

Colour is frequently used as a way of conveying information. In Data Science it is often used as a way of distinguishing points on a chart. However, in order to meet the [WCAG 1.4.1 success criterion around use of colour](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html), colour must not be the only way of conveying information. This does not mean that you cannot use colour, just that you must provide an alternative. You can widen colour accessibility by using a colour palette that is colour deficiency accessible. This is not a solution by itself and you should bear in mind that these palettes are unlikely to work for every colour deficient user because there are several different types of colour blindness affecting different areas of the visual spectrum.

Sequential colour palettes (e.g. a palette that is a gradient of dark blue to light blue) are generally accessible to people with most types of colour blindness. However, you will need to ensure that these palettes have an acceptable level of contrast between each colour so that points are easily distinguishable. This could become trickier with more datapoints. Both MatPlotLib and Seaborn have built in colour blind accessible palettes called '[tableau-colorblind10'](https://github.com/matplotlib/matplotlib/blob/main/lib/matplotlib/mpl-data/stylelib/tableau-colorblind10.mplstyle) and 'colorblind', respectively). The Viridis and cividis palettes in MatPlotLib are also colour blind safe. These palettes are included as of [matplotlib v2.2](https://matplotlib.org/stable/users/prev_whats_new/whats_new_2.2.html). In this article you can see [how the Seaborn palettes appear with various colour vision deficiencies](https://gist.github.com/mwaskom/b35f6ebc2d4b340b4f64a4e28e778486).

Some colour palette generators, for example [Coolors](https://coolors.co/), allow you to visualise the palettes as they will appear to users with various types of colour blindness. [ColorBrewer](https://colorbrewer2.org/) allows you to choose sequential, diverging or qualitative palettes that are accessible to colour blind users. The [Chrome Disability Simulator extension](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla?hl=en) can simulate the different kinds of colour blindness so you can easily check accessibility of your chart / product.

Users with monochromacy (absence of any colour vision) will not benefit from using these colour palettes as all colours are indistinguishable. To accommodate these users, you must provide an alternative to colour for delineating information. In charts this could be providing different patterns instead of colours; directly labelling data on a chart; or allowing users to pick their own colour palettes/patterns. W3 has some [example techniques for using colours and patterns](https://www.w3.org/TR/2016/NOTE-WCAG20-TECHS-20161007/G111) which may be of relevance.

Pattern fills are supported in some libraries, such as the [hatch parameter in matplotlib](https://matplotlib.org/3.5.0/gallery/shapes_and_collections/hatch_style_reference.html) and [hatch\_pattern for Bokeh](https://docs.bokeh.org/en/latest/docs/user_guide/styling.html#fill-properties). You can also use the [set\_hatch method](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch) with Seaborn plots. However, these are not as common as colour map parameters (appear only in specific chart types) and it may be necessary to fall back to constructing chart shapes from polygons rather than using higher-level APIs.

In some cases, colour palettes might produce colours that are hard to distinguish when they are side-by-side. If possible, you might consider putting a white space in between different colours to indicate that they are showing different data points. This may help, for example, on a stacked bar chart where different colours are directly adjacent to each other.

 ![](https://i.imgur.com/TQ0WWPk.png)

_Image from: _[_https://www.storytellingwithdata.com/blog/2018/6/26/accessible-data-viz-is-better-data-viz_](https://www.storytellingwithdata.com/blog/2018/6/26/accessible-data-viz-is-better-data-viz)

Overall, there's unlikely to be one colour scheme to meet all needs, so consider making it possible to switch between several if possible.

**Neurodiversity**

Neurodiverse individuals are more likely have negative sensory reactions to colours. Colours that are too bright are most likely to trigger these responses.

**Contrast**

In text, graphical elements or pictures it is important to consider the luminance contrast of colours, particularly where you have text on a background. The minimum acceptable contrast ratio is 3:1, but this is most acceptable for large text (where large text is a minimum of 18pt, or 14pt bold). For improved accessibility, aim for 4.5:1 ratio as a minimum. To meet the highest accessibility standard, the ratio must be 7:1.

Where possible you should also avoid using the highest contrast ration, as this can decrease readability for users with dyslexia. A [W3C study on colour ratios and readability](https://www.w3.org/WAI/RD/2012/text-customization/r11) suggests that black on cream may be the optimal colour choices for dyslexic users. Bright and contrasting colours should also be avoided for the benefit of users with autism.

The [WebAim contrast checker](https://webaim.org/resources/contrastchecker/) tool is handy for checking your chosen colours for compliance with the minimum acceptable contrast ratio. Bear in mind this tool does not tell you whether your colours have too high a contrast ratio for dyslexic users, for example. For further information on contrast ratios see the [W3C standards on contrast](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html).

**Access to Data Exports**

Allowing users to export data means they can look at it in a way that suits them best. This is beneficial to all users, including those without any particular accessibility requirements.

**Data Science Notebooks**

Unfortunately, screen reader and keyboard-only navigation issues can make Jupyter notebooks unusable for users with visual or motor needs. Whilst the Jupyter project is committed to addressing these issues, at the moment an accessible alternative to notebooks would need to be provided.

The best option would likely depend on the situation but a few alternatives could be:

- Code
  - If users have technical skill and will be familiar with the language the notebook is written in, providing a script or module may be a good alternative
- Data
  - If the main output is a dataset, consider if it's possible to integrate the processing into existing systems or dataflow so that the data appears in existing interfaces without needing to run notebooks

- A web application
  - If users aren't familiar with code or would prefer a simpler way to run the notebook code, developing the interface as an accessible web application could be an option
- A textual report
  - If new inputs aren't expected or execution of the code by the user is not required, then pre-calculating outputs and including them in a written report could be a good option

**Dashboards & Interactive Applications**

Data Science apps such as dashboards, query tools and interactive visualisations are complex and would likely need a whole guide in themselves, although much of the same guidance as in this document applies, particularly for individual components such as charts and tables. This section presents an overview and a few suggestions on designing DS apps for accessibility.

If it's possible to get users with accessibility needs involved with the design process, co-creation would be a great way to make sure that the app will work for them throughout design and implementation. Goal-oriented design is also a useful methodology to keep the design as simple as possible, which can help manage information for cognitive needs and provide an intuitive structure which can help with screen reader and keyboard-only navigation.

Much of the existing guidance can also be drawn on for web development so advice and tools for meeting the WCAG standards will also be useful. It is a requirement to meet WCAG 2.1 Level AA criteria for any web apps, so if you're planning to deliver the DS product as an app, getting familiar with the standard and planning in how you'll meet the criteria will help satisfy the requirement.

Further support

[…]