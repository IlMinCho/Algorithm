# https://www.acmicpc.net/problem/4134

# 다음소수
# 문제
# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

# 출력
# 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.
import math

# 소수 판별 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 소수 찾는 함수
def find_next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1

# 메인
def main():
    # 테스트 케이스 수 입력
    t = int(input())
    # 각 테스트 케이스에 대해
    for _ in range(t):
        n = int(input())
        print(find_next_prime(n))

if __name__ == "__main__":
    main()