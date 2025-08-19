# import sys
# sys.stdin = open('sample_input.txt')

def make_set(num):  # 서로소 집합 만들기
    parent = [i for i in range(num + 1)]
    rank = [0] * (num + 1)
    return parent, rank

def find_set(x):    # 집합의 대표자 찾기
    if x == disjoint_set[x]:
        return disjoint_set[x]

    disjoint_set[x] = find_set(disjoint_set[x])
    return disjoint_set[x]

def union(x, y):    # 집합 합치기
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            disjoint_set[root_y] = root_x
        elif rank[root_y] > rank[root_x]:
            disjoint_set[root_x] = root_y
        else:
            disjoint_set[root_y] = root_x
            rank[root_x] += 1


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    disjoint_set, rank = make_set(n)
    result_str = ""     # 결과 문자열

    for _ in range(m):
        expr, a, b = list(map(int, input().split()))
        if expr == 0:   # 0이면 합집합 연산
            union(a, b)
        else:   # 1이면 a, b가 같은 집합에 있는지 확인 (대표자 비교)
            if find_set(a) == find_set(b):
                result_str += '1'   # 대표자가 같으면 문자열에 1 붙이기
            else: result_str += '0' # 대표자가 다르면 0 붙이기

    print(f"#{tc} {result_str}")