(ch-style-roles-and-directives)=
# Custom Roles and Directives

MyST [roles](xref:myst-spec/overview#roles) and [directives](xref:myst-spec/overview#directives) extend the behaviour of {term}`Markdown`.
They can be used to add features that are not part of [CommonMark](xref:myst-spec/commonmark), or to automate common or complex structures with reusable commands.
The MyST guide has documentation for the built in [roles](xref:myst-guide/roles) and [directives](xref:myst-guide/directives)

We can write our own roles and directives to help improve the books consistency and make writing easier.

## Directives

(ch-style-roles-profile)=
### Profile

The profile directive is used to generate profiles for [](#contributors-record).
The argument is the name of the person being profiled.
There are a number of options to add information to a profile, all of these are optional.

It is best to use a YAML block to write the options as this allows you to write multi-line blocks for the biography.

Here is an example profile,

```Markdown
:::{profile} Your Name
---
roles: >
    semi-colon seperated list;
    of your roles;
    in the community
github: JimMadge # <GitHub id without leading @>
orcid: 0000-0001-6044-164X # <orcid>
mastodon: JimMadge@fosstodon.org # <Mastodon id without leading @, like person@mastodon.social>
twitter: # <Twitter id without leading @>
website: # <website url>
bio: |
    A short Biography about yourself.
    You can write a new sentence of each line.

    Leaving a blank line will start a new paragraph.
    You can use MyST *Markdown* _formatting_ here.
highlights: |
    A few highlights about your experiences in _The Turing Way_
more: |
    Some further information about yourself
quote: |
    A personal quote
---
:::
```

Which renders like,

:::{profile} Your Name
---
roles: >
    semi-colon seperated list;
    of your roles;
    in the community
github: JimMadge # <GitHub id without leading @>
orcid: 0000-0001-6044-164X # <orcid>
mastodon: JimMadge@fosstodon.org # <Mastodon id without leading @, like person@mastodon.social>
twitter: # <Twitter id without leading @>
website: # <website url>
bio: |
    A short Biography about yourself.
    You can write a new sentence of each line.

    Leaving a blank line will start a new paragraph.
    You can use MyST *Markdown* _formatting_ here.
highlights: |
    A few highlights about your experiences in _The Turing Way_
more: |
    Some further information about yourself
quote: |
    A personal quote
---
:::

This profile can be referenced using the label `profile-your-name`.
Like, `[my profile](#profile-your-name)` [my profile](#profile-your-name).

## Roles

(ch-style-roles-github-user)=
### GitHub User

The GitHub User role produces a link to a GitHub user profile.
This helps ensure links to GitHub profiles are consistent across the book and avoids duplicating the user name in text and in the URL.

The role takes one argument, which is the name of the profile.
For example, `` {githubuser}`the-turing-way` `` renders as {githubuser}`the-turing-way`.
