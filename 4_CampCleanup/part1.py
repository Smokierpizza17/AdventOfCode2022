with open("C:\\Users\\oskar\\Drive\\projects\\AdventOfCode2022\\4_CampCleanup\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def doOverlapFully(elf1, elf2):
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:  # elf1 in elf2
        return True
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:  # elf2 in elf1
        return True
    return False

overlapCount = 0
for pair in taskInput:
    elf1, elf2 = [i.split("-") for i in pair.split(",")]
    elf1 = [int(i) for i in elf1]
    elf2 = [int(i) for i in elf2]

    if doOverlapFully(elf1, elf2):
        overlapCount += 1
    
print(overlapCount)