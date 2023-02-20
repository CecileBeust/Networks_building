## Protein-protein (PPI) layer

### Usage

To build the PPI network you need to download the following data files :
- Lit-BM and Hi-Union from HuRI : http://www.interactome-atlas.org/download 
- APID level 2 homo sapiens wihtout inter-species interactions : http://cicblade.dep.usal.es:8080/APID/init.action


Then do :


```chmod +x process_PPI.sh```


```bash process_PPI.sh```

TODO : 
- improve removing of rendundancy and self self
- add procedure for mapping of APID uniprot to gene names
- remove useless files
