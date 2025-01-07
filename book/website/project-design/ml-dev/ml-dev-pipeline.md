(ml-dev-pipeline)=
# ML Development Process in a Fairness Oriented Approach

Building an end-to-end ML pipeline is a challenging process. Managing security, privacy, fairness, and other safety-related characteristics requires a holistic and proactive approach. In this proactive management process, reviewing the overall pipeline, identifying the potential issues, and mitigating the risks with appropriate solutions is a dynamic and non-linear process.

![The figure illustrates design, development, and evaluation stages of the system design process. In this process, confirmation bias in the requirement planning, historical bias in dataset selection, evaluation bias in model validation might occur. From a broader perspective, in continous integration and deployment process, development teams might observe selection bias and representation bias.](../../figures/cicd-bias.png)

For example, the figure above illustrates the potential biases that can occur in the continuous integration/continuous deployment process. In the system design stage, confirmation bias in the requirement planning, historical bias in dataset selection, evaluation bias in model validation might occur. Development teams might observe selection bias when picking the best performing model and representation bias throughout the user-interaction process. These potential harmful biases are only some challenges that are observed throughout the development process. Considering the complexity of logistics in the software development process, and other safety-related characteristics such as robustness and security considerations, it is clear that achieving a safe and reliable AI system requires a structured, proactive safety blueprints.

Koshiyama et al. demonstrated the interrelation between development stages and auditing verticals for fairness and explainability in five main steps {cite}`koshiyama_towards_2021`:

**Stages:** | Data and Task Setup | Feature pre-processing | Model selection | Post-processing and Reporting| Productionizing and Deploying
----|---- | ---- | ----| ---- | ---- |
**Explainability**| Data collection and labelling | Dictionary of variables | Model complexity | Auxiliary tools | Interface and documentation
**Fairness** | Population balance | Fair representations | Fairness constraints | Bias metrics assessments | Real-time monitoring of bias metrics

```{note}
This chapter summarises some suggestions for fair development practices. Check [Equitable AI Cookbok](https://asabuncuoglu13.github.io/equitable-ai-cookbook/index.html) to see a discussion of broader concepts of trustworthiness and real-life development considerations.
```

(ml-dev-pipeline-1)=
## Data and Task Setup

In most machine learning pipelines, the first step is setting up the task and gathering the necessary data. A fairness-oriented approach begins with understanding the context of the data, its sources, and any potential biases that may be inherent due to historical or societal factors.This means identifying imbalances or underrepresentation of certain groups and taking steps to mitigate these issues, either through balanced data sampling, augmentation techniques, or bias-aware collection processes.

Ensuring that the data represents all relevant subgroups equitably is crucial for preventing downstream issues. Additionally, clear labelling and comprehensive metadata should be maintained for transparency. In this stage, collaboration with domain experts can help identify subtle biases in the data that might otherwise go unnoticed.

