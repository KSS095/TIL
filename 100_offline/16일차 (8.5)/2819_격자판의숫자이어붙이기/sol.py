import sys
sys.stdin = open('sample_input.txt')

# 어느 방향으로 갈 지
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, path):
    # 길이가 7이 되면 종료
    if len(path) == 7:
        result_set.add(path)
        return

    # 동서남북 탐색
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 격자판 벗어나지 않는 선에서 재귀
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, path + str(arr[nx][ny]))

T = int(input())
for tc in range(T):
    result_set = set()  # 중복 제거해서 조사하기 위해 set 선택
    arr = [list(map(int, input().split())) for _ in range(4)]   # 행렬 입력

    # 모든 지점에서 dfs 수행
    for i in range(4):
        for j in range(4):
            dfs(i, j, str(arr[i][j]))

    print(f'#{tc + 1} {len(result_set)}')