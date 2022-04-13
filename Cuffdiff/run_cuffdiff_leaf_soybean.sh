#!/bin/bash

#module load cufflinks

#q2q1
#ML-CD-WT 1-5 vs ML-WD-WT 2-9
(cuffdiff -o cuffdiff/ML-CD-WT_1-5_vs_ML-WD-WT_2-9 ../../../../reference/Mus_musculus.GRCm38.102.gff3 \
ML-CD-WT-1_sorted.bam,ML-CD-WT-2_sorted.bam,ML-CD-WT-3_sorted.bam,ML-CD-WT-4_sorted.bam,ML-CD-WT-5_sorted.bam \
ML-WD-WT-2_sorted.bam,ML-WD-WT-3_sorted.bam,ML-WD-WT-4_sorted.bam,ML-WD-WT-5_sorted.bam,ML-WD-WT-6_sorted.bam,ML-WD-WT-7_sorted.bam,ML-WD-WT-8_sorted.bam,ML-WD-WT-9_sorted.bam) \
>& logs_cuffdiff/Cuffdiff_ML-CD-WT_1-5_vs_ML-WD-WT_2-9.txt &

#ML-CD-WT 1-5 vs ML-WD-WT 2-5

(cuffdiff -o cuffdiff/ML-CD-WT_1-5_vs_ML-WD-WT_2-5 ../../../../reference/Mus_musculus.GRCm38.102.gff3 \
ML-CD-WT-1_sorted.bam,ML-CD-WT-2_sorted.bam,ML-CD-WT-3_sorted.bam,ML-CD-WT-4_sorted.bam,ML-CD-WT-5_sorted.bam \
ML-WD-WT-2_sorted.bam,ML-WD-WT-3_sorted.bam,ML-WD-WT-4_sorted.bam,ML-WD-WT-5_sorted.bam) \
>& logs_cuffdiff/cuffdiff_ML-CD-WT_1-5_vs_ML-WD-WT_2-5.txt &

#ML-CD-WT 1-3 vs ML-WD-WT 2-3

(cuffdiff -o cuffdiff/ML-CD-WT_1-3_vs_ML-WD-WT_2-3 ../../../../reference/Mus_musculus.GRCm38.102.gff3 \
ML-CD-WT-1_sorted.bam,ML-CD-WT-2_sorted.bam,ML-CD-WT-3_sorted.bam \
ML-WD-WT-2_sorted.bam,ML-WD-WT-3_sorted.bam) \
>& logs_cuffdiff/cuffdiff_ML-CD-WT_1-3_vs_ML-WD-WT_2-3.txt &

#ML-WD-WT 2-5 vs. ML-WD-WT 6-9

(cuffdiff -o cuffdiff/ML-WD-WT_2-5_vs_ML-WD-WT_6-9 ../../../../reference/Mus_musculus.GRCm38.102.gff3 \
ML-WD-WT-2_sorted.bam,ML-WD-WT-3_sorted.bam,ML-WD-WT-4_sorted.bam,ML-WD-WT-5_sorted.bam \
ML-WD-WT-6_sorted.bam,ML-WD-WT-7_sorted.bam,ML-WD-WT-8_sorted.bam,ML-WD-WT-9_sorted.bam) \
>& logs_cuffdiff/cuffdiff_ML-WD-WT_2-5_vs_ML-WD-WT_6-9.txt &

#ML-WD-WT 2-3 vs. ML-WD-WT 6-8

(cuffdiff -o cuffdiff/ML-WD-WT_2-3_vs_ML-WD-WT_6-8 ../../../../reference/Mus_musculus.GRCm38.102.gff3 \
ML-WD-WT-2_sorted.bam,ML-WD-WT-3_sorted.bam \
ML-WD-WT-6_sorted.bam,ML-WD-WT-7_sorted.bam,ML-WD-WT-8_sorted.bam,ML-WD-WT-9_sorted.bam) \
>& logs_cuffdiff/cuffdiff_ML-WD-WT_2-3_vs_ML-WD-WT_6-8.txt &
