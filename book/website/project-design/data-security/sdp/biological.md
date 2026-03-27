(pd-sdp-biological)=
# Biological data

(pd-sdp-biological-def)=
## Definition of biological data

Sensitive biological data comes from two specific areas: 
* Nature conservation and biodiversity data
* Biosafety (biosecurity) data

### Nature conservation and biodiversity data

Conservation and biodiversity data could be related to endangered species, protection regulations, international environmental agreements, time and location sensitive disturbances such as during breeding periods.

These organisms often appear on a sensitive species lists such as the [National Biodiversity Network Atlas sensitive species list for the UK](https://docs.nbnatlas.org/sensitive-species-list/) that has been approved by the UK’s statutory bodies and relevant experts. 
There could also be species identified on [Biodiversity Action Plans (BAP)](https://jncc.gov.uk/our-work/uk-bap-priority-species/) or red lists of endangered species. 
For example the [Butterfly Red list of Great Britain](https://butterfly-conservation.org/sites/default/files/red-list.pdf) or the International Union for Conservation of Nature’s Red List of Threatened Species [(IUCN Red list)](https://www.iucnredlist.org/).

Being on these lists does not necessarily mean that data about these species cannot be shared openly as some organisms may be less harmed if more information is shared about them. 
An individual risk assessment must be done in each case.

However, some examples of threats that could result from sharing biological data and therefore this data needing to be restricted are:
        
* **Collection for the pet trade and international wildlife market** - for example, nesting locations of rare birds that might lead to poaching of eggs or the collection of a new species such as fish from a coral reef.
        
* **Killing of organisms for recreational hunting, for food and for cultural, social or belief reasons** - for example, killing sharks to reduce human-shark interactions or for shark-fin soup. 
        
* **Threat of habitat destruction or disturbance by humans for recreational purposes, farming, housing or to stop conservation efforts** - for example, disturbance of habitats by bird watchers leading to a decline in breeding or destruction of forests for monoculture farming. 
        
### Biosafety

Certain organisms can pose a direct threat to humans, animals, and plants such as diseases or pests. 
This can also include newly developed organisms such as genetically-modified plants.
The whereabouts and the methods of development of these organisms may be considered sensitive.
At the same time, it must be considered that it may be important to share this data openly to prevent harm. 

Some biosafety data may fall under the confidential data category due to a need to protect the commercial interests of these developed organisms. 
However, this unnecessarily limits transparency and public peer review of these datasets, which are then submitted to regulatory authorities @Nielsen2013biosafety. 

(pd-sdp-biological-benefits)=
## Benefits of opening up sensitive biological data

There are clear benefits to making biological data freely available, including for not-for-profit decision making, education, research and other public benefit. 
Therefore data should only be restricted when harm to the environment, harm to people, or harm to sustainability is possible. 

Some types of biological data, particularly related to biodiversity, should not be shared openly. 
These data should be kept partially or completely private. 
However, attempts should be made to provide access to researchers or individuals who can prove a need for these data such as reuse for research purposes or to peer review research.
Researchers should conduct an assessment of the risks versus benefits of publishing biological data to decide whether (part of the) data can be shared. 

Each country will have specific legal restrictions for rare and endangered species, as well as biosafety regulations, that have to be taken into account for each dataset.

The majority of the biodiversity community feel there are more benefits publishing open datasets as its future reuse could lead to greater conservation opportunities, promote community engagement and reduce duplication of survey efforts @tulloch2018decision.

(pd-sdp-biological-opening)=
## Opening up sensitive biological data
The types of data that need to be considered sensitive include occurrence data surrounding the exact location of rare, endangered or commercially valuable organisms.

In order to protect sensitive biological data, several measures can be taken: 
- Exact locations for organisms can be generalised in different ways to minimise or take away the potential harm (see [Thorpe et al. 2026](https://doi.org/10.5281/zenodo.17588795)
  - Decreasing the precision or resolution of the coordinates, for example by 0.1 degree.
  - Using hexagons around the location (the Discrete Global Grid System) ([Caspari et al. 2024](https://doi.org/10.1038/s41597-024-03354-5))
  - Obscuring the location by adding a buffer around the point or polygon.
  - Replacing the coordinates by the name of an administrative unit.
- Different levels of access can be provided, by providing a general location to the public and more detailed information under restricted access only available to other researchers. 

Current best practice is discussed by [](https://doi.org/10.15468/doc-5jp4-5g10) [pdf](https://docs.gbif.org/sensitive-species-best-practices/master/en/current-best-practices-for-generalizing-sensitive-species-occurrence-data.en.pdf), who sets out 10 principles for generalising sensitive species occurrence data to enable data sharing.

(pd-sdp-biological-examples)=
## Examples of projects and issues with biological data

- [Cooke et al. 2017](https://10.1111/cobi.12895) on animal conservation and management
