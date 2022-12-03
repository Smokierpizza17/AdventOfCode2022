with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\3_RucksackReorganization\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def getPriority(symbol):
    if symbol.islower():
        return ord(symbol) - 96
    elif symbol.isupper():
        return ord(symbol) - 38

prioSum = 0
for line in taskInput:
    splitIndex = len(line) // 2
    compartment1 = list(line[:splitIndex])
    compartment2 = list(line[splitIndex:])
    intersection = list(set(compartment1).intersection(compartment2))[0]
    prioSum += getPriority(intersection)

print(prioSum)