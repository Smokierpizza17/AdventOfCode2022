from collections import OrderedDict
import re
import math as maths

ROUNDCOUNT = 20

with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\11_MonkeyInTheMiddle\testInput.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n\n")

def evaluateFunction(funcString, var, sub):
    '''returns result from function funcString with variable var, if var is substituted with sub'''
    return eval(funcString.replace(var, str(sub)))

def reliefFromItem(worryLevel):
    return maths.floor(worryLevel / 3)

def printState(monkeys):
    for monkey in monkeys.values():
        print(f"{monkey.name}: {monkey.worryLevels}")
    print("")

def getMonkeyBusiness(monkeys):
    inspectionCounts = []
    for monkey in monkeys.values():
        inspectionCounts.append(monkey.inspectionCount)
    twoMostActiveCounts = sorted(inspectionCounts)[-2:]
    return twoMostActiveCounts[0] * twoMostActiveCounts[1]


monkeys = {}
class Monkey():
    def __init__(self, name):
        self.name = name
        monkeys[name] = self
        self.worryLevels = []
        self.operation = None
        self.moduloTest = None
        self.ifTrueMonkey = None
        self.ifFalseMonkey = None

        self.inspectionCount = 0
    
    def performTurn(self):
        for workingWorryLevel in self.worryLevels:
            workingWorryLevel = evaluateFunction(self.operation, "old", workingWorryLevel)
            workingWorryLevel = reliefFromItem(workingWorryLevel)
            self.inspectionCount += 1
            if workingWorryLevel % self.moduloTest == 0:  # throw to ifTrueMonkey
                self.ifTrueMonkey.takeWorryLevel(workingWorryLevel)
            else:
                self.ifFalseMonkey.takeWorryLevel(workingWorryLevel)
        self.worryLevels = []
    
    def takeWorryLevel(self, worryLevel):
        self.worryLevels.append(worryLevel)


for monkeyString in taskInput:
    lines = monkeyString.split("\n")
    name = re.search(r"\d+", lines[0]).group(0)
    startingWorryLevels = re.search(r"Starting items: ((\d+(, )*)+)", lines[1]).group(1)
    startingWorryLevels = [int(i) for i in startingWorryLevels.split(", ")]
    operation = re.search(r"Operation: new = ([^\n]*)", lines[2]).group(1)
    moduloTest = re.search(r"Test: divisible by (\d+)", lines[3]).group(1)
    ifTrueMonkey = re.search(r"If true: throw to monkey (\d+)", lines[4]).group(1)
    ifFalseMonkey = re.search(r"If false: throw to monkey (\d+)", lines[5]).group(1)

    if name in monkeys.keys():
        workingMonkey = monkeys[name]
    else:
        workingMonkey = Monkey(name)
    
    workingMonkey.worryLevels = startingWorryLevels
    workingMonkey.operation = operation
    workingMonkey.moduloTest = int(moduloTest)

    if ifTrueMonkey in monkeys.keys():
        workingMonkey.ifTrueMonkey = monkeys[ifTrueMonkey]
    else:
        Monkey(ifTrueMonkey)
        workingMonkey.ifTrueMonkey = monkeys[ifTrueMonkey]

    if ifFalseMonkey in monkeys.keys():
        workingMonkey.ifFalseMonkey = monkeys[ifFalseMonkey]
    else:
        Monkey(ifFalseMonkey)
        workingMonkey.ifFalseMonkey = monkeys[ifFalseMonkey]

monkeys = OrderedDict(sorted(monkeys.items()))

for roundNumber in range(1,ROUNDCOUNT+1):
    for monkey in monkeys.values():
        monkey.performTurn()

    print("after round %s:" % roundNumber)
    printState(monkeys)

for monkey in monkeys.values():
    print(f"{monkey.name} inspected {monkey.inspectionCount} times")

print(f"------------------\nlevel of monkey business is {getMonkeyBusiness(monkeys)}")