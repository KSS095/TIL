import sys
sys.stdin = open('input1.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(idx, length, direction):
    global N, M, structure, longest, visited
    x, y = idx[0], idx[1]

    if length > longest:    # 최대 길이 갱신
        longest = length

    # 현재 방향으로 계속 진행
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 경계 체크 및 구조물 체크 및 방문 체크
    if (0 <= nx < N and 0 <= ny < M and
            structure[nx][ny] == 1 and (nx, ny) not in visited):
        visited.add((nx, ny))
        dfs((nx, ny), length + 1, direction)    # 길이 1 증가시키고 진행
        visited.remove((nx, ny))  # 백트래킹

T = int(input())    # 사진 데이터 개수
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    structure = [list(map(int, input().split())) for _ in range(N)]
    longest = 0 # 가장 긴 구조물의 길이

    for i in range(N):
        for j in range(M):
            if structure[i][j] == 1:  # 구조물이 있는 곳에서 시작
                for direction in range(4):  # 4방향으로 각각 시작
                    visited = set()     # 방문 여부
                    visited.add((i, j))
                    dfs((i, j), 1, direction)

    print(f'#{tc} {longest}')