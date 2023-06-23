## Protein-Protein Interaction (PPI) Network

### Files

* ```process_PPI.sh``` : bash script to build the PPI network
* ```map_ensembl.py``` : Python script allowing to map Ensembl identifiers to HUGO gene symbols
* ```map_uniprot.py```: Python script allowing to map Uniprot identifiers to HUGO gene symbols
* ```ID_mapping_HUGO_11_01_23.txt``` : Mapping file downloaded from the HGNC custom download page (https://www.genenames.org/download/custom/). Contains identifiers and/or symbols from different sources (HGNC, NCBI, Ensembl, Uniprot) for genes of the HGNC database. This file has been downloaded on 11/01/23. If you want to download an updated version, follow the above link and select "Approved Symbol", "NCBI Gene ID", "Ensembl gene ID" and "UniProt ID" in the custom download section.
* ```utilities.py``` : Python script containing a function to clean a network (remove redundancy and self-edges)

### Usage

To build the PPI network you can download the following updated datadase files :
- Lit-BM and Hi-Union from HuRI : http://www.interactome-atlas.org/download 
- APID level 2 homo sapiens wihtout inter-species interactions : http://cicblade.dep.usal.es:8080/APID/init.action. Rename this file ```APID_level2_homo_sapiens.txt```.
In this case you will have to rename the names of the files in the ```process_PPI.sh``` script.

A version of these databases files downloaded in January 2023 is provided in the ```data``` folder

Then do :


```chmod +x process_PPI.sh```


```bash process_PPI.sh```

This will generate the PPI network file ```PPI_LitBM_HiUnion_APID.tsv``` in the folder ```network_output```.

### References

- Luck, K., Kim, DK., Lambourne, L. et al. A reference map of the human binary protein interactome. Nature 580, 402?408 (2020). https://doi.org/10.1038/s41586-020-2188-x
- Diego Alonso-López, Francisco J Campos-Laborie, Miguel A Gutiérrez, Luke Lambourne, Michael A Calderwood, Marc Vidal, Javier De Las Rivas, APID database: redefining protein–protein interaction experimental evidences and binary interactomes, Database, Volume 2019, 2019, baz005, https://doi.org/10.1093/database/baz005
- Ruth L Seal, Bryony Braschi, Kristian Gray, Tamsin E M Jones, Susan Tweedie, Liora Haim-Vilmovsky, Elspeth A Bruford, Genenames.org: the HGNC resources in 2023, Nucleic Acids Research, Volume 51, Issue D1, 6 January 2023, Pages D1003–D1009, https://doi.org/10.1093/nar/gkac888

