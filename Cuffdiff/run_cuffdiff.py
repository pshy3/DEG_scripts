import csv
import os
import glob
import pandas as pd

reference_file = "../../../reference/Mus_musculus.GRCm39.107.gff3"
comp_file = "../../../scripts/DEG_scripts/Cuffdiff/comp.csv"


comp = pd.read_csv(comp_file)

comp['den'] = ""

for index,row in comp.iterrows():
    #value = []
    value = ""
    print(comp.iloc[index].Reference+"*")
    for filenames in glob.glob(comp.iloc[index].Reference+"*"):
        #value.append(filenames+",")
        if value == "":
            value = filenames
        else:
            value = value + "," + filenames
    comp.at[index,'den'] = value
    
comp['num'] = ""

for index,row in comp.iterrows():
    #value = []
    value = ""
    print(comp.iloc[index].Experiment+"*")
    for filenames in glob.glob(comp.iloc[index].Experiment+"*"):
        #value.append(filenames+",")
        if value == "":
            value = filenames
        else:
            value = value + "," + filenames
    comp.at[index,'num'] = value

#print(comp)
condition = comp['Condition'].unique()

for index,row in comp.iterrows():
    if not os.path.exists('./cuffdiff/'+comp.iloc[index].Condition+'/logs_cuffdiff/'):
        os.makedirs('./cuffdiff/'+comp.iloc[index].Condition+'/logs_cuffdiff/')

#    if not os.path.exists('./counts/count_logs/'):
#        os.makedirs('./counts/count_logs/')

    #if comp.iloc[index].Condition != condition[0]:
    str1 = "(cuffdiff -p 2 -o cuffdiff/"+comp.iloc[index].Condition+"/"+comp.iloc[index].Experiment+"_vs_"+comp.iloc[index].Reference+" "+reference_file+" "+comp.iloc[index].den+" "+comp.iloc[index].num+") >& cuffdiff/"+comp.iloc[index].Condition+"/logs_cuffdiff/log_"+comp.iloc[index].Experiment+"_vs_"+comp.iloc[index].Reference+".txt &"
        
    print(str1+"\n")
        
   # os.system(str1)

