import configparser
import csv
import os
import glob

# Create a configparser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Access the configuration values
substring = config.get('General', 'Substring')
threads = config.get('General', 'Threads')
reference_link = config.get('General', 'Reference_Link')

def trim_files():

    if not os.path.exists('./trimmed_files/'):
        os.makedirs('./trimmed_files/')

    if not os.path.exists('./trimmed_files/trim_logs/'):
        os.makedirs('./trimmed_files/trim_logs/')

    for filenames in glob.glob(substring):
        filenames = filenames.split("1_001.fastq.gz")[0]
        print(filenames)
        str1 = "(trim_galore --output_dir ./trimmed_files --paired "+filenames+"1_001.fastq.gz "+filenames+"2_001.fastq.gz) >& ./trimmed_files/trim_logs/log_"+filenames+"_trim.txt &"
        print(str1+"\n")
        os.system (str1)

def sam_output():
    reference_file = "../reference/GRCm39"
    substring = "*_L004_R1_001_val_1.fq.gz"

    if not os.path.exists('./sam_output_cufflinks/'):
        os.makedirs('./sam_output_cufflinks/')

    if not os.path.exists('./sam_output_cufflinks/align_logs/'):
        os.makedirs('./sam_output_cufflinks/align_logs/')

    for filenames in glob.glob(substring):
        filenames = filenames.split("_L004_R1_001_val_1.fq.gz")[0]
        print(filenames)
        str1 = "(hisat2 -p 1 --dta-cufflinks -x "+reference_file+" -1 "+filenames+"_L004_R1_001_val_1.fq.gz"+" -2 "+filenames+"_L004_R2_001_val_2.fq.gz -S sam_output_cufflinks/"+filenames+".sam) >& sam_output_cufflinks/align_logs/align_"+filenames+"_log.txt &"
        print(str1+"\n")
        os.system (str1)

# Call the functions
trim_files()
sam_output()