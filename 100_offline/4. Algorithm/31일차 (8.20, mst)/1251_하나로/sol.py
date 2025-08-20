import sys
sys.stdin = open('re_sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    islands = int(input())  # 섬의 개수
    x_coord = list(map(int, input().split()))   # x 좌표
    y_coord = list(map(int, input().split()))   # y 좌표
    coordinates = list(zip(x_coord, y_coord))   # (x, y) 로 묶기
    E = float(input())  # 환경 부담 세율
    min_cost = 0  # 최소 환경 부담금

    # print(coordinates)



    print(f'#{tc} {min_cost}')