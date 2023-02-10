import pandas as pd

df = pd.read_csv("complexes_with_name.tsv", sep="\t", header=0)
df = df.reset_index()

# drop stoichiometry, sources, references, identifiers
cols = [0,1,2,3,5,6,7,8]
df.drop(df.columns[cols], axis=1, inplace=True)

 # export to tsv
df.to_csv("complexes_reduced_120123.tsv", sep = "\t", header=False, index=False)

"""for index, row in df.iterrows():
    print(row['components'])"""

import itertools

def build_complex_layer(input_file: str, output_file: str):
    complexes = []
    with open(input_file, 'r') as fi:
        for line in fi:
            list_interactions_in_complex = line.split("_")
            for gene1, gene2 in itertools.combinations(list_interactions_in_complex, 2):
                complexes.append((gene1, gene2))
    
    with open(output_file, 'w') as fo:
        for interaction in complexes:
            gene1 = interaction[0].rstrip()
            gene2 = interaction[1].rstrip()
            fo.write(gene1 + "\t" + gene2 + "\n")                
                
# build_complex_layer("toy_ex_complexes.tsv", "toy_ex_complexes_reordered.tsv")
# build_complex_layer("complexes_reduced_120123.tsv", "Complexes_gene_names_120123.tsv")

def remove_redundancy(input_file: str, output_file: str):
    """Function which remove redundant interactions from 
    a gene interaction file

    Args:
        input_file (str): the name of the input file
        output_file (str): the name of the output file
    """
    list_interactions = []
    with open(input_file, 'r') as fi:
        for line in fi:
            print(line.split("\t"))
            gene1 = line.split("\t")[0]
            gene2 = line.split("\t")[1].rstrip()
            interaction = (gene1, gene2)
            redundant_interaction = (gene2, gene1)
            if interaction not in list_interactions and redundant_interaction not in list_interactions:
                list_interactions.append(interaction)

    with open(output_file, 'w') as fo:
        for interaction in list_interactions:
            gene1 = interaction[0]
            gene2 = interaction[1]
            fo.write(gene1 + "\t")
            fo.write(gene2 + "\n")

remove_redundancy("Complexes_gene_names_120123.tsv", "Complexes_gene_names_WO_redundancy_120123.tsv")