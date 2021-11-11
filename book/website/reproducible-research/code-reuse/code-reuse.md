(cr-code-reuse)=
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

Portability was not previously considered, but for software a different environment (hardware, operating system, etc) may affect the ability for the software to work (e.g. it may affect dependencies).

Also, Generalisable encapsulates two concepts: Extendable (the ability to integrate with other software)
and Modifiable (the ability to change part of the implementation to extend its functionality).

In the rest of this chapter we provide list of recommendations you can follow to make sure your code is reusable.

## How to make your code more reusable
This section contains a checklist of recommendations for making your software more reusable.
The {ref}`cr-code-reuse-recommendation-details` section contains a more in-depth explanation of each of these recommendations. You can follow the recommendations that are more suitable for your type of software and skip the ones which are not relevant in your case.

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
1. If the software depends on any sort of data, the data should be available

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

repeatable, re-runnable, portable, extendable and modifiable

The documentation:
- explains usage, specifying:
  - what the software does; (required for repeatable)
  - how it can be used; (required for repeatable)
  - what options/parameters are available. (required for repeatable)
- contains examples of how to run it. (required for repeatable)
- has installation instructions, including good descriptions of:
  - the hardware it depends on (e.g. GPUs); (required for portable)
  - the operating system the software has been tested on; (required for portable)
  - software requirements (libraries, shell settings, etc). (required for portable)

(cr-code-reuse-recommendation-details)=
## Recommendations for reusable code
UNDER CONSTRUCTION
