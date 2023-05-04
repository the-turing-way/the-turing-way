(rr-licensing-ml)=
# Machine Learning Model Licenses

Like a software license, a Machine Learning (ML) model license governs the use, redistribution of the model and/or algorithm, and distribution of any derivatives of it.
However, there are other components to an AI system, such as {ref}`data<rr-licensing-data>`, 
{ref}`source code<rr-licensing-software>`, or applications, which may have their own separate licenses.
ML model licenses may restrict the use of the model for specific scenarios for which, due to the technical capabilities and limitations  of the model informed by its model card, the licensor is not comfortable that the model is used.

While many ML models may utilise open software licensing (for example MIT, Apache 2.0), 
there are a number of ML model-specific licenses that may be developed for a specific model (for example [OPT-175B license](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/MODEL_LICENSE.md), [BigScience BLOOM RAIL v1.0 License](https://https://bigscience.huggingface.co/blog/the-bigscience-rail-license)), 
company (for example [Microsoft Data Use Agreement for Open AI Model Development](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4Rjfq)), or series of models (for example [BigScience OpenRAIL-M](https://www.licenses.ai/blog/2022/8/26/bigscience-open-rail-m-license) (Responsible AI License)). 

In summary, the growing list of ML licenses reflects the understanding that the ML model is distinct from the source code, and thus in need of new licensing options. 

## Reproduction and propagation of ML models

Many similar or related versions of a model may exist, whether it is the evolution of a model family (for example [GPT-2](https://github.com/openai/gpt-2) and [GPT-3](https://github.com/openai/gpt-3)) or implementations of the model in different languages and frameworks (for example pix2pix in [Pytorch](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) and [Tensorflow](https://github.com/affinelayer/pix2pix-tensorflow)).
This phenomenon is characteristic of modern ML models, where an active community creates many new versions based on an original ML model that may enable greater use for different user groups.
Each version may have its own license, though some model developers are now requiring all downstream models (derived models from the original model) to at least have the same use restrictions as included in the original license. 
In the most extreme cases, a model developer may choose to grant the license exclusively to a single entity or open every aspect of the model to the public, by means of an open license, such as an Apache 2.0 or MIT open source licenses. 

## Open & Responsible ML Licenses

The "open source" approach to collaborative software development has permeated and influenced AI development and licensing practices.
It is a common practice of ML developers to use open source licenses to release their ML models.
This is due to the fact that open source licenses have become a standard practice when it comes to the sharing of artefacts in the entire ICT space (for example, software; datasets; models; apps).
ML developers might colloquially refer to "open sourcing a model" when they make its weights (trained model parameters) available by attaching an official open source license, or any other open software or content license such as Creative Commons. 

However, open source licenses do not take the technical nature and capabilities of the ML model as a different artefact to software/source code into account, and are therefore ill-adapted to enabling a more responsible use of ML models.

In order to balance the principles from open source with a growing demand of responsible ML development, use, and access, a new branch of ML licenses called Responsible AI Licenses (RAIL) emerged in 2019 with the [RAIL Initiative](https://www.licenses.ai/). 
Research initiatives such as [BigScience](https://bigscience.huggingface.co/) and companies such as [Hugging Face](https://huggingface.co/blog/open_rail) have decided to join efforts and push towards this direction along with the RAIL Initiative.

Responsible AI licenses target specific concerns stemming from specific uses of an AI artefact by enacting use restrictions to mitigate potential harms associated with the use of AI-related products and services or component parts such as data, model, code, or applications. 
The integration of use restrictions clauses into open AI licenses brings up the ability to better control the use of AI artifacts and the capacity of enforcement to the licensor of the ML model, standing up for a responsible use of the released AI artifact, in case a misuse of the model is identified.
Licensing enforcement mechanisms are an active area of development, and work by organisations like [Free Software Foundation](https://www.fsf.org/) and [Creative Commons](https://creativecommons.org/license-enforcement/enforcement-principles/) provide direction for structuring enforcement guidelines upon the discovery of a license violation.

While RAILs are the first step towards enabling ethics-informed use restrictions, OpenRAILs take this a step further and seek to strike a balance between open access and responsible use of the licensed AI artefact.
For further information on the implementation of a Responsible AI License, check the material jointly provided by [BigScience and RAIL Initiative](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses).

### Choosing an OpenRAIL

```{figure} ../../figures/rail-diagram.*
---
name: rail-diagram
alt: An illustration depicting a flow chart diagram for a decision making process on which OpenRAIL is the best choice for an ML project.
---
The OpenRAIL flow chart aids the selection and naming of a license for an ML project. Danish Contractor, Carlos Muñoz Ferrandis, Jenny Lee, & Daniel Mcduff. (2022, August).
```

### Example: OpenRAIL-M

The 2 main features of an OpenRAIL license are:

- Open: these licenses allow royalty free access and flexible downstream use and re-distribution of the licensed material, and distribution of any derivatives of it.
- Responsible: OpenRAIL licenses embed a specific set of restrictions for the use of the licensed AI artifact in identified critical scenarios (e.g. illegal or discriminatory content, misinformation).
  To see examples of critical scenarios, see attachment A in the BigScience license in the table below.
  Use restrictions are informed by an evidence-based approach to ML development and use limitations which forces to draw a line between promoting wide access and use of ML against potential social costs stemming from harmful uses of the openly licensed AI artifact.
  Therefore, while benefiting from open access to the ML model, the user will not be able to use the model for the specified restricted scenarios.

OpenRAILs require downstream adoption of at least the same use restrictions by derivatives of the AI artifact, as a means to dissuade users of derivatives of the AI artifact from misuse.
OpenRAILs are a vehicle towards the consolidation of an informed and respectful culture of sharing AI artifacts acknowledging their limitations and the values held by the licensors of the model.

In practical terms, every RAIL or OpenRAIL license requires that the set of use restrictions included in it must also be included in subsequent re-distributions or derivative versions of the ML model.
For instance, all BLOOM RAIL, BigScience OpenRAIL-M, and CreativeML OpenRAIL-M include the same provisions 4.a. and 5 which require the licensee when distributing the model or derivatives of it to include -at minimum- the same use restrictions. 

It is important to acknowledge that RAILs and OpenRAILs should not be conceived as instruments which, due to excessive use restrictions, could hinder incremental innovation in the AI space.
Consequently, as BigScience clarified in its BLOOM RAIL [FAQ](https://bigscience.huggingface.co/blog/the-bigscience-rail-license), the licensor can always at their own discretion make an exception and open some of the restrictions when a licensee justifies that the model has been expressly modified to avoid any concern and/or harm for the specific case at sight. 

## Examples of ML models and their licenses

The table below showcases several well-known examples of ML models in the fields of NLP, vision, and multimodal generatives.
The aim of it is to inform the reader on the licensing options chosen by each of the projects which sometimes differ from one another.
Licensing differences might stem from business models, research purposes or ethics-informed community values.
Each license carries licensor's values and a message from the former to potential users on how the model should be used.

| Model | Model License | Description | Link to License |
| -------- | -------- | -------- | -------- |
| GPT-2  | MIT License + generated output disclaimer | Permissive open source license | [Link to license](https://github.com/openai/gpt-2/blob/master/LICENSE)  |
| GPT-3  | Exclusive | Licensed to Microsoft | [News Article](https://openai.com/blog/openai-licenses-gpt-3-technology-to-microsoft/)    |
| YOLO     | YOLO License    | Public domain license  | [Link to license](https://github.com/pjreddie/darknet/blob/master/LICENSE) |
| DALLE-pytorch     | MIT License | Permissive open source license  | [Link to license](https://github.com/lucidrains/DALLE-pytorch/blob/main/LICENSE)     |
| Stable Diffusion | CreativeML Open RAIL-M | Open & Responsible AI License (RAIL) created by Stability.ai and adapted from the BLOOM RAIL license, including use restrictions (see attachment A) | [Link to license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) |
| OPT | OPT-175B License | Meta restrictive license enabling use of the model weights for research purposes while establishing a set of use restrictions, which could be considered a RAIL | [Link to license](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/MODEL_LICENSE.md) |
| BigScience | BigScience OpenRAIL-M | Open & Responsible AI License (RAIL) created by BigScience and adapted from the BLOOM RAIL license, including use restrictions (see attachment A) | [Link to license](https://huggingface.co/spaces/bigscience/license) |
| Tsinghua University | GLM-130B license | Restrictive license enabling use of the model weights for research purposes | [Link to license](https://github.com/THUDM/GLM-130B/blob/main/MODEL_LICENSE) |
