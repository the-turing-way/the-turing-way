(ml-dev-checklist)=
# Checklist

> **#TODO:**
> List out the action points you want the readers to take based on the key ideas in your chapter.
> Aim for three action points for each topic, however, you can have more than this threshold.
> Aim for a through checklist that can help developers to review all steps of ML Pipelines.

The Turing Way chapters traditionally include a checklist to summarize the key content points. Below is a checklist for developers of machine learning (ML) powered systems to consider throughout the project. This chapter provides an introductory overview for the following questions:

The key question that can prevent harmful outcomes caused by an ML-enabled system is:
- [ ] Is using ML essential for this project?

ML is great for learning patterns from data. But, not every project requires this kind of feature. If your project would benefit from ML-enabled features, start asking the following questions for each trustworthiness component[^nist] (robustness, security, privacy, fairness, explainability, transparency) to achieve equitable AI development:

- [ ] What are the goals and success metrics [for fairness]?
- [ ] What standards or guidelines should be used to assess and manage risks [related to fairness]?
- [ ] How can I gather data that is both useful and ethical [to achieve fair behaviour]?
- [ ] How can I train sustainable and maintainable ML models [considering fairness]?
- [ ] How will I monitor the deployed model and address potential data drift [considering fairness]?

# Further Reading

The following resources present a deeper exploration of best practices and development techniques:

| Resource | Link | Summary |
| -------------|----------| ----------|
| Techworks Best Practices | <https://techworkshub.github.io/best-practice-guide/index.html> | This guide inspired the above checklist and provides detailed answers to each question. |
| Equitable AI Cookbook | <https://asabuncuoglu13.github.io/equitable-ai-cookbook/> | Another project by the Alan Turing Institute researchers, this project focuses on equitable AI best practices. |


[^nist]: NIST AI Risk Management Framework defines trustworthiness with seven sub-components (e.g. robustness, security, privacy fairness, etc.), and each subcomponent requires a careful evaluation based on specific use cases. <https://www.nist.gov/itl/ai-risk-management-framework>