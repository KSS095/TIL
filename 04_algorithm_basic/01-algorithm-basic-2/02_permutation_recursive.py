def perm(selected, remain):  
    '''
    Args:
        selected: 선택된 값 목록
        remain: 선택되지 않고 남은 값 목록
    '''
    # 모든 요소를 선택할 것이니... 나머지가 없을 때까지
    if not remain:
        print(*selected)
    else:   # 아직 선택할 수 있는 요소들이 남아 있다면!
        for idx in range(len(remain)):      # 그 요소를 모두 순회하면서
            # idx 번째의 요소를 선택
            select_item = remain[idx]
            # 선택된 idx번째를 제외한 remain을 만들자. (진짜 나머지 리스트)
            remain_list = remain[:idx] + remain[idx + 1:]
            perm(selected + [select_item], remain_list)


# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])



# selected = [], remain = [1, 2, 3]
# for idx in range(3):
# idx = 0
# select_item = remain[0]   # [1]
# remain_list = remain[:0] + remain[1:]     # [2, 3]
# perm([1], [2, 3])     # 재귀
#
#     selected = [1], remain = [2, 3]
#     for idx in range(2):
#     idx = 0
#     select_item = remain[0]   # [2]
#     remain_list = remain[:0] + remain[1:]     # [3]
#     perm([1, 2], [3])     # 재귀
#
#         selected = [1, 2], remain = [3]
#         for idx in range(1):
#         idx = 0
#         select_item = remain[0]    # [3]
#         remain_list = remain[:0] + remain[1:]     # []
#         perm([1, 2, 3], [])       # 재귀
#
#             selected = [1, 2, 3], remain = []
#             if not remain -> print(selected)         # 출력 : [1, 2, 3]  perm([1, 2, 3], []) 종료
#
#         for문 끝    perm([1, 2], [3])) 종료
#
#     idx = 1
#     select_item = remain[1]       # [3]
#     remain_list = remain[:1] + remain[2:]     # [2]
#     perm([1, 3], [2])     # 재귀
#
#         selected = [1, 3], remain = [2]
#         for idx in range(1):
#         idx = 0
#         select_item = remain[0] # [2]
#         perm([1, 3, 2], [])       # 재귀
#
#             selected = [1, 3, 2], remain = []
#             if not remain -> print(selected)          # 출력 : [1, 3, 2]    perm([1, 3, 2], []) 종료
#
#         for문 끝    perm([1, 3], [2]) 종료
#
#     for문 끝    perm([1], [2, 3]) 종료
# idx = 1
# ...