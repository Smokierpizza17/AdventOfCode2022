with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\1_CalorieCounting\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

elfCalories = []
currSum = 0
for line in taskInput:
    if line == "":
        elfCalories.append(currSum)
        currSum = 0
    else:
        currSum += int(line)

elfCalories = sorted(elfCalories)
print(sum(elfCalories[-3:]))