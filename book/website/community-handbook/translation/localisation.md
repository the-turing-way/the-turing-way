(ch-translation-localisation)=

## Localisation Platforms and Translation


Localization (l10n) and internationalization (i18n) are important aspects in the design of any open-source project or documents.  Internationalization allows open-source project to support and satisfy the needs of multiple locales, thus “enabling” localization, which is the adaptation of it to meet the language, cultural of a specific target locale.  World Wide Web Consortium (W3C) define internationalization (i18n) as:
> "The design and development of a product, application or document content that enables easy localization for target audiences that vary in culture, region, or language"


 **A Translation Management System (TMS)** manages the localisation process from the beginning of a translation process until the finished product. They are widely used in Open source projects because they offer many advantages such as workflow, automation, transparency, and fast project delivery.

```{figure} ../../figures/Translation_management_systems.jpg
---
height: 500px
name: Translation
alt: This illustration shows the features of Translation Management System. It contains Translation Memory, Machine Translation, glossary, QA checks which are easily integrated with GitHub.
---
_The Turing Way_ project illustration by Scriberia.
Used under a CC-BY 4.0 licence.
DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807)
```

### Examples for Localisation Platforms:

Many open source projects are localised using Translation Management System (TMS) such as [GitLab](https://crowdin.com/project/gitlab-ee), [FreeCAD](https://crowdin.com/project/freecad), [electron](https://crowdin.com/project/electron), [PostgreSQL](https://crowdin.com/project/postgresql), [OBS Studio](https://crowdin.com/project/obs-studio).

- [Transifex](https://www.transifex.com/)
- [Crowdin](https://crowdin.com/?gclid=CjwKCAiAvriMBhAuEiwA8Cs5ldEGwrOeDJtdY2kneF6vBXx8hYiXD1oJPcWB1SO0VBSTuz60AaDYUhoCj_8QAvD_BwE)
- [Lokalise](https://lokalise.com/)
- [Pontoon](https://pontoon.mozilla.org/)

### Features of Localisation Platforms:

- **Translation Memory**

Translation Memory can be described as a database of sentences or texts and their translations that can be automatically reused in/outside the project. Translation Memory can be very powerful in ensuring consistent and high-quality translations across different projects.
- **Glossary**

A glossary is a collection of the key terms that are used in the project to ensure consistency. The glossary helps in creating, storing, and managing all the project terminology in one place.
- **Machine Translation**

Machine Translation can speed up the translation process. It provides translation suggestions from automatic translation services like Google Translate and AutoML Translation, Microsoft Translate, and more.
- **Integration with GitHub**

Continuous integration is vital for automation in open sources projects. Many localisation platforms offer integration with GitHub, which synchronises source and translation files between your GitHub repository and translation project.
- **Screenshots for the context**

Screenshots provide context to the text for translation. TMS offer the opportunity of attaching screenshots to each of the phrases to provide a visual context to translators
- **QA checks**

Many TMS support QA checks. These can include spelling and/or grammatical errors, inconsistent placeholders, and unbalanced brackets. These QA checks make the translation process smoother for translators.

In the next chapter, you'll be introduced to Crowdin and how we use it translate _The Turing Way_.
