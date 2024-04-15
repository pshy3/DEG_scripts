import glob
import os

reference_file = "/scratch/SHARE/dataset/RosenfeldC_29_SOL/reference/miRBase/hsa.gff3"
substring = "*.bam"
splitting = "_S"

for filename in glob.glob(substring):
    op_file = filename.split(splitting)[0]
    if not os.path.exists('./counts-miRBase/'):
        os.makedirs('./counts-miRBase/')

    if not os.path.exists('./counts-miRBase/count_logs/'):
        os.makedirs('./counts-miRBase/count_logs/')

        #str1 = "(hisat2 -p 4 --dta -x "+line[2]+" -1 "+line[0]+" -2 "+line[1]+" -S sam_output/"+op_file+".sam) >& sam_output/align_"+op_file+"_log.txt &"
        #str1 = "(samtools sort -@ 4 -o sorted_bams/"+op_file+"_sorted.bam "+line[0]+") >& log_sort_"+op_file+" &"
    str1 = "nohup htseq-count -n 20 "+filename+" "+reference_file+" -t gene -f bam -c counts-miRBase/"+op_file+"_count.csv > counts-miRBase/count_logs/log_"+op_file+"_count.txt 2>&1 &"
        #str2 = "ln -s "+line[4]+" "+line[5] -i gene_id
        
    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)        
