import os
import glob
#from pathlib import Path

substring = "*.sam"
splitting = ".sam"

if not os.path.exists('./sorted_bams/'):
    os.makedirs('./sorted_bams/')

if not os.path.exists('./sorted_bams/sorting_logs/'):
    os.makedirs('./sorted_bams/sorting_logs/')

for filenames in glob.glob(substring):
    op_file =  filenames.split(splitting)[0] 
    #print(op_file)
    #if not os.path.exists('./sorted_bams/'+op_file+'_sorted.bam'):
    #    myfile = Path('./sorted_bams/'+op_file+'_sorted.bam')
    #    myfile.touch(exist_ok=True)
        #str1 = "(hisat2 -p 4 --dta -x "+line[2]+" -1 "+line[0]+" -2 "+line[1]+" -S sam_output/"+op_file+".sam) >& sam_output/align_"+op_file+"_log.txt &"
    str1 = "(samtools sort -@ 2 -T "+op_file+" -o sorted_bams/"+op_file+"_sorted.bam "+filenames+") >& sorted_bams/sorting_logs/log_sort_"+op_file+".txt &"
        #str2 = "ln -s "+line[4]+" "+line[5]
        #sorted_bams/sorting_logs/
    print(str1+"\n")
        #print(str2+"\n")
    #print("running")
    os.system (str1)
        #os.system (str2)        
