(rr-licensing-software)=
# Software Licenses

A software license governs the extent of use or redistribution of software, with or without software documentation.

There are many software licenses in existence.
Many of those allow the licensee to do very little, but some give you more freedom to use and re-use the licensed software.

The [https://choosealicense.com/](https://choosealicense.com/) website offers a straightforward mechanism to help you pick the best license for your project.

To make some sense of this variety, we can categorize them as follows.

```{figure} ..\..\figures\license_categories.PNG
---
name: license_categories
alt: A classification of different types of licenses. Licenses can either be Free or Propietary. Free Licenses can be classed as Copyleft or Permissive, and Copyleft licenses are either Strong or Weak.
---
Licenses can either be Free or Propietary, with Free Licenses further classified as shown.
```

(rr-licensing-software-free)=
## Free Software

Software licenses are either free or proprietary. 
Free software comes with license terms that give you ([as defined by GNU](https://www.gnu.org/philosophy/free-sw.html)):

* _Freedom 1_: The freedom to run the program as you wish, for any purpose.
* _Freedom 2_: The freedom to study how the program works, and change it, so it does your computing as you wish.
Access to the source code is a precondition for this.
* _Freedom 3_: The freedom to redistribute copies so you can help others in your community.
* _Freedom 4_: The freedom to distribute copies of your modified versions to others.
By doing this, you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

These four freedoms together effectively neutralize copyright: **freedoms 1 and 3** let you create derivative works, and **freedoms 2 and 4** let you make copies.

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

|                     | **CopyLeft**                  |                               | **Permissive**                     | **Proprietary** |
|---------------------|---------------------------|-------------------------------|--------------------------------|-------------|
|                     | **Strong**                    | **Weak**                          |                                |             |
| **Use for Anything**    | Yes                       | Yes                           | Yes                            | Sometimes   |
| **Private Changes**     | Yes                       | Yes                           | Yes                            | Rarely      |
| **Distribute Original** | Same license, with source | Same license, with source     | Same license, also binary-only<sup>*</sup> | Rarely      |
| **Distribute Modified** | Same license, with source | Same license, with source<sup>**</sup>     | Any license, also binary-only  | Rarely      |
| **Distribute Combined** | Same license, with source | Any license, binary additions | Any license, also binary-only  | Rarely      |

<sup>*</sup>Under any license for the MIT license

<sup>**</sup>Relicensing LGPL to GPL is allowed
