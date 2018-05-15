# USAGE python melt.py -f/--file [PATH_TO_FILE] -m/--memSize [MEMORY_SIZE]


# Import packages
import argparse
import precompile as pc
import getch

# Setup our arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required = True, help = "Path to the .bf file")
ap.add_argument("-m","--memSize", help = "Size of memory to use (default: 30000)")
ap.add_argument("-d","--debug",help = "Enables debug with a memLength output (default: 8)")
ap.add_argument("-t","--tinify", help = "Retunrs the tinified version of your code")
args = vars(ap.parse_args())

if args["memSize"] is None:
    memSize = 30000
else:
    memSize = int(args["memSize"])

memberDict = {
    "memList" : [0] * memSize,
    "memPointer":0,
    "instructPointer":0
}

def dumpMem(memList):
    for mem in memList:
        print(str(mem) + ",", end="")
    print()


def parseCommands(instructions,memberDict):
    scoopedInst = ""
    scoop = False
    depth = 0

    for char in instructions:
        if scoop:
            if char == "]":
                if depth != 0:
                    depth-=1
                    scoopedInst+=char
                    continue
                scoop = False

                loopPointer = memberDict["memPointer"]
                while (int(memberDict["memList"][loopPointer]) != 0):
                    memberDict = parseCommands(scoopedInst,memberDict)
                    loopPointer = memberDict["memPointer"]

                scoopedInst=""
            elif char == "[":
                depth+=1
                scoopedInst+=char
            else:
                # print(char,end="")
                scoopedInst+=char
        else:
            if char == ">":
                memberDict["memPointer"]+=1
            elif char == "<":
                memberDict["memPointer"]-=1
            elif char == "+":
                memberDict["memList"][memberDict["memPointer"]]+=1
            elif char == "-":
                memberDict["memList"][memberDict["memPointer"]]-=1
            elif char == ".":
                print(chr(memberDict["memList"][memberDict["memPointer"]]),end='')
            elif char == "[":
                scoop = True
            elif char == ",":
                memberDict["memList"][memberDict["memPointer"]] = ord(getch.getch())
            #print(char,end="")


    return memberDict

def printdebug(length,memPointer):
    print()
    print("==========DEBUG START==========");
    for x in range(int(length)):
        if memPointer==x:
            endStr = "<"
        else:
            endStr = ""
        print("["+str(memberDict["memList"][x])+"]",end=endStr)
        if x is not int(length)-1:
            print(",",end="")



with open(args["file"]) as f:
    instructions = pc.preCompile(f)
if args["tinify"] is not None:
    print(instructions)
    exit()
parseCommands(instructions,memberDict)

if args["debug"] is not None:
    printdebug(args["debug"],memberDict["memPointer"])
