(ml-dev-finance)=
# Use Case: Credit Scoring Risk Prediction ML Pipeline

> **#TODO:**
> This is a template. Review it and make any contributions as you like.
> Talk about all key stages in detail. Feel free to use images, code blocks, and admonitions to communicate your ideas.
> Add diagrams for better communication.


## 1. **Data and Task Setup**

### 1.1 **Task Description**
- **Objective:** Predict the likelihood of a loan applicant defaulting on their loan, based on historical data.
- **Target variable:** Loan default (binary: defaulted vs. not defaulted).

### 1.2 **Data Collection**
- **Sources:** Bank transaction histories, credit bureau reports, income levels, employment history, and demographic information.
- **Volume:** Dataset of [X number of] historical loan applicants over [time period].
- **Sensitive Attributes:** Age, gender, race, and location (which could lead to indirect biases).

### 1.3 **Fairness: Population Balance**
- **Fairness Considerations:** Ensure representation across socioeconomic classes, minority groups, and other protected attributes. Initial exploration revealed that [e.g., minority group X] is underrepresented in the training data, which was mitigated by resampling techniques.

### 1.4 **Explainability: Data Collection and Labelling**
- **Documentation:** A comprehensive record of how each data source was collected, how variables were labeled (e.g., income brackets), and assumptions made during data integration.

---

## 2. **Feature Pre-processing**

### 2.1 **Pre-processing Steps**
- **Missing Data Handling:** Imputed missing income data using [method], normalized continuous variables (e.g., income, credit score).
- **Feature Engineering:** Created additional features such as debt-to-income ratio and number of late payments in the last 12 months.

### 2.2 **Fairness: Fair Representations**
- **Fairness Considerations:** Ensured sensitive variables like race and gender were not explicitly used in feature selection but assessed potential proxies (e.g., zip code might serve as a proxy for race). Techniques such as [adversarial de-biasing] were used to reduce bias in the representations.

### 2.3 **Explainability: Dictionary of Variables**
- **Feature Explanation:** A dictionary of features was created, explaining each variable's source, meaning, and any transformations applied. For example, "credit utilization ratio" is derived from dividing total debt by available credit and was capped to mitigate extreme values.

---

## 3. **Model Selection**

### 3.1 **Model Choices**
- **Selected Model:** A [Random Forest/Gradient Boosting/Logistic Regression] model was selected for its ability to handle non-linear relationships and categorical variables.
- **Alternative Models Considered:** Linear regression (due to simplicity and interpretability) and deep learning models (for complex relationships), but rejected due to [specific reasons like overfitting or lack of interpretability].

### 3.2 **Explainability: Model Complexity**
- **Model Trade-offs:** While more complex models (e.g., Gradient Boosting) improved accuracy, simpler models (e.g., Logistic Regression) were considered for better explainability. Final choice balanced these concerns by using SHAP values for interpretability.

### 3.3 **Fairness: Fairness Constraints**
- **Fairness Constraints Applied:** Added fairness constraints during training, ensuring that the model did not disproportionately reject applications from specific demographic groups. Techniques such as demographic parity or equalized odds were evaluated to check for fairness violations.

---

## 4. **Post-processing and Reporting**

### 4.1 **Model Evaluation**
- **Performance Metrics:** Evaluated using accuracy, F1-score, and AUC for overall model performance. Fairness was evaluated by looking at False Positive and False Negative rates across demographic groups.

### 4.2 **Fairness: Bias Metrics Assessments**
- **Bias Assessment:** Used fairness metrics like disparate impact to evaluate the model’s predictions across different groups (e.g., gender, race). Initial analysis showed higher rejection rates for [group], leading to adjustments through post-processing (e.g., re-weighting or recalibrating predictions).

### 4.3 **Explainability: Auxiliary Tools**
- **Tools for Explainability:** SHAP values and LIME were used to explain individual predictions to stakeholders. These tools helped explain why certain applicants were classified as high-risk, with explanations linking back to interpretable features like income, credit history, or payment patterns.

---

## 5. **Productionizing and Deploying**

### 5.1 **Deployment Strategy**
- **Real-time Monitoring:** The model is deployed in a live banking environment, where predictions are used to approve or reject loan applications. Continuous monitoring of performance and fairness metrics is in place.

### 5.2 **Fairness: Real-time Monitoring of Bias Metrics**
- **Bias Monitoring:** Real-time bias metrics such as disparate impact and group fairness are monitored to detect any drift or degradation in model fairness over time. Alerts are triggered if the model starts favoring or penalizing any demographic group disproportionately.

### 5.3 **Explainability: Interface and Documentation**
- **User Interface:** A simple, interpretable interface was built for loan officers to view individual risk scores and explanations behind each decision. Detailed documentation of the model’s functioning, limitations, and fairness audits is available to users and auditors.
