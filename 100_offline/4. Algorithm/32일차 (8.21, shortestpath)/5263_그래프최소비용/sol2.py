import sys
sys.stdin = open('sample_input.txt')


def calc_min_distances(graph):
    n = len(graph)
    distance = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                distance[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                Dik = distance[i][k]
                Dkj = distance[k][j]
                Dij = distance[i][j]

                if Dik + Dkj < Dij:
                    distance[i][j] = Dik + Dkj

    return distance


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    min_distances = calc_min_distances(graph)

    max_distance = max(max(row) for row in min_distances)
    print(f'#{tc} {max_distance}')