# for tc in range(10):
#     res = 0
#     nodes_count = int(input())
#     node_list = []  # 입력한 노드들의 모든 정보를 저장할 리스트
#     data = {}  # 각 노드들의 번호, value를 저장할 dictionary
#
#     for i in range(nodes_count):
#         node_list.append(list(map(str, input().split())))
#         data[int(node_list[i][0])] = node_list[i][1]
#
#     # data에서 value가 연산자라면 해당 key를 이용해서
#     # node_list에서 left_child, right_child를 가져와 그 key를 가지는 value를 가지고 와서 계산하면 되나
#     for j in range(len(data)):
#         if data[j] == '-':
#
#     print(node_list)
#     print(data)
#     print(f'#{tc + 1} {res}')

# import sys
# sys.stdin = open('input.txt')

for tc in range(10):
    nodes_count = int(input())  # 정점의 개수
    node_info = {}   # {노드 번호 : [value, left_child, right_child]}

    for _ in range(nodes_count):
        data = input().strip().split()
        # 첫 번째 인덱스는 노드 번호
        num = int(data[0])
        # 두 번째 인덱스는 연산자 or 피연산자
        value = data[1]

        # data 길이가 2라면 피연산자
        if len(data) == 2:
            node_info[num] = [int(value), None, None]
        # 아니면 연산자
        else:
            left = int(data[2])
            right = int(data[3])
            node_info[num] = [value, left, right]

    # 재귀함수를 이용하여 밑에서부터(후위) 계산
    def calc(node_num):
        value, left, right = node_info[node_num]

        # 숫자 노드라면 value만 반환
        if left is None: return value

        left_val = calc(left)
        right_val = calc(right)

        if value == '+':
            return left_val + right_val
        elif value == '-':
            return left_val - right_val
        elif value == '*':
            return left_val * right_val
        elif value == '/':
            return left_val / right_val

    res = int(calc(1))
    print(f'#{tc + 1} {res}')