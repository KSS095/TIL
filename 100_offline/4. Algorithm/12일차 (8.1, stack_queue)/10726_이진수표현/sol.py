tc = int(input())

for i in range(tc):
    res = 'ON'  # 결과를 저장할 문자열
    N, M = map(int, input().strip().split())
    binary_M = bin(M)[2:]   # 입력받은 M을 이진수로 변환 (앞의 '0b'는 제거)

    stack = []  # 변환된 이진수를 저장할 스택
    for idx in range(len(binary_M)):    # 스택에 이진수 삽입
        stack.append(binary_M[idx])

    # stack이 비거나, 마지막 N개의 비트에 0이 포함되었으면 res = 'OFF'
    for _ in range(N):
        if not stack or stack.pop() == '0':
            res = 'OFF'
            break

    print(f'#{i + 1} {res}')