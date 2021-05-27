# Sharing Very Large Datasets

In the era of Big Data, research datasets can often be several hundreds of gigabytes, or even terabytes, in size. How do we share Very Large Datasets in ways that make it easy for both data contributors and data users?

## Where can I upload and share my Very Large Dataset?

 - For experimental neuroscience data: https://crcns.org/files/data/guide/crcns_instructions_for_contributing_data.pdf
 - More general-purpose: https://dataverse.org/
   - The Harvard Dataverse gives up to 1TB of storage for free: https://dataverse.harvard.edu/
 - Others??
 
## What kind of infrastructure can support the sharing of Very Large Datasets?

Currently, there are very few options for hosting and sharing Very Large Datasets online. It would be beneficial to have more infrastructures that can support Very Large Datasets, especially as research data becomes more multimedia and begins to use formats such as video and audio more widely. 

### What should this infrastructure do for researchers?

A Very Large Dataset sharing infrastructure should make it easy for contributors to upload data and to provide credit for the shared data. The infrastructure should also safeguard the data and check for compliance with a standard for ethical datasets (especially with datasets containing human data). Along the same lines, the data-sharing infrastructure should be clear on if and how the infrastructure provides back-ups to uploaded datasets. 

After a contributor has uploaded a dataset, the data-sharing infrastructure should relieve data contributors from providing technical support for individual users of the data, while also facilitating discussions/collaborations between data contributors and users. To enable easy and flexible online search and access, datasets should be indexed and tagged using descriptive language that creates clear categories. Users should also be able to easily create visualizations of the data, preferably using tools embedded directly in the infrastructure. 

As time passes and technologies advance and change, it will become important that these data-sharing infrastructures are expandable to include new formats, workflows, and genres of data. Given the current trends in dataset size, it will also be important for data-sharing infrastructures to be able to accommodate larger and larger datasets. 

Ideally, data-sharing infrastructures can help make open research practices more accessible by hosting a list of Frequently Asked Questions, or by providing teaching tools to help new contributors and new users figure out how to use the infrastructure. The FAQ and teaching tools can also bridge gaps between language and ways of thinking that arise between areas of expertise. Discussion forums can provide opportunities for user interactions and collaborations, nurturing an open research community. 

Lastly, a data-sharing infrastructure should have measures in place to prevent unfair or bad faith use of the data. 

 Refs for this section: 
 - https://gking.harvard.edu/files/gking/files/dvn.pdf
 - https://crcns.org/files/news/crcns-neuroinformatics-article.pdf

## How should researchers prepare their Very Large Datasets for sharing?

The following is a suggested check-list for meta-data to include when researchers are preparing to share a Very Large Dataset:
 - Description of the theoretical context and experimental paradigm
 - Description of experimental conditions, ideally a fully descriptive data collection protocol
   - date and time of data collection
   - researchers involved in data collection
   - species, age, sex, and so on, of experiment participants/subjects
   - housing conditions / home context of experiment participants/subjects
   - tools and techniques used to collect data (electrode type, video camera model, tissue staining technique, microphone type, and so on)
   - surgical procedures involved, if any
   - if stimuli were used, how were the stimuli generated?
   - how timings of stimuli, recordings, and any other events in the experiment were correlated and/or synchronized
 - Known caveats about the use of the data (for example: identified artifacts)
 - links to publications
 - tools and procedures used to save, archive, transport, process, analyse, and visualize the data (see section on Data Provenance)

## Data Provenance

The word "[provenance](https://en.wikipedia.org/wiki/Provenance)" refers to the chronology (or timeline) of origin, ownership, custody, or location of a historical object, originally used in relation to works of art. If someone has custody of an object, this means that that person is responsible for the keeping of object safe and in good condition. 

**Data provenance** refers to the chronology of origin, ownership, custody, location, and changes made to a dataset. This documentation would ideally involve the following milestones:
 - **"Raw" dataset**: this version of the dataset is what was actually collected during the experiment. Ideally the "raw" dataset can be verified to guarantee that it has not been changed or otherwise tampered with since the date/time of initial data collection. 
 - In some cases, the raw dataset will not be suitable for sharing online (for example: confidential info, videos/photos that can identify individuals, animal research procedures that the general public may find disturbing). In these cases, it would be ideal to include a "nearly raw" dataset that is as close to the "raw" dataset as possible while respecting confidentiality and diverse sensitivities towards invasive research. 
 - **Processed datasets**: these next versions of the dataset are filtered for ease of analysis, communication, or specific application. Each processed version of the dataset should describe the tools and procedures used to process the raw dataset and create the processed dataset. The description should be detailed enough to allow any user to recreate the processed datasets from the original raw or "nearly raw" dataset. 
