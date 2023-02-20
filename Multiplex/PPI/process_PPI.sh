#!/bin/bash

# Merge Lit-Bm and Hi-Union files in one tsv file
cat Lit-BM-090123.tsv > PPI_LitBM_HiUnion.tsv
cat HI-union-090123.tsv >> PPI_LitBM_HiUnion.tsv

# Map the Ensembl IDs to Approved HUGO symbols (Gene names)
python3 map_gene_names_PPI.py 

# Add APID gene names to the file
cut -f4,7 APID_level2_homo_sapiens_170123.txt >> PPI_LitBM_HiUnion_APID_not_cleaned.tsv

# Remove duplicate lines
sort PPI_LitBM_HiUnion_APID_not_cleaned.tsv | uniq > PPI_LitBM_HiUnion_APID_wo_dups.tsv

# run utilities.py to remove rendundant interactions
python3 utilities.py -i PPI_LitBM_HiUnion_APID_wo_dups.tsv -o PPI_HiUnion_LitBM_APID.tsv

# Remove intermediate files
# rm PPI_LitBM_HiUnion.tsv
# rm PPI_LitBM_HiUnion_APID_not_cleaned.tsv
# rm PPI_LitBM_HiUnion_APID_wo_dups.tsv