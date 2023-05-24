# Zero-to-Binder Tutorial: Instructor Guide

## Individual learners

If you are working through the Zero-to-Binder tutorial on your own (as opposed to as part of a workshop), please see [`zero-to-binder-solo.md`](https://github.com/alan-turing-institute/the-turing-way/blob/main/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder-solo.md).
This version includes screenshots to clarify the instructions and let you compare outcomes.

## Running your own Binder Workshop

If you are running your own Binder workshop using our materials, we would recommend that whoever is leading the Zero-to-Binder session also work through [`zero-to-binder-solo.md`](https://github.com/alan-turing-institute/the-turing-way/blob/main/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder-solo.md) to get to grips with the material and understand what each step is demonstrating.

We have set up the session with the following format, though you are free to alter this to suit your needs! :slightly_smiling_face:

* **Before the workshop:** We ask that attendees bring a short analysis script/notebook (taking less than 5 mins to run) and a small dataset (~10MB, a sub-set of data is fine and it must not be sensitive!)
* **Zero-to-Binder Session:** The session leader live codes the instructions along with the attendees following [`zero-to-binder.md`](https://github.com/alan-turing-institute/the-turing-way/blob/main/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder.md) with some helpers on the floor to assist with problems.
  We used a Software Carpentry post-it system (green for completed; red for a problem) to assess the room and this corresponds to the traffic light emojis next to each TO DO section in the notes.
  There is also a bitly link to the instructions so that attendees can bring them up on their own machines: http://bit.ly/zero-to-binder-tutorial .
  This session should last around 1 hour, maybe a little longer if mybinder.org becomes overwhelmed.
* **Build your own Binder Session:** We then turn the workshop over to the attendees to apply what they've learned to the code and data they brought with them.
We give them 45 mins to 1 hour to work on their own Binders and ask whoever is comfortable doing so to present their Binder at the end of the session.

### Potential Problems

#### mybinder.org goes down

Unfortunately, there's not much that can be done about this other than to wait for it to come back online or have a back-up plan for the session.

Sometimes mybinder.org does become overwhelmed with a room full of people all trying to launch binders at the same time.
Usually waiting a short period and trying again will solve this problem.

#### Attendees using R

If you have attendees who bring R code, R packages and RStudio does take a particularly long time for Binder to build.
`tidyverse` especially is a very popular and large data package that can take a _very_ long time to load.
We recommend that R users modify their code to only install the required packages, and not the whole `tidyverse`.
For a more long-term solution, you can point R users to the direction of the following resources:

* https://github.com/binder-examples/rocker
* https://github.com/karthik/holepunch

These repositories provide resources to R users allowing them to build their own minimal Dockerfile containing R packages, which reduces launch time for mybinder.org.

## Contact Us

If you have any questions or issues setting up your Binder workshop, you can [contact us through gitter](https://gitter.im/alan-turing-institute/the-turing-way) or [open an issue](https://github.com/alan-turing-institute/the-turing-way/issues).
