with open(r"C:\Users\oskar\Drive\projects\AdventOfCode2022\7_NoSpaceLeftOnDevice\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

allFolders = []
rootFolder = None
class Folder():
    def __init__(self, name, parentFolder=None):
        allFolders.append(self)
        self.name = name
        if self.name == "/":
            global rootFolder
            rootFolder = self
        self.subfolders = []
        self.files = []
        if type(parentFolder) == Folder:
            parentFolder.addSubfolder(self)
            self.parentFolder = parentFolder

    def addSubfolder(self, folder):
        self.subfolders.append(folder)

    def addFile(self, name, size=None):
        self.files.append([name, size])

    def printTree(self, recursing=False):
        lines = []
        if not recursing:
            lines.append("dir %s (%s)" % (self.name, self.getSize()))
        for file in self.files:
            lines.append("└── %s (%s)" % (file[0], str(file[1])))
        for folder in self.subfolders:
            lines.append("└── dir %s (%s)" % (folder.name, folder.getSize()))
            lines += ["    " + l for l in folder.printTree(True)]
        if recursing:
            return lines
        for l in lines:
            print(l)
    
    def getSize(self):
        totalSize = 0
        for file in self.files:
            totalSize += file[1]
        for folder in self.subfolders:
            totalSize += folder.getSize()
        return totalSize


workingFolder = None
readingContents = False
for line in taskInput:
    if readingContents:
        if line.startswith("$"):
            readingContents = False
        else:
            dirOrSize, name = line.split(" ")
            if dirOrSize.isnumeric():  # file
                workingFolder.addFile(name, int(dirOrSize))
    if line.startswith("$ cd "):
        if line == "$ cd ..":
            workingFolder = workingFolder.parentFolder
            continue
        workingFolder = Folder(line.replace("$ cd ", ""), workingFolder)
    elif line.startswith("$ ls"):
        readingContents = True

rootFolder.printTree()

targetFolderSize = 30000000 - 70000000 + rootFolder.getSize()
foldersWithSizes = []
for folder in allFolders:
    foldersWithSizes.append([folder, folder.getSize()])

foldersWithSizes.sort(key=lambda x:x[1])
for folder, size in foldersWithSizes:
    if size > targetFolderSize:
        print("\n", folder.name, size)
        break