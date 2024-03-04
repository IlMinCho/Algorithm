# https://www.acmicpc.net/problem/21275

# 폰 호석만
# 문제
# 폰 호석만은 진법 변환의 달인이다. 어떤 진법의 수가 주어져도 모든 다른 진법으로의 변환이 가능한 폰 호석만은 새로운 문제를 내기로 했다. 폰 호석만이 내는 문제는 다음과 같이 진행된다.

# 먼저 폰 호석만은 수 3개 X, A, B를 결정한다(0 ≤ X < 263, 2 ≤ A ≤ 36, 2 ≤ B ≤ 36, A ≠ B). 이 때 X는 10진법이다. 그 다음에 X를 A진법으로 표현한 수와 B진법으로 표현한 수를 종이에 써 놓는다.

# 그 다음에 종이에 써져 있는 두 개의 수를 여러분에게 보여주게 된다. 주어진 두 개의 수를 통해 원래 숫자인 X, A, B를 계산해주자. 만약 조건을 만족하는 (X, A, B)로 가능한 조합이 여러 개라면 "Multiple"을 출력하고, 가능한 조합이 없다면 "Impossible"를 출력한다.

# 입력
# 첫번째 줄에 X를 A진법으로 표현한 값과 X를 B진법으로 표현한 값이 공백으로 구분되어 주어진다. 각 자리수는 0 이상 z 이하이다. a부터 z 는 10부터 35 를 의미한다.

# 단, 0을 제외한 각 수는 0 으로 시작하지 않으며, 길이는 최대 70 이다.

# 출력
# 만약 문제의 조건에 맞는 X, A, B가 유일하게 존재한다면, X를 십진법으로 표현한 수와 A와 B를 공백으로 나누어 출력하라. 만약 만족하는 경우가 2가지 이상이라면 "Multiple"을, 없다면 "Impossible"을 출력하라.

# 제한
# 0 ≤ X < 263
# 2 ≤ A ≤ 36
# 2 ≤ B ≤ 36
# A ≠ B
# X는 0 혹은 양의 정수, A와 B는 양의 정수이다.
def find_base(num_str):
    max_digit = max(num_str)
    if max_digit.isdigit():
        return max(int(max_digit) + 1, 2)
    else:
        return max(ord(max_digit) - ord('a') + 10 + 1, 2)

def to_decimal(num_str, base):
    decimal = 0
    for digit in num_str:
        if digit.isdigit():
            decimal = decimal * base + int(digit)
        else:
            decimal = decimal * base + ord(digit) - ord('a') + 10
    return decimal

def find_XAB(num1, num2):
    base1_min = find_base(num1)
    base2_min = find_base(num2)
    solutions = []

    for base1 in range(base1_min, 37):
        dec1 = to_decimal(num1, base1)
        if dec1 >= 2**63:
            break
        for base2 in range(base2_min, 37):
            if base1 == base2:
                continue
            dec2 = to_decimal(num2, base2)
            if dec1 == dec2:
                solutions.append((dec1, base1, base2))
                if len(solutions) > 1:
                    return "Multiple"
    
    if len(solutions) == 1:
        return f"{solutions[0][0]} {solutions[0][1]} {solutions[0][2]}"
    else:
        return "Impossible"

# 사용자로부터 입력 받기
if __name__ == "__main__":
    num1_input, num2_input = input().split()
    result = find_XAB(num1_input, num2_input)
    print(result)