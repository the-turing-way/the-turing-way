(rr-licensing-data)=
# Data Licenses

Like a software license, a data license governs what someone else can do with data that you create or own and that you make accessible to others through, for example, a data repository.
Data licenses vary based on different criteria, such as:
* Attribution to original owner
* Permission to redistribute or modify original
* Inclusion of the same license with derivatives or redistributions

As a result, accessibility to your data is affected by the data license you choose.

(rr-licensing-data-cc)=
## Creative Commons Licenses

Creative Commons or CC provides a number of licenses that can be used with a wide variety of creations that might otherwise fall under copyright restrictions, including music, art, books and photographs.
Although not tailored for data, CC licenses can be used as data licenses because they are easy to understand.
Its website includes a [summary page](https://creativecommons.org/about/cclicenses/){cite:ps}`creativecommons2020licenses` outlining all the available licenses, explained with simple visual symbols.

(rr-licensing-data-cc-permissions)=
### Permission Levels

The permission level provided by a Creative Commons data license can be understood from its name, which is a combination of two-letter "permission marks".
The only exception to this naming scheme is CC0, which will be introduced in the next section.

|**Permission Mark**|**What can I do with the data?**
|---|---|
BY | Creator must be credited
SA | Derivatives or redistributions must have identical license
NC | Only non-commercial uses are allowed
ND | No derivatives are allowed


For example, the CC BY-ND license specifies that users must credit the creator of the data and cannot create any derivatives.

(rr-licensing-data-cc-cc0)=
### Dedicating Your Work to the Public with CC0

CC0 serves as a public dedication mechanism, where you relinquish all copyrights to your data.
This means that anyone can modify, redistribute or build on your work.
Further, by using CC0, you forfeit the right to attribution.
Instead, you have to rely on norms such as good citation practices in academic communities to be recognized as the creator.
Several organizations, such as museums, governmental bodies and scientific publishers, have chosen CC0 for access to at least part of their data.
In many instances, data repositories maintained by universities recommend CC0 as the default option, such as the [4TU.Centre for Research Data](https://researchdata.4tu.nl/en/use-4turesearchdata/archive-research-data/upload-your-data-in-our-data-archive/licencing/).

(rr-licensing-data-odc)=
## Open Data Commons

Open Data Commons provides three licenses that can be applied specifically to data.
The [webpages](https://opendatacommons.org/licenses/index.html) {cite:ps}`odk2020odc` of each of these licenses include human-readable summaries, with the ramifications of the legalese explained in a concise format.

(rr-licensing-data-odc-pddl)=
### The Public Domain Dedication and License or PDDL

The PDDL is analogous to CC0, where you waive all your rights to the data you are putting into the public domain.
It comes with a [set of recommended community norms](https://opendatacommons.org/licenses/pddl/norms.html), which are not mandatory to include and do not form a legal contract but can be useful to have as a guide to encourage fair, open sharing of data.
It is also possible to put together a customized set of norms that serve your data-sharing community better.

(rr-licensing-data-odc-odc-by)=
### The Attribution or ODC-BY License

This license protects your attribution rights as a data owner or creator, just like the **BY** permission mark of CC licenses.
Any use or distribution of your database must also include information on the license used with the original.

(rr-licensing-data-odc-odbl)=
### The Open Database License or ODbL

The ODbL adds two more restrictions to the ODC-BY license.
The first is that any public uses of your data must be shared with the same license, similar to the CC **SA** permission mark.
The second is that if any version of your data is redistributed in a 'closed' format (for example, with Technological Protection Measures), it is mandatory for this redistribution to also be available in a version that is free of such closure measures.

(rr-licensing-data-differences)=
## A note on the differences between CC and ODC Licenses

Although it can seem like the licensing options offered by Creative Commons and Open Data Commons are exactly the same, there are some important differences.

One difference is the scope of rights that are covered by the license, which is nicely explained [here](https://wiki.creativecommons.org/wiki/Data#What_is_the_difference_between_the_Open_Data_Commons_licenses_and_the_CC_4.0_licenses.3F).
The ODC licenses were made specifically to be applied to data, and typically cover only database rights.
On the other hand, the CC licenses are more general-purpose and can be applied to other materials.
CC licenses also cover copyrights and other neighbouring rights.

Another difference is the availability of a standardised Community Norms document with the PDDL.
The lack of such a document with CC0 means that you have to rely on community norms, which may often be unspoken or unwritten and can vary from community to community, to ensure fair attribution.
A comparison between the PDDL and CC0 is provided [here](https://opendatacommons.org/faq.1.html).

(rr-licensing-data-options)=
## Other Licensing Options

It is also possible to choose other data licenses that may have been developed with a specific use case or community in mind or that are not in widespread global use.
These include licenses that were developed by national governments, such as the [Norwegian License for Open Government Data](https://data.norge.no/nlod/en/) {cite:ps}`nlod2020governmentdata`.
Often, such licenses are the recommended data licensing option within the corresponding country, especially for data created or owned by their public bodies.
Another example is the [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) or OGL, which was developed by The National Archives, UK.

The [Data Curation Center (DCC) guide](https://www.dcc.ac.uk/guidance/how-guides/license-research-data) {cite:ps}`ball2011license` on how to license research data expatiates on the licenses discussed in this chapter, and gives more information about [Prepared Licenses](https://www.dcc.ac.uk/guidance/how-guides/license-research-data#x1-6000), [Bespoke Licenses](https://www.dcc.ac.uk/guidance/how-guides/license-research-data#x1-7000), [Multiple Licensing](https://www.dcc.ac.uk/guidance/how-guides/license-research-data#x1-13000) and [Mechanisms for Licensing Data](https://www.dcc.ac.uk/guidance/how-guides/license-research-data#x1-14000).

If you would like to read more about the challenges and finer points of licensing, [this article](https://research.okfn.org/avoiding-data-use-silos/) is a great resource to get you started.

***Chapter Tags**: This chapter is curated for the `Turing Data Study Group` (`turing-dsg`).*
