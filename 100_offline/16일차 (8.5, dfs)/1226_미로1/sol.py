import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]  # 상 하
dy = [0, 0, -1, 1]  # 좌 우

def dfs(idx):
    global possible

    x, y = idx[0], idx[1]
    if (x, y) in visited: return  # 방문 했었다면 종료
    visited.add((x, y)) # 방문 표시

    for i in range(4):  # 현재 위치에서 4방향 검사
        nx = x + dx[i]
        ny = y + dy[i]

        if maze[nx][ny] == 1: continue    # 1이라면 다음 방향 탐색
        if maze[nx][ny] == 3:   # 3이라면 탈출 가능한 것
            possible = 1
            return

        if (nx, ny) not in visited and maze[nx][ny] == 0:   # 아직 방문 안했고 0이라면
            dfs((nx, ny))   # 해당 위치에서 다시 dfs 시작


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    possible = 0    # 도달 가능 여부 (0: 불가능, 1: 가능)
    visited = set() # 방문 여부
    start = (1, 1)  # 시작 지점 (항상 (1, 1))

    dfs(start)
    print(f'#{tc} {possible}')