(ml-dev-finance)=
# Use Case: Credit Scoring Risk Prediction ML Pipeline

[ML Development Process in a Fairness Oriented Approach](./ml-dev-pipeline.md) listed some suggestions to achie safer and fairer ML development. Here, the credit risk prediction use case demonstrates the application of suggested actions.

```{note}
This use case is based on [Fairlearn's Credit Loan Notebook](https://fairlearn.org/v0.12/auto_examples/plot_credit_loan_decisions.html) as a reference implementation to evaluate and mitigate fairness considerations. 

Also check [FAID - Credit Scoring Demo](https://github.com/asabuncuoglu13/faid/blob/main/demos/credit-scoring-default/demo_credit_loan_decisions.ipynb) to observe the use of metadata management as a fairness monitoring approach in action.
```

## 0. **Task Setup**

- Set up experiment monitoring (e.g. wandb, neptune, or customised logs)
- Set up metadata management (e.g. FAID). The metadata can be structured like:
  - Model documentation
  - Data documentation
  - Usecase documentation
  - Risk documentation
  - Experiment logs
- Set up a risk management plan (e.g. ISO31000 based documentation throughout the project lifecycle)
- Review previous incidents (e.g. Apple's recent gender-biased credit card application incident: <https://incidentdatabase.ai/cite/92/#r2035>)

**Also, check the related industry standards before the development process:**

| Fairness terminology| Management and governance | Measurement and test | Performance requirements |
---- | ---- | ---- | ----|
| IEEE P7003 | ISO/IEC 42001 | ISO/IEC TR 24027 | ISO/IEC TR 24027 |
| ISO/IEC TR 24027 | ISO/IEC 23894 | ISO/IEC TS 12791 | ISO/IEC 12791 |
| | ISO 31000 | | |

---

## 1. **Data and Task Setup**

- **Objective:** Predict the likelihood of a loan applicant defaulting on their loan, based on historical data.
- **Target variable:** Loan default (binary: defaulted vs. not defaulted).
- **Dataset Description:** This use case uses a publicly available dataset of credit card defaults in Taiwan collected in 2005. However, open-source datasets are often not adequate to train models that reliably performs in real-life scenarios. So, consider including: 

  - **Multiple sources:** Bank transaction histories, credit bureau reports, income levels, employment history, and demographic information. 
  - **Varying amounts of volume:** Multiple datasets of historical loan applicants over different time periods.
  - **Balanced sensitive attributes representation:** Age, gender, and race are direct sensitive characteristics (based on equality and human rights). Location/postcode information could lead to indirect biases by implicitly reveal ethnicity.

Ensure representation across socioeconomic classes, minority groups, and other protected attributes.  For example, initial exploration revealed that females are represented more in the dataset in this use case. Resampling techniques can be utilised to mitigate this kind of representation biases.

Keep a comprehensive record of how each data source was collected, how variables were labeled (e.g., income brackets), and assumptions made during data integration. In this case, the dataset is obtained from UCI ML Dataset Repository (id = 350). The metadata and variable information can be viewed programmatically:

```python
from ucimlrepo import fetch_ucirepo 
# fetch dataset 
default_of_credit_card_clients = fetch_ucirepo(id=350) 
# metadata 
print(default_of_credit_card_clients.metadata) 
# variable information 
print(default_of_credit_card_clients.variables) 
```

---

## 2. **Feature Pre-processing**

When we look at the distribution of the *loan default rate* in our data, we see that about 78% of individuals do not default on their loans. This means the dataset is somewhat imbalanced, as most people belong to the "no default" category. While this imbalance isn’t extreme, it’s still important to address it when building our models. 

If we ignore the imbalance, the model might become biased toward the majority group (the "no default" cases). For example, a simple model that always predicts "no default" would be correct 78% of the time, but it wouldn’t actually be useful for identifying individuals who are likely to default. 

To handle this issue, we can use the `balanced_accuracy` score as our evaluation metric. This metric ensures that the model pays equal attention to both groups—those who default and those who don’t—so that it doesn’t over-prioritize the majority class. 

On the other hand, this type of imbalance in the *target label* (whether someone defaults or not) is different from imbalances in a *sensitive feature* like `SEX`. Imbalances in sensitive features can raise fairness concerns, while target label imbalances primarily affect model performance.

Here, we listed some other concerns that needs to be handled frequently:
- **Missing Data Handling:** Impute missing data, normalize continuous variables (e.g., income, credit score).
- **Feature Engineering:** Create additional features such as debt-to-income ratio and number of late payments to better understand your data and impact of combination of features in your model performance.
- **Fairness Considerations:** Ensure sensitive variables like race and gender are not explicitly used in feature selection but assessed potential proxies (e.g., zip code might serve as a proxy for race). Techniques such as adversarial de-biasing can be used to reduce bias in the representations.
- **Feature Explanation:** A dictionary of features should be included, explaining each variable's source, meaning, and any transformations applied. For example, "credit utilization ratio" is derived from dividing total debt by available credit and was capped to mitigate extreme values.

---

## 3. **Model Selection**

### 3.1 **Model Choices**

In the model selection, development teams are constrained due to several factors such as regulatory, performance, or fairness requirements. For example, they can choose to use a [Random Forest/Gradient Boosting/etc.] model for its ability to handle non-linear relationships and categorical variables.

However, if the team has to explain the decisions of this automated system, they can choose to use linear regression. However, these models are often rejected due to [specific reasons like overfitting or lack of performance].

```{note}
For example, check the [Equal Opportunity paper](https://arxiv.org/abs/1610.02413) to showcase how fairness constraints can affect the model development process.
```

Some additional considerations that might impact overall fairness:

- **Model complexity considerations:** While more complex models (e.g., Gradient Boosting) can improve accuracy, simpler models (e.g., Logistic Regression) can be considered for better explainability. However, blackbox models can be also interpreted using individual fairness techniques such as testing against counterfactuals. 
  
```{note}
Check [Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR](https://arxiv.org/abs/1711.00399).
```

- **Fairness Constraints** Fairness constraints during training, ensuring that the model did not disproportionately reject applications from specific demographic groups. Techniques such as demographic parity or equalized odds were evaluated to check for fairness violations.

Since the model performance can be evaluated using sub-group, we can use group-fairness metrics to measure fairness:

- **Statistical Parity Difference:** Measures the difference in positive outcome rates between protected and unprotected groups.
- **Disparate Impact:**	Assesses whether decisions disproportionately affect members of a protected group, typically requiring a ratio between rates.
- **Demographic Parity:** Evaluates if the outcome is independent of the protected attributes, aiming for equal outcome rates across groups.
- **Equal Opportunity Difference:**	Computes the difference in true positive rates between groups, assessing fairness in terms of equal opportunity.
- **Average Odds Difference:** Calculates the average difference in false positive and true positive rates between groups.

```{note}
Check [Fairness Metric Ontology](https://github.com/frankj-rpi/fairness-metrics-ontology) as a starting point for selecting fairness notion and metric.
```

---

## 4. **Post-processing and Reporting**

After running and assessing:

- **Performance Metrics:** Accuracy, F1-score, and AUC for overall model performance. 
- **Fairness Metrics:** False Positive and False Negative rates across demographic groups for fairness.
- **Local and global feature importance:** SHAP values and LIME.

Bias mitigation methods are chosen. For example, `ThresholdOptimizer` is a tool that works with an existing machine learning model (which can already be trained or not). It uses the model's predictions as scores and determines separate decision thresholds for each group defined by a *sensitive feature*. 

The goal of the `ThresholdOptimizer` is to improve the fairness of the model by optimizing a specific performance metric (in our case, `balanced_accuracy`) while ensuring it meets a fairness requirement, such as [equalized odds](https://en.wikipedia.org/wiki/Fairness_(machine_learning)). The result is a modified version of the original model that applies these thresholds to make fairer predictions.

---

## 5. **Productionizing and Deploying**

- **Real-time Monitoring:** When the model is deployed in a live environment, where predictions are used to approve or reject loan applications, continuous monitoring of performance and fairness metrics should be in place.
- **Bias Monitoring:** Real-time bias metrics such as disparate impact and group fairness should be monitored to detect any drift or degradation in model fairness over time. Alerts are triggered if the model starts favoring or penalizing any demographic group disproportionately.
- **User Interface:** A simple, interpretable interface can be built for both loan officers and development team to view model behaviour and explanations. Detailed documentation of the model’s functioning, limitations, and fairness audits should be available to users and auditors.