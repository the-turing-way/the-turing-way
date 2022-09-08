(rr-licensing-ml)=
# Machine Learning Model Licenses

Like a software license, a Machine Learning (ML) model license governs the use or redistribution of 
the model or algorithm. However, there are other components to an AI system, which may have their own separate licenses, 
such as [data](https://the-turing-way.netlify.app/reproducible-research/licensing/licensing-data.html), 
[software](https://the-turing-way.netlify.app/reproducible-research/licensing/licensing-software.html), 
or model weights. ML model licenses may restrict or allocate liability associated using the model, component parts, 
and outputs. 

While many ML models may utilise traditional software licensing models (e.g. MIT, Apache 2.0), 
there are a number of ML model-specific licenses that may be developed for a specific model (e.g. OPT-175B license, BigScience RAIL License), 
company (e.g. Microsoft Open AI Model Development agreement), or series of models (e.g. Open RAIL). 
In the most extreme cases, a model developer may choose to grant the license exclusively to a single entity or open every aspect of the model 
to the public domain. 

In summary, the growing list of ML licenses reflects an understanding that ML models and corresponding artefacts are distinct from the code, 
and thus in need of new licensing options. Additionally, due the nature of potential social harms that ML models may enable, 
developers have found value in using ML model licenses as a tool to articulate their intentions for the model and how it is used, 
or as a way to embed community values into the resource.

## Licensing for derived ML models

Many similar or related versions of a model may exist, whether it is the evolution of a model family (e.g. [GPT-2](https://github.com/openai/gpt-2) and [GPT-3](https://github.com/openai/gpt-3)) or implementations of the model in different languages and frameworks (e.g. pix2pix in [Pytorch](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) and [Tensorflow](https://github.com/affinelayer/pix2pix-tensorflow)). This phenomenon is characteristic of modern ML models, where an active community creates many new versions based on an original ML model that may enable greater use for different user groups.

For these model derivatives, licensing can also play an important role. In some cases, the original versions of the models may not be open source, but versions created by the community may be made available under open licenses on other platforms such as Github or HuggingFace. It may also be that each version has its own license, but like the "copyleft" license in the software world, some ML model developers are now requiring all downstream models to at least have the same base license as the original.

## Limitations of existing open software licenses for ML

### Responsible AI Licenses (RAIL)

### Open RAIL

## Examples of ML models and their licenses

### Natural Language Processing

| Model | Model License | Description | Link to License |
| -------- | -------- | -------- | -------- |
| GPT-2  | MIT | Modified MIT License with Software Copyright to OpenAI | https://github.com/openai/gpt-2/blob/master/LICENSE    |
| GPT-3  | Exclusive | Licensed to Microsoft | https://openai.com/blog/openai-licenses-gpt-3-technology-to-microsoft/    |
| OPT | OPT-175B License | Meta license for access to OPT with use restrictions for commercial, illegal, military, surveillance, and biometric processing applications | https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/MODEL_LICENSE.md |
| BigScience | BigScience RAIL License | Responsible AI License (RAIL) created by BigScience for the BLOOM models and tools with use-based restrictions for illegal, harmful, discriminatory, etc. applications | https://huggingface.co/spaces/bigscience/license |

### Computer Vision
| Model | Model License | Description | Link to License |
| -------- | -------- | -------- | -------- |
| OpenCV 4.5+  | Apache 2.0 | Older versions of OpenCV are under the 3-clause BSD License with copyrights to 7 different organisations | https://opencv.org/license/  |
| YOLO     | N/A    | Public domain but no formal license  | https://github.com/pjreddie/darknet/blob/master/LICENSE |
| DALLE-pytorch     | MIT License | Pytorch implementation of DALLE created by individual researcher  | https://github.com/lucidrains/DALLE-pytorch/blob/main/LICENSE     |
| Stable Diffusion | CreativeML Open RAIL-M | Use-based restrictions on generative model against illegal, harmful, misinformation, harassment, medical advice, and law enforcement-related tasks (see attachment A) | https://huggingface.co/spaces/CompVis/stable-diffusion-license |


