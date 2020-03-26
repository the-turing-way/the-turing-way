# Sharing and archiving data

## Motivations for sharing data

The world is witnessing a significant global transformation, facilitated by technology and digital media, and fuelled by data and information.
This transformation has enormous potential to foster more transparent, accountable, efficient, responsive, and effective research. Only a very small proportion of the original data is published in conventional scientific journals.
Existing policies on data archiving notwithstanding, in today’s practice data are primarily stored in private files, not in secure institutional repositories, and effectively are lost to the public.
This lack of access to scientific data should be removed for several reasons:

1. To create possibility to fully reproduce a scientific study by providing the original data.
2. To prevent duplicate efforts and speeds up the scientific progress by sharing data.
Large amounts of research funds and careers of researchers can be wasted by only sharing a small part of research in the form of publications.
3. It facilitates collaboration and increases the impact and quality of scientific research.
4. Research is often publicly-funded, so the results of this research should be openly available as a public good.

Accordingly, there is an ongoing global data revolution that seeks to advance collaboration and the creation and expansion of effective, efficient research programs. Sharing data openly is crucial to meeting these objectives.
Open data means that the data is freely available on the internet permitting any user to download, copy, analyse, re-process, and re-use it for any other purpose without financial, legal, or technical barriers other than those inseparable from gaining access to the internet itself.
This represents a real shift in how research works.
At the moment anyone who wishes to use scientific data from a researcher often has to contact that researcher and make a request.
Open by default turns this on its head and says that there should be a presumption of publication for all.
Researchers need to justify data that’s kept closed, for example for security or data protection reasons.
Free access to, and subsequent use of, data is of significant value to society and the economy, and that data should, therefore, be open by default.
Research is often publicly-funded, so the results of this research should be openly available as a public good.

## Steps to share your data

### Step 1: Select what data you want to share

Not all data can be made openly available, due to ethical and commercial concerns, and you may decide that some of your intermediate data is too large to share.
So you first need to decide which data you need to share for others to be able to reproduce your research.

### Step 2: Choose a data repository or other sharing platform

Data should be shared in a formal, open, and indexed data repository where possible so that it will be accessible in the long-run.
Suitable data repositories by subject, content type or location can be found at [Re3data.org](https://www.re3data.org/) and in [FAIRsharing](https://fairsharing.org/databases) where you can also see which standards (metadata and identifier) the repositories implement and which journal/publisher recommend them.
If possible use a repository which assigns a DOI, a digital object identifier, to make it easier for others to cite your data.

### Step 3: Upload your data and documentation

In line with the FAIR principles outlined above upload the data in open formats as much as possible and include sufficient documentation and metadata that someone else can understand your data.

### Step 4: Choose a licence and link to your paper and code

So that others know what they can do with your data you need to apply a licence to your data.
The most commonly used licences are [Creative Commons](https://creativecommons.org/choose/), [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), or an [Open Data Commons Attribution License](https://opendatacommons.org/licenses/by/index.html).
To get maximum value from data sharing make sure that your paper and code both link to your data, and vice versa, to allow others to best understand your project.

## Barriers to data sharing

Some academics still find sharing data difficult.

Recent surveys {% cite Stuart2018sharing %} amongst researchers find that sharing data is challenging for the following reasons:

- Organising data in a presentable and useful way (mentioned by 46%)
- Unsure about copyright and licensing as mentioned by 37%
- Not knowing which repository to use as raised by 33%

These are cultural challenges that might be addressed in changing practice going forward.

However, there are also legal, ethical or contractual reasons that sometimes prevent making data publicly available in its entirety or even in parts.
Those will be addressed in the following paragraphs.

## Privacy and data protection

Many fields of scientific disciplines involve working with sensitive personal data.
Their management is well regulated in data protection legislation (in Europe through national implementations of the General Data Protection Regulation) and ethics procedures as they are established in most research institutions {% cite EU2016protection %}.

## Consent

In order to make sure that anonymised research data can be made available for future reuse, it is important that consent forms cover sharing anonymised data with other researchers.
Research so far suggests that study participants are usually less concerned about the data being archived and shared than researchers think {% cite Kuula2010archiving %}.
Participant information sheets and consent forms should include how research data will be stored, preserved and used in the long-term, and how confidentiality will be protected when needed.

## Anonymisation

Individuals must be protected from (re)identification via their personal data used for research.
Anonymisation of the data may be sufficient in some cases, but ensuring that re-identification is not possible is becoming increasingly difficult and might be impossible due to technical progress, growing computational power and – ironically – more open data.

For example re-identification may be possible via data-mining of accessible data and so-called quasi-identifiers, a set of (common) properties that are – in their combination – so specific that they can be used to identify.
Preserving privacy may still be possible if partial or generalised datasets are provided like age groups instead of birth date or only the first two digits of postal codes.
It may also be possible to provide the data in such a format that researchers can query it whist keeping the data itself closed, for example, a user may be able to send a query to retrieve the mean of a dataset, but not be able to access any of the individual data points.
Another way to provide anonymised data is to provide [synthetic data](https://en.wikipedia.org/wiki/Synthetic_data), data generated to reflect the conditions and properties of the raw data without including any of the personal information.

## National and commercially sensitive data

In many cases companies are understandably unwilling to publish much of their data.
The reasoning goes that if commercially sensitive information of a company is disclosed, it will damage the company’s commercial interests and undermine competitiveness.
This is based on the thinking that in competitive markets, innovation will only occur with some protection of information: if a company spends time and money developing something new, the details of which are then made public, then its competitors can easily copy it without having to invest the same resources.
The result is that no-one would innovate in the first place.
Similarly governments are often unwilling to publish data that relates to issues such as national security due to public safety concerns.
In such cases it may not be possible to make data open, or it may only be only possible to share partial/obscured datasets as outlined in the section above on privacy.
