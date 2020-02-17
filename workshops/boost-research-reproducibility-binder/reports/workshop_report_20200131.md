# Feedback report on The Turing Way 'Boost your Research Reproducibility with Binder' workshop | January 2020

Kirstie Whitaker - representing _The Turing Way_ team - held a 'Boost your Research Reproducibility with Binder' workshop at the [British Antarctic Survey](https://www.bas.ac.uk) in Cambridge on 31 January 2020.

The half day workshop was organised by [Dr Anita Faul](https://www.bas.ac.uk/profile/anfaul/) - a data scientist and machine learning expert at BAS.
It was a closed event for BAS team members, but Kirstie's talk was recorded and is available for anyone to view at https://youtu.be/q_bfyfZGCVY.

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

Anita added the following feedback:

> I was very happy with the workshop and impressed by the efforts trying to fix the example which wasn't working in real time.
> Kirstie was very engaged and happy to answer all questions.
> There were also interesting discussions over lunch and at coffee.
> In hindsight, it would have been useful to highlight the software carpentry lessons (https://software-carpentry.org/lessons/) for people to work through before the workshop. or run one of those workshops before this one.

## Participant feedback

At the end of each workshop participants were asked to fill in feedback forms rating their understanding and confidence before and after the workshop, what they liked about the workshop, what could be improved and whether they will use Binder in the future.

### Understanding and Confidence

All participants reported feeling **Confident** or **Very confident** in their understanding and confidence in using Binder and capturing their computational environment.

The biggest increases were in understanding what Binder does and feeling confident that they could use it for their own work.
And the smallest increases were in participants' confidence in their ability to share reproducible research.

After the workshop everyone **Strongly Agreed** that research reproducibility should be part research culture and 4/5 respondents agreed that BAS should develop institutional guidance for research reproducibility.

### Positive feedback

The positive feedback was focused around the format and pacing of the workshop and the value of having a friendly and approachable instructor.

Some selected comments are included below:
* I thought the workshop was very well run, with an inclusive code of conduct and was a very good introduction to The Turing Way and BinderHub. I thought the pace was right and the examples were useful.
* Very useful and very helpful to do it interactively
* The examples were clear and working through these simple examples together, at a slow pace was *really* helpful.
* The format worked well - the beginning presentation provided enough information to get started, and it felt like we were able to move on to hands-on examples quite quickly.
* Good balance between theory and practice, very approachable speaker.

### Areas for improvement

Whilst the vast majority of feedback was positive, there were a couple of areas participants identified could be improved:

* Links to software carpentry.
* Making it clear what the broad idea was behind each step in the example creation of a binder, with some brief discussion of how you'd approach it for more complex and substantial projects, rather than purely focusing on the simple example in hand would have made me feel a bit more confident about applying the method myself on more realistic examples.

The links to additional materials to support participants before the workshop can easily be added to the information that is sent out when they register.

Adding additional material and real world examples are already part of the longer workshop.
This feedback emphasises the compromise that has to be made to run a half day rather than full day event.

### Impact

4 out of 5 participants said that they would use Binder in some capacity in the future.
Most people intended to use Binder to ensure their research works across multiple computational environments and sharing their research.

Some selected comments are included below:

* I think I will absolutely use binder in future. Using the 'docker' aspects to ensure I am replicating my environment is something I have never done before, but see will be hugely useful both now when working on different machines, but also looking further ahead will be great if I move institutions, or spend time working at other places.
  Also, when publishing work, saving the entire set up, so the work is truly reproducible, and saved in a way I know will work again in future if I wanted to revisit it is really appealing!
* Possibly.
  My usual data and code are too large for Binder and I opt for directly using containers instead.
  It may be useful for small examples of my research, to demonstrate the method without requiring access to an HPC system.
