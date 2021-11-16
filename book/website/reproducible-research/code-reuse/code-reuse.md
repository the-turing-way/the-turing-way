(rr-code-reuse)=
# Reusable code
Your software project could range from a small script you use for data processing to a notebook used for data analysis, or a software library implementing your algorithms.
Regardless of how big or small your software project is, it is important to make your code reusable.

Different types of software have different requirements for being reusable: for a small script, having sufficient documentation might be enough, while for a mission critical software library, thorough testing might be necessary.
At the most basic level, all you need to do is put your code online somewhere that is likely to last a long time. A more elaborate approach to making your research software more reusable is by following the FAIR Principles for Research Software (FAIR4RS Principles) {cite:ps}`ChueHong2021FAIR4RS`.

When we talk about making code reusable, it is useful to clarify what is we mean. In the {ref}`Table of Definitions for Reproducibility<rr-overview-definitions-reproducibility>` we defined reproducible research as using the same data and the same code.
However, when we talk about code re-use this can take many forms: we may want to run the exact same code (for compiled programming languages, this could even mean the exact same binary file), or we may want to modify the source code and extend it in some particular way to fit our needs.
Freire and Chirigati {cite:ps}`Freire2018Reproducibility` provide a framework of different levels of reproducibility, depending on what can be modified. They define the following levels of reproducibility: repeatable, re-runnable, portable, extendable and modifiable.

We can map the definitions of reproducibly on the Freire framework as follows:

| Freire framework | Definitions of reproducibly |
|------------------|---|
| Repeatable       | Reproducible (same data, same analysis) |
| Re-runnable      | Robust & Replicable (same code, different data/analysis/parameters) |
| Portable         | *Not considered* (Same code/data, different environment) |
| Extendable       | (partly) Generalisable |
| Modifiable       | (partly) Generalisable |

Portability was not previously considered, but for software a different environment (such as different hardware, operating system or even a fresh install on comparable hardware) may affect the ability for the software to work (for example it may affect dependencies).

Also, Generalisable encapsulates two concepts: Extendable (the ability to integrate with other software)
and Modifiable (the ability to change part of the implementation to extend its functionality).

In the rest of this chapter we provide list of recommendations you can follow to make sure your code is reusable.

(rr-code-reuse-recommendation-checklist)=
## How to make your code more reusable
This section contains a checklist of recommendations for making your software more reusable.
The {ref}`rr-code-reuse-recommendation-details` section contains a more in-depth explanation of each of these recommendations.
You can follow the recommendations that are more suitable for your type of software and skip the ones which are not relevant in your case.

### Repeatable recommendations
1. Make sure you can find it (in space)
1. Make sure you can find it (in time)
1. Make sure you can execute the same sequence of operations
1. Make sure your environment and sequence of operations is robust and no human is needed to replicate what was done
1. License your code
    - with a license that allows for reuse;
    - with a license compatible with the dependencies’ licenses
1. Make sure it is citable
1. Write useful documentation*
1. Include necessary data

### Re-runnable recommendations
1. Remove hardcoded bits and make the code modular
1. Test that the modules you made can take different types of input data or parameters
1. Turn the modules into a package/toolbox
1. Write useful documentation*

### Portable recommendations
1. Make sure you can recreate the environment where it lived
1. Write useful documentation*

### Extendable recommendations
1. Write useful documentation*

### Modifiable recommendations
1. Make sure your code is readable by humans
1. Make sure comments are present
1. Write useful documentation*

The observant reader might will notice that `Write useful documentation` is mentioned for every level of reuse.
This is because different levels of documentation are required for different levels of reuse.

### Different documentation requirements for different levels of reuse
Writing useful documentation is an important requirement for all levels of reuse.
However, for the different levels of reuse, there are different documentation requirements:

The documentation:
- explains usage, specifying:
  - what the software does; (required for repeatable)
  - how it can be used; (required for repeatable)
  - what options/parameters are available. (required for repeatable)
- contains examples of how to run it. (required for repeatable)
- has installation instructions, including good descriptions of:
  - the hardware it depends on (for example GPUs); (required for portable)
  - the operating system the software has been tested on; (required for portable)
  - software requirements (such as libraries and shell settings). (required for portable)

(rr-code-reuse-recommendation-details)=
## Recommendations for reusable code
Make sure you (or somebody else) can re-use your code to do the same exact thing you did.
The {ref}`rr-code-reuse-recommendation-checklist` section contains a checklist of recommendations for making your software more reusable.
In this section contains a more in-depth explanation of each of these recommendations, with pointers to other relevant parts of this guide.

