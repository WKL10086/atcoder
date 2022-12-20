from __future__ import annotations


def part1(data: list[str]) -> int:

    return 0


def part2(data: list[str]) -> int:

    return 0


def test_passing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        assert part1(data) == 0
        # assert part2(data) == 0
        f.close()


# Do not change the next line
with open("change_name.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    # part2(data)

    test_passing()

    f.close()
