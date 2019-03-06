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

[What are containers](https://opensource.com/resources/what-are-linux-containers?intcmp=7016000000127cYAAQ) **CC BY-SA 4.0**

Containers allow a developer to package up an project with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. They are designed to make it easier to transfer projects between very different environments.

In a way, containers behave like a virtual machine. To the outside world, they can look like their own complete system. But unlike a virtual machine, rather than creating a whole virtual operating system, containers only contain the individual components they need in order to operate. This gives a significant performance boost and reduces the size of the application.

Anyone can open up a container and view and interact with the project within it as if the machine they are accessing it from has the computational environment specified in the container- regardless of what the computational environment *actually* is.


*Include why to use them*
*When you would use one locally (as not everyone will need to, depends on complexity of project)*
*Say containers are more lightweight than virtual machines*
*Note the points from this blog post: http://urssi.us/blog/2018/12/21/why-research-software-sustainability-wont-be-fixed-by-containers/*

### What are images?



### What is Docker

*Top paragraph, mention singularity but say we're focusing on docker, quick pros/cons*

*Say Dockerfiles build images, images build containers.*


Undoubtedly, one of the biggest reasons for recent interest in container technology has been the Docker open source project, a command line tool for creating and working with containers.

Docker is a command-line tool for programmatically defining the contents of a Linux container in code, which can then be versioned, reproduced, shared, and modified easily just as if it were the source code to a program.

[What is docker](https://opensource.com/resources/what-docker) **CC BY-SA 4.0**



Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

For developers, it means that they can focus on writing code without worrying about the system that it will ultimately be running on.

*Lots of docker images pre-built so easier than starting from scratch, e.g. [R starting images](https://github.com/rocker-org/rocker-versioned)*


[Notes](https://opensource.com/business/14/7/docker-security-selinux) on the importance of making sure Docker containers are secure, and here is a [detailed breakdown](https://opensource.com/business/14/9/security-for-docker) of security features currently within Docker, and how they function.


### Installing Docker

Installers for Docker on a variety of different systems are available [here](https://docs.docker.com/install/). Detailed installation instructions are also available for a variety of oporating systems such as [ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/), [debian](https://docs.docker.com/install/linux/docker-ce/debian/), [Macs](https://docs.docker.com/docker-for-mac/install/), and [Windows](https://docs.docker.com/docker-for-windows/install/).


## Setting up docker, taking notes.

- Using [this](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)
- According to that step 1 is setting up a docker repository. Following the instructions for that.
  - Run `sudo apt-get update`
  - Run
    ```
    sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
    ```
   - Add GPG key using `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
   - Verify that's worked by running `sudo apt-key fingerprint 0EBFCD88` and checking the output against the model output they give which is
     ```
     pub   4096R/0EBFCD88 2017-02-22
           Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
     uid                  Docker Release (CE deb) <docker@docker.com>
     sub   4096R/F273FCD8 2017-02-22
     ```
   - Use `lsb_release -cs` to check my ubuntu distribution, found it's xenial. Don't appear to do anything with the info but it was in the instructions.
   - Run
     ```
     sudo add-apt-repository \
     "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) \
     stable"
     ```
   - Run `sudo apt-get update` again.rjarnold/learning_docker:first_image_online
   - Install docker by `sudo apt-get install docker-ce`
   - Ran `sudo docker run hello-world`, it downloaded something automatically and then came up with a message saying hello and indicating the installation had been sucessful.
     ```
     Hello from Docker!
     This message shows that your installation appears to be working correctly.

     To generate this message, Docker took the following steps:
      1. The Docker client contacted the Docker daemon.
      2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
         (amd64)
      3. The Docker daemon created a new container from that image which runs the
         executable that produces the output you are currently reading.
       4. The Docker daemon streamed that output to the Docker client, which sent it
          to your terminal.

     To try something more ambitious, you can run an Ubuntu container with:
       $ docker run -it ubuntu bashrjarnold/learning_docker:first_image_online

     Share images, automate workflows, and more with a free Docker ID:
       https://hub.docker.com/

     For more examples and ideas, visit:
       https://docs.docker.com/get-started/
     ```
- Listed docker images `sudo docker image ls`, and it came up with the hello-world image that came with the download. The instructions didn't include the sudo but without it I get the error `Got permission denied while trying to connect to the Docker daemon socket`. As far as I can tell this issue isn't unique to me or the borrowed computer I'm using. Believe I need `sudo` in front of all my docker commands.
- Ran the hello world using `sudo docker run hello-world` and got the welcome message again but nothing else happened as far as I can tell, which may be what's supposed to happen.
- Made a new directory (docker-practice) and cd into in.rjarnold/learning_docker:first_image_online
- Made a file called app.py which contained
  ```
  from flask import Flask
  from redis import Redis, RedisError
  import os
  import socket

  # Connect to Redis
  redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

  app = Flask(__name__)

  @app.route("/")
  def hello():
      try:
          visits = redis.incr("counter")
      except RedisError:
          visits = "<i>cannot connect to Redis, counter disabled</i>"

      html = "<h3>Hello {name}!</h3>" \
             "<b>Hostname:</b> {hostname}<br/>" \
             "<b>Visits:</b> {visits}"
      return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

  if __name__ == "__main__":
      app.run(host='0.0.0.0', port=80)
  ```
- Made a file called requirements.txt that just read
  ```
  Flask
  Redis
  ```
- Created a file called `Dockerfile` containing
  ```
  # Use an official Python runtime as a parent image
  FROM python:2.7-slim

  # Set the working directory to /app
  WORKDIR /app

  # Copy the current directory contents into the container at /app
  COPY . /app

  # Install any needed packages specified in requirements.txt
  RUN pip install --trusted-host pypi.python.org -r requirements.txt

  # Make port 80 available to the world outside this container
  EXPOSE 80

  # Define environment variable
  ENV NAME World

  # Run app.py when the container launches
  CMD ["python", "app.py"]
  ```
- Then built the docker image and called it "friendlyhello" using `sudo docker build --tag=friendlyhello .`.
- Did `docker image ls` and the firndlyhello image was listed along with hello-world
- Ran the docker image using `sudo docker run -p 4000:80 friendlyhello`, the `-p 4000:80` says to map the container's port (which is 80 as seet in the docker file) to my manchine's 4000 port. As a result when I go to "http://localhost:4000/" on a web browser I get a hello world message, and a note that it couldn't connect to Redis.
- In the terminal used ctrl+C to end the app and get back to the command line.
- Can run the app in the background from the get go by adding a `-d` before the `-p`.
- Did that then ran `sudo docker container ls` to get a list of active containers which showed that one with a container ID which looks like a git SHA.
- Did `sudo docker container stop the_SHA_like_thing` and the container stopped, so I no longer got the message I got before at "http://localhost:4000/", and when I ls the containers there's none because there's none running.
- Redid it using port 3000 instead of 4000 and it worked fine, so 4000 isn't special.
- Now onto publishing and sharing dockerfiles. Made an account on [https://hub.docker.com/](https://hub.docker.com/).
- Logged into docker via my terminal using `sudo docker login`
- "The notation for associating a local image with a repository on a registry is username/repository:tag. The tag is optional, but recommended, since it is the mechanism that registries use to give Docker images a version." Did `sudo docker tag friendlyhello rjarnold/learning_docker:first_image_online`
- Pushed the image to my account online by `sudo docker tag push rjarnold/learning_docker:first_image_online`
- Refreshed the webpage with my account, the repository had been automatically create and the image placed within it.
- Now try running the image on another machine. On another ubuntu machine I tried running `sudo docker run -p 4000:80 rjarnold/learning_docker:first_image_online` Failed because docker wasn't installed on that machine.
- Installed docker on that machine and tried again. It regonised the image wasn't on my local machine and downloaded it
- Went to "http://localhost:4000/" and the message was there as expected, so success. It had run without making the directory and files on my machine.
- Now looking at [this](https://geohackweek.github.io/Introductory/docker-tutorial_temp/) tutorial **Creative Commons Attribution 3.0 Unported**
- If I then run `docker run -i -t geohackweek2016/arraystutorial` then that image runs. The `-i -t` means that once I hit enter then I get a prefix "root@SHA_type_thing" in the terminal which I can then do standard linux commands with within the container. After experimenting with my own images find generally need `/bin/bash` at the end of this command on order to get the terminal as well as the `-i -t`. Not 100% sure why it wasn't needed for this example, maybe something in the dockerfile. Yeah. If you have `CMD ["/bin/bash"]` in the dockerfile then you don't need to have it when you run the container.
- When I do `ls` I see the stuff in the continer which is comletly different to the directory I ran the image in.
- Move a file from my computer into the container using
  ```
  sudo docker cp file_name Sha_or_name_of_container:path_to_pyt_file/file_name
  ```
- Created a file inside the container, want to get it out, ran
  ```
  sudo docker cp Sha_or_name_of_container:path_to_pyt_file/file_name .
  ```
  The full stop meant the file was put where the terminal I was writing in was located. Note for the copying in/out of the container I ran the commands from outside the container, hence needing the sha to point to it.
- Another [tutorial](http://www.manicstreetpreacher.co.uk/docker-carpentry/aio/) I'm looking at. **Creative Commons Attribution 4.0**
- A docker file can look like this:
  ```
  FROM centos:7
  MAINTAINER spli@dundee.ac.uk

  RUN yum install -y -q epel-release
  RUN yum install -y -q python-pip
  RUN pip install omego
  ```
  where
    - FROM: The name of a base image
    - MAINTAINER: The email of the developer or owner
    - RUN: Runs a shell command
  and some other commonly used docker commands are:
    - COPY: Copies a file (e.g. a script, configuration file, or archive) into the Docker image
    - USER: Change the user that a command is run as (useful for dropping privileges)
    - WORKDIR: Change the current working directory
    - EXPOSE: Lists ports that should be exposed to the outside world
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
- Looking at [this](https://www.tutorialspoint.com/docker/docker_images.htm) tutorial (not open I don't think)
- To remove an image do `sudo docker rmi image_name_or_sha`
- There's docker kill, stop, pause, and unpause. Pause suspends processes running in the container, stop terminates them, kill is for terminating them when you don't case about being graceful about it. There's also restart which restarts after a stop. The syntax for using any of these is `sudo docker what_you_want_to_do container_ID`. Use exit to get out of the interactive bash shell if you started one.
- use `sudo docker rm container_ID` to remove a container. If you include a -v after the rm then it will also remove anny accociated volumes.
- Short example of a docker file
  ```
  #This is a sample Image
  FROM ubuntu
  MAINTAINER demousr@gmail.com

  RUN apt-get update
  RUN apt-get install –y nginx
  ADD my_local_file .
  CMD [“echo”,”Image created”]
  ```
  Breaking this down:
  - Comments by #'s like python.
  - You need some kind of from statement oven if it's `FROM SCRATCH`.
  - MAINTAINER self explanatory and not necessary to include.
  - RUN instructions to run when building the image
  - ADD is used if you have files on your computer you want to be put into the image. The syntax is the path to the file from where you're building the image in, and then the location in the container directory system you want the file to be placed. Note that you can only add files from the level or below where your dockerfile is. Pushed that image to DockerHub and then pulled it to a different computer. When I ran the contianer on that computer the file was in it.
  - CMD is commands to run when your container starts up. So to calify RUN are things you do to *setting up* a container from an image, and CMD is for commands to be automatically run in the container as soon as it's set up. The message only appears if I don't have interactive terminal. Not clear on why.
- It's good practice to use CMD for anything that is going to need to be run before someone starts working in the container. You *can* just follow the instreuction to run the container with a command (e.g `docker run containerID echo Imange created`)  and it'll have the same impact, but then you're relying on whoever is trying to run the container to know they need to follow that up with the command required. Putting it in the Dockerfile means it'll always be run.
- There's ENTRYPOINT, but seems like bad practice to use, so leaving it out.
- Made directories within the container, but when I try using run to cd in and then making another directory within. Didn't work. Asked, this is because each RUN saves and deletes the previous container, then makes a new one from that point, does its run thing, then saves and is deleted and so on. Each layer is like a commit. As a result my RUNing cd into the directory doesn't matter because the next RUN statement restarts the container fresh so the next mkdir goes into the top level. According to David and Will I can use && to have multiple commands on one RUN, but when I try it it doesn't work.
- There's COPY as well as ADD. Serves same function but ADD can also be used to add things from e.g. urls. At least in the one article I read they say it's best to use COPY since it's more explicit. Tested that copy could do the copying local files to an image thing the way add did and it suceeded.
- It's good practice to use .dockerignore files. When you build an image everything in the dockerfile's directory and below is sent to the Docker daemon (which may or may not be on the same machine as where your running the command) to build the image. It uses the dockerfile and the context to build the image. If you're got lots of big files in your context that aren't needed for your image then you're sending the daemon those huge files for nothing. You can make sure they're not sent by including them in a .dockerignore file. You can use syntax like for example `*.png` for example to ignore lots fo different files with similar names/types with few lines.
- Good practise to break RUN statements up to be more readable, for example
  ```
  RUN command_to_do_thing_1 \
     command_to_do_thing_2 \
     command_to_do_thing_3 \
     command_to_do_thing_4
  ```


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
