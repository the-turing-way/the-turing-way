# ML Development: Safety Recipes

We curated some best practices as recipes for safe AI development. We have five main courses in the menu: Trecability, responsibility, explainability, auditability, digestability. 

## Recipe 1: Tracability

We should aim for developing a tracable supply chain management for our ML codebase, so that we can easily identify the source when a vulnerability occurs. To create a "traceability" plan for effectively tracing vulnerabilities, an interdisciplinary ML team can follow these steps:

1. **Establish Version Control and Logging:** Use tools like Git for code and DVC for data checkpoints. You should ensure logging key steps in the ML lifecycle, including data preprocessing, training runs, hyperparameters, and results.
2. **Document End-to-End Processes:** Maintain detailed records of data sources, preprocessing steps, model architectures, and evaluation protocols. Use lineage tools (such as W&B, MLflow, Neptune) to track experiments.
3. **Data Provenance Tracking:** Log the origin, transformations, and usage of datasets. Ensure metadata includes timestamps, contributors, and dataset versions. Choose a dataset recording format and stick with it for all datasets used in the training process.
4. **Dependency Management:** Use standardised approaches such as Bill of Materials (SBOM, AIBOM) to manage dependencies of codebase. Run regular vulnerability analysis for these dependencies.
5. **Monitor and Audit Changes:** Implement change logs for updates to data, model parameters, or deployment environments. Regularly audit changes to identify potential vulnerability sources.
6. **Enable Root Cause Analysis:** Build diagnostic tools to reproduce model predictions, including intermediate outputs, feature importance, and model decision pathways. Include input-output mappings in the logging system for debugging.

## Recipe 2: Responsibility

Responsibility is considering sociotechnical issues throughout the development and monitoring societal impact of the developed tool after deployment. A responsibility plan ensures the ML tool aligns with ethical principles, considers sociotechnical challenges, and continuously monitors its societal impact.

