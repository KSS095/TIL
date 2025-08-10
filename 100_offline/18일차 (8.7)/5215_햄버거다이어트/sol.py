import sys
sys.stdin = open('sample_input.txt')

def low_and_tasty(idx, acc_taste, acc_cal):
    global max_tasty

    if acc_cal > L: return  # 누적 칼로리가 제한 넘으면 종료
    if acc_taste > max_tasty:   # 누적 맛 점수가 더 크면 갱신
        max_tasty = acc_taste

    if idx == N: return # 모든 재료 봤으면 종료

    taste, cal = ingredient_info[idx]   # 현재 idx의 맛, 칼로리 저장

    # 현재 재료 선택 O or 선택 X
    low_and_tasty(idx + 1, acc_taste + taste, acc_cal + cal)
    low_and_tasty(idx + 1, acc_taste, acc_cal)

T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())    # N: 맛점수 개수, L: 제한 칼로리
    ingredient_info = [list(map(int, input().split())) for _ in range(N)]

    max_tasty = 0   # 최대 맛 점수
    low_and_tasty(0, 0, 0) # 처음 인덱스, 맛점수, 칼로리: 0

    print(f'#{tc} {max_tasty}')