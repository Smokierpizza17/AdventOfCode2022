with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\10_CathodeRayTube\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

xRegDeltas = []
for line in taskInput:
    if line == "noop":
        xRegDeltas.append(0)
    else:
        xRegDeltas.append(int(line.split(" ")[1]))
        xRegDeltas.append(0)  # addx takes two cycles to complete, so one delta=0 is inserted

for cycle in range(1,len(xRegDeltas)+1):
    xReg = sum(xRegDeltas[:cycle-2])+1
    beamXPos = (cycle-1) % 40
    if beamXPos == xReg or beamXPos == xReg-1 or beamXPos == xReg+1:
        print("██", end="")
    else:
        print("  ", end="")
    if cycle % 40 == 0:
        print("")
