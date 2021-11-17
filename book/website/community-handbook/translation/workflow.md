## Workflow for translation within TTW

By translation workflow, we do not refer only to the phases that contributors should follow during the translation process. Instead, we refer to a set of key and optional aspects that can lead to a successful and sustainable translation project. The translation process can be grouped into four distinct stages. Let's jump in each of them!

1. Before translation
2. Starting a new language translation
3. During translation
4. After translation

### Before translation

Building a new translation project is an exciting way to contribute towards a global _The Turing Way_. Before starting a translation project, it remains relevant to reflect upon the following questions:
- Which are your expectations with translated content?
- What are the expectations of the target audience?
- Do you see the target language in the localisation platform?
    - Check out within the existing languages being translated.
    - Reach out to existing translation teams and ask them for good practices.

### Starting a new language translation

When starting a new language translation, there are several aspects to consider, apart from [setting up a project in the chosen localisator plaform]().

#### Current workflow

The current workflow for all languages is using Crowdin from a fork that is temporarily located under a GitHub organization specifically created to host translated versions of _The Turing Way_.
This fork is kept updated with the original repository and Crowdin performs automatic machine translations that need review and approval before being accepted as definitive versions.
The deployment of these translated versions is work in progress and some parts of this workflow may change in the future, but for now, feel free to contact anyone on the `#translation` channel of the _The Turing Way_ Slack.


#### Define translation guidelines

It is key to set translation norms for each language.
These norms will guide newcomers on how to translate and review in the translation platform.
For instance, we strongly suggest setting a glossary through the localisation platform.
The Carpentries [Glosario](https://glosario.carpentries.org/) and the [Localization Lab glossary](https://www.localizationlab.org/glossaries) are two good examples of such glossaries.
The decisions at this stage include deciding what terms not to translate, deciding on the translation of some terms, and the governance, for example, deciding who is responsible for each section.

We also suggest setting language-specific guidelines to use inclusive language.
For example, the book [Teaching Tech Together](https://teachtogether.tech/) was translated to Spanish in a collaborative way and they defined their guidelines to account for regional differences and to avoid gendered and other non-inclusive expressions.
They describe the whole process (in Spanish) [here](https://teachtogether.tech/es/index.html#s:traduccion) and an adaptation of their guidelines to English can be found [here](https://github.com/gvwilson/teachtogether.tech#translations).
Document the translation guidelines for your selected language to be discussed and updated by the rest of the team.


#### Create a dedicated Slack channel

We recommend you create a dedicated Slack channel for the language you are translating within the [_The Turing Way_ slack](theturingway.slack.com).
This space will allow you to bring chat with interested parties in your own language.

#### Organise co-working calls

We suggest defining co-working calls to progress on the translation.
These sessions should be open to anyone interested in participating.

You can also work on the translation in the co-working calls of The Turing Way project.
You can find this activity in [_The Turing Way_ calendar](https://calendar.google.com/calendar?cid=dGhldHVyaW5nd2F5QGdtYWlsLmNvbQ).
Please note that these calls are in English.

#### Asynchronous translation

Everyone interested in participating in a translation effort should be able to work asynchronously, have this in mind when writing the translation norms and any other documentation for your language.

### During translation

#### Before you start translating

Localisation platforms integrate different tools and formats for assisting the translation process.
For instance, [Transifex](https://www.transifex.com/) includes the target text blocks to be translated on the left and a translation box on the right.
You can select with the cursor which block to translate.

We recommend that you look at a translated chapter or section before you start translating to familiarise yourself with the process and the translation style.

#### Machine translation / Translation tools

The translation process can be assisted by machine translation.
Localisation platforms such as [Crowdin](https://crowdin.com/?gclid=CjwKCAiAvriMBhAuEiwA8Cs5ldEGwrOeDJtdY2kneF6vBXx8hYiXD1oJPcWB1SO0VBSTuz60AaDYUhoCj_8QAvD_BwE) are integrated with well-known machine translation providers, including Google and Microsoft.
In contrast, for [Transifex](https://www.transifex.com/), this process is performed outside the platform.
In this particular case, we recommend using [DeepL](https://www.deepl.com/) as a translation tool.
DeepL tool recommends a series of synonyms when you click on the translated text.
This can be useful, especially with long texts.

#### Read the translation guidelines

These guidelines are essential to harmonise and standardise translations.
Make sure you read them before you start translating for the first time.

#### Priority list of chapters to translate

In each co-working or external session, prioritise those chapters that are outdated or close to completion.

### After translation

As the Turing Way content grows, the translated content does too.
We strongly encourage monitoring the new content.
While updates of the translated content might change according to the availability of resources, it is a good practice to:

* Set periodical reviews
* Improve the translation
* Update glossaries
