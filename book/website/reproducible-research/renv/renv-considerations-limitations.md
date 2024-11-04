# Considerations for choosing and limitations of reproducible environment tools

This chapter has covered a number of different tools / technologies for describing, capturing and sharing computational environments.
Two axes of comparison on which these methods differ are:

 - Verifiability (as defined in {cite}`Hinsen2018`) or the ability to inspect and understand how the environment was built
 - Completeness how much of the environment is described and how exactly

A virtual machine (VM) image is a highly complete way to capture a computational environment but in the absence of a description of how it was built it is not particularly verifiable.
Closed source software also inherently lacks verifiability.
Many package management tools for programming languages lack completeness, they cannot capture the system dependencies that using a container or VM can facilitate.

What are our options for describing a complete and verifiable compute environments, ideally without needing to attain mastery of a number of different different complex tools in order to do so?

## Verifiability

### Reproducing the images themselves

A container or virtual machine (VM) image once built given the same inputs will very likely give the same outputs but they are something of black box.
Whilst they can be inspected and details of how they were built inferred this is not always easy, and not really a feature around which these technologies were designed.
Their design came out of pragmatic considerations of capturing working computational environments to use in deployed software to keep things working in ever growing production environments.

This is changing, increasingly provenance, software manifests or 'bills of materials', and 'supply chain' are becoming a concern of industry.
This is for reasons of security and compliance with new cybersecurity regulations, so more moneyed interest is now being focused on these problems.

The file specifying how the container or VM image is built for example a Dockerfile helps us to some degree as this is a record of the steps taken to build an image of an environment.
However these methods can fall short in the completeness with which they capture these steps.

A common example is starting a Dockerfile with `FROM ubuntu:latest`, depending on when you ran this you may get a different output.
You will get which ever version of ubuntu was the latest at the time you built the image.
To reproduce this you would have to extract the version of ubuntu from the built image and specify it explicitly in the Dockerfile.
This is also dependent on the historical version still being available to download in order to build the image.
It is common to follow such a first line by up with updating the operating system in case any important patches have come out since the base image was built, this introduces another time depended aspect.
If you are relying on various resources from the internet during such a build what is at the other end of a URL can change or disappear from one build to the next.

Container or VM images alone do not provide useful insight into what a particular piece of logic in a chain of inference is nor why it was made.

###  Balancing stability & verifiability with rapid threat response

In cases where your systems are exposed to the open internet getting the latest security patches to your operating system is desirable.
However there are cases where you do not want the latest updates.
Your system may be an appliance or embedded device, the exactly consistent operation of which, is safety critical for some operation.
Any change to software on such a system must be extensively tested and potentially subject to regulatory processes before it can occur.
Such systems may not only need to be well tested but well understood so that their behaviour can be predicted and accounted for in unusual circumstances.
These systems are, hopefully, deeply and securely nestled in layers of protection from networked threats by firewalls which are moving fast and adapting to the latest threats or even air gaps.
This permits them to prioritise consistency, stability, and reliability and not themselves need to adapt to the latest threats. 

In academic contexts all that may be needed is the ability to re-run an analysis exactly as it was previously performed, to validate the basic reproducibility of an earlier result.
If there is a security vulnerability in some code used in a past analysis this doesn't matter as long as it has no impact of the analysis.
If it can be re-run in an isolated environment it may not to be worth the time of figuring out how to update the environment to patched versions without introducing feature updates which may break the analysis code.

There are plenty of online academic services where security is important and these contexts it is convenient if they are set up in such a fashion as to be able to reproduce responses would have provided at a previous point in time.
This is also true for services of this kind operating, for example in regulated industries, where an accounting may need to be given of how and why a given output was produced at a particular point in time for legal rather than scientific reasons.

### Including things you do not need

Another common problem here is 'packing more than you need' you might add something to your computational environment that you then never use and it's not always easy to tell what you do and do not need.
Many of the dependencies of what runs in your environment remain implicit.
Your base operating system is sufficient to provide the environment that you need but is all of it necessary?
When trying to understand your environment most of these technologies leave you with a lot of noise, a lot of extra parts that may or may not be relevant.
(This is also extra attack surface if you are taking a security lens on the problem.)

### Reproducible Builds & the ability to compare against other's results

