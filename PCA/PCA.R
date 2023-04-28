library(ggfortify)
library(data.table)
library(ggrepel)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
df <- read.csv('counts.csv')
df3 <- df[8:16]
df2 <- transpose(df[8:16])
df2[colnames(df2)] <- lapply(df2[colnames(df2)],as.numeric)
info <- read.csv('Info.csv')
pca_res <- prcomp(df2, center = TRUE, retx = TRUE, scale. = FALSE)
inf <- info[-c(1:5,15:18),]
inf <- info
autoplot(pca_res, data = inf, colour = 'strain',size = 3, show.legend = FALSE) +
  scale_fill_brewer(palette="Dark2")+
  #geom_point(data = inf, colour = info$?..strain, size = 3)+
  geom_label_repel(aes(label = inf$ï..sample,color = inf$group),  show.legend = FALSE , nudge_y = 0.02, label.padding = 0.5, max.time = 2, max.overlaps = 20, force_pull = 2) +
  theme(legend.title = element_text(size = 10), legend.text=element_text(size=15))

