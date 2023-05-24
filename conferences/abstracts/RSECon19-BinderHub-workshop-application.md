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

* [Sarah Gibson](https://www.turing.ac.uk/people/researchers/sarah-gibson) ([The Alan Turing Institute](https://www.turing.ac.uk/)) on behalf of **[The Turing Way](https://github.com/alan-turing-institute/the-turing-way) Collaboration**.
* Anna Krystalli (The University of Sheffield) on behalf of **[The Turing Way](https://github.com/alan-turing-institute/the-turing-way) Collaboration**.
* Patricia Herterich (The University of Birmingham) on behalf of **[The Turing Way](https://github.com/alan-turing-institute/the-turing-way) Collaboration**.

### Abstract

_(1250 characters max, current count: 1213 [please update if you edit])_

BinderHub is a Cloud-based, multi-user server technology that captures the computing environment of a Git repository within a Docker image.
It then provides an interactive browser from which code can be run in the environment under which it was developed without placing installation responsibilities on the user.
A unique URL to this browser is generated making the software easily sharable with collaborators.
BinderHubs can be built anywhere in the world and are Cloud-neutral.
Building an in-house BinderHub is advantageous as it would facilitate the use of private repositories and make available a greater variety of computing resources - facilities which are not currently available on the public Binder service.

By harnessing the power of Cloud computing and building a BinderHub with expanded capabilities, scientific analyses can become more accessible and transparent to the wider community.
BinderHubs can showcase the reproducibility of software as well as being a valuable teaching or demonstration tool.

In this workshop, attendees will learn how to deploy a BinderHub on Microsoft Azure and connect with others who have or are interested in doing so.
Attendees should be comfortable with the command line.

### Audience

_Would your target audience be required to have any prerequisite skills/background knowledge e.g. knowledge of a particular language?_

This workshop is most suitable for participants who are interested in maintaining a service to support researchers, for example at their institute.
They do not need to have access to organisational Cloud computing resources to join the workshop.
Attendees must be comfortable working on the command line.
A familiarity with Microsoft Azure will make participating in the workshop a little easier, but it is not a prerequisite.

### Outcomes

_How will your attendees benefit from your session? What do you expect them to gain/learn?_

_(600 characters max, current count: 525 [please update if you edit])_

Attendees to this workshop will learn how to deploy a BinderHub on Microsoft Azure Cloud platform.
They will learn the multiple applications of a BinderHub as a teaching or demonstration tool; the technology powering a BinderHub; and why reproducibility is important in research.
Attendees will be provided with enough knowledge to make an informed decision on whether operating their own BinderHub is advantageous to their goals and connect with other RSEs/researchers who have built a BinderHub or are interested in doing so.

### Accessibility

_How will you ensure that your content will be accessible to the diverse audience of the conference?_

I will make clear at the beginning of the workshop that all participants are required to comply with the RSE19 code of conduct at all time.
I will make sure that I know the reporting and enforcement details so that I can effectively support any member of the community in the event that they feel unsafe during my session.

The BinderHub workshop doesn't require much prerequisite knowledge or expertise and is set out in such a way that participants of any level can follow along.
It is run using the Software Carpentry "traffic light" post-it system so that as few attendees as possible are left behind and assistance can be asked for without the pressure of "raising your hand".
Time for answering questions and hosting discussions are naturally built into the workshop and it is also written in a Markdown file so is compatible with screen readers.
https://bit.ly/zero-to-binderhub-workshop

The BinderHub workshop has already been successfully run in Sheffield, feedback here: https://github.com/alan-turing-institute/the-turing-way/blob/main/workshops/build-a-binderhub/BinderHub%20workshop.csv

### Promotion

_How will you attract a broad and diverse audience for your session?_

I am a member of the Alan Turing Institute research engineering team, I am an Operator (maintainer) for the Binder community, and a core team member of the Turing Way research team.
I will leverage my network in advance of the conference to make sure that participants know  what to expect when they arrive at the event and that I have successfully run a similar workshop before.
I especially hope that by giving this workshop, I encourage more women, members of the LGBTQ+ and non-binary communities to engage with Cloud computing projects and open source communities.
_The Turing Way_ has a Code of Conduct (https://github.com/alan-turing-institute/the-turing-way/blob/main/CODE_OF_CONDUCT.md) and is passionate about building a diverse community, as evidenced by our book dash application (https://github.com/alan-turing-institute/the-turing-way/blob/main/workshops/book-dash/application-form.md).

### Mentorship

_Optional section._

_Would you like a mentor? If so then what would you like the mentor to do?_

Yes.
I would like a mentor with some Cloud computing experience to help troubleshoot problems on Azure should they arise.
It can be quite difficult to give one-on-one support whilst also live demo-ing to the rest of the room and so a mentor would be appreciated.
Anna Krystalli and Patricia Herterich are other core members of the Turing Way team who have volunteered to help with the session.

### Resources and accessibility needs

_Optional section._

_What technological requirements do you have for your session? Do you have any accessibility needs that we should consider when planning when and where to include your contribution?_

The workshop would need enough red and green post-its for each participant for the "traffic light" system.
(I can bring some, but a back up stash would be appreciated.)

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

### Please confirm that all presenters have completed a RSEConUK 2019 Presenter Details and Diversity Form

_You can find the form here: https://docs.google.com/forms/d/e/1FAIpQLSeuo3c5vrRgP_tn2tgmQUbA4bbT-9HScxaww86nVVBXQxNO8g/viewform_

Yes.

### Use of the details and diversity information

_I confirm that I permit the conference diversity panel to view the answers in the details and diversity form identified above and link those answers to my above submission if it is shortlisted, for the purposes of tracking and balancing the diversity of the overall conference._

Yes.

### Authority to use this information

_By submitting this form, you understand that the details you have provided will be stored by the RSEConUK 2019 Conference committee (https://rse.ac.uk/conf2019) in Google Forms for the purpose of processing, handling and retaining details of your submission to the conference._
_Data will be sent to other parties to facilitate the review of your submission and may be transferred outside the EU for purposes of review and storage in Google Forms._
_The data you provide here will be retained for up to 5 years to support statistical analysis and comparison with subsequent conferences._
_If you have any questions or wish to have your data removed prior to this, please e-mail details to rse2019@rse.ac.uk._
_Anonymised data may be retained indefinitely._

Yes.

### Copyright permission

_I understand that by submitting an this form, I am granting permission to disseminate the abstract, title and author names/affiliations electronically and to re-produce them in the conference programme, both online and in print._

Yes.

### Cloud resources

_I confirm that I will make available all notebooks, docker images, scripts and information related to virtual machines etc. as appropriate by the 9th August via GitHub, dockerhub etc. so that they can be set up on the Cloud Sponsor’s infrastructure for this workshop._
_If you have particular reasons why you cannot use the Cloud Sponsor’s infrastructure then please select "No", and the conference committee will get in touch to discuss your needs._

Yes.
