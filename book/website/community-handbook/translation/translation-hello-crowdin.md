(ch-translation-gateway-crowdsourced-localisation)=

# Your Gateway to Crowdsourced Localisation

The [Crowdin](https://crowdin.com/) editor is your friend.
You can use it to change translation language, proofread, add comments for contributors, contact the managers, vote on translations, view suggestions for translation from Translation Memory or find Machine Translation from Google, Crowdin, DeepL, and others.

Once you click on any file, you will be directed to the comfortable mode in the Crowdin crowdsourcing editor. 
There are different modes and editors inside Crowdin but we will only go through comfortable mode and proofreader mode in the Crowdin crowdsourcing editor.
You can find more information about the Crowdin Editor from the [documentation here](https://support.crowdin.com/enterprise/getting-started-for-translators/).

The comfortable mode is divided into four sections:
1. **Left Sidebar:** It contains all strings in the file that you will translate.
2. **Middle-top area:** The main working area where you edit/upvote the translations.
3. **Middle-bottom area:** This section contains suggestions from Translation Memory, Machine Translation (MT) suggestions, and translations by other project participants
4. **Right sidebar:** You can use it to add comments, report issues, and see the existing Glossary available for the strings.


```{figure} ../../figures/crowdin-editor.*
---
name: crowdin-editor
width: 90%
alt: The crowdin editor with four sections labelled from number 1-4.
---
```  

As shown in the image above, the Middle-top area (3) is the main working area with the source string on the top, and the section where you can type in translations below. 
Crowdin will show you suggestions for translation carried out using three different engines (Google Translate, Crowdin Translate, DeepL), which will show you several possible translations that you can further edit.

```{admonition} Add Translation Engine
:class: tip
If your language of interest works better with different engines (for example, Microsoft Translator, Yandex.Translate, Amazon Translate), please request it and we will do our best to integrate it.  
```
Strings may have the following statuses:

- ![icons](../../figures/icons/untranslated_icon.png) - Untranslated
- ![icons](../../figures/icons/partially_translated_icon.png) - Partially translated (in this case, some of the plural forms are not translated)
- ![icons](../../figures/icons/translated_icon.png) - Translated
- ![icons](../../figures/icons/partially_approved_icon.png) - Partially approved (in this case, some plural forms are not approved)
- ![icons](../../figures/icons/approved_icon.png) - Approved
- ![icons](../../figures/icons/hidden_icon.png) - Hidden (visible only for project managers and proofreaders)

An active string is highlighted with the yellow color but you can turn on/off color highlight of strings by clicking on ![icons](../../figures/icons/preview_filter.png) and show translation preview using ![icons](../../figures/icons/eye.png).

Crowdin editor won't only show you suggestions of a translation made by the translation engine but also suggestions from translation in different projects that shared their Translation Memory (TM) with _The Turing Way_ and will be detected if the string is has a similarity above 70%.
This avoids duplication of effort.
If you would like to re-use our Translation Memory (TM) in your own open-source projects, feel free to contact our Translation and Localisation leads.  

```{figure} ../../figures/translation-memory.*
---
name: Translation_Memory
width: 90%
alt: Translation_Memory suggesting a translation for a project which was carried out in Transifex.
---
```  

```{important}
We can re-use Translation Memory (TM) from projects translated inside and outside Crowdin (for example, TransLocalize, Crowdin, Transifex) or even that were translated manually from Google docs.

Get in touch if you want to share the Translation Memory (TM) of a previously translated project.
```

## Adding terms to the glossary

In order to translate the project's terminology properly and consistently, we keep them in a Glossary.
In the Glossary, you can create, store, and manage all the project terminology in one place. 
The use of glossaries in each language team is optional, but heavily recommended. Each project automatically generates its own Glossary when it's created, and it can be filled with content by each project team. 

```{figure} ../../figures/Glossary.*
---
name: Glossary_
width: 90%
alt: Glossary in Crowdin which is table showing the terms in multiple languages.
---
View of the full Glossary of the different languages. 
Only Crowdin contributors with manager role can access this view.
```  


To add terms to the Glossary you need to double-select a term, and then select the option "create term". 
A new window will appear showing both the English and [language] explanations for that term. 
If the term is new in that language, you'll need to specify the equivalent word in your language for that English term.

```{figure} ../../figures/adding-glossary.*
---
name: Adding-glossary
width: 90%
alt: The Crowdin editor shows the glossary term underlined and you can also add new one by highlighting the term and clicking on add term. A new window will be prompt where you can fill its details.
---
Workflow for adding new terms while translating.
```

For a file that needs to be translated, you can search which words from it are present in the Glossary by selecting the "Terms" icon on the Crowdin editor.

The terms that were added to the project Glossary will be underlined in the source string.
You can check additional explanations added to the term for an accurate translation.


```{admonition} Tip
:class: tip
You can upload a glossary or share glossaries across different projects. To do so, contact a contributor with Crowdin manager role.
```

## Proofreading

Proofreading mode will show you the original string, the current translation and some options proposed by Crowdin.
When a string matches past translations, these past translations will appear among the options.

```{warning}
The translated files won't be exported to GitHub unless they have been completely translated and proofread.

**Do not translate:**
- Python book tags `(#welcome)=`
- Relative file paths
- Fields `name:` and `alt:` in images

**Check for modifications in:**
- References
- Tag and variable order `{ref}<0>text</0>` should have the same structure
```

```{figure} ../../figures/proofreading.gif
---
name: proofreading.gif
width: 90%
alt: The proofreading mode in Crowdin editor where you can click in the tick to approve the translation.
---
```  

When you are proofreading, pay extra attention to punctuation. 
You can either choose one of these or edit directly in each string's field. 
When you reach a satisfactory translation, select Save.


## Adding Comments

You can discuss the meaning of the source string or report issues regarding the source strings in the comment tab (**Right sidebar**). 
You can also use `@` and the username to direct your message to a specific person. 
You can point out if the current translation is wrong or if the translation lacks contextual information.
The issues are reported to the project managers to correct mistakes or add context and resolve the issues.

The terms that were added to the project glossary will be underlined in the source string. 
You can check additional explanations added to the term to help with accurate translation.
A project manager can also give you permission to add terms to the project glossary.

# Embracing Global Accessibility through Localisation and Crowdsourcing

The process of translating _The Turing Way_ into multiple languages through crowdsourcing has been a remarkable endeavor, showcasing the power of collaboration and inclusivity within the open-source community.
Through the collective efforts of volunteers and contributors worldwide, the project has successfully bridged language barriers and expanded its reach to diverse communities.

```{important}
The translation process is an excellent opportunity not only to bring _The Turing Way_ to your language, but also to review and improve its content and make it more accessible and localisable for everyone. 
- If you run into alt text (which should be translated) that is incomplete, too short, or doesn't correspond to the content it's referring to, please create an Issue so we can address it.
- Some sections of the _The Turing Way_ may be written in a way that makes it difficult for language teams to translate them.
For example, translation teams working with languages with gender marks may find it challenging to translate particular contents in a inclusive manner.
There can also be references to very specific contexts in some countries, or certain "internal jokes" that get (literally) lost in translation.
You can help make the handbook more localisable by submitting an Issue that describes the problem, or even better, a Pull Request that modifies the original text to make it more translatable.
```

Crowdsourcing has played a pivotal role in this translation endeavor, harnessing the collective intelligence and linguistic skills of individuals passionate about open science and reproducible research. 
By tapping into the wisdom of the crowd, _The Turing Way_ has been able to leverage the knowledge and expertise of a global network, ensuring accurate and contextually relevant translations.

The benefits of localising and translating _The Turing Way_ are far-reaching.
It not only makes this invaluable resource more accessible to non-English-speaking communities but also fosters a sense of inclusivity, enabling researchers from various cultural backgrounds to engage with best practices and principles in research reproducibility.

The translation of _The Turing Way_ into different languages through crowdsourcing is a testament to the power of collective action and the commitment to open science principles. 
Through the dedication and collaboration of individuals around the world, _The Turing Way_ continues to evolve and thrive as a comprehensive and inclusive resource for the research community, transcending language barriers and fostering a culture of reproducibility on a global scale.
