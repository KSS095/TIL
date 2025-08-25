import sys
sys.stdin = open('sample_input.txt')


def knapsack(size, price, box_size):
    dp = [0] * (box_size + 1)   # 현재 용량(w)에서의 최대 가격 저장

    for i in range(len(size)):  # 물건들 모두에 대해서
        for w in range(box_size, size[i] - 1, -1):  # w를 박스의 크기부터 1까지 역순으로 순회
            dp[w] = max(dp[w], price[i] + dp[w - size[i]])  # 현재 물건을 담는 경우와 담지 않는 경우 중 더 큰 가격 선택

    return dp[box_size]


T = int(input())
for tc in range(1, T + 1):
    box_size, gifts = map(int, input().split())    # 박스의 크기, 상품의 개수 입력

    size_i = []     # 상품들의 크기를 담을 리스트
    price_i = []    # 상품들의 가격을 담을 리스트
    for _ in range(gifts):  # 상품의 개수만큼
        size, price = map(int, input().split()) # 상품의 크기, 가격 입력
        size_i.append(size)
        price_i.append(price)

    # 최대로 담을 수 있는 물건들의 가격 합
    max_price = knapsack(size_i, price_i, box_size)

    print(f'#{tc} {max_price}')