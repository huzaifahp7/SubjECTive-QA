import os
import pandas as pd
count1 = 0
count2 = 0
dir1 = "/Users/hp/Desktop/SubjECTive-QA/all_annotated"
dir2 = "/Users/hp/Desktop/SubjECTive-QA/manual_annotations"

file = "/Users/hp/Desktop/SubjECTive-QA/final_dataset.csv"
df = pd.read_csv(file)
print(len(df))

for file in os.listdir(dir1):
    count1 += 1
for file in os.listdir(dir2):
    count2 +=1
    
    
print(count1)
print(count2)