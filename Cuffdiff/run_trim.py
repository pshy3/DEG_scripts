import csv
import os
import glob


#reference_file = "../reference/GRCm39"
substring = "*1.fq.gz"

if not os.path.exists('../trimmed_files/'):
    os.makedirs('../trimmed_files/')

if not os.path.exists('../trimmed_files/trim_logs/'):
    os.makedirs('../trimmed_files/trim_logs/')

for filenames in glob.glob(substring):
    filenames = filenames.split("1.fq.gz")[0]
    print(filenames)
        ##change --dta-cufflinks to --dta for counts/edgeR/DEseq2
    str1 = "nohup ~/tools/TrimGalore-0.6.10/trim_galore -o ../trimmed_files/ --paired "+filenames+"1.fq.gz "+filenames+"2.fq.gz > ../trimmed_files/trim_logs/log_"+filenames+"_trim.txt 2>&1 &"
    
        #str1 = "ln -s "+line[2]+" "+line[3]
        #str2 = "ln -s "+line[4]+" "+line[5]

    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)
