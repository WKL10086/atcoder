from __future__ import annotations

is_testing = True
is_part_1 = True


def part_1(data: list[str]) -> int:

    return 0


def part_2(data: list[str]) -> int:

    return 0


def run_testing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()

        if is_part_1:
            assert part_1(data) == 0
        else:
            assert part_2(data) == 0

        f.close()


def main():
    # * if next line changed, adjust the change in init.py
    with open("change_name.txt", "r") as f:
        data = f.read().splitlines()

        part_1(data) if is_part_1 else part_2(data)

        f.close()


if __name__ == "__main__":
    run_testing() if is_testing else main()