Producing a reproducible image of a computational environment is somewhat analogous to the problem of producing reproducible binary builds of compiled software.
The ability for people to independently produce bit-for-bit identical binary builds from the same source code is a valuable feature for verifying that a cached binary build of a piece of software is what it claims to be.
Independent parties can take the same code build it and if they get the same result attest to its correctness, this is a valuable countermeasure to the introduction of malicious code during the build process that is not in the source tree.
[Reproducible Builds](https://web.archive.org/web/20240603001422/https://reproducible-builds.org/) is a project sharing best practices for achieving this across a number of open source software projects.
Guix's [`challenge`](https://guix.gnu.org/manual/en/html_node/Invoking-guix-challenge.html) command exposes the ability to compare a locally built to a pre-built binary provided by a remote package cache (a 'substitute' in Guix's terminology).
(The [attempt to introduce a backdoor into the XZ utils library](https://en.wikipedia.org/w/index.php?title=XZ_Utils_backdoor&oldid=1226548252) is an interesting case study into the intricacies of these sorts of attacks and the limits of technical measures for protecting such codebases.)

## Completeness

There are more or less complete ways to describe a computational environment.
We've seen a number of approaches to this problem in this chapter but many either miss certain aspects of an environment in its description or whilst they might capture the whole environment do so in an opaque fashion.

We will start by discussing the nature of the problem of dependencies in a little more depth and then move onto discussing some tools which offer more comprehensive solutions to the problem of more complete description of computational environments.
These are functional package management tools such as [Nix](https://nixos.org/) and [Guix](https://guix.gnu.org/).

### Dependencies - a deeper look

When working on an individual software project, you as the developer, will likely be paying most attention to the packages that you are using from your language's package repository.
You may use a language specific package manager to install and manage the packages that your project needs, in python this might be `pip`.
It is important to remember that your project's dependencies may also have dependencies, these become transitive dependencies of your project creating a dependency tree.
You may also use a language specific environment management tool so that you can have different projects with different version of the same dependencies on your system at the same time, in python this might be `venv`.

Where things start to get a bit more complicated are system dependencies.
A package in a language may expect another tool to be installed on the system on which it is installed, for example a performant image manipulation package written in another language that it uses to perform certain tasks by the language specific package.
Such packages are not managed by language specific package managers but by the operating system.
On Linux based systems this is usually another package manager such as `apt`, or `dnf` for installing packages in the `deb` and `rpm` package formats respectively.
MacOS and Windows do not natively expose package management tools to the end user but tools such as `homebrew` and `chocolatey` respectively add this functionality to these operating systems.

Another source of complexity are build-time vs run-time dependencies.
A build-time dependency is only need whilst a piece of software is being packaged or compiled but not once it is built.
The packaged or binary version requires only its run-time dependencies to be executed once built.
A compiler for example can be a build-time dependency, once compiled the tool likely does not need a compiler to perform its function, unless it itself is a build tool.

This leads in nicely to the bootstrapping problem for software dependency trees.
Software is written as source code but is generally distributed as pre-built packaged binaries, this saves time and resources as it only needs to built once centrally.
All of the tools necessary to build a given sequence of pieces of software must be available in the correct order to build up the dependency tree from source.
For this to be possible the dependency tree must be a directed acyclic graph.
acyclic as you cannot have a piece of software that indirectly depends on itself in order to be built, if you want to be able to bootstrap from source.
You can easily end up with loops in this graph when using pre-built binaries from others if you are not fastidious about keeping such loops out.
As you may imagine this gets interesting very fast for things like compilers, how these issues are resolved at the base of the tree is a fascinating subject in its own right but out of scope for the current discussion.
For a large collection of software, like a modern operating system, compiling everything in the right order from source 'manually' is a very laborious process.
If you want to experience some of what this is like or just get an idea of what this process would look like to do, then checkout the [Linux From Scratch](https://web.archive.org/web/2/https://www.linuxfromscratch.org/) project.
At the root of the tree is a potentially very minimal set of binary files, [GUIX is perhaps the project with the most complete ability to bootstrap from the most minimal starting point](https://web.archive.org/web/20240601042922/https://guix.gnu.org/en/blog/2023/the-full-source-bootstrap-building-from-source-all-the-way-down/) and in a completely automated fashion.

#### Dependency resolution & package conflicts

You can sometimes encounter situations where you need two tools installed which have mutually incompatible dependencies.
This arises because conventionally a package has one place on your system that it is installed with a single name with which it can be invoked in a given environment.
The name 'PackageX' can refer to only one version of that package in your environment.
Even if you can have version 1.0 and version 2.0 of 'PackageX' installed on your system at the same time by naming them differently centrally and aliasing them to their usual name in your environment you cannot generally depend on the different versions in the same environment.
For example: 'Tool A' requires 'PackageX' version >2.0 and 'Tool B' requires 'PackageX' version 1.0 to 1.6 you need both 'Tool A' and 'Tool B' in your project - what do you do?
If you are using these tools at different steps of your analysis it may be possible, indeed desirable, to separate out those steps using a pipeline/workflow management tool where each step is run in its own environment with only the dependencies that it needs.
Sometimes though your are just stuck with this problem and have no good solutions.
Dependency resolution is generally understood to be an NP hard problem without guaranteed solutions, so searching your dependency tree for a reconcilable set of package versions can take a very long time and may not return a valid result.
Functional package management side-steps this issue by having explicit for dependencies of each package, internally uniquely naming package versions and independently linking the dependencies of each package.
This way each tool could make reference to a different version of the same dependency and not have this result in a conflict in an environment containing both tools.

## Functional package management

Described by [Eelco dolstra in his 2006 PhD thesis 'The purely functional software deployment model'](https://api.semanticscholar.org/CorpusID:8511820) Nix and tools adopting many of the same underlying design principles like Guix adopt a 'functional' approach to package management.
Software packages in nix are called 'derivations'.
Ideally a derivation is a 'pure' or 'referentially transparent' function meaning that they have no 'side effects', change nothing outside the function when run and their output is completely determined by their inputs.
So in order to package a piece of software you have to give the derivation everything needed to build the software as an input and the build is performed in an isolated sandbox environment where it cannot access anything not explicitly included as an input to the build.
So for example when you provide the source code to a derivation from a remote repository you also provide a hash of that code which is recorded in the derivation so it is only valid if the exact same code is given to the derivation by the remote if you attempt to rebuild it.

This approach requires something of a higher up front investment as it requires you to be specific and exhaustive about what software you are using up front when packaging your code.
This has some excellent benefits in the long term.

The article [Building a Secure Software Supply Chain with GNU Guix](https://doi.org/10.22152/programming-journal.org/2023/7/1) goes over the uniquely robust trust architecture of this approach to software packaging.
I will note that Thomas Depierre observed in his 2022 blog post [I am not a supplier](https://web.archive.org/web/2/https://www.softwaremaxims.com/blog/not-a-supplier) that conceiving of open source software as a part of the 'software supply chain' misses the crucial point that open source maintainers are not generally treated like supplies of other goods and derives would be in a supply chain and should be if you want to treat their output as a part of your supply chain.
The technical robustness of your system is great for reducing the number of parties who you need to trust or the number of places untrusted parties could target but ultimately the trustworthiness of the software comes back to its maintainers and developers.
If a project you depended is maintained by one person who gets burnt out and stops doing security updates it does not matter that you have a technically robust trust architecture.

## Firmware

Firmware is software that runs on embedded devices and components such as microcontrollers.
You might build a firmware 'image' on your computer and 'flash' it to a device, setting the state of some persistent memory in the device that controls how it behaves.
When on components in a computer firmware code defines logic that sits outside your operating system, stored directly in pieces of hardware and not on the computers main storage devices.
Firmware is often 'spoken to' via 'drivers' in your computer's operating system which provide other software with an interface to use the capabilities of the device.

Firmware is a piece of our computational environments that is often forgotten but is of increasing importance as more computation is performed by dedicated hardware accelerators, this is especially true for machine learning computations.
We are seeing the sophistication of the software installed at a low level on our hardware devices increase as these devices become more capable.
Many PC components from SSDs to GPUs are now essentially entire small von neumann architecture computers in their own right.
Functionality which might previous have lived in operating system drivers is moving on device and is accessed by the driver through relatively high level interfaces.
As our hardware does more, how and what it does matters more for reproducible and trustworthy computation.
Unfortunately the firmware of GPUs and CPUs is almost universally closed and proprietary, making it unverifiable in the sense defined above.
With the advent of more powerful RISC-V CPUs, these being somewhat more open than X84 and Arm we may see improvements in openness at this level.
RISC-V is presently still primarily used in low power applications and is not yet available chips capable of competitive desktop computation.
There is also no guarantee of openness in all regards, proprietary extensions to the instruction set are permitted.
This is a significant problem for the independent verifiability of the trustworthiness of computation as many of the same arguments advanced by Ken Thompson in [Reflections on trusing trust](https://doi.org/10.1145/1283920.1283940) about compiler based attacks apply to the potential for firmware to be used as an attack vector.
Supply chain attacks targeting for example hardware accelerated cryptographic functions like random number generation have significant security implications, so the inability to independently build and flash firmware from open and auditable sources to such devices should be a source of considerable concern.

