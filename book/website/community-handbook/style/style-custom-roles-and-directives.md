(ch-style-roles-and-directives)=
# Custom Roles and Directives

MyST [roles](xref:myst-spec/overview#roles) and [directives](xref:myst-spec/overview#directives) extend the behaviour of Markdown.
They can be used to add features that are not part of [CommonMark](xref:myst-spec/commonmark), or to automate common or complex structures with reusable commands.
The MyST guide has documentation for the built in [roles](xref:myst-guide/roles) and [directives](xref:myst-guide/directives)

We can write our own roles and directives to help improve the books consistency and make writing easier.

## Roles

(ch-style-roles-github-user)=
### GitHub User

The GitHub User role produces a link to a GitHub user profile.
This helps ensure links to GitHub profiles are consistent across the book and avoids duplicating the user name in text and in the URL.

The role takes one argument, which is the name of the profile.
For example, `` {githubuser}`the-turing-way` `` renders as {githubuser}`the-turing-way`.
