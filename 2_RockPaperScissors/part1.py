with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\2_RockPaperScissors\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

shapePoints = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

winningCombos = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}

equivalent = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

yourPoints = 0
for line in taskInput:
    opponentShape, yourShape = line.split(" ")
    if equivalent[yourShape] == opponentShape:  # draw
        yourPoints += shapePoints[yourShape] + 3
    elif winningCombos[yourShape] == opponentShape:  # win
        yourPoints += shapePoints[yourShape] + 6
    else:  # loss
        yourPoints += shapePoints[yourShape]

print(yourPoints)