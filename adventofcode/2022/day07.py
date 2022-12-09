from __future__ import annotations


class Tree:
    def __init__(self, name: str, size: int, parent: Tree = None):
        self.children = []
        self.name = name
        self.size = size
        self.parent = parent

    def insertFile(self, name: str, size: int):
        self.children.append(Tree(name, size, self))
        self.size = self.computeSize()

    def insertDir(self, name: str):
        self.children.append(Tree(name, 0, self))

    def computeSize(self) -> int:
        if len(self.children) == 0:
            return self.size
        else:
            size = 0
            for child in self.children:
                size += child.computeSize()
            self.size = size
            return size

    def navigate(self, path: str):
        if path == "..":
            return self.parent
        else:
            for child in self.children:
                if child.name == path:
                    return child

    def findSmallestDir(self, neededSize: int) -> int:
        if len(self.children) == 0:
            return 70000000
        else:
            ans = self.size
            for child in self.children:
                temp = min(ans, child.findSmallestDir(neededSize))
                if temp >= neededSize:
                    ans = temp

            return ans


def findSumOfDirSizeAtMost100000(tree: Tree):
    ans = 0
    for child in tree.children:
        ans += findSumOfDirSizeAtMost100000(child)

    # check if current tree is a directory and its size is at most 100000
    if tree.size <= 100000 and len(tree.children) > 0:
        ans += tree.size

    return ans


def findNeededSize(root: Tree):
    usedSize = root.size
    return usedSize - 40000000


def createTree(data: list[str]):
    root = None
    currentTree = None

    for line in data:
        command = line.split()
        firstLetter = command[0]
        if firstLetter == "$":
            action = command[1]
            if action == "cd":
                path = command[2]
                if path == "/":
                    root = Tree("/", 0)
                    currentTree = root
                else:
                    currentTree = currentTree.navigate(path)
            elif action == "ls":
                continue
        else:
            if command[0] == "dir":
                currentTree.insertDir(command[1])
            else:
                size = int(command[0])
                name = command[1]
                currentTree.insertFile(name, size)

    root.computeSize()

    return root


def part1(data: list[str]):
    root = createTree(data)

    print(findSumOfDirSizeAtMost100000(root))


def part2(data: list[str]):
    root = createTree(data)
    neededSize = findNeededSize(root)

    print(root.findSmallestDir(neededSize))


# with open("test.txt", "r") as f:
with open("day07.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    f.close()
