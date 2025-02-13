# DNS

Domain Name System (DNS) is how human-readable domains, like `book.the-turing-way.org` get translated to Internet Protocol (IP) addresses that computers use to locate each other.
You can think of DNS like a phone book for the internet.
Without it, you wouldn't be able to use domain names to find websites or services.
DNS is configured by creating records, which give instructions on how to handle requests depending on the domain name.

On the internet, DNS is managed by a series of connect providers.
Google has a DNS service at `8.8.8.8` and `8.8.4.4`.
Cloudflare has a DNS service at `1.1.1.1`.
DNS servers are connected and propagate records to each other.
That means, if you want to host something on your domain you don't have to create records on every DNS server for the public to find it.

It is very likely that you will use a DNS server run by your internet provider, although you can often change this.
DNS is not encrypted, so in theory the DNS server you use can see what domains you are requesting.
However, DNS over HTTPS is available and becoming more common.

To learn more about DNS you can read [Cloudflare's DNS learning documents](https://www.cloudflare.com/learning/dns/what-is-dns/).

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
book.the-turing-way.org. 1800   IN      CNAME   book.the-turing-way.org.

;; Query time: 75 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Mar 18 14:47:29 GMT 2024
;; MSG SIZE  rcvd: 92

```

We can see in the answer section that there is a CNAME record meaning that `book.the-turing-way.org` is an alias for `book.the-turing-way.org`.
What happens if you look for a TXT record at `egg.the-turing-way.org`?

## The Turing Way Records

_The Turing Way's_ DNS records are managed on [NameCheap](https://namecheap.com) by the DNS team, a sub-team of the Infrastructure Working Group.
Here we describe the records that have been created for _The Turing Way_.

The records are in the format,

```
domain type value
```

The domain `@` means the root domain, like `example.com`.
Otherwise the domain is a subdomain of the root domain.
For example `www` would mean `www.example.com`

### CNAME records

As explained in [](#summary-of-records) CNAME records are aliases.
We use a CNAME record for _The Turing Way_ book at `book.the-turing-way.org`.
This is an alias for the domain where the book is hosted, which is currently on Netlify.
If the book is moved to another hosting provider the record can be updated to point to the new host.
That way, the book will _always_ be accessible at `book.the-turing-way.org` no matter how or where it is hosted.

```
book CNAME book.the-turing-way.org.
```

### URL Redirects

Namecheap DNS allows redirecting to URLs.
This is not actually part of DNS and is achieved by returning HTTP redirect signals to requests (like [301](https://developer.mozilla.org/docs/Web/HTTP/Status/301) or [302](https://developer.mozilla.org/docs/Web/HTTP/Status/302)).
You could do the same by having your webserver redirect requests to particular subdomains.
For example, in NGINX you could use [`rewrite`](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html).

The following URL redirects are configured,

Directing the root domain (`the-turing-way.org`) to the start page

```
@ URL-Redirect https://the-turing-way.start.page
```

Directing `git.the-turing-way.org` to the GitHub organisation

```
git URL-Redirect https://github.com/the-turing-way
```

Directing `slack.the-turing-way.org` to the Slack invitation link

```
slack URL-Redirect <slack invite link>
```

Directing `news.the-turing-way.org` to the newsletter archive

```
news URL-Redirect https://buttondown.email/turingway
```

<!--
### CAA

Secure Socket Layer (SSL) is a protocol for secure communication.
SSL is used to encrypt HTTP traffic in HTTPS.
Almost every time you access a website in a browser will be over HTTPS.
It is important to encrypt web traffic, particularly when you are sending or receiving secret information such as user credentials, bank details and personal data.

A [Certification Authority Authorisation (CAA) record](https://letsencrypt.org/docs/caa/) specifies who can issue a valid SSL certificate for a domain.
This is security best practice as it helps verify that the SSL certificate is valid and was issued by the correct authority.
Currently, [Netlify manages SSL certificates](https://docs.netlify.com/domains-https/https-ssl/#netlify-managed-certificates) for the book.
The certificates are issued by Let's Encrypt.

The following CAA record is configured,

```
book CAA 0 issue "letsencrypt.org"
```

This record only allows Let's Encrypt to issue certificates.
Netlify also suggests [specifying their `accounturi` in the record](https://docs.netlify.com/domains-https/https-ssl/#netlify-managed-certificates) which would further ensure that only Netlify can request new certificates from Let's Encrypt.
However, NameCheap doesn't seem to allow this in CAA records.
-->
