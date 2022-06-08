import pandas as pd

first = "ML-CD-WT-"
#first = "ML-WD-WT-"
second = "ML-WD-WT-"
#second = "ML-WD-WT-T-"
fnum = [1, 2, 3]
snum = [1, 2, 3]
diff = "ML-CD-WT_1-3_vs_ML-WD-WT_1-3"

main = pd.read_csv('../cuffdiff_redo/'+ diff +'/gene_exp.diff',sep='\t')
main = main[main['significant'] == 'yes']
main = main["gene_id"]
main = main.replace(regex=['gene:'],value="")
   
for x in range(len(fnum)):
     file1 = pd.read_csv(first+ str(fnum[x]) +"/genes.fpkm_tracking",sep='\t')
     file1 = file1[["gene_id","FPKM"]]
     file1 = file1.replace(regex=['gene:'],value="")
     file1 = file1.rename(columns={"FPKM":first+ str(fnum[x])})
     main = pd.merge(main,file1,on="gene_id",how='left')
     
for y in range(len(snum)):
     file1 = pd.read_csv(second+ str(snum[y]) +"/genes.fpkm_tracking",sep='\t')
     file1 = file1[["gene_id","FPKM"]]
     file1 = file1.replace(regex=['gene:'],value="")
     file1 = file1.rename(columns={"FPKM":second+ str(snum[y])})
     main = pd.merge(main,file1,on="gene_id",how='left')

main.to_csv('./fpkmjoint/'+ diff + '.txt', sep = '\t', index = False)







