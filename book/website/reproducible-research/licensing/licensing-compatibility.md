(rr-licensing-compatibility)=
# License Compatibility

If you use multiple external components in your program, then you may end up with multiple different constraints on the license of the combined work.
If these constraints conflict, then you cannot legally distribute the result (if proprietary software is involved, then you may not legally be able to make the combined work at all).

If two licenses specify incompatible constraints on the license of the combined work, then they are _incompatible_.

The GNU GPL, for instance, is incompatible with proprietary licenses, because it requires the combined work to be licensed under the GPL, with no additional restrictions allowed.
Having a part of the work under a proprietary license is such an additional restriction, so you cannot distribute such a combination (unless the copyright owner of the GPL code gives special permission).

When you use different pieces of software together to solve a problem, and want to distribute the result, here are the questions you have to answer:

- Which separate works are there, and what is derived from what?
- Can the derivative works be distributed? Do the licenses allow this, and are they compatible?
- How should the work(s) be licensed?

The next section shows some examples of how this is done.

(rr-licensing-compatibility-examples)=
## Examples

Many of the examples in this section relate to [xtas](http://xtas.net).
xtas is a natural language processing toolkit for Python that reuses many third-party libraries, programs and data sets, and therefore provides a variety of excellent examples.

```{figure} ../../figures/xtas-overview96.png
---
name: xtas-overview96
alt: A graphical overview of xtas. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Underneath this, there are three side-by-side squares, representing respectively Python libraries, software, and data, that are used by xtas. Within the Python libraries square, there are three boxes. The first box contains the words "BSD", "MIT" and "ALv2". The second box contains "LGPLv2.1". The third box contains "GPLv2+". Within the Software square, there are four boxes. The first box contains "Web Service". The second box contains "LGPL v2.1+". The third box contains "Research only", and the fourth box contains "GPL 2+/3+". The Data square also contains four boxes. The first box contains "CC BY-SA 3.0". The second box contains "Research Only". The third box contains "No license, US" and the fourth box contains "CoNLL'02 only".
---
A graphical overview of xtas.
```

xtas itself is written in Python, and it uses a number of Python libraries that are licensed under common free licenses.
These include the simple permissive BSD and MIT licenses, the permissive Apache License version 2.0 (ALv2), the GNU Lesser General Public License version 2.1 (LGPLv2.1), and the GNU General Public License version 2 or later (GPLv2+).

(Note that the dependency on the GPLv2+ Python library is deprecated, but for the sake of these examples, we will assume it to still be there.)

xtas' Python code is distributed under the Apache License version 2.0.
Since the xtas authors own the copyright, they can license it any way they like (although there is a gray area concerning GPL dependencies, see below).
The xtas authors do not distribute any combined works or binaries, but in the examples below, we will assume that there is a combined work, so that we can consider how it should be licensed.

In the following examples, we will simplify most of this away and look at one or a few dependencies in turn.

(rr-licensing-compatibility-examples-apachevsbsd)=
### Apache vs. BSD

```{figure} ../../figures/xtas-snowball96.png
---
name: xtas-snowball96
alt: An illustration of the xtas vs. Snowball example.  A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "Snowball Stemmer" and "Python lib BSD".
---
An illustration of the xtas vs. Snowball example.
```

xtas uses [Snowball](https://snowballstem.org/), a Python-based stemming library. Snowball is published under the 3-clause BSD license.
Considering only xtas and Snowball, we can answer the three questions as follows:

#### Which separate works are there, and what is derived from what?

There are three works: Snowball, the xtas Python code, and the combined work xtas.
The combined work is derived from Snowball and xtas Python code, which are both independent works.

Note that the ALv2 and the LGPL v2.1 explicitly state that source code that is intended to work in combination with a library is not a derivative work, while the binary resulting from (statically or dynamically) linking the pieces together is.
Other licenses, including the GPL, do not make any explicit statement about this.

As far as I know, there is no case law on this; we will assume it to be the case in these examples.

#### Can the derivative works be distributed? Do the licenses allow this, and are they compatible?

Snowball is licensed under a permissive license.
It can be redistributed under that license, and there are no constraints on the license of derivative works.
The xtas authors can license it any way they want.

#### How should the work(s) be licensed?

The xtas Python code, and the xtas combined work, are licensed under the Apache License v2.0.

If xtas authors redistribute Snowball, they must do so under the BSD license granted by Snowball authors.
(They cannot give additional permissions for Snowball, since they do not own the copyright, and additional restrictions would be unenforceable for the same reason.)

(rr-licensing-compatibility-examples-apachevslgpl)=
### Apache vs. LGPL

```{figure} ../../figures/xtas-chardet96.png
---
name: xtas-chardet96
alt: An illustration of the xtas vs. chardet example. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "chardet" and "Python lib LGPLv2.1".
---
An illustration of the xtas vs. chardet example.
```

xtas uses [chardet](https://pypi.org/project/chardet/), a Python library for detecting the character set used in a string of text. Chardet is published under the GNU Lesser General Public License v2.1.
Considering only xtas and chardet, we can answer the three questions as follows.

#### Which separate works are there, and what is derived from what?

There are three works: chardet, the xtas Python code, and the combined work.
The combined work is derived from chardet and xtas Python code.
The others are independent works.

#### Can the derivative works be distributed? Do the licenses allow this, and are they compatible?

Chardet is licensed under a weak copyleft license, so it can be redistributed under the terms of that license.
Derivative works can be licensed under any license.
However, the LGPL v2.1 requires that the recipient can (and is allowed to) modify the library and use the modified library with the derivative work.

#### How should the work(s) be licensed?

xtas as a whole, and the xtas Python code, can be licensed in any way the authors want, so they used the Apache License v2.0.
If they distribute chardet, they must do so under the LGPL v2.1 license granted by its copyright owners.

(rr-licensing-compatibility-examples-apachevsgplv2)=
### Apache vs. GPLv2

```{figure} ../../figures/xtas-unidecode96.png
---
name: xtas-unidecode96
alt: An illustration of the xtas vs. unidecode example. The large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "unidecode" and "Python lib GPLv2+".
---
An illustration of the xtas vs. unidecode example.
```

xtas previously used [unidecode](https://pypi.org/project/Unidecode/), a Python library for converting text encoded according to The Unicode® Standard into an ASCII approximation of it.
Unidecode is published under the GNU General Public License version 2 or later (GPLv2+).
Considering only xtas and unidecode, we can answer the three questions as follows.

#### Which separate works are there, and what is derived from what?

There are three works: unidecode, the xtas Python code, and the combined work. The combined work derives from unidecode and the xtas Python code.

Whether the xtas Python code is a derivative work of unidecode is not clearly defined by the law, and there is no case law on this.
The Apache license and the LGPL explicitly state that it is not for the purpose of those licenses, but the GPL does not contain such a clause.

As they are developed separately, and there is no code from unidecode in the xtas code, we assume here that it is not a derivative work.

#### Can the derivative works be distributed? Do the licenses allow this, and are they compatible?

Unidecode is licensed under a strong copyleft license, so it is redistributed under the terms of that license. Derivative works must be licensed under the same license.

Unidecode is licensed under the GPL version 2 or later. This is known as a _disjunctive license_.
The copyright owners of unidecode offer everyone a GPLv2 license, but also a GPLv3 license, and even proactively any later version of the GNU GPL that may be created in the future.
A potential user may choose to accept any one of these licenses, or a combination of them, if they want to copy the work or make derivative works.

#### How should the work(s) be licensed?

If the xtas authors distribute unidecode, they should do so under the GPL version 2 or higher, as arbitrarily removing licenses from someone else's code does not make sense.
The combined work xtas must be distributed under the same licenses or a subset of them.
The xtas Python code can be licensed in any way they want.

The xtas authors should choose a license for the xtas Python code that is compatible with at least one of the licenses that unidecode can be distributed under so that others can assemble and distribute combined works.
The ALv2 is compatible with the GPLv3 (but not with the GPLv2, for technical reasons), so they can use it here.

The combined work should then be licensed under the GPL version 3 or later.
If it is important that it can be used under the GPLv2 as well, then the xtas authors can license the xtas Python code under both the ALv2 and the GPLv2 (meaning, they offer both licenses, and the user can choose to accept either or both), and the combined work under the GPL version 2 or later.

Finally, it may be decided later that the xtas Python source code is a derivative work of unidecode because it calls into it.
Even if none of unidecode is included in the work, then the xtas authors must distribute the xtas Python code under at least one of the GPL licenses that unidecode is distributed under.
In that case, they can offer xtas under the ALv2 and GPLv2+ set of licenses.

The simplest solution, in this case, would be to simply license the xtas Python code and the derived work under the GPLv3.

As is probably clear by now, dependencies that are under a strong copyleft license complicate your life if you want people to be able to make proprietary works based on your software.

(rr-licensing-compatibility-examples-apachevsall)=
### Apache vs BSD vs LGPL vs GPLv2

```{figure} ../../figures/xtas-all-python-libs96.png
---
name: xtas-all-python-libs96
alt: An illustration of the xtas and all Python libraries example. A large rectangle represents the combined work xtas. Within this rectangle, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below this, there are three squares. The first square contains the words "Snowball" and "Python lib BSD". The second square contains "chardet" and "Python lib LGPLv2.1". The third square contains the words "unidecode" and "Python lib GPLv2+".
---
An illustration of the xtas and all Python libraries example.
```

Now, we will consider all three of the above examples at the same time.

#### How many separate works are there, and what is derived from what?

There are five works: Snowball, chardet, unidecode, the xtas Python code, and xtas the combined work. The combined work is derived from all its components.

#### Can the derivative works be distributed? Do the licenses allow this, and are they compatible?

The four non-xtas components are under free software licenses, and the xtas authors own the copyright to the xtas Python code, so all five components can be distributed by the xtas authors.
The BSD, LGPLv2.1 and GPLv2+ all allow licensing the combined work under the GPL version 2 or higher, so there is at least one license that the combined work can be licensed under.

#### How should the work(s) be licensed?

The xtas Python code should be licensed under the Apache License v2 and the combined work under the GPL version 3 or higher.
(See the {ref}`unicode example <rr-licensing-compatibility-examples-apachevsgplv2>` above for alternatives.)


### Call External Program

xtas can run the [Stanford CoreNLP program](https://stanfordnlp.github.io/CoreNLP/), which is written in Java and distributed under the GNU GPL version 3 or later. When the user calls the corresponding xtas function, CoreNLP is started by xtas, the user's input is sent to it through a pipe, and then the CoreNLP output is handed back to the user or processed further.

```{figure} ../../figures/xtas-corenlp1-96.png
---
name: xtas-corenlp1-96
alt: An illustration of the xtas vs. CoreNLP example. The square represents the combined work xtas. Within this square, there is a wide low rectangle at the top representing the xtas Python code, licensed under the Apache License v2. Below that is a square containing the words "Stanford CoreNLP" and "Java program GPLv3+".
---
An illustration of the xtas vs. CoreNLP example.
```

One interpretation of this situation is that it is no different from calling a function in a library and that any distribution of xtas, as a whole, including CoreNLP, should therefore be under the GPLv3+.
Contributing to this interpretation is the fact that xtas will download and install CoreNLP automatically if needed.

```{figure} ../../figures/xtas-corenlp2-96.png
---
name: xtas-corenlp2-96
alt: Another illustration of the xtas vs. CoreNLP example. The square on the left represents the combined work xtas. Within this square, there is a rectangle representing the xtas Python code, licensed under the Apache License v2. On the right is a separate square representing CoreNLP, with the text "Stanford CoreNLP" and "Java program GPLv3+". Between the squares are two arrows, one at the top pointing from xtas to CoreNLP, and one at the bottom pointing from CoreNLP to xtas.
---
Another illustration of the xtas vs. CoreNLP example.
```

Another interpretation is that xtas and CoreNLP are separate works and that xtas merely communicates with CoreNLP over its standard user interface.

In this interpretation xtas is a separate program that helps a user use the CoreNLP program from the Python language, and not a derivative work of CoreNLP.
One can consider xtas analogous to a package installer and a command shell here, which are clearly not derivative works of the packages they install or the programs they start.

Under this interpretation, xtas as a whole (not including CoreNLP) can be distributed under any given license (subject to restrictions imposed by its other dependencies of course).

In practice, the xtas authors do not distribute CoreNLP at all; they only distribute the xtas Python code, under the Apache License version 2.


### GPLv3 vs Proprietary License

In this example project we want to combine the [OpenIFS global circulation model](https://confluence.ecmwf.int/display/OIFS) with the [DALES large-eddy simulation model](https://github.com/dalesteam/dales).
Both these models are available as libraries, so the project entails combining the OpenIFS and Dales libraries into a single program.

(This is a simplified example, the reality of this project is a notch or two more complicated, and the below is not exactly what we do.)

The OpenIFS library (part of the ECMWF weather model code) is available under a proprietary license that allows running the program and making private modifications, but does not allow distributing the program or any derivatives.
DALES is published under the GPL version 3.

#### How many separate works are there, and what is derived from what?

There are four works: OpenIFS, DALES, the rest of the program written by us, and the combination of them all. The combined work is derived from its components.

#### Can the derivative works be distributed? Do the licenses allow this, and are they compatible?

The OpenIFS license does not allow redistribution, so it cannot be distributed. DALES can be distributed, under the GPLv3.
The rest of the program is written by us and can be licensed by us if we want to.

The whole combined work cannot be distributed, since it incorporates OpenIFS.
If it did not include OpenIFS, it would have to be distributed under the GPLv3, because of the DALES dependency.

#### Can we work on this privately, without distributing anything?

The GPL allows making private modifications of software covered by it, with no restrictions, provided the changed software is not distributed at all.
The OpenIFS license also allows making private modifications.
So we can work on this project (and prepare and run combined works) without violating the licenses, as long as we do not share the results with anyone.

However, if we want to collaborate with someone outside our organization, this means that we exchange materials between different legal entities, which counts as distribution.
We can do that with our own code (which we can even publish openly under the ALv2) and with DALES, but not with OpenIFS or any combined works.

#### What other options are there in this kind of situation?

We can try to split up the system into independent programs that run in separate processes and communicate with each other over well-documented, generic interfaces.
In this way, there would never be a combined work, just a few independent works that exchange information.
However, to not be considered a single work, how separate the programs have to be is unclear.

We could also ask the OpenIFS and DALES copyright owners for permission to share combined works between our organization and the outsider.
That would remove all uncertainty, but may not be practical in general.

Another option would be to replace one of the dependencies by one we write.
This is usually impractical, both due to time constraints and because the new version would not have the scientific pedigree of the existing one.

The fundamental issue here is that the GPL tries to make everyone shared stewards of the software we use, while proprietary software tries to keep control in the hands of a single owner.

Combining them in a single project is complicated and not without legal risk, and you should avoid it.
If that is not possible, you should tread carefully.
