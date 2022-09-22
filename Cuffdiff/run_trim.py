import csv
import os
import glob


reference_file = "../reference/GRCm39"
substring = "*1_001.fastq.gz"

if not os.path.exists('./trimmed_files/'):
    os.makedirs('./trimmed_files/')

if not os.path.exists('./trimmed_files/trim_logs/'):
    os.makedirs('./trimmed_files/trim_logs/')

for filenames in glob.glob(substring):
    filenames = filenames.split("1_001.fastq.gz")[0]
    print(filenames)
        ##change --dta-cufflinks to --dta for counts/edgeR/DEseq2
    str1 = "(trim_galore --output_dir ./trimmed_files --paired "+filenames+"1_001.fastq.gz "+filenames+"2_001.fastq.gz) >& ./trimmed_files/trim_logs/log_"+filenames+"_trim.txt &"
        #str1 = "ln -s "+line[2]+" "+line[3]
        #str2 = "ln -s "+line[4]+" "+line[5]

    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)




#import csv
#import os

#array=[]
#with open("../scripts/file_names.txt",'r') as name_file:
#    f_names = csv.reader(name_file,delimiter='\t')
#    for line in f_names:
#        array.append(line[0])
        #print(array)

#for x in range(0,len(array),2):
    #print(array[x])
#    op_file = array[x][0:-18]
#    print(op_file)
#    print(array[x],array[x+1])
#    command = "(trim_galore --output_dir "+op_file+" --paired "+array[x]+" "+array[x+1]+") >& log_trim/log_"+op_file+"_trim.txt &"

   # command = "(trim_galore --output_dir trimmed_data_07_117_2021 "+fname") >& log_trim/log_"+fname+"_trim.txt &"
   
    #command = "(srun --mem-per-cpu=32g --time=0-06:00 --partition=BioCompute --job-name="+fname+"_
