'''
Created on 19 Feb 2022

@author: mate

convert the given SAM file to BED, with only chrom, start, and stop
'''

with open("/home/mate/code/nucleome/chr11.sam") as inSamF, open("chr11.bed", "w") as outBedF:
  for inLine in inSamF:
    inL = inLine.rstrip().split("\t")
    outBedF.write(inL[2] + "\t" + str(int(inL[3]) - 1) + "\t" + str(int(inL[3]) - 1 + len(inL[9])) + "\n")
    
