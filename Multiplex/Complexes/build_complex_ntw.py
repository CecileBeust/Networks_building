#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 18/01/23

@author: Cécile Beust

Build a Complexes network layer from a file containing 
informations about proteins involved in the same complexes
obtained with the script extract_proteins_complexes.R
"""

# import modules
import itertools

def build_complex_layer(input_file: str, output_file: str):
    """Function to associate proteins involved in the same
    biological complexes as binary interactions from a tsv
    file

    Args:
        input_file (str): name of the input file
        output_file (str): name of the desired output file
    """
    # initialize a list which will contain all the binary interactions between proteins
    complexes = []
    with open(input_file, 'r') as fi:
        for line in fi:
            # split proteins involved in the same complex
            list_interactions_in_complex = line.split("_")
            # build binary interactions between proteins involved in the same complexes
            for gene1, gene2 in itertools.combinations(list_interactions_in_complex, 2):
                # add them to the list of interactions
                complexes.append((gene1, gene2))
    
    with open(output_file, 'w') as fo:
        list_interactions = []
        to_write = []
        for interaction in complexes:
            gene1 = interaction[0].rstrip()
            gene2 = interaction[1].rstrip()
            # check for redundancy
            interaction = (gene1, gene2)
            redundant_interaction = (gene2, gene1)
            if interaction not in list_interactions and redundant_interaction not in list_interactions:
                to_write += [gene1 + "\t" + gene2]
                list_interactions.append(interaction)
        # write interactions in the output file wihtout redundancy
        fo.write("\n".join([interaction for interaction in to_write]))                
                
build_complex_layer("complexes_gene_name.tsv", "Complexes_ntw_gene_names.tsv")