# How to Write an Effective Prompt

Writing an effective prompt can sometimes feel overwhelming because the user must think about context, task, constraints, audience, and output format all at once. A practical way to simplify the process is to use a repeatable structure.

An effective prompt usually contains these elements:

- **Role**: Who should the AI act as?
- **Context**: What background information does the AI need?
- **Task**: What exactly should the AI do?
- **Audience**: Who will use the output?
- **Constraints**: What should be included, excluded, or handled carefully?
- **Evidence boundary**: What sources should the AI rely on?
- **Output format**: How should the answer be presented?

A strong prompt might look like this:

```text
Act as a clinical research methodologist.

Context:
+We are reviewing a retrospective cohort study about treatment outcomes in pediatric oncology.

Task:
+Summarize the study design and identify methodological strengths and limitations.

Constraints:
+Do not make claims beyond the provided text. Separate confirmed findings from assumptions. Highlight possible confounders, bias, missing data concerns, and generalizability limits.

Audience:
+Clinical researchers, physicians, and data analysts.

Output:
+Use sections for Study Design, Population, Outcomes, Strengths, Limitations, Bias/Confounding, and Questions for Authors.
```

Good prompts are specific but not overloaded. They provide enough information for the AI to succeed while keeping the instruction focused.

When writing prompts, consider these practices:

- Define the AI's role clearly
- Provide business, clinical, scientific, or technical context
- State the exact task
- Identify the intended audience
- Mention what to include and exclude
- Ask for a specific output format
- Provide examples when consistency matters
- Ask the model to identify assumptions
- Ask for risks, limitations, and gaps
- Require evidence boundaries when working with source material
- Review and refine the result

A weak prompt asks for a summary. A strong prompt asks for the right summary, for the right audience, using the right evidence, in the right format.


## Prompt Engineering Frameworks

Frameworks help make prompts repeatable. They are especially useful for teams because they reduce variation and improve consistency.

### TAO Framework

TAO stands for **Thought, Action, and Observation**. It is often used in agent-style AI workflows where the model analyzes a task, performs an action, observes the result, and continues toward a goal.

In healthcare, research, software, and testing workflows, TAO can be adapted as follows:

- **Thought**: Understand the problem, context, stakeholders, risks, assumptions, and evidence.
- **Action**: Summarize, classify, compare, extract, generate, test, validate, or recommend.
- **Observation**: Report findings, limitations, uncertainties, gaps, and next steps.

Example:

```text
Use the TAO framework to review this clinical research abstract.

Thought:
+Identify the research question, study population, intervention/exposure, outcomes, and assumptions.

Action:
+Extract key methodological details and summarize the main findings.

Observation:
+List limitations, missing information, potential sources of bias, and follow-up questions.
```

TAO is useful when the task involves investigation, not just generation. It can help professionals move from understanding a problem to producing an output and then evaluating whether anything is missing.

### CO-STAR Framework

CO-STAR is a prompt framework that stands for:

- **C**: Context
- **O**: Objective
- **S**: Style
- **T**: Tone
- **A**: Audience
- **R**: Response format

Example:

```text
Context:
+We are preparing a patient-friendly explanation of genetic testing results for a hospital genetics clinic.

Objective:
+Explain what the test can and cannot tell the patient, including limitations and the need for clinician interpretation.

Style:
+Clear, structured, and accessible.

Tone:
+Calm, respectful, and non-alarming.

Audience:
+Patients and family members without medical training.

Response format:
+Use short sections, plain language, and a final list of questions the patient may ask their clinician.
```

CO-STAR is useful because it forces the prompt writer to think beyond the task. It considers why the output is needed, who will use it, and how the answer should be shaped