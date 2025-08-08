import sys
sys.stdin = open('input.txt')

from collections import deque

for _ in range(10):

    tc = int(input())
    basic_list = list(map(int, input().strip().split()))
    queue = deque(basic_list)
    cnt = 1
    while queue[-1] > 0:
        if cnt == 6:
            cnt = 1
        queue.append(queue.popleft() - cnt)
        cnt+=1

    queue[-1] = 0
    print(list(queue))

    # print(f'#{tc} {cipher_list}')