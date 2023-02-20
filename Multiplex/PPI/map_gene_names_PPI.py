#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 31/01/23

@authors: 
- function getMappingDict : Ozan Ozisik
- function process_ppi_file_HUGO : Cécile Beust

Functions to map Ensembl gene IDs from
an interaction file to HUGO gene names
"""

# Import modules
import pandas as pd

# Define file names
mapping_file_path = "ID_mapping_HUGO_11_01_23.txt"
PPI_file_path = "PPI_LitBM_HiUnion.tsv"
output_interaction_file = "PPI_LitBM_HiUnion_APID_not_cleaned.tsv"

# Mapping function
def getMappingDict(filePath, convertFrom, convertTo):
	df=pd.read_csv(filePath, sep="\t")
	df=df[[convertFrom, convertTo]]
	df=df.dropna(axis=0)
	if('Approved symbol' in df.columns):
		df['Approved symbol']= df['Approved symbol'].astype(str)
		df['Approved symbol']= df['Approved symbol'].astype(str)
	
	df=df.set_index(convertFrom)
	
	mappingDict=df.to_dict()[convertTo]
	
	return mappingDict

# Processing function
def process_ppi_file_HUGO(input_file: str, output_file: str, From: str, To: str):
	mapping_dict = getMappingDict(
		filePath=mapping_file_path,
		convertFrom=From,
		convertTo=To
	)
	df = pd.read_csv(input_file, sep = "\t", header=None)
	df = df.reset_index()
	interactions = []
	to_write = []
	for index, row in df.iterrows():
		# get ids of interactants
		id_1 = row[0]
		id_2 = row[1]
		# check if Ensemnl gene ID 1 is in the mapping dict
		if id_1  in mapping_dict:
			# get gene name of interactant 1
			name_1 = mapping_dict[id_1]
			# check if Ensembl gene ID 2 is in the mapping dict
			if id_2 in mapping_dict:
				# get gene name of interactant 2
				name_2 = mapping_dict[id_2]
				# keep interaction
				interactions.append((name_1, name_2))
	# writing of the output file
	with open(output_file, 'w') as fo:
		to_write = []
		for genes in interactions:
			gene1 = genes[0]
			gene2 = genes[1]
			to_write += [str(gene1 + "\t" + gene2)]
		fo.write("\n".join([line for line in to_write]))

process_ppi_file_HUGO(PPI_file_path, output_interaction_file, "Ensembl gene ID", "Approved symbol")

"""with open("PPI_LitBM_HiUnion_APID.tsv", 'r') as fi:
	interactions = []
	for line in fi:
		gene1 = line.split("\t")[0].rstrip()
		gene2 = line.split("\t")[1].rstrip()
		interaction = (gene1, gene2)
		red = (gene2, gene1)
		if not interaction in interactions and not red in interactions:
			interactions.append(interaction)
		else:
			print(interaction)
			print(red)
	print(len(interactions))"""