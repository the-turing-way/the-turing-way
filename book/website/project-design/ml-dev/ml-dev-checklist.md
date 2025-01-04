(ml-dev-checklist)=
# Checklist

> **#TODO:**
> List out the action points you want the readers to take based on the key ideas in your chapter.
> Aim for three action points for each topic, however, you can have more than this threshold.
> Aim for a through checklist that can help developers to review all steps of ML Pipelines.

The Turing Way chapters traditionally include a checklist to summarize the key content points. Below is a checklist for developers of ML-powered systems to consider throughout the project. This chapter provides an only introductory overview of these questions.

The main question that can prevent bias caused by an AI-infused system is:
- [ ] Is using ML essential for this project?

ML is great for learning patterns from data. But, not every project requires this kind of feature. If your project requires ML development, start asking these question for each trustworthiness component (robustness, security, privacy, fairness, explainability, transparency) to achieve equitable AI development:

- [ ] What are the goals and success metrics [for fairness]?
- [ ] What standards or guidelines should be used to assess and manage risks [related to fairness]?
- [ ] How can I gather data that is both useful and ethical [to achieve fair behaviour]?
- [ ] How can I train sustainable and maintainable ML models [considering fairness]?
- [ ] How will I monitor the deployed model and address potential data drift [considering fairness]?

The following resources present a deeper exploration of best practices and development techniques:

| Resource | Link | Summary |
| -------------|----------| ----------|
| Techworks Best Practices | <https://techworkshub.github.io/best-practice-guide/index.html> | This guide inspired the above checklist and provides detailed answers to each question. |
| Equitable AI Cookbook | <https://asabuncuoglu13.github.io/equitable-ai-cookbook/> | Another project by the Alan Turing Institute researchers, this project focuses on equitable AI best practices. |