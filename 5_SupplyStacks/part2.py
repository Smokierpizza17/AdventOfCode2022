import re
import sys

with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\5_SupplyStacks\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

crateStacks = {}

def stacksVisualiser():  
    tallestStack = 0
    for stack in crateStacks.values():
        if tallestStack < len(stack.crates):
            tallestStack = len(stack.crates)
    outputLines = []
    for i in range(tallestStack):
        currLine = ""
        for stack in crateStacks.values():
            if i < len(stack.crates):
                currLine += stack.crates[i] + " "
            else:
                currLine += "  "
        outputLines.append(currLine)
    outputLines.reverse()
    outputLines.append("1 2 3 4 5 6 7 8 9")
    print("\n".join(outputLines))

class CrateStack():
    def __init__(self, name):
        crateStacks[name] = self
        self.crates = list()
    def moveCrateTo(self, targetStack):
        targetStack.takeCrate(self.crates[-1])
        self.crates.pop(-1)
    def moveMultipleCrates(self, targetStack, count):
        for crate in self.crates[int(count) * -1:]:
            targetStack.takeCrate(crate)
            self.crates.pop(-1)
    def takeCrate(self, crateStr):
        self.crates.append(crateStr)

lastLineOfStacks = taskInput.index("") - 2  # blank line divides stacks from numbers and instructions
numbersString = taskInput[lastLineOfStacks + 1] 

numbers = [int(i) for i in re.findall(r"\d+", numbersString)]
for i in range(1, max(numbers)+1):
    CrateStack(str(i))

stacksRaw = taskInput[:lastLineOfStacks+1]
stacksRaw.reverse()

for line in stacksRaw:
    for i in range(max(numbers)):
        if 4*i+1 < len(line) and line[4*i+1] != " ":
            stackName = str(i + 1)
            crateStacks[stackName].takeCrate(line[4*i+1])

for line in taskInput[lastLineOfStacks + 3:]:
    count, fromStack, toStack = re.findall(r"\d+", line)
    crateStacks[str(fromStack)].moveMultipleCrates(crateStacks[str(toStack)], count)

topCrates = []
for stack in crateStacks.values():
    topCrates.append(stack.crates[-1])
print("".join(topCrates)) 