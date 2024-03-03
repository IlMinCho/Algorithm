# https://www.acmicpc.net/problem/21919

# 소수 최소 공배수
# 문제
# 행복이는 길이가 
# $N$인 수열 
# $A$에서 소수들을 골라 최소공배수를 구해보려고 한다.

# 행복이를 도와 이를 계산해주자.

# 입력
# 첫째 줄에 수열 
# $A$의 길이 
# $N$이 주어진다. 
# $(1 \le N \le 10,000)$ 

# 그 다음줄에는 수열 
# $A$의 원소 
# $A_{i}$가 공백으로 구분되어 주어진다. 
# $(2 \le A_{i} \le 1,000,000)$ 

# 답이 263 미만인 입력만 주어진다.

# 출력
# 첫째 줄에 소수들의 최소공배수를 출력한다.

# 만약 소수가 없는 경우는 -1을 출력한다.
def calculate_lcm_of_primes(N, A):
    from math import gcd
    from functools import reduce

    # 최소공배수(LCM)를 계산하는 함수
    def lcm(a, b):
        return a * b // gcd(a, b)

    # 소수 찾기
    primes = []
    for num in A:
        if num > 1:  # 1보다 큰 수만 고려
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)

    # 소수의 최소공배수 계산
    if primes:
        lcm_result = reduce(lcm, primes)
    else:
        lcm_result = -1

    return lcm_result

N = int(input())
A = list(map(int, input().split()))

# 결과 계산 및 출력
result = calculate_lcm_of_primes(N, A)
print(result)