(rr-licensing-ip)=
# Intellectual Property (IP)

A basic understanding of IP law is important for anyone producing creative works governed by it, including documentation, software, datasets, graphics and more.
This is true irrespective of the nature of your project: closed commercial projects building on open tooling; commercial projects maintaining an open resource; open community-driven and/or non-profit projects building shared resources.
Each of these may need to make slightly different licensing choices from the beginning of their projects to be compatible with their goals.

Without going into too much detail due to their complexity, in a subchapter, we provide a brief summary of relevant IP laws.

## Copyrights, Patents and Trademarks

IP is an umbrella term that refers to a number of distinct areas of law.
Primarily, these three areas are relevant in research and data science:

- [Copyrights](https://europa.eu/youreurope/business/running-business/intellectual-property/copyright/index_en.htm#shortcut-1/)
- [Patents](https://www.wipo.int/patents/en/)
- [Trademarks](https://euipo.europa.eu/ohimportal/en/trade-mark-definition/)

What these have in common is the attempt to extend property rights to intangible goods, meaning their use by others can be prevented or [licensed](https://www.oshwa.org/faq/#what-is-a-license/).
Governments with such laws effectively create a limited grant of monopoly over these goods for their creators and other holders of these rights.
This is generally done with the ostensible intent to incentivise the creation and improvement of such goods, but can in practice result in perverse incentives which fail to do so.

This chapter is intended to educate people on the basic concepts of Licensing. 
Please do not take the descriptions provided or viewpoints shared as legal advice; they are not that.
Consult your librarian and a legal expert to provide actual legal advice for your case.

```{warning}
It is important to consider that copyright, licenses, and patents are all legal concepts.
As such, they are subject to what the law prescribes, which may change over time and space.
Simply put, different countries have different laws and follow different procedures with regard to enforcing them.
The content provided here is broadly based on American and European law and legal traditions.
It might not be applicable - might even be contraindicated - or relevant in your particular context.
However, most nations are signatories to international treaty agreements which somewhat harmonise these laws, notably the Berne Convention, the [TRIPS Agreement](https://www.wto.org/english/docs_e/legal_e/27-trips_01_e.htm), and others under the [World IP Organisation (WIPO)](https://www.wipo.int/portal/en/index.html).
Whilst international efforts have sought to harmonise copyright enforcement, the real world is a messy place.
```

Perhaps the most relevant part of IP law for software, data and other creative works is copyright.
We will dispense quickly with patents and trademarks here, so we can move on to the main topic of copyright.

(rr-licensing-patents)=
## Patents

The most important difference between patent and copyright to be immediately aware of is that by default, all rights are retained by the author on works made public under copyright, whereas patents must be registered before their content is publicly disclosed.
Thus, if you want to patent something, you must do so prior to sharing it publicly.
The precise details of what constitutes a disclosure and the strictness of the application of this rule can vary by jurisdiction.

Patents on processes and software rather than specific inventions are a matter of contention in US law and explicitly not recognised in EU law (at the time of writing).
Unlike copyright, you generally have to pay to register and maintain a patent.
You must also do so in each jurisdiction in which you want this patent to apply, though some have reciprocal agreements for recognising patents from other jurisdictions.
To ensure that patents held by the authors of software do not impact on the freedom to use and distribute  open software, some licenses specifically include permission to use any applicable patents (for example, section 3 of the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html)), though this cannot protect against patents held by 3rd parties.

<!-- citations needed -->
<!-- when should you patent something and when not?-->
<!-- IP ownership employment & institutions -->
<!-- UK patent info https://www.gov.uk/topic/intellectual-property/patents -->
<!-- UK has a related but distinct concept of a 'registered design' https://www.gov.uk/topic/intellectual-property/designs -->

(rr-licensing-trademarks)=
## Trademarks

Trademarks are a brand, symbol, or identifying mark associated with a project, product or service.
Trademarks differ from copyrights & patents in that their primary function is consumer protection.
They prevent bad actors from impersonating recognisable brands and deceiving consumers into purchasing products that are not being offered by who they think they are.
They, like patents, must also be registered, but unlike patents, this can be done after they have been made public.

Registering a trademark generally comes with an administrative fee, but it is not as costly as maintaining a patent.
Trademarks generally only apply within a specific sector, as people are unlikely to confuse brands which do completely different things.
They can be relevant in the context of the name and logo of a software project, especially when a project changes hands or is forked, in which case the fork may not be able to use the original name of the project even if that project is no longer maintained.
Open source projects not associated with a company which have trademarks may have these held by a legal entity, such as a non-profit, through which they might also take donations and pay for project infrastructure.
It can be valuable for open source projects to register for trademarks as their work can easily be cloned, modified and re-distributed with ill intent.
Examples of modified open source tools distributed with malware added have been documented, and trademark enforcement could, in some cases, help to prevent or deter this.
Nextcloud, for example, has a [comprehensive guide to the use of their marks](https://nextcloud.com/trademarks/) with excellent explanations for the restrictions that they place on their use.
<!--A subtler case is unofficial packages which charge a high rate for the software which could be downloaded elsewhere for free -->

<!-- citations needed -->
<!-- UK trade mark info https://www.gov.uk/topic/intellectual-property/trade-marks -->

(rr-licensing-copyright)=
## Copyright

<!-- UK copyright info https://www.gov.uk/topic/intellectual-property/copyright -->

By default, if you make a work publicly available, you retain the copyright to that work and all rights that this gives you over it.
Anyone wishing to re-use that work must seek to license the right to do so from you, or open themselves to the possibility of a lawsuit for infringing on your copyright.
Irrespective of how you choose to license your work, however, there are some generally accepted exceptions to the protections of copyright that permit the re-use of works (or parts of works) without the consent of the copyright holder, under certain circumstances.
These are known as 'fair use' or 'fair dealing' exceptions.
Under the 'fair use' standard originating in the USA, the following criteria are considered on a case-by-case basis to decide if a use constitutes an infringement of copyright:

> From [17 U.S.C § 107](https://www.law.cornell.edu/uscode/text/17/107)
> - the purpose and character of the use, including whether such use is of a commercial nature or is for nonprofit educational purposes;
> - the nature of the copyrighted work;
> - the amount and substantiality of the portion used in relation to the copyrighted work as a whole; and
> - the effect of the use upon the potential market for or value of the copyrighted work.

The 'fair dealing' standard, originating in British law, generally includes more explicitly enumerated exceptions but with similar intent.
Notably disputes over what constitutes fair-use are not easily administrable and can require protracted court proceedings to settle definitively.
<!-- citations needed -->

For anyone wishing to circulate their work and grant others the right to re-use, remix, or re-distribute that work free of charge, coming to individual licensing arrangements with everyone who might want to do this is obviously impractical.
To address this, there exist numerous pre-made 'off-the-self' licenses that you can apply to your work.
Which of these you choose shapes how and under what circumstances others are permitted to re-use your work without infringing on your copyright.

Pre-made licenses exist that are tailored to the differences between different types of works.
For example, there are licenses intended to be used for software and licenses intended to be used for other creative works such as images, prose (text), as well as hardware & designs.

In addition, there are now licenses tailored for machine learning or artificial intelligence models as these are comprised of several parts, including: training data, code, and model weights.
Each of these parts may be licensed differently, and there is even some dispute as to whether model weights are subject to copyright at all under current law.
<!-- citations needed -->
This is an area which is likely to see (by legal standards) rapid changes in the near future, given recent developments in the commercialisation of AI/ML models.

There are some general principles which apply to licenses across the different types of entity that they try to license.
Licenses can generally be placed on a spectrum from proprietary, through permissive, to 'share alike' or 'copyleft' (the opposite of copyright).
This spectrum is something of an oversimplification, and there are some extensions and caveats we'll get to later.
