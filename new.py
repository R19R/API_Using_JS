fileA = open("C:/Users/LENOVO/Downloads/fileA.txt", "r")
fileB = open("C:/Users/LENOVO/Downloads/fileB.txt", "r")

fileA_list = [x.strip() for x in fileA]
fileB_list = [x.strip() for x in fileB]        

fileA_and_fileB = [x for x in fileA_list and fileB_list]
print(fileA_and_fileB)

fileAOnly = [x for x in fileA_list if x not in fileB_list]
print(fileAOnly)

fileBOnly = [x for x in fileB_list if x not in fileA_list]
print(fileBOnly)


fileA.close()
fileB.close()