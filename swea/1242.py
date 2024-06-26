# 어떤 국가에서는 자국 내 방송국에서 스파이가 활동하는 사실을 알아냈다. 스파이는 영상물에 암호 코드를 삽입하여 송출하고 있었다.
# 암호 코드는 국가 내 중요 시설을 의미하는 숫자임을 알아냈다. 암호 코드의 규칙은 아래와 같다.
 
# 1. 총 8개의 숫자로 이루어져 있다.

# 2. 앞 7자리는 상품 고유의 번호를 나타내며, 마지막 자리는 검증 코드를 나타낸다.

#     - 검증코드는 아래와 같은 방법으로 계산한다.
#     “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.

#     상품 고유의 번호가 8801234일 경우,
#     “( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 ) + 검증 코드”
#     = “42 + 12 + 검증 코드”
#     = “54 + 검증 코드” 가 10 의 배수가 되어야 하므로, 검증코드는 6이 되어야 한다
#         그 외의 검증코드가 포함된 경우 비정상적인 암호코드다.

#     즉, 88012346 이 정상적인 암호코드다.

# A 업체에서는 이 암호코드들을 빠르고 정확하게 인식할 수 있는 스캐너를 개발하려고 한다. 스캐너의 성능은 아래와 같은 방법으로 측정된다.

# 1. 세로 2000. 가로 500 이하의 크기를 가진 직사각형 배열에 암호코드 정보가 포함되어 전달된다.

# 2. 배열은 16진수로 이루어져 있으며, 이 배열을 2진수로 변환하여 그 안에 포함되어 있는 암호코드 정보를 확인해야한다.

# 3. 배열에는 1개 이상의 암호코드가 존재한다. (모든 암호코드가 정상적인 암호코드임을 보장할 수 없다. 비정상적인 암호코드가 포함될 수 있다.)

# 4. 포함된 암호코드들의 고유번호와 검증코드를 확인하여 정상여부를 판별한 뒤 이 정상 암호코드들에 적혀있는 숫자들의 합을 출력한다.

# 5. 총 소요시간이 적을수록 성능이 좋은 것으로 간주된다.


# 배열에 포함되어 있는 암호코드의 세부 규칙은 아래와 같다.

# - 암호코드 하나는 숫자 8개로 구성된다. (7개 고유번호 + 1개 검증코드) 암호코드가 일부만 표시된 경우는 없다. 모든 암호코드는 8개의 숫자로 구성되어 있다.

# - 각 숫자 하나가 차지하는 최소 칸수는 7이다. (최소 7개 비트)  즉, 암호코드 하나의 최소 가로 길이는 56이다.
#   두께가 가장 가는 경우에서의 각 숫자들을 표현하는 방식은 그림1을 참고하라.

# - 암호코드의 가로 길이는 암호코드 선의 두께에 따라 달라지며 암호코드 선이 굵어질 경우, 56의 배수의 길이를 갖게 된다. 
#   예를 들어 암호코드 숫자 하나가 14칸을 사용하는 경우, 암호코드 하나의 가로길이는 112가 된다. 암호코드 하나에 포함되는 암호코드 숫자들은 모두 동일한 크기를 갖는다.
#   두께가 2배가 되었을 때 경우는 그림2를 참고하라.

# - 암호코드의 시작 구분선, 종료 구분선은 별도로 존재하지 않는다.

# - 암호코드의 세로 길이는 5 ~ 100 칸이다.

# - 암호코드들이 붙어있는 경우는 존재하지 않는다. (각 암호코드의 둘레에는 최소 1칸 이상의 빈 공간이 존재한다.)

# 그림1

# 그림2

# 그림2 설명:
# 각 숫자는 흰색과 파란색의 넓이 비로 표현된다. 암호코드의 가로 길이가 길어질 경우, 숫자 하나가 차지하는 길이는 7의 배수가 된다. 예를 들어, 가로 길이가 2배가 될 경우 9는 아래와 같이 표시될 수 있다.



