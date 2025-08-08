# 중위 표기식을 후위 표기식으로 변환할 함수
def infix_to_postfix(expr):
    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식을 저장할 리스트

    for char in expr:  # 표현식 순회
        # 피연산자인 경우
        if char.isnumeric():  # 정수라면
            postfix.append(char)  # 후위 표기식에 삽입
        else:  # 연산자인 경우
            while stack:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())

    return postfix

# 후위 표기식 계산 함수
def run_calculator(expr):
    stack = []  # 피연산자를 저장할 스택

    for char in expr:  # 표현식 순회
        # 피연산자인 경우
        if char.isnumeric():  # 정수라면
            stack.append(int(char))  # 스택에 삽입
        else:   # + 연산자인 경우
            res = stack.pop() + stack.pop()
            stack.append(res)
    return res


for i in range(10):
    str_length = input()
    calc_formula = input()

    # 중위 표기식을 후위 표기식으로 변환
    postfix_expression = infix_to_postfix(calc_formula)
    # 후위 표기식을 이용해 계산식 계산
    print(f'#{i + 1} {run_calculator(postfix_expression)}')