# Case study: branchLSTM

_This project was part of the Alan Turing Institute's Reproducible Research Champions programme, led by Kirstie Whitaker and Martin O'Reilly.
Elena Kochkina was one of three Champions selected from Turing researchers, and her project was further developed by Louise Bowler, a member of the [Research Engineering Group](https://www.turing.ac.uk/research/research-programmes/research-engineering).
Here, Louise writes about her experiences of working on the project._

_The branchLSTM project is available on [GitHub](https://github.com/kochkinaelena/branchLSTM/), and the full paper can be found on the [SemEval 2017 website](https://www.aclweb.org/anthology/S17-2083)._

In 2017, Elena took part in one of the tasks for the [International Workshop on Semantic Evaluation](http://alt.qcri.org/semeval2017/).
In [Task 8A](http://alt.qcri.org/semeval2017/task8/), participants were given data consisting of a selection of tweets from Twitter, where the topic of the tweets was a rumour (defined by the task organisers as a “circulating story of questionable veracity, which is apparently credible but hard to verify, and produces sufficient skepticism and/or anxiety so as to motivate finding out the actual truth”).
The data were arranged in a tree-like structure - the first (root) tweet presented the rumour, and branching tweets were responses to the original or other tweets in the tree.
The aim of the task was to identify whether each tweet in the conversation was supporting, denying, querying or commenting towards the rumour in the root tweet.

Elena used a long short-term memory (LSTM) model which incorporated the branching structure of the tweet conversation - hence the project name, branchLSTM (her [paper](https://www.aclweb.org/anthology/S17-2083) gives the full details).
Parameterising the model was time-consuming, so Elena had made extensive use of the high performance computing resources available at the University of Warwick.
We knew this would throw several interesting challenges our way: we would have to try to reproduce the computational environment used for the original analysis, and we would also have to deal with the inherent difficulties in reproducing results in multi-threaded computation.

Elena's code can be divided into three main stepsIn the first, the data from Twitter are converted into a numerical form.
In the second, the hyperparameters of the branchLSTM model are selected based on training and development datasets.
In the third, the model with the optimal hyperparameters is applied to the test dataset to obtain predictions of whether each tweet is supporting, denying, querying or commenting on the rumour in the original root tweet.
Elena had saved the values of the hyperparameters used for her final run of the code, which was incredibly helpful for checking reproducibility as it was easy to isolate the two stages that involved the branchLSTM model itself.

My first task was to run the final stage of the code on resources other than the cluster that Elena had previously usedI ran my first tests on the computers I had available (an iMac and MacBook Pro) and an NC6 virtual machine from Microsoft Azure, all of which yielded different overall accuracy values to those in Elena's paper.

At this stage, such a result wasn't unexpected - I had used the most up-to-date versions of the Python packages used in the project, whereas most of Elena's work on the project had taken place over a year earlierBut the results were also different between the three computers, so before getting stuck into how the package versions affected the model, I decided to check the earlier stages of the script, where the data preprocessing took place.

This uncovered some of the most interesting differences in interoperability that I've ever come across!

## My computer is not the same as your computer

Each tree of tweets was stored in a separate file, within a folder concerning the theme of those tweets.
The lists of these files were identified by using Python's `os.listdir()` command to list all the files within the relevant data directories.
The order of the output of `listdir()` is actually arbitrary, but this isn’t apparent if you always work on the same machine, as Elena had done.
While the same data overall was being read in on different computers, it was concatenated together in a different order and so the data provided to the model was not exactly the same.
This led to slight differences in model accuracy.

Sorting the list after generating it solved this problem, and it fortunately seemed that the default sort order on the cluster used by Elena had been alphabetical (as it is on many systems), meaning that we could generate the same order used originally.

## How long is a smiley face?

Once loaded, numerical representations of each tweet were generated as 314-element arrays.
The first 14 elements stored quantifiable features of the tweet, such as the number of negation words and the presence of attachments, and the remaining 300 elements stored a [Word2vec](https://skymind.ai/wiki/word2vec) representation of the tweet's textual content.
When I compared these features across machines, I noticed something rather odd - the contents of corresponding elements were identical, apart from those which stored the length (to be more precise, the character count) of some of the tweets.

Judging the length of a tweet seemed like a very simple task - just count the number of characters.
So why were the counts different? Further investigation showed that the mismatched counts occurred in tweets containing emoticons, which led me to look into how these characters were represented in Unicode.

Unicode characters are stored as one or more code points, with the specification dependent on whether the version of Python used is a wide or narrow build.
Most of these terms were unfamiliar to me, so I’d recommend [this blog](https://www.b-list.org/weblog/2017/sep/05/how-python-does-unicode/) post if you’d like a detailed rundown.
On a wide build, each code point is stored in four bytes, while on a narrow build only two bytes are required.
This is fine for most characters, but code points that fall outside of the range that can be represented by two bytes are instead coded as surrogate pairs of two code points.
It was differences in the build type of Python that had caused the differences in tweet length - on my MacBook Pro, emoticons were calculated to have length two as they were represented using surrogate pairs, while the length was calculated as expected, as a single character, on Linux systems (this meant that a consistent length of one had been used in Elena’s paper).
As in the previous example about file load order, this is something that wasn't an issue when Elena originally performed her analysis as she worked on only one machine, but moving the code out of its original computational environment exposed these differences.

To ensure the length of the tweet was calculated consistently, I replaced the pairs of Unicode characters with placeholder letters using a regular expression.
Using the `len()` command to obtain the tweet length then gave consistent results on all machines.

Note: As of Python 3.3 and later, there is a single build rather than wide or narrow options and Unicode is handled in the same way on all systems.
This project used Python 2.7.

## Returning to the package versions

With the preprocessing stage now giving consistent representations of the data across all machines, it was time to look at the influences of the package versions on the output.
At the time Elena was developing this project, neither of the Theano or Lasagne packages had reached version 1.0.
In [semantic versioning](https://semver.org/), such 0.x.x version numbers indicate that the package may undergo large changes with each release, and so getting the version numbers correct was important if we were to ensure the output of the model was as intended.

I knew roughly when Elena had installed the packages, so I started with the versions released around that time.
After trying out a few combinations, I was able to get accuracy values very close to those in the publication when using the optimal set of hyperparameters on the NC6 GPU from Microsoft Azure.
The results were consistent, but there were very small differences between these results and those in Elena’s paper.
As we were using slightly different hardware, we chose to call this an acceptable level of reproducibility rather than searching for further issues.
With the project’s dependencies now pinned down, I was able to start on a set of instructions for setting the project up on a local computer or on Microsoft Azure resources, which can be found in the [README](https://github.com/kochkinaelena/branchLSTM/blob/master/README.md) of the branchLSTM project.

## Tracking down randomness

I then moved on to check the remaining part of Elena’s code, the hyperparameter optimisation process.
Running this stage took around six hours even when using a GPU, so testing this aspect of the project for reproducibility was far more time-consuming than the rest.
Unlike when I ran the other parts of this project’s code, the results of the hyperparameter optimisation process were not consistent each time that I ran the code.
This was somewhat puzzling, given that Elena had been careful to specify random seeds wherever needed.

The hyperparameter optimisation routine was taken from the `hyperopt` package, and digging into the documentation of the package yielded the answer.
While the algorithm Elena had used was not stochastic during the optimisation process itself, the initial set of hyperparameters used by the algorithm was chosen randomly from the available options.
With no seed specified, the system time would have been used to initialise the random number generator used to select the starting point of the algorithm; something which we can’t recover.
This setting was only mentioned in the package’s docstrings, not in any of the tutorials or guides, so it’s entirely understandable that this was missed given that re-running the optimisation process multiple times wasn’t practical.

With the seed now fixed, we can regenerate consistent optimal hyperparameters, although not the exact ones used in the paper as of yet.
I added some additional diagnostic output to the optimisation stage that indicates that identical accuracy scores can be achieved through several different hyperparameter combinations, showing that we’re dealing with a difficult search space with many local minima.
Further tests will hopefully yield a starting point from which we can recover the exact settings from the paper, yet the similarity of the accuracy scores indicates that the method is robust to moderate changes in the model’s hyperparameters.

## Reflections on reproducibility

I’ve learned a lot from this project - I’d expected some ups and downs as we moved the project away from the original cluster and onto Microsoft Azure, but some of the other challenges, particularly the ‘what length is an emoji?’ problem, came as complete surprises.
Achieving complete reproducibility in these type of projects is a lot to expect without the resources to re-run the entire analysis across many different platforms, so I am pleased we have been able to use this opportunity through the Reproducible Research Champions programme to identify many points where it is convenient and practical to take steps to check and improve reproducibility.

First, recording package versions is an easy win for reproducibility.
A simple `pip freeze` or `conda env export` command in Python yields enough information to reconstruct the Python-based aspects of the computational environment within which a project sits.
Having such information recorded also makes it easier to transfer the project across different systems, such as when moving to a new cluster or when someone else wants to try out your project.

Second, identifying distinct stages of a project makes it far easier to track down problems.
Elena’s project naturally split into three stages: preprocessing, optimal hyperparameter identification and application of the trained model to the test data.
Each of these three stages was associated with an output: processed data, a list of optimal hyperparameters and the accuracy and other scores that demonstrated the model’s performance.
Elena’s decision to save each of the outputs made it much easier to identify where issues in reproducibility were arising from when the project was moved into a different computational environment.
A natural next step, were this to become a longer-term project for Elena, would be to introduce a test suite to check the outcomes of each of the three stages, perhaps with a smaller, “toy” dataset to speed up the process.

Third, getting someone else to attempt to run your code has many benefits.
In the academic world, it’s great news if someone else wants to use your code - it means that they’ve read your paper and are looking to build upon your work, which is just what you want to hear when you’re trying to achieve impact, up your citation count or increase your project’s longevity.
But getting your codebase ready for these potential users is hard to do.
Asking someone else in your lab (or in this case, someone like me!) to run your code, or even a short test case, highlights difficulties in setting up the project as well as potential issues for reproducibility that arise from differences in the computational environment.
