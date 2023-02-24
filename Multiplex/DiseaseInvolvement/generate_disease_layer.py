#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 02/02/23

@author: Cécile Beust

Python script to generate a disease involvement
network from a gene-disease associations file, where genes
are paired as binary interactions if they are involved
in the occurence of the same diseases
Database source : DisGeNET gene-disease associations from 2021
"""

# Import modules
import pandas as pd
import itertools
import pickle
import numpy as np

# Define fiel names
gene_disease_associations = "Gene_Disease_DisGeNET_2021.tsv"
output_file = "Gene_involved_in_diseases_layer.tsv"

def build_gene_disease_interactions(input_file:str, output: str):
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
    # Filter gene-disease associations with a threshold of 0.3
    df = df[df[2] >= 0.3]
    print(df.shape)
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
    
    # initialize np array for the associations to store
    to_write = np.zeros(800000000, dtype=object)
    counter = 0
    # get the lsit of genes involved in the same disease
    for disease in dico_disease_genes.keys():
        dico_disease_genes[disease] = sorted(dico_disease_genes[disease])
        # pair the genes from the list 
        # for a list of n genes : n*(n-1)/2 possible combinations
        for gene1, gene2 in itertools.combinations(dico_disease_genes[disease], 2):
            # remove self self interactions
            if gene1 != gene2:
                    # write gene pairs in the output file
                    to_add = str(gene1 + "\t" + gene2)
                    #to_write = np.append(arr=to_write, values=to_add, axis=None)
                    to_write[counter] = to_add
                    counter += 1
                    print(counter)
    # remove duplicates
    to_write = pd.unique(to_write)
    df2 = pd.DataFrame(to_write)
    # drop the last row
    df2.drop(df2.tail(1).index, inplace=True)
    print(df2)
    # if pkl output is desired
    # df2.to_pickle(output)
    # export network to tsv file
    df2.to_csv(output_file, index=False, header=None)

build_gene_disease_interactions(gene_disease_associations, output_file)
