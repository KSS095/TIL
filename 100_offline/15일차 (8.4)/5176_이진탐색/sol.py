import sys
sys.stdin = open('sample_input.txt')

def inorder(idx):
    global number
    left_idx, right_idx = idx * 2, idx * 2 + 1

    if left_idx <= N:   # 트리 끝에 도달할 때 까지
        inorder(left_idx)

    tree[idx] = number  # 현재 노드에 1부터 삽입
    number += 1     # 넣을 값을 1 추가

    if right_idx <= N:  # 트리 끝에 도달할 때 까지
        inorder(right_idx)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    number = 1      # tree에 넣을 숫자
    tree = [0] * (N + 1)    # 노드 인덱스가 1부터 시작하므로
    inorder(1)      # index = 1 부터 탐색

    print(f'#{tc} {tree[1]} {tree[N // 2]}')