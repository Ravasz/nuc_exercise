'''
Created on 19 Feb 2022

@author: mate

read in SAM file and output coverage in WIG format
'''

minLoc = 9999999999
maxLoc = 0
bedL = []
with open("chr11.bed") as inBedF:
  for inLine in inBedF:
    inL = inLine.rstrip().split("\t")
    startNum = int(inL[1])
    endNum = int(inL[2])
    if startNum < minLoc: minLoc = startNum
    if endNum > maxLoc: maxLoc = endNum
    bedL.append([startNum, endNum])

print("start: " + str(minLoc))
print("end: " + str(maxLoc))
print("number of reads: " + str(len(bedL)))

covL = [0] * (maxLoc + 1)

loopCount = 0
for posItem in bedL:
  # track progress if need be
  loopCount += 1
  if loopCount % 10000 == 0: print(".", end = "", flush = True)
  if loopCount % 1000000 == 0: print("") 
  
  # count coverage
  for countNum in range(posItem[0], posItem[1] + 1):
    covL[countNum] += 1

print("\nWriting results to disk. This may take a while...")

# write out coverage to result file
with open("chr11.wig", "w") as outWigF:
  outWigF.write("variableStep\tchrom=chr11\n")
  for i in range(minLoc, maxLoc + 1): outWigF.write(str(i) + "\t" + str(covL[i]) + "\n") 

print("All done.")

  