# 암호코드 정보가 포함된 2차원 배열을 입력으로 받아 정상적인 암호코드를 판별 후 출력하는 프로그램을 작성하라.

# [입력]

# 표준 입력으로 T개의 테스트 케이스가 이어져서 주어진다.

# 각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N<2000, 1≤M<500).

# 그 다음 N 개의 줄에는 M개의 배열의 값이 주어진다. 문제의 모든 배열의 값은 16진수이다.

# [출력]

# 각 테스트 케이스의 답을 순서대로 표준출력으로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다. 이때 C는 케이스의 번호이다.

# 같은 줄에 빈칸을 하나 두고, 입력에 주어진 배열에서 정상적인 암호코드들에 포함된 숫자들의 합을 출력한다.

# [참고]

# 각 테스트 케이스의 구성은 아래와 같다.
 
# 테스트 케이스	 N * M	암호코드 가로 길이	암호코드 개수
# 그룹 1	100 * 26	56	1
# 그룹 2	200 * 50	56 ~ 112	2
# 그룹 3	500 * 126	56 ~ 280	5
# 그룹 4	1000 * 250	제한 없음	제한 없음
# 그룹 5	2000 * 500	제한 없음	제한 없음

# [예제 풀이]

# 1번 케이스의 암호코드 정보를 변환하면 아래와 같다.

# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
 
# 이 숫자가 나타내는 정보는 각각 아래와 같다.
# 0111011(7) 0110001(5) 0111011(7) 0110001(5) 0110001(5) 0001101(0) 0010011(2) 0111011(7)
 
# 검증코드가 맞는지 살펴보면, (7 + 7 + 5 + 2) * 3 + 5 + 5 + 0 + 7 = 80 이므로 올바른 암호코드라고 할 수 있다. 따라서 1번의 출력 값은 38이 된다.
 
# 2번 케이스도 같은 방식으로 계산할 경우, 328D1AF6E4C9BB 는 14468227 이 되며, 검증코드가 틀렸음을 알 수 있다.

# 196EBC5A316C578 는 18694956이 되며, 검증코드가 맞음을 알 수 있다.

# 따라서 2번의 출력 값은 올바른 암호코드인 18694956의 값만 더한 48이 된다.

# def hex_to_bin(hex_string):
#     # 16진수 문자열을 2진수 문자열로 변환
#     return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

# def decode_password(binary_code):
#     CODE_MAP = {
#         "0001101": 0,
#         "0011001": 1,
#         "0010011": 2,
#         "0111101": 3,
#         "0100011": 4,
#         "0110001": 5,
#         "0101111": 6,
#         "0111011": 7,
#         "0110111": 8,
#         "0001011": 9,
#     }
    
#     digits = []
#     for i in range(0, 56, 7):
#         segment = binary_code[i:i + 7]
#         if segment in CODE_MAP:
#             digits.append(CODE_MAP[segment])
#         else:
#             return []
#     return digits

# def is_valid_password(digits):
#     if len(digits) != 8:
#         return False
    
#     odd_sum = sum(digits[i] for i in range(0, 8, 2))
#     even_sum = sum(digits[i] for i in range(1, 8, 2))
#     check_sum = (odd_sum * 3) + even_sum
#     return check_sum % 10 == 0

# def process_case():
#     # 입력 받기
#     N, M = map(int, input().split())
#     hex_matrix = [input().strip() for _ in range(N)]
    
#     unique_codes = set()
#     valid_sum = 0
    
#     for hex_line in hex_matrix:
#         binary_line = hex_to_bin(hex_line)
#         # 암호 코드 부분 찾기 (오른쪽 끝부터 왼쪽으로 검색)
#         for i in range(len(binary_line) - 1, 55, -1):
#             if binary_line[i] == '1':
#                 end = i + 1
#                 start = end - 56
#                 if start < 0:
#                     continue
#                 code = binary_line[start:end]
#                 if code not in unique_codes:
#                     unique_codes.add(code)
#                     digits = decode_password(code)
#                     if digits and is_valid_password(digits):
#                         valid_sum += sum(digits)
    
