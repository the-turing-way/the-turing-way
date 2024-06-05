(er-activism-env-impact)=
# The Environmental Impact of Digital Research

As multiple reports from the United Nations (such as [IPCC | Climate Change 2023: Synthesis Report](https://www.ipcc.ch/report/ar6/syr/) and [WMO | Global Annual to Decadal Climate Update](https://public.wmo.int/en/our-mandate/climate/global-annual-decadal-climate-update)) have shown, the global climate crisis impacts all of us. From this, reducing carbon emissions has emerged as a means of addressing the climate crisis. For those of us that do computing as part of our day-to-day work, it can form a significant part of our environmental impact, both for us personally and for our organisation(s). In particular, if you or your group does intensive computing, making use of high-performance computers or cloud resources, for example to train intricate models or run complex simulations, the carbon footprint can be sizable.



For this reason, it is important to consider the environmental impact of the computational work you and your colleagues and collaborators do, including having awareness of the possible scale of it in relation to other activities you undertake as part of day-to-day life. With this awareness, it follows that we should all aim to reduce our carbon footprint for our work activities.

This guide helps data and computational scientists to better understand the environmental impacts of their work and projects, as well as providing suggestions for reducing the impact of it.

The topic is not new, it has for example been discussed during [CW23](https://software.ac.uk/blog/2023-08-15-tracking-environmental-impact-research-computing).

(er-activism-env-impact-understanding)=
## Understanding the problem

Most of us are aware of the general context of our planet being subject to climate change that results largely from human influence, and how this poses a great threat to our society. However, in case you are not, and indeed to emphasise this crucial background, we’ll summarise this background.

(er-activism-env-impact-climate-change-sumarised)=
### Climate change summarised

Human activities, notably the burning of fossil fuels like oil, gas or coal, to generate electricity and to power cars (amongst many other tasks) release greenhouse gases into the atmosphere. These gases, such as carbon dioxide, trap heat in the atmosphere, which in turn raises the temperature of the surface of the Earth. While not linear, over time, [the global average temperature rises](http://climate.nasa.gov/vital-signs/global-temperature/).


(er-activism-env-impact-rise-in-temperature)=
### Rise in global temperatures illustrated

The rise in this global average temperature is strikingly illustrated by the ‘Warming Stripes’ (‘#ShowYourStripes’) project, a minimalist-style data visualisation created by Ed Hawkins. Average Earth surface temperatures are indicated as stripes in blue hues, representing cooler temperatures, through to red hues, representing warmer ones, where each stripe covers a single year.

The general trend shows a progression, over the past few centuries or so, from there being more blue on the left (towards the past) to more red on the right (towards the present). In short, the surface of our planet is, overall and year-on-year, warming!


```{figure} ../../figures/global_warming_stripes.*
---
height: 500px
name: Global warming stripes, by Ed Hawkins.
alt: Global warming stripes, by Ed Hawkins.
---
Global warming stripes, by Ed Hawkins.
```

This more verbose figure makes it more explicit what the global warming stripes represent. You can find these and more figures on the [canonical warming stripes page](https://showyourstripes.info/s/globe).



```{figure} ../../figures/GLOBE---1850-2022-MO-barslabel.*
---
height: 500px
name: Bars with Scale, by Ed Hawkins.
alt: Bars with Scale, by Ed Hawkins.
---
Bars with Scale, by Ed Hawkins.
```

(er-activism-env-impact-awareness-raising)=
## Awareness raising

Below we share some thought-provoking questions about the Environmental Impact of Digital Research.

- Where in the world did your last computer end up? An estimated 50 million tons of electronic waste are discarded each year. This is equivalent to throwing out 1000 laptops every single second. Less than 20% of e-waste is formally recycled, with 80% either ending up in landfill on developing countries, exposing vulnerable populations and their environment to health and pollution impacts (ref: https://www3.weforum.org/docs/WEF_A_New_Circular_Vision_for_Electronics.pdf).

- How much unused or inaccessible data do you have on the cloud? In 2021, on average, 35% of enterprise data is “dark,” meaning it has an unknown value, while 50% is redundant, obsolete or trivial. Only about 16% is business-critical, the study concluded. (ref: https://www.veritas.com/content/dam/Veritas/docs/reports/GA_ENT_AR_Veritas-Vulnerability-Gap-Report-Global_V1414.pdf)

- How much of the world's total electricity will the technological sector use by 2025? It is predicted that by 2025, the technology sector will consume 20% of the world’s total electricity (compared to 7% in 2022). Ref: https://www.tier1.com/the-environmental-impact-of-our-data-storage/)


(er-activism-env-impact-reduction-strategies)=
## Strategies for reduction

There are several things that can be done to reduce the environmental impact of digital research. In this section we describe some of the possible actions grouped in two major groups, computing and data, and links to external resources that can implement them.

These actions are not listed in any order of importance, and implementing any or some of them is better than not doing anything at all.


You can also read 'Ten simple rules to make your computing more environmentally sustainable' {cite:ps}`lannelongue2021ten` and the [Digital Humanities Climate Coalition Toolkit](https://sas-dhrh.github.io/dhcc-toolkit/).


(er-activism-env-impact-computing)=
### Computing 
As we engage in research activities, our utilization of computers and code execution significantly affects the environment. In this section, we explore approaches that can be employed to mitigate the environmental impact arising from the computational aspects of our research endeavors.

(er-activism-env-impact-code-efficiency)=
#### Improve code efficiency

As mentioned above, the amount of energy spent on running a computation depends on how long the particular computation runs. One way of reducing the energy spent is to optimize the code to make it run faster. 


Several studies show the energy intensity of computing tasks such as training Natural Language Processing models {cite:ps}`strubell2019nlpenergy,Schwartz2020greenai`, astrophysics simulations {cite:ps}`Portegies2020ecologicalimpact`, bioinformatics {cite:ps}`Grealey2022carbonfootprint`, and so forth. 

Optimizing GPU code for energy efficiency is one way to reduce energy usage {cite:ps}`Schoonhoven2022goinggreen`

(er-activism-env-impact-hardware-efficiency)=
#### Improve hardware efficiency

In some cases it is possible to run hardware in more energy-efficient modes. One relevant example is the ARCHER2 national high-performance computer service in the UK where three different CPU frequencies can be selected at run time. A 2022 study investigated the performance / power use trade off and discovered the power usage could often be reduced without noticeable alteration in the run time of most applications, by changing the CPU frequency to a different value from the three possibilities. As a consequence the service reduced the default CPU frequency and updated the user-facing documentation in this area (see Turner, 2022).


For the Summit supercomputer it is known that about 63.8% of the power is consumed by GPUs 
{cite:ps}`Stachowski2020autotuning`.

(er-activism-env-impact-avoid-tasks)=
#### Avoid unnecessary tasks

Another way of reducing energy usage is to avoid running task unnecessarily. Some examples include:


* Running CI[[https://book.the-turing-way.org/reproducible-research/ci/ci-options.html](https://book.the-turing-way.org/reproducible-research/ci/ci-options.html)] only when it is useful. For example: do not run unit tests when changes are made in the documentation and not on the code. 
* If you do test-driven development, run only tests that have previously failed. In this way you do not need to test code which you already know has been tested. You can use this GH action for limiting when tests (pytest) are run: [https://github.com/marketplace/actions/pytest-last-failed](https://github.com/marketplace/actions/pytest-last-failed) 
* Run CI with smaller datasets.

(er-activism-env-impact-schedule-low-emission)=
#### Schedule tasks at low-emission time

Energy usage at different times of the day has different carbon intensity. This means that there is also an opportunity to reduce carbon emissions by running computing jobs at different times of the day. While the energy usage remains the same, the carbon intensity can be lowered in this way.

The Climate Aware Task Scheduler (CATS)[https://github.com/GreenScheduler/cats] has been built specifically with this in mind. This tool can calculate how much carbon will be emitted during the run of a specific task, look at the carbon emission forecast, and schedule the task to be run at a time when carbon intensity is low.

```{figure} ../../figures/environmental-impact.*
---
width: 574px
name: environmental-impact
alt: Cartoon-like sketch depicting the potential environmental impact of digital research. The illustration is mostly done in a teal blue, with a black cloud in the background, with emissions written across it. On the left, a person sits at a desk with a laptop, with a chatbot and "COMPUTING" text above, symbolizing digital communication. Behind the chatbot lurks three black cogwheels. In the center, "EMISSIONS" emerge from a factory, representing pollution. On the right, a figure throws computers into the ocean, labeled "WASTE", indicating electronic disposal issues.

---
Illustration of the potential environmental impact of digital research.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.8169292](https://doi.org/10.5281/zenodo.8169292).
```

(er-activism-env-impact-data)=
### Data
The increasing amount of digital research and the associated storage requirements have implications for the environment, and understanding the environmental impact is key for sustainable scientific research practices. One important aspect to consider is the environmental impact of digital storage:


(er-activism-env-impact-data-reduction)=
#### Data reduction 
Reduction of data volumes is a straight-forward solution to minimize energy consumption in storage systems:
* Compression or deduplication can help to detect and delete repeated information. 
* Optimized data requires less time for transfer and consumes less network bandwidth.

(er-activism-env-impact-data-standardisation)=
#### Standardisation
Storing your data in a standardised data format can have a positive impact on the environment:

* Utilize data formats that are widely accepted within your community to prevent the need for conversion by those interested in reusing your data.
* Similarly, embrace standardized variable names and, if applicable to your data, employ standardized physical units.

In addition, if possible deposit your datasets in domain specific or community archives so that users are promptly informed about the availability of your data. This can also avoid duplication of effort and recomputation/acquisition of the same data.


(er-activism-env-impact-data-green-centers)=
#### Green Data Centers
The usage of shared computing and storage infrastructure is usually a way to reduce the impact of data storage in the environment. The reason is that most data centres invest in energy-efficient servers, storage systems, and networking equipment. This includes using hardware components with high energy efficiency ratings and employing advanced cooling techniques to reduce power consumption. In addition, the implementation of virtualization technologies allows for better usage of server resources.

Finally, some data centers are shifting towards renewable energy sources (solar, wind, hydroelectric power) and reducing their dependencies on fossil fuels.


The greenest data/HPC centers are listed on the [GREEN500 list](https://www.top500.org/lists/green500/).

Whenever you can choose, select data centers that are committed to reducing their carbon footprint.


### Other resources
#### Computation
* [GreenvAlgorithms](https://www.green-algorithms.org/) 
* [Green Algorithms: Quantifying the Carbon Footprint of Computation](https://onlinelibrary.wiley.com/doi/10.1002/advs.202100707) 
* [Carbon footprint estimation for computational research](https://www.nature.com/articles/s43586-023-00202-5.epdf?sharing_token=QTc-q5_jBfbwbgHrxjAF3NRgN0jAjWel9jnR3ZoTv0M5cDtvWq4NDOHdun0YacmqG8iEJ146ZGUvxIp3izWvG3qqEI0oN4e5AgJh1ioWOFtL_b-yexmwuBL7nKWggSD22xXBBQe-_M_1jL9gC5WNNOYCZkXrOcuiKp7L_6DvyMI%3D)
* [Energy and Policy Considerations for Deep Learning in NLP](https://www.aclweb.org/anthology/P19-1355) 
* [Green AI](http://arxiv.org/abs/1907.10597) 
* [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://doi.org/10.1145/3442188.3445922) 
* [Digital Humanities Climate Coalition
](https://www.cdcs.ed.ac.uk/digital-humanities-climate-coalition)
* [Wren Carbon calculator](https://www.wren.co/) 
* [Turner (2022) Study of the impact of CPU frequency on ARCHER2](https://www.archer2.ac.uk/news/2022/12/12/CPUFreq.html). 
* [ARCHER2 documentation](https://docs.archer2.ac.uk/user-guide/energy/) 


#### Data
* [Green Scientific Data Compression](https://centaur.reading.ac.uk/79584/1/tgsdcthiia18-towards_green_scientific_data_compression_through_high_level_i_o_interfaces.pd)
* [Environmental Impact of Video streaming](https://research.vu.nl/ws/portalfiles/portal/214278850/Jancovic_Marek_Keilbach_Judith_2023_Streaming_Against_the_Environment._Digital_Infrastructures_Video_Compression_and_the_Environmental_Footprint_of_Video_Streaming.pdf)
* [Next-generation high-temperature data centers](https://doi.org/10.1016/j.rser.2022.112991)
* [Zero energy consumption data centers](https://doi.org/10.1016/j.energy.2022.125495)

## Credits

This document draws on discussion from the [Software Sustainability Institute](https://www.software.ac.uk/)’s [Collaborations Workshop 2023 (CW23)](https://www.software.ac.uk/cw23), and in particular on the “Raspberry” discussion and speed blogging session on “How do you track the environmental impact of computing?”. We thank all participants of CW23 for engaging around this topic.  

