(pd-missing-data-checklist-resources)=
# Checklist and Resources

## Checklist 
- Identify whether your dataset has missing data; use visualisation tools to help you {ref}`pd-missing-data-visualising-missingness` 
- Try to determine what type of missing data there is (MCAR/MAR/MNAR) as described in {ref}`pd-missing-data-structures`, and don't forget about {ref}`pd-missing-data-structured-missingness`
- Choose an appropriate missing data handling method; you can use {ref}`pd-missing-data-methods` as a starting point for ideas
- Apply the missing data handling method and then continue with your analyses! 

<!-- IMPORTANT!
https://cran.r-project.org/web/packages/naniar/vignettes/naniar-visualisation.html
-->

<!--
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

(pd-missing-data-learn)=
## What to Learn Next

If you happen to be handling sensitive data in your project, check out the {ref}`pd-sdpw` chapter. 

Alternatively, if you want to make your research project and data analysis pipeline more reproducible, see the chapter on {ref}`rr-make`, a build automation tool.  


(pd-missing-data-reading)=
## Further Reading

- [Flexible Imputation of Missing Data](https://stefvanbuuren.name/fimd/): This is a much more in-depth look at missing data imputation that goes into further characterising data, including mathematical definitions, and describing data imputation methods. 
- [Getting Started with naniar](https://naniar.njtierney.com/articles/naniar.html#tidy-missing-data-the-shadow-matrix): More R functions to visualise Data Missingness, including one using decision trees to map out the proportion of missingness in a variable based on all other variables. 
 - [The original paper on MICE]({cite:ps}`vanBuuren2011mice`) is a great resource. 
 - For more R visualisation and imputation packages see:
   - [mi](https://cran.r-project.org/web/packages/mi/index.html)
   - [Amelia](https://cran.r-project.org/web/packages/Amelia/index.html)
   - [missforest](https://cran.r-project.org/web/packages/missForest/index.html)

