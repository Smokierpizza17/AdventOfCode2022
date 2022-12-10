import sys
import numpy as np

with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\9_RopeBridge\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

directions = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
}

ROPELENGTH = 9

head = None
lastKnot = None
knots = []
class RopeKnot():
    def __init__(self, parentKnot=None, daughterKnot=None):
        knots.append(self)
        self.name = str(knots.index(self))
        self.coords = (0,0)

        if daughterKnot == None:  # last knot
            global lastKnot
            lastKnot = self
            self.daughterKnot = None
        else:
            self.daughterKnot = daughterKnot

        if parentKnot == None:  # head
            global head
            head = self
            self.name = "H"
            self.parentKnot = None
        else:
            self.parentKnot = parentKnot

    def moveBy(self, coords):
        self.coords = addCoordinates(self.coords, coords)

    def updateMotion(self):
        deltaX = self.parentKnot.coords[0] - self.coords[0]
        deltaY = self.parentKnot.coords[1] - self.coords[1]
        if any(abs(i) > 1 for i in [deltaX, deltaY]):  # movement necessary
            self.coords = addCoordinates((np.sign(deltaX), np.sign(deltaY)), self.coords)
        else:
            pass

    def updateMotionCascade(self):
        self.updateMotion()
        if self.daughterKnot != None:
            self.daughterKnot.updateMotionCascade()

def addCoordinates(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def printState(knots, visitedCoords=[]):
    minX = min([k.coords[0] for k in knots] + [i[0] for i in visitedCoords])
    minY = min([k.coords[1] for k in knots] + [i[1] for i in visitedCoords])
    maxX = max([k.coords[0] for k in knots] + [i[0] for i in visitedCoords])
    maxY = max([k.coords[1] for k in knots] + [i[1] for i in visitedCoords])
    for y in reversed(range(minY, maxY+1)):
        for x in range(minX, maxX + 1):
            alreadyPrinted = False
            for k in knots:
                if k.coords == (x,y):
                    print(k.name, end="")
                    alreadyPrinted = True
                    break
            if alreadyPrinted:
                continue
            elif x == 0 and y == 0:
                print("s", end="")
            elif (x,y) in visitedCoords:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")

visitedCoords = set()

parentKnot = None
for i in range(ROPELENGTH+1):
    parentKnot = RopeKnot(parentKnot)

for i, knot in enumerate(knots):
    if i+1 < len(knots):
        knot.daughterKnot = knots[i+1]

for instruction in taskInput:
    direction, count = instruction.split(" ")
    count = int(count)
    for _ in range(count):
        visitedCoords.add(lastKnot.coords)
        #printState(knots, visitedCoords)
        head.moveBy(directions[direction])
        head.daughterKnot.updateMotionCascade()
    visitedCoords.add(lastKnot.coords)
    #printState(knots, visitedCoords)
    #print("--------------")
print("\ntail visited %s coords" % (len(visitedCoords)))