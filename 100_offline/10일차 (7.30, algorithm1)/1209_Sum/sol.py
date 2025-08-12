import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = input()
    data = [list(map(int, input().split())) for _ in range(100)]

    # 모든 합을 한 번에 계산
    maximum = max([
        *[sum(row) for row in data],  # 행 합들
        *[sum(data[i][j] for i in range(100)) for j in range(100)],  # 열 합들
        sum(data[i][i] for i in range(100)),  # 좌상->우하 대각선
        sum(data[99 - i][i] for i in range(100))  # 우상->좌하 대각선
    ])

    print(f'#{tc} {maximum}')