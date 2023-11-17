(rr-licensing-ethical)=
# 'Ethical Source'

The ethical source movement seeks to affirmatively protect specific user rights by curtailing freedom 0, the freedom to use software 'for any purpose' and prohibiting the use of the software for unethical purposes.
Consequently, these licence by the classical definitions of free and open-source software from the FSF and OSI would not be considered free or open-source licences, they do however generally resemble them in the  other three criteria of the definition.
Their merits versus conventional open-source licenses has been the subject of some debate, and their adoption has thus far been relatively limited.

A leading figure in this movement is Coraline Ada Ehmke creator of the [Contributor Covenant](https://www.contributor-covenant.org/), the [Hippocratic License](https://firstdonoharm.dev/), and the founder in 2020 of the [Organisation for Ethical Source](https://ethicalsource.dev/).
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

(rr-licensing-ethical-risks)=
## Potential Risks

In the absence of case law deciding on license enforcement decisions for these licenses it is as yet unknown what (if any) administrative burden may be associated with demonstrating compliance with ethical source and RAIL licences.
Whilst unlikely for any given user of software licenced in this fashion, it is hypothetically possible that such licences could be weaponised by bad actors seeking to impose costs on the entities using the licences, as [has occurred before](https://onezero.medium.com/beware-the-copyleft-trolls-a8b85c66b7eb) with 'exploits' in open licences.
A well-intentioned organisation using tools under such a licence could theoretically be sued for not complying with the terms of these licences and have to pay legal fees and/or incur other expenses associated with demonstrating compliance with the terms, depending on decisions made during the legal process.
These licenses because they impose greater restrictions on their licensees expose a greater attack surface for such bad actors, as compliance with the terms of conventional free software licences is relatively easy.
To comply you can simply share the code, if you have a well managed internal code repositories this should be inexpensive.
(If you have to comb through your git history to remove secrets you inadvisedly committed then things might get more expensive.)
In short they suffer from the same issues as fair-use exemptions, they are not readily administrable.
