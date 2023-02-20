########################################################################
# Cextract_proteins_complexes.R : R script to extract proteins involved 
# in the same complexes from the CORUM and hu.MAP databases using the 
# OmnipathR package(https://r.omnipathdb.org/index.html)
#
# Databases sources : CORUM (http://mips.helmholtz-muenchen.de/corum/#)
# and hu.MAP (http://humap2.proteincomplexes.org/)
#
# Output : tsv file containing proteins involved in the
# same biological complexes associated with a "_" character
#
# Created on 31/01/23
#######################################################################

# Install packages
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

install.packages("libxml2-dev")
install.packages("igraph")
BiocManager::install("OmnipathR")
BiocManager::install(c("dnet"))

# Load packages
library(OmnipathR)
library(tidyr)
library(dnet)
library(gprofiler2)

## We check the different complexes databases
get_complex_resources()
## We query and store complexes from CORUM and hu.MAP into a dataframe.
complexes <- import_omnipath_complexes(resources=c("CORUM", "hu.MAP"))
head(complexes)
## Remove unwanted columns : we only keep the gene names component column
complexes <- complexes[,-c(1,2,4,5,6,7)]

## Export the dataframe as a tsv file
write.table(complexes, file='complexes_gene_name.tsv', quote = FALSE, sep="\t", col.names = FALSE, row.names = FALSE)
