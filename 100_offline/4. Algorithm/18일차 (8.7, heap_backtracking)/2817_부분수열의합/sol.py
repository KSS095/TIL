import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, acc):
    global count

    if acc > K: return  # 누적 합이 K보다 커지면 종료
    if acc == K:
        count += 1
        return  # 누적 합이 K와 같다면 종료
    if idx == N: return  # 인덱스가 N과 같다면 종료

    dfs(idx + 1, acc + numbers[idx])  # 현재 숫자를 더하고 재귀
    dfs(idx + 1, acc)  # 현재 숫자를 더하지 않고 재귀

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 수열의 원소 개수, K: 원하는 합
    numbers = list(map(int, input().split()))

    count = 0  # 합이 K가 되는 경우의 수
    dfs(0, 0)  # 인덱스 0부터, 누적 합 0부터 시작

    print(f'#{tc} {count}')

# def power_set():
#     global count
#
#     for i in range(1, 1 << N):  # 공집합을 제외한 모든 부분집합
#         temp_list = []
#         for j in range(N):
#             if i & (1 << j):    # 현재 숫자를 넣을 것인지
#                 temp_list.append(numbers[j])
#         if sum(temp_list) == K: # 리스트에 있는 숫자의 합이 K와 같다면
#             count += 1
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())    # N: 수열의 원소 개수, K: 원하는 합
#     numbers = list(map(int, input().split()))
#
#     count = 0   # 합이 K가 되는 경우의 수
#     power_set()
#
#     print(f'#{tc} {count}')