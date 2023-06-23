#!/bin/bash

# map gene identifiers
python reactome_map_HUGO.py

# clean network (remove redundancy and self loops)
python utilities.py -i network_output/Pathways_reactome_not_cleaned.tsv -o network_output/Pathways_reactome.tsv

# remove intermediate file 
rm network_output/Pathways_reactome_not_cleaned.tsv