(pd-sdpw-private-learning)=
# Privacy-Preserving Machine Learning

Much current research in data science involves machine learning (ML) models interacting with data sourced from many individuals with significant variation in the general level of awareness, consent, and understanding of research goals. 
As such, researchers have a responsibility to protect the confidentiality and privacy of the people whose data is being processed. 
At the same time, sharing both data and trained models drives scientific advancement and promotes important social goals in open and transparent science.

It's important to note that local and international regulations such as the [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) and the EU’s policy on [trustworthy AI](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence) also establish legal duties and principles on privacy protection that the following tools may help researchers meet.

## Sharing data with privacy

Training a complex ML model can often require a very large amount of data, more than a single researcher or organisation could feasibly generate. 
Sharing our data not only helps us to create more reproducible research but promotes advancements in the field as a whole. 
However, this does pose the risk of inadvertently sharing personal information that could be used to identify a subject.

Most researchers will remove uniquely identifying information (such as ID numbers, address, and phone numbers) before publication, but recent research has shown that with access to secondary datasets, such 'pseudonymized' datasets can still be traced back to the individual {cite:ps}`narayananRobustDeanonymizationLarge2008,sunIdentityAnonymizationHighdimensional2012`.

### Differential privacy

Differential privacy is a statistical tool which can estimate the risk of uniquely identifying a member of a dataset, whereupon calibrated noise can be added to ensure that privacy is preserved {cite:ps}`yangDifferentialPrivacyData2012`.

### Synthetic data generation

If sharing the original data raises privacy or ethical concerns, we can still contribute useful information by sharing synthetic datasets that reproduce statistical features of the original dataset without exposing actual instances {cite:ps}`torfiDifferentiallyPrivateSynthetic2020`. 

### Useful resources

- [Individual Risk Tool](https://cpg.doc.ic.ac.uk/individual-risk/) *A useful visualisation of how a few pieces of information can uniquely identify you*
- [The Algorithmic Foundations
of Differential Privacy](https://privacytools.seas.harvard.edu/files/privacytools/files/the_algorithmic_foundations_of_differential_privacy_0.pdf) *The foundational paper to the study of differential privacy.*
- [What is privacy-preserving synthetic data?](https://www.statice.ai/post/what-is-synthetic-data-introduction) *A straightforward introduction to the concept of synthetic data*

## Learning with privacy

Beyond sharing data with other researchers, we can also share our trained models, or make them available as a service: carrying out predictions on data provided by others without the need for them to invest time and resources in training their systems. 
However, this sharing can also carry risks for personal privacy. 
For instance, many ML solutions require users to send personal data to a central server to process, exposing them to the risk of interception or misuse. 
The model itself may learn sequences from the dataset that we don't wish to be retained, a process referred to as unintended memorization {ref:ps}`carliniSecretSharerEvaluating2019`. 
This could be particularly harmful when considering models dealing with large amounts of user-created text {cite:ps}`brownWhatDoesIt2022`.

### Federated learning

Federated Learning is a design paradigm in which the users' data never leaves their own devices, with the model itself being broken down into a set of computations that take place on the edge before updates are sent back to a central coordinator {cite:ps}`kairouzAdvancesOpenProblems2019`.

### Adversarial learning

We can also draw on the experience of research in cross-domain training to teach models to ignore undesirable data by directly controlling the training process {cite:ps}`Coavoux2018`. 
This can also be extended beyond private attributes to the elimination of unwanted biases {cite:ps}`zhangMitigatingUnwantedBiases2018`.

### Differential privacy

Differential privacy has also seen significant use as a technique for preserving privacy during model training, reducing the risk of the model learning individual data points too well by adding small amounts of statistical noise during training {cite:ps}`boulemtafesReviewPrivacypreservingTechniques2020,feyisetanPrivacyUtilitypreservingTextual2020`. 

## Case study: Data privacy in ML neuroimaging
### Why do we want to share neuroimages?
Neuroimaging is an emerging medical technique focusing on the collection and analysis of brain-related data. 
Typical sub-fields are EEG, MEG, MRI, fMRI and PET. 
Neuroimaging methods commonly result in one large, longitudinal data set per individual, making the method suitable for applying machine learning algorithms. 
At the same time, ML techniques can be costly and time-consuming (for example, the average scanning cost for 1-hour of fMRI analysis is estimated to be [between USD 1.600-8.400](https://www.itnonline.com/content/mri-costs), with scanning times for an fMRI experiment lasting between 1.5 and 3hrs.).
These efforts associated with the collection of neuroimaging data have led to the foundation of large neuroimaging consortia, intending to create data sets that go beyond sample sizes of N=20-30 of a typical single neuroimaging study. 
Often, such consortia focus on a specific disorder or mental or cognitive state.
As outlined in this chapter, sharing data is good, but can be particularly dangerous, especially in the case of neuroimaging. 

### What are issues related to sharing neuroimaging data?
Common neuroimaging sharing standards warrant the removal of sensitive information and metadata from neuroimages.
However, given the focus on the brain, MRI and fMRI data naturally consist of images of the head and skull. 
Given the power of recent image processing machine learning algorithms, it has already been demonstrated that anonymized neuroimaging data can be matched and thus identified from images on the internet, especially in the presence of additional information {cite:ps}`schwarzIdentification2019`. 
A second risk associated with neuroimaging data is that a brain scan is often indicated in a combination with a health or medical condition. 
This adds to the sensitivity of those data and makes a potential leak of information even more dangerous. 
In the most extreme case, un-anonymized leakage of such health-related information with the de-anonymized neuroimage could result in severe personal disadvantages (for example, reduced employability, insurance cover).
 
 ### What are possible solutions?
 This evidence that it is feasible to re-identify individuals based on the facial reconstruction from structural MRI data has led to the development of software packages that can “de-face” MR images {cite:ps}`bischoff‐GretheAtechnique2007` {cite:ps}`MilchenkoObscuring2013`. 
 Thus, for data sharing of structural MRI images, it is important to first remove or blur the surface-based features in the images. 
 While programs that remove the possibility of re-identify individuals based on their surface anatomy exist, they may reduce the image quality for downstream pre-processing algorithms {cite:ps}`SitterFacingprivacy2020`.

Lastly, also the education of participants is important. 
In a longitudinal study of child development, children were given some images of their brain (for example, one slice from the structural MRI) after the study had finished {cite:ps}`whitePediatric2018`. 
The authors learned later that some of those images were later uploaded to social media profiles {cite:ps}`whiteDatasharing2020`. 
Thus even following anonymisation standards and removal of facial features from an MRI scan may not completely ensure privacy.


### Useful resources

- [Privacy in Deep Learning: A Survey](https://cseweb.ucsd.edu/~fmireshg/survey_pvdl_2020.pdf) *A useful brief overview of some extant threats and mitigation strategies.*
- [Deep learning and differential privacy](https://github.com/frankmcsherry/blog/blob/fdc265de245a82beb38b9a4f28799ef12f556ac1/posts/2017-10-27.md) *Frank McSherry's thought-provoking blog about the privacy research landscape.*
- [Privacy Preserving Machine Learning: Maintaining confidentiality and preserving trust](https://www.microsoft.com/en-us/research/blog/privacy-preserving-machine-learning-maintaining-confidentiality-and-preserving-trust/) *A recent overview from Microsoft Research of privacy-preserving learning*
- [PySyft](https://github.com/OpenMined/PySyft) *A Federated Learning and privacy preservation library designed for compatibility with major machine learning frameworks PyTorch and TensorFlow*
