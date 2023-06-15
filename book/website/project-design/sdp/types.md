(pd-sd-types)=
# Types of Sensitive Data - overview

Sensitive data is information that must be protected against unauthorised access.
This could be data that personally identifies someone, information that we would not want to openly share with others, or data that might bring harm to other people or organisms.
Protection of this data may therefore be required for legal or ethical reasons.

When measuring how sensitive a data is, different organizations may follow (or be required to follow) certain structure in identifying different levels of sensitive data and information, based on frameworks. 
In general, the sensitivity levels are broadly classified into three categories:
* **High sensitivity / highly restricted data** - could include details like sensitive personal data, salary information, bank details, research data with significant commercial value or obligations. 
If this kind of data is compromised or destroyed in an unauthorized way, it could greatly impact the organizations/individuals involved and they could face repercussions. 
Unauthorized disclosure may result in fines, legal action, reputational damage, economic losses, and other consequences.
* **Medium sensitivity / restricted data** - could include details like personal data that is not classified as 'sensitive', student/alumni contact details, staff contact details. 
This kind of data is usually for internal usages only, and if compromised or destroyed in an unauthorized way, would not be as impactful as high sensitivity data on the organizations/individuals involved.
* **Low sensitivity / internal data** - could include details like non-confidential internal correspondence, working group minutes, internal policies and procedures. 
This kind of data could also comprise of data intended for public use, like public website contents or press releases.

According to the information guidelines provided by [Imperva](https://www.imperva.com/learn/data-security/data-classification/), data could be classified based on content, context or user-based. 
* **Content-based classification** -  involves inspecting and interpreting files and documents looking for sensitive information while reviewing them, and classifying based on that.
* **Context-based classification** -  involves looking into the metadata to classify, such as the application which created the file, person/people involved in its creation, or the location of its authorization. 
Some questions one can ask while looking for this classification are:
  * How is the data being used? 
  * Who has the access to it? 
  * When are they accessing it? 
* **User-based classification** -  involves the expertise of judgement made by one or more knowledgeable users in classifying the file or document. 
Hence, they would be advising on specifying how sensitive the data is and make necessary changes or edits before they release it.

In terms of research the most common reasons data falls under the high sensitivity data are:
* Research data containing personal identifying information, 'personal data' and special categories data as defined in UK and European data protection legislation. 
Such as involvement of human participants, particularly where the research involves sensitive personal data such as health records
* Involvement of commercial collaborators, particularly where the data could be construed as competitive intelligence
* Data relating to species of plants or animals where the release of data may adversely affect rare or endangered species
* Data likely to harm an individual or community or have a significant negative public impact if released
* Working under the terms of a non-disclosure agreement

Organizations usually share guidances and links on storing sensitive data, controlling access to sensitive data, encrypting sensitive data, anonymising sensitive data, transferring sensitive data, and disposing of sensitive data. 
Adhering to the safety protocols are highly essential for ensuring data safety and security. You can learn more about this in the section on {ref}`Data Privacy Strategy<pd-sdpm-privacy>`.

Reproducible research is often thought to require open data or open workflows, but it is possible to work reproducibly within sensitive data projects to demonstrate research quality and create a transparent research record to enable reproducibility.
There are a number of ways to do this that still fulfill the legal and ethical requirements of working with sensitive data such as using advanced version control tools within private repositories or data safe havens throughout the project, and considering carefully how the project can be published to protect the privacy needs of the data but demonstrate research quality.
These are versions of inner source working in which open collaboration and open communication practices are used to form and record the research lifecycle creating a transparent record.
Therefore each research project needs to find the best solution for their needs.

The following sub-chapters give an overview of the types of sensitive data and metadata that need to be identified in datasets and therefore handled securely in research projects.

Here is a short video introducing sensitive data by ELIXIR-UK.

<div class="video-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/2PXFu33IGVU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
