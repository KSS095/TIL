# 아래에 코드를 작성하시오.
numbers = list(range(1, 11))
print(numbers)

for num in numbers:
    if num == 5: break

    if num % 2 == 0:
        print(num)
    else:
        print(f"{num}은(는) 홀수")