#!/bin/bash

# map gene identifiers
python reactome_map_HUGO.py
# clean network (remove redundancy and self loops)
python utilities.py -i Pathways_reactome_not_cleaned.tsv -o Pathways_reactome.tsv
# remove intermediate file 
# rm Pathways_reactome_not_cleaned.tsv