with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\8_TreetopTreeHouse\input.txt", "r") as inputFile:
    taskInput = [[int(l) for l in i] for i in inputFile.read().split("\n")]

def reverseList(lst):
    return list(reversed(lst))

def getScenicScoreForDirection(height, treeLine):
    for distance, neighbourHeight in enumerate(treeLine):
        if neighbourHeight >= height:
            return distance + 1
    return len(treeLine)

maxScore = 0
for y, row in enumerate(taskInput):
    for x, height in enumerate(row):
        scenicScore = 1
        scenicScore *= getScenicScoreForDirection(height, reverseList(row[:x]))
        scenicScore *= getScenicScoreForDirection(height, row[x+1:])
        scenicScore *= getScenicScoreForDirection(height, [r[x] for r in taskInput[y+1:]])
        scenicScore *= getScenicScoreForDirection(height, reverseList([r[x] for r in taskInput[:y]]))
        if scenicScore > maxScore:
            maxScore = scenicScore

print(maxScore)
