import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    parenthesis = input()
    stack = []  # 괄호를 저장할 스택
    cnt = 0     # 잘린 막대기 조각의 총 개수

    for char in parenthesis:
        stack.append(char)

        if char == ')': # 인접한 '('와 ')'
            if stack[-2] == '(':
                cnt += 1

    print(f'#{tc} {cnt}')