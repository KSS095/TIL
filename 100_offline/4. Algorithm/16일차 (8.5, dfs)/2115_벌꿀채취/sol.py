import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 3 <= N <= 10, 1 <= M <= 5, N >= M, 10 <= C <= 30
    N, M, C = map(int, input().split()) # N: 벌통 크기, M: 개수, C: 최대 양
    honey_bee = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 최솟값으로 초기화

    '''
        data[x][y] ~ data[x][y+M-1] 까지의 벌통을 채취
        모든 시작지점 (x, y) 좌표부터 전체 순회
    '''
    for x in range(N):
        for y in range(N-M+1):


    print(f'#{tc} {result}')

