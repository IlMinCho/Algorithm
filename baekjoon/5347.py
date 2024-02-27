# https://www.acmicpc.net/problem/5347

# LCM
# 문제
# 두 수 a와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 n이 주어진다. 다음 n개 줄에는 a와 b가 주어진다. a와 b사이에는 공백이 하나 이상 있다. 두 수는 백만보다 작거나 같은 자연수이다.

# 출력
# 각 테스트 케이스에 대해서 입력으로 주어진 두 수의 최소공배수를 출력한다.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())  # 사용자로부터 테스트 케이스의 수를 입력받음

for _ in range(n):
    a, b = map(int, input().split())  # 사용자로부터 두 수를 입력받음
    print(lcm(a, b))  # 계산된 최소공배수를 출력