# DNS

DNS is …
You can think of DNS like a phone book for the internet.
You configure DNS by creating records.
_The Turing Way's_ DNS records is managed on [NameCheap](https://namecheap.com) by the DNS team, a sub-team of the Infrastructure Working Group.

On the internet, DNS is managed by a series of connect providers.
Google has a DNS service at `8.8.8.8` and `8.8.4.4`.
Cloudflare has a DNS service at `1.1.1.1`.
It is very likely that you will use a DNS server run by your internet provider, although you can often change this.
DNS is not encrypted, so in theory the DNS server you use can see what domains you are requesting.
However, DNS over HTTPS is available and becoming more common.

To learn more about DNS …

## Looking at DNS Records

`dig`, `nslookup` …

## CNAME records

Address aliases
Book `book.the-turing-way.org`

`book CNAME the-turing-way.netlify.app.`

## Redirects

Namecheap DNS allows redirecting to URLs.
This is not part of DNS.
You could achieve a similar thing by having your webserver redirect requests.
For example, with NGINX you could [`rewrite`](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html) a path.

Root `the-turing-way.org`

`@ URL-Redirect https://the-turing-way.start.page`

GitHub `git.the-turing-way.org`

`git URL-Redirect https://github.com/the-turing-way`

Slack `slack.the-turing-way.org`

`slack URL-Redirect <slack invite link>`

Newsletter `news.the-turing-way.org`

`news URL-Redirect https://buttondown.email/turingway`

## SSL

Secure Socket Layer (SSL) is a protocol for secure communication.
SSL is used to encrypt HTTP traffic in HTTPS.
Almost every time you access a website in a browser will be over HTTPS.
It is important to encrypt web traffic, particularly when you are sending or receiving secret information such as user credentials, bank details and personal data.
[Netlify managed SSL certs](https://docs.netlify.com/domains-https/https-ssl/#netlify-managed-certificates)

Add a [CAA record](https://letsencrypt.org/docs/caa/) so that only Netlify can issue certs.
This is security best practice.

`book CAA 0 iodef letsencrypt.org;accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/54403714`
