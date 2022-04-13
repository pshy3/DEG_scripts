#source("https://bioconductor.org/biocLite.R")
#biocLite("Biobase")
#install.packages("Rcpp")
library(WGCNA)
library(snow)
library(iterators)
library(lattice)
options(stringsAsFactors = FALSE)
enableWGCNAThreads()
path = "./fpkmjoint/"
listtxt = list.files(path = path,pattern="*.txt")
for (k in 1:length(listtxt)){
  sr25 <- read.csv(paste0(path,listtxt[k]),header=TRUE,sep='\t',row.names=1)
  sr25 <- t(as.matrix(sr25))
  dim(sr25)
  name = gsub(".txt","",listtxt[k])
  dir.create(paste0("./",name))
  #sr25 <- sr25[,-1]
  #sr25 <- t(as.matrix(sr25[,-1]))
  #dim(sr25)
  powers = c(c(1:10), seq(from = 11, to=30, by=1))
  sft = pickSoftThreshold(sr25, powerVector = powers, verbose = 5)
  cex1 = 0.9
  h1 = paste0('./',name,'/h1.jpg')
  jpeg(h1, height = 1000, width=1200,quality=100,res=200)
  plot(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],xlab='Soft Threshold (power)',ylab='Scale Free Topology Model Fit,signed R^2',type='n',main = paste('Scale independence',name))
  text(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],labels=powers,cex=cex1,col='red')
  abline(h=0.90,col='red')
  dev.off()
  
  h2 = paste0('./',name,'/h2.jpg')
  jpeg(h2, height = 1000, width=1200,quality=100,res=200)
  plot(sft$fitIndices[,1], sft$fitIndices[,5],xlab='Soft Threshold (power)',ylab='Mean Connectivity', type='n',main = paste('Mean connectivity',name))
  text(sft$fitIndices[,1], sft$fitIndices[,5], labels=powers, cex=cex1,col='red')
  dev.off()
}

#DECLARE THE POWER BELOW FOR FURTHER PROCESSING

name <- "fpkmjoint/ML-WD-WT_6-9_vs_ML-WD-WT-T_1-4.txt"
powerassigned = 19


name = gsub(".txt","",name)
name = gsub("fpkmjoint/","",name)
sr25 <- read.csv(paste0(path,'/',name,".txt"),header=TRUE,sep='\t',row.names=1)
sr25 <- t(as.matrix(sr25))
dim(sr25)


h3 = paste0('./',name,'/h3.jpg')
net = blockwiseModules(sr25, power = powerassigned,TOMType = 'unsigned', minModuleSize = 30,reassignThreshold = 0, mergeCutHeight = 0.25,numericLabels = TRUE, pamRespectsDendro = FALSE,saveTOMs = TRUE,saveTOMFileBase = 'SS_vs_WW_lab_FR697_tf+gene_FPKM',verbose = 3)
jpeg(h3, height = 8000, width=50000,quality=100,res=200)
mergedColors = labels2colors(net$colors)
plotDendroAndColors(net$dendrograms[[1]], mergedColors[net$blockGenes[[1]]],'Module colors', hang = 0.03,addGuide = TRUE, guideHang = 0.05)
dev.off()

summaryColor <- table(mergedColors)
write.csv(summaryColor, file=(paste0('./',name,"/summary_",name,"_power-",powerassigned,".csv")))

colorMerge <- rbind(colnames(sr25),mergedColors)
tcolor <- t(colorMerge)
colnames(tcolor) <- c("Gene_ID","mergedColors")
write.csv(tcolor, file=(paste0('./',name,"/color_",name,".csv")))

heatmap = paste0('./',name,'/',"Heatmap_",name,".jpg")
jpeg(heatmap, height = 2000, width=2000,quality=100,res=200)
dissTOM = 1-TOMsimilarityFromExpr(sr25, power = powerassigned)
plotTOM = dissTOM^7
diag(plotTOM) = NA
TOMplot(plotTOM, net$dendrograms[[1]], mergedColors[net$blockGenes[[1]]], main = name)
dev.off()

##TOM to cytoscape op
colormerge_t=t(colorMerge)
mergedColors

## MODIFICATIONS TO tip_genes_in_modules.csv FILE
#1. ADD HEADER TO GENE ID COLUMS = Gene_ID
#2. <<<NOT USED HERE>>>>>ADD ANOTHER COLUMN FOR Gene Ontology terms - no GO terms know for this analysis, so placeholder numbers used.
annot_1 = read.csv(file = (paste0('./',name,"/color_",name,".csv"))); ###change to required file
# Select modules
#modules_1 = c("black","red","blue");
modules_1 = c("black","blue","brown","green","grey","red","turquoise","yellow");
modules_1
# Select module probes
head(sr25)
#probes = names(sr25)
#probes1 = char(head(sr25))
#probes1
#probes2 = as.character(head(sr25))
#probes2
probes1 = colnames(sr25)
probes1
inModule_1 = is.finite(match(mergedColors, modules_1));
inModule_1
modProbes_1 = probes1[inModule_1];
modProbes_1
annot_1
## MAKE SURE YOU ADD "Gene_ID" header for column in tip_genes_in_modules.csv FILE OR THIS WILL NOT WORK
annot_1$Gene_ID
#annot_1$mergedColors
##<<NOT USED>>Gene Annotation not known, so just numbers as placeholder for GO terms
annot_1$GO_term
#--
#modGenes_1 = annot_1$Gene_ID[match(modProbes_1, annot_1$GO_term)];
#modGenes_1 = annot_1$GO_term[match(modProbes_1, annot_1$Gene_ID)];
modGenes_1 = annot_1$GO_term[match(modProbes_1, annot_1$Gene_ID)];
modGenes_1
# Select the corresponding Topological Overlap
dissTOM
modTOM_1 = dissTOM[inModule_1, inModule_1];
modTOM_1
modules_1
modProbes_1
dimnames(modTOM_1) = list(modProbes_1, modProbes_1)
# Export the network into edge and node list files Cytoscape can read
cyt2 = exportNetworkToCytoscape(modTOM_1,
                                edgeFile = paste("./",name,"/CytoscapeInput-edges-", paste(modules_1, collapse="-"), ".txt", sep=""),
                                nodeFile = paste("./",name,"/CytoscapeInput-nodes-", paste(modules_1, collapse="-"), ".txt", sep=""),
                                weighted = TRUE,
                                threshold = 0.8,
                                #nodeNames = modProbes_1,
                                #altNodeNames = modGenes_1,
                                nodeAttr = mergedColors[inModule_1]);

