# Software licenses

There are many software licenses in existence. Many of those allow the licensee to do very little, but some give you more freedom to use and re-use the licensed software.

The [https://choosealicense.com/](https://choosealicense.com/) website offers a very simple mechanism to help you pick the best license for your project.

To make some sense of this variety, we can categorize them as follows.

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

## Examples

Many of the examples in this section relate to [xtas](http://xtas.net). xtas is a natural language processing toolkit for Python that reuses many third-party libraries, programs and data sets, and therefore provides a variety of nice examples.

![A graphical overview of xtas. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Underneath this there are three side-by-side squares, representing respectively Python libraries, Software, and Data, that are used by xtas. Within the Python libraries square, there are three boxes. The first box contains the words "BSD", "MIT" and "ALv2". The seconds box contains "LGPLv2.1". The third box contains "GPLv2+". Within the Software square, there are four boxes. The first box contains "Web Service". The second box contains "LGPL v2.1+". The third box contains "Research only" and the fourth box contains "GPL 2+/3+". The Data square also contains four boxes. The first box contains "CC BY-SA 3.0". The second box contains "Research Only". The third box contains "No license, US" and the fourth box contains "CoNLL'02 only".](xtas_overview_96.svg.png)

xtas itself is written in Python, and it uses a number of Python libraries that are licensed under common Free licenses. These include the simple permissive BSD and MIT licenses, the permissive Apache License version 2.0 (ALv2), the GNU Lesser General Public License version 2.1 (LGPLv2.1), and the GNU General Public License version 2 or later (GPLv2+).

(Note that the dependency on the GPLv2+ Python library has now been removed, but for the sake of these examples we will assume it to still be there.)

xtas' own Python code is distributed by us under the Apache License version 2.0. Since we own the copyright, we can license it any way we like (although there's a gray area with respect to GPL dependencies, see below). We do not distribute any combined works or binaries, but in the examples below we'll assume that there is a combined work, so that we can consider how it should be licensed.

In the following examples, we'll simplify most of this away, and look at one or a few dependencies in turn.


### Libraries: xtas vs. Snowball

![An illustration of the xtas vs. Snowball example. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "Snowball Stemmer" and "Python lib BSD".](xtas_snowball_96.svg.png)

xtas uses Snowball, a Python-based stemming library. Snowball is published under the 3-clause BSD license. Considering only xtas and Snowball, we can answer the three questions as follows.

#### Which separate works are there, and what is derived from what?

There are three works: Snowball, the xtas Python code, and the combined work xtas. The combined work derives from Snowball and from the xtas Python code. The others are independent works.

Note that the ALv2 and the LGPL v2.1 explicitly state that source code that is intended to work in combination with a library is not a derivative work, while the binary resulting from (statically or dynamically) linking the pieces together is; other licenses including the GPL do not make any explicit statement about this.

As far as I know, there is no case law on this; we will assume it to be the case in these examples.

#### Can the works be distributed, i.e. do the licenses allow this and are they compatible?

Snowball is licensed under a permissive license, so it can be redistributed under that license, and there are no constraints on the license of derivative works. We own the copyright to the xtas Python code, so we can license it in any way we want.

#### How should the work(s) be licensed?

The xtas Python code, and the xtas combined work, can be licensed under any license we want, so we should use the default eScience Center license, which is the Apache License v2.0.

If we redistribute Snowball, we must do so under the BSD license granted by its authors. (We cannot give additional permissions for Snowball, since we don't own the copyright, and additional restrictions would be unenforceable for the same reason.)


### Libraries: xtas vs. chardet

![An illustration of the xtas vs. chardet example. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "chardet" and "Python lib LGPLv2.1".](xtas_chardet_96.svg.png)

xtas uses chardet, a Python library for detecting the character set used in a string of text. Chardet is published under the GNU Lesser General Public License v2.1. Considering only xtas and chardet, we can answer the three questions as follows.

#### Which separate works are there, and what is derived from what?

There are three works: chardet, the xtas Python code, and the combined work. The combined work derives from chardet and from the xtas Python code. The others are independent works.

#### Can the works be distributed, i.e. do the licenses allow this and are they compatible?

Chardet is licensed under a weak copyleft license, so it can be redistributed under the terms of that license. Derivative works can be licensed under any license, but the LGPL v2.1 does require that the recipient can (and is allowed to) modify the library and use the modified library with the derivative work.

#### How should the work(s) be licensed?

xtas as a whole, and the xtas Python code, can be licensed in any way we want, so we use the default eScience Center license, which is the Apache License v2.0. If we distribute chardet, we must do so under the LGPL v2.1 license granted by its copyright owners.


### Libraries: xtas vs. unidecode

![An illustration of the xtas vs. unidecode example. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "unidecode" and "Python lib GPLv2+".](xtas_unidecode_96.svg.png)

xtas previously used unidecode, a Python library for converting text encoded according to The Unicode® Standard into an ASCII approximation of it. Unidecode is published under the GNU General Public License version 2 or later (GPLv2+). Considering only xtas and unidecode, we can answer the three questions as follows.

#### Which separate works are there, and what is derived from what?

There are three works: unidecode, the xtas Python code, and the combined work. The combined work derives from unidecode and from the xtas Python code.

Whether the xtas Python code is a derivative work of unidecode is not clearly defined by the law, and there is no case law on this. The Apache license and the LGPL explicitly state that it is not for the purpose of those licenses, but the GPL does not contain such a clause.

As they are developed separately and there is no code from unidecode in the xtas code, we assume here that it is not a derivative work.

#### Can the works be distributed, i.e. do the licenses allow this and are they compatible?

Unidecode is licensed under a strong copyleft license, so it can be redistributed under the terms of that license. Derivative works must be licensed under the same license.

Unidecode is licensed under the GPL version 2 or later. This is known as a _disjunctive license_. The copyright owners of unidecode offer everyone a GPLv2 license, but also a GPLv3 license, and even proactively any later version of the GNU GPL that may be created in the future. A potential user may choose to accept any one of these licenses, or a combination of them, if they want to copy the work or make derivative works.

#### How should the work(s) be licensed?

If we distribute unidecode, we should do so under the GPL version 2 or higher, as arbitrarily removing licenses from someone else's code does not make sense. The combined work xtas must be distributed under the same licenses, or a subset of them. The xtas Python code can be licensed in any way we want.

We should choose a license for the xtas Python code that is compatible with at least one of the licenses that unidecode can be distributed under, so that others can assemble and distribute combined works. Our default license, the ALv2, is compatible with the GPLv3 (but not with the GPLv2, for technical reasons), so we can use it here.

The combined work should then be licensed under the GPL version 3 or later. If it is important that it can be used under the GPLv2 as well, then we can license the xtas Python code under both the ALv2 and the GPLv2 (i.e. we offer both licenses, and the user can choose to accept either or both), and the combined work under the GPL version 2 or later.

Finally, if it is decided at some point in the future that the xtas Python source code is a derivative work of unidecode because it calls into it, even if none of unidecode is included in the work, then we must distribute the xtas Python code under at least one of the GPL licenses that unidecode is distributed under. In that case, we can offer xtas under the ALv2 and GPLv2+ set of licenses.

The simplest solution in this case would be to simply license the xtas Python code and the derived work under the GPLv3. However, we want people to be able to use as much of our software as possible in proprietary software, which is why our preferred license is the permissive ALv2.

As is probably clear by now, dependencies that are under a strong copyleft license complicate your life if you want people to be able to make proprietary works based on your software. For this reason, we try to avoid them.


### Libraries: xtas vs all

![An illustration of the xtas and all Python libraries example. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below this, there are three squares. The first square contains the words "Snowball" and "Python lib BSD". The second square contains "chardet" and "Python lib LGPLv2.1". The third square contains the words "unidecode" and "Python lib GPLv2+".](xtas_all_python_libs_96.svg.png)

Now, we will consider all three of the above examples at the same time.

#### How many separate works are there, and what is derived from what?

There are five works: Snowball, chardet, unidecode, the xtas Python code, and xtas the combined work. The combined work is derived from all its components.

#### Can the works be distributed, i.e. do the licenses allow this and are they compatible?

The four components are under Free Software licenses, and/or we own the copyright, so they can be distributed. The BSD, LGPLv2.1 and GPLv2+ all allow licensing the combined work under the GPL version 2 or higher, so there is at least one license that the combined work can be licensed under.

#### How should the work(s) be licensed?

The xtas Python code should be licensed under our default Apache License v2, and the combined work under the GPL version 3 or higher. (See the unidecode example above for alternatives.)


### In the Clouds

For the project "Towards Large-Scale Cloud-Resolving Climate Simulations", we want to combine the OpenIFS global circulation model with the DALES large-eddy simulation model. Both these models are available as libraries, so the project entails combining the OpenIFS and Dales libraries into a single program.

(This is a simplified example, the reality of this project is a notch or two more complicated, and the below is not exactly what we do.)

The OpenIFS library (part of the ECMWF weather model code) is available under a proprietary license that allows running the program and making private modifications, but does not allow distributing the program or any derivatives. DALES is published under the GPL version 3.

#### How many separate works are there, and what is derived from what?

There are four works: OpenIFS, DALES, the rest of the program written by us, and the combination of them all. The combined work is derived from its components.

#### Can the works be distributed, i.e. do the licenses allow this and are they compatible?

The OpenIFS license does not allow redistribution, so it cannot be distributed. DALES can be distributed, under the GPLv3. The rest of the program is written by us and can be licensed by us if we want to.

The whole combined work cannot be distributed, since it incorporates OpenIFS. If it did not include OpenIFS, it would have to be distributed under the GPLv3, because of the DALES dependency.

#### Can we work on this privately, without distributing anything?

The GPL allows making private modifications of software covered by it, with no restrictions, provided the changed software is not distributed at all. The OpenIFS license also allows making private modifications. So we can work on this project (and prepare and run combined works) within the Netherlands eScience Center without violating the licenses, as long as we do not share the results with anyone.

However, as in most of our projects, we work together with a principal investigator outside the eScience Center. This means that we exchange materials between different legal entities, which counts as distribution. We can do that with our own code (which we can even publish openly under the ALv2) and with DALES, but not with OpenIFS or any combined works.

#### What other options are there in this kind of situation?

We can try to split up the system into independent programs that run in separate processes and communicate with each other over well-documented, generic interfaces. In this way, there would never be a combined work, just a few independent works that exchange information. Exactly how separate the programs have to be to not be considered a single work is, again, a gray area.

We could also ask the OpenIFS and DALES copyright owners for permission to share combined works between the eScience Center and the PI. That would remove all uncertainty, but may not be practical in general.

Another option would be to replace one of the dependencies by one written by ourselves. This is usually impractical, both due to time constraints and because the new version would not have the scientific pedigree of the existing one.

The fundamental issue here is that the GPL tries to make everyone shared stewards of the software we use, while proprietary software tries to keep control over it in the hands of a single owner.

Combining them in a single project is complicated and not without legal risk, and we should avoid it. If that's not possible, we should tread carefully.

### External programs: xtas vs. CoreNLP

xtas can run the Stanford CoreNLP program, which is written in Java and distributed under the GNU GPL version 3 or later. When the user calls the corresponding xtas function, CoreNLP is started by xtas, the user's input is sent to it through a pipe, and then the CoreNLP output is handed back to the user or processed further.

![An illustration of the xtas vs. CoreNLP example. A square represents the combined work xtas. Within this square, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "Stanford CoreNLP" and "Java program GPLv3+".](xtas_corenlp_1_96.svg.png)

One interpretation of this situation is that this is no different from calling a function in a library, and that any distribution of xtas as a whole, including CoreNLP, should therefore be under the GPLv3+. Contributing to this interpretation is the fact that xtas will download and install CoreNLP automatically if needed.

![Another illustration of the xtas vs. CoreNLP example. A square on the left represents the combined work xtas. Within this square, there is a rectangle representing the xtas Python code, licensed under the Apache License v2. On the right is a separate square representing CoreNLP, with the text "Stanford CoreNLP" and "Java program GPLv3+". Between the squares are two arrows, one at the top pointing from xtas to CoreNLP, and one at the bottom pointing from CoreNLP to xtas.](xtas_corenlp_2_96.svg.png)

Another interpretation is that xtas and CoreNLP are separate works, and that xtas merely communicates with CoreNLP over its standard user interface.

In this interpretation xtas is a separate program that helps a user use the CoreNLP program from the Python language, and not a derivative work of CoreNLP. One can consider xtas analogous to a package installer and a command shell here, which are clearly not derivative works of the packages they install or the programs they start.

Under this interpretation, xtas as a whole (not including CoreNLP) can be distributed under any license we choose (subject to restrictions imposed by its other dependencies of course).

In practice, we do not distribute CoreNLP at all; we only distribute the xtas Python code, under the Apache License version 2.


### Data sets: Movie review emotion

xtas contains a function that detects emotions in movie reviews. It works by fitting a model to a set of training data, and then applying the model to the xtas user's data.

The training data set it uses is available on the Internet from the website of a European university, with a note saying that it can be used for academic research purposes only. xtas automatically downloads this data set the first time the user calls the function.

Since it was created in Europe, the training data set is protected by database rights, which limit copying substantial parts of it. This means that the xtas user needs permission to have xtas download the data set, which they only have if they use the data for research purposes.

Since the download happens automatically this may not be obvious, so it is documented in the function's documentation, and the function will refuse to work  unless a named argument `for_academic_research=True` is used when calling it.

xtas itself is not a database, and therefore cannot be a derivative work of the data set. The same goes for the model that is fit to the data.

An alternative way to provide this functionality would be to fit the model once, and then distribute the model (but not the data set) with xtas. Whether doing so constitutes academic research is debatable however.


### Mixed: Download a car?

For an internal research project, we needed annotated images of cars to train a neural network on. Such images can be found easily on car trading web sites, and so the question arose whether we could just grab a big collection of images from such a site.

Dutch database law contains a provision (article 5.b.) that says that retrieval of a substantial part of the contents of a database for scientific research is allowed, as long as the source is acknowledged and the use is non-commercial.

Unfortunately, this is not the only barrier. The photos on the site are also copyrighted works, owned by whoever made them, and making a copy requires their permission.

Furthermore, the web site has a set of general terms and conditions, which forbids retrieving a substantial portion of the database. These apply to anyone using the web site.

Downloading a car? Bad idea.
