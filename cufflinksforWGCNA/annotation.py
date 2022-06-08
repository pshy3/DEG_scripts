import pandas as pd
import glob

main = pd.DataFrame()
filenames = []
for fil in glob.glob('./*/genes.fpkm_tracking'):
    filenames.append(fil)

filenames.sort()
print(filenames)
for k in range(len(filenames)):    
    file1 = pd.read_csv(filenames[k],sep='\t')
    file1 = file1[["gene_id","gene_short_name"]]
    file1 = file1.replace(regex=['gene:'],value="")
    print(main.empty)
    if main.empty:
        main = file1
    else:
        main = pd.merge(main,file1,on=["gene_id","gene_short_name"],how='left')
        main.drop_duplicates(subset = "gene_id",keep=False,inplace=True)
        print(main)

main.to_csv('annotation.txt', sep = '\t', index = False)



