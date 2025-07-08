(rr-code-reuse)=
# Reusable Code
Your software project could range from a small script you use for data processing to a notebook used for data analysis, or a software library implementing your algorithms.
Regardless of how big or small your software project is, it is important to make your code reusable.

Different types of software have different requirements for being reusable: for a small script, having sufficient documentation might be enough, while for a mission critical software library, thorough testing might be necessary.
At the most basic level, all you need to do is put your code online somewhere that is likely to last a long time. 
A more elaborate approach to making your research software more reusable is by following the FAIR Principles for Research Software (FAIR4RS Principles) {cite:ps}`ChueHong2021FAIR4RS`.

When we talk about making code reusable, it is useful to clarify what we mean. 
In the {ref}`Table of Definitions for Reproducibility<rr-overview-definitions-reproducibility>` we defined reproducible research as using the same data and the same code.
However, when we talk about code re-use this can take many forms: we may want to run the exact same code (for compiled programming languages, this could even mean the exact same binary file), or we may want to modify the source code and extend it in some particular way to fit our needs.
Freire and Chirigati {cite:ps}`Freire2018Reproducibility` provide a framework of different levels of reproducibility, depending on what can be modified. 
They define the following levels of reproducibility: repeatable, re-runnable, portable, extendable and modifiable.

We can map the definitions of reproducibly on the Freire framework as follows:

| Freire framework | Definitions of reproducibly |
|------------------|---|
| Repeatable       | Reproducible (same data, same analysis) |
| Re-runnable      | Robust & Replicable (same code, different data/analysis/parameters) |
| Portable         | *Not considered* (same code/data, different environment) |
| Extendable       | (partly) Generalisable |
| Modifiable       | (partly) Generalisable |

Portability was not previously considered, but for software a different environment (such as different hardware, operating system or even a fresh install on comparable hardware) may affect the ability for the software to work (for example it may affect dependencies).

Also, Generalisable encapsulates two concepts: Extendable (the ability to integrate with other software)
and Modifiable (the ability to change part of the implementation to extend its functionality).

In the rest of this chapter we provide list of recommendations you can follow to make sure your code is reusable.
