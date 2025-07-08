(ch-pathways-creating)=
# Creating Learning Pathways

In the Pathway landing page, we describe the motivation and background for developing the Pathway feature - a Python package implementation in the book.

This chapter describes the process of creating curated learning pathways designed to meet the specific needs and interests of particular user personas.
By making the curation process clear, we hope more community members will join in and curate specific pathways that will support the learning experiences of their colleagues and members within *The Turing Way*.

## Why Create a Pathway

Here are a few specific reasons why we encourage creating a pathway, providing specific user groups with a curated set of chapters:

* **Targeted Learning:** Carefully curated pathways provide a focused route through which users can navigate the large number of resources, such as open science, reproducible research, and collaborative practices, without being distracted or feeling overwhelmed.
* **Ensuring Practical Use:** Pathways are often built in collaboration with the target personas, ensuring relevance, shared agency and practical use of the curated resource by them.
* **Promoting Specific Themes:** Pathways can highlight particular themes or methodologies in data science that are of specific interest to a group.
* **Addressing Skill Needs:** By identifying the unique set of chapters for specific user groups (such as Research Software Engineers or Community Managers) or collecting different aspects of a broader topic (such as data management or software citation), we can directly address skills required for specific personas.
* **Onboarding New Members or Community Groups:** Well-defined pathways can serve as effective onboarding tools, guiding newcomers through essential concepts and practices relevant to their context.
* **Reducing Time Burden:** Individuals with time constraints may find it difficult to navigate through resources that are not immediately relevant. By providing specific collections, we can reduce the time and effort needed to identify desired chapters.

## How to Curate Chapters for Your Pathway

