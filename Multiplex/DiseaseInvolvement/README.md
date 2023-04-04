## Disease Involvement Network

This network is a network composed of genes involved in the same diseases. If 2 genes are involved in the occurence of at least one disease, they are linked by an edge in the network. 
This network is built using gene-disease associations from DisGeNET version 2021. Gene-disease associations presenting an association score higher or equal to 0.3 were selected to build the network.

### Files

* ```generate_disease_layer.py``` : Python script to generate a network file where genes are associated if they are commonly involved in the occurence of some diseases
* ```Gene_Disease_DisGeNET_2021.tsv``` : Gene-disease associations downloaded from DisGeNET (https://www.disgenet.org/), version 2021

### Usage

```python generate_disease_layer.py```

This will generate the network file Gene_involved_in_diseases_layer.tsv

### References

- Janet Piñero, Juan Manuel Ramírez-Anguita, Josep Saüch-Pitarch, Francesco Ronzano, Emilio Centeno, Ferran Sanz, Laura I Furlong, The DisGeNET knowledge platform for disease genomics: 2019 update, Nucleic Acids Research, Volume 48, Issue D1, 08 January 2020, Pages D845–D855, https://doi.org/10.1093/nar/gkz1021
