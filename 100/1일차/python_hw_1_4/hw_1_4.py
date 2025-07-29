'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.
students = {'Alice': 85, 'Bob': 78, 'Charlie': 92, 'David': 88, 'Eve': 95}
students_items = list(students.items())

# 모든 학생의 평균 점수를 계산하여 출력
avg_score = sum(students.values()) / 5

print(f'평균 : {avg_score}\n')


# 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출
good_score_students = [name for name, score in students_items if score >= 80]

print(f'80점 이상: {good_score_students}\n')


# 학생들의 점수를 높은 순서대로 정렬하여 출력
ordered_students = sorted(students_items, key=lambda item:item[1], reverse=True)

print('점수 높은 순')
for name, score in ordered_students:
    print(name)
print()


# 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력
print(f'점수 차이 : {ordered_students[0][1] - ordered_students[4][1]}\n')

# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력
bad_score_students = [(name, score) for name, score in students_items if score < avg_score]
print(f'평균 아래 학생 : {bad_score_students}')