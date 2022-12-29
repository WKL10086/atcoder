from __future__ import annotations


class Pair:
    def __init__(self, sensor_x: int, sensor_y: int, beacon_x: int, beacon_y: int):
        self.sensor_x = sensor_x
        self.sensor_y = sensor_y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y

    def compute_Manhattan_distance(self) -> int:
        return abs(self.sensor_x - self.beacon_x) + abs(self.sensor_y - self.beacon_y)


def format_input(line: str) -> tuple[int, int, int, int]:
    _, _, sensor_x, sensor_y, _, _, _, _, beacon_x, beacon_y = line.split()
    sensor_x = int(sensor_x[2:-1])
    sensor_y = int(sensor_y[2:-1])
    beacon_x = int(beacon_x[2:-1])
    beacon_y = int(beacon_y[2:])
    return sensor_x, sensor_y, beacon_x, beacon_y


def add_covered(target_covered: set[int], limit: int, pair: Pair):
    for i in range(pair.sensor_x - limit, pair.sensor_x + limit + 1):
        target_covered.add(i)


def add_covered_within_border(
    target_covered: set[int], limit: int, pair: Pair, border: int
):
    lower_bound = max(0, pair.sensor_x - limit)
    upper_bound = min(border + 1, pair.sensor_x + limit + 1)
    for i in range(lower_bound, upper_bound):
        target_covered.add(i)


def part1(data: list[str], target_height: int) -> int:
    target_covered = set()
    discard = set()
    for line in data:
        sensor_x, sensor_y, beacon_x, beacon_y = format_input(line)
        pair = Pair(sensor_x, sensor_y, beacon_x, beacon_y)
        Manhattan_distance = pair.compute_Manhattan_distance()
        if target_height in range(
            pair.sensor_y, pair.sensor_y + Manhattan_distance + 1
        ):
            limit = pair.sensor_y + Manhattan_distance - target_height
            add_covered(target_covered, limit, pair)
        elif target_height in range(pair.sensor_y - Manhattan_distance, pair.sensor_y):
            limit = target_height - pair.sensor_y + Manhattan_distance
            add_covered(target_covered, limit, pair)

        if pair.beacon_y == target_height:
            discard.add(pair.beacon_x)

    for i in discard:
        target_covered.discard(i)

    ans = len(target_covered)
    print(ans)

    return ans


# really slow
def part2(data: list[str], border: int) -> int:
    ans = 0

    pairs = []
    for line in data:
        sensor_x, sensor_y, beacon_x, beacon_y = format_input(line)
        pair = Pair(sensor_x, sensor_y, beacon_x, beacon_y)
        pairs.append(pair)

    for height in range(border + 1):
        print("height: ", height)
        target_covered = set()
        for pair in pairs:
            Manhattan_distance = pair.compute_Manhattan_distance()
            if height in range(pair.sensor_y, pair.sensor_y + Manhattan_distance + 1):
                limit = pair.sensor_y + Manhattan_distance - height
                add_covered_within_border(target_covered, limit, pair, border)
            elif height in range(pair.sensor_y - Manhattan_distance, pair.sensor_y):
                limit = height - pair.sensor_y + Manhattan_distance
                add_covered_within_border(target_covered, limit, pair, border)

        covered_length = len(target_covered)

        if covered_length != border + 1:
            ans_y = height
            ans_x = 0
            for temp_x in range(border + 1):
                if temp_x not in target_covered:
                    ans_x = temp_x
                    break
            ans = ans_x * 4000000 + ans_y
            break

    print(ans)
    return ans


def run_testing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        # assert part1(data, 10) == 26
        # assert part2(data, 20) == 56000011
        f.close()


# Do not change the next line
with open("day15.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data, 2000000)

    part2(data, 4000000)

    run_testing()

    f.close()
