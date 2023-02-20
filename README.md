# Networks_building
Scripts to build and process biological networks

The ```Multiplex``` folder contains files to build a biological multiplex network composed of 5 layers :

- PPI : Protein-Protein Interactions layer (source : Hi-Union + Lit-BM + APID level 2)
- Pathways : Human protein-protein interactions derived from Reactome pathway data
- Co-expression : Transcript expression levels summarized per gene in 256 tissues from RNA-seq data (source : Human Protein Atlas)
- Complexes : Protein-protein interactions derived from human protein complexes (source : CORUM + Hu.map 2)
- Disease involvement : Associations of genes based on their involvement in the same diseases (source : Gene-disease associations from DisGeNet, version 2021)