| 문제 4 : 이름공간 (배점 15점)

아래 코드의 출력 결과를 예상하고, 인스턴스 변수와 클래스 변수의 탐색 순서와 관련하여 그 이유를 설명하시오.

```python
class MyClass:
    value = 10

obj = MyClass()
obj.value = 20

print(MyClass.value)
print(obj.value)
```

예상 출력 결과
10
20

이유
클래스가 생성이 될 때 클래스 이름 공간이 생성되고, value = 10 에서 클래스 변수가 선언되었다.
그 후 obj라는 MyClass의 인스턴스가 생성될 때, 인스턴스 이름 공간이 생성되어 해당 공간에서 value 값은 20으로 변경되었다.
변수의 탐색 순서는 인스턴스 변수 -> 클래스 변수 순이기 때문에, obj.value는 본인(인스턴스) 공간에 있는 value 값인 20을 가지게 되고, MyClass.value는 본인(클래스) 공간에 있는 value 값인 10을 가지게 된다.

따라서 MyClass.value는 10, obj.value는 20이다.