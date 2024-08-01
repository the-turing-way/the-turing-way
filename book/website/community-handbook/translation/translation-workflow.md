(ch-translation-welcome)=
# Welcome to the Translation and Localisation Team of _The Turing Way_!

We are members of _The Turing Way_ community with different motivations to localise the content to different languages.
Feel free to join the `#translation` channel in [_The Turing Way_ slack](https://theturingway.slack.com).
You will also have to create a Crowdin account but more on that {ref}`in the next section<ch-translation-localisation-journey>`

You can find these activities in [_The Turing Way_ calendar](https://calendar.google.com/calendar?cid=dGhldHVyaW5nd2F5QGdtYWlsLmNvbQ).
Please note that these calls are in English but we are happy to facilitate other co-working calls in different languages.
The deployment of these translated versions is work in progress, and some parts of this workflow may change in the future. Feel free to contact anyone on the `#translation` channel of the _The Turing Way_ Slack if you have any ideas and feedback to help our work.

## Structure of the Meetings
### Co-working Calls & Onboarding Calls
- **Frequency**: Once every month
- **Chair**: Selected from leads
- **Membership**: Open to anyone interested in localisation
- **Objectives**:
  - A facilitator assists with onboarding in the breakout room.
  - It is an 'Ask Me Anything' call for any questions.
  - The main room is dedicated to working on milestones for the localisation work.
  - Tasks are prepared in advance (in Crowdin Kanban) to support new members.
### Community Meeting
- **Frequency**: This is integrated into the TTW Collaboration Café. 
- **Chair**: Selected from leads
- **Membership**: Open to anyone interested in localisation.
- **Objectives**: A forum to discuss deliverables/outputs (e.g. toolkits, glossary, blog post, ...etc), consult the community, and seek feedback.
### Localisaton Lead Team Meeting
- **Frequency**: Bi-monthly
- **Membership**: Exclusive to localisation leads.
- **Objectives**: To review milestones and decisions related to localisation.
### Language Leads Meeting
- **Frequency**: Every four months
- **Membership**: Language leads plus localisation leads.
- **Objectives**: To evaluate the work of each language, discuss potential plans, questions, or support needs.
### Language Localisation Sprints
- **Frequency**: This is organised by each language lead.
- **Chair**: Language lead.
- **Membership**: All language contributors.
- **Objectives**: Language leads, with support from localisation leads, organise localisation sprints. These can occur during a Book Dash or independently.

## Asynchronous translation

Everyone interested in participating in a translation effort should be able to work asynchronously, so don't worry if you cannot join the fortnightly calls. More info can be found in the next chapter about {ref}`our localisation workflow<ch-translation-localisation-journey>`.

## Join or create a language team

Before starting a translation project, check out the existing languages being translated.
Is the language that interests you in the localisation platform? If it isn't, reach out to the team to create a new translation team.
You can see the list of language teams and their managers in the project's [Readme](https://turingway.crowdin.com/turing-way#readme/)
If the language team already exists reach out to the team so you can join them.

When starting a new language translation, there are several aspects to consider in terms of the workflow and translation guidelines.
The decisions at this stage include deciding what terms not to translate, deciding on the translation of some terms, and the governance of the team, to determine who is responsible for each section.

### Define translation guidelines

It is key to set translation guidelines for each language.
These guidelines are essential to harmonise and standardise translations.
They will guide newcomers on how to translate and review translations and may be useful for future teams translating other projects.
These language-specific guidelines should include the use of inclusive language.

For example, the book [Teaching Tech Together](https://teachtogether.tech/) was collaboratively translated to Spanish.
The team defined their guidelines to account for regional differences and avoid gendered and other non-inclusive expressions.
They describe the whole process (in Spanish) [here](https://teachtogether.tech/es/index.html#s:traduccion) and an adaptation of their guidelines to English can be found [here](https://github.com/gvwilson/teachtogether.tech#translations).

Document the translation guidelines for your selected language to be discussed and updated by the rest of the team.
Every team has a repository with these guidelines in the GitHub organisation. 
Check examples for
[Portuguese](https://github.com/TWTranslation/Portuguese_specific_translation_guidelines), [Arabic](https://github.com/TWTranslation/Arabic-specific-Translation-rules), and [Turkish](https://github.com/TWTranslation/Turkish-specific-Translation-rules).
We have also set up a public page for _The Turing Way_ in [Crowdin](https://turingway.crowdin.com/turing-way) with a README file summarising some of the translation guidelines. 
Make sure you read these guidelines before you start translating for the first time.


### Create and update a glossary

We strongly suggest setting a glossary through the localisation platform.
You can read more about project glossaries in {ref}`Adding terms to the glossary<ch-translation-gateway-crowdsourced-localisation>`.
The Carpentries [Glosario](https://glosario.carpentries.org/) and the [Localization Lab glossary](https://www.localizationlab.org/glossaries) are two good examples of such glossaries.

### Share the translation memory of the project

In order to facilitate and speed up the translation of a new language, we recommend sharing translation memory with other projects so similar strings can be translated automatically.
_The Turing Way_ project is linked with the translation memory of a previous version translated in Transifex and another translation for [Open Life Science](https://openlifesci.org/) materials in OLS.

Translation consistency is crucial and can be made easier when the TMS is used.
As soon as you started translating your project, machine learning algorithms engage, and the system shows previous translations for the source words and how often they were used in the project[^1]. 
For example, in Crowdin, you can hover over the source words underlined with the light dashed line to see the previous translations formed by the translation consistency feature. 
You can also search earlier translations for specific source words using the Search TM tab.

```{figure} ../../figures/translation-consistency-previous-translations-editor.*
---
name: translation_consistency_previous_translations_editor
width: 90%
alt: Checking consistency in Crowdin by hovering over the source words underlined and a list of previous translations formed by the translation consistency feature will show.
---
```


### Team governance

We have teams for each language, so that no one works alone.
Each team can decide roles for their project members.
In the translation platform, these roles can translate into having different permissions. 
Roles in Crowdin include manager, translator, and proofreader.
- **Manager** – has similar rights as a project owner except for the ability to manage some of the owner's Resources (for instance, configuring MT engines, advanced workflows, and more) and delete projects.
- **Proofreader** – can translate and approve strings.
Unlike the manager, the Proofreader doesn't have access to project settings.
- **Translator** – can translate strings and vote for translations added by other members.


```{figure} ../../figures/translation-memory-animation.*
---
name: translation-memory
width: 90%
alt: An illustration showing how translation memory can speed up the crowdsourcing of new projects.
---
Illustration of translation as a way to reach global accessibility. _The Turing Way_ project illustration by Scriberia.
Used under a CC-BY 4.0 licence.
DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807)
```  

In each co-working or external session, prioritise those chapters that are outdated or close to completion. 
Check out our {ref}`guidelines<ch-translation-localisation-journey>` for a list of the priorities.

### Decision making
- If any big changes in the infrastructure of the whole workflow have to be made, they can be documented  and the rest of the team should have reasonable time to see the proposal and approve it. What "big" change means, and what "reasonable" time means are up to each one--based on common sense, no need to wait forever for a tiny change--, but tagging the relevant team members to prompt a revision/an opinion can be a good practice to have quick feedback and make decisions quicker. 
- Not everybody in the team lead should have to participate to decide on something, maybe only one +1 is enough. If the first person reviewing does not agree or the change needs more discussion, they can call a third member to give an opinion and discuss the change. 3/4 people should be enough to make a decision.
- Team lead meetings every 1-2 months in the same slot of the translation co-working call. 


# Translation is a continuous process

As _The Turing Way_ content grows, the translated content does too. 
We strongly encourage monitoring the new content and updating the translation fork regularly.
While updates of the translated content might change according to the availability of resources, it is good practice to:

* Set periodical reviews to improve translations
* Update translation guidelines and glossaries

If you have any recommendations for improving the translation guidelines or setting up language-specific rules, contact [the translation and localisation team](https://github.com/the-turing-way/the-turing-way/blob/main/ways_of_working.md).
We are very eager to improve the workflow and make _The Turing Way_ a global project accessible to the wider community.


In the next chapter, you'll be introduced to  Crowdin and how we use it to translate _The Turing Way_.
[^1]: This image and description are borrowed directly from [Crowdin docs](https://support.crowdin.com/translation-consistency/).
