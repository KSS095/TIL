import sys
sys.stdin = open('input.txt')


def dfs(idx, acc):
    global min_height
    if acc >= min_height:    # 누적 합이 현재까지 계산된 최소 높이보다 크다면
        return

    if idx == clerk:    # 모든 점원에 대해 탐색했다면
        if acc >= shelf:    # 누적 합이 선반의 크기를 넘었다면
            min_height = min(min_height, acc)   # min_height 와 비교 후 갱신
        return
    dfs(idx + 1, acc + height[idx])  # 현재 점원의 키를 더하던가
    dfs(idx + 1, acc)                # 안더하고 진행하던가


T = int(input())
for tc in range(1, T + 1):
    clerk, shelf = map(int, input().split())    # 점원 수, 선반 높이
    min_height = 10000 * clerk  # 나올 수 있는 최댓값으로 초기화

    height = list(map(int, input().split()))    # 점원들의 키

    dfs(0, 0)
    print(f'#{tc} {min_height - shelf}')    # 선반 높이와의 차이 출력
