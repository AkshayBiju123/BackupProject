import os
import shutil

source = input('Which file would you like to backup')
destination = input('enter the destination folder')
source = 'source+'/''
destination = 'destination+'/''
list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)