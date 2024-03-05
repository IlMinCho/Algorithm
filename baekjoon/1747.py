# https://www.acmicpc.net/problem/1747

# 소수&팰린드롬
# 문제
# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.

# 어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다.

# 출력
# 첫째 줄에 조건을 만족하는 수를 출력한다.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_smallest_prime_palindrome(N):

    while True:
        if is_palindrome(N) and is_prime(N):
            return N
        N += 1

N = int(input())  # This is just an example; replace with any method to set N
print(find_smallest_prime_palindrome(N))