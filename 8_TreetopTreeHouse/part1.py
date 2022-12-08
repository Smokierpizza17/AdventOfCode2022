with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\8_TreetopTreeHouse\input.txt", "r") as inputFile:
    taskInput = [[int(l) for l in i] for i in inputFile.read().split("\n")]

sumTaller = 0
for y, row in enumerate(taskInput):
    for x, height in enumerate(row):
        taller = False
        if all([i < height for i in row[:x]]) or x == 0:
            taller = True
        elif all([i < height for i in row[x+1:]]) or x == len(row) - 1:
            taller = True
        elif all([i < height for i in [r[x] for r in taskInput[y+1:]]]) or y == 0:
            taller = True
        elif all([i < height for i in [r[x] for r in taskInput[:y]]]) or y == len(taskInput) - 1:
            taller = True
        if taller:
            sumTaller += 1
            print("T", end="")
        else:
            print(" ", end="")
    print("")

print("\n", sumTaller)