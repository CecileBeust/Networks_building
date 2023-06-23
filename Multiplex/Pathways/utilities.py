#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 31/01/23

@author: Cécile Beust

Function to clean a network file by removing
redundant interactions 
"""

# Import modules
import argparse
from os import path

# Argparse
parser = argparse.ArgumentParser(
    prog="utilities.py", 
    description="clean a network file (remove redundancy, duplicate lines and self loops"
    )
parser.add_argument("-i", "--filename", help="input network file", required=True, type=str)
parser.add_argument("-o", "--output", help="output file name for cleaned network", required=False, type=str)
parser.add_argument("-v", "--verbose", help="increase output verbosity", required=False, action="store_true")
args = parser.parse_args()

# Check if the file exist
if path.exists(args.filename) == False :
    raise ValueError("Incorrect file name, please try again")
# Name given by default for output file
if args.output == None:
    args.output = str(args.filename[0:-3]) + "_cleaned.tsv"

filein = args.filename
fileout = args.output

# Function
def clean_network(input: str, output: str):
    to_keep = []
    with open(input, 'r') as fi:
        for line in fi:
            # split the two genes
            gene1 = line.split("\t")[0].rstrip()
            gene2 = line.split("\t")[1].rstrip()
            # check if genes are different
            if gene1 != gene2 : 
                interaction = (gene1, gene2)
                redundant_interaction = (gene2, gene1)
                # check redundant interactions
                if interaction not in to_keep and redundant_interaction not in to_keep:
                    to_keep.append(interaction)
    # writing of the output file
    with open(output, 'w') as fo:
        to_write = []
        for genes in to_keep:
            gene1 = genes[0]
            gene2 = genes[1]
            to_write += [str(gene1 + "\t" + gene2)]
        fo.write("\n".join([line for line in to_write]))
        fo.write("\n")
         
clean_network(filein, fileout)