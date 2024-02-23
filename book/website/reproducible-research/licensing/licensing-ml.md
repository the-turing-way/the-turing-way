(rr-licensing-ml)=
# Licensing Machine Learning models

## Legal Status of AI/ML model weights

It is an open question wether {term}`AI<Artificial Intelligence (AI)>`/{term}`ML<Machine Learning (ML)>` models weights are even copyrightable.
US copyright law specifically excludes the following from works eligible for copyright protection: "any idea, procedure, process, system, method of operation, concept, principle, or discovery, regardless of the form in which it is described, explained, illustrated, or embodied in such work."
In addition the US Copyright Office has stated that this exclusion extends to "scientific or technical methods or discoveries;" "mathematical principles;" and "formulas or algorithms."

A legal doctrine known as the [idea–expression distinction/dichotomy](https://en.wikipedia.org/wiki/Idea%E2%80%93expression_distinction) draws a distinction between an abstract idea and a specific implementation, where code authored by a human that implements an algorithm is copyrightable as a creative work of authorship but the algorithm itself is not.

It is also generally accepted in US copyright law that to be copyrightable a work must be a product of human creative authorship and not that of an automated process.

It is not obvious if model weights would be considered works of human authorship or rather the results of automated processes, as a general principle or discovery or as a specific implementation.
These questions will need to be decided on by the courts and/or legislated on before the status of model weights can be properly established.

In the absence of clarity on this point many organisations are taking the calculated risk of operating under the assumption that they are copyrightable and generally treating them similarly to datasets and/or software.
Some companies are offering legal protections for users of services based on these systems, offering to cover legal expenses arising from challenges to the copyright status of the outputs of these systems.
It is possible that some form of copyright-like protection will be explicitly extended to model weights but it's precise contours are yet to be determined.

Despite these open questions AI/ML model specific licenses are already being developed.

## Machine Learning Model Licenses

Like a software license, a Machine Learning (ML) model license governs the use, redistribution of the model and/or algorithm, and distribution of any derivatives of it.
However, there are other components to an AI system, such as {ref}`data<rr-licensing-data>`, 
{ref}`source code<rr-licensing-floss>`, or applications, which may have their own separate licenses.
ML model licenses may restrict the use of the model for specific scenarios for which, due to the technical capabilities and limitations of the model informed by its model card, the licensor is not comfortable that the model is used.

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
Licensing enforcement mechanisms are an active area of development, and work by organisations like [Free Software Foundation](https://www.fsf.org/), [The Software Freedom Law Center](https://softwarefreedom.org/), [Software Freedom Conservancy](https://sfconservancy.org/), and [Creative Commons](https://creativecommons.org/license-enforcement/enforcement-principles/) provide direction for structuring enforcement guidelines upon the discovery of a license violation.

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

(rr-licensing-ethics-copyright-responsible-rail)=
### OpenRAIL License types

These same principles developed in {ref}`'ethical source'<rr-licensing-ethical>` apply to the 'Open' variants of the licences from RAIL (Responsible AI Licences).
In that, they are attempting to place restrictions on the uses to which licensees can put the thing being licenced.
Traditional software has many of the same concerns which affect machine learning models, and indeed also often contain assets such as images which may be licenced differently from software with which they are bundled.
The primary differences being governance of data used in training the models (see: {ref}`Data Governance for the Machine Learning Pipeline<pd-dg-ml>`) and the lack of interpretability of the decisions of many ML systems, though this latter point can also be an issue for conventional systems if they are closed.
RAIL provides a succinct way of expressing licences for combined machine learning systems which include, the data on which they were trained, the software used to specify this, the model weights generated as a result and the applications which provide an interface to the resulting model.

RAIL provides these definitions of the modifiers that can be applied to their licenses:

> - **D**ata: The dataset(s) used to pretrain or train an AI Model.
> - **A**pplication/service: Any executable software code or application, including API-based remote access to software.
> - **M**odel: Machine-learning based assemblies (including checkpoints), consisting of learnt weights and parameters (including optimizer states), corresponding to the model architecture.
> - **S**ource: The source code and scripts associated with the AI system.

Therefore:

> - RAIL-D:  RAIL License includes Use Restrictions only applied to the data
> - RAIL-A:  RAIL License includes Use Restrictions only applied to the application/executable
> - RAIL-M:  RAIL License includes Use Restrictions only applied to the model
> - RAIL-S:  RAIL License includes Use Restrictions only applied to the source code

These are the restrictions placed on the licencee of a RAIL-M license:

> You agree not to use the Model or Derivatives of the Model:
>
> 	**a.** In any way that violates any applicable national, federal, state, local or international law or regulation;
>
> 	**b.** For the purpose of exploiting, harming or attempting to exploit or harm minors in any way;
>
> 	**c.** To generate or disseminate verifiably false information and/or content with the purpose of harming others;
>
> 	**d.** To generate or disseminate personal identifiable information that can be used to harm an individual;
>
> 	**e.** To generate or disseminate information and/or content (for example images, code, posts, articles), and place the information and/or content in any context (for example bot generating tweets) without expressly and intelligibly disclaiming that the information and/or content is machine generated;
>
> 	**f.** To defame, disparage or otherwise harass others;
>
> 	**g.** To impersonate or attempt to impersonate (for example deepfakes) others without their consent;
>
> 	**h.** For fully automated decision making that adversely impacts an individual’s legal rights or otherwise creates or modifies a binding, enforceable obligation;
>
> 	**i.** For any use intended to or which has the effect of discriminating against or harming individuals or groups based on online or offline social behavior or known or predicted personal or personality characteristics;
>
> 	**j.** To exploit any of the vulnerabilities of a specific group of persons based on their age, social, physical or mental characteristics, in order to materially distort the behavior of a person pertaining to that group in a manner that causes or is likely to cause that person or another person physical or psychological harm;
>
> 	**k.** For any use intended to or which has the effect of discriminating against individuals or groups based on legally protected characteristics or categories;
>
> 	**l.** To provide medical advice and medical results interpretation;
>
> 	**m.** To generate or disseminate information for the purpose to be used for administration of justice, law enforcement, immigration or asylum processes, such as predicting an individual will commit fraud/crime commitment (for example by text profiling, drawing causal relationships between assertions made in documents, indiscriminate and arbitrarily-targeted use).

RAIL-S licences carry their [Software Usage Restrictions](https://www.licenses.ai/source-code-license).

RAIL license can be used in closed applications and Open RAIL licenses are permissive with respect to the model and software but not with respect to the usage restrictions.
Note that there is not an effective equivalent to a copyleft version of the Open RAIL licences.
None of them require that the software or models contained in them also be similarly licenced in derived works, only that the usage restrictions be retained.
This could be a useful extension to these license adding an 'L' for copy**L**eft and including a clause making any software, model weights, or source code in the bundle strong copyleft.

### Example: OpenRAIL-M

The 2 main features of an OpenRAIL license are:

- Open: these licenses allow royalty free access and flexible downstream use and re-distribution of the licensed material, and distribution of any derivatives of it.
- Responsible: OpenRAIL licenses embed a specific set of restrictions for the use of the licensed AI artifact in identified critical scenarios (for example illegal or discriminatory content, misinformation).
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
