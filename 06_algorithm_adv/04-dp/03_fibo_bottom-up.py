def fibo(N):
    global cnt

    if N < 1:
        return N

    # 함수 내에서 저장할 공간 생성
    dp = [0] * (N + 1)
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt += 1
    return dp[N]


cnt = 0
result = fibo(10001)
print(result)   # N번 연산
print(cnt)
