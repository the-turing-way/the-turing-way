(rr-licensing-software)=
# Software Licenses

## Prerequisites

This chapter builds on {ref}`rr-licensing`.

(rr-licensing-software-summary)=
## Summary

A software license governs the extent of use or redistribution of software, with or without software documentation.

There are many software licenses in existence.
Many of those allow the licensee to do very little, but some give you more freedom to use and re-use the licensed software.

The [https://choosealicense.com/](https://choosealicense.com/) website offers a straightforward mechanism to help you pick the best license for your project.
Creative Commons recommends that CC licenses should not be used for licensing software.

To make some sense of this variety, we can categorize them as follows.

## License Categories

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

(rr-licensing-software-free)=
## Free Software

Software licenses are either free or proprietary. 
Free software comes with license terms that give you ([as defined by GNU](https://www.gnu.org/philosophy/free-sw.html)):

* _Freedom 0_: The freedom to run the program as you wish, for any purpose.
* _Freedom 1_: The freedom to study how the program works, and change it, so it does your computing as you wish.
Access to the source code is a precondition for this.
* _Freedom 2_: The freedom to redistribute copies so you can help others in your community.
* _Freedom 3_: The freedom to distribute copies of your modified versions to others.
By doing this, you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

These four freedoms together effectively neutralize copyright; *Freedoms 0* and *2* let you use the original software and share it with others. 
*Freedoms 1* and *3* let you create derivative works based on the software and share these with others.

Note that it is perfectly acceptable to sell copies of free software, warranty, or development services; this is about the freedom to do things with the software, not about its price.

There are two other, similar definitions in use; the Open Source Institute's [Open Source Definition](https://opensource.org/osd-annotated) and the [Debian Free Software Guidelines](https://www.debian.org/social_contract#guidelines).
The free software definition above, by Richard Stallman, is the most straightforward and concise, and in practice, the categories they define are almost identical.

Software that is not free is proprietary.
Software that you are not allowed to copy or modify falls into this category, as does software with usage restrictions, for example, "For research use only" or "For non-commercial use only".

There are some confusingly-named subcategories of proprietary software.
_Freeware_ is software that can be copied without paying anyone, but comes without source and cannot be modified.
_Shared-source_ comes with source, but without permission to modify.
Neither of these is free in the above sense.

(rr-licensing-software-derivative)=
## Derivative Software

Within the category of free software, there are several subcategories, which are distinguished by what is allowed when making derivative software.
There are two basic ways of making a derivative work of a program or library: modifying it (forking), or combining it with other software (for example using a library in your program).
Of course, you can modify and then combine as well.

Modifying a program leads to a new program that is derived from the original. 
This is similar to deriving the new edition of a textbook from the original.
Both the original and modified versions are works under copyright law, and both of them may be licensed.

As an example of combining software, imagine a program A that uses two preexisting libraries B and C.
The complete program A will consist of library B, library C, and some code D that connects the libraries together and perhaps adds additional functionality.
Each of these four items is a work of authorship with a license. 
Program A can sometimes be referred to as the "Combined work", "Work as a whole" or "Larger work".

Different free software licenses place different constraints on how modified versions and combined works can be licensed.

(rr-licensing-software-permissive)=
## Permissive Licenses

As the name implies, permissive free software licenses are the least restrictive.
They let you distribute the software unchanged under that license, with or without source code.
They will also let you distribute a modified version under any license you like, and let you distribute a combined work under any license.

Examples of well-known permissive licenses are the various BSD licenses, the MIT license, and the Apache License 2.0.

(rr-licensing-software-copyleft)=
## Copyleft

Copyleft licenses add some restrictions to the licensing of derivative works.
Like permissive licenses, they let you distribute the software unchanged under that license. 
However, if you distribute a binary, then you have to include the source code as well.
Modified versions have to be distributed under the same license as the original; you are not allowed to change the license.

When creating a combined work, a further distinction can be made.
_Strong_ copyleft licenses on a component require a combined work to be licensed under the same license as the component.
In the example above, if library B is distributed under a strong copyleft license such as the GNU GPL, then program A must be distributed under that same license.

_Weak_ copyleft licenses allow the combined work (A) to be distributed under any license, as long as the source for the licensed component (B) is also made available under its original license.
They may also require that the recipient of the combined work can re-link the modules after modifying the component.

(rr-licensing-software-overview)=
## Permission Overview

<table>
    <thead>
        <tr>
            <th rowspan="2"></th>
            <th colspan="2">Copyleft</th>
            <th rowspan="2">Permissive</th>
            <th rowspan="2">Proprietary</th>
        </tr>
        <tr>
            <th>Strong</th>
            <th>Weak</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>Use for anything</th>
            <td>Yes</td>
            <td>Yes</td>
            <td>Yes</td>
            <td>Sometimes</td>
        </tr>
        <tr>
            <th>Private changes</th>
            <td>Yes</td>
            <td>Yes</td>
            <td>Yes</td>
            <td>Rarely</td>
        </tr>
        <tr>
            <th>Distribute original</th>
            <td>Same license, with source</td>
            <td>Same license, with source</td>
            <td>Same license, also binary-only<sup>1</sup></td>
            <td>Rarely</td>
        </tr>
        <tr>
            <th>Distribute modified</th>
            <td>Same license, with source</td>
            <td>Same license, with source<sup>2</sup></td>
            <td>Any license, also binary-only</td>
            <td>Rarely</td>
        </tr>
        <tr>
            <th>Distribute combined</th>
            <td>Same license, with source</td>
            <td>Any license, binary additions</td>
            <td>Any license, also binary-only</td>
            <td>Rarely</td>
        </tr>
    </tbody>
    <caption>
      <div class="footnote">
        <sup>1</sup>Under any license for the MIT license <sup>2</sup>Relicensing LGPL to GPL is allowed
      </div>
      Permissive licenses grant the largest set of permissions to users. Copyleft licenses require redistribution of the original or modified source to use the same license, with weak copyleft licences allowing a different choice of license for the combined work. Proprietary licenses rarely provide any permissions beyond the right to use the software.
    </caption>
</table>

