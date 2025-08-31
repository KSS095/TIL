import sys
sys.stdin = open('sample_input.txt')


def floyd_warshall(graph):
    n = len(graph)  # 전체 노드의 개수
    dist = [[float('inf')] * n for _ in range(n)]   # 거리를 inf로 초기화

    for i in range(n):  # 본인과의 거리는 0
        dist[i][i] = 0

    for u in range(n):
        for v in range(n):
            if graph[u][v] != 0:    # 다른 노드와 연결돼있다면
                dist[u][v] = graph[u][v]    # dist 갱신(연결 안돼있으면 inf로 냅두기)

    print(dist)
    # 모든 정점을 경유정점으로 고려
    for k_node in range(n):
        for start in range(n):  # 시작 노드
            for end in range(n):  # 도착 노드
                Dik = dist[start][k_node]
                Dkj = dist[k_node][end]
                Dij = dist[start][end]
                if Dik + Dkj < Dij:  # k를 경유하는게 더 가까우면
                    dist[start][end] = Dik + Dkj  # 그걸로 바꿈
    return dist


T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 노드의 개수
    graph_matrix = [list(map(int, input().split())) for _ in range(N)]  # 비용 인접행렬

    shortest_path = floyd_warshall(graph_matrix)

    max_shortest = max(max(row) for row in shortest_path)   # 계산한 최소 이동 비용 중 최댓값
    print(f'#{tc} {max_shortest}')