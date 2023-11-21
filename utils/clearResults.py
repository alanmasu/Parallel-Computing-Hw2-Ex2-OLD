import os

# Delete the files if they exist
if os.path.isfile("results/matTFile.csv"):
    os.remove("results/matTFile.csv")
    print("Removed matTFile.csv")

if os.path.isfile("results/matBlockTFile.csv"):
    os.remove("results/matBlockTFile.csv")
    print("Removed matBlockTFile.csv")

if os.path.isfile("results/infoFile.csv"):  
    os.remove("results/infoFile.csv")
    print("Removed infoFile.csv")

if os.path.isfile("results/dateFile.csv"):
    os.remove("results/dateFile.csv")
    print("Removed dateFile.csv")

if os.path.isfile("a.out"):
    os.remove("a.out")
    print("Removed a.out")