### Repeatable recommendations
At this stage, you might not even need to be able to open the code and read it, you just want to make sure you can re-run all the needed steps and obtain the same results you had.

#### 1. Make sure you can find it (in space)
Your code must be stored publicly and shared with collaborators. It has an unique persistent identifier, so that everyone can find it and access it.

**See also**: {ref}`rr-vcs`

#### 1. Make sure you can find it (in time)
Ideally the temporal evolution of the code is documented with version control. This allows you to retrieve a specific version from the past.

**See also**: {ref}`rr-vcs`

#### 1. Make sure you can execute the same sequence of operations
Often the human who set up the environment is also the one who wrote the code and the one who knows the exact order of steps needed to be able to re-run the code and reproduce the results.
This could surely be carefully documented for another human to re-do it.

**See also**: [CodeRefinery lesson on Reproducible Research](https://coderefinery.github.io/reproducible-research/)

#### 1. Make sure your environment and sequence of operations is robust and no human is needed to replicate what was done
You do not want to depend on humans. They tend to make errors even if they do not have bad intentions. So you want your environment to be scripted and be re-created when needed and you want your sequence of operations to be run by a pipeline script that glues together all the sequence of steps.

**See also**: {ref}`rr-renv-options`

#### 1. License your code
Make sure you attach a license to your code and specify how you want to be cited when people re-use it.
Consider using a permissive license that allows for reuse.
Also, you should choose a license which is compatible with the licenses of libraries or packages your software depends on.

**See also**: {ref}`rr-licensing-software`, {ref}`rr-licensing-software-permissive`, {ref}`rr-licensing-compatibility`

#### 1. Make sure it is citable
Make sure to specify how you want to be cited when people re-use it.

**See also**: {ref}`cm-citable-cite-software`

#### 1. Include necessary data
If the software depends on any sort of data, the data should be available

**See also**: {ref}`rr-rdm-data`

### Re-runnable recommendations
Make sure you (or others) can re-use it to do the thing you did, but with different data/different parameters

#### 1. Remove hardcoded bits and make the code modular
You do not want to have details specific of your data or analysis parameters hardcoded into the code.
If something can become a reusable function, separate it from the hardcoded parameters and turn it into something (re)usable on its own.
Make the modules pure: given the same input, a pure function always returns the same value.

**See also**: [CodeRefinery Modular Code Development lesson](https://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md/#1)

#### 1. Test that the modules you made can take different types of input data or parameters
You might not know yet how your code will be re-used in the future, but you can prevent how it should not be used if you can test which parameters are allowed.

**See also**: [CodeRefinery lesson on Automated testing](https://coderefinery.github.io/testing/motivation/)

#### 1. Turn the modules into a package/toolbox
Separate even more the specifics of your project with the bits that can be reused in other of your projects or by other people.

**See also**: {ref}`rr-renv-package`, [Packaging software](https://scicomp.aalto.fi/scicomp/packaging-software/), [Software packaging in Python](https://aaltoscicomp.github.io/python-for-scicomp/packaging/)

### Portable recommendations
Portability refers to the ability to transfer software to a new environment.
This could refer to an identical (but not the same) machine, but it can also refer to a new hardware architecture, operating system and such.
Both of these are important for software reuse.

#### 1. Make sure you can recreate the environment where it lived
The environment is a fragile snapshot in time which silently accompanies the code.
It can include the human who operated the software, the steps the human did to prepare the data, the hardware, the OS, the libraries, external packages/toolboxes/dependencies.
All this can be carefully documented for another human to re-do all the same exact steps.

**See also**: {ref}`rr-renv`

### Extendable and Modifiable recommendations
Make sure others can build on your code to extend it and improve it.

#### 1. Make sure your code is readable by humans
It often pays more to write code for other humans so they can read it (including your future self).
A cryptic oneliner with obscure variable names is not any faster or more efficient than splitting the one liner into multiple steps with readable variable names that make sense.
Furthermore, using coding conventions will help other readers.

**See also**: {ref}`rr-code-style-and-formatting`, {ref}`rr-code-quality-advantages`

#### 1. Make sure comments are present
Write comments before writing the actual code. Imagine that somebody could just read the comments and skip all the code bits between comments and get a full picture of what is going on as if they read the whole code.
