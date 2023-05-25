(rr-code-error)=
# Error management

## Why should you care about error management?

We all have experienced it: you just wrote a new piece of code, but when you try it, it does not work as expected.
Perhaps there is a typo, or a bug, or you just passed the wrong parameter to a function.
It is not a big deal... as long as you notice.
Noticing something is wrong is the first step to fixing it.

Unfortunately, not all errors are easy to foresee.
This is particularly true when your code is going to be used by someone else than you.

Error management practices dramatically reduce our code's chances to let an error pass unnoticed.
Depending on the severity of the error, we may want to try an automated solution, warn the user, or even abort the whole workflow.

The first step in ensuring your code is robust and nice to use, is to make sure it does not fail silently.
There will be many assumptions you make when writing a program: for example, the data type of your imports; the structure of a data file, but also the behavior of any dependencies; from individual functions, entire libraries, to the programming language you use and how it functions in various operating systems.
It is natural to have assumptions to build on, but it can become problematic when these assumptions are incorrect for a specific instance, yet the program carries on regardless.

Silent failures can occur in two ways:

- Silent failure in an early step, that leads to problems (and errors) in later stages
- Silent failure that does not lead to any problems, but results in answers that may not make sense.

The former will likely lead to strange and unintelligible error messages, that do not have anything to do with the actual problem.
We will go into this more in the next section.

## Workflow

### Step 1: Describe assumptions

Your code contains many assumptions.
For example, a function performing a simple mathematical operation assumes that its input is numerical.
What happens if this function is used on a bit of text?
Or a dataframe?
Or an open file?

In a different example, let's imagine a data science workflow.
As part of this workflow, a column labeled "Age" is selected.
What happens if this column does not exist?
The workflow plots the column "Age", but the plot is cut off at age 100.
What happens if the data contains ages over 100?
Or if this column contains negative numbers?

In making decisions about cases like these, the first step is to be explicit about the assumptions made.
To identify assumptions in your code, you can ask yourself:

- What type of object/data do I expect here?
- What files need to exist for my workflow to run, and where?
- ...

If you think critically, there is no end to the assumptions that you make.
For instance, you assume that a built-in function you use works in a specific way.
Labeling all these assumptions would perhaps drive you crazy, and that is not the point of this exercise.
Instead, try to focus on assumptions you make about the data and/or files a user puts into your workflow or code.

### Step 2: Assert/verify assumptions

Once you have identified assumptions, you can verify if they are true.
This is also called 'asserting'.
Depending on your programming language, and the nature of the assumption, there are many creative ways to do this.
A good starting point for verifying an assumption can be an if/else statement:

```
if my_assumption is TRUE:
    continue
else:
    do something
```

If the assumption is met, nothing happens and your code executes as usual.

However, simply the existence of this if/else block will be able to alert a user if an important condition is not met.
If they are trying to select a column that does not exist, for instance.
Or if they are performing mathematical operations on pieces of text.

You can also take advantage of errors that are raised by the programming language you use.
We will go into that in more detail in [Error handling](#error-handling).

### Step 3: Deal with unmet assumptions

What can you do when a condition is not met?

There are roughly three ways you can deal with an unmet assumption:

- Redirect: you can send the program in a different direction based on the information you are given;
- Report: you can inform the user that something is different than what the program expects;
- Abort: you can stop executing the program.

All programming languages have the option to raise an error.
These errors can come in different flavors.
Two main flavors that you will find in most programming languages are 'warning' and 'error'.
A 'warning' is less severe than an 'error'; it indicates a potential problem, but does not stop the program.
An 'error' is thrown when the program needs to halt.

Thus, error types fit well with the different ways of dealing with unmet assumptions:

|          | Error type | Action           |
|:---------|:-----------|:-----------------|
| Redirect | None       | Choose next step |
| Report   | Warning    | No action        |
| Abort    | Error      | Stop executing   |

## Error handling

Whatever programming language you are using, errors already exist there.
The good part about errors appearing, is that something has gone wrong, and your user knows about it.
The bad part is that the message is likely not informative to your user:

```
object of type 'closure' is not subsettable
```

You can catch these errors in your workflow, and deal with them in the same way as you deal with unmet assumptions: redirect, report, or abort.
Redirecting from an error has a technical term: "exception handling".
In this case, you expect a certain error to be raised, but instead of stopping your program, you change its course.
In many programming languages, this is done in a `try... except` block.
Reporting or aborting from an error can be done in the same way, but instead of using the default error, you raise your own.
Importantly, raising a warning or error message from your own program means you have control over the quality of the message.

## Error message quality

When raising an error (or warning), you have the option to add information.
This is important information for a user who attempts to use your program, but runs into a problem.
The information you provide can help them 'debug': make the changes necessary to successfully execute the run.

> "Make sure that when it fails, it fails informatively."
>
> [Jenny Bryan](https://github.com/jennybc/debugging#readme)

Writing good error messages is a skill that comes with a lot of practice.
You have likely received error messages that were of little use to you, and instead of helping you fix the problem, they only confused you.
An error message is unhelpful when it is too broad, too vague, or unclear about what the next steps may be.
When making your program robust, therefore, you should put thought into the information you provide in an error message.

These qualities make a good error message:

- It clearly pinpoints the problem.
- It points a user to next steps: items to check, or other steps they can take to further understand or fix the problem.
- It uses jargon appropriately, and keeps its target audience in mind.
- It is honest about what it knows and does not know.

```{figure} ../../figures/error-management.*
---
width: 500px
name: error-management
alt: Cartoon showing three stages of error management, left, a person working on a computer that is smoking, but the program looks to be running just fine and the person is unaware. Middle, a person with a computer that is smoking, and the program shows an error message. The person does not understand the error message and looks confused. Right, a person with a computer that is smoking, and presenting an error message that allows the person to fix the problem. The person looks happy.
---
Three stages of error management: silent failure (left) leaves a user blissfully unaware of problems; unintelligible errors (middle) show there is a problem, but leave a user confused; informative errors (right) show a user there is a problem, and allow them to solve it.
```


<!--```
image:
Sliding scale from "No error / silent failure" (bugs!!), to "unintelligible error", "generic error", to "informative error".
The goal is first to catch issues (so: no silent failure), then to maximize the informativeness of the error along this axis.
```-->

## 4. Troubleshooting

Dealing with unintelligible errors, both in your code (automating error management) and other peoples' (troubleshooting).

How do you make sure you detect a silent failure state?
How to get your code to warn you that things are not going as planned?
How do you start making your assumptions explicit, and make sure a fire is not happening under your nose without your knowledge?

>The major difference between a thing that might go wrong and a thing that cannot possibly go wrong is that when a thing that cannot possibly go wrong goes wrong it usually turns out to be impossible to get at or repair.
> Douglas Adams


## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

- [ ] Find assumptions in your code, and make them explicit.
- [ ] Write if/else statements to test your assumptions.
- [ ] Decide per assumption when not meeting it should lead to redirect, report, and/or abort.


## What to learn next
> recommended next chapters that are a good next step up
This chapter is complementary to testing

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography
> Credit/urls for any materials that form part of the chapter's text.
