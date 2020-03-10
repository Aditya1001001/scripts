''' It’s often a good idea to first run your program with rmdir(),unlink(),rmtree() calls commented out 
and with print() calls added to show the files that would be deleted. '''


import os
import shutil

PATH = "C:\\Windows\Temp"


def emptyTemp(path, c=0, initial=True):
    if initial:
        os.chdir(path)
    for folderName, subfolders, filenames in os.walk('.'):
        for subfolder in subfolders:
            try:
                c += 1
                os.rmdir("\\".join([path, subfolder]))
            except:
                try:
                    c += 1
                    shutil.rmtree("\\".join([path, subfolder]))
                except:
                    continue
                # emptyTemp("\\".join([path,subfolder]), c, False)

        for filename in filenames:
            try:
                c += 1
                os.unlink("\\".join([path, filename]))
                print("\\".join([path, filename]))
            except:
                continue

    print(c)


emptyTemp(PATH)
