(ch-infrastructure-dns)=
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

(summary-of-records)=
## Summary of Records

There are many DNS record types.
The following table gives a simple explanation of some of the more common ones.

| Record      | Purpose                                                               |
| --------    | --------------------------------------------------------------------- |
| A           | Directs a hostname to an IPv4 address                                 |
| AAAA        | The same as A but for IPv6                                            |
| CNAME       | Makes the hostname an alias for another                               |
| ALIAS/ANAME | Similar to a CNAME record, but can be used at the root domain         |
| MX          | Points to an email server for the domain                              |
| TXT         | Arbitrary text, often used to configure SSL or email authentication   |
| NS          | Delegates DNS to a different nameserver                               |

## Looking at DNS Records

You can inspect DNS records using the `dig` or `nslookup` commands.

The `dig` command line can be formatted like

```console
dig [@DNS-server] [domain] [record-type]
```

For example, we can check the A record for `book.the-turing-way.org` using Google's DNS server (`8.8.8.8`) like this

```console
$ dig @8.8.8.8 book.the-turing-way.org A

; <<>> DiG 9.10.6 <<>> @8.8.8.8 book.the-turing-way.org A
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28689
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;book.the-turing-way.org.       IN      A

;; ANSWER SECTION:
book.the-turing-way.org. 300    IN      A       99.83.231.61
book.the-turing-way.org. 300    IN      A       75.2.60.5

;; Query time: 16 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Tue May 20 11:27:38 BST 2025
;; MSG SIZE  rcvd: 84
```

We can see in the answer section that there are two A records for `book.the-turing-way.org` pointing to two IP addresses where the book is served.
This is actually an ALIAS record, but these records resolve to A records when you query them.
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

### ALIAS records

We use an ALIAS record for _The Turing Way_ book at `book.the-turing-way.org`.
This is an alias for the Netlify load balancer, where the book is currently hosted.
If the book is moved to another hosting provider the record can be updated to point to the new host.
That way, the book will _always_ be accessible at `book.the-turing-way.org` no matter how or where it is hosted.

```
book ALIAS apex-loadbalancer.netlify.com.
```

We also redirect the root domain, `the-turing-way.org`, to the Netlify load balancer.
This is a feature of ALIAS records that wouldn't be possible with CNAME.
We do this so that we can [redirect subdomains](#ch-infrastructure-redirects).

```
@ ALIAS apex-loadbalancer.netlify.com.
```

### CNAME records

As explained in [](#summary-of-records) CNAME records are aliases.
We use a CNAME record for `www` so that looking up `www.the-turing-way.org` or `www.book.the-turing-way.org` will be treated the same as the non-www domains.
`www.` has no special meaning and is just a normal subdomain.
However, historically it was commonly used for websites (as opposed to other services like FTP) so many will still expect a site to be served there.

```
www CNAME the-turing-way.org.
www.book CNAME book.the-turing-way.org.
```

We also have a set of CNAME records to route "helper" subdomains to our webserver so we can [redirect them to community resources](#ch-infrastructure-redirects-helpers).

```
git CNAME the-turing-way.org.
news CNAME the-turing-way.org.
slack CNAME the-turing-way.org.
```

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
