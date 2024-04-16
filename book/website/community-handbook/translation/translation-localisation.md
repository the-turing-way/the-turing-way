(ch-translation-localisation)=

# Translation of Open Source Projects
## Localisation Platforms and Translation


Localisation (l10n) and internationalisation (i18n) are important aspects in the design of any open-source project.
Internationalisation allows open-source projects to support and satisfy the needs of multiple regions and languages, thus enabling localisation, which is the adaptation to meet the language and cultural context of a specific target locale.
The World Wide Web Consortium ([W3C](https://www.w3.org/)) defines internationalisation (i18n) as:
> "The design and development of a product, application or document content that enables easy localisation for target audiences that vary in culture, region, or language"


Localisation involves more than just translation, which only transforms text.
Localisation addresses other factors such as text length and cultural references.
A **Translation Management System (TMS)** manages the localisation process from the beginning of a translation process until the finished product.
TMS are widely used in Open source projects because they offer many advantages such as workflow automation, transparency, and fast project delivery.

```{figure} ../../figures/translation-management-systems.*
---
height: 500px
name: Translation_
alt: This illustration shows the features of a Translation Management System. It contains Translation Memory, Machine Translation, glossary, QA checks, integration with GitHub, and some community features that facilitate collaboration.
---
_The Turing Way_ project illustration by Scriberia.
Used under a CC-BY 4.0 licence.
DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807)
```

## Examples for Localisation Platforms

Many open source projects such as [GitLab](https://crowdin.com/project/gitlab-ee), [FreeCAD](https://crowdin.com/project/freecad), [electron](https://crowdin.com/project/electron), [PostgreSQL](https://crowdin.com/project/postgresql), [OBS Studio](https://crowdin.com/project/obs-studio) are localised using various Translation Management Systems (TMS).

- [Transifex](https://www.transifex.com/)
- [Crowdin](https://crowdin.com/?gclid=CjwKCAiAvriMBhAuEiwA8Cs5ldEGwrOeDJtdY2kneF6vBXx8hYiXD1oJPcWB1SO0VBSTuz60AaDYUhoCj_8QAvD_BwE)
- [Lokalise](https://lokalise.com/)
- [Pontoon](https://pontoon.mozilla.org/)
- [Weblate](https://weblate.org/en/)

### Features of Localisation Platforms


Localisation platforms integrate different tools and formats for assisting the translation process.
The translation process can be assisted by machine translation.
Different languages may work better with a specific machine translation engine. For example, Spanish works very well with [DeepL](https://www.deepl.com/) as a translation tool but other languages (for example, Arabic) don't. 
DeepL recommends a series of synonyms when you click on the translated text.
This can be useful, especially with long texts.
For [Transifex](https://www.transifex.com/), a popular TMS used by several Open Source projects, the automated process is performed outside the platform.
In contrast, [Crowdin](https://crowdin.com/?gclid=CjwKCAiAvriMBhAuEiwA8Cs5ldEGwrOeDJtdY2kneF6vBXx8hYiXD1oJPcWB1SO0VBSTuz60AaDYUhoCj_8QAvD_BwE) is integrated with well-known machine translation providers, including Google, Microsoft, DeepL, and Yandex.


- **Translation Memory**

Translation Memory can be described as a database of sentences or texts and their translations that can be automatically reused in and outside the project.
Translation Memory can be very powerful in ensuring consistent and high-quality translations across different projects.

- **Glossary**

A glossary is a collection of the key terms that are used in the project to ensure consistency.
The glossary helps in creating, storing, and managing all the project terminology in one place.


- **Machine Translation**

Machine Translation can speed up the translation process.
It provides translation suggestions from automatic translation services like Google Translate and AutoML Translation, Microsoft Translate, and more.

- **Integration with GitHub**

Continuous integration is vital for automation in open sources projects. Many localisation platforms offer integration with GitHub, which synchronises source and translation files between your GitHub repository and translation project.

- **Screenshots for the context**

Screenshots provide context to the text for translation.
TMS offer the opportunity of attaching screenshots to each of the phrases to provide a visual context to translators

- **QA checks**

Many TMS support QA checks.
These can include spelling and/or grammatical errors, inconsistent placeholders, and unbalanced brackets.
These QA checks make the translation process smoother for translators.

In the next chapter, you will be introduced to  the translation and localisation team and how we organise our workflows.
