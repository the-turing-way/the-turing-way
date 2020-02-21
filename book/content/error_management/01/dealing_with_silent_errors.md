## Preventing silent failures


The first step in ensuring your code is robust and nice to use, is to make sure it does not fail silently.
There will be many assumptions you make when writing a program: for example, the data type of your imports; the structure of a data file, but also the behavior of any dependencies; from individual functions, entire libraries, to the programming language you use and how it functions in various operating systems. 
It is natural to have assumptions to build on, but it can become problematic when these assumptions are incorrect for a specific instance, yet the program carries on regardless.

Silent failures can occur in two ways:
- Silent failure in an early step, that leads to problems (and errors) in later stages
- Silent failure that does not lead to any problems, but results in answers that may not make sense.

The former will likely lead to strange and unintelligible error messages, that do not have anything to do with the actual problem. 
We will go into this more in the next section.

The latter is the subject of this section.
How do you make sure you detect a silent failure state?
How to get your code to warn you that things are not going as planned?
How do you start making your assumptions explicit, and make sure a fire is not happening under your nose without your knowledge?

>The major difference between a thing that might go wrong and a thing that cannot possibly go wrong is that when a thing that cannot possibly go wrong goes wrong it usually turns out to be impossible to get at or repair.
> Douglas Adams


### If/else



### 








## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

