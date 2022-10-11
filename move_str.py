import os
from os import walk
from pathlib import Path
import shutil

# Directories you need to scan
pathToScan = ['C:\\Utils\\dev\\plex-subtitles\\test\\str']

# Plex & Str couple
languages = [['en', 'English.str'], ['fr', 'French.str']]
video_exts = ['.mp4', '.mkv']
SUB_CHECK = "Sub"

def getFilesize(file):
    size = os.path.getsize(file)
    return size

for path in pathToScan:
    print("Scan " + path + " path")
    for root, dirs, files in walk(path):
        for (file) in files:
            fileLang = file.split("_")[-1]
            strFile = os.path.join(root, file)
            sub  = strFile.split("\\")[-3]
            name = strFile.split("\\")[-2]

            for lang in languages: 
                if fileLang == lang[1] and SUB_CHECK == sub :
                    
                    # print("IF Language.str file found in " + strFile + " " + str() +" o" )

                    vid_root = os.path.dirname(os.path.dirname(root))
                    targetStrFile = os.path.join(vid_root, name + "." + lang[0] + ".str")
                    
                    fileDir = strFile
                    # print("  ROOT\\SUB\\NAME:" + str(vid_root) + "|" + sub + "|" + name )
                    if os.path.isfile(targetStrFile):
                        # print("    str file already here!: " + targetStrFile + " ? is getFilesize" + strFile + " > " + targetStrFile )
                        if (getFilesize(strFile) > getFilesize(targetStrFile)):
                            print("        OK IF str file > EXISTING str file -> Copy & Rename : " + strFile + " -> " + targetStrFile)
                            shutil.copy(strFile, targetStrFile)
                    else:
                        # print("    else NO str file already here!: " + targetStrFile)
                        
                        for ext in video_exts:
                            vid_file = os.path.join(vid_root, name + ext)
                            # print("    ? isfile:" + vid_file)
                            if (os.path.isfile(vid_file)):
                                print("      OK " + vid_file + " exists -> Copy & Rename : " + strFile + " -> " + targetStrFile)
                                shutil.copy(strFile, targetStrFile)

                    # if () #If ROOT / NAME.str exists


#  IF this str size > root str file
#    Copy & Rename
#  ELSE
#    If ROOT / NAME.mkv|mp4|?? exists
#      Copy & Rename