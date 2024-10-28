(ml-dev-pipeline)=
# ML Development Process in a Fairness Oriented Approach

> **#TODO:**
> This is a template. Review it and make any contributions as you like.
> Talk about all key stages in detail. Feel free to use images, code blocks, and admonitions to communicate your ideas.
> Add real-life examples from a variety of fields.
> Final Review
> Remember to use the [style guide](https://book.the-turing-way.org/community-handbook/style.html) and Jupyter Book's [Cheat Sheet](https://jupyterbook.org/reference/cheatsheet.html) to guide your writing.
> The [style guide](https://book.the-turing-way.org/community-handbook/style/style-citing.html) also contains _The Turing Way's_ recommendations for referencing and citation.
> To include an image in your writing, use the MyST directive shown below. 
> Remember to add your image to the `figures` [folder](https://github.com/the-turing-way/the-turing-way/tree/main/book/website/figures) and use the correct path, else it will not be displayed.
> See more about styling and chapter template here: <https://github.com/the-turing-way/the-turing-way/tree/main/book/templates/chapter-template>

Building an end-to-end ML pipeline is a challenging process. Keeping a proactive focus on potential security, privacy, fairness, or any other safety related issue makes the process more challenging. In this sense, reviewing the overall pipeline, regardless of its type, is a dynamic and non-linear process. Koshiyama et al. demonstrated the interrelation between development stages and auditing verticals for fairness and explainability in five main steps {cite}`koshiyama_towards_2021`:

**Stages:** | Data and Task Setup | Feature pre-processing | Model selection | Post-processing and Reporting| Productionizing and Deploying
----|---- | ---- | ----| ---- | ---- |
**Explainability**| Data collection and labelling | Dictionary of variables | Model complexity | Auxiliary tools | Interface and documentation
**Fairness** | Population balance | Fair representations | Fairness constraints | Bias metrics assessments | Real-time monitoring of bias metrics

(ml-dev-pipeline-1)=
## Data and Task Setup

In most machine learning pipelines, the first step is setting up the task and gathering the necessary data. A fairness-oriented approach begins with understanding the context of the data, its sources, and any potential biases that may be inherent due to historical or societal factors. Ensuring that the data represents all relevant subgroups equitably is crucial for preventing downstream issues. Additionally, clear labelling and comprehensive metadata should be maintained for transparency. In this stage, collaboration with domain experts can help identify subtle biases in the data that might otherwise go unnoticed.

### Data Collection and Labelling
Explainability in this stage focuses on documenting the process of data collection and labelling. Ensuring that the collection is consistent, representative, and transparent allows others to understand the origin of the dataset and the rationale behind labelling choices. This documentation should be made available to ensure that decisions made here can be traced and scrutinized later.

### Population Balance
Fairness starts with making sure the dataset includes diverse representations of the target population. This means identifying imbalances or underrepresentation of certain groups and taking steps to mitigate these issues, either through balanced data sampling, augmentation techniques, or bias-aware collection processes.

(ml-dev-pipeline-2)=
## Feature Pre-processing

Once data is collected, the next step is transforming it into a format suitable for the model. This includes handling missing data, normalizing features, and encoding categorical variables. However, this process can unintentionally introduce biases. For example, encoding methods or normalization schemes could disadvantage certain groups if not carefully designed. A fairness-aware pre-processing approach actively looks for such risks.

### Dictionary of Variables
Creating a dictionary of variables that clearly explains each feature’s meaning, origin, and transformation is key for explainability. This dictionary ensures that anyone reviewing the pipeline can understand how each feature was derived and its role in the model.

### Fair Representations
Feature pre-processing should be performed with fairness in mind, ensuring that the transformations do not introduce or amplify existing biases. Techniques such as adversarial de-biasing or learning fair representations can help ensure that sensitive attributes (e.g., race or gender) do not disproportionately influence the model outcomes.

(ml-dev-pipeline-3)=
## Model Selection

Selecting a model involves choosing the algorithm that will learn from the data. In a fairness-oriented pipeline, model selection should prioritize not only accuracy but also fairness constraints. Certain models, such as decision trees, may provide better explainability, while others, such as deep neural networks, may offer higher performance but less interpretability. The trade-offs between explainability, fairness, and performance need to be carefully balanced.

### Model Complexity
The complexity of the chosen model affects how interpretable its predictions are. For example, linear models are easier to explain but may not capture complex relationships in the data, whereas more complex models like neural networks can be more accurate but harder to interpret. The choice should align with both the project’s needs and its fairness goals.

### Fairness Constraints
Incorporating fairness constraints into model training is a proactive way to ensure that the model’s outcomes are equitable. This could involve methods like demographic parity, equal opportunity, or equalized odds, depending on the fairness objectives of the project. Careful evaluation during this stage can prevent unfair treatment of certain subpopulations.

## Post-processing and Reporting

After a model is trained, the next step is post-processing and evaluating its outcomes. This stage is critical for both fairness and explainability. Bias may not become apparent until this step, and without proper reporting, it may be difficult to detect and rectify unfair outcomes. Transparency in how decisions are made by the model and clear communication with stakeholders are essential.

### Auxiliary Tools
Explainability at this stage often relies on auxiliary tools like SHAP or LIME that help interpret the model’s predictions. These tools make it possible to explain individual predictions, allowing stakeholders to understand why certain outcomes were produced. Such tools are especially valuable for communicating model behavior to non-technical audiences.

### Bias Metrics Assessments
Post-processing must include a thorough evaluation of fairness through bias metrics. This can involve checking for disparate impact, group fairness metrics, or individual fairness measures. By quantifying bias in the model’s predictions, corrective actions can be taken if unfair outcomes are detected. Adjustments like reweighting or recalibrating predictions can be applied to enhance fairness at this stage.

## Productionizing and Deploying

Deploying the model into a production environment introduces new challenges in maintaining fairness and explainability. Once live, the model’s performance and fairness must be continuously monitored to ensure that it remains aligned with both accuracy and fairness goals. Real-world data distribution can shift over time, leading to model degradation or bias accumulation.

### Interface and Documentation
When deploying a model, maintaining detailed documentation of how the system works is essential for both transparency and accountability. A clear user interface that allows for human oversight and provides meaningful explanations for decisions ensures that the model remains interpretable in production. Additionally, well-structured documentation provides a reference for audits and ongoing evaluations.

### Real-time Monitoring of Bias Metrics
Fairness in deployment requires ongoing monitoring of bias metrics in real-time. This involves setting up triggers or alerts for significant shifts in bias or performance degradation. It’s critical to establish mechanisms for feedback and regular re-evaluation to ensure the model remains fair and unbiased as new data enters the system.