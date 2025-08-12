import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, input())) for _ in range(N)]
    profit = 0
    center = N // 2     # 각 행의 중앙
    for i in range(N):
        # 각 행에서 정사각형 마름모에 해당하는 범위 계산
        if i <= center:     # 중앙 위쪽: 중앙에서부터 i만큼 좌우로 확장
            distance = i
        else:   # 중앙 아래쪽: 중앙에서부터 (N - i - 1)만큼 좌우로 확장
            distance = N - i - 1

        # 해당 행의 범위 내 값 모두 더하기
        for j in range(center - distance, center + distance + 1):
            profit += farm[i][j]

    print(f'#{tc} {profit}')