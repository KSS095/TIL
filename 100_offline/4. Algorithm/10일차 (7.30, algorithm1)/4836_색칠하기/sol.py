import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    red = set()     # 빨강색 칠할 좌표
    blue = set()    # 파랑색 칠할 좌표

    for _ in range(N):
        paint = list(map(int, input().split()))
        r1, c1, r2, c2 = paint[:4]
        # 칠해질 좌표
        coordinates ={(i, j) for i in range(r1, r2 + 1) for j in range(c1, c2 + 1)}

        if paint[4] == 1:   # 1이면 red에 해당 좌표 추가
            red.update(coordinates)
        else:               # 2이면 blue에 해당 좌표 추가
            blue.update(coordinates)

    purple = len(red & blue)    # red와 blue가 겹치면 purple
    print(f'#{tc} {purple}')

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#
#     grid = [[0] * 10 for _ in range(10)]  # 10 x 10 좌표계
#
#     for _ in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())
#
#         # 해당하는 격자 모두 색칠(red라면 1씩, blue라면 2씩 증가)
#         for i in range(r1, r2 + 1):
#             for j in range(c1, c2 + 1):
#                 grid[i][j] += color
#
#     # 겹쳐서 격자값이 3이 된 보라색 칸 수 세기
#     purple = 0
#     for i in range(10):
#         for j in range(10):
#             if grid[i][j] == 3:
#                 purple += 1
#
#     print(f"#{tc} {purple}")