with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\10_CathodeRayTube\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

xRegDeltas = []
for line in taskInput:
    if line == "noop":
        xRegDeltas.append(0)
    else:
        xRegDeltas.append(int(line.split(" ")[1]))
        xRegDeltas.append(0)  # addx takes two cycles to complete, so one delta=0 is inserted

# for cycle in range(2,len(xRegDeltas)+4):
#     print(cycle, sum(xRegDeltas[:cycle-2])+1)

signalStrengthSum = 0
for cycle in range(20,221,40):
    print(cycle, (sum(xRegDeltas[:cycle-2])+1)*cycle)
    signalStrengthSum += (sum(xRegDeltas[:cycle-2])+1)*cycle

print("\nsignalStrengthSum: %s" % signalStrengthSum)