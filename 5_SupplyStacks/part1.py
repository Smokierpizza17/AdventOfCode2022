import re

with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\5_SupplyStacks\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

crateStacks = {}

class CrateStack():
    def __init__(self, name):
        crateStacks[name] = self
        self.crates = list()
    def moveCrateTo(self, targetStack):
        targetStack.takeCrate(self.crates[-1])
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
    for _ in range(int(count)):
        crateStacks[str(fromStack)].moveCrateTo(crateStacks[str(toStack)])

topCrates = []
for stack in crateStacks.values():
    topCrates.append(stack.crates[-1])
print("".join(topCrates))