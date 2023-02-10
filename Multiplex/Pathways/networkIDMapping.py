#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:28:34 2022

@author: Ozan

Converts IDs of genes in a network file
"""

import pandas as pd


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



def mapIDs(nwFileInput, nwFileOutput, mappingFile, convertFrom, convertTo, columnsToMap, keepInteractionEvenIfNoMap):
	'''
	

	Parameters
	----------
	nwFileInput : str
		Path of the input interactions file
	nwFileOutput : str
		Path of the output interactions file
	mappingFile : str
		Path of the mapping file with one type of ID in each column
	convertFrom : str
		One of these: 'Approved symbol' 'NCBI Gene ID(supplied by NCBI)' 'Ensembl ID(supplied by Ensembl)'
	convertTo : str
		One of these: 'Approved symbol' 'NCBI Gene ID(supplied by NCBI)' 'Ensembl ID(supplied by Ensembl)'
	columnsToMap : list of int
		Indicates columns to be mapped, starts from ZERO
	keepInteractionEvenIfNoMap : bool
		Whether to keep the interaction in the case of one or more interactors are not found in the maping file (original IDs are maintained)

	Returns
	-------
	None.

	'''
	
	mappingDict=getMappingDict(mappingFile, convertFrom, convertTo)

	fout=open(nwFileOutput, 'w') 
	with open(nwFileInput, 'r') as f:
		lines=[line.rstrip('\n') for line in f]
		for line in lines:
			if not line.startswith("ChEBI"):
				substrings=line.split('\t')
				noMapping=False
				neoLine=''
				for i in range(len(substrings)):
					if i in columnsToMap:
						if substrings[i][10:] in mappingDict:
							neoID=mappingDict[substrings[i][10:]]
						else:
							neoID=substrings[i]
							noMapping=True
					else:
						neoID=substrings[i]
					
					neoLine=neoLine+neoID
					if(i<len(substrings)-1):
						neoLine=neoLine+'\t'
				
				neoLine=neoLine+'\n'
				if(keepInteractionEvenIfNoMap or (not noMapping)):
					fout.write(neoLine)
			
	fout.close()



##############################################################################


if __name__ == "__main__":

	mapIDs('Data/PreNetwork/brain_topEntrez.csv',
		   'Data/Network/brainGiantTop.csv',
		   'Data/PreNetwork/HGNC 220523.csv',
		   'NCBI Gene ID(supplied by NCBI)',
		   'Approved symbol',
		   [0,1],
		   False)


'''
	mapIDs('Data/PreNetwork/HuRI.tsv',
		   'Data/Network/HuRI2.tsv', 
		   'Data/PreNetwork/HGNC 220523.csv',
		   'Ensembl ID(supplied by Ensembl)',
		   'Approved symbol',
		   [0,1],
		   False)
'''



#######################################

'''
## Removing interactions thata involve OMIM gene codes
## We already have ppi, we need only OMIM diseases

f=open('Data/Other/OMIMgenes.txt','r')
omimGenes=set(line.rstrip('\n') for line in f)
f.close()

nwFileInput='Data/Network/gda_disgenet_03 PMID33634312 Edited.csv'
nwFileOutput='Data/Network/gda_disgenet_03 PMID33634312 Edited 2.csv'

fout=open(nwFileOutput, 'w') 
with open(nwFileInput, 'r') as f:
	lines=[line.rstrip('\n') for line in f]
	for line in lines:
		substrings=line.split('\t')
		if (substrings[0] not in omimGenes) and (substrings[1] not in omimGenes):
			fout.write(line+'\n')

fout.close()
'''
#######################################

