# Risk assessment: complexity and impact

## The risk matrix

A risk matrix is a popular way of quantifying the risk of your project. 
One axis measures exposure in some way, and the other the impact of a mishap.
The further from the origin an event sits, the more safeguards are needed to make the risk acceptable.

![Impact vs complexity risk matrix](../../figures/risk_matrix.png)

In our case, we will use ‘complexity’ and ‘impact’ as the two axes. Below are some case studies which illustrate how it works.

### Case 1
Richard needs to submit 100 small jobs to the department cluster, with the names of the jobs varying according to a simple pattern. This is tedious and he wants to go outside and play. 
Therefore, Richard decides to write a short shell script to submit all the jobs. 
He pauses for a few seconds and asks:
_"How complicated is this? It’ll only be about 1 screen of text."_
_"What if it goes wrong? The jobs won’t submit or run and I’ll get some failure emails."_

Here, Richard decides that both the complexity and impact of this tiny piece of software are low. 
Therefore, using version control and writing documentation is disproportionate right now. 
He decides to do a dry run by echoing the submit line to the terminal so he can give it a quick check.

A few weeks later, someone else in the lab wants to do the same thing. 
Richard considers his script which had worked quite well for him. 
But the goalposts have moved, so Richard pauses for a few more seconds and reassesses the risk.
It's now worthwhile uploading the code to a repository using version control so that the latest version is always available.
It also makes sense to document the usage of the script: how it is called, whether it takes any parameters, and so on.

5 years later, Richard’s script has evolved into a large workflow control system allowing several universities to manage complex workflows  consisting of thousands of jobs being submitted to a range of different compute resources. 
The software now has a formal project board that sets the governance and direction of the software, ensuring that it is sustainable and that it meets the needs of the hundreds of users worldwide.

### Case 2

Jemma is having some trouble visualising some data. 
The library she normally uses can’t cope with the format her data. 
She’s heard about Seth’s Friday afternoon project where he’s written a wrapper around this library to solve what seems to be the same problem. 
They have a coffee and decide to work together. 
During this coffee, they make some decisions about how they’re going to work successfully together; this is their risk assessment. 
Seth agrees to go away and improve the inline documentation and add some use case examples before sharing. 
Jemma agrees to set up a repository into which Seth will put the code.

Over time, more people start to make use of this software, with feature requests adding complexity and changes in the underlying library causing breakages and compatibility issues. 
Jemma and Seth agree that using the wrapper has become risky because the impact of publishing wrong results is quite large.
They therefore improve their testing, introduce continuous integration and a review process to ensure things remain sustainable. (As an aside, in this case they could suggest to the original library's maintainers that they add support for the format of the data!)

The key point of these case studies is that every piece of software has different needs to be sustainable, and these requirements can change over time. 
The use of version control, testing, documentation, continuous integration and other software engineering practices are useful for managing risk. 
Using none of these tools leaves your software exposed to things going wrong, but using all of them from the outset can get in the way of innovation.
The risk assessment approach helps you find the toolset your project needs at each level of maturity. 

## More about measuring complexity
One measure of complexity is line count.
The more lines you have, the more places there are to make a mistake. 
However, there are other things one might care about.
How many libraries do you depend on? How many functions are there? All of these measure the complexity of the codebase.
Complexity can take other forms too.
How many use cases are there?
Does your blob counting software only get used for counting blobs in the biosciences?
Are there people using it to count blobs in CCTV images?
What types of computer are people using it on?
CPU? GPU? Raspberry Pi?
Take a broad view of your software.

## More about measuring impact
What happens when (not if) your software doesn’t work?
Sometimes, it just annoys you for a few minutes.
However, other software going wrong can have huge consequences—the retraction of your seminal paper or even lives being lost.
Measuring the impact requires good knowledge of what your software is being used for.
It can sometimes be difficult to keep track of this until things go wrong.
However, one can try to head this off at the pass by asking questions like ‘is this piece of software I use for the analysis in my paper any good?’.
Again, take a broad view of your software.