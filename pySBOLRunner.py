import os
import sys
from sbol import *

file = ""
retrievedfilePath = ""

def main():
    if (len(sys.argv) != 3):
        sys.exit("Please enter the input SBOL file and filepath to place retrieved files")
        
    file = sys.argv[1]
    print(file)
    if(file == ""):
        sys.exit("file field is empty")

    retrievedfilePath = sys.argv[2]
    if(retrievedfilePath == ""):
        sys.exit("filePath field is empty")

    pySBOLRunner(file, retrievedfilePath)

def pySBOLRunner(file, retrievedfilePath):
    doc = sbol.Document()
    doc.read(file) 
    doc.write(retrievedfilePath) 

if __name__ == "__main__":
    main()
