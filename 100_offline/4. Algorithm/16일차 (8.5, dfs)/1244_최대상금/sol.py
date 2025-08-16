import sys
sys.stdin = open('input.txt')

def dfs(num, cnt):
    global max_price

    if cnt == change:   # 교환 횟수만큼 교환했으면
        max_price = max(max_price, int(num))    # 최댓값 갱신
        return
    if (num, cnt) in visited: return    # 이미 있는 조합이면 종료
    visited.add((num, cnt))     # 이미 조사한 조합 set에 추가

    num = list(num)     # string을 list로 변환
    for i in range(len(num)):
        for j in range(i + 1, len(num)):    # 모든 경우의 수
            num[i], num[j] = num[j], num[i] # 교환
            dfs(''.join(num), cnt + 1)      # list를 다시 string으로 변환, 교환 횟수 1 증가
            num[i], num[j] = num[j], num[i] # 원상복구

T = int(input())
for tc in range(1, T + 1):
    num, change = input().split()
    change = int(change)
    max_price = 0   # 최댓값 저장할 변수
    visited = set() # 중복 여부

    dfs(num, 0)

    print(f'#{tc} {max_price}')