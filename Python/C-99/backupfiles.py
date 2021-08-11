import os
import shutil

source= "C:/Users/kathi_fhacahv/Desktop/important"
destination= "E:/Python/C-99/backup"

listoffiles = os.listdir(source)
for file in listoffiles:
    shutil.copy(source+'/'+file,destination+'/'+file)
    