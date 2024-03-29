#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  11 2023

@authors: 
- function getMappingDict : Ozan
- function process_reactome_file_HUGO : Cécile

Processes Reactome Human Protein-Protein interaction file downloaded from
https://reactome.org/download/current/interactors/reactome.homo_sapiens.interactions.tab-delimited.txt

1 . Get Ensembl Gene IDs from mapping to HUGO Gene IDs
2 . Writes interactome output file
"""

# Import modules
import pandas as pd

# Defined file paths
mapping_file_path = "ID_mapping_HUGO_11_01_23.txt"
reactome_file_path = "data/reactome.homo_sapiens.interactions.tab-delimited.txt"
output_interaction_file = "network_output/Pathways_reactome_not_cleaned.tsv"

def getMappingDict(filePath, convertFrom, convertTo):
	df=pd.read_csv(filePath, sep="\t")
	df=df[[convertFrom, convertTo]]
	df=df.dropna(axis=0)
	if('UniProt ID(supplied by UniProt)' in df.columns):
		df['UniProt ID(supplied by UniProt)']= df['UniProt ID(supplied by UniProt)'].astype(str)
		df['UniProt ID(supplied by UniProt)']= df['UniProt ID(supplied by UniProt)'].astype(str)
	
	df=df.set_index(convertFrom)
	
	mappingDict=df.to_dict()[convertTo]
	
	return mappingDict

def process_reactome_file_HUGO(input_file: str, output_file: str, From: str, To: str):
    """Function which takes as input a human protein-protein
    interaction file downloaded from Reactome and gives as 
    output an interaction file with IDs or gene names mapped
    from HUGO Gene National Consortium

    Args:
        input_file (str): name of the reactome input file
        output_file (str): desired name of the interactome
        output file
        From (str) : identifier of symbol that you want to replace by mapping (column from mapping file)
        To (str) : identifier or symbol that you want to get by mapping (column from mapping file)
    """
    # Get dictionnary for mapping : Uniprot IDs and Ensembl Gene IDs
    # or gene names
    mapping_dict = getMappingDict(
    filePath = mapping_file_path, 
    convertFrom = From, 
    convertTo = To)

    # Load the reactome file
    df = pd.read_csv(input_file, sep = "\t", header=0)
    df = df.reset_index()
    interactions = []
    count_interactions = 0
    for index, row in df.iterrows():
        up_id_1 = row['# Interactor 1 uniprot id']
        up_id_2 = row['Interactor 2 uniprot id']
        # If the first interactant is present in the mapping dict
        if up_id_1[10:] in mapping_dict:
            # Map the ID of the first interactant 
            id1 = mapping_dict[up_id_1[10:]]
            # if the second interactant is prensent in the mapping dict
            if up_id_2[10:] in mapping_dict:
                # Map the ID of the second interactant
                id2 = mapping_dict[up_id_2[10:]]
                # If we managed to get both both identifiers for interactant 1 and 2
                # We get an interaction and add it to the interaction list
                count_interactions += 1
                interactions.append((id1, id2))
    # Writing of the output file
    with open(output_file, 'w') as fo:
        for genes in interactions:
            fo.write(genes[0] + "\t" + genes[1] + "\n")

process_reactome_file_HUGO(reactome_file_path, output_interaction_file , "UniProt ID(supplied by UniProt)", "Approved symbol")
