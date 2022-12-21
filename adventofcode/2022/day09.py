from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def is_touching(self, pre: Point) -> bool:
        if pre.x in range(self.x - 1, self.x + 2) and pre.y in range(
            self.y - 1, self.y + 2
        ):
            return True
        return False

    def move(self, direction: str):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1

    def adjust(self, pre: Point):
        if self.y + 2 == pre.y:
            if self.x - 1 == pre.x:
                self.x -= 1
                self.y += 1
            elif self.x == pre.x:
                self.y += 1
            elif self.x + 1 == pre.x:
                self.x += 1
                self.y += 1
            elif self.x - 2 == pre.x:
                self.x -= 1
                self.y += 1
            elif self.x + 2 == pre.x:
                self.x += 1
                self.y += 1
        elif self.y - 2 == pre.y:
            if self.x - 1 == pre.x:
                self.x -= 1
                self.y -= 1
            elif self.x == pre.x:
                self.y -= 1
            elif self.x + 1 == pre.x:
                self.x += 1
                self.y -= 1
            elif self.x - 2 == pre.x:
                self.x -= 1
                self.y -= 1
            elif self.x + 2 == pre.x:
                self.x += 1
                self.y -= 1
        elif self.x + 2 == pre.x:
            if self.y - 1 == pre.y:
                self.x += 1
                self.y -= 1
            elif self.y == pre.y:
                self.x += 1
            elif self.y + 1 == pre.y:
                self.x += 1
                self.y += 1
        elif self.x - 2 == pre.x:
            if self.y - 1 == pre.y:
                self.x -= 1
                self.y -= 1
            elif self.y == pre.y:
                self.x -= 1
            elif self.y + 1 == pre.y:
                self.x -= 1
                self.y += 1


def part1(data: list[str]) -> int:
    head = Point(0, 0)
    tail = Point(0, 0)
    tail_tracker = set()
    tail_tracker.add((tail.x, tail.y))

    for line in data:
        direction, times = line.split()
        times = int(times)

        for _ in range(times):
            head.move(direction)
            if not tail.is_touching(head):
                tail.adjust(head)
            tail_tracker.add((tail.x, tail.y))

    print(len(tail_tracker))
    return len(tail_tracker)


def part2(data: list[str]) -> int:
    snack = [Point(0, 0) for _ in range(10)]
    tail_tracker = set()
    tail_tracker.add((snack[9].x, snack[9].y))

    for line in data:
        direction, times = line.split()
        times = int(times)

        for _ in range(times):
            snack[0].move(direction)
            for i in range(1, 10):
                if not snack[i].is_touching(snack[i - 1]):
                    snack[i].adjust(snack[i - 1])
            tail_tracker.add((snack[9].x, snack[9].y))

    print(len(tail_tracker))
    return len(tail_tracker)


def run_testing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        # assert part1(data) == 13
        assert part2(data) == 36
        f.close()


# Do not change the next line
with open("day09.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    run_testing()

    f.close()
