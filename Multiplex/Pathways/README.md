## Pathways layer

### Files

* ```generate_pathways_network.sh``` : bash script to build the pathways network
* ```reactome_map_HUGO.py``` : Python script to generate a network of protein-protein interactions extracted from Pathway data of Reactome (dowload data from : https://reactome.org/download/current/interactors/reactome.homo_sapiens.interactions.tab-delimited.txt)
* ```ID_mapping_HUGO_11_01_23.txt``` : Mapping file downloaded from the HGNC custom download page (https://www.genenames.org/download/custom/). Contains identifiers and/or symbols from different sources (HGNC, NCBI, Ensembl, Uniprot) for genes of the HGNC database. This file has been downloaded on 11/01/23. If you want to download an updated version, follow the above link and select "Approved Symbol", "NCBI Gene ID", "Ensembl gene ID" and "UniProt ID" in the custom download section.

### Usage

Download Human protein-protein interactions file from Reactome from the link above and run :

```chmod +x generate_pathways_network.sh``` \
```bash generate_pathways_network.sh```