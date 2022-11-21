# ans 1
N = int(input())

ans = dict()
lookup = dict()


def solve(n):

    if n < 0:
        return False

    if n == 0:
        return True

    if n not in lookup:
        lookup[n] = (
            solve(n - 100)
            or solve(n - 101)
            or solve(n - 102)
            or solve(n - 103)
            or solve(n - 104)
            or solve(n - 105)
        )

    return lookup[n]


for i in range(1, 100001):
    ans[i] = solve(i)

if ans[N]:
    print(1)
else:
    print(0)


# ans 2
N = int(input())


class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        dp = [-1 for i in range(0, amount + 1)]
        for i in coins:
            if i > len(dp) - 1:
                continue
            dp[i] = 1
            for j in range(i + 1, amount + 1):
                if dp[j - i] == -1:
                    continue
                elif dp[j] == -1:
                    dp[j] = dp[j - i] + 1
                else:
                    dp[j] = min(dp[j], dp[j - i] + 1)
            # print(dp)
        return dp[amount]


ob1 = Solution()
if ob1.coinChange([100, 101, 102, 103, 104, 105], N) != -1:
    print(1)
else:
    print(0)
