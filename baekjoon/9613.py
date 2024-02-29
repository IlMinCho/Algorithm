# https://www.acmicpc.net/problem/9613

# GCD 합
# 문제
# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

# 출력
# 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다. 

# from math import gcd

# def calculate_gcd_sum():
#     t = int(input())  # 사용자로부터 테스트 케이스의 개수를 입력받음
#     for _ in range(t):
#         # 각 테스트 케이스에 대한 입력: 첫 번째 숫자는 숫자의 개수, 이후 숫자들은 해당 테스트 케이스의 숫자들
#         case = list(map(int, input().split()))
#         sum_gcd = 0
#         for i in range(1, len(case)):
#             for j in range(i+1, len(case)):
#                 sum_gcd += gcd(case[i], case[j])
#         print(sum_gcd)

# # 메인 함수 실행
# if __name__ == "__main__":
#     calculate_gcd_sum()

def gcd_manual(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_gcd_sum_manual():
    t = int(input())  # 사용자로부터 테스트 케이스의 개수를 입력받음
    for _ in range(t):
        # 각 테스트 케이스에 대한 입력: 첫 번째 숫자는 숫자의 개수, 이후 숫자들은 해당 테스트 케이스의 숫자들
        case = list(map(int, input().split()))
        sum_gcd = 0
        for i in range(1, len(case)):
            for j in range(i+1, len(case)):
                sum_gcd += gcd_manual(case[i], case[j])
        print(sum_gcd)

# 메인 함수 실행
if __name__ == "__main__":
    calculate_gcd_sum_manual()