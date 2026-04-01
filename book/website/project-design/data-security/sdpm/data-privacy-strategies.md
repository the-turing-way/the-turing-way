(pd-sdpm-privacy)=
# Data Privacy Strategies

There are a number of strategies that you can adopt to **safeguard the privacy** of your research subjects:

(pd-sdpm-privacy-minimisation)=
## 1. Data minimisation
* If personal information isn't needed, don't collect it.
* Periodically review whether you are retaining unnecessary identifying information.
* When identifying information is no longer needed, safely remove, delete or destroy it.

(pd-sdpm-privacy-retention)=
## 2. Data retention limits
* Decide how long you will retain identifiable data before removing direct identifiers, applying more complex anonymisation techniques, or deleting the data altogether.
* When deleting sensitive data you need to be aware that standard methods for deleting files (for example moving files to the recycle bin and emptying it) are not secure.
These deleted files may be recovered. 
Use **software** like BleachBit (Linux, Windows), BC Wipe, DeleteOnClick and Eraser (Windows) or Permanent Eraser or 'secure empty trash' (Mac) to safely delete the data.
An alternative is the **physical destruction** of the storage media.
**Degaussing** disturbs the magnetic alignment of magnetic storage media (such as hard drives and tapes) and may render those unusable. 
If you [encrypted](#pd-sdpm-privacy-encryption) the data, you can also **delete the encryption key**.

(pd-sdpm-privacy-transfer)=
## 3. Secure data transfer
* Before deciding to transfer personal data, you should consider whether the transfer of identifiable data is necessary.
For example, can data be de-identified or anonymised? 
* If data cannot be made unidentifiable then you must ensure you have authority to transfer the personal data, and that there are appropriate safeguards in place to protect the data before, during and after transit.
* Keeping data in one place is safer than transferring it elsewhere. 
Consider whether it is possible to provide access to the data, instead of transferring them outside of your institution.
* Often your university or institute will provide solutions for secure file transfer. 
Contact your research data, privacy or IT support team for guidance.
* Trusted Research Environment (TRE) platforms can provide secure and transparent access to lsensitive data, such as the [Secure Data Environment](https://digital.nhs.uk/services/secure-data-environment-service) and [OpenSAFELY](https://www.opensafely.org/).

(pd-sdpm-privacy-encryption)=
## 4. Encryption
* Encryption provides protection by ensuring that only someone with the relevant encryption key (or password) will be able to access the contents.
    * Protect on disk level: Bitlocker for Windows, FileVault for MacOS
    * Protect on “container” level (a folder containing multiple files):  Veracrypt (or Archive for MacOS)
    * Portable storage: Bitlocker
    * File level / Exchange information:
      * Simple method: use 7zip, and pack with a password
      * More complicated to setup: use PGP tooling (can also be used to securely send email)
    * See the [Ghent University Encryption for Researchers manual](https://osf.io/nx8km/) for more details and step-by-step guides

(pd-sdpm-privacy-access)=
## 5. Access permissions
* Control who has access to which parts of the data, and which type of permissions they have, such as "read" vs. "write" access.
* Deny access to sensitive data if that access is no longer needed.
* Password protection.

(pd-sdpm-privacy-anonymisation)=
## 6. Anonymisation
Anonymisation is a process by which identifying information in a dataset is removed. 
It is used primarily to allow data to be shared or published without revealing the confidential information it contains.
* Where possible, direct identifiers (such as names, addresses, telephone numbers and account numbers) should be removed as soon as the identifying information is no longer needed. 
You can delete the data or replace it with pseudonyms. 
For qualitative data you should replace or generalise identifying characteristics when transcribing interviews.
* De-identified data that can be re-identified using a linkage file (for example, information linking data subjects to identifiable individuals) is known as pseudonymised data. 
NOTE: In this instance, the linkage file should be encrypted and stored securely and separately from the de-identified research data.
  * Identification of individuals in pseudonymised or de-identified data may still be possible using combinations of indirect identifiers (such as age, education, employment, geographic area and medical conditions). 
Further, data and outputs containing small cell counts may be potentially disclosive, particularly where samples are drawn from small populations or include cases with extreme values or relatively rare characteristics.
   * As such, when intending to share potentially identifiable data or the outputs generated from the data, you may need to consider more advanced anonymisation techniques such as statistical disclosure control (SDC, see [this handbook](https://securedatagroup.org/sdc-handbook/) for more information).

(pd-sdpm-privacy-anonymisation-information)=
### More anonymisation information  
* Watch [this webinar by Enrico Glerean](https://www.youtube.com/watch?v=JpMvdddunqI) 
* Watch a presentation on [Amnesia – Data Anonymisation Made Easy](https://www.youtube.com/watch?v=9wu_xGeYsQw) or a webinar on [Amnesia - a tool to make anonymisation easy](https://www.youtube.com/watch?v=9wu_xGeYsQw)
* Or read an [explanation by the Finnish social science data archive](https://www.fsd.tuni.fi/en/services/data-management-guidelines/anonymisation-and-identifiers/)
* [Anonymisation step-by-step](https://ukdataservice.ac.uk/learning-hub/research-data-management/anonymisation/anonymisation-step-by-step/)
*  McGill Data Anonymization Workshop Series: [Reducing Risk: An Introduction to Data Anonymization](https://www.youtube.com/watch?v=IAmxErXPvHU&list=PLfMfJihLOASUMZwKQ32OQkOfTEv20spmH&index=1) and [Ethically sharing qualitative data](https://www.youtube.com/watch?v=eSZzUD4EVMQ&list=PLfMfJihLOASUMZwKQ32OQkOfTEv20spmH&index=3)
*  [Anonymisation](https://ukdataservice.ac.uk/learning-hub/research-data-management/#anonymisation) by UK Data Services
*  [Anonymisation and open data: an introduction to managing the risk of re-identification](https://theodi.hacdn.io/media/documents/OPEN-RDP8-Anonymisation-and-open-data_-An-introduction-to-managing-the-risk-of_thVQCgw.pdf) by the Open Data institute (2019)
* Tools for anonimisation
   * [Amnesia](https://amnesia.openaire.eu/) (tabular data)
   * [ARX](https://arx.deidentifier.org/) (tabular data)
   * [Cornell Anonymization Toolkit](https://sourceforge.net/projects/anony-toolkit/) (tabular data)
   * [mri_deface](https://surfer.nmr.mgh.harvard.edu/fswiki/mri_deface) (MRI data)
   * [MITRE Identification Scrubber Toolkit (MIST)](http://mist-deid.sourceforge.net/) (free text medical records)
   * [Stanford Named Entity Recognizer (NER)](https://nlp.stanford.edu/software/CRF-NER.html) (for unstructured text)

## 7. Synthethic data
It is also possible to generate a synethic dataset that mimics a real dataset. 
A syntethic dataset preserves some of the aspects and characteristics of the real data, yet generates a different dataset which can safeguard the original senstive data.

### More synthethic data information
- Read more about [syntethic data on the Data Impact Blog](https://blog.ukdataservice.ac.uk/not-real-but-really-useful-synthetic-data-a-cost-benefit-analysis-of-its-practical-value/)
- A webinar on [The Practices of Sharing Synthetic Dataset](https://www.youtube.com/watch?v=0epApx2S5-o) or [Using agent-based models as a simulation tool to generate synthetic data](https://www.youtube.com/watch?v=wk9jd9u9mRY)
- Tools:
   - [synthcity](https://github.com/vanderschaarlab/synthcity): A library for generating and evaluating synthetic tabular data
   - [synthea](https://synthetichealth.github.io/synthea/)
   - [metasyn](https://github.com/sodascience/metasyn)
   - [Pointblank](https://posit.co/blog/building-realistic-fake-datasets-with-pointblank/) (Python library)

## More information
- [Data minimization and de-identification](https://www.rug.nl/digital-competence-centre/privacy-and-data-protection/data-protection/guide-on-data-minimization-and-de-identification-v0-2.pdf) by the University of Groningen


