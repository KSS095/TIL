# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    nodes = list(map(int, input().split()))
    node_count = nodes[0]   # 노드 개수
    leaf_count = nodes[1]   # 리프 개수
    print_node = nodes[2]   # 출력하고자 하는 노드

    # node_info = {}
    tree = [0] * (node_count + 1)

    for _ in range(leaf_count):
        leaf_info = list(map(int, input().split()))
        # node_info[leaf_info[0]] = leaf_info[1]
        tree[leaf_info[0]] = leaf_info[1]

    # 재귀함수를 이용하여 후위 계산
    def calc(node):
        # 재귀함수 종료 조건 (node 번호가 개수를 넘어가면 0 반환)
        if node > node_count:
            return 0

        # 이미 계산이 돼있는 node라면 해당 value를 반환
        if tree[node] != 0:
            return tree[node]

        # 원하는 노드의 자식들 계산
        left_child = 2 * node
        right_child = 2 * node + 1

        left_val = calc(left_child)
        right_val = calc(right_child)

        tree[node] = left_val + right_val
        return tree[node]

    res = calc(print_node)
    print(f'#{tc + 1} {res}')