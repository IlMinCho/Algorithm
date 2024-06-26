# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

# 예를 들어

# “3+(4+5)*6+7”

# 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

# "345+6*+7+"

# 변환된 식을 계산하면 64를 얻을 수 있다.

# 문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

# 이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

# 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

# [입력]

# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

# 총 10개의 테스트 케이스가 주어진다.

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

def infix_to_postfix(expression):
    """중위 표기식을 후위 표기식으로 변환하는 함수"""
    precedence = {'+': 1, '*': 2, '(': 0}
    output = []
    operators = []
    
    for char in expression:
        if char.isdigit():  # 피연산자인 경우
            output.append(char)
        elif char == '(':  # 여는 괄호는 스택에 쌓는다
            operators.append(char)
        elif char == ')':  # 닫는 괄호는 여는 괄호를 만날 때까지 연산자를 출력
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # 여는 괄호 제거
        elif char in precedence:  # 연산자인 경우
            while operators and precedence[operators[-1]] >= precedence[char]:
                output.append(operators.pop())
            operators.append(char)
    
    while operators:
        output.append(operators.pop())
    
    return ''.join(output)

def evaluate_postfix(expression):
    """후위 표기식을 계산하는 함수"""
    stack = []
    
    for char in expression:
        if char.isdigit():  # 피연산자인 경우
            stack.append(int(char))
        elif char in {'+', '*'}:  # 연산자인 경우
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '*':
                stack.append(a * b)
    
    return stack[0]

# 테스트 케이스 처리
for tc in range(1, 11):
    length = int(input().strip())
    expression = input().strip()
    
    postfix_expression = infix_to_postfix(expression)
    result = evaluate_postfix(postfix_expression)
    
    print(f"#{tc} {result}")