import csv
import os
import glob
import pandas as pd

reference_file = "../reference/Homo_sapiens.GRCh38.111.gtf"
comp_file = "../DEG_scripts/Cuffdiff/comp.csv"


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
    if not os.path.exists('../cuffdiff/'+comp.iloc[index].Condition+'/logs_cuffdiff/'):
        os.makedirs('../cuffdiff/'+comp.iloc[index].Condition+'/logs_cuffdiff/')

#    if not os.path.exists('./counts/count_logs/'):
#        os.makedirs('./counts/count_logs/')

    # if comp.iloc[index].Condition != condition[1]:
    str1 = "nohup ~/tools/cufflinks-2.2.1.Linux_x86_64/cuffdiff -p 4 -o ../cuffdiff/"+comp.iloc[index].Condition+"/"+comp.iloc[index].Experiment+"_vs_"+comp.iloc[index].Reference+" "+reference_file+" "+comp.iloc[index].den+" "+comp.iloc[index].num+" > ../cuffdiff/"+comp.iloc[index].Condition+"/logs_cuffdiff/log_"+comp.iloc[index].Reference+"_vs_"+comp.iloc[index].Experiment+".txt 2>&1 &"
    
    print(str1+"\n")
        
    os.system(str1)

