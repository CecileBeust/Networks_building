#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 2023

@author: Cécile

Functions to analyze a network interaction file
"""

import networkx as nx

def analyse_network(network: str):
    """Function which analyzes a network
    interactome file by computing some
    network metrics :
       - number of nodes
       - number of edges
       - number of self-loops
       - density

    Args:
        network (str): the name of the interactome file
    """
    # We use the networkx Graph class : undirected graph,
    # wihtout parallel edges
    ntw = nx.read_edgelist(network, create_using = nx.Graph)
    print(f"number of nodes : {nx.number_of_nodes(ntw)}")
    print(f"number of edges :  {nx.number_of_edges(ntw)}")
    print(f"number of self loops : {nx.number_of_selfloops(ntw)}")
    print(f"self loops : {list(nx.nodes_with_selfloops(ntw))}")
    print(f"density : {nx.density(ntw)}")
    all_degress = ntw.degree()
    average_degree = (sum(all_degress.values()))/(nx.number_of_nodes(ntw))
    print(f"average degree : {average_degree}")


print("PPI")
analyse_network("~/Multiplex/PPI/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv")
print(" ")
print("Pathway")
analyse_network("~/Multiplex/Pathways/reactome_pathways_gene_names_190123.tsv")
print(" ")
print("Complexes")
analyse_network("~/Multiplex/Complexes/Complexes_gene_names_190123.tsv")
print(" ")
print("CoExp")
analyse_network("~/Multiplex/CoExpression/Coexpresssion_th05_020223_final.tsv")
print(" ")
print("Disease Involvement")
analyse_network("~/Multiplex/DiseaseInvolvement/Gene_involved_in_diseases_layer_020223.tsv")

