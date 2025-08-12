import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    for _ in range(N):
        heap_nodes= MeanHeap()
        op = list(map(int, input().split()))

        if op[1] == 1:
            heappush(op[2])
        else: heappop()

    # heap_nodes
    # print(f'#{tc} {heap_nodes}')