(z2b)=
# Zero-to-Binder

In this chapter, we will create a Binder project from scratch: we will first make a repository on GitHub and then launch in on mybinder.org.
Sections where you are expected to complete a task are denoted by three traffic light 🚦 emojis.
Some steps give you the option of Python, Julia or R - click on the tab of your preferred language.

```{admonition} Attributions
This tutorial is based on Tim Head's _Zero-to-Binder_ workshops which can be found here: <http://bit.ly/zero-to-binder> and <http://bit.ly/zero-to-binder-rise>

Thank you to Anna Krystalli and Oliver Strickson for their help developing the R and Julia content, respectively.
```

```{attention}
Binder can take a long time to load, but this doesn't necessarily mean that your Binder will fail to launch.
You can always refresh the window if you see the "... is taking longer to load, hang tight!" message.
```

```{admonition} If you are using R...
If you are following the R path, we have included some alternative steps using the [`holepunch` package](https://github.com/karthik/holepunch) which will build your environment using a [rocker base image](https://github.com/rocker-org/rocker) and should, ultimately, be faster to build and launch.
```

(z2b-reqs)=
## Requirements

You will need:

- **Some code and some data.**
  The code should take less than **10 minutes to run**, and the data should be less than **10 MB**.
  This might mean that you just pick one script from a bigger project, or bring a subset of your data.
  Note that it's really important that the code and data can be made **public** because we'll be using the public binder instance.
- **A GitHub account.**
  Please sign up for one if you don't already have one: <https://github.com/join>

(z2b-step-1)=
## 1. Creating a repo to Binderize

🚦🚦🚦


`````{tab-set}
````{tab-item} Python
:sync: key1
1) Create a new repo on GitHub called "my-first-binder"
   - Make sure the repository is **public**, _not private_!
   - Don't forget to initialise the repo with a README!
2) Create a file called `hello.py` via the web interface with `print("Hello from Binder!")` on the first line and commit to the `main` branch
````

````{tab-item} Julia
:sync: key2
1) Create a new repo on GitHub called "my-first-binder"
   - Make sure the repository is **public**, _not private_!
   - Don't forget to initialise the repo with a README!
2) Create a file called `hello.jl` via the web interface with `println("Hello from Binder!")` on the first line and commit to the `main` branch
3) Create a file called `Project.toml` (WARNING: the capitalisation is important!) with the following content and commit it to `main`.
   This will install Julia into the Binder environment.

   ```julia
   [compat]
   julia = "1.3"
   ```
````

````{tab-item} R
:sync: key3
1) Create a new repo on GitHub called "my-first-binder"
   - Make sure the repository is **public**, _not private_!
   - Don't forget to initialise the repo with a README!
2) Create a file called `hello.R` via the web interface with `print("Hello from Binder!")` on the first line and commit to the `main` branch
3) Create a file called `runtime.txt` with `r-2022-01-01` on the first line.
   This date represents the snapshot of [CRAN](https://cran.r-project.org/) hosted on the [RStudio Package Manager](https://packagemanager.rstudio.com) we will use.
   Commit this file to the `main` branch.

   ```{note}
   In R you can use `holepunch::write_runtime()` to create a `runtime.txt` in the `.binder/` directory; it will be configured with today's date.
   ```
````
`````

(z2b-public-repo)=
### Why does the repo have to be public?

mybinder.org cannot access private repositories as this would require a secret token.
The Binder team choose not to take on the responsibility of handling secret tokens as mybinder.org is a public service and proof of technological concept.
If accessing private repositories is a feature you/your team need, we advise that you look into building your own [BinderHub](https://binderhub.readthedocs.io).

(z2b-step-2)=
## 2. Launch your first repo!

🚦🚦🚦

1) Go to **<https://mybinder.org>**
2) Type the URL of your repo into the "GitHub repo or URL" box.
   It should look like this:
   > **https://github.com/YOUR-USERNAME/my-first-binder**
3) As you type, the webpage generates a link in the "Copy the URL below..." box
   It should look like this:
   > **https://mybinder.org/v2/gh/YOUR-USERNAME/my-first-binder/HEAD**
4) Copy it, open a new browser tab and visit that URL
   - You will see a "spinner" as Binder launches the repo

If everything ran smoothly, you'll see a JupyterLab interface.

(z2b-background-1)=
### What's happening in the background? - Part 1

