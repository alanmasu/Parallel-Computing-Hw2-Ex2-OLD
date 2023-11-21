import os
import shutil
from datetime import datetime
import os.path

def copyFile(src, dest):
    try:
        if(os.path.isfile(dest)):
            os.remove(dest)
            print("Removed old file")
        shutil.copyfile(src, dest)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        return "error"
    return "success"

#Create directory on ./results/<new_dir>
def createFolder ():
    date = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

    ##saving the date on a file
    if not os.path.isfile("./results/date.csv"):
        print("Date file not exist")
        file = open("./results/date.csv", "w")
        file.write(date)
        file.close()
    else:
        file = open("./results/date.csv", "r")
        line = file.readline()
        if line == "":
            file.close()
            file = open("./results/date.csv", "w")
            file.write(date)
            print("Date file empty")
        else:
            date = line.strip('\n \r')
            print("Date restored")
        file.close()

    print("Date: " + date)

    if os.path.exists("./results/run-" + date):
        print("Directory already exists")
        if copyFile(r"./results/infoFile.csv", r"./results/run-" + date + "/infoFile.csv") == "error":
            return "error on copy infoFile"
        if copyFile(r"./results/matTFile.csv", r"./results/run-" + date + "/matTFile.csv") == "error":
            return "error on copy matTFile"
        if copyFile(r"./results/matBlockTFile.csv", r"./results/run-" + date + "/matBlockTFile.csv") == "error":
            return "error on copy matBlockTFile"
    else:
        try:  
            os.mkdir("./results/run-" + date)
            print("Directory created")
            if copyFile(r"./results/infoFile.csv", r"./results/run-" + date + "/infoFile.csv") == "error":
                return "error on copy infoFile"
            if copyFile(r"./results/matTFile.csv", r"./results/run-" + date + "/matTFile.csv") == "error":
                return "error on copy matTFile"
            if copyFile(r"./results/matBlockTFile.csv", r"./results/run-" + date + "/matBlockTFile.csv") == "error":
                return "error on copy matBlockTFile"
        except OSError as error:  
            print(error)
            return "error on create directory"
    return "./results/run-" + date