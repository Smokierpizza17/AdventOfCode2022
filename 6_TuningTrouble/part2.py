with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\6_TuningTrouble\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = taskInput[0]
# taskInput = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # testing

for i in range(14,len(taskInput)):
    currStringlet = taskInput[i-14:i]
    if len(set(currStringlet)) == 14:  # all characters unique
        print(i)
        break