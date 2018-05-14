import re


def preCompile(file):
    pattern = re.compile('\[|\+|\.|\,|\<|\>|\]|\-')
    instructionSet = ""
    for line in file:
        for char in line:
            if pattern.match(char):
                instructionSet+=char

    return instructionSet
