def bellman_ford(graph, start):
    n = len(graph)  # 정점의 수
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    # 마지막 정점을 제외한 횟수만큼 순회
    for _ in range(n - 1):
        updated = False     # 이번 회차에 갱신여부 확인용
        # 각 정점별 인접 정점 순회
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight    # 갱신
                    updated = True
        # 이번 회차에 전체 노드에 대한 조사를 했음에도 갱신이 없다?
        if not updated: break

    # 음수 사이클 검사
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                # 어 ? 조사 끝났는데 왜 또 갱신해야 하는 상황 나옴?
                print('음수 사이클이 있습니다.')
                return False
    return distances

# 예시 그래프
graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': 3, 'd': 2, 'e': 3},
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

# # 음수 사이클 예시 그래프
# graph = {
#     'a': {'b': 4, 'c': 2},
#     'b': {'c': -3, 'd': 2, 'e': 3},
#     'c': {'b': 1, 'd': 4, 'e': 5},
#     'd': {'e': -3},
#     'e': {'f': 2},
#     'f': {}
# }

# # 시작 정점 설정
# start_vertex = 'a'

# 벨만-포드 알고리즘 실행
for start_vertex in graph.keys():
    result = bellman_ford(graph, start_vertex)
    print(f"'{start_vertex}': {result}")
