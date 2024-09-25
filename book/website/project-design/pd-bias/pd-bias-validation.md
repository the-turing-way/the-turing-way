(pd-bias-validation)=
# Validation and Generalisability 
Data analysis often involves making quantitative estimates of performance (such as assessing the accuracy of predictions), in a process called validation. 
Poor validation can lead to the research results being inaccurate, uninformative, or misleading.

Validations are often weak due to the use of small and potentially non-representative samples. 
When working with sampled data, it is essential to extract the most information possible, which often means using some of the following techniques:
- (Stratified) Cross-validation 
- Bootstrapping (and other variability measures)
- External validation
- Statistical tests (hypothesis tests)

Such methods can help to evaluate the variability and generalisability of results.
This is particularly useful when comparing different modelling approaches or exposures, as without measuring the variability we cannot be certain whether 'better' results were simply caused by random chance. 

It is also important in validation to choose appropriate metrics. 
No individual metric is able to assess all relevant aspects of performance, and as such it is far more informative to calculate several different metrics with different properties. 
These should then *all* be reported on, without simply cherry-picking the ones which portray the best performance. 
It is not always clear which metrics are most useful for a given task, so it may be useful to refer to any [specific guidance](https://www.nature.com/articles/s41592-023-02151-z) for the field.


When working with imbalanced data, it is also important to consider the effect this has on the results.
For example, if a dataset contains 99% cats and 1% dogs, then a classification model can simply say everything is a cat to get 99% accuracy.
Such a model is completely useless, and this would be obvious if we used a *balanced accuracy*, which would give a score of 50%. 
Similar effects also apply to other metrics, and these can similarly be balanced based on the data available. 
