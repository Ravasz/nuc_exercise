'''
Created on 16 Feb 2022

@author: mate
'''

def exer_file_reader(fname):
  """
  read in a file for this exercise and return it as a list of lists
  """
  mesL = []
  chrOrder = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 
              'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr3', 'chr4', 
              'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY']
  with open("/home/mate/code/nucleome/" + fname) as inMesF:
    next(inMesF)
    for inLine in inMesF:
      curLine = inLine.rstrip().split("\t")[:3]
      curLine[0] = chrOrder.index(curLine[0])
      curLine[1] = int(curLine[1])
      curLine[2] = int(curLine[2])
      curLine.append((curLine[1] + curLine[2]) / 2)
      mesL.append(tuple(curLine))
  print(len(mesL))
  return mesL

def overlap_finder(firstL, secL):
  """
  Find overlapping and non-overlapping sequences in the two genomic location lists.
  This could be rewritten to be much faster with hashed objects.
  """
  firstOverlapSet = set()
  firstOverlapList = []
  secOverlapSet = set()
  loopCount = 0
  for firstI in firstL:
    closestCtr = 100000000000
    foundFlag = False
    endFlag = False
    for secI in secL:
      loopCount += 1
      if loopCount % 100000 == 0: print(".", end = "", flush = True)
      if loopCount % 10000000 == 0: print("")
      if firstI[0] > secI[0]: continue
      if abs(firstI[3] - secI[3]) < abs(closestCtr): closestCtr = firstI[3] - secI[3]
      # check for overlaps
      if secI[1] <= firstI[1] <= secI[2] or secI[1] <= firstI[2] <= secI[2] or firstI[1] <= secI[1] <= firstI[2]:
        firstOverlapSet.add(firstI)
        firstOverlapList.append(firstI + (closestCtr,))
        # if foundFlag: print("two overlaps!")
        secOverlapSet.add(secI)     
        foundFlag = True
        continue
      if firstI[0] < secI[0]: 
        if not foundFlag: firstOverlapList.append(firstI + (closestCtr,))
        endFlag = True
        break
    if not endFlag and not foundFlag: firstOverlapList.append(firstI + (closestCtr,))
  return [firstOverlapSet, secOverlapSet, firstOverlapList]

def output_writer(outSet, fname):
  """
  write a set or list out to a csv file, similar to the exercise input format
  """
  chrOrder = ['chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 
              'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr3', 'chr4', 
              'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY']
  if not isinstance(outSet, list): 
    outL = list(outSet)
    listFlag = False
  else: 
    outL = outSet
    listFlag = True
  with open(fname, "w") as outF:
    if listFlag: outF.write("chr\tstart\tstop\tcentre\tdist\n")
    else: outF.write("chr\tstart\tstop\tcentre\n")
    for outI in outL:
      outF.write(chrOrder[outI[0]] + "\t")
      for outPiece in outI[1:-1]:
        outF.write(str(outPiece) + "\t")
      outF.write(str(outI[-1]) + "\n")

########## script starts here ########################

# read in files
mesL = exer_file_reader("mES.tsv")
terL = exer_file_reader("Ter119.tsv")

# find overlaps
overlapRes = overlap_finder(mesL, terL)
output_writer(overlapRes[0], "mES_overlap.tsv")
output_writer(overlapRes[1], "ter119_overlap.tsv")
output_writer(overlapRes[2], "mES_distances.tsv")

# find unique regions
mesS = set(mesL)
terS = set(terL)
mesUnique = mesS - overlapRes[0]
terUnique = terS - overlapRes[1]
output_writer(mesUnique, "mES_unique.tsv")
output_writer(terUnique, "ter119_unique.tsv")

print("\nAll done.")

