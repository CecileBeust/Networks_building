## Complexes layer

### Files

* ```extract_proteins_complexes.R``` : R script to extract proteins involved in the same biological complexes (source : CORUM, hu.MAP)
* ```build_complex_ntw.py``` : Python script to pair proteins involved in the same complex as binary interactions inside a network file

### Usage

1. Run the ```extract_proteins_complexes.R``` script 
2. Run the ```build_complex_ntw.py``` script (uses the output of the previous script)

### References

- Madalina Giurgiu, Julian Reinhard, Barbara Brauner, Irmtraud Dunger-Kaltenbach, Gisela Fobo, Goar Frishman, Corinna Montrone, Andreas Ruepp, CORUM: the comprehensive resource of mammalian protein complexes—2019, Nucleic Acids Research, Volume 47, Issue D1, 08 January 2019, Pages D559–D563, https://doi.org/10.1093/nar/gky973
- Kevin Drew, John B. Wallingford, Edward M. Marcotte hu.MAP 2.0: integration of over 15,000 proteomic experiments builds a global compendium of human multiprotein assemblies Mol Syst Biol (2021)17:e10016https://doi.org/10.15252/msb.202010016 
- D Turei, A Valdeolivas, L Gul, N Palacio-Escat, M Klein, O Ivanova, M Olbei, A Gabor, F Theis, D Modos, T Korcsmaros and J Saez-Rodriguez (2021) Integrated intra- and intercellular signaling knowledge for multicellular omics analysis. Molecular Systems Biology 17: e9923; DOI: 10.15252/msb.20209923
