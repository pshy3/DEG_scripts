import csv
import os
import glob


reference_file = "../reference/GRCh38"
substring = "*1_val_1.fq.gz"

if not os.path.exists('../sam_output_cufflinks/'):
    os.makedirs('../sam_output_cufflinks/')

if not os.path.exists('../sam_output_cufflinks/align_logs/'):
    os.makedirs('../sam_output_cufflinks/align_logs/')

for filenames in glob.glob(substring):
    filenames = filenames.split("1_val_1.fq.gz")[0]
    print(filenames)
        ##change --dta-cufflinks to --dta for counts/edgeR/DEseq2
    str1 = "nohup hisat2 -p 4 -t --dta-cufflinks -x "+reference_file+" -1 "+filenames+"1_val_1.fq.gz"+" -2 "+filenames+"2_val_2.fq.gz -S ../sam_output_cufflinks/"+filenames+".sam > ../sam_output_cufflinks/align_logs/align_"+filenames+"_log.txt 2>&1 &"
        #str1 = "ln -s "+line[2]+" "+line[3]
        #str2 = "ln -s "+line[4]+" "+line[5]

    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)
