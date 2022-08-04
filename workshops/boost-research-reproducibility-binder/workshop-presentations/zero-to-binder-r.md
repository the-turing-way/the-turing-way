# From Zero to Binder in R!

:construction: :construction: :construction: This file is no longer maintained!
Please see the [Zero-to-Binder tutorial in the Guide for Communication](https://the-turing-way.netlify.app/communication/binder/zero-to-binder.html) instead! :construction: :construction: :construction:

Sarah Gibson, _The Alan Turing Institute_ & Anna Krystalli, _University of Sheffield_

[**The Turing Way**](https://github.com/alan-turing-institute/the-turing-way) - making reproducible Data Science "too easy not to do"

Based on Tim Head's _Zero-to-Binder_ workshops which can be found here: <http://bit.ly/zero-to-binder> and <http://bit.ly/zero-to-binder-rise>

To follow these instructions on your own machine, follow this link: **<http://bit.ly/zero-to-binder-r>**

Binder can take a long time to load, but this doesn't necessarily mean that your Binder will fail to launch.
You can always refresh the window if you see the "... is taking longer to load, hang tight!" message.

- [Running Code is more complicated than Displaying Code](#running-code-is-more-complicated-than-displaying-code)
- [What Binder Provides](#what-binder-provides)
- [1. Creating a repo to Binderize](#1-creating-a-repo-to-binderize)
  - [Why did the repo have to be public?](#why-did-the-repo-have-to-be-public)
- [2. Launch your first repo!](#2-launch-your-first-repo)
  - [What's happening in the background? - Part 1](#whats-happening-in-the-background---part-1)
- [3. Run `hello.R`](#3-run-hellor)
- [4. Pinning Dependencies](#4-pinning-dependencies)
  - [What's happening in the background? - Part 2](#whats-happening-in-the-background---part-2)
  - [More on pinning dependencies](#more-on-pinning-dependencies)
- [5. Check the Environment](#5-check-the-environment)
- [6. Sharing your Work](#6-sharing-your-work)
- [7. Accessing data in your Binder](#7-accessing-data-in-your-binder)
  - [Small public files](#small-public-files)
  - [Medium public files](#medium-public-files)
  - [Large public files](#large-public-files)
  - [Private files](#private-files)
- [8. Get data with `postBuild`](#8-get-data-with-postbuild)
- [Beyond Notebooks...](#beyond-notebooks)
- [Now over to you!](#now-over-to-you)

---

## Running Code is more complicated than Displaying Code

GitHub is a great service for sharing code, but the contents are **static**.

How could you _run_ a GitHub repository **without installing complicated requirements**?
Or even **in your browser**?

To run code, you need:

- Hardware on which to run the code
- Software, including:
  - The code itself
  - The programming language (e.g. Python, R, Julia, and so on)
  - Relevant packages (e.g. pandas, matplotlib, tidyverse, ggplot)

## What Binder Provides

[Binder](https://mybinder.org) is a service that provides your code and the hardware and software to execute it.

You can create a link to a **live, interactive** version of your code!

- An example binder link:
  > **<https://mybinder.org/v2/gh/trekhleb/homemade-machine-learning/master?filepath=notebooks%2Fanomaly_detection%2Fanomaly_detection_gaussian_demo.ipynb>**
  From this repo: **<https://github.com/trekhleb/homemade-machine-learning>**
  - Notice that the Binder link has a similar structure to the GitHub repo link (`<github-username>/<github-repo-name>`)
  - The "filepath" argument opens a specific notebook (`.ipynb` file) in the repo

> In R, we can use package [`holepunch`](https://github.com/karthik/holepunch) to **binderise** our projects! The package provides functionality to create the necessary files and automatically configure them with the required information. All files created with `holepunch` are store in a hidden `.binder/` directory and Binder knows to use those files to build your environment.

## 1. Creating a repo to Binderize

**TO DO:** :vertical_traffic_light:

1) Create a new repo on GitHub called "my-first-binder".
   - Make sure the repository is **public**, _not private_!
   - Don't forget to initialise with a README!
2) Create a file called `hello.R` via the web interface with `print("Hello from Binder!")` on the first line and commit to the `main` branch.
3) Create a file called `runtime.txt` with `r-YYYY-MM-DD` on the first line, where `YYYY-MM-DD` is today's date (eg `r-2020-05-26`). Commit to the `main` branch.
   - _In R you can use `holepunch::write_runtime()` to create a `runtime.txt` in the `.binder/` directory, configured with today's date._

### Why did the repo have to be public?

mybinder.org cannot access private repositories as this would require a secret token.
The Binder team choose not to take on the responsibility of handling secret tokens as mybinder.org is a public service and proof of technological concept.
If accessing private repositories is a feature you/your team need, we advise that you look into building your own [BinderHub](https://binderhub.readthedocs.io).

## 2. Launch your first repo!

**TO DO:** :vertical_traffic_light:

1) Go to **<https://mybinder.org>**
2) Type the URL of your repo into the "GitHub repo or URL" box.
   It should look like this:
   > **<https://github.com/your-username/my-first-binder>**

3) As you type, the webpage generates a link in the "Copy the URL below..." box
   It should look like this:
   > **<https://mybinder.org/v2/gh/your-username/my-first-binder/HEAD>**

4) Copy it, open a new browser tab and visit that URL.
   - You will see a "spinner" as Binder launches the repo.

If everything ran smoothly, you'll see a Jupyter Notebook interface.

### What's happening in the background? - Part 1

While you wait, BinderHub (the backend of Binder) is:

- Fetching your repo from GitHub
- Analysing the contents
- Creating a Docker file based on your repo
- Launching that Docker image in the Cloud
- Connecting you to it via your browser

## 3. Run `hello.R`

**TO DO:** :vertical_traffic_light:

1. In the top right corner, click "New" :arrow_right: "Rstudio"
2. In the console (the left-side panel) in Rstudio, type `source("hello.R")` and press return

`Hello from Binder!` should be printed to the terminal.

## 4. Pinning Dependencies

It was easy to get started, but our environment is barebones - let's add a **dependency**!

**TO DO:** :vertical_traffic_light:

1) In your repo, create a file called `install.R`
2) Add a line that says: `install.packages("readr")`
   - _In R you can create an `install.R` file and automatically add the code to install all dependencies in your project using `holepunch::write_install()`._
3) Check for typos! Then commit to the `main` branch.
4) Visit **<https://mybinder.org/v2/gh/your-username/my-first-binder/HEAD>** again in a new tab

This time, click on "Build Logs" in the big, horizontal, grey bar.
This will let you watch the progress of your build.
It's useful when your build fails or something you think _should_ be installed is missing.

**N.B.:** Sometimes Binder's build logs prints things in red font, such as warnings that `pip` is not up-to-date (`pip` is often out of date because it's regularly updated!) or installation messages, especially if you're using R.
These red messages don't necessarily mean there's a problem with your build and it will fail - it's just an unfortunate font colour choice!

### What's happening in the background? - Part 2

This time, BinderHub will run `install.R` and install package `readr` into our project.

### More on pinning dependencies

In the above example, we specified that we want to use R in our project included a date in `runtime.txt`. The date tells Binder which MRAN snapshot to source R and packages from. [MRAN](https://mran.microsoft.com/) hosts a "CRAN Time Machine" of daily snapshots of the CRAN R packages and R releases as far back as Sept. 17, 2014. In the above example, the MRAN snapshot dated `r-2020-05-26` is used and the version of R and `readr` available at that date and installed. For the workflow to work correctly, please ensure you do not supply a date earlier than this example date.

This provides some rudimentary package versioning for R Users but is not as robust as pinning versions in a `requirements.txt` in python. For more robust and specific version pinning in R, have a look at package [`renv`](https://rstudio.github.io/renv/)

## 5. Check the Environment

**TO DO:** :vertical_traffic_light:

1) In the top right corner, click "New" :arrow_right: "R" (under _Notebook_) to open a new R notebook
2) Type the following into a new cell:

   ```r
   library(readr)
   packageVersion("readr")
   read_csv(system.file("extdata/mtcars.csv", package = "readr"))
   ```

3) Run the cell.
    - Press either SHIFT+RETURN or the "Run" button in the Menu bar.
    You should see the following output:
      - the version number of the installed version of `readr`.
      - a tibble of the contents of the `mtcars.csv` which is a csv file included in package `readr`.

**N.B.:** If you save this notebook, it **will not** be saved to the GitHub repo.
Pushing changes back to the GitHub repo through the container is not possible with Binder.
**Any changes you have made to files inside the Binder will be lost once you close the browser window.**

## 6. Sharing your Work

Binder is all about sharing your work easily and there are two ways to do it:

- Share the **<https://mybinder.org/v2/gh/your-username/my-first-binder/HEAD>** URL directly
- Visit **<https://mybinder.org>**, type in the URL of your repo and copy the Markdown or ReStructured Text snippet into your `README.md` file.
  This snippet will render a badge that people can click, which looks like this: ![Binder](https://mybinder.org/badge_logo.svg)

**TO DO:** :vertical_traffic_light:

1) Add the **Markdown** snippet from **<https://mybinder.org>** to the `README.md` file in your repo
   - The grey bar displaying a binder badge will unfold to reveal the snippets.
     Click the clipboard icon next to the box marked with "m" to automatically copy the Markdown snippet.
2) Click the badge to make sure it works!

## 7. Accessing data in your Binder

Another kind of dependency for projects is **data**.
There are different ways to make data available in your Binder depending on the size of your data and your preferences for sharing it.

### Small public files

The simplest approach for small, public data files is to add them directly into your GitHub repository.
They are then directly encapsulated into the environment and versioned along with your code.

This is ideal for files up to **10MB**.

### Medium public files

To access medium files **from a few 10s MB up to a few hundred MB**, you can add a file called `postBuild` to your repo.
A `postBuild` file is a shell script that is executed as part of the image construction and is only executed once when a new image is built, not every time the Binder is launched.

See [Binder's `postBuild` example](https://mybinder.readthedocs.io/en/latest/config_files.html#postbuild-run-code-after-installing-the-environment) for more uses of the `postBuild` script.

**N.B.:** New images are only built when Binder sees a new commit, not every time you click the Binder link.
Therefore, the data is only downloaded once when the Docker image is built, not every time the Binder is launched.

### Large public files

It is not practical to place large files in your GitHub repo or include them directly in the image that Binder builds.
The best option for large files is to use a library specific to the data format to stream the data as you're using it or to download it on demand as part of your code.

For security reasons, the outgoing traffic of your Binder is restricted to HTTP or GitHub connections only. You will not be able to use FTP sites to fetch data on mybinder.org.

### Private files

There is no way to access files which are not public from mybinder.org.
You should consider all information in your Binder as public, meaning that:

- there should be no passwords, tokens, keys etc in your GitHub repo;
- you should not type passwords into a Binder running on mybinder.org;
- you should not upload your private SSH key or API token to a running Binder.

In order to support access to private files, you would need to create a local deployment of [BinderHub](https://binderhub.readthedocs.io/en/latest/) where you can decide the security trade-offs yourselves.

**N.B.:** Building a BinderHub is not a simple task and is usually taken on by IT/RSE groups for reasons around managing maintenance, security and governance.
However, that is not to say that they are the _only_ groups of people who should/could build a BinderHub.

## 8. Get data with `postBuild`

**TO DO:** :vertical_traffic_light:

1) Go to your GitHub repo and create a file called `postBuild`
2) In `postBuild`, add a single line reading: `wget -q -O gapminder.csv http://bit.ly/2uh4s3g`
   - `wget` is a program which retrieves content from web servers. This line extracts the content from the bitly URL and saves it to the filename denoted by the `-O` flag (capital "O", not zero), i.e. `gapminder.csv`.
     The `-q` flag tells `wget` to do this quietly, i.e. don't print anything to the console.
3) Update your `install.R` file to install two additional dependencies, `"tidyr"` and `"ggplot2"`. To do so, supply a character vector of the required packages to `install.packages()` instead of a single character string. The installation command should now look like this:

   ```r
   install.packages(c("readr", "tidyr", "ggplot2"))
   ```

    - These packages aren't necessary to download the data but we will use them to read the CSV file, process it and make a plot
4) Click the binder badge in your README to launch your Binder

Once the Binder has launched, you should see a new file has appeared that was not part of your repo when you clicked the badge.

Now visualise the data by creating a new notebook ("New" :arrow_right: "R") and running the following code in a cell.

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

See this [Software Carpentry lesson](https://swcarpentry.github.io/python-novice-gapminder/09-plotting/index.html) for more info.

## Beyond Notebooks...

**JupyterLab** is installed into your containerized repo by default.
You can access the environment by changing the URL you visit to:

> **<https://mybinder.org/v2/gh/your-username/my-first-binder/HEAD?urlpath=lab>**

**N.B.:** We've already seen how the `?filepath=` argument can link to a specific file in the ["What Binder Provides"](#what-binder-provides) section at the beginning of this workshop.

Here you can access:

- Notebooks
- IPython consoles
- Terminals
- A text editor

If you use R, you can also open **RStudio** using `?urlpath=rstudio`.

## Now over to you!

Now you've binderized (bound?) this demo repo, it's time to binderize the example script and data you brought along!

**Some useful links:**

- Choosing languages:
  - **<https://mybinder.readthedocs.io/en/latest/howto/languages.html>**
- Configuration files:
  - **<https://mybinder.readthedocs.io/en/latest/config_files.html>**
- Example Binder repos:
  - **<https://mybinder.readthedocs.io/en/latest/sample_repos.html>**
- Getting data:
  - With `wget`: **<https://github.com/binder-examples/getting-data>**
  - With `quilt`: **<https://github.com/binder-examples/data-quilt>**
  - From remote storage: **<https://github.com/binder-examples/remote_storage>**
