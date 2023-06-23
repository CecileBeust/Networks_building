#!/bin/bash

# Concatenate Lit-Bm and Hi-Union files in one tsv file
cat data/Lit-BM-090123.tsv > network_output/PPI_V1.tsv
cat data/Hi-union-090123.tsv >> network_output/PPI_V1.tsv

# Map the Ensembl IDs to Approved HUGO symbols (Gene names)
python3 map_ensembl.py -i network_output/PPI_V1.tsv -o network_output/PPI_V1_mapped.tsv

# Map APID
tail -n +2 data/APID_level2_homo_sapiens_170123.txt | cut -f2,5 > data/APID_interactions_uniprot.txt
python3 map_uniprot.py -i data/APID_interactions_uniprot.txt -o data/APID_interactions_mapped.txt

# Add APID gene names to the file
cat data/APID_interactions_mapped.txt >> network_output/PPI_V1_mapped.tsv

# Remove duplicate lines
sort network_output/PPI_V1_mapped.tsv | uniq > network_output/PPI_V2.tsv

# run utilities.py to remove rendundant interactions
python3 utilities.py -i network_output/PPI_V2.tsv -o network_output/PPI_LitBM_HiUnion_APID.tsv

# Uncomment these lines if you want to remove intermediate files
rm network_output/PPI_V1.tsv
rm network_output/PPI_V1_mapped.tsv
rm network_output/PPI_V2.tsv
