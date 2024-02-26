# https://www.acmicpc.net/problem/2745

# 진법전환
# 문제
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.
def base_to_decimal(n, b):
    """B진법 수 N을 10진법으로 변환하는 함수"""
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decimal_value = 0
    for digit in n:
        decimal_value = decimal_value * b + digits.index(digit)
    return decimal_value

# 외부 입력값 받기
n, b = input().split()
b = int(b)

# 변환 결과 출력
print(base_to_decimal(n, b))