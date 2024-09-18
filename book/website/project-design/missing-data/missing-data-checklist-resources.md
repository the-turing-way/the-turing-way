(pd-missing-data-checklist-resources)=
# Checklist and Resources

## Checklist 
- Identify whether your dataset has missing data; use visualisation tools to help you {ref}`pd-missing-data-visualising-missingness` 
- Try to determine what type of missing data there is (MCAR/MAR/MNAR) as described in {ref}`pd-missing-data-structures`, and don't forget about {ref}`pd-missing-data-structured-missingness`
- Choose an appropriate missing data handling method; you can use {ref}`pd-missing-data-methods` as a starting point for ideas
- Apply the missing data handling method and then continue with your analyses! 

<!-- Below commented out as I am not sure it is necessary: 

## References by Sub-Chapter
{ref}`pd-missing-data`
.. bibliography::
   :filter: False

   Pederson2017missingdata
   Buuren2018imputation

- {cite:ps}`Pederson2017missingdata`
- {cite:ps}`Buuren2018imputation` 

{ref}`pd-missing-data-structures`
- {cite:ps}`Rubin1976missingdata`

{ref}`pd-missing-visualising-missingness`
- [missingno python package](https://github.com/ResidentMario/missingno)
- ggplot, visdat, and naniar
-  

{ref}`pd-missing-data-methods`
- {cite:ps}`Joel2022missingdatahandling
- {cite:ps}`Woods2024multipleimputation`
- {cite:ps}`Pigott2001missingdatamethods`
- {cite:ps}`vanBuuren2011mice`
- {cite:ps}`Azur2011mice`
- {cite:ps}`Wulff2017mice`
- {cite:ps}`White2011mice`

{ref}`pd-missing-data-structured-missingness`
- {cite:ps}`Mitra2023structuredmissingness`
- {cite:ps}`Jackson2023structuredmissingness`
--> 

## References

Coding segments of this chapter were in part created thanks to several online tutorials which were used as a reference: 
- [Visualizing Missing Data](https://www.kaggle.com/code/selahattinsanli/visualizing-missing-data/notebook): A python notebook exploring the use of the missingno library. 
- [Gallery of Missing Data Visualisations](https://cran.r-project.org/web/packages/naniar/vignettes/naniar-visualisation.html): A tutorial on missing data visualisation in R. 
- [Imputing Missing Data with R; MICE package](https://datascienceplus.com/imputing-missing-data-with-r-mice-package/) 
- [Intro to MICE: An Imputation Strategy](https://www.kaggle.com/code/shilongzhuang/intro-to-mice-an-imputation-strategy/notebook): A short notebook introducing implementing MICE in python. 
- Lastly, the scikit-learn documentation is incredibly helpful and detailed with regards to implementing missing data handling in python: 
  - [6.4. Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html)
  - [Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)
  
Other textbook and paper references used, that have not been previously directly cited: 
- On types of missing data {cite:ps}`Bland2015medicalstatistics,Mack2018patientregistries`
- On multiple imputation {cite:ps}`deGoeij2013multipleimputation,Austin2021multipleimputation`


(pd-missing-data-learn)=
## What to Learn Next

If you happen to be handling sensitive data in your project, check out the {ref}`pd-sdpw` chapter. 

Alternatively, if you want to make your research project and data analysis pipeline more reproducible, see the chapter on {ref}`rr-make`, a build automation tool.  


(pd-missing-data-reading)=
## Further Reading

- [Flexible Imputation of Missing Data](https://stefvanbuuren.name/fimd/): This is a much more in-depth look at missing data imputation that goes into further characterising data, including mathematical definitions, and describing data imputation methods. 
- [Getting Started with naniar](https://naniar.njtierney.com/articles/naniar.html#tidy-missing-data-the-shadow-matrix): More R functions to visualise Data Missingness, including one using decision trees to map out the proportion of missingness in a variable based on all other variables. 
- The papers cited throughout this chapter are all good resources for further reading. The original paper on MICE {cite:ps}`vanBuuren2011mice` and the review papers on missing data handling {cite:ps}`Pigott2001missingdatamethods, Joel2022missingdatahandling` are especially great resources.  
- For more R visualisation and imputation packages see:
   - [mi](https://cran.r-project.org/web/packages/mi/index.html)
   - [Amelia](https://cran.r-project.org/web/packages/Amelia/index.html)
   - [missforest](https://cran.r-project.org/web/packages/missForest/index.html)
- The Turing-Roche partnership has some resources on structured missingness:
   - See *#ExplainToMe: The Problem of Structured Missing Data* for a great animated overview
      <div class="video-container">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/nlevyS1GLlQ?si=4exk2HIvU1-5y004" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
   - Papers on structured missingness (that were cited previously): {cite:ps}`Mitra2023structuredmissingness` and {cite:ps}`Jackson2023structuredmissingness`
   - For more in-depth recordings from the Turing-Roche Knowledge Series see: 
     - *Modern Topics on Missing Data*, which also provides a brief overview of missing data:
         <div class="video-container">
         <iframe width="560" height="315" src="https://www.youtube.com/embed/Cbj3X5wBeEg?si=ILs6NMeNX1FPkqnW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
         </div>
     - *Structured Missingness Challenges in Data Integration*: 
         <div class="video-container">
         <iframe width="560" height="315" src="https://www.youtube.com/embed/lnLd7LLkmDY?si=OjFgZZhgqCBoNLA1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
         </div>

