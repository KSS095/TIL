import sys
sys.stdin = open('sample_input.txt')

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x


def mst(edges):
    mst_list = []
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        x, y, w = edge
        if find_set(x) != find_set(y):
            union(x, y)
            mst_list.append(edge)

    return mst_list


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    parent = [i for i in range(V + 1)]
    min_weight_sum = 0

    mst_lists = mst(edges)

    for mst_list in mst_lists:
        min_weight_sum += mst_list[2]

    print(f'#{tc} {min_weight_sum}')