Collaboration with target user groups is essential for creating a successful pathway.
This can involve various community events, such as regular short-format [Collaboration Cafés](#ch-community-calls-collabcafe), intensive long-format [Book Dashes](#ch-bookdash), or custom workshops tailored to specific groups or topics.
Irrespective of the format, the core steps for curating pathways generally remain the same.

With this principle in mind, below we offer a step-by-step process for curating a specific pathway.
Note that these steps do not provide the event design or organisation of such meetings, which are extensively covered in our [](#cl).
Instead, we offer five overarching considerations, informed by our experiences curating pathways for practical application by diverse groups.

### 1. Engaging Your Community in the Needs Assessment Process

#### Facilitated Discussion

Begin by engaging your target user group in a dialogue to understand their needs.
This group should include not only potential learners but also experienced members responsible for developing data science skills within their community.
This combination helps to mitigate expert awareness bias and ensures that the perspectives of those who know what learners don't know are also considered.

In a facilitated discussion or brainstorming session, encourage participants to share the skills they believe their colleagues need.
At this initial stage, it's not necessary to review the book or identify existing chapters.

#### Encourage a Wide Range of Ideas

Promote participation from diverse members within the group, representing various teams and areas of expertise.
Incorporating small breakout discussions as part of a larger group event can foster a broader range of ideas.

This initial idea-gathering can also be done through surveys, ideally after an introductory session explaining the purpose and potential uses of learning pathways.
The primary goal is to involve the community in identifying their learning objectives, current skill levels, and the challenges they encounter in their work.

Even if enabling a synchronous meeting, allow additional time for participants to contribute to improving the notes asynchronously after the discussion.

#### Documenting Ideas

Ensure that all generated ideas are captured in a written format.
Shared notes, sticky notes, whiteboards, or even GitHub issues can be valuable tools at this stage.
Create a comprehensive list of all the data science skills, topics, and challenges that the community members identify as important.
Avoid dismissing any ideas at this point, even if they don't immediately seem to fit within typical data science skills.

### 2. Synthesise Notes and Map them to the Existing Chapters

Once you've gathered ideas from the community, whether through real-time discussions or other methods, the next step is to consolidate and cluster related topics.
Look for recurring themes and overarching skills that emerge from the collected input.

#### Explore Existing Content in *The Turing Way*

Now, map these identified topics and skills to the existing chapters and sections within *The Turing Way*. 
Determine which content directly addresses the community's needs or provides the necessary foundational understanding.

To do this, use the search feature within *The Turing Way* book to look up relevant keywords.
Additionally, you can search for any ongoing discussions on these topics by exploring the issues and Pull Requests on the book's GitHub repository.

#### Curate Chapters for Your Intended Pathway

Based on your mapping, you can begin compiling links to the chapters that directly address the needs identified in the initial steps.
At this stage, it is recommended to be selective.
A well-designed pathway focuses on the most relevant content for the target persona, avoiding extraneous information that could lead to cognitive overload. Aim for a maximum of around 15 chapters to maintain focus.

If you find that there are too many important ideas and topics to include concisely, revisit your user group and seek their feedback on prioritising the most crucial chapters.
If all the suggested chapters truly are essential, consider offering different entry points by organising the content into multiple, distinct pathways.

### 3. Integrate and Showcase Your Pathway

Follow the standard *The Turing Way* contribution guidelines to submit your pathway idea via a *The Turing Way* GitHub issue.
Within the issue, share any relevant resources and the list of curated chapters.
This allows original contributors and the broader community members to provide feedback.

In addition to this, draft a concise 1-2 sentence description outlining the target users for this pathway.

#### Updating the `profiles.yml` File

Once your pathway idea is ready for integration, add the proposed persona name and its details to the `profiles.yml` file.
This file is located in the `book/website` directory of *The Turing Way* GitHub repository.
You can find detailed technical instructions for this process in the Infrastructure chapter within the Community Handbook.

After updating the YAML file, create a Pull Request following the standard contribution guidelines for review and approval.

Once the pathway is reviewed and approved, and the Pull Request is merged, it will appear on the welcome page of the book and will also be listed under the 'Pathways' section before the Foreword.
Each pathway is displayed in its own dedicated page, providing a direct link to access and showcase the curated set of chapters.

### 4. Sharing and Maintaining Your Pathway

Curating chapters in a pathway is just one step towards increasing awareness of effective data science practices.
It is crucial to have plans in place to actively promote its use within your community.

Carefully consider strategies for ensuring access and adoption of these curated resources and the corresponding practices.
This might include sharing the pathway through community channels, facilitating discussion sessions, designing training workshops, and actively referencing the curated resources in other materials used by community members.

#### Maintenance and Review

While the underlying pathway infrastructure is maintained by the Infrastructure Working Group, the upkeep of specific pathways is the responsibility of the representatives and groups involved in their development.
Cultivate a culture of continuous improvement by encouraging community members to suggest updates and contribute new content to keep the pathway current and valuable.

It is highly recommended to periodically review the pathway to ensure its ongoing relevance and accuracy.
In dedicated community spaces, actively involve and support members in identifying areas for improvement, proposing new chapters, and updating outdated content based on the evolving needs of the community.

### 5. Identifying Gaps and Community Involvement

As you map the community's suggested topics and skills with the existing chapters in *The Turing Way*, you will likely identify gaps where specific guidance or dedicated chapters are currently missing.
This presents an excellent route for your community to further engage with and contribute to *The Turing Way*.

#### Create a List of Missing Content

Within the original GitHub issue or a new one, please compile a list of the topics and themes that your community has identified as important but are not yet documented within *The Turing Way*.
Keeping an issue or other shared resource allows community members to easily identify, review and add their own suggestions.

#### Encourage and Facilitate Community Contribution

This list of missing resources is itself a valuable tool for engaging your community members with _The Turing Way_.
It empowers them to transition from being readers or users to active contributors and sharers of their expertise.

Reach out to members who express interest in specific topics and support them in collaborating with others within *The Turing Way* community to develop new chapters or expand existing ones.

Those who wish to contribute can be connected with the relevant groups within *The Turing Way* community.
Community meetings and events, such as [Collaboration Cafés](#ch-community-calls-collabcafe), [Book Dashes](#ch-bookdash), and locally organised contribution sessions, can provide an effective way to boost your community's involvement in creating the resources they need.

In the next subchapters, we provide case studies and examples from different communities and groups that created context-specific personas.
