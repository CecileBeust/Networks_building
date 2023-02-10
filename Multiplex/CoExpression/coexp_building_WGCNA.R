################################################################################################################
# R script to build co-expression network from RNA-seq expression data
# for 20 000 genes in 254 tissues with the WGCNA protocol
# WGCNA : Weighted Gene Correlation Network Analysis
# Data downloaded from Human Protein Atlas : https://www.proteinatlas.org/download/rna_tissue_hpa.tsv.zip
# Tissue description available at : https://www.proteinatlas.org/download/rna_tissue_hpa_description.tsv.zip
# Data downloaded on Wed 25 Jan 2023 and preprocessed to remove retired Gene Identifiers from input file
# (removing of 8 gene identifiers not recognized by HGCN)
# Author : Cécile Beust

# Software and packages versions
# R version 4.1.0
# WGCNA version 1.72-1
# hpoPlot version 2.4
# Rgraphviz version 2.38.0
# reshape 2 version 1.4.4
################################################################################################################

# Load packages and import data
library(WGCNA)
library(reshape2)

exprData <- read.table(file = "rna_tissue_hpa_250123_WOBadIDs.tsv", header = TRUE, sep = "\t")
head(exprData)

# remove unwanted columns : Gene, TPM and pTPM
# we only need Gene.name, Tissue and nTPM (normalized expression)
exprData <- exprData[,-c(1,4,5)]
head(exprData)

# reshape the data frame to have genes in columns, tissues in rows and nTPM as values
exprData_reshaped <- dcast(exprData, Tissue~Gene.name, fun.aggregate = sum, value.var = "nTPM")
# display dataframe head
exprData_reshaped[c(1:5), c(1:5)]
# write the new dataframe in an output file
write.table(exprData_reshaped, file='exprData_reshaped.tsv', quote=FALSE, sep='\t', col.names=NA)

# Remove first column containing tissue names and store it in another object
dataExpr0 <- exprData_reshaped[,-1]
dataExpr0[c(1:5), c(1:5)]
# Add row names = tissue names
rownames(dataExpr0) <- exprData_reshaped$Tissue
dataExpr0[c(1:5), c(1:5)]

# Check if the dataset contains missing data
gsg <- goodSamplesGenes(datExpr = dataExpr0, verbose = 3)
gsg$allOK

print(gsg$goodSamples)
print(gsg$goodGenes)

# If all the genes do not pass the cut, then remove the bad ones
if (!gsg$allOK)
{
  # Optionally, print the gene and sample names that were removed:
  if (sum(!gsg$goodGenes)>0)
    printFlush(paste("Removing genes:", paste(names(dataExpr0)[!gsg$goodGenes], collapse = ", ")));
  if (sum(!gsg$goodSamples)>0)
    printFlush(paste("Removing samples:", paste(rownames(dataExpr0)[!gsg$goodSamples], collapse = ", ")));
  # Remove the offending genes and samples from the data:
  dataExpr0 = dataExpr0[gsg$goodSamples, gsg$goodGenes]
}

# Build dendrogramm of tissue expression
TissueTree <- hclust(d = dist(dataExpr0), method = "average")
# We choose a cutoff value of 3e+05
plot(TissueTree, main = "Tissue dendrogram", sub = "", xlab = abline(h = 3e+05, col="red"))
# There are 2 outlier tissues : pancreas and salivary gland

# Removing of outliers : cut the tree in 2 parts
clust <- cutreeStatic(TissueTree, cutHeight = 3e+05, minSize = 10)
table(clust)
# Keep only tissues in the secong group
keepTissue <- clust == 1
dataExpr0 <- dataExpr0[keepTissue,]
nGenes <- ncol(dataExpr0)
nTissues <- nrow(dataExpr0)
nGenes
nTissues
# 19788 genes and 251 tissues remaining

# Add informations about tissues
#TissueInformations <- read.table(file = "rna_tissue_hpa_description.tsv", sep = "\t", head = TRUE, stringsAsFactors = TRUE)
#head(TissueInformations)
#TissueInformations <- TissueInformations[-c(212, 116, 217),]
#tissues <- rownames(dataExpr0)
#description_rows <- match(tissues, TissueInformations$Tissue)
#TissueData <- TissueInformations[description_rows, -1]
#head(TissueData)
#rownames(TissueData) <- TissueInformations[description_rows, 1]
#length(TissueData$Tissue.group)
#head(TissueData)

# Network construction

powers <- c(c(1:10), seq(from = 12, to = 20, by = 2))
powers

sft <- pickSoftThreshold(dataExpr0, powerVector = powers, verbose = 5)
plot(sft$fitIndices[,1], -sign(sft$fitIndices[,3])* sft$fitIndices[,2],
     xlab = "Soft Threshold power", ylab = "Scale Free Topology Model Fit, R²",
     type = "n", main = "Scale independence")
text(sft$fitIndices[,1], -sign(sft$fitIndices[,3])* sft$fitIndices[,2], labels = powers, col = "black")
abline(h = 0.80, col = "red")
plot(sft$fitIndices[,1], sft$fitIndices[,5],
     xlab = "Soft Threshold power", ylab = "Mean connectivity", 
     type = "n", main = "Mean connectivity")
text(sft$fitIndices[,1], sft$fitIndices[,5], labels = powers, col = "black")

# we choose power = 7

# similarity matrix construction
softPower <- 7
similarityMat <- adjacency(dataExpr0, power = softPower)
similarityMat[c(1:5), c(1:5)]

# Topological overlap matrix construction
TOM <- TOMsimilarity(similarityMat)
colnames(TOM) <- colnames(similarityMat)
rownames(TOM) <- rownames(similarityMat)
TOM[c(1:5), c(1:5)]

# export network for visualization with Cytoscape
cyt <- exportNetworkToCytoscape(TOM,
                                edgeFile = "CytoscapeInput_edges_018.txt",
                                weighted = TRUE,
                                threshold = 0.16,
                                nodeNames = colnames(dataExpr0))

