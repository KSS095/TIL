import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    charge_count = 0    # 충전 횟수
    maximum_move, bus_stop_length, charger_count = list(map(int, input().split()))    # 최대 이동 가능 수, 정류장 길이, 충전기 갯수
    charger = list(map(int, input().split()))   # 충전기 위치

    current_pos = 0     # 현재 위치

    while True:
        current_pos += maximum_move # 일단 이동
        if current_pos >= bus_stop_length: break # 도착지에 도착하거나 지나간다면 종료

        if current_pos in charger:  # 현재 위치에 충전기가 있다면
            charge_count += 1
        else:   # 현재 위치에 충전기가 없다면 뒤로 돌아가면서 가장 가까운 충전기 찾기
            find = False    # 충전기 찾은지 안찾은지 확인
            for possible in range((current_pos - 1), current_pos - maximum_move, -1):   # 현재 위치 이전부터 전에 있던 위치 바로 다음 위치까지 탐색
                if possible in charger: # 이전 위치에 충전기가 있다면
                    charge_count += 1
                    current_pos = possible  # 현재 위치를 충전기 위치로 변경
                    find = True # 충전기 발견
                    break
            if not find:    # 충전기 발견 못했다면
                charge_count = 0    # 앞으로 더 갈 수 없다는 뜻이므로 0 반환
                break

    print(f'#{tc} {charge_count}')