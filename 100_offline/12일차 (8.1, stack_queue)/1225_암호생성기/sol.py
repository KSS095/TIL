import sys
sys.stdin = open('input.txt')

from collections import deque

for _ in range(10):
    tc = int(input())
    # 입력 받은 리스트를 덱에 저장
    basic_list = deque(list(map(int, input().split())))
    cnt = 1

    while basic_list[-1] > 0:   # 마지막 계산 값이 음수가 될 때까지
        if cnt == 6:    # 5 감소 후 새로운 사이클 시작
            cnt = 1
        # 리스트 첫번째 값을 빼서 감소 후 마지막에 저장
        basic_list.append(basic_list.popleft() - cnt)
        cnt += 1

    basic_list[-1] = 0  # 마지막 값을 0으로 저장
    cipher_list = list(basic_list)

    print(f'#{tc}', end=' ')
    for i in range(len(cipher_list)):
        print(cipher_list[i], end=' ')
    print()