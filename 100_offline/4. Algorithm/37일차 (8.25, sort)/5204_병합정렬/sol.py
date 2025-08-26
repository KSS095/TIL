import sys
sys.stdin = open('sample_input.txt')


# 나누는 파트
def merge_sort(arr):
    n = len(arr)

    # 배열의 길이가 1 이하인 경우, 배열을 반환
    # 더 이상 나눌 수 없는 경우
    if n <= 1:
        return arr

    mid = n // 2  # 배열을 반으로 나눌 중간 인덱스를 구함
    left_half = arr[:mid]  # 왼쪽 절반 배열
    right_half = arr[mid:]  # 오른쪽 절반 배열

    # 왼쪽 절반과 오른쪽 절반을 재귀적으로 병합 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 정렬된 두 절반을 병합
    # 더 이상 나눌 수 없는 부분까지 가면 아래 코드가 실행되고
    # 합쳐진 결과는 다시 15,16 라인에서 결과가 변수에 할당되면서
    # 재귀를 탈출하면서 결과를 구함
    return merge(left_half, right_half)


# 합치는 파트
def merge(left, right):
    global count
    result = []  # 병합된 결과를 저장할 리스트
    if left[len(left) - 1] > right[len(right) - 1]:
        count += 1

    i, j = 0, 0
    # 왼쪽 배열과 오른쪽 배열이 모두 비어있지 않은 동안 반복
    while i < len(left) and j < len(right):
        # 왼쪽 배열의 첫 번째 요소가 오른쪽 배열의 첫 번째 요소보다 작은 경우
        if left[i] < right[j]:
            result.append(left[i])  # 왼쪽 배열의 첫 번째 요소를 결과에 추가
            i += 1
        else:
            result.append(right[j])  # 오른쪽 배열의 첫 번째 요소를 결과에 추가
            j += 1

    # 왼쪽 배열에 남은 요소들을 결과에 추가
    result.extend(left[i:])
    # 오른쪽 배열에 남은 요소들을 결과에 추가
    result.extend(right[j:])
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0   # 오른쪽 원소가 먼저 복사되는 경우의 수

    arr = merge_sort(arr)

    print(f'#{tc} {arr[N // 2]} {count}')