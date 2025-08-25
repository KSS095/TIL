import sys
sys.stdin = open('sample_input.txt')

def bino(n, a):
    dp = [[0 for _ in range(a + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, a) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    return dp[n][a]


T = int(input())
for tc in range(1, T + 1):
    n, a, b = map(int, input().split())
    coefficient = bino(n, a)

    print(f'#{tc} {coefficient}')