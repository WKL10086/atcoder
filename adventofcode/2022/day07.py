class Tree:
    def __init__(self, name: str, size: int):
        self.children = []
        self.name = name
        self.size = size

    def insertFile(self, name: str, data: int):
        self.children.append(Tree(name, data))
        self.size = self.computeSize()

    def insertDir(self, name: str):
        self.children.append(Tree(name, 0))

    def computeSize(self):
        if len(self.children) == 0:
            return self.size
        else:
            size = 0
            for child in self.children:
                size += child.computeSize()
            return size


def handleAction_cd(path: str, currentPath: list[str]):
    if path == "..":
        currentPath.pop()
    else:
        currentPath.append(path)


def findTree(currentTree: Tree, currentPath: list[str]):
    if len(currentPath) == 0:
        return currentTree
    else:
        for child in currentTree.children:
            if child.name == currentPath[0]:
                return findTree(child, currentPath[1:])


def part1(data: list[str]):
    currentPath = []

    for line in data:
        command = line.split()
        firstLetter = command[0][0]
        if firstLetter == "$":
            action = command[1]
            if action == "cd":
                path = command[2]
                handleAction_cd(path, currentPath)
            elif action == "ls":
                continue
        else:
            size = int(command[0])
            name = command[1]


def part2(data: list[str]):
    ans = 0

    print(ans)


with open("test.txt", "r") as f:
    # with open("day07.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    # part2(data)

    f.close()
