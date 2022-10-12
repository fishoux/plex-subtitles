import os
from os import walk

# Directories you need to scan
pathToScan = ['C:\\Utils\\dev\\plex-subtitles\\test\\mp4']

# Plex & Str couple
tmp_ext = '.qt'
target_ext = '.mp4'

for path in pathToScan: # FOR EACH FOLDERS
    print(r"path" + path)
    for root, dirs, files in walk(path): # FOR EACH SUB FILES

        for (file) in files:
            
            ext = os.path.splitext(file)[1]
            print("file " + ext + " == " + tmp_ext)
            if ext == tmp_ext:
                current = os.path.join(root, file)
                target = os.path.splitext(os.path.join(root, file))[0] + target_ext
                print("Rename : " + current + " -> " + target)
                os.rename(current, target)
