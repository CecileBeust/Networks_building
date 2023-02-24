## Protein-protein (PPI) layer

### Files

* ```process_PPI.sh``` : bash script to build the PPI network
* ```map_gene_names.py``` : Python script containing functions for the mapping of gene identifiers
* ```ID_mapping_HUGO_11_01_23.txt``` : Mapping file downloaded from the HGNC custom download page (https://www.genenames.org/download/custom/). Contains identifiers and/or symbols from different sources (HGNC, NCBI, Ensembl, Uniprot) for genes of the HGNC database. This file has been downloaded on 11/01/23. If you want to download an updated version, follow the above link and select "Approved Symbol", "NCBI Gene ID", "Ensembl gene ID" and "UniProt ID" in the custom download section.
* ```utilities.py``` : Python script containing a function to clean a network (remove redundancy and self-edges)

### Usage

To build the PPI network you need to download the following data files :
- Lit-BM and Hi-Union from HuRI : http://www.interactome-atlas.org/download 
- APID level 2 homo sapiens wihtout inter-species interactions : http://cicblade.dep.usal.es:8080/APID/init.action. Rename this file ```APID_level2_homo_sapiens.txt```.


Then do :


```chmod +x process_PPI.sh```


```bash process_PPI.sh```