import glob
import os

reference_file = "/home/pshy3/share/dataset/RosenfeldC_29_SOL/reference/ensemble/Homo_sapiens.GRCh38.111.chr.gtf"
substring = "*sortedByCoord.out.bam"
splitting = "_L004Aligned.sortedByCoord.out"

for filename in glob.glob(substring):
    op_file = filename.split(splitting)[0]
    if not os.path.exists('./counts/'):
        os.makedirs('./counts/')

    if not os.path.exists('./counts/count_logs/'):
        os.makedirs('./counts/count_logs/')

        #str1 = "(hisat2 -p 4 --dta -x "+line[2]+" -1 "+line[0]+" -2 "+line[1]+" -S sam_output/"+op_file+".sam) >& sam_output/align_"+op_file+"_log.txt &"
        #str1 = "(samtools sort -@ 4 -o sorted_bams/"+op_file+"_sorted.bam "+line[0]+") >& log_sort_"+op_file+" &"
    str1 = "n(htseq-count "+filename+" "+reference_file+" -t gene -f bam > counts/count.txt) >& counts/count_logs/log_count.txt &"
        #str2 = "ln -s "+line[4]+" "+line[5] -i gene_id
        
    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)        
