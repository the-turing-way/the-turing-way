(pd-risks-of-bias-identifying-risks-of-bias)=
# Identifying Risks of Bias
[Many tools](https://osf.io/dmrq6) have been established to identify/assess risks of bias.
While most risk of bias identification tools are intended to be used retrospectively during a literature review, we can use lessons from these to guide project design. 
Furthermore, while many tools have been developed specifically for health research, the same concepts can be applied across disciplines. 

The concepts in this section are organised similarly to those in [*Prediction model Risk Of Bias ASsessment Tool (PROBAST)*](https://pubmed.ncbi.nlm.nih.gov/30596875/) and [*A revised Cochrane risk of bias tool for randomized trials* (RoB 2)](https://methods.cochrane.org/bias/resources/rob-2-revised-cochrane-risk-bias-tool-randomized-trials), which are commonly used in the assessment of health data science models.
These are useful checklists which prompt the user to consider whether there are limitations in the participants, predictors, outcome, and analysis included in the given research. 

It is important to identify potential risks of bias while planning research so that bias mitigation strategies can be put in place.
Creating a research protocol can be invaluable in ensuring that the research has been thoroughly planned.
The protocol can even be peer-reviewed before the start of the active research, and can be published alongside the findings in a [registered report](https://book.the-turing-way.org/communication/dif-articles/reg.html#registered-reports). 


(pd-risks-of-bias-identifying-risks-of-bias-sampling)=
## Sampling
In statistics, a *population* is any group of similar individuals that is being modelled.
Individuals may be physical objects, such as people with a specific disease, or rivers in South America, or they may be conceptual, such as different news sources or political ideologies. 

It is rarely possible to thoroughly analyse an entire population, so researchers will typically focus on a *sample*, which is a subset of the population. 
The hope is that lessons learned about the sample will apply to the whole population, but this is not always the case. 

Samples are typically intended to be uniform and random, meaning that every inidividual in the population has equal chance of being selected. 
*Sampling bias* occurs when systematic issues cause some individuals to be more likely to be included than others. 
This may be caused by *convenience sampling*, where potential participants are selected because they are easy to access. 


In many studies, samples cannot be truly random as they depend upon members of the population volunteering themselves.
This often leads to a *participation bias*, where some population subgroups are more able or willing to participate than others. 
For example, it is very common for participation to be related to socio-economic factors, with healthy, wealthy, older people more likely to have the time and financial security required to volunteer in research. 
It is often impossible to completely eliminate such biases, but they can be mitigated by taking measures to [enable and encourage](https://www.evalacademy.com/articles/incentives-for-participation) a wider group of the population to participate. 

A sample may also differ from the population simply due to random chance - the only way to guarantee exact representation is to include every member of the population.
*Stratified sampling* can keep certain characteristics consistent between the population and the sample - for example, if the gender proportions of a population are known then a stratified sample can be taken with these same proportions.
This may be referred to as 'proportional representation'.
However, not all relevant factors can be controlled this way, with stratification only being applicable when every member of the population can be neatly allocated to one group. 

Increasing the size of a sample reduces the chance of a sample not being representative due to randomness.
Given the difficulty and cost of taking a larger sample, [*power calculations*](https://emj.bmj.com/content/20/5/453) can be used to determine the minimum appropriate sample size that can be taken to give a particular level of statistical certainty to the results. 


(pd-risks-of-bias-identifying-risks-of-bias-exposures)=
## Exposures and Outcomes
Research questions can often be simplified to "how does X affect Y?" - we refer to X as an *exposure* or *predictor*, and to Y as an *outcome*. 
For example, when considering "does smoking cause lung cancer?", smoking is the exposure and lung cancer is the outcome. 

The exposure can be anything which varies within the population, such as different treatments given in medical research, or smoking vs non-smoking, or different strategies for forest management. 
The term 'intervention' may be used to refer to exposures which are actively applied rather than observed, such as different treatments in a medical trial. 

The outcome can be anything which is measurable, either by qualitative (descriptive) or quantitative (numerical) means. 
In answering the research question, the exposures and outcomes must be clearly defined, and applied/assessed consistently for all participants. 
If the outcome is assessed qualitatively, it is also important that it is assessed without knowledge of the predictors to avoid an *observer bias*. 

(pd-risks-of-bias-identifying-risks-of-bias-analysis)=
## Analysis and Reporting
Bias remains an issue after the data collection stage, with potential risks in the data analysis and reporting of results. 

Weak validation can lead to bias due to overly optimistic results.
For example, if results are generated using a single small test set then they may be better than expected (optimistic) simply due to random chance. 
This is especially true if many different experiments are conducted, with a large enough number of experiments guaranteeing at least one positive result due to random chance. 
This is sometimes referred to as 'p-hacking' in a statistical context where positive results have small p-values, and as such it is not always sufficient to use the standard p-value threshold of 0.05 (for example, [genome-wide association studies](https://academic.oup.com/g3journal/article/11/2/jkaa056/6080665) often use a threshold of 0.00000005, which can be written more clearly as 5x10<sup>-8</sup>). 

Weak validations give imprecise results which are unlikely to generalise well to data outside of the training set. Thorough validation methods are explored in the 
{ref}`validation and generalisability subchapter <pd-risks-of-bias-validation-generalisability>`. 

It is also important that research is reported in a fair and unbiased manner. 
*Reporting bias* typically involves placing undue emphasis on positive results while downplaying or ignoring negative results (also called *selective reporting* or *cherry picking*). 
Failure to report negative results can be a significant form of scientific misconduct, and in medical research it is a breach of the [Declaration of Helsinki](https://www.wma.net/policies-post/wma-declaration-of-helsinki-ethical-principles-for-medical-research-involving-human-subjects/). 
*Reporting bias* can also include bias in choosing which previous studies to cite in order to give unfair emphasis to a particular narrative. 

To avoid biases in reporting research, it is helpful to define what the primary results are before conducting research, then these can be reported regardless of whether the finding was positive or negative. 
As such, it is highly beneficial to [develop and register a study protocol](https://www.nature.com/articles/s42256-023-00705-6) at the start of a research project.
This gives an opportunity to ensure research is properly thought-through, as well as improving the transparancy and trustworthiness of research. 


(pd-risks-of-bias-identifying-risks-of-bias-blinding)=
## Blinding

In prospective research, blinding (also called _masking_) can help to address many of the risks related to exposures and outcomes. 
People who have been blinded cannot know which exposure has been administered to any specific participant. 

Blinding participants is a common approach to avoid selection and participation biases (such as people only participating if they receive a specific treatment), and to avoid behavioural changes due to the psychological effects of receiving different treatments, such as the placebo effect. 
This is not possible in observational research. 

Blinding assessors can help to avoid an information bias, where the assessment of outcome is influenced by the expectations of the exposure. 
Data analysts can also be blinded to ensure a fair assessment of the final data. 

Typically the phrase 'single-blind' will refer to blinding only the participants, 'double-blind' to participants and assessors, and 'triple-blind' to participants, assessors, and data analysts. 
However, these terms are not always used consistently, so it should always be made explicitly clear which groups have been blinded. 
