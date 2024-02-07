(er-datahazardsintro)=
# Introduction to Data Hazards Project

Data Hazards is a community project to develop a shared vocabulary of data science risks (in the form of Data Hazard labels) and materials to help data practitioners use them.

These labels and materials are provided CC-BY licensed on the [Data Hazards website](https://datahazards.com).
They exist to facilitate interdisciplinary discussions and self-reflection about all kinds of data ethics risks. 
Ultimately, the project aims to help data practitioners to identify and mitigate these risks.
You can watch a short animation explaining the project below:

<div style="text-align: center">
<iframe width="560" 
  height="315" 
  src="https://www.youtube-nocookie.com/embed/26fNnar4JvY?controls=0" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

(er-datahazardsintro-datahazardslabels)=
## Data Hazards labels
In this section, we explain the nature of the project.
Feel free to skip ahead to the next section for more practical guidance on {ref}`how to use the Data Hazards<er-datahazardshowtouse>` in your data-intensive work.

### What do they look like? Anatomy of a Data Hazards label

Each label has, as described in the main website: 

- **Hazard image**, title, and description which represents and describes the risk.
- **Examples** to clarify what the hazard covers.
- **Safety Precautions** things that we would want to see done before the research is deployed.

### Example label: high environmental cost
```{figure} ../../figures/data-hazard-environmental-cost.*
---
height: 250px
name: data-hazard-environmental-cost
alt: A red diamond with an image of the earth at the centre. The earth is surrounded by a flame. 

---
_Data Hazards_ project illustration by Yasmin Dwiputri. Used under a CC-BY 4.0 licence. [DOI.](https://doi.org/10.31219/osf.io/hzmyp).
```

#### Description
This hazard is appropriate where methodologies are energy-hungry, data-hungry (requiring more and more computation), or use special hardware that requires rare materials. Alternatively, this could also apply to research which outputs high amounts of waste.

#### Examples
 - Example 1: Wet-lab experiments which create large amounts of single-use plastic waste, for example, pipette tips or petri dishes; or specific chemicals that are harmful to the environment {cite:ps}`Freeland2022`, {cite:ps}`Leak2023`. 
 
 - Example 2: Running big models on High-Performance Clusters can have a big environmental impact with the energy they consume {cite:ps}`alaparthi2020bidirectional`, {cite:ps}`Bender2021`.

#### Safety Precautions
 - Consider recycling programmes, as well as reducing purchasing and shipping. 
 - To communicate the scale of the issue to other stakeholders, you may want to [convert units of energy into more relatable units](https://calculator.green-algorithms.org/).
 - Find out if your cloud provider uses renewable energy.
 - Consider profiling your code, and rewriting it to use less energy. 
 - Consider future work that would reduce the need to use increasingly more resources.

---

### But Why Hazard Labels?
The Data Hazards framework takes inspiration from the visual nature of chemical hazard symbols, communicating to users the potential outcomes and risks of a project. 
Similarly, to chemical hazards, labelling something as hazardous does not change or reduce its inherent risk.
However, the visual display of the risk allows the user to make choices based on this knowledge. 
The user can choose to take the necessary precautions to keep themselves, others and their environment safe. 
This also applies to the Data Hazard labels, where if we can identify the risks, we can act accordingly and mitigate possible risks.


### Where did they come from?
There were originally six labels, which were identified through reading data ethics papers at [Data Ethics Club](http://dataethicsclub.com): a fortnightly journal club for data science and ethics.
Through collecting suggestions [on GitHub](https://github.com/very-good-science/data-hazards), and at conferences and Data Hazards workshops, further labels were suggested and added until we reached the current 11 labels as of November 2023.

### The Hazard labels are versioned
<!--The Hazard labels are versioned!-->
The Data Hazard labels are a living project and will continue to change as we gather more suggestions - for this reason, they are versioned semantically.
At the time of writing, in `v1.0`, there are 11 Data Hazard labels: you can [explore the Data Hazard labels yourself](https://datahazards.com/labels) on the Data Hazards website.

(er-datahazardsintro-ethicalframeworks)=
## Ethical Frameworks 
Ethical frameworks can provide a toolkit to help researchers, stakeholders, developers, policy-makers and decision-makers understand what is required and should be considered when engaging in responsible research and innovation. 
Philosophically and socially, ethical frameworks have been considered broadly outside of data science and AI settings and projects.

As not everyone may agree on a shared meaning of research ethics, there are many ethical frameworks available.
Individuals may adopt and interpret ethical meanings based on unique priorities, personal needs, professional requirements or societal and cultural roles. 

Some examples of ethical frameworks that already exist in scientific domains include: 

1. Citizen Science and Public and Patient Participation in Research {cite:ps}`Groot2022`
2. Ethical Framework for Presenting Scientific Results to Policy-Makers{cite:ps}`Schroeder2022`
3. Five Dimensions of Research Ethics: A Stakeholder Framework for Creating a Climate of Research Integrity {cite:ps}`Dubois2018`
4. ESRC Framework for Research Ethics {cite:ps}`esrc2010Framework`
5. Ethics of AI in Education: Towards a Community-Wide Framework {cite:ps}`Holmes2022`

The Data Hazards framework has some similarities to the example frameworks listed above. 
However, the Data Hazards provides an intuitive and visual approach to evaluating and reflecting on risks associated with a research project. 
It allows the dangers to be explicitly stated alongside some mitigation strategies researchers can use to tackle these risks. 
It provides us with a toolkit to facilitate discussions, reflection and decision-making for current and future stakeholders.   
Crucially, it also considers a more holistic view of ethics, not focusing on a specific domain or risk, or separating human-centered ethics from non-human animal or environmental frameworks. 
This toolkit allows for reflection across a spectrum of risks and ethical considerations. 
The Data Hazards framework also provides an open-source approach to an ethical framework, where flexibility and creativity to adapt and develop the framework are strongly encouraged! 

(er-datahazardsintro-keyterms)=
## Key Terms
Risk and hazard are terms sometimes used interchangeably, but sometimes they can have nuanced specific meanings. 
Certain fields like environmental sciences, engineering or medicine require a clear and consistent use of these terminologies.
Generally, "hazard" refers to the inherent qualities or characteristics of something that make it potentially harmful. 
It's more focused on the nature of the threat rather than the likelihood of it occurring. 
Whereas "risk" is a term that refers to the likelihood and impact of something happening. 
It's often used in decision-making contexts to evaluate the potential consequences of actions.