1. **Establish Ethical Principles**: Define guiding principles such as fairness, accountability, transparency, and inclusivity. Align with frameworks like the *AI Ethics/Responsibility Guidelines* (e.g., OECD, Microsoft, Google). Map your company principles to legal requirements such as EU AI Act.
2. **Create a Responsibility Matrix** Assign clear roles to team members for ethical oversight, impact assessment, remediation ownership. Use tools like a RACI chart (Responsible, Accountable, Consulted, Informed).
3. **Stakeholder Engagement** Include diverse perspectives by involving both end-users, domain experts, and vulnerable communities in design and testing. Conduct regular consultations with external ethicists, sociologists, and legal advisors. Establish feedback mechanisms for continuous stakeholder input.
4. **Sociotechnical Risk Assessment** Conduct structured assessments, considering technical capacity, human interaction, and systemic impact layers (see Deepmind's paper: https://arxiv.org/pdf/2310.11986#page=31.10).
5. **Develop Customised Metrics for Societal Impact** Monitor fairness, equity, trustworthiness metrics like, and create your customised metrics based on your use case. Create customised benchmarks based on the existing benchmarks and continuously refine them based on stakeholder feedback.
6. **Incident Reporting System** Create channels for users and stakeholders to report ethical concerns and unintended harms or misuse. Ensure reports are logged, prioritized, and addressed transparently.
7. **Ethics Review Board** If you don't already have, establish an interdisciplinary review board with representatives from interdisplinary areas such as ethics, sociology, law, and technical domains. If you have a review board, ensure they consider the latest developments and potential harms.

## Recipe 3: Explainability

We should be able to explain the output of our AI system. Here, we don't mean completely interpretable models like decision trees, or local explanations methods like SHAP. The explaination can also be an intuitive explanation combining multiple techniques. But, every stakeholder behind the model should understand the model capabilities and either completely or intuitively explain the model decisions by listing clear reasons. An explainability plan ensures that the ML system's behavior can be understood and communicated effectively to stakeholders, regulators, and users. Here's a structured plan:

1. **Define Explainability Goals** Identify stakeholders (e.g., developers, end-users, regulators) and their needs. Set objectives to explain individual predictions (local explainability) and understand the model's overall behavior (global explainability).
2. **Select Explainability Techniques**
   - **Model-Agnostic Methods:** SHAP, LIME, or Partial Dependence Plots (PDP) can interpret model predictions across models. Note that, these methods focus on local explanations, and can potentially misguide developers by priorising certain features for the selected local area.
   - **Model-Specific Techniques:** Leverage built-in features (e.g., feature importance in decision trees, saliency maps for neural networks).
   - **Simplified Surrogate Models:** Train interpretable models (e.g., linear regression, decision trees) to approximate complex models.
3. **Embed Explainability in Development** Maintain clear documentation of data features, sources, and preprocessing steps. During model development, evaluate which features contribute most to predictions. If no clear evidence (such as performance trade-offs) is provided to favour a black-box model, prefer inherently interpretable models (e.g., linear/logistic regression).
4. **Evaluate Explainability Quality** Use human-centric metrics like comprehensibility, consistency, and actionability. Ask yourself the following questions:
   - Do non-technical stakeholders understand the explanations? (comprehensibility)
   - Are similar predictions explained similarly? (consistency)
   - Can users act on the provided explanations? (actionability)
5. **Implement Documentation Standards** Log explanations alongside predictions for audit trails. Document simplifications, biases, or risks that might affect interpretations. Record how model updates affect explainability metrics.

## Recipe 4: Auditability

We should aim for documenting clear KPIs and success metrics for our safety goals and claims. To define clear KPIs for safety claims in an interdisciplinary ML team as part of an auditability plan, follow these steps:

1. **Define Safety Goals:**  Identify specific safety claims relevant to the ML system (e.g., fairness, reliability, robustness, and compliance). Involve domain experts, data scientists, and stakeholders to ensure metrics reflect both technical performance and domain-specific safety requirements.
2. **Make Metrics Quantifiable:**  Create measurable KPIs. For example, a fairness KPI can be quantifiable representation of disparity in outcomes across demographic groups (e.g., ≤ 5% difference in false positive rates).
3. **Document Assumptions:**  Record why specific KPIs were chosen and how they map to safety claims to ensure traceability.
4. **Establish Benchmarks:** Set thresholds for acceptable performance and ensure alignment with regulatory or organizational standards.
5. **Monitor Regularly:**  Use dashboards or reports to continuously track KPIs during development and deployment, adjusting as needed.
6. **Implement Automated Testing:** Develop unit tests and end-to-end tests to check for errors or inconsistencies in data and models.

## Recipe 5: Digestability

We should increase the visibility of the decisions and potential vulnerabilities and make them digestable for diverse stakeholders. A digestibility plan ensures that potential issues and vulnerabilities are surfaced, easily understood, and actionable by relevant stakeholders throughout the Continuous Integration/Continuous Deployment (CI/CD) pipeline. Here's the structured plan:

1. **Centralized Dashboard for Real-Time Monitoring** Implement a central platform to display pipeline stages and their statuses, key metrics like test coverage, latency, and model drift, alerts for anomalies or failures. Use visual elements (charts, heatmaps, timelines) as much as possible for clarity. Create customasible presentations for different teams. 
2. **Notification and Escalation Channels** Configure automated alerts for different teams to assign responsibilities in an interdisciplinary team.
3. **Digestible Reporting** Create different types of reports for stakeholders. Based on your needs and resource availability customised it for business analysts, developers, and designers. Implement layered drill-down capabilities:  High-level overviews for managers and non-technical stakeholders, and detailed logs and traces for developers and DevOps teams.
4. **Knowledge Base for Recurrent Issues** Maintain a repository of known issues and solutions. Include FAQs, remediation workflows, and troubleshooting guides. Align them with the existing Incidents Databases such as https://incidentdatabase.ai/.


# The Ultimate Plan

Now, considering all these single recipes for each main course, here is the ultimate recipe for ensuring **traceability**, **auditability**, **explainability**, **digestibility**, and **responsibility** in developing and deploying ML tools.

| **Aspect** | **Traceability** | **Auditability** | **Explainability** | **Digestibility** | **Responsibility** |
|-------|-------|-------|-------|-------|-------|
| **1. Goals** | Track the source of vulnerabilities across data, models, and processes.         | Define KPIs to evaluate safety claims and compliance.                          | Ensure model behavior is interpretable for diverse stakeholders.            | Increase visibility and clarity of issues and vulnerabilities in the pipeline.    | Consider sociotechnical risks and monitor societal impact of the tool.            |
| **2. Tools**      | Use version control (Git, DVC), lineage tracking (MLflow, W&B), and dependency tools (SBOM, AIBOM). | Implement dashboards to track KPIs (e.g., fairness, robustness). | Leverage multiple explainability techniques by focusing on "what if". | Deploy centralized monitoring with automated alerts. | Use frameworks and participatory assessments to analyze societal impact.|
| **3. Processes**  | Log every stage of the pipeline with unique IDs and detailed metadata.          | Regularly evaluate KPIs with stakeholders to ensure alignment.                | Document data and model decisions, highlighting assumptions and biases.     | Categorize and tag issues by severity, type, and ownership for easier tracking.    | Conduct regular ethics reviews, audits, and consultations with stakeholders.      |
| **4. Monitoring** | Automate logging for data provenance, pipeline runs, and model updates.         | Monitor KPI trends continuously and adjust thresholds as necessary.           | Create reports showing local and global explainability metrics.            | Monitor pipeline health with visual summaries and layered drill-downs.            | Continuously evaluate societal impact through feedback, audits, and studies.      |
| **5. Communication** | Provide access to logs, documentation, and artifacts for all stakeholders.    | Publish safety performance reviews and incident analyses.                     | Share simplified and technical insights tailored to each stakeholder group. | Generate digestible reports (daily, weekly, postmortems) with clear visuals.       | Publish societal impact reports and host forums for public transparency.          |
| **6. Education**  | Train the team on traceability tools and documentation best practices.           | Educate stakeholders on the meaning and importance of KPIs.                   | Provide training on understanding explainability tools and their outputs.   | Train team members to interpret alerts, dashboards, and issue logs.               | Conduct workshops on sociotechnical risks and responsible AI development.         |
| **7. Continuous Improvement** | Simulate vulnerabilities and refine traceability practices iteratively. | Refine KPIs based on user feedback and audit results.                          | Test and improve explainability methods based on stakeholder usability.     | Collect feedback to improve reporting, categorization, and dashboards.            | Adjust the tool or policies to mitigate new societal risks and unintended effects. |