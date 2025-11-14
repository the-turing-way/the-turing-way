(ch-acknowledgement-record)=
# Record of Contributions

The [](#contributors-record) in the [](#aw) is where contributors to _The Turing Way_ are presented.
The [](#contributors-record) draws from three sources,

:::{table}
:label: tab-contribution-records
| Record type                        | Source                                                                                                                    | Presented in                          |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Individual highlights and profiles | [Page source](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/afterword/contributors/profiles.md) | [](#contributors-record-individual)  |
| All contributors                   | [All contributors file](https://github.com/the-turing-way/the-turing-way/blob/main/.all-contributorsrc)                   | [](#contributors-record-all)          |
| Translations                       | Crowdin API                                                                                                               | [](#contributors-record-translators) |
:::


We invite all our members to co-create this record to capture the important work they do around answering questions, representing the project, developing and maintaining the infrastructure, and all other nurturing roles that make _The Turing Way_ community so special.

The process of developing this record is described below.

## Getting Recognised

### All Contributors Table

The [all contributors table](#contributors-record-all) is updated with every contributor's name using the [all contributors bot](https://allcontributors.org/)'s [emoji key](https://allcontributors.org/docs/en/emoji-key).

Instructions for using the all contributors bot are given in [the contributing guide](#ch-style-roles-profile).

**No contribution is too small**, and these emojis allow us to recognise and fairly acknowledging all kinds of contributions our community members make to the project.
Those contributions can include (but are not limited to) bug fixing, chapter planning, writing, editing, reviewing, idea generation, presentation, project management, and maintenance.
Please see [](#ch-acknowledgement-examples) for details.

```{figure} ../../../figures/allcontributorsbot-emoji.*
---
height: 400px
name: AllContributorsEmojiKey
alt: Table with different emojis that is used by the contributors bot
---
[Emoji key table](https://allcontributors.org/docs/en/emoji-key) of the all contributors bot that _The Turing Way_ uses for acknowledging different contributions from community members.
```

(ch-acknowledgement-record-individual)=
### Individual highlights and profiles

To add or edit your profile on the [](#contributors-record-individual) page, edit that page.
We use the [`profile`](#ch-style-roles-profile) directive to create entries.
Instructions for how to use the directive are given [here](#ch-style-roles-profile).

All types of contributions made towards _The Turing Way_ can be added to [personal highlights](#contributors-record-highlights).
These highlights can be individually decided by the contributors to record what they consider to be their significant and useful contributions for their personal profile.
This can be supplemented with supporting materials such as links to chapters, pull requests, issues, and blog posts.

This record can be directly translated towards the professional development of our community members, which can be further used for enhancing their personal or professional portfolio (profile, CV, resume).

The personal highlights are very valuable for capturing the impact that _The Turing Way_ has for its community members in terms of personal networking, professional development, skill sharing and other relevant activities, and how they have made positive impacts around transparency, reproducibility and ethical collaboration in their organisation.

### Translators

The data for the [record of translators](#contributors-record-translators) is fetched from the Crowdin API.
A regular action is run to open a pull request updating this data.
If you have contributed translations to _The Turing Way_ through Crowdin, you should automatically be acknowledged.
