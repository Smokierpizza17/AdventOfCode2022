with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\2_RockPaperScissors\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

shapePoints = {
    "A": 1,
    "B": 2,
    "C": 3
}

yourShapeForLoss = {
    "A": "C",
    "B": "A",
    "C": "B"
}

yourShapeForWin = {
    "A": "B",
    "B": "C",
    "C": "A"
}

yourPoints = 0
for line in taskInput:
    opponentShape, gameSituation = line.split(" ")
    if gameSituation == "X":  # lose
        yourShape = yourShapeForLoss[opponentShape]
        yourPoints += shapePoints[yourShape]
    elif gameSituation == "Y":  # draw
        yourShape = opponentShape
        yourPoints += shapePoints[yourShape] + 3
    elif gameSituation == "Z":  # win
        yourShape = yourShapeForWin[opponentShape]
        yourPoints += shapePoints[yourShape] + 6

print(yourPoints)