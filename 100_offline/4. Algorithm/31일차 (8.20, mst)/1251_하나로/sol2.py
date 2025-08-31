import sys
sys.stdin = open('re_sample_input.txt')


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x


def kruskal(e):
    e.sort(key=lambda x: x[2])
    acc_cost = 0

    for edge in e:
        x, y, w = edge
        if find_set(x) != find_set(y):
            union(x, y)
            acc_cost += w

    return acc_cost


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    E = float(input())

    parent = [i for i in range(N + 1)]
    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            w = (x_coords[i] - x_coords[j]) ** 2 + (y_coords[i] - y_coords[j]) ** 2
            edges.append((i, j, w))

    min_cost = kruskal(edges)
    min_cost *= E

    print(f'#{tc} {round(min_cost)}')
