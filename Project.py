import os
import shutil

list = os.listdir('C:/Users/HIBA PC/Desktop/Python/os and shutil')
print(list)

for x in list:
    month = os.path.splitext(x)
    if month[1] == '.txt':
        os.remove(x)
    
for y in list:
    year = os.path.splitext(y)
    if year[1] == '':
        shutil.rmtree(y)
