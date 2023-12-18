import glob
import os

substring = "*.bam"
splitting = "_sorted.bam"
reference_file = "../../../reference/Mus_musculus.GRCm39.107.gff3"

if not os.path.exists('./cufflinks/'):
    os.makedirs('./cufflinks/')

if not os.path.exists('./cufflinks/logs_cufflinks/'):
    os.makedirs('./cufflinks/logs_cufflinks/')


for filenames in glob.glob(substring):
    op_file = filenames.split(splitting)[0]
#str1 = "(hisat2 -p 4 --dta -x "+line[2]+" -1 "+line[0]+" -2 "+line[1]+" -S sam_output/"+op_file+".sam) >& sam_output/align_"+op_file+"_log.txt &"
        #str1 = "(samtools sort -@ 4 -o sorted_bams/"+op_file+"_sorted.bam "+line[0]+") >& log_sort_"+op_file+" &"
        #str1 = "(htseq-count "+line[0]+" /home/ssz74/scratch/ron_mittler_data/refgenome_soybean/Glycine_max.Glycine_max_v2.1.51.gff3 -t gene -f bam > counts/"+op_file+".count.txt) >& count_logs/log_count_"+op_file+".txt &"
        #str2 = "ln -s "+line[4]+" "+line[5] -i gene_id

	#cufflinks -p 8 -G ".$gene_gtf." sorted_bams_FIXED/".$1."_aligned.bam -o cufflinks_FIXED/".$1.") >& logs_cufflinks_FIXED/log_cuff_".$1." &";

    str1 = "(cufflinks -p 2 -G "+reference_file+" "+filenames+" -o cufflinks/"+op_file+") >& cufflinks/logs_cufflinks/log_"+op_file+".txt &"

        
    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #neos.system (str2)        
