#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  31 2023

@author: Cécile

Input : Gene-Disease associations tsv file (downloaded from DisGeNET in 2021)
Output : Tsv file containing associations of genes involved in the same disease
"""

# Import modules
import pandas as pd
import itertools

gene_disease_associations = "Gene_Disease_DisGeNET_2021.tsv"
output_file = "Gene_involved_in_diseases_layer_010223.tsv"

def build_gene_disease_interactions(input_file:str, output_file: str):
    """Function which gets genes involved the same diseases from 
    a gene-disease association file

    Args:
        input_file (str): the name of the gene-disease association
        file
        output_file (str): the desired name of the output file
    """
    dico_disease_genes: dict = {}
    # reading of the input file
    df = pd.read_csv(input_file, sep = "\t", header=None)
    df = df.reset_index()
    # browsing of the file
    for index, row in df.iterrows():
        disease: str = row[0]
        gene: str = row[1]
        # we add the disease in the dico if it has not
        # previously been listed in the keys
        if disease not in dico_disease_genes:
            dico_disease_genes[disease] = []
        # we add the corresponding genes as values
        dico_disease_genes[disease].append(gene)

    # open and write the output file
    with open(output_file, 'w') as fo:
        seen = []
        to_write = []
        # get the lsit of genes involved in the same disease
        for disease in dico_disease_genes.keys():
            # pair the genes from the list 
            # for a list of n genes : n*(n-1)/2 possible combinations
            for gene1, gene2 in itertools.combinations(dico_disease_genes[disease], 2):
                # remove self self interactions
                if gene1 != gene2:
                    if (gene1, gene2) not in seen and (gene2, gene1) not in seen:
                        seen.append((gene1, gene2))
                        # write gene pairs in the output file
                        to_write += [str(gene1 + "\t" + gene2)]
        fo.write("\n".join([line for line in to_write]))

build_gene_disease_interactions(gene_disease_associations, output_file)