#     return valid_sum

# # 전체 테스트 케이스 처리
# test_cases = int(input())
# for tc in range(1, test_cases + 1):
#     result = process_case()
#     print(f"#{tc} {result}")

def ten_to_binary(n):  # 10진수를 2진수로 변환
    ans = ''
    for i in range(4):  # 4자리
        ans = str(n % 2) + ans  # 나머지를 왼쪽에 붙여준다.
        n //= 2
    return ans

def hex_to_binary(n):
    ans = ''
    for c in n:  # 입력받은 16진수 순회
        if c.isdigit():  # 숫자인 경우
            ans += ten_to_binary(int(c))
        else:  # 문자인 경우 딕셔너리 활용
            ans += ten_to_binary(hex_c[c])
    return ans

def search_code():  # 메인 함수, 총 암호 해독 값의 합을 찾는다.
    total = 0
    for i in range(len(arr)):  # 줄 별로 확인
        binary_line = hex_to_binary(arr[i])
        arr[i] = binary_line
        while '1' in binary_line:  # '1'이 더 이상 없으면 종료
            e, width = code_status(binary_line)  # 코드의 너비와 끝점을 받아온다.
            if e == -1:  # 유효한 끝점을 찾지 못한 경우
                break
            binary = binary_line[e - 56 * width + 1:e + 1: width]  # 코드 길이로 자르기
            if binary not in visited:  # 중복된 코드가 있으면 보지 않는다.
                total += solve_code(binary)
                visited.add(binary)
            binary_line = binary_line[:e - 56 * width + 1].rstrip('0')  # 확인한 코드는 제거 후 배열에서 오른쪽 0을 다 지운다.
    return total

def code_status(line):  # 너비와 끝점 찾는 함수
    cnt, e = 0, -1  # 암호의 길이와 끝점, 유효하지 않은 끝점은 -1
    current = '0'  # 암호를 확인하고 값을 저장
    change = 0  # 네번 바뀌는지 파악하기 위한 변수
    for j in range(len(line))[::-1]:
        if current != line[j]:
            if change == 4:  # 4번 바뀌면 종료
                break
            change += 1
            current = line[j]
        if line[j] == '1':
            if cnt == 0:
                e = j  # 끝 점 기억
            cnt += 1  # 1 개수 세기
        if cnt and line[j] == '0':
            cnt += 1  # 0 개수 세기
    width = cnt // 7  # 7의 몇 배수인지 파악
    if cnt % 7 != 0:  # 암호 코드가 7의 배수가 아닌 경우 무효 처리
        return -1, -1
    return e, width  # 끝점과 너비

def solve_code(code):  # 암호 시작점을 받아 해독한다.
    result = []  # 시작부분에 padding을 넣어준다.
    for i in range(8):  # 딕셔너리에 적은 코드와 같으면 그 값인 숫자로 넣어준다.
        segment = code[i * 7:(i + 1) * 7]
        if segment in d:
            result.append(d[segment])
        else:
            return 0  # 유효하지 않은 코드
    odd_sum, even_sum = 0, 0
    for i in range(8):
        if i % 2 == 0:  # 홀수 인덱스 (1-based)
            odd_sum += result[i]
        else:  # 짝수 인덱스 (1-based)
            even_sum += result[i]

    if (odd_sum * 3 + even_sum) % 10 == 0:  # 계산 후 10으로 나누어 떨어지는지 판별
        return sum(result)
    else:
        return 0

d = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}
hex_c = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    arr = list(set([input().strip().rstrip('0') for _ in range(n)]))  # 오른쪽에 0 제거, set로 중복제거한 후 다시 리스트에 담는다.
    visited = set()  # 중복된 코드가 있는지 확인
    print(f'#{tc} {search_code()}')