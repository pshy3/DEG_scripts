#collect cuffdiff files into one folder with their comparison names as their filenames
import glob
import pandas as pd
import numpy as np
import math
import os 

identifier = "_vs_"

diff = []

if not os.path.exists('./cuffdiff_files/'):
    os.makedirs('./cuffdiff_files/')


# glob for getting all the files in the directory
for filenames in glob.glob("*"+identifier+"*/"):
    print(filenames)
    fil = filenames.split("/")[0]
    diff.append(fil)

print(diff)

for i in range(len(diff)):
    main = pd.read_csv( diff[i] +'/gene_exp.diff',sep='\t')
    main = main.replace(regex=['gene:'],value="")
    main = main.replace(regex=['transcript:'],value="")
    main.astype({'log2(fold_change)': 'float64'}).dtypes
    #print("+ and - inf before: ")
    #print(len(main['log2(fold_change)'][main['log2(fold_change)'].isin([-np.inf, np.inf])]))
    #for row in main[main['log2(fold_change)'] == -np.inf].itertuples():
    #    main
    #    break
    #print(main.head())
    main.loc[main['log2(fold_change)'] == -np.inf,'log2(fold_change)'] = np.log2((main['value_2'][main['log2(fold_change)'] == -np.inf]+1)/(main['value_1'][main['log2(fold_change)'] == -np.inf]+1))
    main.loc[main['log2(fold_change)'] == np.inf,'log2(fold_change)'] = np.log2((main['value_2'][main['log2(fold_change)'] == np.inf]+1)/(main['value_1'][main['log2(fold_change)'] == np.inf]+1))
    #print(main.head())
    main['log2(fold_change)'] = main['log2(fold_change)'].fillna(0)
    
    #print(diff[i])
    #print("+ and - inf after: ")
    #print(len(main['log2(fold_change)'][main['log2(fold_change)'].isin([-np.inf, np.inf])]))
#main['log2(fold_change)'] = main['log2(fold_change)'](main['log2(fold_change)'] == -np.inf)math.log2(main['value_1']+1/main['value_2']+1),inplace=True)
    #main['log2(fold_change)'].replace(np.inf,(math.log2(main['value_1'] + 1 / main['value_2'] + 1)),inplace=True)
    #main['log2(fold_change)'].replace(np.inf,0.00000001,inplace=True)
    #main['log2(fold_change)'].replace([0.00000001],(main['log2(fold_change)'].max()),inplace=True)
    # print(main.tail())
    main.to_csv("./cuffdiff_files/"+diff[i]+"_gene_exp.csv", sep = ',', index = False)
       

