import csv
import os
import glob


#reference_file = "../reference/GRCm39"
substring = "*1_001.fastq.gz"

if not os.path.exists('./fast-mcf-75/'):
    os.makedirs('./fast-mcf-75/')

if not os.path.exists('./fast-mcf-75/trim_logs/'):
    os.makedirs('./fast-mcf-75/trim_logs/')

for filenames in glob.glob(substring):
    filenames = filenames.split("1_001.fastq.gz")[0]
    print(filenames)
    # str1 = "nohup cutadapt -j 6 -q 14 -m 15 --interleaved --poly-a --pair-adapters -a AGATCGGAAGAGC -A NNNAGATCGGAAGAGC -u 3 -o ./cutadapt_trimmed/"+filenames+"1.fastq.gz -p ./cutadapt_trimmed/"+filenames+"2.fastq.gz "+filenames+"1_001.fastq.gz  "+filenames+"2_001.fastq.gz > ./cutadapt_trimmed/trim_logs/log_"+filenames+"trim.txt 2>&1 &"
    str1 = "nohup fastq-mcf -p 30 -k 0 -l 15 adapters.fasta -o ./fast-mcf-75/"+filenames+"1_pair.fastq.gz -o ./fast-mcf-75/"+filenames+"2_pair.fastq.gz "+filenames+"1_001.fastq.gz  "+filenames+"2_001.fastq.gz > ./fast-mcf-75/trim_logs/log_"+filenames+"_pair_trim.txt 2>&1 &"
    # str1 = "nohup cutadapt -j 6 --auto -o ./cutadapt_trimmed/"+filenames+"1_pair.fastq.gz -p ./cutadapt_trimmed/"+filenames+"2_pair.fastq.gz "+filenames+"1_001.fastq.gz  "+filenames+"2_001.fastq.gz > ./cutadapt_trimmed/trim_logs/log_"+filenames+"_pair_trim.txt 2>&1 &"
    # str2 = "nohup cutadapt -j 2 -m 15 -u 3 -a AAAAAAAAAA -o "+filenames+"R2_001.fastq.gz ./trimmed_files/"+filenames+"R2.fastq.gz > ./trimmed_files/trim_logs/log_"+filenames+"R2_trim.txt 2>&1 &"
    # str1 = "nohup fastp --thread 6 -z 4 -q 20 -c -x -p -f 3 -F 3 --adapter_sequence AAAAAAAAAA -i "+filenames+"R1_001.fastq.gz -I "+filenames+"R2_001.fastq.gz  -o ./fastp_trimmed_files/"+filenames+"R1.fastq.gz -O ./fastp_trimmed_files/"+filenames+"R2.fastq.gz --unpaired1 ./fastp_trimmed_files/"+filenames+"R1.unpaired.fl.fastq.gz --unpaired2 ./fastp_trimmed_files/"+filenames+"R2.unpaired.fl.fastq.gz --html ./fastp_trimmed_files/trim_logs/log_"+filenames+"R1.html > ./fastp_trimmed_files/trim_logs/"+filenames+".txt 2>&1 &"
    # str1 = "nohup ~/tools/TrimGalore-0.6.10/trim_galore -o ./trim_galoretrimmed_files/ --paired "+filenames+"R1_001.fastq.gz "+filenames+"R2_001.fastq.gz > ./trim_galore_trimmed_files/trim_logs/log_"+filenames+"trim.txt 2>&1 &"
    # str1 = "nohup flexbar -n 6 -av 20 -ap SHORT -a adapters.fasta --align-log MOD -j -R ./cutadapt_trimmed/"+filenames+"1_pair.fastq.gz -P ./cutadapt_trimmed/"+filenames+"2_pair.fastq.gz -r "+filenames+"1_001.fastq.gz -p "+filenames+"2_001.fastq.gz > ./cutadapt_trimmed/trim_logs/log_"+filenames+"_pair_trim.txt 2>&1 &"
    print(str1+"\n")
    os.system (str1)
    # print(str2+"\n")
    # os.system (str2)
# Seq= 
# "TTTTTTTTTTTTTTTGTTACCTGCACGGCTCCCTTCGCAGATCGGAAGAGCGTGGTGTAGG" | "TTGTTACCTGCACGGCTCCCTTCGCAGATCGGAAGAGCGTGGTGTAGGGAAAGAGGGTGCG" | CCTACACCACGCTCCTTCGATCTGCGAAGGGAGCCGTGCAGGTAACAAAAAAAAAAAAAAAA |GCAGATCGAAGGAGCGTGGTGTAGG
# "GCGAAGGGAGCCGTGCAGGTAACAAAAAAAAAAAAAAAAGATCGGAAGAGCACACGTCTGA" | "AAGGGAGCCGTGCAGGTAAC" | "GTTACCTGCACGGCTCCCTT"
# trim galore = "AGATCGGAAGAGC"
# trim galore rev comp = "GCTCTTCCGATCT"
# trim galore comp = "TCTAGCCTCTCG"
# cats = "GCTCTTCCGATCT"
# cats = "GATCGGAAGAGCACACGTCTG"
# rev_comp cats = "CAGACGTGTGCTCTTCCGATC"
# comp =  "CTAGCCTCTCGTGTGCAGAC"
# illumina truseq = "TGGAATTCTCGGGTGCCAAGG"
# illumina truseq read1 = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"
# illumina truseq read2 = "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"
# qiaseq = "AACTGTAGGCACCATCAAT"
# qiaseq comp = "TTGACATCCGTGGTAGTTA"
# illumina multi = "CTGTCTCTTATACACATCT"
# illumina small rna = "TGGAATTCTCGGGTGCCAAGG"
# tagmentation = "ATGTGTATAAGAGACA"
# nextflex = "TGGAATTCTCGGGTGCCAAGG"
# "AGGCACACAGGG"

# high rep unmatched = "CGACTCTTAGCGGTGGATCACTCGGCTCGTGCGTCGATGAAGAACGCAGCTAGCTGCGAGAATTAATGTGAATTGCAGG"
# umatched = "GGGCAGCGAGACAGCGATGTCGAGCTAATCTCC"
# "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT"
# "GGTCTTATCCTCCTGGTCTCCCCCC"
# "TTTTTTTTTTTTTGTCATCTGCTGTGGCTGTTCTATGAACCACCTTCTTCTTTCTGCGAGCAGTTCCTTTCCCACCAATCGG"
# "CAGCCACAGCAGATGAC"