While you wait, BinderHub (the backend of Binder) is:

- Fetching your repo from GitHub
- Analysing the contents
- Building a Docker image based on your repo
- Launching that Docker image in the cloud
- Connecting you to it via your browser

(z2b-step-3)=
## 3. Run the script

🚦🚦🚦

````{tab-set}
```{tab-item} Python
:sync: key1
1. From the launch panel, select "Terminal"
2. In the new terminal window, type `python hello.py` and press return
```

```{tab-item} Julia
:sync: key2
1. From the launch panel, select "Terminal"
2. In the new terminal window, type `julia hello.jl` and press return
```

```{tab-item} R
:sync: key3
1. From the launch panel, select "Terminal"
2. In the new terminal window, type `Rscript -e 'source("hello.R")'` and then press return
```
````

`Hello from Binder!` should be printed to the terminal.

(z2b-step-4)=
## 4. Pinning Dependencies

It was easy to get started, but our environment is barebones - let's add a **dependency**!

🚦🚦🚦

`````{tab-set}
````{tab-item} Python
:sync: key1
1) In your repo, create a file called `requirements.txt`
2) Add a line that says: `numpy==1.25.0`
3) Check for typos! Then commit to the `main` branch
4) Visit **https://mybinder.org/v2/gh/YOUR-USERNAME/my-first-binder/HEAD** again in a new tab
````

````{tab-item} Julia
:sync: key2
1) In your repo, edit the `Project.toml` file
2) Add a new block that says:

   ```julia
   [deps]
   CSV = "336ed68f-0bac-5ca0-87d4-7b16caf5d00b"
   ```

3) Check for typos! Then commit to `main`.
4) Visit **https://mybinder.org/v2/gh/YOUR-USERNAME/my-first-binder/HEAD** again in a new tab
````

````{tab-item} R
:sync: key3
1) In your repo, create a file called `install.R`
2) Add a line that says: `install.packages("readr")`
3) Check for typos! Then commit to the `main` branch
4) Visit **https://mybinder.org/v2/gh/YOUR-USERNAME/my-first-binder/HEAD** again in a new tab

```{note}
If using `holepunch`, you can create an `install.R` file and automatically add the code to install all dependencies in your project using `holepunch::write_install()`.
```
````
`````

This time, click on "Build Logs" in the big, horizontal, grey bar.
This will let you watch the progress of your build.
It's useful when your build fails or something you think _should_ be installed is missing.

```{note}
Sometimes Binder's build logs prints things in red font, such as warnings that `pip` is not up-to-date (`pip` is often out of date because it's regularly updated!) or installation messages, especially if you're using R.
These red messages don't necessarily mean there's a problem with your build and it will fail - it's just an unfortunate font colour choice!
```

(z2b-background-2)=
### What's happening in the background? - Part 2

This time, BinderHub will read the configuration file you added and install the specific version of the package you requested.

(z2b-dependencies)=
### More on pinning dependencies

````{tab-set}
```{tab-item} Python
:sync: key1
In the above example, we used two equals signs (`==`) to pin the version of `numpy`.
This tells Binder to install that _specific_ version.

Another way to pin a version number is to use the greater than or equal to sign (`>=`) to allow any version above a particular one to be installed.
This is useful when you have a lot of dependencies that may have dependencies on each other and allows Binder to find a configuration of your dependencies that do not conflict with one another whilst avoiding any earlier versions which may break or change your code.

Finally, you could not provide a version number at all (just the name of the library/package) and Binder will install the latest version of that package.
```

```{tab-item} Julia
:sync: key2
In the above example, we copied a hash into our `Project.toml` file which is related to the version of the package we'd like to install.
For a full dependency graph, we would also need to include a `Manifest.toml` file which would document dependencies of dependencies.
Between these two files, we are able to instantiate an exact replication of a Julia environment.

Of course we can imagine that, as the environment grows and the inter-dependencies become more complex, it would become very taxing to write these files by hand!
The truth is that you'd never do it manually, the built-in package manager `Pkg` can [generate them automatically](https://julialang.github.io/Pkg.jl/v1/environments/).
```

