import csv
import os

with open("../../../../scripts/sortedbam_list.txt",'r') as name_file:
    f_names = csv.reader(name_file,delimiter='\t')
    for line in f_names:
        op_file = line[0][0:-11]
        #str1 = "(hisat2 -p 4 --dta -x "+line[2]+" -1 "+line[0]+" -2 "+line[1]+" -S sam_output/"+op_file+".sam) >& sam_output/align_"+op_file+"_log.txt &"
        #str1 = "(samtools sort -@ 4 -o sorted_bams/"+op_file+"_sorted.bam "+line[0]+") >& log_sort_"+op_file+" &"
        #str1 = "(htseq-count "+line[0]+" /home/ssz74/scratch/ron_mittler_data/refgenome_soybean/Glycine_max.Glycine_max_v2.1.51.gff3 -t gene -f bam > counts/"+op_file+".count.txt) >& count_logs/log_count_"+op_file+".txt &"
        #str2 = "ln -s "+line[4]+" "+line[5] -i gene_id

	#cufflinks -p 8 -G ".$gene_gtf." sorted_bams_FIXED/".$1."_aligned.bam -o cufflinks_FIXED/".$1.") >& logs_cufflinks_FIXED/log_cuff_".$1." &";

        str1 = "(cufflinks -p 4 -G ../../../../reference/Mus_musculus.GRCm38.102.gff3 "+line[0]+" -o cufflinks/"+op_file+") >& logs_cufflinks/log_cuff_"+op_file+" &"

        
        print(str1+"\n")
        #print(str2+"\n")

        os.system (str1)
        #neos.system (str2)        
