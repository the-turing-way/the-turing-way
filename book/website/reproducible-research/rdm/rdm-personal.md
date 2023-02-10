(rr-rdm-personal)=
# Personal data management

For a more practical overview on tools and practises that facilitate reproducibility, please see the [Sensitive Data chapters](https://the-turing-way.netlify.app/project-design/sdp.html) on [managing](https://the-turing-way.netlify.app/project-design/sdpm.html) and [working on](https://the-turing-way.netlify.app/project-design/sdpw.html) sensitive data under the [Guide for Project Design](https://the-turing-way.netlify.app/project-design/project-design.html#pd).

## Personal data

Personal data is information about **living people** who can be identified using the data that you are processing, either directly or indirectly (for example, a person's name, address or other unique identifier such as their Social Security number). 
Find out more about what personal data is and what policies apply to this type of data in the {ref}`personal data section<pd-sdp-personal>`.


(rr-rdm-informed-consent)=
## Informed consent

Informed, voluntary and fair consent to participate in a study is very important for any research project that involves human participants. You can find more information about this in the {ref}`Informed Consent section<pd-sdpm-informed>`.


(rr-rdm-privacy)=
## Safeguard privacy
There are a number of strategies that you can adopt to **safeguard the privacy** of your research subjects, which are described in detail in the {ref}`Data Privacy Strategies section<pd-sdpm-privacy>`. If you do plan to share or publish the data you should ensure that this can be done so safely: read the {ref}`Sharing Sensitive Data section<pd-sdpm-sharing>`

**1. Data minimisation**

* If personal information isn't needed, don't collect it.
* Periodically review whether you are retaining unnecessary identifying information.
* When identifying information is no longer needed, safely remove, delete or destroy it.

**2. Data retention limits**
* Decide how long you will retain identifiable data before removing direct identifiers, applying more complex anonymisation techniques, or deleting the data altogether.
* When deleting sensitive data you need to be aware that standard methods for deleting files (for example moving files to the recycle bin and emptying it) are not secure.
These deleted files may be recovered. 
Use software like BleachBit to safely delete the data.

**3. Secure data transfer**
* Before deciding to transfer personal data, you should consider whether the transfer of identifiable data is necessary.
For example, can data be de-identified or anonymised? 
* If data cannot be made unidentifiable then you must ensure you have authority to transfer the personal data, and that there are appropriate safeguards in place to protect the data before, during and after transit.
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
* Management of shared folder permissions.
* Password protection.


**6. Anonymisation**

Anonymisation is a process by which identifying information in a dataset is removed. 
It is used primarily to allow data to be shared or published without revealing the confidential information it contains, while limiting the loss of information.
* Where possible, direct identifiers (such as names, addresses, telephone numbers and account numbers) should be removed as soon as the identifying information is no longer needed. 
You can delete the data or replace it with pseudonyms. 
For qualitative data you should replace or generalise identifying characteristics when transcribing interviews.
* De-identified data that can be re-identified using a linkage file (for example, information linking data subjects to identifiable individuals) is known as pseudonymised data. 
NOTE: In this instance, the linkage file should be encrypted and stored securely and separately from the de-identified research data.
  * Identification of individuals in pseudonymised or de-identified data may still be possible using combinations of indirect identifiers (such as age, education, employment, geographic area and medical conditions). 
Further, data and outputs containing small cell counts may be potentially disclosive, particularly where samples are drawn from small populations or include cases with extreme values or relatively rare characteristics.
   * As such, when intending to share potentially identifiable data or the outputs generated from the data, you may need to consider more advanced anonymisation techniques such as statistical disclosure control (SDC, see [this handbook](https://securedatagroup.org/sdc-handbook/) for more information).
* For more information about anonymisation you can watch [this webinar by Enrico Glerean](https://www.youtube.com/watch?v=ILXeA4fx3cI), or a webinar on [Amnesia - a tool to make anonymisation easy](https://www.youtube.com/watch?v=9wu_xGeYsQw), or read an [explanation by the Finnish social science data archive](https://www.fsd.tuni.fi/en/services/data-management-guidelines/anonymisation-and-identifiers/).

**7. Sharing sensitive data**

If you plan to share or publish your data you must ensure that your data are appropriate and safe to share. 
For example, you should consider whether the data can be adequately anonymised, and whether anonymised data will remain useful (see also {ref}`Barriers to data sharing<rr-rdm-sharing>`Open Research Chapter).
After applying methods to de-identify and anonymise sensitive data, there may still be a risk of re-identification (see {cite}`Meyer2018personaldata`). 

## More resources 
Check out the resources listed in the {ref}`Resources<pd-sdpm-resources>` of the {ref}`Managing Sensitive Data Projects chapter<pd-sdpm>` 

