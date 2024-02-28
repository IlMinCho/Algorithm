# https://www.acmicpc.net/problem/2960

# 에라토스테네스의 체
# 문제
# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

# 이 알고리즘은 다음과 같다.

# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
# N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)

# 출력
# 첫째 줄에 K번째 지워진 수를 출력한다.

def eratosthenes_sieve(N, K):
    numbers = list(range(2, N + 1))  # 2부터 N까지의 숫자 배열
    removed = []  # 제거된 숫자 저장 배열
    
    while numbers:  # numbers 배열에 아직 숫자가 남아있는 동안
        prime = numbers[0]  # 가장 작은 수를 소수로 선택
        i = 0
        while i < len(numbers):
            if numbers[i] % prime == 0:  # 소수의 배수를 찾으면
                removed.append(numbers[i])  # 제거된 배열에 추가
                numbers.pop(i)  # 해당 숫자 제거
                if len(removed) == K:  # K번째로 제거된 숫자를 찾으면
                    return removed[-1]  # 그 숫자 반환
            else:
                i += 1
                
    return "Not found"  # K번째로 제거된 숫자를 찾지 못했을 경우 (이론상 발생하지 않음)

# 외부 입력 처리
N, K = map(int, input().split())

# 결과 출력
print(eratosthenes_sieve(N, K))