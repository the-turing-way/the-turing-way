(rr-licensing-floss)=
# Free/Libre' or 'Open Source' software

These same concepts developed originally in the context of software have often been applied to other creative outputs.
Consequently, they are among the most developed and useful context for understanding the licensing of other things.

Software that is not free (in the 'libre' sense defined below) is proprietary.
Software that you are not allowed to copy or modify falls into this category, as does software with usage restrictions, for example, "For research use only" or "For non-commercial use only".

Permissively licensed things can generally be used by anyone for any purpose.
A popular minimal example of this for software is known as the [MIT license](https://mit-license.org/), for other works, [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) the 'public domain' license.
Copyleft licenses attempt to ensure that any re-distributions or derived works also remain 'free', the canonical example is the [GPL](https://www.gnu.org/licenses/gpl-3.0.html).
Unlike permissively licensed content, which can be modified and redistributed under a different license (including as a part of a closed and/or for profit project), copyleft content (modified or unmodified) must be distributed under the same, or a compatible license, which retains the copyleft obligation.
In other words if you take copyleft content, modify it, and distribute your modifications, those modifications must also be copyleft.

(rr-licensing-floss-copyleft)=
## Copyleft License

The concept of copyleft licenses and their first example, the GPL, originated with Richard Stallman, who founded the free-software foundation (FSF) in 1985.
The idea is a 'hack' of copyright law to use the protections that it affords to privately owned software to a software commons.
<!-- citations needed -->

### The FSF's four Fundamental Freedoms of FLOSS

- Freedom 0: The freedom to run the program as you wish, for any purpose.
- Freedom 1: The freedom to study how the program works, and change it, so it does your computing as you wish.
  Access to the source code is a precondition for this.
- Freedom 2: The freedom to redistribute copies so you can help others in your community.
- Freedom 3: The freedom to distribute copies of your modified versions to others.
  By doing this, you can give the whole community a chance to benefit from your changes.
  Access to the source code is a precondition for this.

Other influential definitions of free and open source software include: The Debian project's [Debian Free Software Guidelines (DFSG)](https://www.debian.org/social_contract#guidelines), and the open source initiative (OSI)'s [Open Source Definition](https://opensource.org/osd/).
The terms 'Free'/'Libre' & 'Open Source' software are often used somewhat interchangeably, but have different connotations.
The use of 'free software' typically denotes a more hardline political commitment to the ideals of the free software movement, and is associated with a preference for copyleft licenses.
The name 'open source' places the emphasis on freedom 1 and could more readily be confused with the concept of 'source available' software, based on a naive interpretation of the name.
'Open source' is associated with, if not a preference for, then a more favourable view of, permissive licenses.

```{note}
The word 'free' in english does not distinguish something being monetarily free 'gratis' from politically free 'libre'.
This is often summarised along the lines of: "free as in speech, not necessarily free as in beer"
Thus the phrase 'libre software' is sometimes encountered in English to succinctly distinguish the concept of software which respects your liberty from software which is finacially free to use ('gratis').
This ambiguity confusingly leads to the name 'Freeware' which is software that can be copied without paying anyone, but comes without source and cannot be modified.
The 'free' in 'freeware' is gratis but not libre.
It is also common to encounter the acronyms FOSS (Free and open source software) and FLOSS (Free/libre and open source software)
```

The FSF contends that all software should respect these freedoms and that all software which does not respect these freedoms creates an asymmetric relationship between the users and developers of that software which can readily be abused by the developers to exploit their users.
If developers are bad stewards of a free software projects, the friction for replacing them is lower, as all of the work put into the software does not need to be re-done.
A 'fork' of the project can be made, developed and maintained by different developers whom the community of users deem a better steward.

This is not true of proprietary projects where the developers own the rights to the code and thus cannot be readily replaced by the community of users if they begin to abuse these users who are now held captive by switching costs.
It should be noted that an acrimonious project fork is quite uncommon and by no means always successful, it is the move of last resort.
The credible threat of a fork redresses the power balance between developers and users giving users leverage if developers make unpopular choices.

### Protecting the Rights of Creators and Users

Copyleft licenses are an attempt to ensure that software remains effectively under community ownership and cannot be used to make proprietary software which does not respect the four freedoms and may thus result in the abuse of its users.
To attempt to achieve this goal, copyleft software requires that when distributing copyleft software or in some cases derived works that you do so under the same terms as the original license.
Creative commons 'share-alike' licenses attempt the same thing for other content.
One of the advantages of this approach is that the simplest way to redistribute your changes is often to contribute them to the 'upstream project' or to 'upstream' them.
If you add some features to a codebase for your own use and contribute them upstream then you get the advantage of the assistance of upstream maintainers in keeping your code up to date and working correctly with the rest of the project.
You don't have to maintain your own fork and keep it up to date with the latest patches from the rest of the codebase and you don't have to manage your own distribution.
All this also means that everyone else benefits from your improvements and you benefit from everyone elses'.
Being a good open source citizen means playing by these rules and, if you can, contributing your fixes and improvements to upstream projects; not just freeloading off of them.

Copyleft licenses do not prohibit commercial use, indeed numerous companies exist which develop copyleft projects.
Many of those generate revenue through support services instead of selling licenses, which would incentivise an unhealthy relationship with their users.
[Nextcloud](https://nextcloud.com/) is an excellent example of a commercial, open source project.
Nextcloud makes use of the [AGPL v3.0](https://www.fsf.org/bulletin/2021/fall/the-fundamentals-of-the-agplv3) a license which extends the protections of the GPL to software used over a network.
It gives users who interact with this software over a network, for example by using a web service, rather than run it on their own computers, the right to access a copy of the source code; which they are further free to modify and distribute as is usual for the GPL.

Within copyleft licenses, there are 'strong' and 'weak' copyleft licenses.
'Strong' copyleft licenses require that combined works which contain them as a library also carry the same license but weak copyleft licenses permit their re-distribution as a library within a combined work under a different license.
We will define derived and combined works in the section on license compatibility where the detailed implications of the distinctions between strong & weak copyleft, and permissive licencing are explored in more practical detail.
It is important to note that licenses can be incompatible such that creating a combined work is highly impractical to do legally.

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

(rr-licensing-usage-restriction)=
## What are 'Usage Restricting' Licenses?

Usage restricting licenses seek to affirmatively protect users or others affected by the use of the work by placing specific restrictions on its use.
This curtails freedom 0, the freedom to use software 'for any purpose' and prohibiting the use of the software, or other system, for unethical purposes.
Both 'Ethical source' & 'Responsible AI' Licenses are examples of this approach and seek to place restrictions on the uses to which the licensees can put the software or machine learning systems licensed in this fashion.
Consequently, these licenses by the classical definitions of free and open source software from the FSF and OSI would not be considered free or open source licenses. They do however generally resemble them in the other three criteria of the definition.
Their merits versus conventional open source licenses have been the subject of some debate, and their adoption has thus far been relatively limited.

Even an attribution requirement (the BY in CC-BY) can in some cases be considered a usage restriction.
For example the Debian project found the [Common Public Attribution License (CPAL)](https://en.wikipedia.org/wiki/Common_Public_Attribution_License) to be incompatible their free-software guidelines for this reason whilst it is approved by the Open Source Initiative.
In the case of academic works attribution requirements can serve to re-enforce the citation convention with the force of copyright law.

(rr-licensing-welcoming)=
### Alternative to Proprietary Solutions

Some people avoid using proprietary or non-free resources, such as software, on principle to the greatest extent that they can.
It is highly impractical to completely avoid all non-free software in the world today, so many have compromises and workarounds.
This might include measures such as only running proprietary code in a sandboxed environment like a web browser, but this can impose an additional burden on these users.
This is especially true if proprietary tools do not offer first-class features in browsers or support free software operating systems like Linux.
Consequently, the choice to use open infrastructure is important if you want to be inclusive of people who adhere strongly to the free software ethos and consider being asked to use non-free software as an imposition.
A small minority of people simply will not participate if doing so requires that they use non-free software.

(rr-licensing-choosing)=
### Where to Find Open Licenses for Code and Software?

- The [Open Source Initiaitive (OSI)](https://opensource.org/licenses/) maintains a list of [approved licenses](https://opensource.org/licenses/) open source licenses
- [Free Software Foundation](https://www.fsf.org/) maintains a [list of GPL-Compatible Free Software Licenses](https://www.gnu.org/licenses/license-list.html#SoftwareLicenses)
   - [GNU/FSF recomendations](https://www.gnu.org/licenses/license-recommendations.html)
- [choosealicense.com](https://choosealicense.com/) provides a tool to guide you through the license choice project.
- [Organisation for ethical source](https://ethicalsource.dev/) maintains a list of [ethical source licenses](https://ethicalsource.dev/licenses/)
- License guidance for Machine Learning Models have been provided in the {ref}`rr-licensing-ml`
  - You can refer to [Responsible AI Licenses (RAIL)](https://www.licenses.ai/) for Machine Learning (ML)/Artificial Intelligence (AI) systems
  - [Creative Commons](https://creativecommons.org/) licenses do not contain specific terms about the distribution of source code, however, it can be combined with Software licenses to different parts of ML/AI systems: Creative Commons to training data and weights, software licenses to code used in training / deployment.

License for documentation, data, hardware and machine learning models, please refer to next subchapters.

(rr-licensing-enforcement)=
### Licencing enforcement

There have been a number of successful legal cases that have been brought in defence of the terms of copyleft licenses obliging the parties abusing the terms of these licenses to appropriately release their code.
But this can be hard to discover, as it is not immediately obvious if copyleft code has been used from looking at a black box proprietary end product.

<!-- citations needed -->

Organisations which take legal action in defence of free software, and which can provide information and resources for anyone else seeking to do the same, include:

- [Software Freedom Conservancy](https://sfconservancy.org/)
- [Software Freedom Law Centre](https://softwarefreedom.org/)
- [FSF - licensing and compliance](https://www.fsf.org/licensing/)
- [Free Software Foundation Europe (FSFe) - legal work](https://fsfe.org/activities/legal.en.html)
- [Electronic Frontiers Foundation - legal cases](https://www.eff.org/cases)

(rr-licensing-edge)=
### Pertinent edge cases

(rr-licensing-edge-clas)=
#### Contributor license Agreements

The holder of the copyright on a copyleft project can still re-license that project or dual-license that project under a different license, for example to grant exclusive rights to commercially distribute that project with proprietary extensions or to make future versions proprietary.
In a large community developed project, this would require the consent of all contributors, as they each own the copyright to their contributions.
To get around this, some copyleft projects developed by companies that commercially license proprietary extensions to these projects ask their contributors to sign contributor license agreements (CLAs) which may assign the contributor's copyright to the company, or include other provisions so that they can legally dual-license the project.

(rr-licensing-edge-available)=
#### 'Source Available' or 'Shared Source'

Under a proprietary license the code is generally not made public.
Some projects share their code but do not license its re-use, modification or redistribution.
This is known as being 'source available' or 'shared-source', the [Vivaldi](https://vivaldi.com/) web browser is an example of such a project.