Explainability in this stage focuses on documenting the process of data collection and labelling. Ensuring that the collection is consistent, representative, and transparent allows others to understand the origin of the dataset and the rationale behind labelling choices. This documentation should be made available to ensure that decisions made here can be traced and scrutinized later. Creating data cards and documenting fairness consideration in this documentation in a standardised format can help to understand possible issues beforehand. For example, [The Data Cards Playbook](https://sites.research.google/datacardsplaybook/) asks for data source distribution related to bias (e.g. geographic, and gender), and sampling tasks.

FAIR (Findable, Accessible, Interoperable, Reusable) principles are the most popular assessment criteria among the reproducible research community. The principles _"put specific emphasis on enhancing the ability of machines to automatically find and use the data, in addition to supporting its reuse by individuals."_

In line with FAIR principles, Pipino et al.’s data quality assessment framework offers a standardised and comprehensive approach to evaluating data quality, making it applicable to various industries [^pipino]. It has been adopted by businesses in the last two decades to ensure the reliability and usability of their data. By utilising this framework, development teams can systematically evaluate the data quality and identify areas for improvement.

| Useful Resources | Link | Explanation |
| -------------|----------| ----------|
| FAIR Data Principles | <https://book.the-turing-way.org/reproducible-research/rdm/rdm-fair> | Findable, Accessible, Interoperable, and Reusable (FAIR) - Turing Way Chapter|
|  |  |


(ml-dev-pipeline-2)=
## Feature Pre-processing

Once data is collected, the next step is transforming it into a format suitable for the model. This includes handling missing data, normalizing features, and encoding categorical variables. However, this process can unintentionally introduce biases. For example, encoding methods or normalization schemes could disadvantage certain groups if not carefully designed. A fairness-aware pre-processing approach actively looks for such risks.

**Creating a dictionary of variables** that clearly explains each feature’s meaning, origin, and transformation is key for explainability. This dictionary ensures that anyone reviewing the pipeline can understand how each feature was derived and its role in the model.

**Feature pre-processing** should be performed with fairness in mind, ensuring that the transformations do not introduce or amplify existing biases. Techniques such as adversarial de-biasing or learning fair representations can help ensure that sensitive attributes (e.g., race or gender) do not disproportionately influence the model outcomes.

| Useful Resources | Link | Explanation |
| -------------|----------| ----------|
| Fair Preprocessing: Towards Understanding Compositional Fairness of Data Transformers in Machine Learning Pipeline | <https://arxiv.org/pdf/2106.06054> | The paper analyses the existing pre-processing methods as potential bias sources. |

(ml-dev-pipeline-3)=
## Model Selection

Selecting a model involves choosing the algorithm that will learn from the data. In a fairness-oriented pipeline, model selection should prioritize not only accuracy but also fairness constraints. Certain models, such as decision trees, may provide better explainability, while others, such as deep neural networks, may offer higher performance but less interpretability. The trade-offs between explainability, fairness, and performance need to be carefully balanced.

**The complexity of the chosen model** affects how interpretable its predictions are. For example, linear models are easier to explain but may not capture complex relationships in the data, whereas more complex models like neural networks can be more accurate but harder to interpret. The choice should align with both the project’s needs and its fairness goals.

**Incorporating fairness constraints** into model training is a proactive way to ensure that the model’s outcomes are equitable. This could involve methods like demographic parity, equal opportunity, or equalized odds, depending on the fairness objectives of the project. Careful evaluation during this stage can prevent unfair treatment of certain subpopulations.

| Useful Resources | Link | Explanation |
| -------------|----------| ----------|
| Kaggle Models | https://www.kaggle.com/models | Models shared by Kaggle community |
| Huggingface Models | https://huggingface.co/models | Models shared by Huggingface community |

```{note}
Note that running open-weight models from unverified organisations carries similar security risks with running an executable from an unverified resource. Open-weight models can be susceptible to adversarial attacks, where malicious inputs could manipulate the model's behavior, leading it to produce incorrect or harmful outputs. 

[OWASP's AI Security and Privacy Guide](https://github.com/OWASP/www-project-ai-security-and-privacy-guide/) is an open source reference material to review the overall security concerns.
```

## Post-processing and Reporting

After a model is trained, the next step is post-processing and evaluating its outcomes. This stage is critical for both fairness and explainability. Bias may not become apparent until this step, and without proper reporting, it may be difficult to detect and rectify unfair outcomes. Transparency in how decisions are made by the model and clear communication with stakeholders are essential.

Explainability at this stage often relies on auxiliary tools like SHAP or LIME that help interpret the model’s predictions. These tools make it possible to explain individual predictions, allowing stakeholders to understand why certain outcomes were produced. Such tools are especially valuable for communicating model behavior to non-technical audiences.

Post-processing must include a thorough evaluation of fairness through bias metrics. This can involve checking for disparate impact, group fairness metrics, or individual fairness measures. By quantifying bias in the model’s predictions, corrective actions can be taken if unfair outcomes are detected. Adjustments like reweighting or recalibrating predictions can be applied to enhance fairness at this stage.

| Useful Resources | Link | Explanation |
| -------------|----------| ----------|
| A lecture from Carpentries on Fair and Explainable AI | https://carpentries-incubator.github.io/fair-explainable-ml/5a-explainable-AI-method-overview.html | Review of some explainability methods from a fairness-oriented perspective |

(ml-dev-pipeline-4)=
## Productionizing and Deploying

Deploying the model into a production environment introduces new challenges in maintaining fairness and explainability. Once live, the model’s performance and fairness must be continuously monitored to ensure that it remains aligned with both accuracy and fairness goals. Real-world data distribution can shift over time, leading to model degradation or bias accumulation.

**Maintaining detailed documentation** of how the system works is essential for both transparency and accountability when deploying a model. A clear user interface that allows for human oversight and provides meaningful explanations for decisions ensures that the model remains interpretable in production. Additionally, well-structured documentation provides a reference for audits and ongoing evaluations.

Fairness in deployment requires ongoing **monitoring of bias metrics in real-time**. This involves setting up triggers or alerts for significant shifts in bias or performance degradation. It’s critical to establish mechanisms for feedback and regular re-evaluation to ensure the model remains fair and unbiased as new data enters the system.

| Useful Resources | Link | Explanation |
| -------------|----------| ----------|
| Neptune AI's blog on CI/CD automation | https://neptune.ai/blog/automating-ml-experiment-management-with-ci-cd | It is a blog post on integrating Neptune's commercial product, however it is also a useful resource to understand potential CI/CD applications throughout the ML development |

[^pipino]: Data Quality Assessment. <https://dl.acm.org/doi/10.1145/505248.506010>