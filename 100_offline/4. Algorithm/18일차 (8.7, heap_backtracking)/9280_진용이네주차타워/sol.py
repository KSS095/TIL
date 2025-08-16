# 차가 주차장에 도착하면, 진용이는 비어있는 주차 공간이 있는지 검사한다.
# 비어있는 공간이 없다면, 빈 공간이 생길 때까지 차량을 입구에서 기다리게 한다.
# 빈 주차 공간이 있으면 진용이는 곧바로 주차를 시키며, 주차 가능한 공간 중 번호가 가장 작은 주차 공간에 주차하도록 한다.
# 만약 주차를 기다리는 차량이 여러 대라면, 입구의 대기장소에서 자기 차례를 기다려야 한다. 운전자들은 예의가 바르기 때문에 새치기를 하지 않는다.

import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    n, m = list(map(int, input().split()))
    weight_fee = []     # 단위 무게 당 요금, 누적 요금, 차량 번호
    car_weight = []     # 차량의 무게
    parking = {}        # 주차장 상태
    total_fee = 0       # 총 요금
    queue = []          # 대기 중인 차량

    for i in range(n):
        weight_fee.append((int(input()), 0, 0)) # (차량의 무게, 요금, 차량 번호)
        parking[i] = weight_fee[i]

    for _ in range(m):
        car_weight.append(int(input()))

    for i in range(2 * m):
        in_out = int(input())   # 들어오거나 나가는 차량
        if in_out > 0:  # 차량이 들어오면
            placed = False  # 차량이 없는 상태
            for j in range(len(parking)):   # 모든 주차공간 돌면서
                if parking[j][2] == 0:  # 들어온 차량이 없다면(공간이 비어있다면)
                    fee = parking[j][0] * car_weight[in_out - 1]    # 요금 = 단위 무게 당 요금 X 차의 무게
                    parking[j] = (parking[j][0], fee, in_out)   # 주차장 공간 갱신
                    total_fee += parking[j][1]  # 총 요금에 합산
                    placed = True   # 차량 들어옴
                    break
            if not placed:  # 차량이 없다면
                queue.append(in_out)    # 대기 큐에 저장

        else:   # 차량이 나가면
            car_num = abs(in_out)   # 차량 번호
            for j in range(n):
                if parking[j][2] == car_num:    # 차량이 나간 공간을 찾으면
                    parking[j] = (parking[j][0], parking[j][1], 0)  # 주차장 공간 초기화
                    break
            if queue:   # 차량이 대기 중이라면
                waiting_car = queue.pop(0)
                for j in range(n):
                    if parking[j][2] == 0:
                        fee = parking[j][0] * car_weight[waiting_car - 1]
                        parking[j] = (parking[j][0], parking[j][1] + fee, waiting_car)  # 주차장 공간 갱신
                        total_fee += fee
                        break

    print(f"#{tc} {total_fee}")

# TC = int(input())
# for tc in range(1, TC + 1):
#     n, m = map(int, input().split())
#     weight_fee = []
#     car_weight = []
#     parking = {}
#     total_fee = 0
#     queue = []  # 대기 중인 차량
#
#     for i in range(n):  # 단위 무게 당 요금
#         weight_fee.append(int(input()))
#         parking[i] = [weight_fee[i], 0, 0, False]  # 요금, 누적요금, 차량번호, 자리상태
#
#     for _ in range(m):  # 차량 무게
#         car_weight.append(int(input()))
#
#     for _ in range(2 * m):
#         in_out = int(input())
#         if in_out > 0:  # 차량 들어옴
#             placed = False
#             for j in range(n):
#                 if not parking[j][3]:  # 빈 자리
#                     fee = parking[j][0] * car_weight[in_out - 1]
#                     parking[j][1] += fee
#                     parking[j][2] = in_out
#                     parking[j][3] = True
#                     total_fee += fee
#                     placed = True
#                     break
#             if not placed:
#                 queue.append(in_out)
#
#         else:  # 차량 나감
#             car_num = abs(in_out)
#             for j in range(n):
#                 if parking[j][2] == car_num:
#                     parking[j][2] = 0
#                     parking[j][3] = False
#                     break
#             if queue:
#                 waiting_car = queue.pop(0)
#                 for j in range(n):
#                     if not parking[j][3]:
#                         fee = parking[j][0] * car_weight[waiting_car - 1]
#                         parking[j][1] += fee
#                         parking[j][2] = waiting_car
#                         parking[j][3] = True
#                         total_fee += fee
#                         break
#
#     print(f"#{tc} {total_fee}")
