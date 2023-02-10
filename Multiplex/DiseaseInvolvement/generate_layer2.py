# Import modules
import pandas as pd
import itertools
import pickle
import numpy as np

gene_disease_associations = "Gene_Disease_DisGeNET_2021.tsv"
output_file = "Gene_involved_in_diseases_layer_020223.pkl"

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
    
    print(len(dico_disease_genes))
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
    to_write = pd.unique(to_write)
    df2 = pd.DataFrame(to_write)
    # drop the last row
    df2.drop(df2.tail(1).index, inplace=True)
    print(df2)
    df2.to_pickle(output)
    print(df2)
    df2.to_csv("Gene_involved_in_diseases_layer_020223.tsv", index=False, header=None)

build_gene_disease_interactions(gene_disease_associations, output_file)


#df = pd.read_csv(gene_disease_associations, sep = "\t", header=None)

#df = df[df[2] >= 0.3]


# genes = []
# browsing of the file
"""for index, row in df.iterrows():
    disease: str = row[0]
    gene: str = row[1]
    genes.append(gene)

genes_uniq = set(sorted(genes))
print(len(genes_uniq))

s = (800000000, 2)
graph_all_genes = np.zeros(s, dtype=object)
print(graph_all_genes)
counter = 0
for gene1, gene2 in itertools.combinations(genes_uniq, 2):
    graph_all_genes[counter, 0] = gene1
    graph_all_genes[counter, 1] = gene2
    counter += 1
    print(counter)
print(graph_all_genes)

graph_all_genes = np.unique(graph_all_genes)
df2 = pd.DataFrame(graph_all_genes)
print(df2)
# df2.drop_duplicates()
#df2.drop(df2.tail(1).index, inplace=True)
print(df2)
df2.to_pickle("graph_all_genes.pkl")"""
