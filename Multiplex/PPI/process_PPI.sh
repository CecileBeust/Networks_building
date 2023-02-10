#!/bin/bash

# Merge PPI files in one tsv file
cat Lit-BM-090123.tsv > PPI_merged.tsv
cat HI-union-090123.tsv >> PPI_merged.tsv

# Map the Ensembl IDs to Approved HUGO symbols (Gene names)
python3 map_gene_names_PPI.py 

# Add APID
cat APID_uniprot_gene_names.tsv >> PPI_final.tsv

# Remove duplicate lines
awk '!seen[$0]++' PPI_final.tsv > PPI_final_not_cleaned.tsv

# python3 utilities # mettre les noms des fichiers en argument
python3 "/home/cbeust/Landscape_PA/Github_Codes/Networks_building/utilities.py" -i PPI_final_not_cleaned.tsv -o PPI_HiUnion_LitBM_APID_310123.tsv