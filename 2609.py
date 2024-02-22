# https://www.acmicpc.net/problem/2609

# 최대공약수와 최소공배수

# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
def gcd(a, b):
    """두 수의 최대공약수를 계산하는 함수"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """두 수의 최소공배수를 계산하는 함수"""
    return a * b // gcd(a, b)

def main():
    # 두 자연수 입력 받기
    a, b = map(int, input().split())

    # 최대공약수와 최소공배수 계산
    gcd_result = gcd(a, b)
    lcm_result = lcm(a, b)

    # 결과 출력
    print(gcd_result)
    print(lcm_result)

if __name__ == "__main__":
    main()