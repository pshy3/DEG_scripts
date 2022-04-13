import csv
import os

array=[]
with open("../scripts/file_names.txt",'r') as name_file:
    f_names = csv.reader(name_file,delimiter='\t')
    for line in f_names:
        array.append(line[0])
        #print(array)

for x in range(0,len(array),2):
    #print(array[x])
    op_file = array[x][0:-18]
    print(op_file)
    print(array[x],array[x+1])
    command = "(trim_galore --output_dir "+op_file+" --paired "+array[x]+" "+array[x+1]+") >& log_trim/log_"+op_file+"_trim.txt &"

   # command = "(trim_galore --output_dir trimmed_data_07_117_2021 "+fname") >& log_trim/log_"+fname+"_trim.txt &"
   
    #command = "(srun --mem-per-cpu=32g --time=0-06:00 --partition=BioCompute --job-name="+fname+"_trim trim_galore 
#--paired "+fname+"_1.fq.gz "+fname+"_2.fq.gz --gzip) >& log_trim/log_"+fname+"_trim.txt &"


    print (command)
    os.system (command)
