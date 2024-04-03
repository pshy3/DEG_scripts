import os 

str1 = "nohup miRge3.0 -s samples.txt -db miRBase -lib /home/pshy3/share/dataset/RosenfeldC_29_SOL/raw_files/miRge3_Lib/ -o miRge/ -cpu 30 -on human -spl -m 15 -p cats> miRge/log_mirge.out 2>&1 &"
print(str1+"\n")
os.system (str1)
