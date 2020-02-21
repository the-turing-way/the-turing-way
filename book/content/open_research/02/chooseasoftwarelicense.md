# Software licenses

There are many software licenses in existence. Many of those allow the licensee to do very little, but some give you more freedom to use and re-use the licensed software. To make some sense of this variety, we can categorize them as follows.

## License categories

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
            <td>GPL CDDL</td>
            <td>LGPL MPL</td>
            <td>BSD MIT Apache</td>
            <td>Research-only No&nbsp;copying No&nbsp;modification</td>
        </tr>
    </tbody>
</table>

## Free software

The main distinction among software licenses is that of Free software versus proprietary software. Free software is software with license terms that give you ([Stallman, 1986](https://www.gnu.org/philosophy/free-sw.html))

0. The freedom to run the program as you wish, for any purpose (freedom 0).
1. The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.
2. The freedom to redistribute copies so you can help your neighbor (freedom 2).
3. The freedom to distribute copies of your modified versions to others (freedom 3). By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

These four freedoms together effectively neutralize copyright: freedoms 1 and 3 let you create derivative works, and freedoms 2 and 3 let you make copies.

Note that it's perfectly fine to sell copies of Free software, or warranty, or development services; this is about freedom to do things with the software, not about its price.

There are two other, similar definitions in use, the Open Source Institute's [Open Source Definition](https://opensource.org/osd-annotated) and the [Debian Free Software Guidelines](https://www.debian.org/social_contract#guidelines). The Free Software definition above, due to Richard Stallman, is the simplest and most concise, and in practice the categories they define are almost identical.

Software that is not Free is proprietary. Software that you're not allowed to copy or modify falls into this category, as does software with usage restrictions, e.g. "For research use only" or "For non-commercial use only".

There are some confusingly-named subcategories of proprietary software. _Freeware_ is software that can be copied without paying anyone, but comes without source and cannot be modified. _Shared source_ comes with source, but without permission to modify. Neither of these are Free in the above sense.

## Derivative software

Within the category of Free software, there are several subcategories, which are distinguished by what is allowed when making derivative software. There are two basic ways of making a derivative work of a program or library: modifying it (forking), and combining it with other software (e.g. using a library in your program). Of course, you can modify and then combine as well.

Modifying a program leads to a new program that is derived from the original, much like a new edition of a textbook is derived from the original. Both the original and the modified version are works under copyright law, and both of them may be licensed.

As an example of combining software, imagine a program A that uses two pre-existing libraries B and C. The complete program A will consist of library B, library C, and some code D that connects the libraries together and perhaps adds additional functionality. Each of these four items is a work of authorship with a license, with A sometimes referred to as the "Combined work", "Work as a whole" or "Larger work".

Different Free software licenses place different constraints on how modified versions and combined works can be licensed.

## Permissive licenses

As the name implies, permissive Free software licenses are the least restrictive. They let you distribute the software unchanged under that license, with or without source code. They will also let you distribute a modified version under any license you like, and let you distribute a combined work under any license.

Examples of well-known permissive licenses are the various BSD licenses, the MIT license, and the Apache License 2.0 that we have standardized on.

## Copyleft

Copyleft licenses add some restrictions to the licensing of derivative works. Like permissive licenses, they let you distribute the software unchanged under that license, but if you distribute a binary, then you have to include the source code as well. Modified versions have to be distributed under the same license as the original; you are not allowed to change the license.

When creating a combined work, a further distinction can be made. _Strong_ copyleft licenses on a component require a combined work to be licensed under the same license as the component. In the example above, if library B is distributed under a strong copyleft license such as the GNU GPL, then program A must be distributed under that same license.

_Weak_ copyleft licenses allow the combined work (A) to be distributed under any license, as long as the source for the licensed component (B) is made available as well under its original license. They may also require that the recipient of the combined work can relink the modules after modifying the component.

## Permission overview

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
            <td>Same license, also binary-only*</td>
            <td>Rarely</td>
        </tr>
        <tr>
            <th>Distribute modified</th>
            <td>Same license, with source</td>
            <td>Same license, with source**</td>
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
</table>

 * Under any license for the MIT license
** Relicensing LGPL to GPL is allowed

## License compatibility

If you use multiple external components in your program, then you may end up with multiple different constraints on the license of the combined work. If these constraints conflict, then you cannot legally distribute the result (if proprietary software is involved, then you may not legally be able to make the combined work at all).

If two licenses specify incompatible constraints on the license of the combined work, then they are _incompatible_.

The GNU GPL for instance is incompatible with proprietary licenses, because it requires the combined work to be licensed under the GPL, with no additional restrictions allowed. Having a part of the work under a proprietary license is such an additional restriction, so you cannot distribute such a combination (unless the copyright owner of the GPL code gives a special permission).

When you use different pieces of software together to solve a problem, and want to distribute the result, here are the questions you have to answer:

- Which separate works are there, and what is derived from what?
- Can the works be distributed, i.e. do the licenses allow this and are they compatible?
- How should the work(s) be licensed?

The next section shows some examples of how this is done.

