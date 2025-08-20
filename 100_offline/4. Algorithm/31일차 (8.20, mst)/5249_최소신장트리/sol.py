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


def mst_kruskal(temp):
    mst = []
    # 가중치 정렬
    temp.sort(key=lambda x: x[2])
    for tp in temp:
        x, y, w = tp
        if find_set(x) != find_set(y):
            union(x, y)
            mst.append(tp)
    return mst


T = int(input())

for tc in range(1, T + 1):


    # 모든 노드 간의 간선 정보를 기록한다.
    parent = [i for i in range(N)]


    # print(f'#{tc} {}')
