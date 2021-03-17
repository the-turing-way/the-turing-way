# Barriers to reproducibility

So far we have described the [importance](../01/importantforscience) of reproducible research and motivated why we think [you should care](../02/whycare).

But there are many barriers to reproducible research.
You can watch Kirstie Whitaker describe some of them in [her talk about _The Turing Way_](https://youtu.be/wZeoZaIV0VE?t=312) at [csv,conf,v4](https://csvconf.com/2019) in May 2019.
You can use and re-use her slides under a CC-BY licence via Zenodo (doi: [10.5281/zenodo.2669547](https://doi.org/10.5281/zenodo.2669547)).
The section describing the slide below starts around 5 minutes into the video.

| ![Barriers to reproducible research](../../figures/reproducibility/barriers.png) |
| -------------------------------------------------------------------------------------------------------- |
|  Some of the barriers to reproducible research. |

This chapter outlines some of those barriers, and a couple of suggestions to get around them.

## Plead the fifth

No-one wants to incriminate themselves, and no-one is infallible. Putting your code online can be very revealing and intimidating, and people are scared of being judged by others. However, releasing code can help other researchers provide feedback, learn and may help them in their research. Publishing your code encourages you to write your code to a high standard and can help generate new ideas. **Let the person who is without bugs report the first error.**

## Publication bias towards novel findings

Novel results are not necessarily accurate or interesting but they are rewarded in the academic world!
Papers that do not find statistically significant relationships are hard to publish, particularly if the results *do not* reproduce previously published findings.
(That includes statistically significant findings that go in the opposite direction to already published work.)
Similarly, an article might be less likely to be accepted to a journal or a confence if it successfully reproduces already-published results instead of producing a new set.
There's a good chance that reviewers will say "we already know this" and reject the submission.

John Ioannidis published an influential paper in 2005 titled "Why Most Published Research Findings Are False" (doi: [10.1371/journal.pmed.0020124](https://doi.org/10.1371/journal.pmed.0020124)) which discusses the many factors that contribute to publication bias.
Therefore it is very likely that there is a lot of duplicated work in data science.
Too many different researchers are asking the same question, not getting the answer they expect or want, and then not telling anyone what they have found.

## Held to higher standards than others

A researcher who makes their work reproducible by sharing their code and data may be held to a higher standard than other researchers.
If authors share nothing at all then all readers of a manuscript can do is trust (or not trust) the results.
If code and data are available, peer reviewers may go looking for differences in the implementation (compared to how they would have analysed the data) and require additional changes from the authors of the submitted manuscript before it is accepted for peer review.
This problem also relates to readers of a published paper scrutinising the work more carefully as described in the [Plead the Fifth](#plead-the-fifth) section above.

## Is not considered for promotion

In the current academic system, a primary consideration for promotion is the proven ability to be awarded grants and recruit students.
Both funding bodies and prospective students value novelty (it is probably part of the human condition!) and this behaviour is reflected in preferentially rewarding papers with a high [journal impact factor](https://en.wikipedia.org/wiki/Impact_factor).
As [discussed above](#publication-bias), this bias towards novelty causes a systematic publication bias.

More broadly, the promotion system in academia tends to reward individuals who have shown themselves to be different than others in their field.
That means sharing code and data to make it easy for "competitors" to do the same work ends up being discouraged by promotion and funding selection panels.
A good example of this bias is the Nobel Prize award which only goes to a small number of researchers each year, and as such ["overlooks many of its important contributors"](https://www.theatlantic.com/science/archive/2017/10/the-absurdity-of-the-nobel-prizes-in-science/541863/) (Ed Yong, The Atlantic, 2017).
One of the goals of _The Turing Way_ is to draw attention to the misalignment of the tenure and promotion process with collaborative and reproducible data science.

## Barrier 5

*replace this text with the content of barrier 5*

## Takes time

Making an analysis reproducible takes time and effort, particularly at the start of the project.
This may include agreeing upon a [testing framework](.../../testing/testing), setting up [version control](../../version_control) such as a Github repository and [continuous integration](../../continuous_integration/continuous_integration), and [managing data](../../rdm/rdm.html).
Throughout the project, time may be required to maintain the reproducible pipeline.

Time may also be spent communicating with collaborators to agree which parts of the project may be open source and when and how these outputs are shared.
However, time may be lost at review due to framework explanation and suggested adaptations.

There will be fewer errors and less time spent correcting mistakes.
The analysis pipeline can be easily adapted as needed in response to co-author and reviewer requests.


## Support additional users

Many people worry that by making their analysis reproducible they will be required to answer lots of questions from future users of their code.
These questions may cover software incompatibility across operating systems and the dependencies changing over time (see the [Big data and complex computational infrastructure](#big-data-and-complex-computational-infrastructure) barrier below).
They may also include questions about how to adjust the code for a different purpose.
This barrier is based in part on conflating "reproducible" with "open" research.
The _Turing Way_ [definition of "reproducible"](../03/definitions) doesn't require authors to support the expansion and re-use of the data and code beyond running the exact analyses that generate the published results in the accompanying manuscript.

In almost all cases, making code and data open source requires better documentation than a researcher would write for themselves.
This can feel like an additional barrier, although - as discussed in the previous section on reproducible research taking extra time](#takes-time) it is likely that the primary beneficiaries of well commented and tested code with detailed documentation are the research team - particularly the principle investigator of the project - themselves.

## Big data and complex computational infrastructure

Big data is conceptualised in different ways by different researchers.
"Big" data may be complex, come from a variety of data sources, is large in storage volume and/or be streamed at very high temporal resolution.
Although there are ways to set random seeds and take snapshots of a dataset at a particular moment in time, it can be difficult to have identical data across different runs of an analysis pipeline.
This is particularly relevant in the context of tools for parallel computing.
For example, streaming data such as flight tracking or internet traffic can not be stored and must be processed in real time.

A more common challenge for "big data" researchers is the variability of software performance across operating systems and how quickly the tools change over time.
An almost constantly changing ecosystem of data science technologies is available, which means reproducing results in the future is highly variable and dependent on using perfectly backwards compatible tools as they develop.
Very often the results of statistical tests will vary depending on the configuration of the infrastructure that was used in each of the experiments, making it very hard to independently reproduce a result.
Experiments are often dependent on random initialisation for iterative algorithms and not all software includes the ability to fix a pseudorandom number without limiting parallelisation capabilities (for example  e.g. in Tensorflow).
These tools can require in depth technical skills which are not widely available to data scientists.
The Hadoop framework, for instance, is extremely complex to deploy data science experiments without strong software and hardware engineering knowledge.
Even "standard" high performance computing, can be difficult to set up to be perfectly reproducible, particularly across different cloud computing providers or institutional configurations.

## Being reproducible does not mean the answer is right

By making the code and data used to produce a result openly available to others, our results may be **reproduced** but mistakes made by the initial author can be carried through.
Getting the same wrong answer each time is a step in the right direction, but still very much a **wrong** answer!

It is important to remember that reproducibility is necessary but not sufficient for good quality research.
A critical approach is needed, rather than naively using existing software without understanding what it does.
(See, for example, [a discussion](https://ryxcommar.com/2019/08/30/scikit-learns-defaults-are-wrong) in August 2019 about whether the default settings for Scikit-learn's implementation of logistic regression are misleading to new users.)
Interperability and interoperability are required to properly evaulate the original research and to strengthen findings.
