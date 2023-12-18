import os
import glob
import pandas as pd

identifier = "D"

if not os.path.exists('./fpkm/'):
        os.makedirs('./fpkm/')

main1 = pd.DataFrame()
for files in glob.glob("*"+identifier+"*"):
    name = files.split("/")[0]
    name = name.replace("_sorted","")
    file1 = pd.read_csv(files+"/genes.fpkm_tracking",sep='\t')
    #file1 = file1[["gene_id","FPKM"]]
    file1['gene_id'] = file1['gene_id'].astype(str)
    file1 = file1.replace(regex=['gene:',"transcript:"],value="")
    file1.to_csv('./fpkm/'+name+'.csv', sep = ',', index = False)
# file1 =  file1[file1["FPKM"] != 0 & ~file1.duplicated()]
#       print(file1.shape)
    #file1 = file1.rename(columns={"FPKM":name})
    #if main1.empty:
    #    main1 = file1
    #else:
    #    main1 = pd.merge(main1,file1,on="gene_id",how='left')
    #    main1 = main1.drop_duplicates()
    #    print(main1.shape)
#print(main1)
