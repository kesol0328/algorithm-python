'''
Q28 고정점 찾기
고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다.
예를 들어 수열 a = {-15, -4, 2, 8, 13}이 있을 때 a[2] = 2이므로, 고정점은 2가 됩니다.
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하게요.
만약 고정점이 없다면 -1을 출력합니다.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.

<입력 조건>
- 첫째 줄에 N이 입력됩니다. (1 <= N <= 1,000,000)
- 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-10^9 <= 각 원소의 값 <= 10^9)

<출력 조건>
- 고정점을 출력한다. 고정점이 없다면 -1을 출력합니다.

<입력 예시 1>
5
-15 -6 1 3 7

<출력 예시 1>
3

<입력 예시 2>
7
-15 -4 2 8 9 13 15

<출력 예시 2>
2

<입력 예시 3>
7
-15 -4 3 8 9 13 15

<출력 예시 3>
-1s

'''

# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

# 이진 탐색(Binary Search) 수행
index = binary_search(array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 고정점이 있는 경우 해당 인덱스 출력
else:
    print(index)