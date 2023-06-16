# Open Hardware Licenses- section to be used in the licensing section.

## Introduction
Licensing is an important aspect of sharing/publishing open source projects as it provides clarity for anyone looking to reuse your open source project.
Without licenses in place, anyone who wants to reuse it is left with legal ambiguity as to the status of using your intellectual property.
While we are looking to focus on open source hardware licenses the context is that this is within the broader open source movement. 
The open source licensing of hardware came out of open source software licenses and in fact several open source software licenses are widely accepted within the open hardware community. 

```{warning}
It is important to consider that copyright, licenses, patents etc are all legal concepts and are as such subject to what the law says.
Laws can change.
This change is not simply one of the laws changing over time, though that is a factor, but changes in jurisdiction and enforcement.
Simply put different countries have different laws and follow different procedures with regard to enforcing them.
The content provided here is broadly based on American and European law and legal traditions and might not be applicable - might even be contra indicated - or relevant.
While things like the Berne Convention have sought to harmonize copyright enforcement, the real world is a messy place.

Please also note that the information provided here is not by a lawyer specialising in intellectual property law or any other sort of lawyer for that matter.
So do not take the descriptions provided or viewpoints shared as legal advice, they are not that and not intended to be used in that manner.
Consult a legal expert to provide actual legal advice for your case.  
```

## Content
To understand what licenses do and how to apply them, it is first important to be familiar with a number of terms.
Often terms like copyright, licenses, patents, trademarks etc. are used interchangeably and maybe incorrectly and leads to confusion as to what exactly is being discussed and what the implications that arise from them are.
Familiarise yourself with the following terms and follow the links to understand more about them.


```{admonition} Info
**[Copyright](https://europa.eu/youreurope/business/running-business/intellectual-property/copyright/index_en.htm#shortcut-1/):** “When you create an original literary, scientific and artistic work, such as poems, articles, films, songs or sculptures, you are protected by copyright.
Nobody apart from you has the right to make the work public or reproduce it.
” And, “If you create literary, scientific and artistic work, you automatically have copyright protection, which starts from the moment you create your work, so you don't need to go through any formal application process.”

**[License](https://www.oshwa.org/faq/#what-is-a-license/):** “ Licensing is a way to give people rights that they wouldn’t otherwise have to use your intellectual property (IP) and, in return, to place restrictions on how they exercise those rights.”

**[Patent](https://www.wipo.int/patents/en/):** “A patent is an exclusive right granted for an invention, which is a product or a process that provides, in general, a new way of doing something, or offers a new technical solution to a problem.
To get a patent, technical information about the invention must be disclosed to the public in a patent application.”
 
**[Trademark](https://euipo.europa.eu/ohimportal/en/trade-mark-definition/)**: "Trade marks are signs used in trade to identify products.
Your trade mark is the symbol your customers use to pick you out.
It distinguishes you from your competitors.
You can protect and build upon your trade mark if you register it."

```

Copyrights are generally what make open source licenses enforceable.
So for many open source licenses to be applicable it is necessary to figure out what parts of the project are actually copyrightable and therefore can be licensed.
This complicates thing since copyrights do not protect functional items and hardware can be a combination of creative and functional elements, while the former is protected by copyright the latter would usually need a patent (if it is indeed patentable) to be protected.
It is important to note that copyrights and patents are mutually exclusive, that is something is either protected by copyright or it is protected by a patent but not both simultaneously. 

### What licenses to use

