# Sharing Very Large Datasets

In the era of Big Data, research datasets can often be several hundreds of gigabytes, or even terabytes, in size. How do we share Very Large Datasets in ways that make it easy for both data contributors and data users?

## Where can I upload and share my Very Large Dataset?

 - For experimental neuroscience data: https://crcns.org/files/data/guide/crcns_instructions_for_contributing_data.pdf
 - More general-purpose: https://dataverse.org/
   - allows 1TB for free on Harvard Dataverse; other dataverses not sure. 
 - Others??
 
## What should an infrastructure for sharing Very Large Datasets provide?

 - should be easy for contributors to upload data to the infrastructure
 - should be easy to provide credit for sharing data
 - the infrastructure should safeguard the data and check for compliance with a standard for ethical datasets (especially with datasets containing human data)
 - the infrastructure should relieve data contributors from providing technical support for individual users of the data, while also facilitating discussions/collaborations between data contributors and users
 - the datasets should be indexed and tagged for easy and flexible online search and access
 - users should be able to easily create visualizations of the data, preferably using tools embedded directly in the infrastructure
 - infrastructure should be expandable to include novel formats, workflows, and genres of data
 - include an FAQ list and discussion forums
 - provide teaching tools to help new contributors and new users figure out how to use the infrastructure, and to bridge gaps between language and ways of thinking that arise between areas of expertise
 - create, track, and refine the vocabularies and categories used to describe data and metadata
 - prevent unfair or bad faith use of data

## Suggested Meta-data to include

 - Description of the theoretical context and experimental paradigm
 - Description of experimental conditions, ideally a fully descriptive data collection protocol
   - date and time of data collection
   - researchers involved in data collection
   - species, age, sex, etc of experiment participants/subjects
   - housing conditions / home context of experiment participants/subjects
   - tools and techniques used to collect data (electrode type, video camera model, tissue staining technique, microphone type, etc)
   - surgical procedures involved, if any
   - if stimuli were used, how were the stimuli generated?
   - how timings of stimuli, recordings, and any other events in the experiment were correlated and/or synchronized
 - Known caveats about the use of the data (i.e. identified artifacts)
 - links to publications
 - tools and procedures used to save, archive, transport, process, analyse, and visualize the data (see section on Data Provenance)

## Data Provenance

The word "[provenance](https://en.wikipedia.org/wiki/Provenance)" refers to the chronology (or timeline) of origin, ownership, custody, or location of a historical object, originally used in relation to works of art. If someone has custody of an object, this means that that person is responsible for the keeping of object safe and in good condition. 

**Data provenance** refers to the chronology of origin, ownership, custody, location, and changes made to a dataset. This documentation would ideally involve the following milestones:
 - **"Raw" dataset**: this version of the dataset is what was actually collected during the experiment. Ideally the "raw" dataset can be verified to guarantee that it has not been changed or otherwise tampered with since the date/time of initial data collection. 
 - In some cases, the raw dataset will not be suitable for sharing online (confidential info, videos/photos that can identify individuals, animal research procedures that the general public may find disturbing, etc). In these cases, it would be ideal to include a "nearly raw" dataset that is as close to the "raw" dataset as possible while respecting confidentiality and diverse sensitivities towards invasive research. 
 - **Processed datasets**: these next versions of the dataset are filtered for ease of analysis, communication, or specific application. Each processed version of the dataset should describe the tools and procedures used to process the raw dataset and create the processed dataset. The description should be detailed enough to allow any user to recreate the processed datasets from the original raw or "nearly raw" dataset. 
