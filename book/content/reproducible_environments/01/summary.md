<a name="Summary"></a>

## Summary

Every computer has its own unique computational environment consisting of its operating system, what software it has installed, what versions of software packages are installed, and other features that we will describe later. If a research project is carried out on one computer and then that project and all its associated files are transferred to a different computer, there is no guarantee the analysis will even be able to run, let alone generate the same results, if the analysis is dependent on any of the considerations listed above.

In order for research to be reproducible, the computational environment that it was conducted in must be captured in such a way that it can be replicated by others. This chapter describes a variety of methods for capturing computational environments and gives guidance on their strengths and weaknesses.

<a name="What_is_a_computational_environment"></a>

### What is a computational environment?

In broad terms, the computational environment is the system where a program is run. This includes features of hardware (e.g. numbers of cores in any CPUs) and features of software (e.g. the operating system, programming languages, supporting packages and other pieces of software that are installed, and their versions and configuration).

Software versions are often defined via [semantic versioning](https://semver.org). In this system three numbers, e.g 2.12.4 are used to define each version of a piece of software. When a change is made to the software its version is incremented. These three numbers follow the pattern MAJOR.MINOR.PATCH, and are incremented as follows:

- MAJOR: significant changes
- MINOR: to add functionality
- PATCH: for bug fixes

<a name="How_this_will_help_you_why_this_is_useful"></a>

## How this will help you/ why this is useful

Let's go though an example of why computational environments are important. Say I have a very simple Python script:

```
a = 1
b = 5
print(a/b)
```

One divided by five is `0.2`, and this is what is printed if the script is run using Python 3. However, if a slightly older version of Python; Python 2 is used, the result printed is `0`. This is because integer division is applied to integers in Python 2, but (normal) division is applied to all types, including integers, in Python 3.

Therefore this extremely simple script returns _different_ answers depending on the computational environment in which it is run. Using the wrong version of Python is easy to do, and demonstrates how a perfectly valid piece of code can give different results depending on its environment. If such issues can impact a simple script like this, imagine how many could appear in a complex analysis procedure which may involve thousands of lines of code and dozens of dependent packages.

It is vital for researchers to understand and capture the computational environments in which they are conducting their work, as it has the potential to impact three parties:

- The researcher themselves. The researcher's working environment evolves over time as they update software, install new software, and move to different computers. If the project environment is not captured and the researcher needs to return to that project after months or years (as is common in research), they will be unable to confidently do so as they will have no way of knowing what changes to the environment have occurred and what impact those changes might have on their ability to run the code, and on the results.
- Collaborators. Much research is now collaborative, and conducting research in multiple different computational environments opens up a minefield of potential bugs. Trying to fix these kinds of issues is often time consuming and frustrating as researchers have to figure out what the differences between computational environments are, and their effects. Worse, some bugs may remain undetected, potentially impacting the results.
- Science itself. Scholarly research has evolved significantly over the past decade, but the same cannot be said for the methods by which research processes are captured and disseminated. In fact, the primary method for dissemination - the scholarly publication - is largely unchanged since the advent of the scientific journal in the 1660s. This is no longer sufficient to verify, reproduce, and extend scientific results. Despite the increasing recognition of the need to share all aspects of the research process, scholarly publications today are often disconnected from the underlying analysis and, crucially, the computational environment that produced the findings. For research to be reproducible researchers must publish and distribute the entire contained analysis, not just its results. The analysis should be _mobile_. Mobility of compute is defined as the ability to define, create, and maintain a workflow locally while remaining confident that the workflow can be executed elsewhere. In essence, mobility of compute means being able to contain the entire software stack, from data files up through the library stack, and reliably move it from system to system. Any research that is limited to where it can be deployed is instantly limited in the extent that it can be reproduced.

This chapter will describe how to capture, preserve and share computational environments along with code to ensure research is reproducible.
