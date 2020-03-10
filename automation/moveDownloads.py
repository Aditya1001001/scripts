import os
import shutil

PATH = "C:\\Users\Lucif\Downloads"
os.chdir(PATH)
for folderName, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename[-7:] == 'torrent':
            os.unlink("\\".join([PATH, filename]))
            print("\\".join([PATH, filename]))
# for filename in Path.home().glob('*.torrent'):
#     print(filename)