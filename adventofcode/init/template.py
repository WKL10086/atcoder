from __future__ import annotations

working_stage = 1
test_part_1_answer = 0
test_part_2_answer = 0

if working_stage == 1:
    is_testing = True
    is_part_1 = True
elif working_stage == 2:
    is_testing = False
    is_part_1 = True
elif working_stage == 3:
    is_testing = True
    is_part_1 = False
else:
    is_testing = False
    is_part_1 = False


def part_1(data: list[str]) -> int:

    return 0


def part_2(data: list[str]) -> int:

    return 0


def run_testing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()

        if is_part_1:
            assert part_1(data) == test_part_1_answer
        else:
            assert part_2(data) == test_part_2_answer

        f.close()


def main():
    # * if next line changed, adjust the change in init.py
    with open("change_name.txt", "r") as f:
        data = f.read().splitlines()

        part_1(data) if is_part_1 else part_2(data)

        f.close()


if __name__ == "__main__":
    run_testing() if is_testing else main()
