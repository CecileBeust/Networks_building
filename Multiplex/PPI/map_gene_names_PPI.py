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
	print(mapping_dict)
	df = pd.read_csv(input_file, sep = "\t", header=0)
	df = df.reset_index()
	interactions = []
	count_interactions = 0
	for index, row in df.iterrows():
		id_1 = row[0]
		id_2 = row[1]
		count_interactions += 1
		if id_1  in mapping_dict:
			name_1 = mapping_dict[id_1]
			if id_2 in mapping_dict:
				name_2 = mapping_dict[id_2]
				interactions.append((name_1, name_2))
	with open(output_file, 'w') as fo:
		for genes in interactions:
			fo.write(genes[0] + "\t" + genes[1] + "\n")

process_ppi_file_HUGO(PPI_file_path, output_interaction_file, "Ensembl gene ID", "Approved symbol")


