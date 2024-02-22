# https://www.acmicpc.net/problem/5618

# 공약수
# 문제
# 자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 2 또는 3이다. 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다. 모든 자연수는 108 이하이다.

# 출력
# 입력으로 주어진 n개 수의 공약수를 한 줄에 하나씩 증가하는 순서대로 출력한다.
def gcd(a, b):
    """유클리드 호제법을 사용하여 최대공약수를 구하는 함수"""
    while b != 0:
        a, b = b, a % b
    return a

def find_gcd_of_list(lst):
    """리스트 내의 모든 요소에 대한 최대공약수를 찾는 함수"""
    n = lst[0]
    for i in range(1, len(lst)):
        n = gcd(n, lst[i])
    return n

def find_divisors(n):
    """주어진 수의 약수를 모두 찾는 함수"""
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# 외부로부터 입력값을 받는 부분
n = int(input())
numbers = list(map(int, input().split()))

# 최대공약수 및 공약수 찾기
gcd_value = find_gcd_of_list(numbers)
divisors = find_divisors(gcd_value)

# 공약수 출력
for divisor in divisors:
    print(divisor)