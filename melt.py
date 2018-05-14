# Import packages
import argparse

# Setup our arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required = True, help = "Path to the .bf file")
ap.add_argument("-m","--memSize", help = "Size of memory to use (default: )")

args = vars(ap.parse_args())

if args["memSize"] is None:
    memSize = 30000
else:
    memSize = int(args["memSize"])

memList = [0] * memSize
memPointer = 0
scoop = False
scoopedInst = ""

def dumpMem(memList):
    for mem in memList:
        print(str(mem) + ",",end="")

    print()
with open(args["file"]) as f:
    for line in f:
        for char in line:
            if scoop:
                if char == "]":

                    scoop = False
                    loopPointer = memPointer

                    while (int(memList[loopPointer]) > 0):
                        for char in scoopedInst:
                            if char == ">":
                                memPointer+=1
                            elif char == "<":
                                memPointer-=1
                            elif char == "+":
                                memList[memPointer]+=1
                            elif char == "-":
                                memList[memPointer]-=1
                            elif char == ".":
                                print(memList[memPointer])
                                print(chr(memList[memPointer]),end='')
                            elif char == "[":
                                scoop = True

                else:
                    scoopedInst+=char
            else:
                if char == ">":
                    memPointer+=1
                elif char == "<":
                    memPointer-=1
                elif char == "+":
                    memList[memPointer]+=1
                elif char == "-":
                    memList[memPointer]-=1
                elif char == ".":
                    print(chr(memList[memPointer]),end='')
                elif char == "[":
                    scoop = True
