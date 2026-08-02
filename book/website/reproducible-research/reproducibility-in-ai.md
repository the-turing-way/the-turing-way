---
abbreviations:
  OSI: Open Source Initiative (https://opensource.org/) 
---
# Reproducibility in AI

At the time of this writing, AI has become a large part of human life and part of our daily processes.
Active and inactive users alike have to interact with AI, either directly or indirectly.
For researchers, the question arises of how this applies to science and how we can create AI systems that carry on the principle of reproducibility.
The topic of reproducibility in AI is important, as it helps us build on systems and research that can be reproduced and studied by researchers.

## Definitions

### What are AI systems

There are two definitions to be highlighted in this article.

> Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making.
> It is a field of research in engineering, mathematics and computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals 
>
> -- [Wikipedia](https://en.wikipedia.org/wiki/Artificial_intelligence#).

**Organisation for Economic Co-operation and Development (OECD)**
> An AI system is a machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.
> Different AI systems vary in their levels of autonomy and adaptiveness after deployment. ([OECD, Artificial Intelligence Papers, March 2024](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_3c815e51/623da898-en.pdf))

For the sake of this chapter, we lean more towards the OECD definition.

When discussing reproducibility, although it is not always the same definition as "open," there is a tendency to have open principles, as they sometimes overlap.
In that regard, we define AI with respect to Open Source, using the OSI definition.

> In this case, a 'system' encompasses both a fully functional structure and its discrete structural elements.
> To be considered Open Source, the requirements are the same, whether applied to a system, a model, weights and parameters, or other structural elements.
>
> An Open Source AI is an AI system made available under terms and in a way that grant the freedoms to:
> - Use the system for any purpose and without having to ask for permission.
> - Study how the system works and inspect its components.
> - Modify the system for any purpose, including to change its output.
> - Share the system for others to use with or without modifications, for any purpose.
>
> -- [OSI open source AI definition](https://opensource.org/ai/open-source-ai-definition)

Finally, we define what reproducibility is according to The Turing Way, and narrow it down with the definition by Gundersen, Coakley, et al. (2023).

According to The Turing Way, reproducible research is work that can be independently recreated from the same data and the same code that the original team used.
More specifically:

> Interpretation reproducibility does not require the reproduced experiment to have the same or similar outcome nor analysis, but requires the interpretation to be the same as the original one.
>
> — Gundersen, Coakley, et al. (2023)

## Why is reproducibility important

We write about this extensively in the [Added Advantages](https://book.the-turing-way.org/reproducible-research/overview/overview-benefit/) chapter of _The Turing Way_ book. 

In summary: open data and code, ease of access, and review.

## Reproducibility in AI

In Artificial Intelligence, reproducibility takes on a slightly more complex approach, as there are a lot more moving parts that cannot be directly affected by human input.
For example, models are trained on data, and this data is converted to numbers, which the system matches to each other, producing responses for users.

The fact that there are some parts of the process that cannot be easily interpreted by humans gives credence to some of the debate on how much of an AI system should be open.
In this book, we won't lean on either side of the principle, but stick to The Turing Way philosophy of "as closed as necessary, as open as possible."

To aid this, here are some steps to factor in when working on an AI system:

- **Document everything used**: data sources, code versions, hyperparameters, and computational requirements.
- **Set a random seed**: let your computer know to begin evaluations from the same point every time, to enable some level of predictability, so results are as near as possible to the original result.
- **Log all results**: the best way to avoid duplicating efforts is to know what didn't work and why it didn't work.
  All results should be logged, both positive and negative.
- **Work with a checklist**: when working, it can be easy to forget some of the important steps.
  Having a simple checklist enables you to know what's missing and what's not, without a lot of mental hassle.

### A simple comparison of models and systems

| Model / system | Weights | Training code | Training data | What you can do |
|---|---|---|---|---|
| Llama (Meta) | ✅ | ❌ | ❌ | Download and run, fine-tune |
| Mistral models | ✅ | ❌ | ❌ | Download and run, fine-tune |
| Gemma (Google) | ✅ | ❌ | ❌ | Download and run, fine-tune |
| BLOOM (BigScience) | ✅ | ✅ | ✅ | Fully reproduce training |
| OLMo (AI2) | ✅ | ✅ | ✅ | Fully reproduce training |
| GPT / Claude / Gemini (hosted API) | ❌ | ❌ | ❌ | Query via API only |

*Table generated by Claude, Sonnet 5 (effort: medium).*

Most "open" models only tick the first box.
Full reproducibility needs all three.

### References

- Gundersen, O. E., Cappelen, O., Mølnå, M., & Nilsen, N. G. (2024). The unreasonable effectiveness of open science in AI: A replication study (arXiv No. 2412.17859). arXiv. https://doi.org/10.48550/arXiv.2412.17859 
- Pineau, J., Vincent-Lamarre, P., Sinha, K., Larivière, V., Beygelzimer, A., d'Alché-Buc, F., Fox, E., & Larochelle, H. (2020). Improving reproducibility in machine learning research: A report from the NeurIPS 2019 reproducibility program (arXiv No. 2003.12206). arXiv. https://doi.org/10.48550/arXiv.2003.12206
- Gundersen, O. E., Coakley, K., Kirkpatrick, C. R., & Gil, Y. (2022). Sources of irreproducibility in machine learning: A review. arXiv. https://doi.org/10.48550/arXiv.2204.07610
