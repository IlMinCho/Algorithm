# 4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.

# 이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램을 작성한다.

# 예를 들어 아래와 같은 문자열은 유효하다고 판단할 수 있다.

# 아래와 같은 문자열은 유효하지 않은 문자열이다. 붉은색으로 표시된 괄호의 짝을 찾을 수 없기 때문이다.

# 아래 문자열은 열고 닫는 괄호의 개수는 유효하나 짝이 맞지 않는 괄호가 사용 되었기 때문에 유효하지 않다.

# [입력]

# 각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 길이가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

# 총 10개의 테스트케이스가 주어진다.

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 유효성 여부를 1 또는 0으로 표시한다 (1 - 유효함, 0 - 유효하지 않음).


def is_valid_brackets(test_case):
    # 괄호 짝을 맞추기 위한 딕셔너리
    brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
    stack = []

    for char in test_case:
        if char in brackets.values():  # 여는 괄호인 경우
            stack.append(char)
        elif char in brackets.keys():  # 닫는 괄호인 경우
            if stack == [] or stack.pop() != brackets[char]:
                return 0  # 유효하지 않음

    return 1 if not stack else 0  # 스택이 비어 있으면 유효함

# 입력 및 출력 처리
for t in range(1, 11):
    length = int(input())  # 문자열 길이
    test_case = input().strip()  # 괄호 문자열
    result = is_valid_brackets(test_case)
    print(f"#{t} {result}")
