import os 

if not os.path.exists('./miRge/'):
    os.makedirs('./miRge/')

str1 = "nohup miRge3.0 -s samples.txt -db miRBase -lib /home/pshy3/share/dataset/RosenfeldC_29_SOL/raw_files/miRge3_Lib/ -o miRge/ -cpu 40 -on human -rr -dex -mdt samples.csv > miRge/log_mirge.out 2>&1 &"
print(str1+"\n")
os.system (str1)
