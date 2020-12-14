'''
Q27 정렬된 배열에서 특정 수의 개수 구하기
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계사지 않으면 '시간 초과' 판정을 받습니다.

<입력 조건>
- 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다.
(1 <= N <= 1,000,000), (-10^3 <= x <= 10^9)
- 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
(-10^9 <= 각 원소의 값 <= 10^9)

<출력 조건>
- 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가 하나도 없으면 -1을 출력합니다.

<입력 예시 1>
7 2
1 1 2 2 2 2 3

<출력 예시 1>
4

<입력 예시 2>
7 4
1 1 2 2 2 2 3

<출력 예시 2>
-1
'''

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return last(array, target, mid + 1, end)

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x를 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 x인 데이터의 개수 계산
count = count_by_value(array, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)