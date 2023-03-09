(ch-translation-workflow)=

# Workflow for translation within TTW
By translation workflow, we do not refer only to the phases that contributors should follow during the translation process.
Instead, we refer to a set of key and optional aspects that can lead to a successful and sustainable translation project.
The translation process can be grouped into four distinct stages.
Let's jump in each of them!


1. Before translation
2. Starting a new language translation
3. During translation
4. After translation

## Before translation

Building a new translation project is an exciting way to contribute toward a global _The Turing Way_.
Before starting a translation project, it remains relevant to reflect upon the following questions:
- What are your expectations with translated content?
- What are the expectations of the target audience?
- If you are using right-to-left (RTL) languages (for example, Arabic, Urdu), does your localisation platform support RTL languages?
- Do you see the target language in the localisation platform?
    - Check out the existing languages being translated.
    - Reach out to existing translation teams and ask them for good practices.

## Starting a new language translation

When starting a new language translation, there are several aspects to consider in terms of the workflow and translation guidelines.

### Current workflow

The current workflow for all languages is using Crowdin from [a fork](https://github.com/TWTranslation/the-turing-way) that is temporarily located under [a GitHub organisation](https://github.com/TWTranslation) specifically created to host translated versions of _The Turing Way_.
This fork is kept updated with the original repository automatically, and Crowdin performs automatic machine translations that need review and approval before being accepted as definitive versions.
The deployment of these translated versions is work in progress, and some parts of this workflow may change in the future, but for now, feel free to contact anyone on the `#translation` channel of the _The Turing Way_ Slack.


### Define translation guidelines

It is key to set translation norms for each language.
These norms will guide newcomers on how to translate and review translations.
For instance, we strongly suggest setting a glossary through the localisation platform.
The Carpentries [Glosario](https://glosario.carpentries.org/) and the [Localization Lab glossary](https://www.localizationlab.org/glossaries) are two good examples of such glossaries.
The decisions at this stage include deciding what terms not to translate, deciding on the translation of some terms, and the governance, for example, determining who is responsible for each section.

We also suggest setting language-specific guidelines to use inclusive language.
For example, the book [Teaching Tech Together](https://teachtogether.tech/) was collaboratively translated to Spanish.
The team defined their guidelines to account for regional differences and avoid gendered and other non-inclusive expressions.
They describe the whole process (in Spanish) [here](https://teachtogether.tech/es/index.html#s:traduccion) and an adaptation of their guidelines to English can be found [here](https://github.com/gvwilson/teachtogether.tech#translations).
Document the translation guidelines for your selected language to be discussed and updated by the rest of the team.
They may be useful for future teams translating other projects.

We suggest having roles of project members, which include manager, translator, and proofreader.
- **Manager** – has similar rights as a project owner except for the ability to manage some of the owner's Resources (for instance,, configuring MT engines, advanced workflows, and more.) and delete projects.
- **Proofreader** – can translate and approve strings.
Unlike the manager, the Proofreader doesn't have access to project settings.
- **Translator** – can translate strings and vote for translations added by other members.

In order to facilitate and speed up the translation of a new language, we recommend sharing translation memory with other projects so similar strings can be translated automatically.
The Turing Way project is linked with the translation memory of a previous version of the Turing Way translated in Transifex and another translation for [Open Life Science](https://openlifesci.org/) materials in OLS.

It is key to set translation norms. These norms will guide newcomers on how to translate and review in the translation platform. For instance, we strongly suggest setting a [glossary] through the localisation platform.

```{figure} ../../figures/translation-memory.jpeg
---
name: translation-memory
width: 90%
alt: An illustration showing how translation memory can speed up the crowdsourcing of new projects.
---
Illustration of translation as a way to reach global accessibility. _The Turing Way_ project illustration by Scriberia.
Used under a CC-BY 4.0 licence.
DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807)
```  


## Create a dedicated Slack channel and co-working calls

We recommend creating a dedicated Slack channel for the language you are translating within the [_The Turing Way_ slack](https://theturingway.slack.com).
This space will allow you to chat with interested parties in your own language.
You can join the `#translation` channel in [_The Turing Way_ slack](https://theturingway.slack.com).

We also suggest defining co-working calls to check progress on the translation.
These sessions should be open to anyone interested in participating.
You can also work on the translation in the co-working calls of The Turing Way project.
You can find this activity in [_The Turing Way_ calendar](https://calendar.google.com/calendar?cid=dGhldHVyaW5nd2F5QGdtYWlsLmNvbQ).
Please note that these calls are in English but we are happy to facilitate other co-working calls in different languages.

## Asynchronous translation

Everyone interested in participating in a translation effort should be able to work asynchronously, have this in mind when writing the translation norms and any other documentation for your language.
We have set up a public page for _The Turing Way_ in [Crowdin](https://turingway.crowdin.com/turing-way) with a README file summarising some of the translation guidelines.

# During translation

## Before you start translating

Localisation platforms integrate different tools and formats for assisting the translation process.
For instance, [Transifex](https://www.transifex.com/) includes the target text blocks to be translated on the left and a translation box on the right. You can select with the cursor which block to translate. We recommend that you look at a translated chapter or section before you start translating to familiarise yourself with the process and the translation style.

### Machine translation / Translation tools

The translation process can be assisted by machine translation.
Localisation platforms such as [Crowdin](https://crowdin.com/?gclid=CjwKCAiAvriMBhAuEiwA8Cs5ldEGwrOeDJtdY2kneF6vBXx8hYiXD1oJPcWB1SO0VBSTuz60AaDYUhoCj_8QAvD_BwE) are integrated with well-known machine translation providers, including Google and Microsoft.
In contrast, for [Transifex](https://www.transifex.com/), this process is performed outside the platform.
Different languages may work better with a specific machine translation engine. For example, Spanish works very well with  [DeepL](https://www.deepl.com/) as a translation tool but other languages (for example, Arabic) don't. DeepL tool recommends a series of synonyms when you click on the translated text. This can be useful, especially with long texts.

### Read the translation guidelines

These guidelines are essential to harmonise and standardise translations. Make sure you read them before you start translating for the first time. Translation consistency is crucial and can be made easier when TMS is used. As soon as you start translating your project, machine learning algorithms engage, and the system shows previous translations for the source words and how often they were used in the project[^1]. For example, in Crowdin, you can hover over the source words underlined with the light dashed line to see the previous translations formed by the translation consistency feature. You can also search earlier translations for specific source words using the Search TM tab.

```{figure} ../../figures/translation_consistency_previous_translations_editor.png
---
name: translation_consistency_previous_translations_editor
width: 90%
alt: Checking consistency in Crowdin by hovering over the source words underlined and a list of previous translations formed by the translation consistency feature will show.
---
```  

In each co-working or external session, prioritise those chapters that are outdated or close to completion. Check out our [guidlines](ch-translation-getting-started) for a list of the priority list.

# After translation

As the Turing Way content grows, the translated content does too. We strongly encourage monitoring the new content. While updates of the translated content might change according to the availability of resources, it is a good practice to:

* Set periodical reviews
* Improve the translation
* Update glossaries

If you have any recommendations for improving the translation guidelines or setting up language-specific rules, contact [the translation and localisation team](https://github.com/alan-turing-institute/the-turing-way/blob/main/ways_of_working.md).
We are very eager to improve the workflow and make the _The Turing Way_ a global project accessible to the wider community.

[^1]: This image and description are borrowed directly from [Crowdin docs](https://support.crowdin.com/translation-consistency/).
