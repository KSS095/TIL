# import sys
# sys.stdin = open('input.txt')

for tc in range(10):
    width = int(input())    # 한 변의 길이
    table = [list(map(int, input().split())) for _ in range(width)]
    deadlock = 0    # 교착상태 개수 저장할 변수

    # table을 순회
    for col in range(width):
        stack = []  # 교착상태 확인
        for row in range(width):
            # 자성체가 N극을 띠고 스택이 비어있다면 스택 채우기
            if table[row][col] == 1 and not stack:
                stack.append(table[row][col])
            # 자성체가 S극이고
            elif table[row][col] == 2:
                # 스택에 N극이 있다면 deadlock 1 증가 및 스택 비우기
                if stack:
                    deadlock += 1
                    stack.pop()

    print(f"#{tc + 1} {deadlock}")