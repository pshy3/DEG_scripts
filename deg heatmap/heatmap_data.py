import pandas as pd
import glob
import numpy as np

# PARAMETERS

# unqiue identifier present in all the folder names for getting log fold values
identifier = "m"

# diff is used for collecting all the log values in different files and leave empty for all files
diff = ["CD_PTWT_16m_vs_CD_PTWT_6m","CD_PTWT_18_27m_vs_CD_PTWT_6m","WD_PTWT_16m_vs_WD_PTWT_6m","WD_PTWT_18_27m_vs_WD_PTWT_6m"]
#diff = []

# diff1 is used for getting the deg's involved can be left empty for all output
diff1 = ["CD_PTWT_16m_vs_CD_PTWT_6m","CD_PTWT_18_27m_vs_CD_PTWT_6m","WD_PTWT_18_27m_vs_WD_PTWT_6m"]
hfold1 = 1
lfold1 = -1
qval1 = 0.01

#diff2 is used for getting the deg's with different values than the diff1 if left empty then not used
diff2 = ["./WD_PTWT_16m_vs_WD_PTWT_6m/"]
hfold2 = 1
lfold2 = -1
qval2 = 0.05

# Ouput filename
output = "./WD_and_CD_PTWT_months_log_data.txt"



# CODE

# glob for getting all the files in the directory
if len(diff) == 0:
    for filenames in glob.glob("*"+identifier+"*/"):
        fil = filenames.split("/")[0]
        diff.append(fil)
   

# aggregating all the logfold data
main1 = pd.DataFrame()
for i in range(len(diff)):
    main = pd.read_csv( diff[i] +'/gene_exp.diff',sep='\t')
    main = main[["gene_id","log2(fold_change)"]]
    main = main.replace(regex=['gene:'],value="")
    main = main.replace(regex=['transcript:'],value="")
    main.astype({'log2(fold_change)': 'float64'}).dtypes
    main['log2(fold_change)'].replace(-np.inf,10000,inplace=True)
    main['log2(fold_change)'].replace([10000],(main['log2(fold_change)'].min()),inplace=True)
    main['log2(fold_change)'].replace(np.inf,0.00000001,inplace=True)
    main['log2(fold_change)'].replace([0.00000001],(main['log2(fold_change)'].max()),inplace=True)
    name = diff[i]
    main = main.rename(columns={"log2(fold_change)":name})
    if main1.empty:
        main1 = main
    else:
        main1 = pd.merge(main1,main,on="gene_id",how='outer')


print("Shape of all data: ",main1.shape)

# glob for getting all the files in the diectory for diff1 if left empty
if len(diff1) == 0:
    for filenames in glob.glob("*"+identifier+"*/"):
        fil = filenames.split("/")[0]
        diff1.append(fil)


# removing the diff2 from diff1 if present in diff1
#if len(diff2) != 0:
#    for v in range(len(diff2)):
#        diff1.remove(diff2[v])
#print(diff)

# getting the deg's in the one df named main2
main2 = pd.DataFrame()
for j in range(len(diff1)):
    main = pd.read_csv(diff1[j]+'/gene_exp.diff',sep='\t')
    main = main[((main['log2(fold_change)'] >= hfold1) | (main['log2(fold_change)'] <= lfold1)) & (main['q_value'] <= qval1) & (main['significant'] == 'yes')]
    main = main["gene_id"]
    main = main.replace(regex=['gene:','transcript:'],value="")
    if main2.empty:
        main2 = main
    else:
        main2 = pd.merge(main2,main,on="gene_id",how='outer')

if len(diff2) != 0:
    for j in range(len(diff2)):
        main = pd.read_csv(diff2[j] +'/gene_exp.diff',sep='\t')
        main = main[((main['log2(fold_change)'] >= hfold2) | (main['log2(fold_change)'] <= lfold2)) & (main['q_value'] <= qval2) & (main['significant'] == 'yes')]
        main = main["gene_id"]
        main = main.replace(regex=['gene:','transcript:'],value="")
        if main2.empty:
            main2 = main
        else:
            main2 = pd.merge(main2,main,on="gene_id",how='outer')


# subsetting the deg's list from the all logfold change data
main3 = main1[main1["gene_id"].isin(main2["gene_id"])]
print("Shape of the final dataframe: ",main3.shape)

# File to txt with tab sepreation
main3.to_csv(output, sep = '\t', index = False)







