## Co-expression layer

### Files

* ```coexp_building_WGCNA.R``` : R script allowing to build a co-expression network from expression data file using the WGCNA (Weighted Gene Coexpression Network Analysis) method. 
* ```rna_tissue_hpa.tsv```: expression data downloaded from the Human Protein Atlas (RNA HPA tissue gene data : https://www.proteinatlas.org/about/download). Data correspond to transcript expression levels summarized per gene in 256 tissues based on RNA-seq.

### Usage

Download the expression file ```rna_tissue_hpa.tsv``` from HPA (link above) and run the script ```coexp_building_WGCNA.R```. 

This will generate a file ```Coexpression_edges.tsv```.

### References

- Uhlén M, Fagerberg L, Hallström BM, Lindskog C, Oksvold P, Mardinoglu A, Sivertsson Å, Kampf C, Sjöstedt E, Asplund A, Olsson I, Edlund K, Lundberg E, Navani S, Szigyarto CA, Odeberg J, Djureinovic D, Takanen JO, Hober S, Alm T, Edqvist PH, Berling H, Tegel H, Mulder J, Rockberg J, Nilsson P, Schwenk JM, Hamsten M, von Feilitzen K, Forsberg M, Persson L, Johansson F, Zwahlen M, von Heijne G, Nielsen J, Pontén F. Proteomics. Tissue-based map of the human proteome. Science. 2015 Jan 23;347(6220):1260419. doi: 10.1126/science.1260419. PMID: 25613900.
- Langfelder, P., Horvath, S. WGCNA: an R package for weighted correlation network analysis. BMC Bioinformatics 9, 559 (2008). https://doi.org/10.1186/1471-2105-9-559
