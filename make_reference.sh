#!/bin/bash

# Variables

working_dir="/data/pshy3/dr_pawan"
raw_dir="/data/pshy3/dr_pawan/raw_files"
file_identifier_1="1.fq.gz"
cores=20

# Code

# Setup Environment
conda init bash
conda activate rna-seq


# Create Index

# Check if the directory exists
if [ -d "$working_dir/reference" ]; then
    echo "File exists: $file/reference"
else
    mkdir "$working_dir/reference"
fi

cd "$working_dir/reference"

wget -c "https://ftp.ensembl.org/pub/release-111/fasta/homo_sapiens/dna_index/Homo_sapiens.GRCh38.dna.toplevel.fa.gz"
wget -c "https://ftp.ensembl.org/pub/release-111/gtf/homo_sapiens/Homo_sapiens.GRCh38.111.gtf.gz"

gunzip *.gz

hisat2-build -p 20 *.fa GRCh38

# cd ../

# Trimming 

# Check if the directory exists
# if [ -d "$working_dir/trimmed_files" ]; then
#     echo "Directory exists: $working_dir/trimmed_files"
# else
#     mkdir "$working_dir/trimmed_files"
#     mkdir "$working_dir/trimmed_files/trim_logs"
# fi
# set -f
# for file in "$raw_dir/*$file_identifier_1"; do
#     set +f 
#     echo $file
#     if [[ $file_identifier_1 == "1"* ]]; then
#         file_identifier_2="2${filename_identifier_1:1}"
#         filename="${file//$file_identifier_1/}"
#         # echo $filename
#         echo "nohup trim_galore --output_dir $working_dir/trimmed_files --paired $filename$file_identifier_1 $filename$file_identifier_2 > $working_dir/trimmed_files/trim_logs/log_$filename_trim.txt 2>&1 &"
#     else
#         filename="${file/$file_identifier_1/}"
#         echo "nohup trim_galore --output_dir $working_dir/trimmed_files $filename$file_identifier_1 > $working_dir/trimmed_files/trim_logs/log_"+filenames+"_trim.txt 2>&1 &"
#     fi
#     set -f
# done
