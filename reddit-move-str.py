from os import walk
import shutil
import os
pathToScan = ['profit.txt', 'sales.txt', 'sample.txt']


# Absolute pathname of current directory
path = os.path.abspath(os.getcwd())
subsPath = path + "\Subs"

print(path)
print(subsPath)


def getFilesize(path, filename):
    full = path + "\\" + filename
    size = os.path.getsize(full)
    return size
    
fileDict = {}
for (dirpath, dirnames, filenames) in walk(subsPath):
    for (file) in filenames:
        mylang = file.split("_")[-1]
        sub = file.split("_")[0]
 
        newName = dirpath.split("\\")[-1]
        oldPath = dirpath + "\\" + file
        if (mylang == 'English.srt'):
        
            fullPath = path + "\\" + newName + "." + "en.srt"
            currentLargest = fileDict.get(fullPath, -1)
            thisSize = getFilesize(dirpath, file)
            
            if (currentLargest <= thisSize):
                print(oldPath)
                print("\t\t" + fullPath)
                shutil.copy(oldPath, fullPath)