# Types of Prompting Techniques

Different prompting techniques are useful for different kinds of tasks. Some are simple and fast, while others are better for complex reasoning, comparison, planning, or structured analysis.

## Zero-Shot Prompting

Zero-shot prompting means asking the model to perform a task without giving examples. The model relies only on the instruction and its general training.

Example:

```text
Explain the difference between sensitivity and specificity in diagnostic testing.
```

This technique is useful when the task is common, simple, or exploratory. It works well for quick explanations, first drafts, definitions, summaries, and brainstorming.

Examples across professions:

```text
Summarize the main limitations of this clinical study.
```

```text
Generate a checklist for validating a healthcare data import pipeline.
```

```text
Explain this lab result in patient-friendly language at an eighth-grade reading level.
```

Zero-shot prompting is fast, but the result may be generic. For high-stakes tasks, the output should be refined with source material, constraints, and expert review.

## Few-Shot Prompting

Few-shot prompting means giving the model a few examples before asking it to produce a similar output. This helps the model understand the desired style, format, level of detail, and structure.

Example:

```text
Here is the format I want:

Finding: Elevated fasting glucose
Interpretation: May suggest impaired glucose regulation; interpret with clinical context.
Follow-up: Consider repeat testing or additional evaluation based on clinician judgment.

Now use the same format to explain the following lab findings.
```

Few-shot prompting is useful when consistency matters. It is helpful for clinical note summaries, literature extraction tables, patient education material, test case design, defect summaries, data review reports, and manuscript editing.

Another example:

```text
Example output:
Study Objective: ...
Population: ...
Methods: ...
Key Findings: ...
Limitations: ...

Now extract the same fields from the following abstract.
```

## Chain-of-Thought Prompting

Chain-of-thought prompting asks the model to work through a problem step by step. It can be useful for complex analysis, such as evaluating study design, comparing treatment options, reviewing data quality, or identifying possible causes of a software failure.

Example:

```text
Analyze this research question step by step. Identify the population, intervention, comparator, outcome, study design considerations, possible confounders, and limitations.
```

In professional usage, it is often better to ask for a concise rationale or structured explanation rather than a long internal reasoning trace. For example:

```text
Provide your final recommendation and include a brief rationale, key assumptions, and limitations.
```

This keeps the output useful, reviewable, and concise.

## Meta Prompting

Meta prompting is the technique of asking the model to improve, evaluate, or generate prompts. Instead of directly asking for the final output, the user asks the AI to help design a better prompt for the task.

Example:

```text
Create a strong prompt that I can use to summarize clinical trial papers. The prompt should require the model to extract study objective, population, intervention, comparator, outcomes, adverse events, limitations, and level of evidence.
```

Meta prompting is valuable when teams want reusable prompt templates. It helps standardize how AI is used across research, clinical operations, software development, testing, and reporting workflows.

## Tree of Thoughts

Tree of Thoughts is a prompting approach where the model explores multiple possible solution paths before selecting or recommending the best answer. Instead of producing one immediate response, the model considers alternatives.

Example:

```text
Suggest three possible approaches for analyzing this dataset: a descriptive analysis approach, a statistical modeling approach, and a machine learning approach. Compare the strengths, limitations, assumptions, and risks of each, then recommend the most appropriate approach for a clinical research team.
```

This technique is useful for complex planning, research design, differential analysis, software architecture decisions, quality strategy, and risk assessment. It encourages broader thinking and reduces the chance of accepting the first obvious answer.