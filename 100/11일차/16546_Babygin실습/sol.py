from itertools import permutations

# 연속된 세 장의 카드가 1씩 차이가 나는지(연속적인 번호를 갖는지) 확인
def is_run(cards):
    return int(cards[0]) + 1 == int(cards[1]) and int(cards[1]) + 1 == int(cards[2])

# 연속된 세 장의 카드가 같은 번호를 갖는지 확인
def is_triplet(cards):
    return cards[0] == cards[1] == cards[2]

# run과 triplet을 모두 만족하는지 확인
def is_babygin_permutations(cards):
    # 가능한 모든 순열을 만들고, 두 그룹으로 나누기
    for perm in permutations(cards):
        first_group = perm[:3]
        second_group = perm[3:]

        # 두 그룹 모두 각각 run이나 triplet을 만족하면 True 반환
        if (is_run(first_group) or is_triplet(first_group)) and (is_run(second_group) or is_triplet(second_group)):
            return True
    # 아니라면 False 반환
    return False

tc = int(input())

for T in range(tc):
    card = input().strip()

    res = 'true' if is_babygin_permutations(card) else 'false'
    print(f'#{T + 1} {res}')