While as discussed above there are difficulties with regard to applying licenses to open source hardware projects, there are community practices that are good to know and follow.
A good place to start is to see which licenses are generally accepted by OSHWA,
- [GNU General Public License (GPL)](http://www.gnu.org/licenses/gpl.html/)
-	[Creative Commons licenses](https://creativecommons.org/licenses/)
-	[CERN Open Hardware Licenses](https://ohwr.org/project/cernohl/wikis/home)
-	[TAPR Open Hardware License](https://tapr.org/the-tapr-open-hardware-license/)
-	[Solderpad Hardware License](http://solderpad.org/licenses/)

The licenses listed above that are used in open source hardware can be broadly classified as permissive licenses and reciprocal or copyleft licenses.
That these are terms right out of open source software licenses is not a accident, as discussed before. 

In broad terms copyleft licenses impose an obligation of reciprocity on users of any of the licensed items, that is if something is licensed under a copyleft license then any derivative works need to be shared under the same rights.
Copyleft licenses do not prohibit the commercial use of copyrighted item only that you may not place additional restrictions on the derivative work.

Permissive licenses are those licenses that do not impose the reciprocity requirements.
These licenses allow for the proprietary licensing of derivative works.

#### Non-Hardware Native licenses
The GNU(GPL) developed within the context of the open source software movement (by Richard Stallman) is a popular copyleft license. The CC-BY-SA license falls under open source copyleft licenses. 
Most copyleft licenses fall under open source licenses but not all open source licenses are copyleft.

 The CC licenses offer a spectrum of licensing with the CC0 and CC-BY licenses being permissive open source licenses.
 Creative Commons recommends that CC licenses should not be used for licensing software.
 The MIT license and FreeBSD license are also permissive licenses. 

#### Hardware Native licenses

Due to the unique challenges faced when licensing open source hardware, licenses specifically tailored to be used with open source hardware have been created.
The CERN Open Hardware License is a prominent member in this category with the [CERN OHL v2.0](https://ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2/) license coming in three flavours the copyleft or strongly reciprocal CERN-OHL-S  variant, the weakly reciprocal CERN-OHL-W variant and the permissive CERN-OHL-P variant.
The aforementioned TARP Open hardware license is also a copyleft license while the Solderpad Hardware License is a permissive license. 

The advantage of using the licenses developed specifically for hardware is that they try to address the peculiarities of licensing open source hardware.
The CERN OHL v2.0 for example address the fact that there are different elements to an open hardware project and can be used for the software parts of the open hardware project as well, though CERN itself encourages the use of dedicated open source software licenses for those parts. 

### How and where to add licenses
The choice of license is a personal one based on the goals of the hardware project and the scope for collaboration and growth.
However, structuring the project and adding the appropriate licenses to the different section is much more universal.
Adopting the OSHWA certification regime to distinguish and apply the licenses is a good strategy. 

The certification considers four elements: a) the **hardware**, b) **software**, c) **documentation** and d) **branding**.
Depending on the type of project and scope one or two elements might not be relevant but for the most part having a plan for all four is a good idea. 

The licenses used should generally be featured in the main page where the project is hosted.
For example if GitHub is used a license file should be added to the topmost layer of the repo along with a Readme file.
The appropriate licenses should also attached to the different elements.
For example the software license should be attached to the code, with the appropriate declaration at the start of any section.

#### Hardware
This consists of the actual hardware elements of the project and utilising a license like a CERN OHL would be appropriate.
This element consists of the functional parts of the “product”.
In general functional parts of an invention could be protected by a patent but in our context the Open Hardware Licenses play the role. 

Since a patent has to be specifically applied for and given by the patent office of the country the aspects that the open hardware licence actually protects can be uncertain.
This does not mean there is no point to utilising such a license but simply that one must be  mindful of limitations.
The following line from the certification guidelines from OSHWA, gives a good perspective on the use of these hardware licenses, “It is best to think of hardware licenses as guiding tools for good actors, not ways to punish bad actors.”

#### Software
Depending on the type of open hardware project this element might not be needed.
But in the case where software is required for the functioning of the open source hardware this element should be addressed.
Using an open source initiative approved  compatible license is a good way to go about this.
Using for example the GNU(GPL) 3.0 for a copyleft license of the software and perhaps the MIT or FreeBSD in case of permissive software licensing.
Do keep in mind that the software under discussion here includes things like firmware.
Firmware is not considered an element of the hardware. 

#### Documentation
This element includes all the descriptions and discussions on how to build and use the hardware.
This include the design files.
The licenses applied here work on the basis of copyright and as such what is protected is the copyrightable aspects presented here.
So creative aspects of the design might be protected but not the functional ones. 

The copyright protection of the documentation offers protection from unauthorised copying and distribution of the actual documentation it does not prevent anyone from making the physical objects that are described in the documentation.
Nor does it prevent anyone from creating their own version of the documentation. 

Using a CC license for the documentation is advisable.
A CC-BY for permissible and a CC-BY-SA for copyleft.
Note that for a project to be considered open source restriction on field of use or commercial use should not be placed.

> []#### Branding
For most small scale open source hardware projects and those that fall within scope of hobbies branding is unlikely to be of concern.
But depending on the project it is important that branding and trademarks are appropriately protected and presented.
If the hardware elements include brand logos or trademarks it is advisable to include only "clean" versions of the hardware in the open source documentation.
This will ensure that any recreations or distributions of the product are not done so with your branding unless explicit permission is given by you. 

> []If branding and trademarks are relevant to your project it is important to apply for and obtain those certifications from the appropriate government authorities. 

### Limitations
It is important to keep in mind that licenses are only as powerful as the ability to enforce them.
This means that while you can curate and choose the best license that fits your goals it might entirely be redundant if enforcement is not possible.

The good news is that open source software licenses have been tested across different jurisdictions and been upheld in many cases, including the USA, Germany and many others.
The full scope of enforceability and effectiveness is still being explored. 

On the other hand open source hardware licensing is relatively recent and appears to be entirely untested in an actual court of law.
This means that the protections offered by such licenses stand on unproven grounds.
Added to this is the fact that a lot of the licensing is based on copyright law which does not transfer well when dealing with actual hardware.

This mean that the open hardware licenses might not offer as much or in fact any protections.
So it is good to repeat, “It is best to think of hardware licenses as guiding tools for good actors, not ways to punish bad actors.”
 
## extra notes

It is highly recommended to provide an [SPDX short license identifier](https://spdx.org/licenses/) to make the licensing terms machine-referenceable.







## Reference and further readings
- Open source hardware https://larszimmermann.de/licensing-open-source-hardware-by-michael-weinberg/  (accessed Sep. 23, 2022).
- OSHWA faq https://www.oshwa.org/faq/ (accessed Sep. 23, 2022)
- Certification procedure from OSHWA  https://certification.oshwa.org/process/hardware.html (accessed Sep. 23, 2022)
- Copyright https://europa.eu/youreurope/business/running-business/intellectual-property/copyright/index_en.htm#shortcut-1/  (accessed Sep. 23, 2022)
- Open Source Initiative https://opensource.org/faq (accessed Sep. 23, 2022)
- CERN Open Hardware License project https://ohwr.org/project/cernohl (accessed Sep. 23, 2022)
- License selector https://ufal.github.io/public-license-selector/ (accessed Sep. 23, 2022)
- Open source license litigation https://en.wikipedia.org/wiki/Open_source_license_litigation (accessed Sep. 24, 2022)
- Legal guide to open source https://opensource.guide/legal/ (accessed Sep. 24, 2022)
- Resources on Intellectual property https://www.wipo.int/reference/en/ (accessed Sep. 24, 2022)

## Notes
This part of the book is a derivative of Licensing Open Hardware by Santosh Ilhamparuthi. (2022, September 23) Zenodo. https://doi.org/10.5281/zenodo.7195720
