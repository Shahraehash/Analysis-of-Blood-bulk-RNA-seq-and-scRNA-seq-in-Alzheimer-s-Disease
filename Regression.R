library(Seurat)
library(dplyr)

seurat_obj <- readRDS("/Users/raehash/Desktop/CMU/CMU Masters Year/Fall Semester/02-719 Genomics and Epigenetics of the Brain/Grad_Project/LefKolPBMC2024_seu_DE.rds")
DefaultAssay(seurat_obj) = "RNA"

agg_expr <- AggregateExpression(seurat_obj, group.by = "orig.ident")
write.csv(agg_expr$RNA, "pseudo_bulk.csv", row.names = TRUE)

write.csv(seurat_obj@meta.data, "metadata_seurat.csv", row.names = TRUE)

