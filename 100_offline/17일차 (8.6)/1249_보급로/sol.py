import sys
sys.stdin = open('input.txt')

from collections import deque
#     상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def supply_route(road, N):
    queue = deque()
    queue.append((0, 0))

    visited = [[False] * N for _ in range(N)]
    route_weight = 0
    min_route_weight =
    visited[0][0] = True

    while queue:
        row, col = queue.popleft()

        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            # 경계 밖으로 나가는지, 방문 했는지 확인
            if (0 <= nx < 16) and (0 <= ny < 16) and (not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append((nx, ny))
                route_weight += road[nx][ny]

    min_route_weight = max(min_route_weight, route_weight)


T = int(input())

for C in range(1, T + 1):
    N = int(input())
    supply_road = [list(map(int, input())) for _ in range(N)]

    restore_time = supply_route(supply_road, N)

    print(f'#{C} {restore_time}')