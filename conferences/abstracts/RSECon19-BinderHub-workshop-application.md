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

_(1250 characters max, current count: -- [please update if you edit])_

#### Below is stolen (and edited) from my Cloud WG abstract, I quite like it!

Binder (http://conference.scipy.org/proceedings/scipy2018/pdfs/project_jupyter.pdf)[1]/ BinderHub (https://binderhub.readthedocs.io/en/latest/index.html) is a Cloud-based, multi-user server technology that captures the computing environment of a GitHub repository within a Docker image.
It then provides an interactive browser from which code can be run in the environment under which it was developed without placing installation responsibilities on the user.
A unique URL to this browser is generated making the software easily sharable with collaborators.
BinderHubs can be built anywhere in the world and are Cloud-neutral.
Building a locally hosted BinderHub is advantageous as it would facilitate the use of private repositories and make available a greater variety of computing resources - facilities which are not currently available on the public Binder service.

By harnessing the power of Cloud computing and building a BinderHub with expanded capabilities, scientific analyses can become more accessible and transparent to the wider community.
We can improve reproducibility by making it easy to showcase and re-run analyses, improve reliability by making it easy to review analyses and catch bugs early in the development process without installation, and improve the reusability of the code by capturing the computing environment.

[1] Project Jupyter, et al. (2018). Binder 2.0 - Reproducible, interactive, sharable environments for science at scale. In Proceedings of the 17th Python in Science Conference. SciPy. https://doi.org/10.25080/majora-4af1f417-011

_(1574 characters)_

#### Original attempt, feel meh about it.

A BinderHub (https://binderhub.readthedocs.io/en/latest/index.html) is a Cloud-based, multi-user server technology that hosts a code repository of Jupyter Notebooks as an interactive browser and generates a unique URL that is easily sharable.
It works by building a Docker image containing the software with all of it's dependencies installed.
This is then hosted in the Cloud and connected to the user's browser so they can run and interact with the code.
Building your own BinderHub to host within your own institute/organisation/RSE group is beneficiary as it can be customised to the needs of your specific team.
A privately hosted BinderHub can give the team the choice to host private repos and when these are publicly shared while working reproducibly.
Further customisations can be made, such as: authentication, altering the user-allocated computational resources, persistent storage for users, etc.

_(908 characters)_

### Audience

_Would your target audience be required to have any prerequisite skills/background knowledge e.g. knowledge of a particular language?_

Attendees would preferably be familiar with Microsoft Azure and the command line.

### Outcomes

_How will your attendees benefit from your session? What do you expect them to gain/learn?_

_(600 characters max, current count: 340 [please update if you edit])_

Attendees to this workshop will learn how to deploy a BinderHub on Microsoft Azure Cloud platform.
They will learn the purpose of a BinderHub, how one works and why reproducibility is important in research.
They will gain enough knowledge in the area to make an informed decision on whether building their own BinderHub is a viable option.

### Accessibility

_How will you ensure that your content will be accessible to the diverse audience of the conference?_

### Promotion

_How will you attract a broad and diverse audience for your session?_

### Mentorship

_Optional section._

_Would you like a mentor? If so then what would you like the mentor to do?_

No?

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
