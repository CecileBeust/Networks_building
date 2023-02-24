## Co-expression layer

### Files

* ```coexp_building_WGCNA.R``` : R script allowing to build a co-expression network from expression data file using the WGCNA (Weighted Gene Coexpression Network Analysis) method. 
* ```rna_tissue_hpa.tsv```: expression data downloaded from the Human Protein Atlas (RNA HPA tissue gene data : https://www.proteinatlas.org/about/download). Data correspond to transcript expression levels summarized per gene in 256 tissues based on RNA-seq.

### Usage

Download the expression file ```rna_tissue_hpa.tsv``` from HPA (link above) and run the script ```coexp_building_WGCNA.R```