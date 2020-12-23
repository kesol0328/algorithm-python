'''
소수: 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수.

어떠한 수 X가 주어졌을 때 해당 수가 소수인지 아닌지 판별하는 방법은
X를 2부터 X - 1까지의 모든 자연수로 나누었을 때 나누어떨어지는 수가 하나라도 존재하면 X는 소수가 아니다.
시간 복잡도: O(X) 비효율적임.

X의 제곱근까지만 확인하는 방법 사용
시간 복잡도: O(X^(1/2))
'''

import math

#소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True