```{tab-item} R
:sync: key3
In the above example, we specified that we want to use R in our project by including a date in `runtime.txt`.
The date tells Binder which CRAN snapshot to source R and packages from.
These snapshots are sourced from the [RStudio Package Manager](https://packagemanager.rstudio.com) (RSPM).
In the above example, the RSPM snapshot dated `r-2022-01-01` is used and the version of R and `readr` available at that date and installed.
For the example workflow to work correctly, please ensure you do not supply a date earlier than this example date.

This provides some rudimentary package versioning for R users but is not as robust as pinning versions in a `requirements.txt` in Python.
For more robust and specific version pinning in R, have a look at the [`renv`](https://rstudio.github.io/renv/) package.
```
````

(z2b-step-5)=
## 5. Check the Environment

🚦🚦🚦

`````{tab-set}
````{tab-item} Python
:sync: key1
1) From the launch panel, select "Python 3" from the Notebook section to open a new notebook
2) Type the following into a new cell:

   ```python
   import numpy
   print(numpy.__version__)
   numpy.random.randn()
   ```

   ```{attention}
   Note the two underscores either side of `version`!
   ```

3) Run the cell to see the version number and a random number printed out
   - Press either SHIFT+RETURN or the "Run" button in the Menu bar
````

````{tab-item} Julia
:sync: key2
1) From the launch panel, select "Julia" from the Notebook section to open a new Julia notebook
2) Type the following into a new cell:

   ```julia
   using Pkg
   Pkg.status()
   ```

3) Run the cell to see the version number printed out
   - Press either SHIFT+RETURN or the "Run" button in the Menu bar
````

````{tab-item} R
:sync: key3
1) From the launch panel, select "R" from the Notebook section to open a new R notebook
2) Type the following into a new cell:

   ```r
   library(readr)
   packageVersion("readr")
   read_csv(system.file("extdata/mtcars.csv", package = "readr"))
   ```

3) Run the cell
    - Press either SHIFT+RETURN or the "Run" button in the Menu bar
    You should see the following output:
      - the version number of the installed version of `readr`
      - a tibble of the contents of the `mtcars.csv` which is a csv file included in package `readr`
````
`````

```{attention}
If you save this notebook, it **will not** be saved to the GitHub repo.
Pushing changes back to the GitHub repo through the container is not possible with Binder.
**Any changes you have made to files inside the Binder will be lost once you close the browser window.**
```

(z2b-step-6)=
## 6. Sharing your Work

Binder is all about sharing your work easily and there are two ways to do it:

- Share the **https://mybinder.org/v2/gh/YOUR-USERNAME/my-first-binder/HEAD** URL directly
- Visit **<https://mybinder.org>**, type in the URL of your repo and copy the Markdown or ReStructured Text snippet into your `README.md` file.
  This snippet will render a badge that people can click, which looks like this: ![Binder](https://mybinder.org/badge_logo.svg)

🚦🚦🚦

1) Add the **Markdown** snippet from **<https://mybinder.org>** to the `README.md` file in your repo
   - The grey bar displaying a binder badge will unfold to reveal the snippets.
     Click the clipboard icon next to the box marked with "m" to automatically copy the Markdown snippet.
2) Click the badge to make sure it works!

(z2b-step-7)=
## 7. Accessing data in your Binder

Another kind of dependency for projects is **data**.
There are different ways to make data available in your Binder depending on the size of your data and your preferences for sharing it.

(z2b-small-files)=
### Small public files

The simplest approach for small, public data files is to add them directly into your GitHub repository.
They are then directly encapsulated into the environment and versioned along with your code.

This is ideal for files up to **10MB**.

(z2b-medium-files)=
### Medium public files

To access medium files **from a few 10s MB up to a few hundred MB**, you can add a file called `postBuild` to your repo.
A `postBuild` file is a shell script that is executed as part of the image construction and is only executed once when a new image is built, not every time the Binder is launched.

