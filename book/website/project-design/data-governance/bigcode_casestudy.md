(pd-dg-bigcode)=

# BigCode Data Governance Case Study

```{admonition} Info
:class: info
This case study was adapted from the [BigCode Governance card](https://huggingface.co/datasets/bigcode/governance-card) in May 2023.
Learn more about tools and best practices for data governance activities in the {ref}`Data Governance for the Machine Learning Pipeline <pd-dg-ml>` chapter.
```
 
[BigCode](https://www.bigcode-project.org/) is an open scientific collaboration working on the responsible development and use of large language models (LLM) for code, aiming to empower the machine learning and open source communities through open governance.
Code LLMs enable the completion and synthesis of code, both from other code snippets and natural language descriptions, and can be used across a wide range of domains, tasks, and programming languages. 
These models can, for example, assist professionals and hobbyists with building new LLM applications.
As part of BigCode, the team created the [StarCoder and StarCoderBase Large Language Models for Code](https://huggingface.co/blog/starcoder). 

## Data Collection and Management Plan

### Overview 
The primary training dataset used for the BigCode project is The Stack, which was obtained by gathering public code files, issues, and commits from GitHub. 
For more information on The Stack dataset, visit [this page](https://huggingface.co/datasets/bigcode/the-stack) to request access and view the dataset card.
To collect Github repositories, they first extracted a list of repositories from [GHArchive](https://www.gharchive.org/) and subsequently cloned all of them using a large CPU cluster. 
They also used the data from GHArchive to extract the Github issues. 
The git commits were gathered from a public BigQuery service. 
Additionally, they collected a dataset of annotations of several kinds of private information on a subset of The Stack to support our privacy risk mitigation efforts.

The legal basis for data collection under fair use and with regards to GDPR and the corresponding case law are still evolving. 
In this context, the data collection and data management plans were carefully crafted with support from leading experts in the open source and legal tech community that participated in the BigCode Legal, Ethics, Governance Working Group in a best-effort approach to reflect current understandings of legal requirements for data collection and management.

The following sections will dive into the details of how the team approached key data governance activities like data collection, data management & opt-out, and data processing.

### Data Collection

The StarCoder model was trained on The Stack v1.2, which exclusively contains 6.4TB of permissively licensed data from GitHub repositories, processed from an original source dataset of 102TB. 
Selecting repositories based on licenses is only the first step, however, so this approach is complemented by also giving repository owners the ability to opt out of having their repositories included in The Stack, described further in the Data Management & Opt-out section.
- **Data selection**: One of the goals of BigCode is to give developers agency over their source code and let them decide whether or not it can be used to develop and evaluate LLMs.
  Software developers typically rely on licenses to express how they want their work to be re-used.
  In particular, developers who choose Open Source licenses often do so because they want their code to be broadly re-used.
  This motivated us to start by selecting data from repositories that met the following criteria:
    - The repository has an open source license attached - open source, while chosen for very different reasons by different people, typically indicates a willingness to have one's work reused or adapted
    - The license does not have an attribution clause - attribution is a difficult technical problem for code LLMs.
      Since they cannot guarantee that the model will be used in a way that attributes its generations to specific training data in a way that satisfies the intent of the licensor, they chose to only keep licenses without an attribution clause
- **Data updates**: For as long as the BigCode team is maintaining The Stack dataset, they will provide regular updates to the dataset to remove data that has been flagged since the last version.
  This includes data that has been opted out, and data that was flagged as containing PII, malicious code or using a non-permissive license since the previous release.
  The current plan is to update the dataset every 3 months, although the schedule may change based on the volume of requests received.
  If the team is no longer in a position to continue maintaining the dataset, they plan to stop distributing it in its current format and update its terms of use to limit its range of applications further.

### Data Management & Opt-Out

#### Data Access
- **What data can be accessed**: the 6.4TB of processed data can be accessed through the Hugging Face Hub, while the original 102TB are only accessible to the stewards of the project for the purposes of enabling the research and to support future internal and external requirements that may arise, for example to search the full dataset to recall licenses, determine code provenance, and attribution.
- **Conditions for data accesss**: users are able to inspect the dataset via the [Dataset Card](https://huggingface.co/datasets/bigcode/the-stack#dataset-card-for-the-stack), but are required to agree to the Terms of Use for The Stack before being able to download it.
  This includes the requirements to:
    1. abide by the terms of original source code licenses, including attribution clauses when required (The Stack provides provenance information for each data point)
    2. agree to update copies of The Stack to the most recent usable version specified [here](https://huggingface.co/datasets/bigcode/the-stack/discussions/7)
    3. include the Terms of Use and require users to agree to it if a copy is to be hosted, shared, or otherwise provided.
    As of May 3, 2023, The Stack had been downloaded 50,200 times

#### Data Opt-Out
- **How a data subject request that their data be removed:** Developers that find that their data is in The Stack by using the [Am I In the Stack? website](https://huggingface.co/spaces/bigcode/in-the-stack) can use a custom link that automatically generates an issue in the BigCode opt-out repository for an official opt-out request.
  You can choose which repos you’d like to remove, as well as your commits and issues. After submitting the issue, your request is added to the queue for removal from all future iterations of The Stack.
  Additionally, anyone who is concerned about specific data they have encountered in The Stack, for example relating to PII, malicious code, or code that has an incorrect license or attribution can email contact@bigcode-project.org.
At the time of the data processing for the StarCoder model training, 44 people had opted out of The Stack and associated repositories were removed.

### Data Processing

One significant concern with respect to privacy was the risk that the code LLM may generate private information found in its training data, including private tokens or passwords matched with identifiers or email addresses. 
Additionally, while users can (and have) requested that data be removed from The Stack dataset because it contains personal data, removing specific information from trained model weights after the fact remains an open technical challenge. 
In order to minimize this risk, they chose to apply automated PII redaction at the pre-processing stage during training.

The PII redaction process consisted of the following steps:
- **Creating an annotated dataset for PII:** they found that neither regular expression-based approaches nor existing commercial software for PII detection met our performance requirements.
  In doing so, they aimed to balance the constraints of costs (fair compensation), time (the timing and time to complete the work was on the critical path for the project), and quality (to ensure that PII Detection Model training was not impacted). 
- **Collaborating with crowd-workers in a responsible way:** While traditional data annotation services using salaried employees were considered, they decided to work with crowd-workers through Toloka after reviewing several service providers and their compensation practices - and finding that most would not provide sufficient transparency and guarantees about worker compensation.
  We selected pay and eligible countries of crowd-workers to ensure that:
    - Absolute hourly wage was always higher than the US federal minimum wage ($7.30)
    - Hourly wage was equivalent to the highest state minimum wage in the US in terms of purchasing power parity ($16.50 at the time of writing)
- **Training a PII detection model:** We engaged 1,399 crowd-workers across 35 countries in annotating a diverse dataset for PII in source code.
  Our PII detection model, trained on 22,950 secrets, achieves 90% F1 score surpassing regex-based tools, especially for secret keys.
  The PII annotations are available to approved individuals, and researchers and developers that are granted access are expected to uphold ethical standards and data protection measures.
  By making it accessible, our aim is to encourage further research and development of PII redaction technology.

Learn more about the PII redaction process through this [blog post from Toloka](https://toloka.ai/blog/bigcode-project/).

## Acknowledgments

This case study is based on the BigCode Governance card, thanks to the efforts of the [hundreds of BigCode participants](https://huggingface.co/bigcode), a living document that will evolve over time with the BigCode project. 
Please leave any comments in the [HuggingFace Community space](https://huggingface.co/datasets/bigcode/governance-card/discussions) to ask a question or start a conversation about BigCode project governance. 
