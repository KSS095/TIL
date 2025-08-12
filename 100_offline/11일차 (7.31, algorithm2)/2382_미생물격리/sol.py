import sys
sys.stdin = open('sample_input.txt')

# opposite = {1: 2, 2: 1, 3: 4, 4: 3}
#
# T = int(input())
# for tc in range(1, 3):
#     width, time, association_count = list(map(int, input().split()))    # 변의 길이, 격리 시간, 군집의 개수
#     sector = [[False] * width for _ in range(width)]    # 미생물 군집이 위치한 곳 표시
#     association_info = []   # 미생물 군집 정보 저장할 리스트
#
#     for i in range(association_count):
#         association_info[i] = list(map(int, input().split()))  # 미생물 군집 정보 (row, col, 미생물 수, 이동 방향)
#         association_info[i].append(1)  # 정보에 생존 플래그 추가 (1: 생존, 0: 사멸)
#
#         row, col, micro_count, direction, live = association_info[i]
#         sector[row][col] = False  # 이동할 거니까 False로 바꾸기
#         if direction == 1:  # 위로 이동
#             row -= 1
#         elif direction == 2:  # 아래로 이동
#             row += 1
#         elif direction == 3:  # 왼쪽으로 이동
#             col -= 1
#         else:  # 오른쪽으로 이동
#             col += 1
#
#         if row == 0 or col == 0:    # 가장자리에 군집이 도달했다면
#             micro_count //= 2       # 미생물 수 반으로 줄이기
#             direction = opposite.get(direction) # 이동 방향 반대로
#
#         if sector[row][col]:    # 가고자 하는 자리에 다른 군집이 있다면
#
#
#         else:   # 없었다면
#             sector[row][col] = True  # 이동한 위치 True로 바꾸기
#
#         association_info[i] = list(row, col, micro_count, direction, live)
#
#     print(f'#{tc} {micro_org}')


opposite = {1: 2, 2: 1, 3: 4, 4: 3}  # 방향 반대로 바꾸기
# 0: dummy, 1: 상, 2: 하, 3: 좌, 4: 우
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    width, time, association_count = map(int, input().split())  # 변의 길이, 격리 시간, 군집 개수
    microbes = []   # 군집 정보 저장

    for _ in range(association_count):
        row, col, micro_count, direction = map(int, input().split())
        microbes.append([row, col, micro_count, direction])

    for _ in range(time):  # 격리 시간 동안 이동
        after_move = {}  # (row, col)를 key로, 군집 목록을 value로 저장, 이번 시간에 이동한 모든 군집의 정보 저장

        # 모든 군집 이동
        for row, col, micro_count, direction in microbes:
            nr = row + dr[direction]    # 진행 방향으로 이동
            nc = col + dc[direction]    # 진행 방향으로 이동

            if (nr == 0) or (nr == width - 1) or (nc == 0) or (nc == width - 1):    # 가장자리에 군집이 도달했다면
                micro_count //= 2   # 미생물 수 반으로 줄이기
                direction = opposite[direction] # 이동 방향 반대로

            if micro_count > 0:  # 살아있는 군집만
                if (nr, nc) not in after_move:  # 구역 안에 군집이 없었다면 새로 만들기
                    after_move[(nr, nc)] = []
                after_move[(nr, nc)].append([micro_count, direction])   # 군집 정보에 미생물 수, 방향 정보 추가

        # 군집끼리 만났을 때
        new_microbes = []   # 군집 정보 업데이트 해놓을 리스트
        for (r, c), groups in after_move.items():   # 구역 안 모든 위치에 대해서
            if len(groups) == 1:    # 같은 위치에 군집이 하나라면
                new_microbes.append([r, c, groups[0][0], groups[0][1]]) # 군집 정보 그냥 업데이트
            else:   # 같은 위치에 군집이 여러개라면
                total_num = sum(g[0] for g in groups)   # 미생물 수 전부 더하기
                max_num, direction = max(groups, key=lambda x: x[0])    # 미생물 수가 가장 많은 군집을 찾아서 방향 선택
                new_microbes.append([r, c, total_num, direction])   # 군집 정보 업데이트

        microbes = new_microbes  # 업데이트

    # 격리 시간 후 전체 미생물 수 합
    answer = sum(m[2] for m in microbes)
    print(f"#{tc} {answer}")