# Networks_building
Scripts to build a 5 layers Multiplex biological network of gene/protein interactions.

The ```Multiplex``` folder contains specific folders and files to build a biological multiplex network composed of 5 layers :

- PPI : Protein-Protein Interactions network (source : Hi-Union + Lit-BM + APID level 2)
- Pathways : Human protein-protein interactions derived from Reactome pathway data
- Co-expression : Transcript expression levels summarized per gene in 256 tissues from RNA-seq data (source : Human Protein Atlas)
- Complexes : Protein-protein interactions derived from human protein complexes (source : CORUM + Hu.map 2)
- Disease involvement : Associations of genes based on their involvement in the same diseases (source : Gene-disease associations from DisGeNet, version 2021)