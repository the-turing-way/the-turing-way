# Error management

## 1. Why should you care about error management?

~~~

## 2. Some simple examples on error management (e.g. if/else; if someone gets only this far they already have some simple ideas on how to get started on making their assumptions explicit!)

~~~

## 3. Making silent errors visible, how to get out of the worst state; how to get your code to warn you if you are in a silent failure state.

~~~

## 4. Dealing with unintelligible errors, both in your code (automating error management) and other peoples' (troubleshooting).

~~~

### 5. Writing informative error messages in your own code, what does a good error look like?

---

# Error management

## Prerequisites / recommended skill level
> other chapters that should have been read before or content you should be familiar with before you read this

| Prerequisite | Importance | Notes |
| -------------|----------|------|
| Chapter/topic | How important it is | Any notes |

## Summary
> easy to understand summary - a bit like tl;dr

## How this will help you/ why this is useful
> why we think you should read the whole thing

## Chapter content
> depending on the content, this might be more structured, e.g. with exercises, gotcha sections etc





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

### Explicit assumptions



### If/else




###








## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go
[ ]


## Troubleshooting


Dealing with unintelligible errors, both in your code (automating error management) and other peoples' (troubleshooting).



## Writing error messages


Writing informative error messages in your own code, what does a good error look like?


## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

- [ ] Find assumptions in your code, and make them explicit.
- [ ] Write if/else statements to test your assumptions.
- [ ] Decide per assumption when not meeting it should lead to redirect, report, and/or abort.


## What to learn next
> recommended next chapters that are a good next step up

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography
> Credit/urls for any materials that form part of the chapter's text.
