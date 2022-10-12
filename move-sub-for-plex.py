# shared by https://www.reddit.com/user/Saafris/ here https://pastebin.com/pbpJU08R
# DONE: Args & Network disk handeled
# python .\move-sub-for-plex.py '\\SYNOFISH\Documents\TV Shows [VO]\Cyberpunk Edgerunners\Cyberpunk.Edgerunners.S01.JAPANESE.1080p.WEBRip.x265-RARBG' 
# TODO Search for all Movie/TV Show folders
# TODO Apply this script on all Movie/TV Show folders
# TODO Remove all RARBG.txt files

from os import walk
import shutil
import os
import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv[1]))

path = os.path.abspath(sys.argv[1])
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