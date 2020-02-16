# Feedback report on The Turing Way 'Boost your Research Reproducibility with Binder' workshop | January 2020

Kirstie Whitaker - representing _The Turing Way_ team - held a 'Boost your Research Reproducibility with Binder' workshop at the [British Antarctic Survey](https://www.bas.ac.uk) in Cambridge on 31 January 2020.

The half day workshop was organised by [Dr Anita Faul](https://www.bas.ac.uk/profile/anfaul/) - a data scientist and machine learning expert at BAS.
It was a closed event for BAS team members, but Kirstie's talk was recorded and is available for anyone to view at *insert youtube link*.
The workshop went smoothly all thanks to Anita's hard work - thank you!

The agenda for this [British Antarctic Survey: 31 January 2020](../agenda.md#british-antarctic-survey-31-january-2020) workshop includes with links to PDFs of the presentations and markdown files for the code-along exercises.

## Instructor and team reflections

Kirstie re-did the slides for the introduction and "Why you need a reproducible computing environment and how Binder can help" presentations ([IntroBoostResReproBinder_20200131.pdf](../workshop-presentations/IntroBoostResReproBinder_20200131.pdf) and [ReproducibleComputationalEnvironment_20200131.pdf](../workshop-presentations/ReproducibleComputationalEnvironment_20200131.pdf)) before this workshop so they're now more interoperable with other talks about the project.
They use the Turing Institute template and include a doi and twitter hashtag.

There was a major snafu with the second of the [paired examples](paired_examples.md) exercise.
It turns out that the [CompEnv-Ex2](https://github.com/alan-turing-institute/CompEnv-Ex2) one relies on a very old (and no-longer supported) version of matplotlib and (probably) as a result of python 2 being retired on [1 January 2020](https://pythonclock.org/) the binder with that old version didn't build.

* Fortunately Kirstie realised this before the workshop so was prepared to ask participants to skip that example.
* Huge thank you to Turing Way team member and Binder operator Sarah Gibson who tried to fix the problem during the workshop (after a last minute request on Gitter).
  And thank you to the workshop participants for their understanding of the problem.
* Fortunately for future workshops, Sarah [opened an issue](https://github.com/alan-turing-institute/CompEnv-Ex2/issues/1) and [fixed the problem](https://github.com/alan-turing-institute/CompEnv-Ex2/pull/2)! 🙌 ✨ 👾
* The lesson to learn is to double check all the exercises well in advance of the workshop.
  Kirstie ended up missing out on some very interesting discussions because she was trying to multitask and fix the error at the same time.

Taking a team photo was really wonderful!
Let's try to make sure that's in all future workshops.

![](https://raw.githubusercontent.com/scott-hosking/my-first-binder/master/BoostReproducibilityBinder_BAS_2020-01-31.jpg)

*Add Anita's comments here.*

## Participant feedback

At the end of each workshop participants were asked to fill in feedback forms rating their understanding and confidence before and after the workshop, what they liked about the workshop, what could be improved and whether they will use Binder in the future.

### Understanding and Confidence

*Replace the `X`, `Y`, `Z` values below, and adapt the sentences as needed.*

On average participants reported an increase of between `X` and `Y`% in their understanding and confidence in using Binder, capturing their computational environment and reproducing their research.

The biggest increases (`Z`%) were in *insert aspect here*.

Participants showed the smallest increase in understanding *insert aspect here*.

*Add sentence interpreting these numbers if relevant.*

### Positive feedback

*Add sentence summarising positive aspects of the feedback.*

Some selected comments are included below:
* *add quote here*
* *add quote here*

*Add a tweets from participants here if relevant.*

### Areas for improvement

Whilst the vast majority of feedback was positive there were a couple of areas participants identified could be improved:

* *Add aspect of the workshop that could be changed here*
* *Add aspect of the workshop that could be changed here*

### Impact

X out of N participants said that they would use Binder in some capacity in the future.
Most people intended to use Binder to *insert purpose here*.

