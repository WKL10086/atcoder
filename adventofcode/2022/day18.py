from __future__ import annotations


class Cube:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def find_adjacent_num(self, three_d_plot) -> int:
        adjacent = 0
        if (self.x + 1, self.y, self.z) in three_d_plot:
            adjacent += 1
        if (self.x - 1, self.y, self.z) in three_d_plot:
            adjacent += 1
        if (self.x, self.y + 1, self.z) in three_d_plot:
            adjacent += 1
        if (self.x, self.y - 1, self.z) in three_d_plot:
            adjacent += 1
        if (self.x, self.y, self.z + 1) in three_d_plot:
            adjacent += 1
        if (self.x, self.y, self.z - 1) in three_d_plot:
            adjacent += 1
        return adjacent


def part1(data: list[str]) -> int:
    all_cubes = []
    three_d_plot = set()
    for line in data:
        x, y, z = map(int, line.split(","))
        all_cubes.append(Cube(x, y, z))
        three_d_plot.add((x, y, z))

    sides = 0
    for cube in all_cubes:
        adjacent = cube.find_adjacent_num(three_d_plot)
        sides += 6 - adjacent

    print(sides)
    return sides


def part2(data: list[str]) -> int:

    return 0


def run_testing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        # assert part1(data) == 64
        assert part2(data) == 0
        f.close()


# Do not change the next line
with open("day18.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    # part2(data)

    run_testing()

    f.close()
