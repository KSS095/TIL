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
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    lst = []
    for i in range(N):
        lst.append([x_list[i], y_list[i]])

    # 환경 부담율
    E = float(input())

    # 모든 노드 간의 간선 정보를 기록한다.
    parent = [i for i in range(N)]
    temp = []

    for i in range(N):
        for j in range(i + 1, N):
            w = (lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2
            temp.append((i, j, w))

    # 가중치 최솟값 찾기
    result = mst_kruskal(temp)
    total = 0

    # 길이의 제곱 총합 구하기
    for re in result:
        total += re[2]

    ans = E * total

    print(f'#{tc} {round(ans)}')




# T = int(input())
# for tc in range(1, T + 1):
#     islands = int(input())  # 섬의 개수
#     x_coord = list(map(int, input().split()))   # x 좌표
#     y_coord = list(map(int, input().split()))   # y 좌표
#     coordinates = list(zip(x_coord, y_coord))   # (x, y) 로 묶기
#     E = float(input())  # 환경 부담 세율
#     min_cost = 0  # 최소 환경 부담금
#
#     # print(coordinates)
#
#
#
#     print(f'#{tc} {min_cost}')