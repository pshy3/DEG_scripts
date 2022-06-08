import pandas as pd
import glob

first = "CD-PTWT-"
second = "CD-PTKO-"
third = "WD-PTKO-"
fourth = "WD-PTWT-"

fnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
snum = [1, 2, 3, 4, 5]
tnum = [1, 2, 3, 4, 5, 6, 7]
foum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#diff = ["ML-CD-WT_1-5_vs_ML-WD-WT_1-9",  "ML-WD-WT_1-9_vs_ML-WD-WT-T_1-4"]

main1 = pd.DataFrame()
diff = []

for filenames in glob.glob("../cuffdiff_output/*m/"):
    print(filenames)
    filenames = filenames.split('/')[2]
    diff.append(filenames)

print(diff)
 
for i in range(len(diff)):
    main = pd.read_csv('../cuffdiff_output/'+ diff[i] +'/gene_exp.diff',sep='\t')
    main = main[((main['log2(fold_change)'] >= 1) | (main['log2(fold_change)'] <= -1)) & (main['q_value'] <= 0.01) & (main['significant'] == 'yes')]
    main = main["gene_id"]
    main = main.replace(regex=['gene:'],value="")
    if main1.empty:
        main1 = main
    else:
        main1 = pd.merge(main1,main,on="gene_id",how='outer')
   
for x in range(len(fnum)):
     file1 = pd.read_csv(first+ str(fnum[x]) +"/" +first+ str(fnum[x]) +"_genes.fpkm_tracking",sep='\t')
     file1 = file1[["gene_id","FPKM"]]
     file1 = file1.replace(regex=['gene:'],value="")
     file1 = file1.rename(columns={"FPKM":first+ str(fnum[x])})
     main1 = pd.merge(main1,file1,on="gene_id",how='left')
print("1 done")     
for y in range(len(snum)):
     file1 = pd.read_csv(second+ str(snum[y]) +"/" +second+ str(snum[y]) +"_genes.fpkm_tracking",sep='\t')
     file1 = file1[["gene_id","FPKM"]]
     file1 = file1.replace(regex=['gene:'],value="")
     file1 = file1.rename(columns={"FPKM":second+ str(snum[y])})
     main1 = pd.merge(main1,file1,on="gene_id",how='left')
print("2 done")
for z in range(len(tnum)):
     file1 = pd.read_csv(third+ str(tnum[z]) +"/"+third+ str(tnum[z])+"_genes.fpkm_tracking",sep='\t')
     file1 = file1[["gene_id","FPKM"]]
     file1 = file1.replace(regex=['gene:'],value="")
     file1 = file1.rename(columns={"FPKM":third+ str(tnum[z])})
     main1 = pd.merge(main1,file1,on="gene_id",how='left')
print("3 done")
for k in range(len(foum)):
     file1 = pd.read_csv(fourth+ str(foum[k]) +"/"+fourth+ str(foum[k])+"_genes.fpkm_tracking",sep='\t')
     file1 = file1[["gene_id","FPKM"]]
     file1 = file1.replace(regex=['gene:'],value="")
     file1 = file1.rename(columns={"FPKM":fourth+ str(foum[k])})
     main1 = pd.merge(main1,file1,on="gene_id",how='left')
print("4 done")
main1.to_csv('./all_fpkm.txt', sep = '\t', index = False)







