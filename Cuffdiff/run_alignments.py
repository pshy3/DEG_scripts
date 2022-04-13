import csv
import os

array=[]
with open("../../scripts/trimmed_file_list.txt",'r') as name_file:
    f_names = csv.reader(name_file,delimiter='\t')
    #print(f_names)
    for line in f_names:
        #print(line)
        array.append(line[0])
        #print(array)

for x in range(0,len(array),2):
    #print(array[x])
    op_file = array[x][0:-25]
    print(op_file)
        ##change --dta-cufflinks to --dta for counts/edgeR/DEseq2
    str1 = "(hisat2 -p 4 --dta-cufflinks -x ../../reference/Mus_musculus.GRCm39.dna.toplevel -1 "+array[x]+" -2 "+array[x+1]+" -S sam_output_cufflinks/"+op_file+".sam) >& sam_output_cufflinks/align_logs/align_"+op_file+"_log.txt &"
        #str1 = "ln -s "+line[2]+" "+line[3]
        #str2 = "ln -s "+line[4]+" "+line[5]
        
    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)        
