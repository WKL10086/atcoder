class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, direction: str):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1


class Head(Point):
    pass


class Tail(Point):
    def checkTouchingHead(self, head: Point):
        if head.x in [self.x - 1, self.x, self.x + 1] and head.y in [
            self.y - 1,
            self.y,
            self.y + 1,
        ]:
            return True
        return False

    def moveDiagonal(self, direction: str, head: Point):
        if direction == "U":
            self.y += 1
            self.x = head.x
        elif direction == "D":
            self.y -= 1
            self.x = head.x
        elif direction == "R":
            self.x += 1
            self.y = head.y
        elif direction == "L":
            self.x -= 1
            self.y = head.y


def findDirection(head: Head, tail: Tail) -> str:
    if tail.y == head.y:
        if tail.x < head.x:
            return "R"
        elif tail.x > head.x:
            return "L"
    elif tail.x == head.x:
        if tail.y < head.y:
            return "U"
        elif tail.y > head.y:
            return "D"


def findDiagonalDirection(head: Head, tail: Tail) -> str:
    if tail.y < head.y:
        if tail.x == head.x - 1 or tail.x == head.x + 1:
            return "U"
        elif tail.x - 2 == head.x:
            return "L"
        elif tail.x + 2 == head.x:
            return "R"
    elif tail.y > head.y:
        if tail.x == head.x - 1 or tail.x == head.x + 1:
            return "D"
        elif tail.x - 2 == head.x:
            return "L"
        elif tail.x + 2 == head.x:
            return "R"


def part1(data: list[str]):
    head = Head(0, 0)
    tail = Tail(0, 0)
    tailPath = set()
    tailPath.add((tail.x, tail.y))

    for line in data:
        direction, num = line.split()
        num = int(num)

        for _ in range(num):
            head.move(direction)

            if not tail.checkTouchingHead(head):
                if tail.x == head.x or tail.y == head.y:
                    tail.move(direction)
                else:
                    tail.moveDiagonal(direction, head)

            tailPath.add((tail.x, tail.y))

    print(len(tailPath))


# TODO: pass test case, dont know why it doesnt work on actual input
def part2(data: list[str]):
    head = Head(0, 0)
    snake = [Tail(0, 0) for _ in range(9)]
    snake.insert(0, head)
    lastTail = snake[-1]
    tailPath = set()
    tailPath.add((lastTail.x, lastTail.y))

    for line in data:
        direction, num = line.split()
        num = int(num)

        for _ in range(num):
            for i in range(len(snake)):
                currentPoint = snake[i]
                if i == 0:
                    currentPoint.move(direction)
                else:
                    prev = snake[i - 1]
                    if not currentPoint.checkTouchingHead(prev):
                        if currentPoint.x == prev.x or currentPoint.y == prev.y:
                            currentDirection = findDirection(prev, currentPoint)
                            currentPoint.move(currentDirection)
                        else:
                            currentDirection = findDiagonalDirection(prev, currentPoint)
                            currentPoint.moveDiagonal(currentDirection, prev)

            tailPath.add((lastTail.x, lastTail.y))

    print(len(tailPath))


def test():
    head = Head(-2, 0)
    tail = Tail(0, 0)

    if not tail.checkTouchingHead(head):
        if tail.x == head.x or tail.y == head.y:
            currentDirection = findDirection(head, tail)
            print(currentDirection)
            tail.move(currentDirection)
        else:
            currentDirection = findDiagonalDirection(head, tail)
            print(currentDirection)
            tail.moveDiagonal(currentDirection, head)

    print(tail.x, tail.y)


# with open("test.txt", "r") as f:
with open("day09.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    # test()

    f.close()
