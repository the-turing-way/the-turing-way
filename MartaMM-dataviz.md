## Various issues in data visualisation

Data visualisation can be defined as _the visual representation and presentation of data to facilitate understanding_.
It involves seeing data using _marks_ (for example, shapes) and _attributes_ such as size, position, and colours.
Good data visualisation helps us to show vast amounts of numbers and relations between them at a glance, using images and visual features.
 
The understanding process involves three steps:
- Perceiving (what do I see?)
- Interpreting (what does it mean for the subject?)
- Comprehending (what does it mean to me?)
These three processes are intrinsically uncertain, we cannot be sure that understanding happens for everyone in the way we expect or want it to happen. Therefore, data visualisation can be seen as a game of decisions. To make the best decisions, you need to be familiar with all your options (things you could do) and aware of the things that will influence your choices (things you will do).

<!--this part is taken from A. Kirk slides from the dataviz course-->

Three points of effective and efficient design process:
- trustworthy: is it reliable?
- accessible: is it usable?
- elegant: is it aesthetics?
 
### external constraints to good data visualisation:
* people
* deliverable
* constraints

### working with data: 
1. acquisition
2. examination
3. transformation
4. exploration

<!--this part is taken from A. Kirk slides from the dataviz course ENDS-->

### editorial thinking

Data visualisation is not a "one size fits all/most" tool. 
It is an interpretation of reality through a specific angle and framing.
It involves choices and decisions which vary depending on one's goals (informing? convincing? persuading? supporting an argument?). A. Kirk defines this as _editorial thinking_
<!--this part is taken from A. Kirk slides from the dataviz course ENDS-->

As it employs a visual/graphic medium to convey quantitative as well as qualitative information, data visualisation is intrinsically multidisciplinary and relies on a variety of skills working in sinergy. 
A data scientist provides the quantitative information to be represented, graphic designers devise the most appropriate visual representation for it, and psychologists raise awareness on perceptual and cognitive constraints which can affect people's understanding and interpretation of the visualisation.
 
the classical text "The visual display of quantitative information" by Tufte and Graves-Morris (1983) is a goldmine of resources and suggestions but, because it was published in 1983, it did not (and could not, for obvious reasons) address all the data visualisation opportunities that state of the art platforms and software offer nowadays. 

### design solution

* data representation: marks and attributes
### influencing factors:

### potential applications of interactivity

### use of colour
<!---use of colour in domain-specific contexts: Christen, M., Brugger, P., & Fabrikant, S. I. (2021). Susceptibility of domain experts to color manipulation indicate a need for design principles in data visualization. PloS one, 16(2), e0246479. -->

<!--### Storytelling
Data visualisation and infographics are essential tools for _storytelling_-->

### choosing the right visual representations for the data and task at hand
### Anscombe's quartet
### visual analysis as individual/social process

In a sea of data, data visualisation represents a time-constrained activity which offers options to represent data analysis, making users/people aware of the different options they have. Dataviz can be considered an *informed list of possibilities* that empowers people instead of overwhelming them.
tradeoff between having a large amount of information and knowing what to do with it 
PEIR (personal environmental impact report)
YFD (your flowing data): "to make personal data understandable to nonprofessional" ("Beautiful Data", Segaran and Hammerbacher, 2009).
color schemes and other visual cues significantly help to convey the message behind the data representation.
When collecting data through a form, it is crucial to tailor the form itself to the specific population it refers to (for example, using bigger font for older people).
it is also crucial to design for _accurate_ data collection and maximise data quality. 
test everything!
different concerns with observational vs experimental data
dataviz can, and should, help "data finds data" processes (see "Beautiful Data"). 

### Importance of considering gender issues when approaching data and data visualisation
"Users" are not all white men from a medium-high socioeconomic background, in a USA setting. 
Male should *not* be the 'default' option, this attitude limits data accessibility, applicability, and generalizability. 
As thoroughly described and argued by Caroline Criado Perez ("Invisible Women", 2019), taking gender data into account in (city/transport/local plan) planning requires changes and solutions that have a ripple effect with broader consequences on the general society.
Fenwick, Sandell, and Berengueres (2019) in their book on data visualisation suggest a chart checklist to check for bias in data visualisation. This checklist covers aspects such as the type of chart, use of colurs, use of metaphors, and captions. 

### Data accessibility

How do you qualify what you produce in terms of data visualisation?
<!--need to check what you wrote in the notes-->
Use of colours and accessibility: [colororacle](www.colororacle.org) is a colour blindness simulator, allowing data scientists to consider colour branding and output restrictions when working on their charts.

### Possible negative effects of data collection?
### Sense.us case study <!--does anyone know more about them?-->
"Our goal was to realize the potential beauty of data by fostering collective data analysis".
Source: IPUMS-USA
Importance of effective visual encodings
### Case study: the Bakery project (

### tendency to create a story out of noise!

[The chartmaker territory](https://chartmaker.visualisingdata.com/) provides a valuable resource for deciding what type of chart you shoud use depending on the type of data you are working with and, even more relevantly(?), the relation between data that you want to highlight.


<!--## UK data service!-->
<!--further development: use of dashboards-->

### References
- Perez, C. C. (2019). Invisible women: _Exposing data bias in a world designed for men._ Random House.
- Fenwick, A., Berengueres, A. F. J., & Sandell, M. (2019). _Introduction to Data Visualization & Storytelling A Guide For The Data Scientist._
- Kirk, A. (2016). _Data visualisation: A handbook for data driven design._ Sage.
- Lankow, J., Ritchie, J., & Crooks, R. (2012). _Infographics: The power of visual storytelling._ John Wiley & Sons.
- Perez, C. C. (2019). _Invisible women: Exposing data bias in a world designed for men._ Random House.
- Segaran, T., & Hammerbacher, J. (2009). _Beautiful data: the stories behind elegant data solutions._ " O'Reilly Media, Inc.".
- Spiegelhalter, D. (2019). _The art of statistics: learning from data._ Penguin UK.
- Tufte, E. R., & Graves-Morris, P. R. (1983). The visual display of quantitative information (Vol. 2, No. 9). Cheshire, CT: Graphics press.
- [We all count](https://weallcount.com/the-data-process/)
- For R users: [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/) by Claus O. Wilke, [Data Visualization, A practical introduction](https://socviz.co/) by Kieran Healy and [The Data Validation Cookbook](https://data-cleaning.github.io/validate/) by Mark P.J. van der Loo
