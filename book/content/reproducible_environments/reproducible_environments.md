# Reproducible environments

## Prerequisites / recommended skill level

| Prerequisite                                                                                  | Importance | Notes                                                                                    |
| --------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------- |
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Necessary  | Experience with downloading software via the command line is particularly useful         |
| [Version control](/version_control/version_control)                                           | Helpful    | Experience using git and GitHub are helpful for the section on [Binder](#Binder_section) |

A tutorial on working via the command line can be found
[here](https://programminghistorian.org/en/lessons/intro-to-bash).

Recommended skill level: intermediate-advanced.

## Table of contents

- [Summary](#Summary)
  - [What is a computational environment?](#What_is_a_computational_environment)
- [How this will help you/why this is useful](#How_this_will_help_you_why_this_is_useful)
- [Summary of ways to capture computational environments](./01/options#Summary_of_ways_to_capture_computational_environments)
  - [Package management systems outline](./01/options#Package_management_systems_outline)
  - [Binder outline](./01/options#Binder_outline)
  - [Virtual machines outline](./01/options#Virtual_machines_outline)
  - [Containers outline](./01/options#Containers_outline)
- [Package management systems](./02/package-management#Package_management_systems)
  - [What does Conda do?](./02/package-management#What_does_Conda_do)
  - [Installing Conda](./02/package-management#Installing_Conda)
  - [Making and using environments](./02/package-management#Making_and_using_environments)
  - [Deactivating and deleting environments](./02/package-management#Deactivating_and_deleting_environments)
  - [Installing and removing packages within an environment](./02/package-management#Installing_and_removing_packages_within_an_environment)
  - [Exporting and reproducing computational environments](./02/package-management#Exporting_and_reproducing_computational_environments)
- [YAML files](./03/yaml#YAML_files)
  - [YAML syntax](./03/yaml#YAML_syntax)
    - [Scalars](./03/yaml#Scalars)
    - [Lists and Dictionaries](./03/yaml#Lists_and_Dictionaries)
    - [YAML gotchas](./03/yaml#YAML_gotchas)
  - [How to use YAML to define computational environments](./03/yaml#How_to_use_YAML_to_define_computational_environments)
  - [Security issues](./03/yaml#Security_issues)
- [Binder](./04/binder#Binder_section)
  - [Disambiguation](./04/binder#Disambiguation)
  - [Creating a Binder for a project](./04/binder#Creating_a_binder_for_a_project)
    - [Step 1: Specify your computational environment](./04/binder#Step_1_Specify_your_computational_environment)
    - [Step 2: Put your code on GitHub](./04/binder#Step_2_Put_your_code_on_GitHub)
    - [Step 3: Generate a link to a Binder of your project](./04/binder#Step_3_Generate_a_link_to_a_Binder_of_your_project)
  - [Including data in a Binder](./04/binder#Including_data_in_a_Binder)
    - [Small public files](./04/binder#Small_public_files)
    - [Medium public files](./04/binder#Medium_public_files)
    - [Large public files](./04/binder#Large_public_files)
- [Virtual machines](./05/virtual-machines#Virtual_machines)
  - [What are virtual machines?](./05/virtual-machines#What_are_virtual_machines)
  - [Using virtual machines for reproducible research](./05/virtual-machines#Using_virtual_machines_for_reproducible_research)
    - [Setting up a virtual machine](./05/virtual-machines#Setting_up_a_virtual_machine)
    - [Starting a virtual machine](./05/virtual-machines#Starting_a_virtual_machine)
    - [Sharing virtual virtual machines](./05/virtual-machines#Sharing_virtual_virtual_machines)
- [Containers](./06/containers#Containers_section)
  - [What are containers?](./06/containers#What_are_containers)
  - [What are images](./06/containers#What_are_images)
  - [What is Docker?](./06/containers#What_is_Docker)
  - [Installing Docker](./06/containers#Installing_Docker)
  - [Key commands](./06/containers#Key_commands)
  - [Writing Dockerfiles](./06/containers#Writing_Dockerfiles)
    - [WORKDIR](./06/containers#WORKDIR)
    - [Other commands](./06/containers#Other_commands)
  - [Building images and .dockerignore files](./06/containers#Building_images_and_dockerignore_files)
  - [Sharing images](./06/containers#Sharing_images)
  - [Singularity](./06/containers#Singularity)
  - [Copying files to and from containers](./06/containers#Copying_files_to_and_from_containers)
  - [Volumes](./06/containers#Volumes)
- [Checklist](./07/checklist#Checklist)
- [What to learn next](./08/resources#What_to_learn_next)
- [Further reading](./08/resources#Further_reading)
- [Definitions/glossary](./08/resources#Definitions_glossary)
- [Bibliography](./08/resources#Bibliography)

<a name="Summary"></a>

## Summary

Every computer has its own unique computational environment consisting of its operating system, what software it has
installed, what versions of software packages are installed, and other features that we will describe later. If a
research project is carried out on one computer and then that project and all its associated files are transferred to a
different computer, there is no guarantee the analysis will even be able to run, let alone generate the same results, if
the analysis is dependent on any of the considerations listed above.

In order for research to be reproducible, the computational environment that it was conducted in must be captured in
such a way that it can be replicated by others. This chapter describes a variety of methods for capturing computational
environments and gives guidance on their strengths and weaknesses.

<a name="What_is_a_computational_environment"></a>

### What is a computational environment?

In broad terms, the computational environment is the system where a program is run. This includes features of hardware
(such as the numbers of cores in any CPUs) and features of software (such as the operating system, programming languages,
supporting packages and other pieces of software that are installed, and their versions and configuration).

Software versions are often defined via [semantic versioning](https://semver.org). In this system three numbers, e.g
2.12.4 are used to define each version of a piece of software. When a change is made to the software its version is
incremented. These three numbers follow the pattern MAJOR.MINOR.PATCH, and are incremented as follows:

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

One divided by five is `0.2`, and this is what is printed if the script is run using Python 3. However, if a slightly
older version of Python; Python 2 is used, the result printed is `0`. This is because integer division is applied to
integers in Python 2, but (normal) division is applied to all types, including integers, in Python 3.

Therefore this extremely simple script returns _different_ answers depending on the computational environment in which
it is run. Using the wrong version of Python is easy to do, and demonstrates how a perfectly valid piece of code can
give different results depending on its environment. If such issues can impact a simple script like this, imagine how
many could appear in a complex analysis procedure which may involve thousands of lines of code and dozens of dependent
packages.

It is vital for researchers to understand and capture the computational environments in which they are conducting their
work, as it has the potential to impact three parties:

- The researcher themselves. The researcher's working environment evolves over time as they update software, install new
  software, and move to different computers. If the project environment is not captured and the researcher needs to
  return to that project after months or years (as is common in research), they will be unable to confidently do so as
  they will have no way of knowing what changes to the environment have occurred and what impact those changes might
  have on their ability to run the code, and on the results.
- Collaborators. Much research is now collaborative, and conducting research in multiple different computational
  environments opens up a minefield of potential bugs. Trying to fix these kinds of issues is often time consuming and
  frustrating as researchers have to figure out what the differences between computational environments are, and their
  effects. Worse, some bugs may remain undetected, potentially impacting the results.
- Science itself. Scholarly research has evolved significantly over the past decade, but the same cannot be said for the
  methods by which research processes are captured and disseminated. In fact, the primary method for dissemination - the
  scholarly publication - is largely unchanged since the advent of the scientific journal in the 1660s. This is no
  longer sufficient to verify, reproduce, and extend scientific results. Despite the increasing recognition of the need
  to share all aspects of the research process, scholarly publications today are often disconnected from the underlying
  analysis and, crucially, the computational environment that produced the findings. For research to be reproducible
  researchers must publish and distribute the entire contained analysis, not just its results. The analysis should be
  _mobile_. Mobility of compute is defined as the ability to define, create, and maintain a workflow locally while
  remaining confident that the workflow can be executed elsewhere. In essence, mobility of compute means being able to
  contain the entire software stack, from data files up through the library stack, and reliably move it from system to
  system. Any research that is limited to where it can be deployed is instantly limited in the extent that it can be
  reproduced.

This chapter will describe how to capture, preserve and share computational environments along with code to ensure
research is reproducible.
