import sys
sys.stdin = open('sample_input.txt')

from collections import deque
#     상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 터널 타입 별로 연결 가능한 방향 리스트
tunnel_type = {
    1: [0, 1, 2, 3],       # 상 하 좌 우
    2: [0, 1],             # 상 하
    3: [2, 3],             # 좌 우
    4: [0, 3],             # 상 우
    5: [1, 3],             # 하 우
    6: [1, 2],             # 하 좌
    7: [0, 2]              # 상 좌
}
# 반대 방향 매핑
opposite = {0: 1, 1: 0, 2: 3, 3: 2}

# 현재 위치의 구조물과 다음으로 갈 구조물이 연결되어 있는지(이동할 수 있는지) 체크
def can_move(start, direction, end):
    return (direction in tunnel_type.get(start)) and (opposite[direction] in tunnel_type.get(end))

def escape(R, C, L, tunnel):
    global possible_locations

    queue = deque()
    queue.append((R, C, 1))
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True

    while queue:
        row, col, time = queue.popleft()
        # 주어진 시간 넘어가면 해당 direction 으로는 그만
        if time >= L:
            continue

        # 현재 터널 구조물의 타입
        current_type = tunnel[row][col]

        # 구조물의 타입에 따라 갈 수 있는 방향 모두 검사
        for direction in tunnel_type.get(current_type):
            nx = row + dx[direction]
            ny = col + dy[direction]

            # 터널 밖으로 넘어가는지, 방문했는지, 0이 아닌지 검사
            if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny]) and (tunnel[nx][ny]):
                # 현재 구조물의 타입, 갈 방향, 갈 방향에 있는 다음 구조물의 타입을 인자로 넘겨버리기
                if can_move(current_type, direction, tunnel[nx][ny]):  # 다음 구조물로 넘어갈 수 있다면
                    visited[nx][ny] = True
                    possible_locations += 1
                    queue.append((nx, ny, time + 1))

T = int(input())
for tc in range(1, T + 1):
    # N: 터널 height, M: 터널 width, R: 뚜껑 row, C: 뚜껑 column, L: 탈출 소요 시간
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range (N)]   # 터널 정보

    possible_locations = 1  # 탈주범이 있을 수 있는 장소 개수 (시작지점 포함)
    escape(R, C, L, tunnel) # 탈출 감행

    print(f'#{tc} {possible_locations}')