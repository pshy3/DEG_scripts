import json
import csv
import os
import glob

# Read the configuration file
with open('config.json', 'r') as f:
    config = json.load(f)

# Access the configuration values
substring = config['General']['Substring']
threads = config['General']['Threads']
reference_link = config['General']['Reference_Link']
output_folder = config['General']['Output_Dir']

def folder_structure():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    if not os.path.exists(output_folder+"/trimmed_files/"):
        os.makedirs(output_folder+"/trimmed_files/")
        
    if not os.path.exists(output_folder+"/trimmed_files/trim_logs/"):
        os.makedirs(output_folder+"/trimmed_files/trim_logs/")
    
    if not os.path.exists(output_folder+"/sam_output_cufflinks/"):
        os.makedirs(output_folder+"/sam_output_cufflinks/")
        
    if not os.path.exists(output_folder+"/sam_output_cufflinks/align_logs/"):
        os.makedirs(output_folder+"/sam_output_cufflinks/align_logs/")
        
    if not os.path.exists(output_folder+"/cufflinks_output/"):
        os.makedirs(output_folder+"/cufflinks_output/")
        
    if not os.path.exists(output_folder+"/cufflinks_output/cufflinks_logs/"):
        os.makedirs(output_folder+"/cufflinks_output/cufflinks_logs/")
        
    if not os.path.exists(output_folder+"/cuffdiff_output/"):
        os.makedirs(output_folder+"/cuffdiff_output/")
    
    if not os.path.exists(output_folder+"/reference/"):   
        os.makedirs(output_folder+"/reference/")   

def trim_files():
    for filenames in glob.glob(substring):
        filenames = filenames.split("")[0]
        print(filenames)
        str1 = "(trim_galore --output_dir ./trimmed_files --paired "+filenames+"1_001.fastq.gz "+filenames+"2_001.fastq.gz) >& ./trimmed_files/trim_logs/log_"+filenames+"_trim.txt &"
        print(str1+"\n")
        os.system (str1)

def sam_output():
    reference_file = "../reference/GRCm39"
    substring = "*_L004_R1_001_val_1.fq.gz"
    
    for filenames in glob.glob(substring):
        filenames = filenames.split("_L004_R1_001_val_1.fq.gz")[0]
        print(filenames)
        str1 = "(hisat2 -p 1 --dta-cufflinks -x "+reference_file+" -1 "+filenames+"_L004_R1_001_val_1.fq.gz"+" -2 "+filenames+"_L004_R2_001_val_2.fq.gz -S sam_output_cufflinks/"+filenames+".sam) >& sam_output_cufflinks/align_logs/align_"+filenames+"_log.txt &"
        print(str1+"\n")
        os.system (str1)

# Call the functions
folder_structure()
trim_files()
sam_output()