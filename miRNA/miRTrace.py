import os 

str1 = "nohup java -Xms8G -Xmx8G -jar /home/pshy3/miniconda3/envs/miRNA/share/mirtrace-1.0.1-1/./mirtrace.jar qc -f -t 10 -s hsa -c samples.txt -o ./mirtrace/. > log_mirtrace.txt 2>&1 &"
print(str1+"\n")
os.system (str1)
