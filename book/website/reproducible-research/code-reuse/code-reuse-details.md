
(rr-code-reuse-details)=
# Detailed Recommendations for Code Reuse

Make sure you (or somebody else) can re-use your code to do the same exact thing you did.
This section contains a simple checklist of recommendations for making your software more reusable.
In this section contains a more in-depth explanation of each of these recommendations, with pointers to other relevant parts of this guide.

## Repeatable Recommendations

At this stage, you might not even need to be able to open the code and read it, you just want to make sure you can re-run all the needed steps and obtain the same results you had.

### 1. Make sure you can find it (in space)

Your code must be stored publicly and shared with collaborators. It has an unique persistent identifier, so that everyone can find it and access it.

**See also**: {ref}`rr-vcs`

### 2. Make sure you can find it (in time)

Ideally the temporal evolution of the code is documented with version control. This allows you to retrieve a specific version from the past.

**See also**: {ref}`rr-vcs`

### 3. Make sure you can execute the same sequence of operations

Often the human who set up the environment is also the one who wrote the code and the one who knows the exact order of steps needed to be able to re-run the code and reproduce the results.
This could surely be carefully documented for another human to re-do it.

**See also**: [CodeRefinery lesson on Reproducible Research](https://coderefinery.github.io/reproducible-research/)

### 4. Make sure your environment and sequence of operations is robust and no human is needed to replicate what was done

You do not want to depend on humans. 
They tend to make errors even if they do not have bad intentions. 
So you want your environment to be scripted and be re-created when needed and you want your sequence of operations to be run by a pipeline script that glues together all the sequence of steps.
A nice side-effect of scripting the sequence of operations is that this often can serve as documentation of the steps.

**See also**: {ref}`rr-renv-options`

### 5. License your code

Make sure you attach a license to your code and specify how you want to be cited when people re-use it.
Consider using a permissive license that allows for reuse.
Also, you should choose a license which is compatible with the licenses of libraries or packages your software depends on.

**See also**: {ref}`rr-licensing`, {ref}`rr-licensing-floss`, {ref}`rr-licensing-compatibility`

### 6. Make sure it is citable

Make sure to specify how you want to be cited when people re-use it.

**See also**: {ref}`cm-citable-cite-software`

### 7. Include necessary data

If the software depends on any sort of data, the data should be available

**See also**: {ref}`rr-rdm-data`

## Re-runnable recommendations

Make sure you (or others) can re-use it to do the thing you did, but with different data/different parameters

### 1. Remove hardcoded bits and make the code modular
You do not want to have details specific to your data or analysis parameters hardcoded into the code.
If something can become a reusable function, separate it from the hardcoded parameters and turn it into something (re)usable on its own.
Make the modules pure: given the same input, a pure function always returns the same value.
Instead of specifying file paths inside the scripts, consider passing them as command line arguments for a more portable and general and reusable script.

**See also**: [CodeRefinery Modular Code Development lesson](https://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md/#1)

### 2. Test that the modules you made can take different types of input data or parameters
You might not know yet how your code will be re-used in the future, but you can prevent how it should not be used if you can test which parameters are allowed.

**See also**: [CodeRefinery lesson on Automated testing](https://coderefinery.github.io/testing/motivation/)

### 3. Turn the modules into a package/toolbox
Separate even more the specifics of your project with the bits that can be reused in other of your projects or by other people.

**See also**: {ref}`rr-renv-package`, [Packaging software](https://scicomp.aalto.fi/scicomp/packaging-software/), [Software packaging in Python](https://aaltoscicomp.github.io/python-for-scicomp/packaging/)

## Portable Recommendations
Portability refers to the ability to transfer software to a new environment.
This could refer to an identical (but not the same) machine, but it can also refer to a new hardware architecture, operating system and such.
Both of these are important for software reuse.

### 1. Make sure you can recreate the environment where it lived
The environment is a fragile snapshot in time which silently accompanies the code.
It can include the human who operated the software, the steps the human did to prepare the data, the hardware, the OS, the libraries, external packages/toolboxes/dependencies.
All this can be carefully documented for another human to re-do all the same exact steps.

**See also**: {ref}`rr-renv`

## Extendable and Modifiable Recommendations
Make sure others can build on your code to extend it and improve it.

### 2. Make sure your code is readable by humans
It often pays more to write code for other humans so they can read it (including your future self).
A cryptic oneliner with obscure variable names is not any faster or more efficient than splitting the one liner into multiple steps with readable variable names that make sense.
Furthermore, using coding conventions will help other readers.

**See also**: {ref}`rr-code-style-and-formatting`, {ref}`rr-code-quality-advantages`

### 3. Make sure comments are present
Write comments before writing the actual code. Imagine that somebody could just read the comments and skip all the code bits between comments and get a full picture of what is going on as if they read the whole code.
