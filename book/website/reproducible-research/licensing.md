(rr-licensing)=
# Licensing

(rr-licensing-prerequisites)=
## Prerequisites

No previous knowledge is needed, this chapter explains how important it is to understand how laws and licensing can affect your project.

(rr-licensing-summary)=
## Summary

> This chapter was written using American English, in which the word **license** is a noun **_and_** a verb.
> With British English, however, **licence** is a noun (as in, _to issue a licence_), while **license** is a verb (as in, _they licensed the event_).  

As with anything else in society, some of what you can and cannot do in software (or hardware) development is determined by the law.
Licensing is therefore an important aspect of sharing/publishing open source projects as it provides clarity for anyone looking to reuse an open source project.
Without licenses in place, anyone who wants to reuse it will be left with legal ambiguity as to the status of using your intellectual property.

Most of the constraints in this particular domain stem from intellectual property laws: laws that make abstract things like designs, stories, or computer programs resemble physical objects by allowing them to be owned.

This chapter aims to give a brief summary of relevant intellectual property laws (enough to be able to read most software licenses), explain free and open source software licensing, and explain how combining software from different sources works from a legal perspective.
It also gives some rules we have worked out to deal with common situations.

## Motivation

Without a license, all rights are with the author of the code, and that means nobody else can use, copy, distribute, or modify the work without consent.
A license gives this consent.
If you do not have a license for your research output, it is effectively unusable by the whole research community.

```{warning}
It is important to consider that copyright, licenses, and patents are all legal concepts.
As such, they are subject to what the law prescribes, which may change over time and space.
This change is not only that one of the laws is changing over time, but it changes over space: depending on jurisdiction and enforcement.
Simply put, different countries have different laws, and follow different procedures with regard to enforcing them.
The content provided here is broadly based on American and European law and legal traditions.
It might not be applicable - might even be contra indicated - or relevant in your particular context.
While things like the Berne Convention have sought to harmonize copyright enforcement, the real world is a messy place.

Good legal advice is timely, specific, and given by an expert; this chapter is none of these.
It was written by an engineer, not by a lawyer, and it is a heavily simplified overview of a very complex field.
The intent is to give you an overview of the basics so that you will know when to check whether something you want to do has potential legal ramifications.
Do not make any important decisions based solely on the contents of this chapter.

So do not take the descriptions provided or viewpoints shared as legal advice, they are not that.
This document is not intended to be used in that manner.
Consult a legal expert to provide actual legal advice for your case.  
```

## Legal terms

To understand what licenses do and how to apply them, it is first important to be familiar with a number of terms.
Terms like copyright, licenses, patents, and trademarks are often used interchangeably (and sometimes incorrectly).
This may lead to confusion as to what exactly is being discussed and what the implications are.
Familiarise yourself with the following terms and follow the links to understand more about them.


```{admonition} Info
**[Copyright](https://europa.eu/youreurope/business/running-business/intellectual-property/copyright/index_en.htm#shortcut-1/):** “When you create an original literary, scientific and artistic work, such as poems, articles, films, songs or sculptures, you are protected by copyright.
Nobody apart from you has the right to make the work public or reproduce it.
” And, “If you create literary, scientific and artistic work, you automatically have copyright protection, which starts from the moment you create your work, so you don't need to go through any formal application process.”

**[License](https://www.oshwa.org/faq/#what-is-a-license/):** “Licensing is a way to give people rights that they wouldn’t otherwise have to use your intellectual property (IP) and, in return, to place restrictions on how they exercise those rights.”

**[Patent](https://www.wipo.int/patents/en/):** “A patent is an exclusive right granted for an invention, which is a product or a process that provides, in general, a new way of doing something, or offers a new technical solution to a problem.
To get a patent, technical information about the invention must be disclosed to the public in a patent application.”
 
**[Trademark](https://euipo.europa.eu/ohimportal/en/trade-mark-definition/)**: "Trade marks are signs used in trade to identify products.
Your trade mark is the symbol your customers use to pick you out.
It distinguishes you from your competitors.
You can protect and build upon your trade mark if you register it."

```

Copyrights are generally what make open source licenses enforceable.
For many open source licenses to be applicable, it is necessary to figure out what parts of the project are actually copyrightable and therefore can be licensed.
 
## Copyleft Versus permissive

In broad terms copyleft licenses impose an obligation of reciprocity on users of any of the licensed items. 
If something is licensed under a copyleft license, then any derivative works need to be shared under the same rights.
Note that it can make things difficult if you want to combine different elements having different copy-left licenses.
Most copyleft licenses fall under open source licenses but not all open source licenses are copyleft.

Copyleft licenses do not prohibit the commercial use of the copyrighted content. 
It only prohibit you to place additional restrictions on the derivative work.

Permissive licenses are those licenses that do not impose the reciprocity requirements.
These licenses allow for the proprietary licensing of derivative works.

A more detailed explanation is given in the chapter on license for software. {ref}`rr-licensing-software-permissive`.


### How and where to add licenses
The choice of license is a personal one based on the goals of the project and the scope for collaboration and growth.
However, structuring the project and adding the appropriate licenses to the different section is much more universal.

The licenses used should generally be featured in the main page where the project is hosted.
For example if GitHub is used, a license file should be added to the topmost layer of the repo along with a Readme file.
The appropriate licenses should also attached to the different elements.
For example the software license should be attached to the code, with the appropriate declaration at the start of any section.

### Limitations
It is important to keep in mind that licenses are only as powerful as the ability to enforce them.
This means that while you can curate and choose the best license that fits your goals, it might entirely be redundant if enforcement is not possible.

The good news is that open source software licenses have been tested across different jurisdictions and have been upheld in many cases, including the USA and Germany.
The full scope of enforceability and effectiveness is still to be explored. 

## Extra notes

It is highly recommended to provide an [SPDX short license identifier](https://spdx.org/licenses/) to make the licensing terms machine-referenceable.