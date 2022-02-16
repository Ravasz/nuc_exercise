'''
Created on 16 Feb 2022

@author: mate
'''
from idlelib.run import flush_stdout

# read in mES file
mesL = []
with open("/home/mate/code/nucleome/mES.tsv") as inMesF:
  next(inMesF)
  for inLine in inMesF:
    curLine = inLine.rstrip().split("\t")[:3]
    curLine[1] = int(curLine[1])
    curLine[2] = int(curLine[2])
    mesL.append(tuple(curLine))

# read in Ter file
terL = []
with open("/home/mate/code/nucleome/Ter119.tsv") as inTerF:
  next(inTerF)
  for inLine in inTerF:
    curLine = inLine.rstrip().split("\t")[:3]
    curLine[1] = int(curLine[1])
    curLine[2] = int(curLine[2])
    terL.append(tuple(curLine))
    

# build contigs in each dataset
stopFlag = True
countNum = 0
for mesI in mesL:
  for mesSecI in mesL:
    countNum += 1
    if countNum % 100000 == 0: print(".", end = "", flush = True)
    if countNum % 10000000 == 0: print("")
    if mesI[0] == mesSecI[0]:
      if mesSecI[1] < mesI[1] <= mesSecI[2]:
        endNum = max([mesSecI[2], mesI[2]])
        print(mesI)
        print(mesSecI)

        



# find overlapping contigs (answer 1)

# find non-overlapping contigs (answer 2)

