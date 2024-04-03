import csv
import os
import glob


# reference_file = "../../reference/genecode/bowtie_index/GRCh38_bowtie2"
# reference_file = "../../reference/ensemble/GRCh38"
substring = "*_R2_001.fastq.gz"
    
if not os.path.exists('./shortstack_out/'):
    os.makedirs('./shortstack_out/')

if not os.path.exists('./shortstack_out/align_logs/'):
    os.makedirs('./shortstack_out/align_logs/')

for filenames in glob.glob(substring):
    filenames = filenames.split("_R2_001.fastq.gz")[0]
    print(filenames)
        ##change --dta-cufflinks to --dta for counts/edgeR/DEseq2
    # str1 = "nohup hisat2 -p 6 -t --dta -x "+reference_file+" -1 "+filenames+"_R1.fastq.gz -2 "+filenames+"_R2.fastq.gz -S ./cutadapt_sam_output_cufflinks/"+filenames+".sam > ./cutadapt_sam_output_cufflinks/align_logs/align_"+filenames+"_log.txt 2>&1 &"
    str1 = "nohup STAR --runThreadN 8 \
            --genomeDir /home/pshy3/share/dataset/RosenfeldC_29_SOL/reference/genecode/STAR-unannotated/ \
            --sjdbGTFfile /home/pshy3/share/dataset/RosenfeldC_29_SOL/reference/rna-central/homo_sapiens.GRCh38.gtf \
            --readFilesIn `"+filenames+"_R1_001.fastq.gz "+filenames+"_R2_001.fastq.gz`\
            --readFilesCommand zcat \
            --outFileNamePrefix ./star_align_rna_central_new/"+filenames+" \
            --outSAMtype BAM SortedByCoordinate \
            --outFilterMismatchNmax 2 \
            --outFilterMismatchNoverLmax 0.1 \
            --outFilterMultimapNmax 20 \
            --outFilterScoreMin 20 \
            --outFilterScoreMinOverLread 0 \
            --outFilterMatchNminOverLread 0 \
            --outFilterMatchNmin 15 \
            --clip3pAdapterSeq polyA polyA \
            --clip3pAdapterMMp 0.3 0.3 \
            --alignIntronMax 1 \
            --winAnchorMultimapNmax 20 \
            --seedSearchStartLmax 50 \
            --seedPerReadNmax 200 \
            --alignMatesGapMax 5 \
            --outReadsUnmapped Fastx \
            --quantMode TranscriptomeSAM GeneCounts > ./star_align_rna_central_new/align_logs/"+filenames+"_log.out 2>&1 &"
            
            #last used options --outSAMtype BAM SortedByCoordinate --outFilterMismatchNmax 1 --outFilterMismatchNoverLmax 0.05 --outFilterScoreMinOverLread 0 --outFilterMatchNminOverLread 0 --outFilterMatchNmin 15 --clip3pAdapterSeq AGATCGGAAGAGCACACGTCTGAACTCCAGTCA AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT --clip3pAdapterMMp 0.2 0.2 --alignIntronMax 1 --outReadsUnmapped Fastx --quantMode TranscriptomeSAM GeneCounts
    print(str1+"\n")

    os.system (str1)
