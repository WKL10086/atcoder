S = input()


def test_in_format(s: str) -> bool:
    if (
        len(s) == 8
        and s[0].isupper()
        and s[-1].isupper()
        and s[1:-1].isnumeric()
        and int(s[1:-1]) in range(100_000, 1_000_000, 1)
    ):
        return True
    return False


ans = test_in_format(S)

print("Yes" if ans else "No")
