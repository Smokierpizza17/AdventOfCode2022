with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\6_TuningTrouble\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = taskInput[0]
# taskInput = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # testing

for i in range(4,len(taskInput)):
    currStringlet = taskInput[i-4:i]
    if len(set(currStringlet)) == 4:  # all characters unique
        print(i)
        break