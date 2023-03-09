(ch-translation-hello-crowdin)=

# Crowdin 101

Crowdin editor is your friend.
You can use it to change translation language, proofread, add comments for contributors, contact the managers, vote translations, view suggestions for translation from translation memory or find Machine Translation from Google, Crowdin, DeepL, and others.

## Hello Crowdin

Once you click on any file, you will be directed to the comfortable mode in Crowdin crowdsourcing editor. 
There are different modes and editors inside Crowdin but we will only go through comfortable mode and proofreader mode in Crowdin crowdsourcing editor.
You can find more information about Crowdin Editor from the [documentation here](https://support.crowdin.com/enterprise/getting-started-for-translators/).

The comfortable mode is divided into four sections:
1. **Left Sidebar:** It contains all strings in the file that you will translate.
2. **Middle-top area:** The main working area where you edit/upvote the translations.
3. **Middle-bottom area:** This section contains suggestions from Translation Memory, Machine Translation (MT) suggestions, and translations by other project participants
4. **Right sidebar:** You can use it to add comments, report issues, and see the existing Glossary available for the strings.


```{figure} ../../figures/crowdin-editor.png
---
name: crowdin-editor
width: 90%
alt: The crowdin editor with four sections labelled from number 1-4.
---
```  

As shown in the image below, the Middle-top area (3) is the main working area with the source string on the top, and the section where you can type in translations below. 
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

An active string is highlighted with the yellow color but you can turn on/off color highlight of strings by clicking on ![icons](../../figures/icons/preview_filter.png) and  - show translation preview using ![icons](../../figures/icons/eye.png).

Crowdin editor won't only show you suggestions of a translation made by the translation engine but also suggestions from translation in different projects that shared their translation memory (TM) with the Turing Way and will be detected if the string is similar by 70%.
This avoids duplication of effort.
If you would like to re-use our translation memory (TM) in your own open-source projects, feel free to contact our Translation and Localisation leads.  

```{figure} ../../figures/Translation_Memory.gif
---
name: Translation_Memory
width: 90%
alt: Translation_Memory suggesting a translation for a project which was carried out in Transifex.
---
```  

```{important}
We can re-use translation memory (TM) from projects translated inside and outside Crowdin (for example, TransLocalize, Crowdin, Transifex) or even that were translated manually from Google docs.

Get in touch if you want to share the translation memory (TM) of a previously translated project.
```

## Adding glossary

In order to translate the project's terminology properly and consistently, we keep them in a Glossary.
In the Glossary, you can create, store, and manage all the project terminology in one place.

```{figure} ../../figures/Glossary.png
---
name: Glossary_
width: 90%
alt: Glossary in Crowdin which is table showing the terms in multiple languages.
---
```  

```{admonition} Tip
:class: tip
You can upload Glossary or share Glossaries across different projects.
```

```{figure} ../../figures/Adding-glossary.gif
---
name: Adding-glossary
width: 90%
alt: The Crowdin editor shows the glossary term underlined and you can also add new one by highlighting the term and clicking on add term. A new window will be prompt where you can fill its details.
---
```  

The terms that were added to the project glossary will be underlined in the source string.
You can check additional explanations added to the term for an accurate translation.


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
When you reach a satisfactory translation, click on Save.


## Adding Comments

You can discuss the meaning of the source string or report the issues regarding the source strings in the comment tab (**Right sidebar**). 
You can also use `@` and the username to direct your message to a specific person. 
You can point out if the current translation is wrong or if the translation lacks contextual information.
The issues are reported to the project managers to correct mistakes or add context and resolve the issues.

The terms that were added to the project glossary will be underlined in the source string. You can check additional explanation added to the term for the accurate translation. A project manager can also give you permission to add terms to the project glossary.

In the next chapter, we'll go through how you can manage the project and manage your translation team.
