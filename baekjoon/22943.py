# https://www.acmicpc.net/problem/22943

# 수
# 문제
# 0부터 9까지 
# $K$가지의 숫자를 한 번씩만 사용하여 만들 수 있는 수 중 아래 조건을 모두 만족하는 수들의 개수를 구해보자. 단, 수의 맨 앞에는 0이 올 수 없다. 즉, 0143는 불가능하다.

# 서로 다른 두 개의 소수의 합으로 나타낼 수 있는 경우
#  
# $M$으로 나누어 떨어지지 않을때까지 나눈 수가 두 개의 소수의 곱인 경우, 이 때, 두 개의 소수가 같아도 된다.
# 예를 들어, 
# $K$가 1이고 
# $M$이 11인 경우로 생각해보자. 한자리 수 중 1번 조건을 만족하는 수는 5, 7, 8, 9이고 2번 조건을 만족하는 수는 4, 6, 9가 있다. 이 두개의 조건을 둘다 만족하는 수는 9이므로 이 경우에는 1개이다.

# 입력
# 첫 번째 줄에 
# $K$와 
# $M$ 주어진다.

# 출력
# 2가지 조건을 만족하는 수의 개수를 출력한다.

# from itertools import permutations
# from math import sqrt

# # 1. 소수 찾기: 에라토스테네스의 체 알고리즘 사용
# def get_primes(n):
#     sieve = [True] * (n+1)
#     primes = []
#     for i in range(2, n+1):
#         if sieve[i]:
#             primes.append(i)
#             for j in range(i*i, n+1, i):
#                 sieve[j] = False
#     return primes

# # 2. 소수의 합으로 만들 수 있는 값들 찾기
# def prime_sums(primes, n):
#     prime_sum = [False] * (n+1)
#     for i in primes:
#         for j in primes:
#             if i != j and i + j <= n:
#                 prime_sum[i + j] = True
#     return prime_sum

# # 3. 소수의 곱으로 만들 수 있는 값들 찾기
# def prime_products(primes, n):
#     prime_product = [False] * (n+1)
#     for i in primes:
#         for j in primes:
#             if i * j <= n:
#                 prime_product[i * j] = True
#     return prime_product

# # 4. M으로 나누어 떨어지지 않을 때까지 나눈 수가 소수의 곱인지 확인
# def check_divisible_by_m(n, m, prime_product):
#     while n % m == 0:
#         n //= m
#     return prime_product[n]

# # 5. K가지 숫자로 이루어진 수인지 확인
# def is_k_digit_number(num, k):
#     return len(str(num)) == k and len(set(str(num))) == k

# # 메인 함수: 조건을 만족하는 수의 개수 계산
# def count_valid_numbers(k, m):
#     max_num = 10**k - 1
#     primes = get_primes(max_num)
#     prime_sum = prime_sums(primes, max_num)
#     prime_product = prime_products(primes, max_num)
#     count = 0
    
#     for num in range(10**(k-1), max_num+1):
#         if is_k_digit_number(num, k) and prime_sum[num] and check_divisible_by_m(num, m, prime_product):
#             count += 1
    
#     return count

# # 입력 받기
# k, m = map(int, input().split())

# # 결과 출력
# print(count_valid_numbers(k, m))

import math
from itertools import permutations

MAX = 1000001
is_prime = [True] * MAX

# 에라토스테네스의 체를 사용하여 소수 리스트를 생성하는 함수
def make_prime():
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX, i):
                is_prime[j] = False

# M으로 나누어 떨어지지 않을 때까지 나누는 함수
def divide_until_not_divisible(num, k):
    while num % k == 0 and num >= k:
        num //= k
    return num

# 조건 1: 서로 다른 두 개의 소수의 합으로 나타낼 수 있는지 확인하는 함수
def condition_1(n):
    for i in range(2, n // 2 + 1):
        if i != n - i and is_prime[i] and is_prime[n - i]:
            return True
    return False

# 조건 2: 소수의 곱으로 나타낼 수 있는지 확인하는 함수
def condition_2(n, k):
    n = divide_until_not_divisible(n, k)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime[i] and is_prime[n // i]:
            return True
    return False

# 소수 리스트 생성
make_prime()

# 입력 받기
K, M = map(int, input().split())

# 유효한 숫자의 개수 계산
answer = 0
for num in permutations('0123456789', K):
    if num[0] == '0':  # 첫 자리가 0인 경우 제외
        continue
    num = int(''.join(num))
    if condition_1(num) and condition_2(num, M):
        answer += 1

# 결과 출력
print(answer)