# https://www.acmicpc.net/problem/1978

# 소수찾기
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    N = int(input())  # 수의 개수 입력
    numbers = list(map(int, input().split()))  # N개의 수 입력

    # Count primes
    prime_count = sum(is_prime(number) for number in numbers)
    print(prime_count)  # 소수의 개수 출력

main()