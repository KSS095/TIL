import sys
sys.stdin = open('input.txt')

import heapq

#     상  하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move_to_end():
    heap = []
    heapq.heappush(heap, (0, 0, 0)) # x, y, dist
    distances = [[float('inf')] * N for _ in range(N)]  # 모든 지점에서의 거리를 inf 로 저장

    while heap:
        r, c, dist = heapq.heappop(heap)
        if distances[r][c] < dist: continue         # 현재 저장되어있는 거리보다 길다면 패스
        if (r, c) == (N - 1, N - 1): return dist    # 도착점에 도달했다면 계산한 거리 반환

        for i in range(4):  # 네 방향 탐색
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N: # 벽 탐색
                next_distance = dist + war_map[nr][nc]  # 다음 장소까지 거리

                if next_distance < distances[nr][nc]:   # 현재 저장되어있는 거리보다 짧다면
                    distances[nr][nc] = next_distance   # 갱신
                    heapq.heappush(heap, (nr, nc, next_distance))   # 힙에 삽입

    return distances[N - 1][N - 1]  # 도착점에 저장된 거리 반환


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    war_map = [list(map(int, input())) for _ in range(N)]

    min_distance = move_to_end()    # 거리 계산
    print(f'#{tc} {min_distance}')
