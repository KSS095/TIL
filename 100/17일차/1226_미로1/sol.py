import sys
sys.stdin = open('input.txt')

from collections import deque
#     상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def maze_trip(maze):
    queue = deque()
    queue.append((1, 1))

    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True

    while queue:
        row, col = queue.popleft()

        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            # 경계 밖으로 나가는지, 방문 했는지, 1이 아닌지 확인
            if (0 <= nx < 16) and (0 <= ny < 16) and (not visited[nx][ny]) and maze[nx][ny] != 1:
                # 도착점을 찾았다면 1을 반환
                if maze[nx][ny] == 3: return 1

                visited[nx][ny] = True
                queue.append((nx, ny))
    # 도착점을 찾지 못한다면 0을 반환
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # 미로 탐험
    reachable = maze_trip(maze)

    print(f'#{tc} {reachable}')