# From Zero to Binder!

Sarah Gibson, _The Alan Turing Institute_

[**The Turing Way**](https://github.com/alan-turing-institute/the-turing-way) - making reproducible Data Science "too easy not to do"

Based on Tim Head's _Zero-to-Binder_ workshops which can be found here: http://bit.ly/zero-to-binder and http://bit.ly/zero-to-binder-rise

## Running Code is more complicated than Displaying Code

GitHub is a great service for sharing code, but the contents are **static**.

How could you _run_ a GitHub repository **without installing complicated requirements**?
Or even **in your browser**?

To run code, you need:
* Hardware on which to run the code
* Software, including:
  * The code itself
  * The programming language (e.g. Python, R)
  * Relevant packages (e.g. pandas, matplotlib, tidyverse, ggplot)

## What Binder Provides

[Binder](https://mybinder.org) is a service that provides your code and the hardware and software to execute it.

You can create a link to a **live, interactive** version of your code!

* An example binder link:

  > **https://mybinder.org/v2/gh/trekhleb/homemade-machine-learning/master?filepath=notebooks%2Fanomaly_detection%2Fanomaly_detection_gaussian_demo.ipynb**

  From this repo: **https://github.com/trekhleb/homemade-machine-learning**

  * Notice that the Binder link has a similar structure to the GitHub repo link
  * The "filepath" argument opens a specific notebook in the repo

## 1. Creating a repo to Binderize

**TO DO:** :vertical_traffic_light:

1) Create a new repo on GitHub called "my-first-binder".
   * Don't forget to initialise with a README!
2) Create a file called `hello.py` via the web interface with `print("Hello from Binder!")` on the first line and commit to master
   * Bad practice :see_no_evil: but we're not collaborating right now!

## 2. Launch your first repo!

**TO DO:** :vertical_traffic_light:

1) Go to **https://mybinder.org**
2) Type the URL of your repo into the "GitHub repo or URL" box.

   Should look like this:
   > **https://github.com/your-username/my-first-binder**

3) As you type, the webpage generates a link in the "Copy the URL below..." box

   Should look like this:
   > **https://mybinder.org/v2/gh/your-username/my-first-binder/master**

4) Copy it, open a new browser tab and visit that URL.
   * You will see a "spinner" as Binder launches the repo.

If everything ran smoothly, you'll see a Jupyter Notebook interface.

#### What's happening in the background?

While you wait, BinderHub (the backend of Binder) is:
* Fetching your repo from GitHub
* Analysing the contents
* Creating a Docker file
* Launching that Docker image in the Cloud
* Connecting you to it via your browser

## 3. Run `hello.py`

**TO DO:** :vertical_traffic_light:

1. In the top right corner, click "New" :arrow_right: "Terminal"
2. In the new tab with the terminal, type `python hello.py` and press return

`Hello from Binder!` should be printed to the terminal.

## 4. Pinning Dependencies

It was easy to get started, but our environment is barebones - let's add a **dependency**!

**TO DO:** :vertical_traffic_light:

1) In your repo, create a file called `requirements.txt`
2) Add a line that says: `numpy==1.14.5`
3) Check for typos!
4) Visit **https://mybinder.org/v2/gh/your-username/my-first-binder/master** again in a new tab

This time, click on "Build Logs" in the big, horizontal, grey bar.
This will let you watch the progress of your build.
It's useful when your build fails or something you think _should_ be installed is missing.

#### What's happening in the background?

This time, BinderHub will read `requirements.txt` and install version `1.14.5` of the `numpy` package.

## 5. Check the Environment

**TO DO:** :vertical_traffic_light:

1) In the top right corner, click "New" :arrow_right: "Python 3" to open a new notebook

2) Type the following into a new cell:
   ```python
   import numpy
   print(numpy.__version__)
   numpy.random.randn()
   ```
   **Note the two underscores either side of `version`!**

3) Run the cell to see the version number and a random number printed out
   * Press either SHIFT+RETURN or the "Run" button in the Menu bar

## 6. Sharing your Work

Binder is all about sharing your work easily and there are two ways to do it:
* Share the **https://mybinder.org/v2/gh/your-username/my-first/binder/master** URL directly

* Visit **https://mybinder.org**, type in the URL of your repo and copy the Markdown or ReStructured Text snippet into your `README.md` file.
  This snippet will render a badge that people can click, which looks like this: ![Binder](https://mybinder.org/badge_logo.svg)

**TO DO:** :vertical_traffic_light:

1) Add the **Markdown** snippet from **https://mybinder.org** to the `README.md` file in your repo

   * The grey bar displaying a binder badge will unfold to reveal the snippets.
    Click the clipboard icon next to the box marked with "m" to automatically copy the Markdown snippet.

2) Click the badge to make sure it works!

## Beyond Notebooks...

**JupyterLab** is installed into your containerized repo by default.
You can access the environment by changing the URL you visit to:

> **https://mybinder.org/v2/gh/your-username/my-first-binder/master?urlpath=lab**

**N.B.:** We've already seen how the `?filepath=` argument can link to a specific file.

Here you can access:
* Notebooks
* IPython consoles
* Terminals
* A text editor

If you use R, you can also open **RStudio** using `?urlpath=rstudio`.
