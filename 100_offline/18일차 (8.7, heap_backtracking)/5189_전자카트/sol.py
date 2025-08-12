import sys
sys.stdin = open('sample_input.txt')

def calc_consume(idx, current, acc_battery):
    global lowest_battery

    # 누적 배터리량이 최소 배터리를 넘으면 종료
    if acc_battery >= lowest_battery: return

    if idx == N:    # 조사를 마쳤다면 최소 배터리 반환
        lowest_battery = min(lowest_battery, acc_battery + sector[current][0])
        return

    for next in range(1, N):    # 1번부터 N-1번 구역까지
        if not visited[next]:   # 방문 하지 않았다면
            visited[next] = True    # 방문 했다는 표시
            calc_consume(idx + 1, next, acc_battery + sector[current][next])
            visited[next] = False   # 복구

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    sector = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    visited[0] = True

    lowest_battery = 100 * N * N    # 나올 수 있는 최대 배터리량으로 초기화
    calc_consume(1, 0, 0)   # 인덱스는 1부터 시작, 현재 위치와 누적 배터리 = 0

    print(f'#{tc} {lowest_battery}')