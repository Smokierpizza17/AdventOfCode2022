with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\3_RucksackReorganization\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def getPriority(symbol):
    if symbol.islower():
        return ord(symbol) - 96
    elif symbol.isupper():
        return ord(symbol) - 38

prioSum = 0
for line1, line2, line3 in zip(taskInput[::3], taskInput[1::3], taskInput[2::3]):
    intersection = list(set(line1).intersection(line2).intersection(line3))[0]
    prioSum += getPriority(intersection)

print(prioSum)