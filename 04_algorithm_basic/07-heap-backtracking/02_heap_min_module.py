import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

# 리스트를 최소 힙으로 변환
heapq.heapify(numbers)
print(numbers)

heapq.heappush(numbers, -1)
print(numbers)

smallest = heapq.heappop(numbers)
print(smallest)
print(numbers)