'''
투 포인터: 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
2개의 변수를 이용해 리스트 상의 위치를 기록한다.
부분 연속 수열의 시작점과 끝점의 위치를 기록한다.
특정한 부분합을 M이라고 할 때, 구체적인 알고리즘은 다음과 같다.

1. 시작점(start)과 끝점이(end) 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
2. 현재 부분합이 M과 같다면 카운트한다.
3. 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.
'''

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)