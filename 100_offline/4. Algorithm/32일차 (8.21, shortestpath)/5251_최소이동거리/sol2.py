import sys
sys.stdin = open('sample_input.txt')

import heapq

def calc_min_distance(vertex, start):
    distances = [float('inf') for _ in range(N + 1)]
    distances[start] = 0
    visited = set()

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        dist, current = heapq.heappop(heap)

        if distances[current] < dist or current in visited: continue
        visited.add(current)

        for next, weight in vertex[current].items():
            next_dist = dist + weight
            if next_dist < distances[next]:
                distances[next] = next_dist
                heapq.heappush(heap, [next_dist, next])
    return distances


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    vertex = {v: {} for v in range(N + 1)}

    for s, e, w in edges:
        vertex[s][e] = w

    min_distance = calc_min_distance(vertex, 0)
    print(f'#{tc} {min_distance[N]}')
