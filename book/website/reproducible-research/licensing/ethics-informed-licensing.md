(rr-licensing-ethics)=
# Ethics-informed Licensing

'Intellectual property (IP)' law is a complex subject, however some understanding of it is important for anyone producing creative works governed by it including; software, datasets, graphics and more.
This is true when producing a work as a contribution to open culture or as a potential commercial venture. Decisions about licencing made at the inception of a project can have long-lasting and significant ramifications.
This section is framed in terms of ethics because of these ramifications, the choices that you make about how your work is licenced shape who can and cannot legally use your work and for what purpose.
It aims to be informative about the implications of licencing choices for the use of your work but not to prescribe a specific ethic, as there are divergent schools of thought on the ethics of different licencing choices.

Intellectual property is an umbrella term that refers to a number of distinct areas of law, primarily these three:

- Copyright
- Patent
- Trademark

What these have in common is the attempt to extend property rights to intangible goods.

```{note}
There are differences between countries laws on these points and it is worth paying attentention to the particulars of the the law in the juristications where you are working but most nations are signatories to international treaty agreements which somewhat harmonise these laws notably the [TRIPS Agreement](https://www.wto.org/english/docs_e/legal_e/27-trips_01_e.htm).
```

Perhaps the most relevant for software, data and other creative works is copyright.
We will dispense quickly with patents and trademarks here, so we can move on to the main topic of copyright.

(rr-licensing-ethics-patents)=
## Patents

The most important difference between patent and copyright to be immediately aware of is that by default all rights are retained by the author on works made public under copyright, whereas patents must be registered before their content is publicly disclosed.
Thus, if you want to patent something, you must do so prior to sharing it publicly.
The precise details of what constitutes a disclosure and the strictness of the application of this rule can vary by jurisdiction.
Patents on processes and software rather than specific inventions are a matter of contention in US law and explicitly not recognised in EU law (at time of writing).
Unlike copyright, you generally have to pay to register and maintain a patent.
You must also do so in each jurisdiction in which you want this patent to apply, though some have reciprocal agreements for recognising patents from other jurisdictions.
To ensure that patents held by the authors of software do not impact on the freedom to use and distribute  open software, some licences specifically include permission to use any applicable patents (for example [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html), see section 3), though this cannot protect against patents held by 3rd parties.

<!-- citations needed -->
<!-- when should you patent something and when not?-->
<!-- IP ownership employment & institutions -->
<!-- UK patent info https://www.gov.uk/topic/intellectual-property/patents -->
<!-- UK has a related but distinct concept of a 'registered design' https://www.gov.uk/topic/intellectual-property/designs -->

(rr-licensing-ethics-trademarks)=
## Trademarks

Trademarks are a brand, symbol, or identifying mark associated with a project, product or service.
They, like patents, must also be registered, but unlike patents, this can be done after they have been made public.
Registering a trademark generally comes with an administrative fee, but is not as costly as maintaining a patent.
They are generally legal protected to help prevent impersonation.
Consequently, trademarks generally only apply within a specific sector, as people are unlikely to confuse brands which do completely different things.
They can be relevant in the context of the name and logo of a software project, especially when a project changes hands or is forked, in which case the fork may not be able to use the original name of the project even if that project is no longer maintained.
Open-source projects not associated with a company which have trademarks may have these held by a legal entity such as a non-profit, through which they might also take donations and pay for project infrastructure.

<!-- citations needed -->
<!-- UK trade mark info https://www.gov.uk/topic/intellectual-property/trade-marks -->

(rr-licensing-ethics-copyright)=
## Copyright

<!-- UK copyright info https://www.gov.uk/topic/intellectual-property/copyright -->

By default, if you make a work publicly available, you retain the copyright to that work and all rights that this gives you over it.
Anyone wishing to re-use that work must seek to licence the right to do so from you, or open themselves to the possibility of a lawsuit for infringing on your copyright.
Irrespective of how you choose to licence your work, however, there are some generally accepted exceptions to the protections of copyright that permit the re-use of works (or parts of works) without the consent of the copyright holder, under certain circumstances.
These are known as 'fair use' or 'fair dealing' exceptions.
Under the 'fair use' standard originating in the USA, the following criteria are considered on a case-by-case basis to decide if a use constitutes an infringement of copyright:

