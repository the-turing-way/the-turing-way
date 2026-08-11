---
abbreviations:
  OSI: Open Source Initiative (https://opensource.org/) 
---
# Reproducibility in AI

### Why reproducibility matters in AI

AI systems have become a large part of human life and are increasingly used in our daily processes. Active and inactive users alike may interact with AI, either directly or indirectly.

For researchers, this raises questions about how AI applies to science and how we can create AI systems that support the principle of reproducibility. Reproducibility is particularly important in AI because AI research often involves many interacting components, including data, models, code, computational environments, and stochastic processes.

Reproducible research helps researchers examine, verify, and build on existing work. It provides a record of how results were produced, making it easier to identify errors, understand the basis for results, and avoid unnecessary duplication of effort.

In AI research, these principles are particularly important because the final result can depend on many different parts of the research process. Changes to the training data, code, model configuration, software, hardware, or computational environment can affect the resulting model or its outputs.

Understanding how these components affect reproducibility can therefore help researchers build on existing AI research and make its results easier to study and verify.

We write about the benefits of reproducibility more extensively in the [Added Advantages](https://book.the-turing-way.org/reproducible-research/overview/overview-benefit/) chapter of *The Turing Way*.

### What is an AI system?

Before discussing reproducibility in AI, it is useful to establish what we mean by an AI system. There are several definitions of artificial intelligence, two of which are highlighted here.

**Definition 1**

> Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making.
>
> It is a field of research in engineering, mathematics and computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.
>
> -- [Wikipedia](https://en.wikipedia.org/wiki/Artificial_intelligence#)

**Definition 2**

> An AI system is a machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.
>
> Different AI systems vary in their levels of autonomy and adaptiveness after deployment, as defined by the OECD.
>
> -- [Organisation for Economic Co-operation and Development (OECD)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_3c815e51/623da898-en.pdf)

For the purposes of this chapter, we use the OECD definition of an AI system [@oecd2024ai].

### What does "open source AI" mean?

When discussing reproducibility, it is useful to consider how it relates to openness. Although reproducibility and openness are not the same thing, they can overlap.

With AI, there is no universally agreed definition of what makes an AI system open source. Different definitions place emphasis on different components of an AI system. The discussion is usually about which structural elements of an AI system should be made available, how much of them should be available, and whether a single definition can adequately describe openness across different types of AI systems.

Several definitions and frameworks have been proposed.

For example, the [OSI Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) frames openness around the freedoms to use, study, modify, and share an AI system.

Other approaches place greater emphasis on the availability of training information and training code, and some also consider the availability of training data. One example is the [Open Weights definition](https://github.com/Open-Weights/Definition/blob/main/Definition.md).

The [_Opening up ChatGPT_](https://opening-up-chatgpt.github.io/) resource, maintained by Liesenfeld, Lopez, and Dingemanse, provides an updated overview of models considered open source (Liesenfeld et al., 2023).

For this chapter, we do not adopt one definition of open-source AI over another. Instead, we consider the different components of an AI system that may be relevant to understanding and reproducing it.

These components can include:

- model parameters, including weights and biases;
- model architecture;
- training and inference code;
- training methodology and configuration;
- intermediate checkpoints;
- training datasets;
- training-data composition, provenance, and preprocessing; and
- software, hardware, and computational environments.

These components can be available to different degrees. For example, a model may make its weights available while keeping its training data or training code unavailable. Having access to one component therefore does not necessarily mean that the system can be fully studied or reproduced.

### What is reproducibility?

For this chapter, we use the definition of reproducibility described by *The Turing Way*: research that can be independently recreated using the same data and code as the original work.

We also draw on the work of Gundersen, Coakley, et al. [@gundersen2022sources], which discusses different sources and forms of reproducibility in machine learning.

More specifically:

> Interpretation reproducibility does not require the reproduced experiment to have the same or similar outcome nor analysis, but requires the interpretation to be the same as the original one.
>
> -- Gundersen, Coakley, et al. (2022)

The meaning of reproducibility can vary depending on the type of research being reproduced. In AI, it can be useful to consider both whether the same analysis can be performed and whether the process used to produce a model or result can be recreated.

### How openness, open science, and reproducibility relate

Open source, open science, and reproducibility are related, but they are not interchangeable.

**Open source** concerns the freedoms to use, study, modify, and share the relevant components of a system. In AI, different definitions of open source differ in which components they consider relevant and what must be made available [@osi2024opensourceai; @openweightsdefinition].

**Open science** is broader. It includes practices that make research more accessible, transparent, and reusable. In AI research, open science practices can support the independent evaluation and reproduction of research results [@gundersen2024open].

**Reproducibility** concerns whether research results or computational processes can be independently recreated using the information and resources provided [@gundersen2022sources].

These concepts can support one another, but one does not necessarily imply the others.

An AI system may be open in some respects without providing everything needed to reproduce its training or results. For example, a model may provide access to its weights while not providing the training data or code needed to reproduce how those weights were produced.

Similarly, a research project may provide enough information to reproduce its results without satisfying a particular definition of open source.

For this chapter, we therefore do not try to establish a universal definition of what makes an AI system open source. Instead, we focus on the information and resources that can help make AI research reproducible.

### Why can reproducibility in AI be difficult?

In AI, reproducibility can be more complex because there are many moving parts that can affect the final result.

For example, models are trained on data. The data is processed and converted into a form that can be used by the model. The model is then trained using particular code, parameters, and computational resources. The resulting model can then be used to produce outputs for users.

Each of these steps can affect the final result.

Two researchers may use the same model architecture and dataset but obtain different results because they use different software versions, hardware, hyperparameters, random seeds, preprocessing methods, or training configurations.

Similarly, even when model weights are available, reproducing the process that generated those weights may require information about the training data, training code, computational environment, and training procedure.

This is why an AI system should not necessarily be considered only in terms of its final model or its weights. For reproducibility, it may be necessary to document the broader process through which the model was developed, trained, and evaluated.

In this chapter, we do not lean on either the OSI or Open Weights definition of openness. Instead, we follow *The Turing Way* philosophy of **" as closed as necessary, as open as possible."**

Regardless of which definition of openness is used, the core question for reproducibility is:

> **Can another researcher, using the same data, code, model configuration, and relevant computational environment, reproduce the reported results?**

The answer will depend on the type of AI system and the type of result being reproduced. 

However, there are some practices that can help researchers document the information needed to make reproduction possible:

- **Document everything used:** Record data sources, dataset versions, code versions, model versions, hyperparameters, software dependencies, and computational requirements. Where possible, also document preprocessing steps, evaluation procedures, and the hardware used.
  
- **Set and document random seeds:** Use fixed random seeds where appropriate to reduce variability between runs. A fixed seed does not guarantee bit-for-bit reproducibility across different software, hardware, or computational environments. However, recording the seed alongside other configuration information can help researchers reproduce the conditions of an experiment.
  
- **Log all results:** Log successful and unsuccessful experiments. Recording failed approaches can prevent duplicated effort and provide a record of decisions made during development. Where possible, record the configuration associated with each result so that experiments can be traced back to the conditions under which they were performed.
  
- **Work with a checklist:** When working on an AI system, it can be easy to forget important steps or dependencies. A simple checklist can help identify what has been documented and what is still missing. The checklist should be adapted to the type of AI system and research being conducted.

  At a minimum, consider documenting:
  
  - the data and its provenance;
  - data preprocessing and transformations;
  - model architecture and parameters;
  - training and evaluation code;
  - hyperparameters and configuration;
  - random seeds;
  - software dependencies and versions;
  - hardware and computational environment;
  - intermediate checkpoints where relevant; and
  - evaluation procedures and results.

Taken together, these practices can help make AI research easier to understand, verify, reproduce, and build upon.

As referenced previously, the [*Opening up ChatGPT*](https://opening-up-chatgpt.github.io/) resource, maintained by Liesenfeld, Lopez, and Dingemanse, provides an updated overview of models considered open source [@liesenfeld2023opening].

### References

1. Gundersen, O. E., & Kjensmo, S. (2018). State of the art: Reproducibility in artificial intelligence. In *Proceedings of the AAAI Conference on Artificial Intelligence*, 32(1). [https://doi.org/10.1609/aaai.v32i1.11503](https://doi.org/10.1609/aaai.v32i1.11503)

1. Gundersen, O. E., Coakley, K., & others. (2022). *Sources of irreproducibility in machine learning*. [Add the DOI or URL used in your existing `@gundersen2022sources` reference.]

1. Liesenfeld, A., Lopez, A., & Dingemanse, M. (2023). Opening up ChatGPT: Tracking openness, transparency, and accountability in instruction-tuned text generators. In *CUI '23: Proceedings of the 5th International Conference on Conversational User Interfaces*. 10.1145/3571884.3604316

1. Open Source Initiative. (2024). *The Open Source AI Definition 1.0*. [https://opensource.org/ai/open-source-ai-definition](https://opensource.org/ai/open-source-ai-definition)

1. Organisation for Economic Co-operation and Development (OECD). (2024). *Explanatory memorandum on the updated OECD definition of an AI system*. [https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_3c815e51/623da898-en.pdf](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_3c815e51/623da898-en.pdf)

1. The Turing Way Community. (2026). *The Turing Way: A handbook for reproducible, ethical and collaborative research*. [https://book.the-turing-way.org/](https://book.the-turing-way.org/)
