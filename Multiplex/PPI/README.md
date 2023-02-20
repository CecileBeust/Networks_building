## Protein-protein (PPI) layer

### Usage

To build the PPI network you need to download the following data files :
- Lit-BM and Hi-Union from HuRI : http://www.interactome-atlas.org/download 
- APID level 2 homo sapiens wihtout inter-species interactions : http://cicblade.dep.usal.es:8080/APID/init.action. Rename this file ```APID_level2_homo_sapiens.txt```.


Then do :


```chmod +x process_PPI.sh```


```bash process_PPI.sh```