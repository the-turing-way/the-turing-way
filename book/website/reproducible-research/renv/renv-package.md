(rr-renv-package)=
# Package Management Systems

Package managers install and keep track of the different software packages (and their versions) that you use within an environment.
There are quite a few to choose from, for example, Yum, Zypper, dpkg, Nix (which will be mentioned in the {ref}`rr-binderhub` section), and language specific package managers [Python Packages](https://py-pkgs.org/) and [R Packages](https://r-pkgs.org/). We are going to focus on [Conda](https://conda.io/en/latest/), which has several useful functionalities.

(rr-renv-package-conda)=
## What Does Conda Do?

Conda allows users to create any number of entirely separate environments, and quickly and switch between them.
For example, say a researcher has a project, _Project One_, which has its own environment, defined by Conda, that is made up of the following set of packages:

| **Package Name** | **Version** |
| ------------ | ------- |
| `Package A`    | `1.5.2`   |
| `Package B`   | `2.1.10`  |
| `Package C`    | `0.7.9`   |

Later, the researcher starts _Project Two_ in its own environment, with the following packages:

| _Package Name_ | _Version_ |
| ------------ | ------- |
| `Package B`    | `2.1.10`  |
| `Package C`    | `1.2.4`   |
| `Package D`    | `1.5.2`   |
| `Package E`    | `3.7.1`   |

Note here that the version of `package C` used in _Project Two_ has been updated from the version used in _Project One_.
If these project environments were not separate, then the researcher would have the choice of:

- A) Using the older version of `package C` forever and not benefiting from updates and bugfixes in later versions.
- B) Installing the updated version of the package and hoping that it does not impact _Project One_.
- C) Installing the updated version of the package for use in _Project Two_, then uninstalling it and reinstalling the old one whenever they need to do work on _Project One_.
This would be extremely annoying and is a step that risks being forgotten.

All of these options are extremely poor, hence the utility of Conda for creating distinct environments that are easily interchangeable.

Conda can also be used to capture and export computational environments easily.
It can go in the other direction too; it can generate computational environments from configuration files which can be used to recreate someone else's environment.

Another benefit of Conda is that it offers much greater flexibility to users who do not have admin privileges on the machines they are working on (as is very common when working with high-performance computing facilities).
Without Conda, it is typically challenging to install required software onto such machines.
However, because Conda creates and changes _new_ environments rather than making changes to a machine's overall system environment, admin privileges are not required.

Finally, while Conda is Python-centric to a degree, it is also well-integrated for use with other languages.
For example, the base version of Conda includes the C++ standard library.

(rr-renv-package-installing)=
## Installing Conda

Note that these installation instructions are directed towards Linux systems.
Instructions for installing Conda on Windows or Mac systems can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

Go to [https://repo.continuum.io/miniconda/](https://repo.continuum.io/miniconda/) and download the latest Miniconda 3 installer for your system (32 bit or 64 bit). It will have a name like `miniconda_version_number.sh`.
Run the installer using:

```
bash Miniconda_version_number.sh
```

You can check that Conda has installed successfully by typing:

```
conda --version
```

which should output a version number.

(rr-renv-package-using)=
## Making and Using Environments

Conda automatically installs a base environment with some commonly used software packages.
It is possible to work in this base environment; however, it is good practice to create a new environment for every project you start.

To create an environment, use `conda create --name your_project_env_name` followed by a list of packages to include.
To include the `scipy` and `matplotlib` packages, add them to the end of the command:

```
conda create --name Project_One scipy matplotlib
```

You can specify the versions of certain (or all) packages by using `=package_number` after the name. For example, to specify `scipy 1.2.1` in the above environment:

```
conda create --name Project_One scipy=1.2.1 matplotlib
```

When creating environments, you can also specify versions of languages to install. For example, to use `Python 3.7.1` in the _Project_One_ environment:

```
conda create --name Project_One python=3.7.1 scipy=1.2.1 matplotlib
```

Now that an environment has been created, it is time to activate (start using) it via `conda activate environment_name`.
So in this example:

```
conda activate Project_One
```

Note that you may need to use `source` instead of `conda` if you are using an old version of Conda.

Once an environment is activated, you should see the environment name before each prompt in your terminal:

```
(Project_One) $ python --version
Python 3.7.1
```

(rr-renv-package-deleting)=
## Deactivating and Deleting Environments

You can deactivate (get out of) an environment using:

```
conda deactivate
```

and remove (delete) an environment as shown here:

```
conda env remove --name Project_One
```

To check if an environment has been successfully removed, you can look at a list of all the Conda environments on the system using:

```
conda env list
```

However, deleting an environment may not delete the package files that were associated with it.
This can lead to a lot of memory being wasted on packages that are no longer required.
Packages that are no longer referenced by any environments can be deleted using:

```
conda clean -pts
```

Alternatively, you can delete an environment (such as _Project_One_) along with its associated packages via:

```
conda remove --name Project_One --all
```

(rr-renv-package-removing)=
## Installing and Removing Packages Within an Environment

Within an environment, you can install more packages using:

```
conda install package_name
```

similarly, you can remove them via:

```
conda remove package_name
```

This is the best way to install packages from within Conda as it will also install a Conda-tailored version of the package.
However, it is possible to use other methods if a Conda-specific version of a package is not available.
For example, `pip` is commonly used to install Python packages.
So, a command like:

```
pip install scipy
```

will install the `scipy` package explicitly - as long as `pip` is installed inside the currently active Conda environment.
Unfortunately, when Conda and `pip` are used together to create an environment, it can lead to a state that can be hard to reproduce.
Specifically, running Conda after `pip` may potentially overwrite or break packages installed via `pip`.
One way to avoid this is by installing as many requirements as possible with Conda, and then use pip.
Detailed information can be read on the post, [Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/).

Although Python packages have been used in many of the examples given here, Conda packages do not have to be Python packages. For example, here the R base language is installed along with the R package `r-yaml`:

```
conda create --name Project_One r-base r-yaml
```

To see all of the installed packages in the current environment, use:

```
conda list
```

To check if a particular package is installed, for example, `scipy` in this case:

```
conda list scipy
```

A Conda channel is where it downloaded a package from.
Common channels include `Anaconda` (a company which provides the defaults conda package channel), and `conda-forge` (a community-driven packaging endeavour).
You can explicitly install a package from a certain channel by specifying it like:

```
conda install -c channel_name package_name
```

(rr-renv-package-exporting)=
## Exporting and Reproducing Computational Environments

Conda environments can be exported easily to human-readable files in the YAML format.
YAML files are discussed in more detail {ref}`later <rr-renv-yaml>` in this chapter.

To export a conda environment to a file called `environment.yml`, activate the environment and then run:

```
conda env export > environment.yml
```

Similarly, Conda environments can be created from YAML files via:

```
conda env create -f environment.yml
```

This allows researchers to reproduce one another's computational environments quickly.
Note that the list of packages is not just those explicitly installed.
It can include OS-specific dependency packages so environment files may require some editing to be portable to different operating systems.

Environments can also be cloned.
This may be desirable, for example, if a researcher begins a new project and wants to make a new environment to work on it in; the new project's environment (at least initially) may require the same packages as a previous project's environment.

For example, to clone the _Project_One_ environment, and give this new environment the name _Project_Two_:

```
conda create --name Project_Two --clone Project_One
```
