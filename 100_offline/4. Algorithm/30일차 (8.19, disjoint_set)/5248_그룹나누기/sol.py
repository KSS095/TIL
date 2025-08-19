# import sys
# sys.stdin = open('sample_input.txt')

def make_set(num):  # 서로소 집합 만들기
    return [i for i in range(num + 1)]

def find_set(x):    # 집합의 대표자 찾기
    if x == disjoint_set[x]:
        return disjoint_set[x]

    disjoint_set[x] = find_set(disjoint_set[x])
    return disjoint_set[x]

def union(x, y):    # 집합 합치기
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        disjoint_set[root_y] = root_x


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    disjoint_set = make_set(N)

    paper = list(map(int, input().split())) # 제출한 신청서에 쓰여진 번호를 저장할 리스트

    for i in range(0, len(paper), 2):    # 2개씩 묶어서 하나의 집합으로
        union(paper[i], paper[i + 1])

    for i in range(0, len(paper), 2):    # 2개씩 묶어서 하나의 집합으로 한번 더
        union(paper[i], paper[i + 1])

    res = len(set(disjoint_set)) - 1    # 0을 제외한 모든 대표자 개수 계산

    print(f"#{tc} {res}")