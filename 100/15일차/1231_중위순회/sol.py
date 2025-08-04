import sys
sys.stdin = open('input.txt')

# 트리 중위 순회 함수
def inorder_traversal(idx, tree):
    result = ""
    if idx in tree and tree[idx][0]:  # 노드가 존재하고 값이 있는지 확인
        # 왼쪽 서브 트리를 먼저 조사
        left_child = tree[idx][1]
        if left_child:
            result += inorder_traversal(left_child, tree)

        # 루트 노드 조사
        result += tree[idx][0]

        # 오른쪽 서브 트리를 마지막에 조사
        right_child = tree[idx][2]
        if right_child:
            result += inorder_traversal(right_child, tree)

    return result

N = int(input())

for tc in range(N):
    node_info = input().strip().split()
    tree = {}  # 트리의 정보를 저장할 dictionary

    # 첫 번째 인덱스는 노드 번호
    num = int(node_info[0])
    # 두 번째 인덱스는 알파벳
    value = node_info[1]

    # left_child 또는 right_child가 없다면 None으로 저장
    if len(node_info) == 2:
        tree[num] = [value, None, None]
    elif len(node_info) == 3:
        tree[num] = [value, int(node_info[2]), None]
    else:
        tree[num] = [value, int(node_info[2]), int(node_info[3])]

    word = inorder_traversal(1, tree)
    print(f'#{tc + 1} {word}')