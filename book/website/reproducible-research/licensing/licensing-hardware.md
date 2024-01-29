(rr-licensing-hardware)=
# Open Hardware Licenses

(rr-licensing-hardware-prerequisites)=
## Prerequisites

This chapter builds on the chapter {ref}`rr-licensing` and it is advisable to read it before reading this one.

## Introduction

While this chapter focuses on open source hardware licenses, this should be considered within the broader open source movement. 
The open source licensing of hardware came out of open source software licenses and, in fact, several open source software licenses are widely accepted within the open hardware community. 
Please refer to the warnings and description of terms you will find in the introductory chapter
{ref}`rr-licensing`.

As explained there, for many open source licenses to be applicable, it is necessary to figure out what parts of the project are actually copyrightable and therefore can be licensed.
This complicates thing for hardware, as copyrights do not protect functional items and hardware can be a combination of creative and functional elements.
While the former is protected by copyright, the latter would usually need a patent (if it is indeed patentable) to be protected.
It is important to note that copyrights and patents are mutually exclusive: something is either protected by copyright or it is protected by a patent, but not both simultaneously.



### Which licenses to use

While, as discussed above, there are difficulties with regard to applying licenses to open source hardware projects, there are community practices that are good to know and follow.
A good place to start is to see which licenses are generally accepted by OSHWA:

- [GNU General Public License (GPL)](http://www.gnu.org/licenses/gpl.html/)
-	[Creative Commons licenses](https://creativecommons.org/licenses/)
-	[CERN Open Hardware Licenses](https://ohwr.org/project/cernohl/wikis/home)
-	[TAPR Open Hardware License](https://tapr.org/the-tapr-open-hardware-license/)
-	[Solderpad Hardware License](http://solderpad.org/licenses/)

The licenses listed above are used in open source hardware. 
They can be broadly classified as permissive licenses and reciprocal or copyleft licenses.
You may see here the connection with software licenses.
As mentioned before, this is not an accident.



#### Non-Hardware Native licenses

For the software and documentation part of your hardware documentation package, you should use a corresponding license. Please refer to the description below {ref}`rr-licensing-hardware-multiple` and to the other sub-chapter of the licenses chapter.
Usually, the CC licenses offer a spectrum of licensing for documentation and data, with the CC0 and CC-BY licenses being permissive open source licenses. 

For software, the GNU(GPL) developed within the context of the open source software movement (by Richard Stallman) is a popular copyleft license.
The MIT license and FreeBSD license are also permissive licenses. 

#### Hardware Native licenses

Due to the unique challenges faced when licensing open source hardware, licenses specifically tailored to be used with open source hardware have been created.
The CERN Open Hardware License is a prominent member in this category with the [CERN OHL v2.0](https://ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2/) license coming in three flavours:

- the copyleft or strongly reciprocal CERN-OHL-S variant
- the weakly reciprocal CERN-OHL-W variant
- the permissive CERN-OHL-P variant.
 
  
The aforementioned TARP Open hardware license is also a copyleft license, while the Solderpad Hardware License is a permissive license. 

The advantage of using the licenses developed specifically for hardware is that they try to address the peculiarities of licensing open source hardware.
The CERN OHL v2.0 for example address the fact that there are different elements to an open hardware project and can be used for the software parts of the open hardware project as well, though CERN itself encourages the use of dedicated open source software licenses for those parts. 

(rr-licensing-hardware-multiple)=
### Multiple licenses for hardware

Adopting the OSHWA certification regime to distinguish and apply the licenses is a good strategy. 
The certification considers four elements: a) the **hardware**, b) **software**, c) **documentation** and d) **branding**.
Depending on the type of project and scope one or two elements might not be relevant but for the most part having a plan for all four is a good idea. 


#### Hardware design and licenses

This consists of the actual hardware elements of the project and utilising a license like a CERN OHL would be appropriate.
This element consists of the functional parts of the "product".
In general, functional parts of an invention could be protected by a patent, but in our context the Open Hardware Licenses play that role. 

Since a patent has to be specifically applied for and given by the patent office of the country, the aspects that the open hardware licence actually protects can be uncertain.
This does not mean there is no point to utilizing such a license but simply that one must be mindful of their limitations.
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

The copyright protection of the documentation offers protection from unauthorised copying and distribution of the actual documentation, it does not prevent anyone from making the physical objects that are described in the documentation.
Nor does it prevent anyone from creating their own version of the documentation. 

Using a CC license for the documentation is advisable.
A CC-BY for permissible and a CC-BY-SA for copyleft.
Note that for a project to be considered open source, restriction on field of use or commercial use should not be placed.

#### Branding
For most small scale open source hardware projects and those that fall within scope of hobbies, branding is unlikely to be of concern.
But depending on the project, it is important that branding and trademarks are appropriately protected and presented.
If the hardware elements include brand logos or trademarks, it is advisable to include only "clean" versions (without branding) of the hardware in the open source documentation.
This will ensure that any recreations or distributions of the product do not contain your branding, unless explicit permission is given by you. 

> If branding and trademarks are relevant to your project it is important to apply for and obtain those certifications from the appropriate government authorities. 

### Limitations


Open source hardware licensing is relatively recent and appears to be entirely untested in an actual court of law.
This means that the protections offered by such licenses stand on unproven grounds.
We should alsa add that the licensing is based on copyright law which does not transfer well when dealing with actual hardware.

This mean that the open hardware licenses might not offer as much or even any protections.
So it is good to repeat, “It is best to think of hardware licenses as guiding tools for good actors, not ways to punish bad actors.”
 

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
