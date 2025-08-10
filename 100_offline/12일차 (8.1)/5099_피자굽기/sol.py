import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N: 화덕의 크기, M: 피자 개수
    cheese = list(map(int, input().split()))
    oven = deque()  # 피자가 들어갈 화덕
    waiting = deque()   # 대기할 피자가 있을 공간

    for i in range(N):
        oven.append((cheese[i], i + 1)) # (치즈의 양, 피자 번호)

    for i in range(N, M):   # 나머지 피자는 대기 공간에 저장
        waiting.append((cheese[i], i + 1))

    while len(oven) > 1: # 화덕에 하나만 남을 때까지
        current_cheese, pizza_num = oven.popleft()  # 피자 꺼내보기
        melt = current_cheese // 2

        if melt == 0: # 치즈가 다 녹았다면
            if waiting: # 기다리고 있는 피자가 있다면
                oven.append(waiting.popleft())  # 화덕에 넣기
        else:   # 치즈가 다 안녹았다면
            oven.append((melt, pizza_num))  # 치즈가 녹은 상태로 마지막 순서에 넣기

    print(f'#{tc} {oven[0][1]}')    # 마지막 남은 피자의 인덱스