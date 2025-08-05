import sys
sys.stdin = open('sample_input.txt')

T = int(input())    # 테스트케이스 입력
for tc in range(T):
    N = int(input())    # 숫자(피연산자) 개수 입력

    operator = list(map(int, input().split()))      # 연산자(개수)를 입력받아 리스트에 저장 ('+', '-', '*', '/' 순)
    operand = list(map(int, input().split()))       # 피연산자를 입력받아 리스트에 저장

    # 연산 중의 값은 -100,000,000 이상 100,000,000 이하임이 보장
    max_val = -100000000
    min_val = 100000000

    # dfs
    def dfs(depth, result, operators):
        global max_val, min_val

        # 모든 연산이 끝났을 때
        if depth == N - 1:
            max_val = max(max_val, result)  # 연산 최댓값 갱신
            min_val = min(min_val, result)  # 연산 최솟값 갱신
            return

        # 모든 연산자 사용
        for i in range(4):
            if operators[i] > 0:  # 해당 연산자가 남아있다면
                operators[i] -= 1  # 연산자 사용

                if i == 0:  # 덧셈
                    dfs(depth + 1, result + operand[depth + 1], operators)
                elif i == 1:  # 뺄셈
                    dfs(depth + 1, result - operand[depth + 1], operators)
                elif i == 2:  # 곱셈
                    dfs(depth + 1, result * operand[depth + 1], operators)
                elif i == 3:  # 나눗셈
                    if result < 0:  # 음수 나눗셈
                        new_result = -((-result) // operand[depth + 1])
                    else:
                        new_result = result // operand[depth + 1]
                    dfs(depth + 1, new_result, operators)

                operators[i] += 1  # 연산자 복원

    dfs(0, operand[0], operator[:])  # operator 복사본 전달

    print(f'#{tc + 1} {max_val - min_val}')


# # 순열 이용 (시간 개 오래걸림)
# from itertools import permutations
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     operator_counts = list(map(int, input().split()))  # ['+'개수, '-'개수, '*'개수, '/'개수]
#     operands = list(map(int, input().split()))
#
#     # 연산자 배열 생성
#     op = []
#     op.extend(['+'] * operator_counts[0])
#     op.extend(['-'] * operator_counts[1])
#     op.extend(['*'] * operator_counts[2])
#     op.extend(['/'] * operator_counts[3])
#
#     max_result = float('-inf')
#     min_result = float('inf')
#
#     # 모든 연산자 순열에 대해 계산
#     for perm in permutations(op):
#         result = operands[0]  # 첫 번째 피연산자로 시작
#
#         # 각 연산자에 대해 순차적으로 계산
#         for i in range(len(perm)):
#             if perm[i] == '+':
#                 result += operands[i + 1]
#             elif perm[i] == '-':
#                 result -= operands[i + 1]
#             elif perm[i] == '*':
#                 result *= operands[i + 1]
#             elif perm[i] == '/':
#                 # 음수 나눗셈 처리
#                 if result < 0:
#                     result = -((-result) // operands[i + 1])
#                 else:
#                     result = result // operands[i + 1]
#
#         max_result = max(max_result, result)
#         min_result = min(min_result, result)
#
#     print(f'#{tc + 1} {max_result - min_result}')