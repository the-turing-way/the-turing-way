(rr-testing)=
# Code Testing

| Prerequisite | Importance |
| -------------|------------|
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Necessary |

## Summary

Researcher-written code now forms a part of a huge portion of research, and if there are mistakes in the code the results may be partly or entirely unreliable.
Testing code thoroughly and frequently is vital to ensure reliable, reproducible research.
This chapter will provide general guidance for writing tests and describe a number of different kinds of testing, their uses and how to go about implementing them.

```{figure}  ../figures/error-management.jpg
---
name: error-management
alt: A person is happily coding, then a error throws and the coder gets confused. Then the coder can find the error and fix it.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

## Motivation

It is very, very easy to make mistakes when coding.
A single misplaced character can cause a program's output to be entirely wrong.
One of the examples above was caused by a plus sign which should have been a minus.
Another was caused by one piece of code working in meters while a piece of code written by another researcher worked in feet.
*Everyone* makes mistakes, and in research the results can be catastrophic.
Careers can be damaged/ended, vast sums of research funds can be wasted, and valuable time may be lost to exploring incorrect avenues. This is why tests are vital.

Here's a couple of illustrations exemplifying of why should write tests:

```{figure}  ../figures/testing-motivation1.png
---
name: testing-motivation1
alt:
---
```

```{figure}  ../figures/testing-motivation2.png
---
name: testing-motivation2
alt:
---
```

Even if problems in a program are caught before research is published it can be difficult to figure out what results are contaminated and must be re-done.
This represents a huge loss of time and effort.
Catching these problems as early as possible minimises the amount of work it takes to fix them, and for most researchers time is by far their most scarce resource.
You should not skip writing tests because you are short on time, you should write tests *because* you are short on time.
Researchers cannot afford to have months or years of work go down the drain, and they can't afford to repeatedly manually check every little detail of a program that might be hundreds or hundreds of thousands of lines long.
Writing tests to do it for you is the time-saving option, and it's the safe option.

As researchers write code they generally do some tests as they go along, often by adding in print statements and checking the output.
However, these tests are often thrown away as soon as they pass and are no longer present to check what they were intended to check.
It is comparatively very little work to place these tests in functions and keep them so they can be run at any time in the future.
The additional labour is minimal, the time saved and safeguards provided are invaluable.
Further, by formalising the testing process into a suite of tests that can be run independently and automatically, you provide a much greater degree of confidence that the software behaves correctly and increase the likelihood that defects will be found.

Testing also affords researchers much more peace of mind when working on/improving a project.
After changing their code a researcher will want to check that their changes or fixes have not broken anything.
Providing researchers with a fail-fast environment allows the rapid identification of failures introduced by changes to the code.
The alternative, of the researcher writing and running whatever small tests they have time for is far inferior to a good testing suite which can thoroughly check the code.

Another benefit of writing tests is that it typically forces a researcher to write cleaner, more modular code as such code is far easier to write tests for, leading to an improvement in code quality.
{ref}`Good quality code<rr-code-quality>` is far easier (and altogether more pleasant) to work with than tangled rat's nests of code I'm sure we've all come across (and, let's be honest, written). This point is expanded upon in the section {ref}`rr-testing-unittest`.

## The advantages of testing for research

As well as advantaging individual researchers testing also benefits research as a whole.
It makes research more reproducible by answering the question "how do we even know this code works".
If tests are never saved, just done and deleted the proof cannot be reproduced easily.

Testing also helps prevent valuable grant money being spent on projects that may be partly or wholly flawed due to mistakes in the code.
Worse, if mistakes are not at found and the work is published, any subsequent work that builds upon the project will be similarly flawed.

Perhaps the cleanest expression of why testing is important for research as a whole can be found in the [Software Sustainability Institute](https://www.software.ac.uk/) slogan: better software, better research.
