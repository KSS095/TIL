# import sys
# sys.stdin = open('input.txt')

# from itertools import permutations
#
# def calc():
#     global max_prob, acc_prob
#
#     for perm in permutations(range(N), N):  # 각 직원이 할 일에 대한 순열 구하기
#         acc_prob = 1.0    # acc_prob 초기화
#
#         for i in range(len(perm)):  # 모든 순열에 대해서 성공할 확률 계산
#             acc_prob *= suc_prob[i][perm[i]] / 100.0
#
#         acc_prob *= 100.0
#         max_prob = max(acc_prob, max_prob)  # 최댓값 갱신
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     suc_prob = [list(map(int, input().split())) for _ in range(N)]
#     max_prob = 0.0    # 모든 일을 성공할 최대 확률
#     acc_prob = 1.0    # 연산된 확률
#
#     calc()
#     print(f'#{tc} {max_prob:.6f}')

# import sys
# sys.stdin = open('input.txt')

def dfs(idx, prob):
    global max_prob

    if prob <= max_prob:    # 현재 확률이 이미 최댓값보다 작다면
        return
    if idx == N:  # 직원들에게 모든 일을 배정했으면 최댓값 갱신
        max_prob = max(max_prob, prob)
        return

    # idx번째 직원에게 남은 일 중 하나 배정
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            # idx 하나 늘리고, 확률 계산하여 넘기기
            dfs(idx + 1, prob * (suc_prob[idx][i] / 100.0))
            visited[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    suc_prob = [list(map(int, input().split())) for _ in range(N)]
    max_prob = 0.0  # 모든 일을 성공할 최대 확률
    visited = [False] * N

    dfs(0, 1.0)  # 처음 확률 1

    print(f'#{tc} {max_prob * 100:.6f}')