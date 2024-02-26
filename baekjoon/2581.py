# https://www.acmicpc.net/problem/2581

# 소수
# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(m, n):
    """Find all prime numbers in the range [m, n]."""
    primes = [i for i in range(m, n+1) if is_prime(i)]
    if primes:
        return sum(primes), primes[0]
    else:
        return -1, -1

# 사용자로부터 M과 N 값을 입력받음
m = int(input())
n = int(input())

# 주어진 범위 내의 소수 찾기 및 결과 출력
sum_primes, min_prime = find_primes_in_range(m, n)

# 결과 출력
if sum_primes == -1:
    print(-1)
else:
    print(sum_primes)
    print(min_prime)