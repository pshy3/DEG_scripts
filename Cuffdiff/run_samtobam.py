import os
import glob

substring = "*.sam"

if not os.path.exists('./bam_output_cufflinks/'):
    os.makedirs('./bam_output_cufflinks/')

if not os.path.exists('./bam_output_cufflinks/align_logs/'):
    os.makedirs('./bam_output_cufflinks/align_logs/')

for filenames in glob.glob(substring):
    op_file = filenames.split(".sam")[0]
    print(filenames)
        ##change --dta-cufflinks to --dta for counts/edgeR/DEseq2
    str1 = "(samtools view -h -bS "+filenames+" -o bam_output_cufflinks/"+op_file+".bam) >& bam_output_cufflinks/align_logs/align_"+op_file+"_log.txt &"
        #str1 = "ln -s "+line[2]+" "+line[3]
        #str2 = "ln -s "+line[4]+" "+line[5]

    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)
