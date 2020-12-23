'''
구간 합 문제: 연속적으로 나열된 N개의 수가 있을 때, 틀정 구간의 모든 수를 합한 값을 구하는 문제.
M개의 쿼리가 존재하고, 각 쿼리는 [Left, Roght]의 구간을 갖는다.
시간 복잡도: O(NM)

접두사 합
각 쿼리에 대해 구간 합을 빠르게 계산하기 위해서는 N개의 수의 위치 각각에 대하여 접두사 합을 미리 구해 놓으면 된다.
리스트 맨 앞부터 특정 위치까지의 합을 구해 놓은 것을 의미.

1. N개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장한다.
2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L - 1]이다.
시간 복잡도: O(N + M)
'''

# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1]) # 70