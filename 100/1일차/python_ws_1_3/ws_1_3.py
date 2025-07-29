users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

# 아래에 코드를 작성하시오.
import adult, active, adult_active

print(f'adult: {adult.adult(users)}')
print(f'activate: {active.active(users)}')
print(f'adult_activate: {adult_active.adult_active(users)}')