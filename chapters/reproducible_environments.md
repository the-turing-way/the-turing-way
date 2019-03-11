# Reproducible environments

- Ways to capture computational environments
  - Very quick runthrough with advice on **which to use for which circumstances**
  - Virtual machines
    - ?
  - Images and Containers
    - What are they
    - How to use Docker to make/share images and run containers (warn need to be ok with it being open unless dockerhub)
    - **Are there less arduous ways of generating Dockerfiles/images than hand writing them? Yes, build on previous well tested ones**
    - **Are there standard structures for Dockerfiles/how does a novice know what to include?**
    - Mention Singularity (+ others maybe) and give a quick pros/cons.

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| -------------|------------|-------|
| Experience with the command line | Necessary | Experience with downloading software via the command line is particularly useful |
| Version control | Helpful | Particularly with using version control via GitHub. Only important for some subsections of this chapter. |

A tutorial on working via the command line can be found [here](https://programminghistorian.org/en/lessons/intro-to-bash).

Recommended skill level: intermediate-advanced.

## Table of contents

- [Package management systems](#Package_management_systems)
    - [What does Conda do?](#What_does_Conda_do)
    - [Installing Conda](#Installing_Conda)
    - [Making and using environments](#Making_and_using_environments)
    - [Deactivating and deleting environments](#Deactivating_and_deleting_environments)
    - [Installing and removing packages within an environment](#Installing_and_removing_packages_within_an_environment)
    - [Exporting and reproducing computational environments](#Exporting_and_reproducing_computational_environments)
- [YAML files](#YAML_files)
    - [YAML syntax](#YAML_syntax)
        - [Scalars](#Scalars)
        - [Lists and Dictionaries](#Lists_and_Dictionaries)
        - [YAML gotchas](#YAML_gotchas)
    - [How to use YAML to define computational environments](#How_to_use_YAML_to_define_computational_environments)
    - [Security issues](#Security_issues)
- [Binder](#Binder)
    - [Disambiguation](#Disambiguation)
    - [Creating a binder for a project](#Creating_a_binder_for_a_project)
        - [Step 1: Specify your computational environment](#Step_1_Specify_your_computational_environment)
        - [Step 2: Put your code on GitHub](#Step_2_Put_your_code_on_GitHub)
        - [Step 3: Generate a link to a Binder of your project](#Step_3_Generate_a_link_to_a_Binder_of_your_project)
    - [Including data in a Binder](#Including_data_in_a_Binder)
        - [Small public files](#Small_public_files)
        - [Medium public files](#Medium_public_files)
        - [Large public files](#Large_public_files)
- [Virtual machines](#Virtual_machines)
- [Containers](#Containers)



## Summary
> easy to understand summary - a bit like tl;dr


### What is a computational environment?

Computational environment is (in broad terms) the system setup where a program is being run. This includes features of hardware (e.g. numbers of cores in any CPUs) and features of software (e.g. the operating system, what programming languages are installed, which supporting packages/versions of those packages are included, what other pieces of software are installed and how are they configured).

Software versions are often defined via [semantic versioning](https://semver.org). In this system three numbers, e.g 2.12.4 are used to define each version of a piece of software. When a change is made to the software then its version is incremented. These three numbers follow the pattern MAJOR.MINOR.PATCH, and are incremented as follows:

- MAJOR: significant changes
- MINOR: to add functionality
- PATCH: for bug fixes

### Materials used

- [semantic versioning](https://semver.org)

## How this will help you/ why this is useful

Let's go though an example of why computational environments are important. Say I have a very simple python script:

```
a = 1
b = 5
print(a/b)
```

One divided by five is `0.2`, and that is what is printed if this script is run using python 3. However if a slightly older version of python, python 2, is used the result printed is `0` because both a and b are integers so in python 2 an integer is returned. Therefore this simple, simple script returns *different* answers depending on the computational environment it is run in. This is a mistake that would be very easy to make, and demonstrates how a perfectly valid piece of code can output different results depending on the environment it is run in. If such bugs can impact a simple script like this you can only imagine how many could appear in a complex analysis procedure which may involve thousands of lines of code and dozens of dependent packages/pieces of software.

As such it is vital for researcher to understand and capture the computational environments they are conducting their work in, as it has the potential to impact three parties:

- The researcher themselves. If the environment is not captured and a research needs to return to a project after months or years (as is common in research) they will be unable to confidently do so as they will have no way of knowing what the potential changes to the environment are or what impact they have on the results. That is if they are still able to run their analysis in the modified computational environment, which may or may not be the case.   
- Collaborators. Much research is now collaborative, and conducting research in multiple different computational environments, potentially even at different institutions opens up a minefield of potential bugs. Trying to fix these kinds of issues is often time consuming and frustrating as researchers have to figure out what the differences between computational environment are, and their effects. Worse, some bugs may remain undetected potentially impacting the results.
- Science itself. Scholarly research has evolved significantly over the past decade, the same cannot be said for the methods by which research processes are captured and disseminated. In fact, the primary method for dissemination – the scholarly publication –is largely unchanged since the advent of the scientific journal in the 1660’s. This is no longer sufficient to verify, reproduce, and extend scientific results. Despite the increasing recognition of the need to share all aspects of the research process, scholarly publications today are often disconnected from the underlying analysis and, crucially, the computational environment that produced the findings. For research to be reproducible researchers must publish and distribute the entire contained analysis not just its results. The analysis should be *mobile*. Mobility of compute is defined as the ability to define, create, and maintain a workflow locally while remaining confident that the workflow can be executed elsewhere. In essence, mobility of compute means being able to contain the entire software stack, from data files up through the library stack, and reliability move it from system to system. Any research that is limited to where it can be deployed is instantly limited in the extent that it can be reproduced.

This chapter will describe how to capture, preserve and share computational environments along with code to ensure research is reproducible.

### Materials used

- [A. Brinckman, et al., Computing environments for reproducibility: Capturing the "Whole Tale", Future Generation Computer Systems (2018), https://doi.org/10.1016/j.future.2017.12.029](https://www.sciencedirect.com/science/article/pii/S0167739X17310695) **Attribution 4.0 International (CC BY 4.0)**
- [Paper presenting singularity](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) **CC0 1.0 Universal (CC0 1.0)**

## Summary of ways to capture computational environments


<table>
  <tr>
    <th></th>
    <th></th>
    <th colspan="2">Important transfer machine</th>
  </tr>
  <tr>
  <th></th>
  	<td></td>
    <td>Yes</td>
    <td>No</td>
  </tr>
  <tr>
    <th rowspan="2">Complex requirements</th>
    <td>Yes</td>    
    <th>Virtual Machine</th>
    <th>Containers</th>
  </tr>
  <td>No</td>
  <th>Binder</th>
  <th>Conda</th>
  <tr>
  </tr>
</table>

There are a number of ways to capture a computational environment, and which is the most appropriate for you will depend  on the nature of your project. If you are working with languages such as Python and R which have a number of tools for freezing and exporting environments as YAML files (discussed later in this chapter) then using one of those tools is likely the best course of action.

*Outline other and why*


- As always prevention is better than a cure! If you can install the specific version at the time of running and not up date it.
  - requirements.txt say install e.g. matplotlib
  - Breaks because don't have the right version of matplotlib
  - install packages that require specific versions of other packages, dependancies.
  - Useful to have different environments for different projects so that they don't go out of date! https://conda.io/docs/user-guide/tasks/manage-environments.html
  - Local computational environments
    - Python `virtualenv` and `venv`, `conda` environments
    - Equivalent for R


The advent of virtual machines [4, 5] introduced the exciting reality than an entire environment, including software dependencies, libraries, runtime code, and data, could be encapsulated and run anywhere. Virtual machines, however, also introduced large computational overhead due to the required level of virtualization for emulating the OS and kernel. With the addition of lightweight virtualization features to the Linux kernel (e.g., namespaces) a new lightweight virtualization, containers [15, 16], became possible to implement. Implementations such as Docker, one of the container solutions made open source in 2013 [15, 16], offered additional improvements over standard virtual machines. Containers could share resources with the host without incurring much of the performance penalties of hardware-level virtualization [17].

Researchers can develop reproducible containers on their local machines, providing a simple way to collaborate on code or applications without the hassle of having different software versions or broken dependencies. Containers are ideal not just for the final analysis, but for the development of it. A user is most comfortable working with his or her text editor, programs, and environment of choice, and containers make it possible to work locally and develop in a specific environment simultaneously.

If you need to work with HPC containers save having to install a whole bunch of stuff on the cluster before you can, and installing may not even be possible if you need to download form the internet.

One of the major factors that prevents Docker from being the standard container technology in HPC is its security concerns. From an IT security perspective, a machine can be considered compromised if any user is able to run arbitrary code as the root user. While Docker takes steps to mitigate the risk of allowing users to run arbitrary code, there is a fatal design flaw that limits Docker’s ability to run in HPC environments: for every container that Docker runs, the container process is spawned as a child of a root owned Docker daemon. As the user is able to directly interact with and control the Docker daemon, it is theoretically possible to coerce the daemon process into granting the users escalated privileges. Any user being able to escalate up to system administrator status, a user called “root”, would introduce unthinkable security risks for a shared compute environment.
[Paper presenting singularity](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) **CC0 1.0 Universal (CC0 1.0)**

<a name="Package_management_systems"></a>
## Package management systems

Package managers, as you may deduce, manage and keep track of the different software packages (and their versions) that you install in an environment. There are quite a few to choose from, for example Yum, Zypper, dpkg, and Nix (which will be mentioned briefly later in the [Binder](#Binder) section). We're going to focus on Conda, which has three main useful functionalities.

<a name="What_does_Conda_do"></a>
### What does Conda do?

Conda allows users to create any number of environments which are entirely separate, and to quickly and easily change between them. For example say a researcher has a project, Project One, which has its own environment defined by Conda i.e. a set of packages and versions of those packages:

| Package name | Version |
| ------------ | ------- |
| Package A    | 1.5.2   |
| Package B    | 2.1.10  |
| Package C    | 0.7.9   |

Later the researcher starts Project Two in its own environment:

| Package name | Version |
| ------------ | ------- |
| Package B    | 2.1.10  |
| Package C    | 1.2.4   |
| Package D    | 1.5.2   |
| Package E    | 3.7.1   |

Note here that version of package C used in Project Two has been updated from the version used in Project One. If these project environments were not separate then the researcher would have the choice of:

- A) Using the older version of package C forever and not benefiting from updates and bugfixes in later versions.
- B) Installing the updated version of the package and hoping that it doesn't impact Project One.
- C) Installing the updated version of the package for use in Project Two then uninstalling it and reinstalling the old one whenever they need to do work on Project One. This would be extremely annoying, and is a step that risks being forgotten.  

All of these options are extremely poor, hence the utility of Conda for creating distinct environments which can be easily swapped between.

Conda can also be used to easily capture and export computational environments, and it can go in the other direction too. I.e. it can generate computational environments from configuration files, which is useful for recreating someone else's environment.

Another benefit of Conda is that it offers much greater flexibility to users that do not have admin privileges on the machines they are working on (as is very common when working with high performance computing facilities). Without Conda it is typically very difficult to install required software onto such machines. However because Conda creates and changes *new* environments rather than making changes to a machine's overall system environment admin privileges are not required.  

Finally, while Conda is python centric to a degree it is also well integrated for use with other languages, for example the base version of Conda includes the C++ standard library.

<a name="Installing_Conda"></a>
### Installing Conda

Note that these installation instructions are directed towards Linux systems. Instructions for installing Conda Windows or Mac systems can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

Go to [https://repo.continuum.io/miniconda/](https://repo.continuum.io/miniconda/) and download the latest Miniconda 3 installer for your system (32 bit or 64 bit), which will have like Miniconda_version_number.sh. Run the installer using
```
bash Miniconda_version_number.sh
```

You can check that Conda has installed successfully by typing
```
conda --version
```

which should output a version number.

<a name="Making_and_using_environments"></a>
### Making and using environments

Conda automatically installs a base environment with some python and non-python packages. It is possible to just work in this base environment, however it is a good practise to create a new environment for each project you start. To create an environment use `conda create --name your_project_env_name` followed by a list of packages to include, for example to create an environment called Project_One that includes the packages scipy and matplotlib:
```
conda create --name Project_One numpy matplotlib
```

When you create an environment you have to include at least one package. To create the environment with specific versions of certain (or all) packages use `=package_number`, e.g. to specify scipy 1.2.1 in the above environment
```
conda create --name Project_One scipy=1.2.1 matplotlib
```

When creating environments you can also specify versions of languages to install, for example to use Python 3.7.1 in the Project_One environment:
```
conda create --name Project_One python=3.7.1 scipy=1.2.1 matplotlib
```

Now that an envronment has been created it's time to activate (start using) it using `conda activate environment_name`, so in this example:
```
conda activate Project_One
```
Note that you may need to use `source` instead of `conda` if you're using an old version of conda.

Once an environment is activated you should see the environment name before each prompt in your terminal:
```
(Project_One) $ python --version
Python 3.7.1
```

<a name="Deactivating_and_deleting_environments"></a>
### Deactivating and deleting environments

You can deactivate (get out of) an environment using
```
conda deactivate
```

and remove an environment as show here for removing the Project_One environment
```
conda env remove --name Project_One
```

To check if an environment has been successfully removed you can look at a list of all the Conda environments on the system using
```
conda env list
```

However deleting an environment may not delete package files that were associated with it. This can lead to a lot of memory being wasted on packages that re no longer required. Packages that are no longer referenced by any environments can be deleted using
```
conda clean -pts
```

Alternatively you can delete an environment (such as Project_One) and its associated packages via:
```
conda remove --name Project_One --all
```

<a name="Installing_and_removing_packages_within_an_environment"></a>
### Installing and removing packages within an environment

Within an environment you can install more packages using
```
conda install package_name
```

and similarly you can remove them via
```
conda remove package_name
```

This is the best way to install packages from within Conda as it will also install a COnda-specific version of the package. However it is possible to use other methods if a Conda-specific version of a package is not available. For example `pip` is commonly used to install python packages, so a command like
```
pip install scipy
```

still works.

Although Python packages have been used in many of the examples given here Conda packages do not have to be Python packages, for example here the R base language is installed along with the R package r-yaml

```
conda create --name Project_One r-base r-yaml
```

A Conda channel is where it downloaded a package from. Common channels include Anaconda (a company which provides the `defaults` conda package channel), and conda-forge (a community-driven packaging endevour). You can explicitly install a package from a certain channel by specifying it like:

```
conda install -c channel_name package_name
```

<a name="Exporting_and_reproducing_computational_environments"></a>
### Exporting and reproducing computational environments

Conda environments can be exported easily to human-readable files called YAML files. YAML files are discussed in more detail [later](#YAML_files) in this chapter.

To export a conda environment to a file called `environment.yml` activate the environment and then run
```
conda env export > environment.yml
```

Similarly Conda environments can be created form YAML files like this via
```
conda env create -f environment.yml
```

This allows researchers to easily reproduce one another's computational environments. Note that the list of packages is not just those explicitly installed. It can include OS-specific dependency packages so environment files may require some editing to be portable.

Environments can also be cloned. This may be desirable, for example, if a researcher begins a new project and want to make a new environment to work on it in, but the new project's environment (at least initially) requires the same packages as another project's environment.

For example to clone the Project_One environment, and give this new environment the name Project_Two:
```
conda create --name Project_Two --clone Project_One
```

### Materials used
- [Package Managers](https://opensource.com/article/18/7/evolution-package-managers)
- [Talk by Will Furnass on Conda](https://github.com/willfurnass/conda-rses-pres/blob/master/content.md) **Attribution-NonCommercial-ShareAlike 4.0 International**

<a name="YAML_files"></a>
## YAML files

YAML is an indentation-based markup language which aims to be both easy to read and easy to write. Many projects use it for configuration files because of its readability, simplicity and good support for many programming languages. It can be used for a great many things including defining computational environments, and is well integrated with [Travis](https://travis-ci.org/) which is discussed in the chapter on continuous integration.

An a YAML file defining a computational environment might look something like this:
```
# Define the operating system as Linux
os: linux

# Use the xenial distribution of Linux
dist: xenial

# Use the programming language python
language: python

# Use version of python 3.2
python: 3.2

# Use the python package numpy and use version 1.16.1
packages:
  numpy:
    version: 1.16.1
```
Note that as you can see here that comments can be added by preceding them with a `#`.

<a name="YAML_syntax"></a>
### YAML syntax

A YAML document can consist of the following elements.

<a name="Scalars"></a>
#### Scalars

Scalars are ordinary values: numbers, strings, booleans.
```
number-value: 42
floating-point-value: 3.141592
boolean-value: true

# strings can be both 'single-quoted` and "double-quoted"
string-value: 'Bonjour'
```

YAML syntax also allows unquoted string values for convenience reasons:
```
unquoted-string: Hello World
```

<a name="Lists_and_Dictionaries"></a>
#### Lists and Dictionaries

Lists are collections of elements:

```
jedis:
  - Yoda
  - Qui-Gon Jinn
  - Obi-Wan Kenobi
  - Luke Skywalker
```

Every element of the list is indented and starts with a dash and a space.

Dictionaries are collections of `key: value` mappings. All keys are case-sensitive.

```
jedi:
  name: Obi-Wan Kenobi
  home-planet: Stewjon
  species: human
  master: Qui-Gon Jinn
  height: 1.82m
```

Note that a space after the colon is mandatory.

<a name="YAML_gotchas"></a>
#### YAML gotchas

Due to the format aiming to be easy to write and read, there're some ambiguities in YAML.

- **Special characters in unquoted strings:** YAML has a number of special characters you cannot use in unquoted strings. For example, parsing the following sample will fail:
  ```
  unquoted-string: let me put a colon here: oops
  ```
  Quote the string value makes this value unambiguous:
  ```
  unquoted-string: "let me put a colon here: oops"
  ```
  Generally, you should quote all strings that contain any of the following characters: `[] {} : > |`.
- **Tabs versus spaces for indentation:** do *not* use tabs for indentation. While resulting YAML can still be valid, this can be a source of many subtle
parsing errors. Just use spaces.

<a name="How_to_use_YAML_to_define_computational_environments"></a>
### How to use YAML to define computational environments

Because of their simplicity YAML files can be hand written. Alternatively they can be automatically generated as discussed [above](#Package_management_systems). From a YAML file a computational environment can be replicated in a few ways.

*Add link to virtual machine section*  

- **Manually.** It can be done manually by carefully installing the specified packages etc. Because YAML files can also specify operating systems and versions that may or may not match that of the person trying to replicate the environment this may require the use of a virtual machine.
- **Via package management systems such as Conda.** As [discussed](#Package_management_systems) as well as being able to generate YAML files from computational environments Conda can also generate computational environments from YAML files.

<a name="Security_issues"></a>
### Security issues

There is an inherent risk in downloading/using files you have not written to your computer, and it is possible to include malicious code in YAML files. Do not load YAML files or generate computational environments from them unless you trust their source.  

### Materials used

- [yaml tutorial](https://gettaurus.org/docs/YAMLTutorial/) **[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)**

<a name="Binder"></a>
## Binder

Below is a comic to help illustrate what Binder is, and we will expand on it here in the text.

**Step 1:** As you can see in step one there is a researcher that has completed a project and wants to share her work with anyone regardless of their computational environment. Note that Binder does not only have to be applied to finished projects, it can be used in exactly the same way to share projects that are in progress.

**Step 2:** The researcher's project contains many files of different types. In the comic the researcher is working on these files via a Jupyter notebook, and it is true that Binder is very well integrated with these notebooks. However if you are not familiar with these, not to worry, Binder can be used just as effectively without them.

**Step 3:** The researcher uploads her code to some publicly available repository, such as GitHub, where it can be accessed by others. She includes a file describing the computational environment required to run the project.

**Step 4:** Using [mybinder.org](https://mybinder.org) she generates a link. By clicking on this link anyone can access a "Binderized" version of her project. This means they will be taken to a copy of her project in their web browser that they can interact with. (By default this will not impact the researcher's own copy, though this setting to be changed if the research has access to a private [BinderHub](#Disambiguation) and wants others such as collaborators to be able to work on/modify the project via the Binder). This copy of the project they interact with will behave as if it is hosted in the environment the researcher specified in step 3, regardless of the computational environment of the person is accessing it from.

![binder_comic](../figures/binder_comic.png)

Figure credit: [Juliette Taka, Logilab and the OpenDreamKit project](https://opendreamkit.org/2017/11/02/use-case-publishing-reproducible-notebooks/)

To get an idea of what this looks like here's what a binder of a simple example project looks like. Files are listed and can be clicked on and modified by the person accessing the binder.

![binder_home](../figures/binder_home.png)

Users can also open terminals to run or otherwise interact with the files by clicking on "New" and then "Terminal" in the top right of the home binder screen shown above. Here this is used to run the analysis script in the example binder which performs a linear regression on some data:

![binder_terminal](../figures/binder_terminal.png)

As mentioned Binder is well integrated with Jupyter notebooks which can be opened by clicking on "New" and then under "Notebook" in the same way terminals can be opened. These may be more convenient for those working with graphical outputs, as shown here where one is used to run `make_plot.py` in the example Binder:

![binder_notebook](../figures/binder_notebook.png)

If R is installed in a bindr the option will also be available in the dropdown menu to open R Jupyter notebooks and RStudio sessions in the Binder.

<a name="Disambiguation"></a>
### Disambiguation

In this section there are a number of related terms, which will be outlined here for clarity:

- Binder: A sharable version of a project that can be viewed and interacted within a reproducible computational environment via a web browser.
- BinderHub: A service which generates Binders. Anyone can build a BinderHub if they so wish. An example or a reason someone may wish to do so is if they want to make a binder of a project which involves confidential files, and thus cannot be made public.
- [mybinder.org](https://mybinder.org): A public and free BinderHub. Because it is public you should not use it if your project requires any personal or sensitive information (such as passwords)
- Binderize: To make a Binder of a project.

<a name="Creating_a_binder_for_a_project"></a>
### Creating a binder for a project

Creating a Binderized version of a project involves three key steps which will be explained in this section:

1. Specify the computational environment
2. Put the project files somewhere publicly available (we will describe how to do this with GitHub)
3. Generate a link to a Binder of the project

For a list of sample repositories for use with Binder, see the [Sample Binder Repositories](https://mybinder.readthedocs.io/en/latest/sample_repos.html) page.

<a name="Step_1_Specify_your_computational_environment"></a>
#### Step 1: Specify your computational environment

If a project contains no file specifying the computational environment when a Binder is generated the environment will be the Binder default environment, (containing python 3.6) which may or may not be suitable for the project. However if it does contain a configuration file for the environment then the Binder will be generated with the specified environment. A full list of such files binder accepts with examples can be found [here](https://mybinder.readthedocs.io/en/latest/config_files.html), but here are some of the key ones, some of which are language-specific:

- environment.yml
    - Recall that environment.yml files were discussed in the [Package management systems](#Package_management_systems) section.
- Dockerfile
    - Dockerfiles will be discussed in the [Containers](#Containers) section, so will not be discussed further here.
- apt.txt
    - Dependencies that would typically installed via commands such as `sudo apt-get install package_name` should be listed in an apt.txt file, and will be automatically installed in the binder.
    - For example if a project uses Latex the apt.txt file should read
    ```
    texlive-latex-base
    ```  
    to install the base Latex package.
- default.nix
    - For those that use the [package management system](#Package_management_systems) Nix a default.nix can be a convenient way to capture their environment.
- requirements.txt (python)
    - For python users a requirements.txt file can be used to list dependent packages.
    - For example to have Binder install numpy this file would simply need to read:
    ```
    numpy
    ```
    - Specific package version can also be specified using an `==`, for example to have Binder install numpy version 1.14.5 then the file would be
    ```
    numpy==1.14.5
    ```
    - The requirement.txt file does not need to be hand written. Running the command `pip freeze > requirements.txt` will output a requirements.txt file that fully defines the python environment.
- runtime.txt
    - Used to specify a particular version of python of R for the Binder to use.
    - To specify which version of R to use specify find the date it was captured on [MRAN](https://mran.microsoft.com/documents/rro/reproducibility) and include it in the runtime.txt file as
    ```
    r-<YYYY>-<MM>-<DD>
    ```
    - To specify a version of python, similarly state the version in this file. For example to use Python 2.7 the file would need to read
    ```
    python-2.7
    ```
- install.R or DESCRIPTION (R/RStudio)
    - An install.R file lists the packages to be installed, for example to install the package tibble in the Binder:
    ```
    install.packages("tibble")
    ```
    - [DESCRIPTION files](https://cran.r-project.org/doc/manuals/r-release/R-exts.html#The-DESCRIPTION-file) are more typically used in the R community for dependency management.

<a name="Step_2_Put_your_code_on_GitHub"></a>
#### Step 2: Put your code on GitHub

GitHub is discussed at length in the chapter on version control, which you should refer to if you wish to understand more about this step. In this chapter we will give the briefest possible explanation. GitHub is a very widely used platform where you can make "repositories", and upload code, documentation, or any other files into them. To complete this step:

1. Make an account on [GitHub](https://github.com/).
2. Create a repository for the project you wish to make a Binder of.
3. Upload your project files (including the file you have created to specify your computational environment) to the repository and save ("commit" in the vocabulary of GitHub) them there.

Again, if you are unable to complete these steps refer to the chapter on version control for a fuller explanation.

<a name="Step_3_Generate_a_link_to_a_Binder_of_your_project"></a>
#### Step 3: Generate a link to a Binder of your project

Head to [https://mybinder.org](https://mybinder.org). You'll see a form that asks you to specify a repository for [mybinder.org](https://mybinder.org) to build. In the first field, paste the URL of the project's GitHub repository. It'll look something like this: `https://github.com/<your-username>/<your-repository>`

![mybinder_gen_link](../figures/mybinder_gen_link.png)

As you can see there are additional fields in this form, but these are optional are will not be discussed here.

Once the URL to the project to be Binderized is supplied two fields will be automatically populated on the screen depicted above:

- The "Copy the URL below and share your Binder with others" field, which provides a link to the binder which can be copied and shared by you.
- The "Copy the text below, then paste into your README to show a binder badge" field, which as described can be included by you in GitHub to create a button that allows anyone that accesses your project on GitHub to launch the Binder.

Finally, click the launch button. This will ask [mybinder.org](https://mybinder.org) to build the environment needed to run the project, note that this may take several minutes. You can click on the "Build logs" button to see the logs generated by the build process. These logs are helpful for resolving any issues that cause the build to fail, such as errors in the file defining the computational environment to be generated.

Once it has been built the Binder will be automatically launched, again this may take some time.

<a name="Including_data_in_a_Binder"></a>
### Including data in a Binder

There are a few ways to make data available in your Binder. Which is the best one depends on how big your data is and your preferences for sharing data. Note that the more data that is included include the longer it will take for a Binder to launch. Data also takes up storage space which must be paid for, so it is good to be considerate and minimise the data you include, especially on the publicly provided mybinder.org](https://mybinder.org).

<a name="Small_public_files"></a>
#### Small public files

The simplest approach for small data files that are public is to add them directly to your GitHub repository, i.e to include them along with the rest of your project files in the Binder. This works well and is reasonable for files with sizes up to maybe 10MB.

<a name="Medium_public_files"></a>
#### Medium public files

For medium sized files, a few 10s of megabytes to a few hundred megabytes, find some other place online to store them and make sure they are publicly available. Then add a file named postBuild (which is a shell script so the first line must be `#!/bin/bash`) in your project. In the postBuild file add a single line reading `wget -q -O name_of_your_file link_to_your_file`.

The postBuild file is used to execute commands when the files to produce the Binder are being generated. In this case it can be used to download your data into the files used to launch the binder.

<a name="Large_public_files"></a>
#### Large public files

The best option for large files is to use a library specific to the data format to stream the data as you are using it. There are a few restrictions on outgoing traffic from your Binder that are imposed by the team operating [mybinder.org](https://mybinder.org). Currently only connections to HTTP and Git are allowed. This comes up when people want to use FTP sites to fetch data. For security reasons FTP is not allowed on [mybinder.org](https://mybinder.org).

### Materials used

- [mybinder docs intro](https://github.com/jupyterhub/binder/blob/master/doc/introduction.rst) **[BSD 3-Clause](https://github.com/binder-examples/requirements/blob/master/LICENSE)**
- [Original zero to binder](https://github.com/Build-a-binder/build-a-binder.github.io/blob/master/workshop/10-zero-to-binder.md) **[BSD 3-Clause](https://github.com/binder-examples/requirements/blob/master/LICENSE)**
- [Sarah Gibson's zero to Binder](https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder.md) **MIT**
- [Zero to Binder](https://github.com/Build-a-binder/build-a-binder.github.io/blob/master/workshop/10-zero-to-binder.md)  **[BSD 3-Clause](https://github.com/binder-examples/requirements/blob/master/LICENSE)**

<a name="Virtual_machines"></a>
## Virtual machines

 Vagrant?

<a name="Containers"></a>
## Containers

<a name="What_are_containers"></a>
### What are containers?

Containers allow a researcher to package up an project with all of the parts it needs, such as libraries, dependencies, and system settings and ship it all out as one package. Anyone can then open up a container and work within it, viewing and interacting with the project as if the machine they are accessing it from is identical to the machine specified in the container- regardless of what their computational environment *actually* is. They are designed to make it easier to transfer projects between very different environments.

In a way, containers behave like a virtual machine. To the outside world, they can look like their own complete system. But unlike a virtual machine, rather than creating a whole virtual operating system, containers only contain the individual components they need in order to operate. This gives a significant performance boost and reduces the size of the application.

Containers are particularly useful way for reproducing research which relies on software to be configured in a certain way, and/or which makes use of libraries that vary between (or don't exist on) different systems. In summary containers are a more robust way of sharing reproducible research than, for instance, package management systems of Binder because they reproduce the entire system used for the research, not just the packages explicitly used by it. Their major downside is that due to their greater depth they are conceptually more difficult to grasp and produce than many other methods of replicating computational environments.

<a name="What_are_images"></a>
### What are images?

Images are the files used to generate containers. Humans don't make images, they write the recipes to generate images.

Think of it like this:

- A recipe file a human writes contains all the steps to generate a working version of the project and its computational environment, but no actual materials. Think of this as like a blueprint.
- Building an image takes that recipe and using it assembles all the packages, software libraries, configurations etc needed to make the fully fledged project and environment and bundles them up in a condensed lump. Think of images like a bit of flat pack furniture made using the blueprint.
- Containers take that image and assemble a full working version of the project inside its own little environment needed to run it. Think of this as assembling the bit of flat pack furniture.   

So if a researcher wants to allow others to reproduce their work they would need to write a recipe file, and use it to build an image of their project. They can then share this image file with anyone who wants to replicate their work. That person can then use the image to generate a container containing a working version of the project.

<a name="What_is_Docker"></a>
### What is Docker?

There are a number of different tools available for creating and working with containers. We will focus on Docker, which is widely used, but be aware that others such as Singularity also exist. Singularity is sometimes preferred for use on HPC systems as it does not need `sudo` permissions to be run, while Docker does.     

In Docker the recipe files used to generate images are known as Dockerfiles, and should be named `Dockerfile`.

[DockerHub](https://hub.docker.com/) hosts a great many pre-made images which can be downloaded and build upon, such as [images](https://hub.docker.com/_/ubuntu) of Ubuntu machines. This makes the process of writing Dockerfiles relatively easy since users very rarely need to start from scratch. However, this does leave a user vulnerable to similar security issues as were described in the section on [YAML files](#Security_issues):

- It is possible to include malicious code in Docker images
- It is possible for people producing images to unknowingly include software in them with security vulnerabilities

[This](https://opensource.com/business/14/7/docker-security-selinux) article goes deeper into the potential security vulnerabilities of containers and here is a [detailed breakdown](https://opensource.com/business/14/9/security-for-docker) of security features currently within Docker, and how they function. The best advice for using images built by others is as standard- only download and run something on your machine if it comes from a trusted source. DockerHub has "official image" badges for commonly used, verified images as shown here:

![Docker_official_image](../figures/docker_official_image.png)

<a name="Installing_Docker"></a>
### Installing Docker

Installers for Docker on a variety of different systems are available [here](https://docs.docker.com/install/). Detailed installation instructions are also available for a variety of operating systems such as [ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/), [debian](https://docs.docker.com/install/linux/docker-ce/debian/), [Macs](https://docs.docker.com/docker-for-mac/install/), and [Windows](https://docs.docker.com/docker-for-windows/install/).

<a name="Key_commands"></a>
### Key commands

Here are a few key commands for creating and working with containers.

- To build an image from a Dockerfile go to the directory where the Dockerfile is and run:
  ```
  sudo docker build tag=name_to_give_image
  ```
- To list the images on your system use
  ```
  sudo docker image ls
  ```
- To remove an image run
  ```
  sudo docker rmi image_name
  ```
- To open a container from an image run
  ```
  sudo docker run -i -t image_name
  ```
  The `-i -t` flags automatically open up an interactive terminal within the container so you can view and interact with the project files.
- To exit an interactive terminal use the command `exit`.
- To get a list of active containers with IDs run
  ```
  sudo docker container ls
  ```
- There are also three main commands used for changing the status of containers:
  - Pausing suspends the process running the container. Containers can be unpaused by replacing `pause` with `unpause`.
    ```
    sudo docker container_ID pause
    ```
  - Stopping a container terminates the process running it. A container must be stopped before it can be deleted.
    ```
    sudo docker container_ID stop
    ```
    A stopped container can be restarted by replacing `stop` with `restart`.
  - If `stop` does not work containers can be killed using
    ```
    sudo docker container_ID kill
    ```  
- To remove a container run
  ```
  sudo docker rm container_ID
  ```

<a name="Writing_Dockerfiles"></a>
### Writing Dockerfiles

Lets go through the anatomy of a very simple Dockerfile:
```
# Step 1: Set up the computational environment

# Set the base image
FROM ubuntu

# Install packages needed to run the project
RUN apt-get update
RUN apt-get install sudo
RUN sudo apt-get update
RUN sudo apt-get install -y python3.7
RUN sudo apt-get install -y python3-pip
RUN pip3 install numpy

#-----------------------

# Step 2: Include the project files in the image

# Make a directory called "project" to hold the project files
RUN mkdir project

# Copy files from the machine building the image into the image
COPY project_files/* project/
```

This looks complicated, but most of the lines in this example are comments (which are preceded by `#`s), There are only nine lines of actual code. The first of these is a `FROM` statement specifying a base image. All Dockerfiles require a FROM, even if it's just `FROM SCRATCH`.  All the following commands in a Dockerfile build upon the base image to make a functioning version of the researcher's project.

It is worth spending time carefully choosing an appropriate base image as doing do can reduce the amount of work involved in writing a Dockerfile dramatically. For example a collection of images with the R programming language included in them can be found [here](https://github.com/rocker-org/rocker-versioned). If a project makes use of R it is convenient to use one of these as a base image rather than spend time writing commands in your Dockerfile to install R.  

The biggest block of lines comes next, it's a series of `RUN` statements, which run shell command when building the image. In this block they are used to install the software necessary to run the project. Run commands can also be chained as follows if desired:
```
RUN command_to_do_thing_1 \
   command_to_do_thing_2 \
   command_to_do_thing_3 \
   command_to_do_thing_4
```

Another RUN statement is used to run the shell command `RUN mkdir project` which makes a directory called project in the container to host the files related to this project.

Finally the `COPY` command is used to copy the project files from the machine building the image into the image itself. The syntax of this command is `COPY file_to_copy location_in_container_to_copy_to`. In this example all the files in the "project_files" directory are included in the "project" file in the container. Note that you can only copy files from the directory where the Dockerfile is located, or subdirectories within it (in the example given here the project_files subdirectory).

The `ADD` command has the same capabilities as `COPY`, but it can also be used to add files not on the machine building the image. For example it can be used to include files hosted online by following ADD with a URL to the file. It is good practice to use `COPY` except where `ADD` is specifically required as the term `COPY` is more explicit about what is being done.

Here's what happens if a container is opened from an image called book_example built from the example above:

![container_example](../figures/container_example.png)

As you can see the directory "project" has been created, and if we look inside the project files "analysis.py" and "data.csv" have been copied into it. Because the software required for the project has already been included by the Dockerfile in the image the "analysis.py" script runs without any further software needing to be installed.

#### WORKDIR

This command can be used in Dockerfiles to change the current working directory. Commands that follow this in the Dockerfile will be applied within the new working directory unless/until another WORKDIR changes the working directory. When a container is opened with an interactive terminal the terminal will open in the final working directory. Here's a simple example of a Dockerfile that uses `WORKDIR`, and the container it generates.
```
# Basic setup
FROM ubuntu
RUN apt-get update

# Make a directory called A
RUN mkdir A

# Make the working directory A
WORKDIR A

# Make two directories, one called B_1 and one called B_2
RUN mkdir B_1
RUN mkdir B_2
```

![workdir_example](../figures/workdir_example.png)

WORKDIR should be used whenever changing directories is necessary when building an image. It may be tempting to use `RUN cd directory_name` instead as this syntax will be more familiar to those that commonly work via the command line, but this can lead to errors. After each `RUN` statement in a Dockerfile the image is saved, any following commands are applied to the image anew. As an example here is what happens in the above example if the `WORKDIR A` line is swapped for `RUN cd A`

![cd_example](../figures/cd_example.png)

All the directories have are in the top level in this case, rather than B_1 and B_2 being inside A. This is because the image was restarted after the `RUN cd A` command and opened at the top (root) level by default, so that is where the `mkdir B_1` and `mkdir B_2` commands took effect.

#### Other commands

Other commands that are sometimes used in Dockerfiles include:

- `CMD`: This is used to run commands as soon as the container is opened. To clarify this is different to RUN commands which are commands run as part of *setting up* a container. For example to have a welcome message when a container is opened from the image CMD could be used as follows:
  ```
  CMD ["echo","Welcome! You just opened this container!"]
  ```
  It's good practice to use CMD for any commands that need to be run before someone starts working in the container instead of forcing users to do run them themselves (and trusting that they will even know that they need to).
- `VOLUMES`: These will be discussed [later](#Volumes).
- `MAINTAINER`: information regarding the person that wrote the Dockerfile. Typically included at the top of a Dockerfile.
- `EXPOSE`: This includes ports that should be exposed, this is more relevant to people using Docker to share apps.
- `USER`: Change the user that a command is run as (useful for dropping privileges)

### Building images and .dockerignore files.

As mentioned in the [key commands](#Key_commands) section, to build an image open a terminal in the same directory as the Dockerfile to be used and run
```
sudo docker build tag=name_to_give_image
```

When an image is built everything in the Dockerfile's directory and below (this is called the "context") is sent to the Docker daemon to build the image. The deamon uses the Dockerfile and its context to build the image. If the context contains many large files which aren't needed for building the image (old datafiles, for example) then it is a waste of time sending them to the daemon, and doing do can make the process of building an image slow. Files cna be excluded from the context by listing them in a text file called .dockerignore, and it is good practise to do so.

The files do not need to be listed individually in the .dockerignore file. Here is an example of the contents of a .dockerignore file:
```
*.jpg
**/*.png
data_files/*
file_to_exclude.txt
```

This excludes from the context:
- All jpg files in the same directory as the Dockerfile file
- All png files in the same directory as the Dockerfile file *or any subdirectories within it*
- All files within the data_files directory
- The file named "file_to_exclude.txt"

### Sharing images

Docker images can be shared most easily via [DockerHub](https://hub.docker.com/), which requires an account. Say two researchers, Alice and Bob, are collaborating on a project and Alice wishes to share an image of some of her work with Bob.

To do this Alice must:

- Write a Dockerfile to produce an image of her work
- Build the image. She (being inventive) calls it image_name
- Go to DockerHub and sign up for an account. Say Alice (again, being inventive) chooses the username username_Alice    
- Log into DockerHub via the terminal on her machine using `sudo docker login`
- Tag the image of her project on her machine via the command line by supplying the name of the image and using the pattern `username/image_name:version`, so Alice runs the command:
  ```
  sudo docker tag image_name username_Alice/image_name:version_1
  ```
- Push the image to her DockerHub account using  `sudo docker tag push username_Alice/image_name:version_1`
- Alice's miage is now online and can be downloaded. Over to Bob...

Bob (assuming he already has Docker installed) can run Alice's image simply by running
```
sudo docker run -i -t username_Alice/image_name:version_1
```
Initially Docker will search for this image on Bob's machine, and when it doesn't find it it will *automatically* search DockerHub, download Alice's image, and open a container with Alice's work on Bob's machine.

### Copying files to and from running containers

- Move a file from my computer into the container using
  ```
  sudo docker cp file_name Sha_or_name_of_container:path_to_pyt_file/file_name
  ```
- Created a file inside the container, want to get it out, ran
  ```
  sudo docker cp Sha_or_name_of_container:path_to_pyt_file/file_name .
  ```
  The full stop meant the file was put where the terminal I was writing in was located. Note for the copying in/out of the container I ran the commands from outside the container, hence needing the sha to point to it.

<a name="Volumes"></a>
### Volumes

    - VOLUMES: Directories that should be managed separately from the container (e.g. persistent data that should be kept after the container exits)

- If you do some work in a container, close it, then open a new container from the image your work will be gone because it's building from the start
- If you need to do work in a container and save it you can make a "volume" where it'll save the work so even if you close the container when you next make one from that image it'll still have your work. Do this by
  ```
  sudo docker run -i -t --mount source=my_volume_name,target=/notebooks image_name
  ```
  where the target is the directory in the container you're doing work in you want it to save. Then closed and restarted using the same command and my work was still there.
- Volume related commands:
  - List volumes: docker volume ls
  - Delete a volume: docker volume rm VOLUME-NAME
  - Delete all unattached volumes: docker volume prune

- use `sudo docker rm container_ID` to remove a container. If you include a -v after the rm then it will also remove any associated volumes.


### Materials used

- [What is docker](https://opensource.com/resources/what-docker) **CC BY-SA 4.0**
- [What are containers](https://opensource.com/resources/what-are-linux-containers?intcmp=7016000000127cYAAQ) **CC BY-SA 4.0**
- [Docker carpentry](http://www.manicstreetpreacher.co.uk/docker-carpentry/aio/) **Creative Commons Attribution 4.0**
- [Geohackweek tutorial](https://geohackweek.github.io/Introductory/docker-tutorial_temp/) **Creative Commons Attribution 3.0 Unported**

## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go

## What to learn next

We recommend reading the chapter on Testing, and then the chapter on Continuous Integration. Note that the chapter on Version Control is a prerequisite for the chapter on Continuous Integration.

## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail

## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter

## Bibliography

[Figure](https://opendreamkit.org/2017/11/02/use-case-publishing-reproducible-notebooks/) **Permission to use granted by Juliette Taka, Logilab and the OpenDreamKit project.**