> From [17 U.S.C § 107](https://www.law.cornell.edu/uscode/text/17/107)
> - the purpose and character of the use, including whether such use is of a commercial nature or is for nonprofit educational purposes;
> - the nature of the copyrighted work;
> - the amount and substantiality of the portion used in relation to the copyrighted work as a whole; and
> - the effect of the use upon the potential market for or value of the copyrighted work.

The 'fair dealing' standard, originating in British law, generally includes more explicitly enumerated exceptions but with similar intent. <!-- citations needed -->

For anyone wishing to circulate their work and grant others the right to re-use, remix, or re-distribute that work free of charge, coming to individual licensing arrangements with everyone who might want to do this is obviously impractical.
To address this, there exist numerous pre-made 'off-the-self' licenses that you can apply to your work.
Which of these you choose shapes how and under what circumstances others are permitted to re-use your work without infringing on your copyright.

Pre-made Licences exist that are tailored to the differences between different types of works.
For example, there are licences intended to be used for software and licences intended to be used for other creative works such as images & prose (text).

In addition, there are now licences tailored for machine learning / artificial intelligence models as these are comprised of several parts, including: training data, code, and model weights.
Each of these parts may be licenced differently, and there is even some dispute as to whether model weights are subject to copyright at all under current law.
<!-- citations needed -->
This is an area which is likely to see (by legal standards) rapid changes in the near future, given recent developments in the commercialisation of ML models.

There are some general principles which apply to licences across the different types of entity that they try to licence.
Licences can generally be placed on a spectrum from proprietary, through permissive, to 'share alike' or 'copy-left' (the opposite of copyright).
This spectrum is something of an oversimplification, and there are some extensions and caveats we'll get to later.

Permissively licenced things can generally be used by anyone for any purpose.
A popular minimal example of this for software is known as the [MIT licence](https://mit-license.org/), for other works, [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) the 'public domain' licence.
Copy-left licences attempt to ensure that any re-distributions or derived works also remain 'free', the canonical example is the [GPL](https://www.gnu.org/licenses/gpl-3.0.html).
Unlike permissively licenced content, which can be modified and redistributed under a different licence, including as a part of a closed and/or for profit project.

(rr-licensing-ethics-copyright-free)=
### What is 'free' software?

The concept of copy-left licences and their first example, the GPL, originated with Richard Stallman, who founded the free-software foundation (FSF) in 1985.
<!-- citations needed -->

The four fundamental freedoms of free/libre* software:

- Freedom 0: The freedom to run the program as you wish, for any purpose.
- Freedom 1: The freedom to study how the program works, and change it, so it does your computing as you wish. Access to the source code is a precondition for this.
- Freedom 2: The freedom to redistribute copies so you can help others in your community.
- Freedom 3: The freedom to distribute copies of your modified versions to others.
  By doing this, you can give the whole community a chance to benefit from your changes.
  Access to the source code is a precondition for this.

Other influential definitions of free and open-source software include: The Debian project's [Debian Free Software Guidelines (DFSG)](https://www.debian.org/social_contract#guidelines), and the open source initiative (OSI)'s [Open Source Definition](https://opensource.org/osd/).

```{note}
The word 'free' in english does not distinguish something being moneratily free 'gratis' from politically free 'libre'.
This is often sumarised along the lines of: "free as in speech, not necessarily free as in beer"
Thus the phrase 'libre software' is sometimes encountered in english to succinctly distinguish the concept of software which respects your liberty from software which is finacially free to use ('gratis').
It is also common to encounter the acronyms FOSS (Free and open-source software) and FLOSS (Free/libre and open source software)
```

The FSF contends that all software should respect these freedoms and that all software which does not respect these freedoms creates an asymmetric relationship between the users and developers of that software which can readily be abused by the developers to exploit their users.
If developers are bad stewards of a free software projects, the friction for replacing them is low, as all of the work put into the software does not need to be re-done.
A 'fork' of the project can be made, developed and maintained by different developers whom the community of users deem a better steward.
This is not true of proprietary projects where the developers own the rights to the code and thus cannot be readily replaced by the community of users if they begin to abuse these users who are now held captive by switching costs.

Copy-left licences are an attempt to ensure that software remains effectively under community ownership and cannot be used to make proprietary software which does not respect the four freedoms and may thus result in the abuse of its users.
To attempt to achieve this goal, copy-left software requires that when distributing copy-left software or derived works that you do so under the same terms as the original licence.
Creative commons 'share-alike' licences attempt the same thing for other content.

Copy-left licences do not prohibit commercial use of code, indeed numerous companies exist which develop copy-left projects and sell support services for deploying those projects instead of using proprietary licences which would incentivise an unhealthy relationship with their users, [Nextcloud](https://nextcloud.com/) is an excellent example.
Nextcloud makes use of the [AGPL v3.0](https://www.fsf.org/bulletin/2021/fall/the-fundamentals-of-the-agplv3) a license which extends the protections of the GPL to software used over a network.
It gives users who interact with this software over a network, for example by using a web service, rather than run it on their own computers, the right to access a copy of the source code; which they are further free to modify and distribute as is usual for the GPL.

Within copy-left licenses, there are 'strong' and 'weak' copy-left licences.
'Strong' copy-left licenses require that combined works which contain them as a library also carry the same license but weak copy-left licenses permit their re-distribution as a library within a combined work under a different license.
We will define derived and combined works in the section on licence compatibility where the detailed implications of the distinctions between strong & weak copyleft, and permissive licencing are explored in more practical detail.

<table>
    <thead>
        <tr>
            <th colspan="3">Free</th>
            <th rowspan="3">Proprietary</th>
        </tr>
        <tr>
            <th colspan="2">Copyleft</th>
            <th rowspan="2">Permissive</th>
        </tr>
        <tr>
            <th>Strong</th>
            <th>Weak</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>GPL<sup>1</sup> CDDL<sup>2</sup></td>
        <td>LGPL<sup>3</sup> MPL<sup>4</sup></td>
        <td>BSD<sup>5</sup> MIT<sup>6</sup> Apache</td>
            <td>Research Only: No&nbsp;copying, No&nbsp;modification</td>
        </tr>
    </tbody>
    <caption>
      <div class="footnote">
        <sup>1</sup>GPL: GNU General Public License <sup>2</sup>CDDL: Common Development and Distribution License <sup>3</sup>LGPL: GNU Lesser General Public License <sup>4</sup> MPL: Mozilla Public License <sup>5</sup> BSD: Berkeley Software Distribution <sup>6</sup> MIT: Massachusetts Institute of Technology
      </div>
      Licenses can either be Free or Proprietary, with Free Licenses further classified as Copyleft or Permissive.
    </caption>
</table>


(rr-licensing-ethics-copyright-responsible)=
### What are 'Ethical source' and 'Responsible AI' Licenses?

Both 'Ethical source' & 'Responsible AI' Licenses seek to place restrictions on the uses to which the licensees can, but the software or machine learning system to prohibit their use for unethical activities.

(rr-licensing-ethics-copyright-responsible-ethical)=
#### 'Ethical Source'

The ethical source movement seeks to affirmatively protect specific user rights by curtailing freedom 0, the freedom to use software 'for any purpose' and prohibiting the use of the software for unethical purposes.
Consequently, these licence by the classical definitions of free and open-source software from the FSF and OSI would not be considered free or open-source licences, they do however generally resemble them in the  other three criteria of the definition.
Their merits versus conventional open-source licenses has been the subject of some debate, and their adoption has thus far been relatively limited.

A leading figure in this movement is Coraline Ada Ehmke creator of the [contributor covenant](https://www.contributor-covenant.org/), the [Hippocratic License](https://firstdonoharm.dev/), and the founder in 2020 of the [organisation for ethical source](https://ethicalsource.dev/).
In the words of its advocates, [Ethical Source](https://ethicalsource.dev/) was created to "empower developers, giving us the freedom and agency to ensure that our work is being used for social good and in service of human rights."
Motivated by the growing use of open source software for technologies such as mass surveillance and racial profiling, the movement aims to reduce this "misuse" of open-source software.

Ethical Source extends upon the principles of open source to provide developers additional means to ensure their work is used for applications aligned with ethical values important to them like:
- Advocating for workers' rights and human rights
- Ensuring protections against violence and discrimination
- Protecting privacy

A list of Ethical Licenses and their targeted applications can be found on the [Ethical Source website](https://ethicalsource.dev/licenses/).
The core Hippocratic licence, for example, prohibits a variety of human rights abuses and mandates equal pay for equal work.
It can be further extended using [their licence building tool](https://firstdonoharm.dev/build/) with modules covering:

- Fossil Fuel Divestment
- Ecocide
- Extractive Industries 
- Boycott / Divestment / Sanctions
- Taliban
- Myanmar
- Xinjiang Uygur Autonomous Region
- US Tariff Act
- Mass Surveillance
- Military Activities
- Law Enforcement
- Media
- Social Auditing
- Workers on Board of Directors
- Supply Chain Transparency
- Copyleft

Licensees are given 30 days upon notification of a violation or harm to remedy them before the license is terminated.
The potential difficulty of demonstrating compliance with these terms and of bringing effective legal action against any party not complying with them has attracted some skepticism about the effectiveness of this approach.

(rr-licensing-ethics-copyright-responsible-rail)=
#### Responsible AI Licenses

These same principles developed in 'ethical source' apply to the 'Open' variants of the licences from RAIL (Responsible AI Licences).
In that, they are attempting to place restrictions on the uses to which licensees can put the thing being licenced.
Traditional software has many of the same concerns which affect machine learning models, and indeed also often contain assets such as images which may be licenced differently from software with which they are bundled.
The primary differences being governance of data used in training the models (see: Data Governance for the Machine Learning Pipeline) and the lack of interpretability of the decisions of many ML systems, though this latter point can also be an issue for conventional systems if they are closed.
RAIL provides a succinct way of expressing licences for combined machine learning systems which include, the data on which they were trained, the software used to specify this, the model weights generated as a result and the applications which provide an interface to the resulting model.

RAIL provides these definitions of the modifiers that can be applied to their licenses:

> - **D**ata: The dataset(s) used to pretrain or train an AI Model.
> - **A**pplication/service: Any executable software code or application, including API-based remote access to software.
> - **M**odel: Machine-learning based assemblies (including checkpoints), consisting of learnt weights and parameters (including optimizer states), corresponding to the model architecture.
> - **S**ource: The source code and scripts associated with the AI system.

Therefore:

> - RAIL-D:  RAIL License includes Use Restrictions only applied to the data
> - RAIL-A:  RAIL License includes Use Restrictions only applied to the application/executable
> - RAIL-M:  RAIL License includes Use Restrictions only applied to the model
> - RAIL-S:  RAIL License includes Use Restrictions only applied to the source code

These are the restrictions placed on the licencee of a RAIL-M license:

> You agree not to use the Model or Derivatives of the Model:
> 
> 	**a.** In any way that violates any applicable national, federal, state, local or international law or regulation;
> 
> 	**b.** For the purpose of exploiting, harming or attempting to exploit or harm minors in any way;
> 
> 	**c.** To generate or disseminate verifiably false information and/or content with the purpose of harming others;
> 
> 	**d.** To generate or disseminate personal identifiable information that can be used to harm an individual;
> 
> 	**e.** To generate or disseminate information and/or content (for example images, code, posts, articles), and place the information and/or content in any context (for example bot generating tweets) without expressly and intelligibly disclaiming that the information and/or content is machine generated;
> 
> 	**f.** To defame, disparage or otherwise harass others;
> 
> 	**g.** To impersonate or attempt to impersonate (for example deepfakes) others without their consent;
> 
> 	**h.** For fully automated decision making that adversely impacts an individual’s legal rights or otherwise creates or modifies a binding, enforceable obligation;
> 
> 	**i.** For any use intended to or which has the effect of discriminating against or harming individuals or groups based on online or offline social behavior or known or predicted personal or personality characteristics;
> 
> 	**j.** To exploit any of the vulnerabilities of a specific group of persons based on their age, social, physical or mental characteristics, in order to materially distort the behavior of a person pertaining to that group in a manner that causes or is likely to cause that person or another person physical or psychological harm;
> 
> 	**k.** For any use intended to or which has the effect of discriminating against individuals or groups based on legally protected characteristics or categories;
> 
> 	**l.** To provide medical advice and medical results interpretation;
> 
> 	**m.** To generate or disseminate information for the purpose to be used for administration of justice, law enforcement, immigration or asylum processes, such as predicting an individual will commit fraud/crime commitment (for example by text profiling, drawing causal relationships between assertions made in documents, indiscriminate and arbitrarily-targeted use).

RAIL-S licences carry their [Software Usage Restrictions](https://www.licenses.ai/source-code-license).

This flow diagram guides you through the choice of a suitable RAIL:

![source: https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses](https://images.squarespace-cdn.com/content/v1/5c2a6d5c45776e85d1482a7e/381a69a4-28d9-4b6a-be5c-516330e7d8b9/diagram.png)
 <!-- alt text needed! -->

RAIL license can be used in closed applications and Open RAIL licenses are permissive with respect to the model and software but not with respect to the usage restrictions.
Note that there is not an effective equivalent to a copyleft version of the Open RAIL licences.
None of them require that the software or models contained in them also be similarly licenced in derived works, only that the usage restrictions be retained.
This could be a useful extension to these license adding an 'L' for copy**L**eft and including a clause making any software, model weights, or source code in the bundle strong copyleft.

(rr-licensing-ethics-copyright-responsible-risks)=
#### Potential Risks

In the absence of case law deciding on license enforcement decisions for these licenses it is as yet unknown what (if any) administrative burden may be associated with demonstrating compliance with ethical source and RAIL licences.
Whilst unlikely for any given user of software licenced in this fashion, it is hypothetically possible that such licences could be weaponised by bad actors seeking to impose costs on the entities using the licences, as [has occurred before](https://onezero.medium.com/beware-the-copyleft-trolls-a8b85c66b7eb) with 'exploits' in open licences.
A well-intentioned organisation using tools under such a licence could theoretically be sued for not complying with the terms of these licences and have to pay legal fees and/or incur other expenses associated with demonstrating compliance with the terms, depending on decisions made during the legal process.
These licenses because they impose greater restrictions on their licensees expose a greater attack surface for such bad actors, as compliance with the terms of conventional free software licences is relatively easy.
To comply you can simply share the code, if you have a well managed internal code repositories this should be inexpensive, if you have to comb through your git history to remove secrets you inadvisedly committed then things might get more expensive.

(rr-licensing-ethics-copyright-finding)=
### Where to find open licenses for different types of work

- Code
    - The [Open Source Initiaitive (OSI)](https://opensource.org/licenses/) maintains a list of [approved Licences](https://opensource.org/licenses/) open-source licences
    - [Free Software Foundation](https://www.fsf.org/) maintains a [list of GPL-Compatible Free Software Licenses](https://www.gnu.org/licenses/license-list.html#SoftwareLicenses)
        - [GNU/FSF recomendations](https://www.gnu.org/licenses/license-recommendations.html)
    - [choosealicense.com](https://choosealicense.com/) provides a tool to guide you through the license choice project.
    - [Organisation for ethical source](https://ethicalsource.dev/) maintains a list of [ethical source licenses](https://ethicalsource.dev/licenses/)
- Prose, Images, Audio, Video, Datasets, etcetera
    - [Creative Commons (CC)](https://creativecommons.org/)
        - [Creative Commons License Chooser](https://creativecommons.org/choose/)
          ![figure from https://libguides.gwu.edu/opentextbooks/creative_commons](https://s3.amazonaws.com/libapps/accounts/22603/images/CC-License-Chart.png)
          <!-- alt text needed! -->
- Machine Learning (ML) / artificial inteligence (AI) systems
    - Creative commons and Software licences can be applied to different parts of ML/AI systems, CC to training data and weights, software licences to code used in training / depoyment.
    - [Responsible AI Licenses (RAIL)](https://www.licenses.ai/)

(rr-licensing-ethics-copyright-enforcement)=
### Licencing enforcement

There have been a number of successful legal cases that have been brought in defence of the terms of copyleft licenses obliging the parties abusing the terms of these licenses to appropriately release their code.
But this can be hard to discover, as it is not immediately obvious if copyleft code has been used from looking at a black box proprietary end product.

<!-- citations needed -->

Organisations which take legal action in defence of free software, and which can provide information and resources for anyone else seeking to do the same, include:

- [Software Freedom concervancy](https://sfconservancy.org/)
- [Software Freedom Law Centre](https://softwarefreedom.org/)
- [FSF - licensing and compliance](https://www.fsf.org/licensing/)
- [Free Software Foundation Europe (FSFe) - legal work](https://fsfe.org/activities/legal.en.html)
- [Electronic Fontiers Foundation - legal cases](https://www.eff.org/cases)

(rr-licensing-ethics-copyright-wellcoming)=
### Being a wellcoming space to those who do not want to use proprietary software

Some people avoid using non-free software on principle to the greatest extent that they can.
It is highly impractical to completely avoid all non-free software in the world today, so many have compromises and workarounds.
This might include measures such as only running proprietary code in a sandboxed environment like a web browser, but this can impose an additional burden on these users.
This is especially true if proprietary tools do not offer first class features in browsers or support free software operating systems like Linux.
Consequently, the choice to use open infrastructure is important if you want to be inclusive of people who adhere strongly to the free software ethos and consider being asked to use non-free software as an imposition.
A small minority of people simply will not participate if doing so requires that they use non-free software.

(rr-licensing-ethics-copyright-edge)=
### Pertinant edge cases

(rr-licensing-ethics-copyright-edge-clas)=
#### Contributor Licence Agreements

The holder of the copyright on a copy-left project can still re-licence that project or dual-licence that project under a different licence, for example to grant exclusive rights to commercially distribute that project with proprietary extensions or to make future versions proprietary.
In a large community developed project, this would require the consent of all contributors, as they each own the copyright to their contributions.
To get around this, some copy-left projects developed by companies that commercially licence proprietary extensions to these projects ask their contributors to sign contributor licence agreements (CLAs) which assigns the contributor's copyright to the company so that they can legally dual-licence the project.

(rr-licensing-ethics-copyright-edge-available)=
#### 'Source Available'

Under a proprietary license the code is generally not made public.
Some projects share their code but do not licence its re-use, modification or redistribution. This is known as being 'source available' or 'shared-source', the [Vivaldi](https://vivaldi.com/) web browser is an example of such a project.

## Further reading

- General Reading on copyright, its potential reforms, and history of application in software
    - [Free as in freedom 2.0](https://archive.org/details/faif-2.0/mode/2up)
    - [What if we could reimagine copyright?](https://www.jstor.org/stable/j.ctt1q1crjg)
    - [Chokepoint capitalism](https://craphound.com/chokepoint/2022/09/27/twitch-does-a-chokepoint-capitalism/)
    - [Intellectual Property & Monopoly Capitalism]( https://crashcourseeconomics.org/webinar/intellectual-property-and-monopoly-capitalism)
- Tools
    -[Reuse](https://reuse.software/)
- Relevant Legal Materials
	- International treaties impacting most nation state level IP law
		- [Berne Convention for the Protection of Literary and Artistic Works](https://www.wipo.int/treaties/en/ip/berne/)
		- [TRIPS](https://www.wto.org/english/docs_e/legal_e/27-trips_01_e.htm)
	- Statutes / Directives
		- US
			- [DMCA](https://www.congress.gov/bill/105th-congress/house-bill/2281)

<!-- additional statutes needed, add EU directives -->
