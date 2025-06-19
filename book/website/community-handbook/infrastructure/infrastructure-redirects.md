(ch-infrastructure-redirects)=
# Redirects

When a web server receives a request, it may return a [redirection response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#redirection_messages) (with a 30X return code).
We use redirects for a few purposes,

- to prevent link rot by forwarding old paths to new locations
- to redirect specific addresses to external domains

Redirecting at the web server rather than with [DNS](#ch-infrastructure-dns) has some advantages,

- We have more control over the format of the redirect, for example we can use wildcards and substitution.
- Redirection will happen _after_ TLS, so HTTPS can be used.
- Clients will receive HTTP codes indicating that they were redirected, and whether the redirect should be considered permanent.
- The redirects are described in plain text in the book repository, making them more visible and easier to contribute to.

## Netlify redirects

Redirects for _The Turing Way_ are defined in [nelify.toml](https://github.com/the-turing-way/the-turing-way/blob/main/netlify.toml) in the array of tables `[[redirects]]`.
The [TOML syntax](https://toml.io/en/v1.0.0#array-of-tables) means that a new `[[redirects]]` item is added for each redirect we want to define.
The syntax for Netlify redirects [is described in their documentation](https://docs.netlify.com/routing/redirects/#syntax-for-the-netlify-configuration-file), where the [available options](https://docs.netlify.com/routing/redirects/redirect-options) are also explained.

:::{important}
For Netlify to redirect a domain, that domain **must**,

1. Resolve to the Netlify load balancer (which means [DNS](#ch-infrastructure-dns) must be configured to point that domain to Netlify)
2. The [domain must be assigned to the site](https://docs.netlify.com/routing/redirects/redirect-options/#domain-level-redirects).
   After your primary domain, these extra domains should be added as [aliases](https://docs.netlify.com/domains/configure-domains/add-a-domain-alias/).
   This is so that Netlify knows that _we_ want to handle the requests to these domains reaching their load balancer, as they host many site with their own rules.
3. For HTTPS support, the TLS certificate must include the subdomain to redirect.
   You can view which domains the cert covers in the Netlify dashboard, and renew the cert if you have added new subdomains.
:::

## Our redirects

### www

We have a [wildcard](https://docs.netlify.com/routing/redirects/redirect-options/#splats), permanent redirect for `https://www.book.the-turing-way.org/*` which returns the preferred url, without www.

### Old book domain

We have a [wildcard](https://docs.netlify.com/routing/redirects/redirect-options/#splats), permanent redirect for the old book domain at `https://the-turing-way.netlify.app/*` which returns the new url.

### Start page

In our [DNS](#ch-infrastructure-dns) configuration we have pointed `the-turing-way.org` and `www.the-turing-way.org` to the Netlify load balancer. We redirect these to `the-turing-way.start.page` as a landing page for _The Turing Way_ project as a whole.

### Moved chapters

Most of the redirects are for chapters or pages which have moved internally.
The full list of these isn't described here but can be seen in [nelify.toml](https://github.com/the-turing-way/the-turing-way/blob/main/netlify.toml).

(ch-infrastructures-redirects-helpers)=
### Helpers

Our helper redirects allow us to have easy to remember and share URLs which we can point to community resources, which may move.
We currently have the following helpers,

| Helper URL                                                   | Directs to                           |
| ---                                                          | ---                                  |
| [git.the-turing-way.org](https://git.the-turing-way.org)     | Our git repositories                 |
| [news.the-turing-way.org](https://news.the-turing-way.org)   | Our newsletters archive              |
| [slack.the-turing-way.org](https://slack.the-turing-way.org) | An invitation to our Slack workspace |
