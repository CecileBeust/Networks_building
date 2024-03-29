## Pathway Network

The Pathway network connects proteins involved in common biological pathways from Reactome


### Files

* ```generate_pathways_network.sh``` : bash script to build the pathways network
* ```reactome_map_HUGO.py``` : Python script to generate a network of protein-protein interactions extracted from Pathway data of Reactome (dowload data from : https://reactome.org/download/current/interactors/reactome.homo_sapiens.interactions.tab-delimited.txt)
* ```ID_mapping_HUGO_11_01_23.txt``` : Mapping file downloaded from the HGNC custom download page (https://www.genenames.org/download/custom/). Contains identifiers and/or symbols from different sources (HGNC, NCBI, Ensembl, Uniprot) for genes of the HGNC database. This file has been downloaded on 11/01/23. If you want to download an updated version, follow the above link and select "Approved Symbol", "NCBI Gene ID", "Ensembl gene ID" and "UniProt ID" in the custom download section. To build this network, Uniprot identifiers from the original Reactome file will be mapped to their cooresponding Gene Symbol in accordance to the Hugo Gene Name Consortium. 

### Usage

If you want to build this network on updated data, you can download the Human protein-protein interactions file from Reactome from the link above. Then check if the filename corresponds from the one written in the scripts, and run :

```chmod +x generate_pathways_network.sh``` \
```bash generate_pathways_network.sh```

You can also use a version of the data file downloaded in January 2023 provided in the ```data``` folder.

This will generate the network file ```Pathways_reactome.tsv``` in the ```network_output``` folder.

### References

- Marc Gillespie, Bijay Jassal, Ralf Stephan, Marija Milacic, Karen Rothfels, Andrea Senff-Ribeiro, Johannes Griss, Cristoffer Sevilla, Lisa Matthews, Chuqiao Gong, Chuan Deng, Thawfeek Varusai, Eliot Ragueneau, Yusra Haider, Bruce May, Veronica Shamovsky, Joel Weiser, Timothy Brunson, Nasim Sanati, Liam Beckman, Xiang Shao, Antonio Fabregat, Konstantinos Sidiropoulos, Julieth Murillo, Guilherme Viteri, Justin Cook, Solomon Shorser, Gary Bader, Emek Demir, Chris Sander, Robin Haw, Guanming Wu, Lincoln Stein, Henning Hermjakob, Peter D’Eustachio, The reactome pathway knowledgebase 2022, Nucleic Acids Research, 2021;, gkab1028, https://doi.org/10.1093/nar/gkab1028

- Ruth L Seal, Bryony Braschi, Kristian Gray, Tamsin E M Jones, Susan Tweedie, Liora Haim-Vilmovsky, Elspeth A Bruford, Genenames.org: the HGNC resources in 2023, Nucleic Acids Research, Volume 51, Issue D1, 6 January 2023, Pages D1003–D1009, https://doi.org/10.1093/nar/gkac888