See [Binder's `postBuild` example](https://mybinder.readthedocs.io/en/latest/using/config_files.html#postbuild-run-code-after-installing-the-environment) for more uses of the `postBuild` script.

```{note}
New images are only built when Binder sees a new commit, not every time you click the Binder link.
Therefore, the data is only downloaded once when the Docker image is built, not every time the Binder is launched.
```

(z2b-large-files)=
### Large public files

It is not practical to place large files in your GitHub repo or include them directly in the image that Binder builds.
The best option for large files is to use a library specific to the data format to stream the data as you're using it or to download it on demand as part of your code.

For security reasons, the outgoing traffic of your Binder is restricted to HTTP/S or GitHub connections only. You will not be able to use FTP sites to fetch data on mybinder.org.

(z2b-private-files)=
### Private files

There is no way to access files which are not public from mybinder.org.
You should consider all information in your Binder as public, meaning that:

- there should be no passwords, tokens, keys and so on in your GitHub repo;
- you should not type passwords into a Binder running on mybinder.org;
- you should not upload your private SSH key or API token to a running Binder.

In order to support access to private files, you would need to create a local deployment of [BinderHub](https://binderhub.readthedocs.io) where you can decide the security trade-offs yourselves.

```{note}
Building a BinderHub is not a simple task and is usually taken on by IT/RSE groups for reasons around managing maintenance, security and governance.
However, that is not to say that they are the _only_ groups of people who should/could build a BinderHub.
```

(z2b-step-8)=
## 8. Get data with `postBuild`

🚦🚦🚦

`````{tab-set}
````{tab-item} Python
:sync: key1
1) Go to your GitHub repo and create a file called `postBuild`
2) In `postBuild`, add a single line reading: `wget -q -O gapminder.csv http://bit.ly/2uh4s3g`
   - `wget` is a program which retrieves content from web servers.
     This line extracts the content from the bitly URL and saves it to the filename denoted by the `-O` flag (capital "O", not zero), in this case `gapminder.csv`.
     The `-q` flag tells `wget` to do this quietly, meaning it won't print anything to the console.
3) Update your `requirements.txt` file by adding a new line with `pandas` on it and another new line with `matplotlib` on it
   - These packages aren't necessary to download the data but we will use them to read the CSV file and make a plot
4) Click the binder badge in your README to launch your Binder

Once the Binder has launched, you should see a new file has appeared that was not part of your repo when you clicked the badge.

Now visualise the data by creating a new notebook (selecting "Python 3" from the Notebook section) and run the following code in a cell.

```python
%matplotlib inline

import pandas

data = pandas.read_csv("gapminder.csv", index_col="country")

years = data.columns.str.strip("gdpPercap_")  # Extract year from last 4 characters of each column name
data.columns = years.astype(int)              # Convert year values to integers, saving results back to dataframe

data.loc["Australia"].plot()
```

```{note}
See this [Software Carpentry lesson](https://swcarpentry.github.io/python-novice-gapminder/09-plotting/index.html) for more info.
```
````

````{tab-item} Julia
:sync: key2
1) Go to your GitHub repo and create a file called `postBuild`
2) In `postBuild`, add a single line reading: `wget -q -O gapminder.csv http://bit.ly/2uh4s3g`
   - `wget` is a program which retrieves content from web servers.
     This line extracts the content from the bitly URL and saves it to the filename denoted by the `-O` flag (capital "O", not zero), in this case `gapminder.csv`.
     The `-q` flag tells `wget` to do this quietly, meaning it won't print anything to the console.
3) Update your `Project.toml` file by adding new dependencies to `[deps]` with the following lines:

   ```julia
   DataFrames = "a93c6f00-e57d-5684-b7b6-d8193f3e46c0"
   Plots = "91a5bcdd-55d7-5caf-9e0b-520d859cae80"
   ```

   - These packages aren't necessary to download the data but we will use them to read the CSV file and make a plot
4) Click the binder badge in your README to launch your Binder

Once the Binder has launched, you should see a new file has appeared that was not part of your repo when you clicked the badge.

Now visualise the data by creating a new notebook (selecting "Julia" from the Notebook section) and run the following code in a cell.

```julia
using DataFrames
using CSV
using Plots

data = CSV.read("gapminder.csv", DataFrame)

# Extract the row corresponding to Australia
aus_gdp = data[data[:, :country] .== "Australia", :]
aus_gdp = Matrix(aus_gdp[:,2:end])[:]  # as vector

# Extract the years as Ints from the column names
years = [x[end-3:end] for x in names(data)[2:end]]
years = parse.(Int, years)

# Plot
plot(years, aus_gdp)
```
````

````{tab-item} R
:sync: key3
1) Go to your GitHub repo and create a file called `postBuild`
2) In `postBuild`, add a single line reading: `wget -q -O gapminder.csv http://bit.ly/2uh4s3g`
   - `wget` is a program which retrieves content from web servers.
     This line extracts the content from the bitly URL and saves it to the filename denoted by the `-O` flag (capital "O", not zero), in this case `gapminder.csv`.
     The `-q` flag tells `wget` to do this quietly, meaning it won't print anything to the console.
