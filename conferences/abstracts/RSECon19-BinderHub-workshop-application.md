# Research Software Engineering Conference 2019

* Conference website: https://rse.ac.uk/conf2019/
* Application form: https://docs.google.com/forms/d/e/1FAIpQLScVml19n44QfuOfjuaRlJUtXNMih-X4xUrNjlr8XJVHeyTyQg/viewform
* Location: University of Birmingham
* Date: 17th - 19th September 2019

### Workshop Length

180 mins (to allow time for Kubernetes cluster deployment and an introduction to reproducible research and BinderHub).

### Title

"Build a BinderHub for hosting Reproducible Software in the Cloud"

### Authors

* [Sarah Gibson](https://www.turing.ac.uk/people/researchers/sarah-gibson), ([The Alan Turing Institute](https://www.turing.ac.uk/)) on behalf of **[The Turing Way](https://github.com/alan-turing-institute/the-turing-way) Collaboration**.

### Abstract

_(1250 characters max, current count: 1244 [please update if you edit])_

BinderHub is a Cloud-based, multi-user server technology that captures the computing environment of a GitHub repository within a Docker image.
It then provides an interactive browser from which code can be run in the environment under which it was developed without placing installation responsibilities on the user.
A unique URL to this browser is generated making the software easily sharable with collaborators.
BinderHubs can be built anywhere in the world and are Cloud-neutral.
Building a locally hosted BinderHub is advantageous as it would facilitate the use of private repositories and make available a greater variety of computing resources - facilities which are not currently available on the public Binder service.

By harnessing the power of Cloud computing and building a BinderHub with expanded capabilities, scientific analyses can become more accessible and transparent to the wider community.
BinderHubs can showcase the reproducibility of software as well as being a valuable teaching or demonstration tool.

In this workshop, attendees will learn how to deploy a BinderHub on Microsoft Azure and connect with others who have or are interested in doing so.
Attendees should be familiar with Azure Cloud computing and the command line.

### Audience

_Would your target audience be required to have any prerequisite skills/background knowledge e.g. knowledge of a particular language?_

This workshop is most suitable for participants who are interested in maintaining a service to support researchers, for example at their institute.
They do not need to have access to organisational Cloud computing resources to join the workshop.
Attendees must be comfortable working on the command line.
A familiarity with Microsoft Azure will make participating in the workshop a little easier, but it is not a prerequisite.

### Outcomes

_How will your attendees benefit from your session? What do you expect them to gain/learn?_

_(600 characters max, current count: 524 [please update if you edit])_

Attendees to this workshop will learn how to deploy a BinderHub on Microsoft Azure Cloud platform.
They will learn the multiple applications of a BinderHub as a teaching or demonstration tool; the technology powering a BinderHub; and why reproducibility is important in research.
Attendees will be provided with enough knowledge to make an informed decision on whether building their own BinderHub is advantageous to their goals and connect with other RSEs/researchers who have built a BinderHub or are interested in doing so.

### Accessibility

_How will you ensure that your content will be accessible to the diverse audience of the conference?_

### Promotion

_How will you attract a broad and diverse audience for your session?_

I am a member of the Alan Turing Institute research engineering team, I am an Operator (maintainer) for the Binder community, and a core team member of the Turing Way research team.
I will leverage my network in advance of the conference to make sure that participants know  what to expect when they arrive at the event and that I have successfully run a similar workshop before.
I especially hope that by giving this workshop, I encourage more women, members of the LBGTQ+ and non-binary communities to engage with Cloud computing projects and open source communities.

### Mentorship

_Optional section._

_Would you like a mentor? If so then what would you like the mentor to do?_

Yes.
I would like a mentor with some Cloud computing experience to help troubleshoot problems on Azure should they arise.
It can be quite difficult to give one-on-one support whilst also live demo-ing to the rest of the room and so a mentor would be appreciated.

### Resources and accessibility needs

_Optional section._

_What technological requirements do you have for your session? Do you have any accessibility needs that we should consider when planning when and where to include your contribution?_

Attendees will require:
* a "Free Trial" subscription to Azure;
* a valid DockerHub account.

If they are able to install software before the event, that would be preferred:
* Azure CLI - https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest
* Kubernetes CLI (`kubectl`) - https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos
* Helm (Kubernetes package manager) - https://helm.sh/docs/using_helm/#installing-helm

### Will you be applying for a travel bursary?

No.

### Licence

_All materials uploaded and generated for your session will be published on the conference app and website will be shared under a CCBY license._
_This is a requirement for all presenters._
_Do you agree to this?_

Yes.
