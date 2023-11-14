(rr-code-error)=
# Writing robust code

We all have experienced it: you just wrote a new piece of code, but when you try it, it does not work as expected.
Perhaps there is a typo, a bug, or you just passed the wrong parameter to a function.
It is not a big deal, as long as you notice!
Noticing something is wrong is the first step to fixing it.

## Silent failures
There will be many assumptions you make when writing a program.
For example, the data type of your imports, the structure of a data file, but also the behavior of any dependencies, from individual functions, entire libraries, to the programming language you use and how it functions in various operating systems.
It is natural to have assumptions to build on.
However, it can become problematic when these assumptions are incorrect for a specific instance and the program carries on regardless.
This is what is called a 'silent failure'.

Silent failures can lead to problems down the line, likely resulting in strange and unintelligible error messages that do not have anything to do with the actual problem.
A silent failure that stays silent will generate results that are wrong, and needs sharp eyes to be detected.
To make sure these things do not happen, your program needs built-in checks and balances.
Having good error management practices dramatically reduces the chance that a problem occurs, and especially, that it passes unnoticed.
This chapter's main purpose is to help you make your code robust, and capable of dealing with different potential problems.

(rr-code-error-workflow)=
## Workflow

(rr-code-error-workflow-step1)=
### Step 1: Describe your assumptions

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
- When calling a function, am I relying on default settings for arguments?
- When a function returns multiple outputs, do I ensure they are in the right order?

If you think critically, there is no end to the assumptions that you make.
For instance, you assume that a built-in function you use works in a specific way.
Labeling all these assumptions would perhaps keep you busy eternally, and that is not the point of this exercise.
Instead, try to focus on assumptions you make about the data and/or files a user puts into your workflow or code.

(rr-code-error-workflow-step2)=
### Step 2: Assert/verify assumptions

Once you have identified assumptions, you can verify if they are true.
This is also called '**asserting**'.
Depending on your programming language, and the nature of the assumption, there are many creative ways to do this.
A good starting point for verifying an assumption can be an if/else statement:

```
if my_assumption is not TRUE:
    do something
else:
    continue
```

If the assumption is `TRUE`, nothing happens and your code executes as usual.

However, simply the existence of this if/else block will be able to alert a user if an important condition is not met.
If they are trying to select a column that does not exist, for instance.
Or if they are performing mathematical operations on pieces of text.

You can also take advantage of errors that are raised by the programming language you use.
We will go into that in more detail in [Error handling](#error-handling).

(rr-code-error-workflow-step3)=
### Step 3: Deal with unmet assumptions

What can you do when a condition is not met?

There are roughly three ways you can deal with an unmet assumption:

- Redirect: you can send the program in a different direction based on the information you are given;
- Report: you can inform the user that something is different than what the program expects;
- Abort: you can stop executing the program.

All programming languages have the option to raise an error.
These errors can come in different flavors.
Two main flavors that you will find in most programming languages are 'warning' and 'error'.
A '**warning**' is less severe than an 'error'; it indicates a potential problem, but does not stop the program.
An '**error**' is thrown when the program needs to halt.

Thus, error types fit well with the different ways of dealing with unmet assumptions:

|          | Error type | Action           |
|:---------|:-----------|:-----------------|
| Redirect | None       | Choose next step |
| Report   | Warning    | No action        |
| Abort    | Error      | Stop executing   |

(rr-code-error-handling)=
## Error handling

Whatever programming language you are using, errors already exist.
The good part about errors appearing is that something has gone wrong and your user knows about it.
The bad part is that the message is likely not informative to your user:

```output
object of type 'closure' is not subsettable
```

You can catch these errors in your workflow, and deal with them in the same way as you deal with unmet assumptions: redirect, report, or abort.
Redirecting from an error has a technical term: '**exception handling**'.
In this case, you expect a certain error to be raised, but instead of stopping your program, you change its course.
In many programming languages, this is done in a `try... except` or `try... catch` block:

```
try:
    do_something_that_might_fail()
except ErrorType:
    do_something_else()
```

Reporting or aborting from an error can be done in the same way, but instead of using the default error, you raise your own.
Importantly, raising a warning or error message from your own program means you have control over the quality of the message.
And, contrasting most built-in errors, it can give a user instructions on how to fix it.

(rr-code-error-messages)=
## Writing good error messages

When raising an error (or warning), you should add information about the problem in an error message.
This is important information for a user who attempts to use your program and runs into a problem.
The information you provide can help them 'debug': make the changes necessary to successfully execute the run.

> "Make sure that when [your program] fails, it fails informatively."
>
> [Jenny Bryan](https://github.com/jennybc/debugging#readme)

Writing good error messages is a skill that comes with a lot of practice.
You have likely been on the receiving end of error messages that were of little use to you, and instead of helping you fix the problem, they only confused you.
An error message is unhelpful when it is too broad, too vague, or unclear about what the next steps may be.
When making your program robust, you should therefore put thought into the information you provide in an error message.

```{figure} ../../figures/error-management.*
---
name: error-management
alt: Three stages of error management. Left, a person working on a computer that is smoking, but the screen is clear and the person is unaware that there is a problem. Middle, a person with a computer that is smoking, displaying an error message. The person does not understand the message and is confused. Right, a person with a smoking computer that is presenting a clear error message. The person can now fix the problem and is happy.
---
Three stages of error management: silent failures (left) leave a user blissfully unaware of problems; unintelligible errors (middle) show there is a problem, but confuse the user; informative errors (right) both show a user there is a problem, and how to solve it.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

These qualities make a good error message:

- It clearly pinpoints the problem.
- It points a user to next steps: items to check, or other steps they can take to further understand or fix the problem.
- It uses jargon appropriately, and keeps its target audience in mind.
- It is honest about what it knows and does not know.

## Read more

The practices described in this chapter are not the same as testing your code.
Instead, they go hand in hand, and can be used to complement each other.
For example:

- Use tests to pass strange data to your workflow, and confirm that your workflow redirects, reports, or aborts as expected.
- Use tests to confirm you receive the expected error messages.

To read more about how to implement code testing in your project, see the dedicated chapter on {ref}`rr-testing`.