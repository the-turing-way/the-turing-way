(rr-licensing-ethical)=
# 'Ethical Source'

The ethical source movement seeks to affirmatively protect specific user rights by curtailing freedom 0, the freedom to use software 'for any purpose' and prohibiting the use of the software for unethical purposes.
Consequently, these licenses by the classical definitions of free and open source software from the FSF and OSI would not be considered free or open source licenses.
Ethical Source licenses do generally resemble conventional free/libre and open source in the other three criteria of the definition.
Their merits versus conventional open source licenses has been the subject of some debate, and their adoption has thus far been relatively limited.

A leading figure in this movement is Coraline Ada Ehmke creator of the [Contributor Covenant](https://www.contributor-covenant.org/), the [Hippocratic License](https://firstdonoharm.dev/), and the founder in 2020 of the [Organisation for Ethical Source](https://ethicalsource.dev/).
In the words of its advocates, [Ethical Source](https://ethicalsource.dev/) was created to "empower developers, giving us the freedom and agency to ensure that our work is being used for social good and in service of human rights."
Motivated by the growing use of open source software for technologies such as mass surveillance and racial profiling, the movement aims to reduce this "misuse" of open source software.

Ethical Source extends upon the principles of open source to provide developers additional means to ensure their work is used for applications aligned with ethical values important to them like:

- Advocating for workers' rights and human rights
- Ensuring protections against violence and discrimination
- Protecting privacy

A list of Ethical Licenses and their targeted applications can be found on the [Ethical Source website](https://ethicalsource.dev/licenses/).
The core Hippocratic license, for example, prohibits a variety of human rights abuses and mandates equal pay for equal work.
It can be further extended using [their license building tool](https://firstdonoharm.dev/build/) with modules covering:

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

Whilst many potential violaters of these license terms lie outside the jurisdictional reach of courts which might enforce them, many also do business with partners which might reside within the reach of these courts.
If for example Thermo Fisher Scientific had been using a library licensed under the Hippocratic license, especially one using the Xinjiang Uygur Autonomous Region module, in the software on their sequencing instruments they might have opened themselves up to liability when [selling DNA testing equipment to police departements in Xinjiang and Tibet](https://theintercept.com/2022/09/13/china-tibet-police-dna-thermo-fisher/) legal action against them in the US courts is more plausible than legal action against the CCP.
The challenge might then be one of persuading such companies to expose themselves to the liabilities associated with using software with these licenses.

(rr-licensing-ethical-risks)=
## Potential Risks

In the absence of case law deciding on license enforcement decisions for these licenses it is as yet unknown what (if any) administrative burden may be associated with demonstrating compliance with ethical source and RAIL licenses.
Whilst unlikely for any given user of software licensed in this fashion, it is hypothetically possible that such licenses could be weaponised by bad actors seeking to impose costs on the entities using the licenses, as [has occurred before](https://onezero.medium.com/beware-the-copyleft-trolls-a8b85c66b7eb) with 'exploits' in open licenses.
A well-intentioned organisation using tools under such a license could theoretically be sued for not complying with the terms of these licenses and have to pay legal fees and/or incur other expenses associated with demonstrating compliance with the terms, depending on decisions made during the legal process.
These licenses, because they impose greater restrictions on their licensees, expose a greater attack surface for such bad actors.
Compliance with the terms of conventional free software licenses is relatively easy to demonstrate.
To comply you can simply share the code, if you have a well managed internal code repositories this should be inexpensive.
(If you have to comb through your git history to remove secrets you inadvisedly committed then things might get more expensive.)
Compliance with the terms of an ethical source license may however be considerably more complex and expensive to demonstrate definitively.
Such cost are less likely to be weaponised against indiviual end users of software licensed in this fashion but rather institutions which depend on software on this kind.
Institutions which are either small enough have their finances serioulsy damaged or their operation immpeeded, or which are large enough to extract a monetary settlement of some kind, would be possible targets.
In short they suffer from the same issues as fair-use exemptions, they are not readily administrable.

Even if it is not the intent of proponents of ethical source some parties may seek to use technical enforcement measures, also known as digital rights/restrictions management (DRM), to enforce the terms of ethical source licenses.
Returning to the earlier example, if sequencing instruments being used for unlicensed purposes could be remotely disabled by their manufactures this raises some questions.
What about the use of these machines with 3rd party or unlicensed components in places which cannot afford 'official' components but which need to use these machines for public health reasons?
Property rights, the 'doctrine of first sale', and 'right(s) to repair' would conventionally protect the osstensible owners of equipment from such an imposition by its original manufacturer.
These rights come at the expense of being able to use technical enforcement measures to police the misuse of these systems but with the bennefit of protecting the freedoms to do as you will with your own property.
Technical enforcement measures are often brittle, what happens when your sequencer can't phone home to check-in with the server that tells it if its license is valid, or when that server disappears because the model is no longer in its official support window?
Technical enforcement measures are often invasive, to avoid being circumvented they must run with the highest level of priviledge on a system and this access can readily be abused to surveil users as well as creating a security weakness.
Technical enforcement measures are often ineffective, they can often be bypassed by technically compentant users who can share their bypasses with other less technical users.
These measures are often more effective legally than they are technically due to the existence of 'anti-circumvention' laws.
The canonical example of an anti-circumvention law is [17 U.S. Code § 1201](https://www.law.cornell.edu/uscode/text/17/1201) but many other jurisdictions have equivalent statutes as a results of treaty and trade agreements.
These laws criminalise bypassing such protections meaning that law abiding users must suffer the downsides of technical enforcement whilst the supposed targets, often outside the jurisdiction of would be enforcers, simply circumvent these measures and use them anyway.
This often permits manufactures to abuse these statues to prevent users of their products from using them in ways not in the financial interest of the original manufacturer such as by using cheaper 3rd party consumables or repairs.
Manufactuers can also leverage their ongoing access to their devices to non-consensually, (generally with the veneer of consent provided by requiring the acceptance of an end user license agreement (EULA)), spy on end users harvesting their data and extracting value from it.
Expanded usage restrictions could create an incentive or excuse for manufactures to strengthen or expand technical enforcement measures.
It could be argued that they now have a greater obligation to police the use of their tools in order to demonstate compliance with these licenses.
