import numpy as np

with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\9_RopeBridge\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

directions = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
}

def getTailMotion(tailCoords, headCoords):
    deltaX = headCoords[0] - tailCoords[0]
    deltaY = headCoords[1] - tailCoords[1]
    if any(abs(i) > 1 for i in [deltaX, deltaY]):  # movement necessary
        return (np.sign(deltaX), np.sign(deltaY))
    else:
        return (0,0)

def addCoordinates(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def printState(headCoords, tailCoords, visitedCoords=[]):
    maxX = max([headCoords[0], tailCoords[0]] + [i[0] for i in visitedCoords])
    maxY = max([headCoords[1], tailCoords[1]] + [i[1] for i in visitedCoords])
    for y in reversed(range(maxY+1)):
        for x in range(maxX + 1):
            if headCoords[0] == x and headCoords[1] == y and tailCoords[0] == x and tailCoords[1] == y:
                print("B", end="")
            elif headCoords[0] == x and headCoords[1] == y:
                print("H", end="")
            elif tailCoords[0] == x and tailCoords[1] == y:
                print("T", end="")
            elif x == 0 and y == 0:
                print("s", end="")
            elif (x,y) in visitedCoords:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")

headCoords = (0,0)
tailCoords = (0,0)
visitedCoords = set()

for instruction in taskInput:
    direction, count = instruction.split(" ")
    count = int(count)
    for _ in range(count):
        visitedCoords.add(tailCoords)
        # printState(headCoords, tailCoords, visitedCoords)
        headCoords = addCoordinates(headCoords, directions[direction])
        tailCoords = addCoordinates(tailCoords, getTailMotion(tailCoords, headCoords))

    visitedCoords.add(tailCoords)
    #printState(headCoords, tailCoords, visitedCoords)
    #print("--------------")
print("\ntail visited %s coords" % (len(visitedCoords)))