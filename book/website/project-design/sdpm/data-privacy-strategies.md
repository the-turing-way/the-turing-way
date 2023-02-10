(pd-sdpm-privacy)=
# Data Privacy Strategies

There are a number of strategies that you can adopt to **safeguard the privacy** of your research subjects:

**1. Data minimisation**

* If personal information isn't needed, don't collect it.
* Periodically review whether you are retaining unnecessary identifying information.
* When identifying information is no longer needed, safely remove, delete or destroy it.

**2. Data retention limits**
* Decide how long you will retain identifiable data before removing direct identifiers, applying more complex anonymisation techniques, or deleting the data altogether.
* When deleting sensitive data you need to be aware that standard methods for deleting files (for example moving files to the recycle bin and emptying it) are not secure.
These deleted files may be recovered. 
Use **software** like BleachBit (Linux, Windows), BC Wipe, DeleteOnClick and Eraser (Windows) or Permanent Eraser or 'secure empty trash' (Mac) to safely delete the data.
An alternative is the **physical destruction** of the storage media.
**Degaussing** disturbs the magnetic alignment of magnetic storage media (such as hard drives and tapes) and may render those unusable. 
If you encrypted the data (see point 4 below), you can also **delete the encryption key**.

**3. Secure data transfer**
* Before deciding to transfer personal data, you should consider whether the transfer of identifiable data is necessary.
For example, can data be de-identified or anonymised? 
* If data cannot be made unidentifiable then you must ensure you have authority to transfer the personal data, and that there are appropriate safeguards in place to protect the data before, during and after transit.
* Keeping data in one place is safer than transfering it elsewhere. 
Consider whether it is possible to provide access to the data, instead of transferring them outside of your institution.
* Often your university or institute will provide solutions for secure file transfer. 
Contact you research data, privacy or IT support team for guidance. 

**4. Encryption** 
* Encryption provides protection by ensuring that only someone with the relevant encryption key (or password) will be able to access the contents.
    * Protect on disk level: Bitlocker for Windows, FileVault for MacOS
    * Protect on “container” level (a folder containing multiple files):  Veracrypt (or Archive for MacOS)
    * Portable storage: Bitlocker
    * File level / Exchange information:
      * Simple method: use 7zip, and pack with a password
      * More complicated to setup: use PGP tooling (can also be used to securely send email)
    * See the [Ghent University Encryption for Researchers manual](https://osf.io/nx8km/) for more details and step-by-step guides

**5. Access permissions**
* Control who has access to which parts of the data, and which type of permissions they have, such as "read" vs. "write" access.
* Deny access to sensitive data if that access is no longer needed.
* Password protection.


**6. Anonymisation**

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
* For more information about anonymisation 
   * Watch [this webinar by Enrico Glerean](https://www.youtube.com/watch?v=ILXeA4fx3cI) 
   * Watch a presentation on [Amnesia – Data Anonymisation Made Easy](https://www.youtube.com/watch?v=9wu_xGeYsQw) or a webinar on [Amnesia - a tool to make anonymisation easy](https://www.youtube.com/watch?v=9wu_xGeYsQw)
   * Or read an [explanation by the Finnish social science data archive](https://www.fsd.tuni.fi/en/services/data-management-guidelines/anonymisation-and-identifiers/)
   * [Anonymisation step-by-step](https://ukdataservice.ac.uk/learning-hub/research-data-management/anonymisation/anonymisation-step-by-step/)