3) Update your `install.R` file to install two additional dependencies, `"tidyr"` and `"ggplot2"`. To do so, supply a character vector of the required packages to `install.packages()` instead of a single character string. The installation command should now look like this:

   ```r
   install.packages(c("readr", "tidyr", "ggplot2"))
   ```

    - These packages aren't necessary to download the data but we will use them to read the CSV file, process it and make a plot
4) Click the binder badge in your README to launch your Binder

Once the Binder has launched, you should see a new file has appeared that was not part of your repo when you clicked the badge.

Now visualise the data by creating a new notebook (selecting "R" from the Notebook section) and running the following code in a cell.

```r
library(readr)
library(tidyr)
library(ggplot2)

data <- read_csv("gapminder.csv") %>%
    pivot_longer(-country,
                 names_to = "year",
                 values_to = "gdpPercap",
                 names_prefix = "gdpPercap_",
                 names_transform = list(year = as.integer))

data[data$country == "Australia", ] %>%
    ggplot(aes(x = year, y = gdpPercap)) +
    geom_line()
```
````
`````

(z2b-beyond-notebooks)=
## Changing the Interface

Throughout this tutorial, we have been using the JupyterLab interface.
This is the default interface for newly created Binder instances.
However, this is not the only interface available on mybinder.org, the Classic Notebook view and RStudio are available too.
(An R environment needs to be installed for RStudio to be available.)

You can access the different interfaces in different ways.
The easiest way is to use the buttons in the JupyterLab Launcher, but you can provide URL parameters to directly open a specific interface (or file!) when the Binder instance launches.
We'll now cover three ways you can manipulate your Binder URL to navigate between interfaces.

### from inside a running Binder

Here is the structure of the URL inside a running Binder instance running JupyterLab:

> **https://<some-prefix>.mybinder.org/user/<a composite of your username, your repo name and a hash>/lab**

You can change the interface from JupyterLab to either the Classic Notebook or RStudio by changing the `/lab` part of the URL to:

- **Classic Notebook:** `/tree`
- **RStudio:** `/rstudio`

### by changing the mybinder.org launch link

Here is the launch link you have been using throughout this tutorial:

> **https://mybinder.org/v2/gh/YOUR-USERNAME/my-first-binder/HEAD**

You can access each interface by appending one of the following to the end of you URL:

- **Jupyter Notebook:** `?urlpath=tree`
- **JupyterLab:** `?urlpath=lab`
- **RStudio:** `?urlpath=rstudio`

### by using the mybinder.org form

You can also set the interface when constructing your launch link on the mybinder.org website (instead of editing the URL directly) as demonstrated in the below gif.

```{figure} https://user-images.githubusercontent.com/1448859/53651127-4dabe900-3c46-11e9-8684-2cfde840d4ce.gif
---
name: changing_interfaces
alt: A gif demonstrating how to change the interface of a Binder on the mybinder.org website
---
Use the "URL to open" option on the mybinder.org site to select your interface
```

(z2b-over-to-you)=
## Now over to you!

Now you've binderized (bound?) this demo repo, it's time to binderize the example script and data you brought along!

**Some useful links:**

- Choosing languages:
  - **<https://mybinder.readthedocs.io/en/latest/howto/languages.html>**
- Configuration files:
  - **<https://mybinder.readthedocs.io/en/latest/using/config_files.html>**
- Example Binder repos:
  - **<https://mybinder.readthedocs.io/en/latest/sample_repos.html>**
- Getting data:
  - With `wget`: **<https://github.com/binder-examples/getting-data>**
  - With `quilt`: **<https://github.com/binder-examples/data-quilt>**
  - From remote storage: **<https://github.com/binder-examples/remote_storage>**

**Advanced usage patterns:**

- Separating content from envorinment with `nbgitpuller` to reduced rebuilds:
  - **<https://discourse.jupyter.org/t/tip-speed-up-binder-launches-by-pulling-github-content-in-a-binder-link-with-nbgitpuller/922>**
- Tips for reducing the start-up time of your repository:
  - **<https://discourse.jupyter.org/t/how-to-reduce-mybinder-org-repository-startup-time/4956>**
