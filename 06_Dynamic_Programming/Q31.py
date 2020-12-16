'''
Q31 금광
n * m 크기의 금광이 있습니ㅏㄷ.
금광은 2 * 1크리의 칸으로 나누어져 있으며, 각 칸은 특정한 크시의 금이 들어 있습니다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다.
맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

만약 다음과 같이 3 * 4크기의 금광이 존재한다고 가정합시다.
1  3  3  2
2  1  4  1
0  6  4  7

가장 왼쪽 위의 위치를 (1, 1), 가장 오른쪽 아래의 위치를 (n, m)이라고 할 때, 
위 예시에서는 (2, 1) -> (3, 2) -> (3, 3) -> (3, 4)의 위치로 이동하면 총 19만큼의 금을 채굴할 수 있으며, 이때의 값이 최댓값입니다.

<입력 조건>
- 첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
- 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20)
  둘쩨 줄에 n * m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1 <= 각 위치에 매장된 금의 개수 <= 100)

<출력 조건>
- 테스트 케이스마다 채굴자가 얻을 수 있는 금의 초대 크기를 출력합니다. 각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.

<입력 예시>
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

<출력 예시>
19
16
'''

# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
        
    print(result)