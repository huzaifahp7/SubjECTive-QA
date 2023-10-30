import os
count1 = 0
count2 = 0
dir1 = "datasets"
dir2 = "manual_annotations"

for file in os.listdir(dir1):
    count1 += 1
for file in os.listdir(dir2):
    count2 +=1
    
    
print(count1)
print(count2)