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

## Summary of Records

There are many DNS record types.
The following table gives a simple explanation of some of the more common ones.

| Record | Purpose                                                             |
|--------|---------------------------------------------------------------------|
| A      | Directs a hostname to an IPv4 address                               |
| AAAA   | The same as A but for IPv6                                          |
| CNAME  | Makes the hostname an alias for another                             |
| MX     | Points to an email server for the domain                            |
| TXT    | Arbitrary text, often used to configure SSL or email authentication |
| NS     | Delegates DNS to a different nameserver                             |

## Looking at DNS Records

You can inspect DNS records using the `dig` or `nslookup` commands.

The `dig` command line can be formatted like

```console
dig [@DNS-server] [domain] [record-type]
```

For example, we can check the CNAME record for `book.the-turing-way.org` using Google's DNS server (`8.8.8.8`) like this

```console
$ dig @8.8.8.8 book.the-turing-way.org CNAME

; <<>> DiG 9.10.6 <<>> @8.8.8.8 book.the-turing-way.org CNAME
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64376
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;book.the-turing-way.org.       IN      CNAME

;; ANSWER SECTION:
book.the-turing-way.org. 1800   IN      CNAME   the-turing-way.netlify.app.

;; Query time: 75 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Mar 18 14:47:29 GMT 2024
;; MSG SIZE  rcvd: 92

```

We can see in the answer section that there is a CNAME record meaning that `book.the-turing-way.org` is an alias for `the-turing-way.netlify.app`.
What happens if you look for a TXT record at `egg.the-turing-way.org`?

## The Turing Way Records

Here we describe the records that have been created for _The Turing Way_.

### CNAME records

Address aliases
Book `book.the-turing-way.org`

`book CNAME the-turing-way.netlify.app.`

### Redirects

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

### CAA

Secure Socket Layer (SSL) is a protocol for secure communication.
SSL is used to encrypt HTTP traffic in HTTPS.
Almost every time you access a website in a browser will be over HTTPS.
It is important to encrypt web traffic, particularly when you are sending or receiving secret information such as user credentials, bank details and personal data.
[Netlify managed SSL certs](https://docs.netlify.com/domains-https/https-ssl/#netlify-managed-certificates)

Add a [CAA record](https://letsencrypt.org/docs/caa/) so that only Netlify can issue certs.
This is security best practice.

`book CAA 0 iodef letsencrypt.org;accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/54403714`
